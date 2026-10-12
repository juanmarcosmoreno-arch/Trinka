import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
import TrinkaCore

public enum PubMedError: Error, Equatable, Sendable {
    case offline
    case httpStatus(Int)
    case invalidResponse
    case parsing(String)
    case rateLimited
}

/// Abstraction over the HTTP layer so the client can be tested without the network.
public protocol HTTPDataLoading: Sendable {
    func data(from url: URL) async throws -> (Data, URLResponse)
}

/// Default loader backed by `URLSession`.
public struct URLSessionLoader: HTTPDataLoading {
    public let session: URLSession

    public init(session: URLSession = .shared) {
        self.session = session
    }

    public func data(from url: URL) async throws -> (Data, URLResponse) {
        try await session.data(from: url)
    }
}

/// Client for NCBI E-utilities (https://www.ncbi.nlm.nih.gov/books/NBK25501/).
///
/// - `esearch` finds PMIDs for a query.
/// - `efetch` (XML) retrieves full metadata, including abstracts and DOIs.
///
/// NCBI asks clients to identify themselves (`tool`, `email`) and to stay under
/// 3 requests/second without an API key (10 with one); `RequestThrottle` enforces that.
public struct PubMedClient: Sendable {
    public struct Configuration: Sendable {
        public var baseURL: URL
        /// Registered tool name sent with every request.
        public var tool: String
        /// Developer contact e-mail, as requested by NCBI's usage policy.
        public var email: String?
        /// Optional NCBI API key. Not a secret credential, but keep it out of source control.
        public var apiKey: String?

        public init(
            baseURL: URL = URL(string: "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/")!,
            tool: String = "trinka",
            email: String? = nil,
            apiKey: String? = nil
        ) {
            self.baseURL = baseURL
            self.tool = tool
            self.email = email
            self.apiKey = apiKey
        }

        var minimumInterval: TimeInterval { apiKey == nil ? 0.34 : 0.11 }
    }

    public let configuration: Configuration
    private let loader: HTTPDataLoading
    private let throttle: RequestThrottle

    public init(configuration: Configuration = Configuration(), loader: HTTPDataLoading = URLSessionLoader()) {
        self.configuration = configuration
        self.loader = loader
        self.throttle = RequestThrottle(minimumInterval: configuration.minimumInterval)
    }

    /// Searches PubMed and returns full article metadata.
    public func searchArticles(_ query: PubMedQuery) async throws -> [ArticleReference] {
        let pmids = try await search(query)
        guard !pmids.isEmpty else { return [] }
        let articles = try await fetchArticles(pmids: pmids)
        // Keep esearch's ranking.
        let order = Dictionary(uniqueKeysWithValues: pmids.enumerated().map { ($1, $0) })
        return articles.sorted { (order[$0.pmid] ?? .max) < (order[$1.pmid] ?? .max) }
    }

    /// Returns PMIDs matching `query`.
    public func search(_ query: PubMedQuery) async throws -> [String] {
        var items = [
            URLQueryItem(name: "db", value: "pubmed"),
            URLQueryItem(name: "retmode", value: "json"),
            URLQueryItem(name: "retmax", value: String(max(1, min(query.maxResults, 100)))),
            URLQueryItem(name: "sort", value: query.sort.rawValue),
            URLQueryItem(name: "term", value: query.term),
        ]
        if query.publishedAfter != nil || query.publishedBefore != nil {
            items.append(URLQueryItem(name: "datetype", value: "pdat"))
            items.append(URLQueryItem(name: "mindate", value: PubMedQuery.entrezDate(query.publishedAfter ?? Date(timeIntervalSince1970: -2_208_988_800))))
            items.append(URLQueryItem(name: "maxdate", value: PubMedQuery.entrezDate(query.publishedBefore ?? Date())))
        }
        let data = try await get("esearch.fcgi", items)
        return try ESearchResponse.pmids(from: data)
    }

    /// Fetches full records (title, authors, journal, year, DOI, abstract, publication types).
    public func fetchArticles(pmids: [String]) async throws -> [ArticleReference] {
        let valid = pmids.filter(QuestionValidator.isValidPMID)
        guard !valid.isEmpty else { return [] }
        var results: [ArticleReference] = []
        // efetch accepts long ID lists, but small batches keep responses light on cellular.
        for batch in stride(from: 0, to: valid.count, by: 50).map({ Array(valid[$0..<min($0 + 50, valid.count)]) }) {
            let data = try await get("efetch.fcgi", [
                URLQueryItem(name: "db", value: "pubmed"),
                URLQueryItem(name: "retmode", value: "xml"),
                URLQueryItem(name: "id", value: batch.joined(separator: ",")),
            ])
            results += try PubMedXMLParser.parse(data)
        }
        return results
    }

    /// Convenience for a single article.
    public func fetchArticle(pmid: String) async throws -> ArticleReference? {
        try await fetchArticles(pmids: [pmid]).first
    }

    // MARK: - Transport

    func url(_ endpoint: String, _ items: [URLQueryItem]) -> URL {
        var components = URLComponents(url: configuration.baseURL.appendingPathComponent(endpoint), resolvingAgainstBaseURL: false)!
        var all = items
        all.append(URLQueryItem(name: "tool", value: configuration.tool))
        if let email = configuration.email { all.append(URLQueryItem(name: "email", value: email)) }
        if let apiKey = configuration.apiKey { all.append(URLQueryItem(name: "api_key", value: apiKey)) }
        components.queryItems = all
        // `+` is legal in queries but Entrez reads it as a space; encode it explicitly.
        components.percentEncodedQuery = components.percentEncodedQuery?.replacingOccurrences(of: "+", with: "%2B")
        return components.url!
    }

    private func get(_ endpoint: String, _ items: [URLQueryItem]) async throws -> Data {
        await throttle.wait()
        let data: Data
        let response: URLResponse
        do {
            (data, response) = try await loader.data(from: url(endpoint, items))
        } catch let error as URLError where [.notConnectedToInternet, .networkConnectionLost, .dataNotAllowed, .timedOut].contains(error.code) {
            throw PubMedError.offline
        }
        guard let http = response as? HTTPURLResponse else { throw PubMedError.invalidResponse }
        switch http.statusCode {
        case 200: return data
        case 429: throw PubMedError.rateLimited
        default: throw PubMedError.httpStatus(http.statusCode)
        }
    }
}

/// Spaces requests to respect NCBI's rate limits.
actor RequestThrottle {
    private let minimumInterval: TimeInterval
    private var nextAllowed = Date.distantPast

    init(minimumInterval: TimeInterval) {
        self.minimumInterval = minimumInterval
    }

    func wait() async {
        let now = Date()
        let start = max(now, nextAllowed)
        nextAllowed = start.addingTimeInterval(minimumInterval)
        let delay = start.timeIntervalSince(now)
        if delay > 0 {
            try? await Task.sleep(nanoseconds: UInt64(delay * 1_000_000_000))
        }
    }
}

/// Decodes the JSON `esearch` response.
enum ESearchResponse {
    private struct Envelope: Decodable {
        struct Result: Decodable {
            var idlist: [String]
        }

        var esearchresult: Result
    }

    static func pmids(from data: Data) throws -> [String] {
        do {
            return try JSONDecoder().decode(Envelope.self, from: data).esearchresult.idlist
        } catch {
            throw PubMedError.parsing("esearch: \(error)")
        }
    }
}
