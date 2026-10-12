import Foundation
import TrinkaCore

/// PubMed publication types TRINKA lets users filter by (`[pt]` field).
public enum PublicationType: String, CaseIterable, Codable, Hashable, Identifiable, Sendable {
    case journalArticle = "Journal Article"
    case review = "Review"
    case systematicReview = "Systematic Review"
    case metaAnalysis = "Meta-Analysis"
    case randomizedControlledTrial = "Randomized Controlled Trial"
    case clinicalTrial = "Clinical Trial"

    public var id: String { rawValue }
    public var localizationKey: String { "publicationType.\(String(describing: self))" }
}

/// A PubMed search, built from TRINKA's filters.
public struct PubMedQuery: Hashable, Sendable {
    public enum Sort: String, Sendable {
        case relevance
        case publicationDate = "pub_date"
    }

    public var category: ScienceCategory?
    /// Free-text research topic, e.g. "gut microbiota".
    public var topic: String?
    /// Additional keywords, all required.
    public var keywords: [String]
    /// Inclusive publication-date range.
    public var publishedAfter: Date?
    public var publishedBefore: Date?
    /// Any of these types (OR).
    public var publicationTypes: Set<PublicationType>
    /// Only articles that have an abstract (needed for summaries and question verification).
    public var requireAbstract: Bool
    public var sort: Sort
    public var maxResults: Int

    public init(
        category: ScienceCategory? = nil,
        topic: String? = nil,
        keywords: [String] = [],
        publishedAfter: Date? = nil,
        publishedBefore: Date? = nil,
        publicationTypes: Set<PublicationType> = [],
        requireAbstract: Bool = true,
        sort: Sort = .relevance,
        maxResults: Int = 20
    ) {
        self.category = category
        self.topic = topic
        self.keywords = keywords
        self.publishedAfter = publishedAfter
        self.publishedBefore = publishedBefore
        self.publicationTypes = publicationTypes
        self.requireAbstract = requireAbstract
        self.sort = sort
        self.maxResults = maxResults
    }

    /// The Entrez `term` expression.
    public var term: String {
        var clauses: [String] = []
        if let category { clauses.append("(\(category.pubMedQuery))") }
        if let topic = topic?.trimmingCharacters(in: .whitespacesAndNewlines), !topic.isEmpty {
            clauses.append("(\(Self.sanitize(topic)))")
        }
        for keyword in keywords {
            let cleaned = Self.sanitize(keyword)
            if !cleaned.isEmpty { clauses.append("\"\(cleaned)\"[Title/Abstract]") }
        }
        if !publicationTypes.isEmpty {
            let types = publicationTypes.map(\.rawValue).sorted().map { "\"\($0)\"[pt]" }
            clauses.append("(" + types.joined(separator: " OR ") + ")")
        }
        if requireAbstract { clauses.append("hasabstract") }
        // Exclude retracted publications from discovery.
        clauses.append("NOT \"Retracted Publication\"[pt]")
        if clauses.count == 2, requireAbstract {
            // Only the default filters: PubMed needs something to search for.
            clauses.insert("science[Title/Abstract]", at: 0)
        }
        return clauses.joined(separator: " AND ").replacingOccurrences(of: " AND NOT ", with: " NOT ")
    }

    /// Strips characters with special meaning in Entrez syntax.
    static func sanitize(_ text: String) -> String {
        let forbidden = CharacterSet(charactersIn: "\"[]()")
        return text.components(separatedBy: forbidden).joined(separator: " ")
            .components(separatedBy: .whitespacesAndNewlines).filter { !$0.isEmpty }.joined(separator: " ")
    }

    /// `yyyy/MM/dd` as expected by `mindate` / `maxdate`.
    static func entrezDate(_ date: Date) -> String {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "UTC")!
        let c = calendar.dateComponents([.year, .month, .day], from: date)
        return String(format: "%04d/%02d/%02d", c.year ?? 0, c.month ?? 1, c.day ?? 1)
    }
}
