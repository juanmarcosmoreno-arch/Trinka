import Foundation
import TrinkaCore

/// Small on-disk cache of PubMed results so Discover keeps working offline.
///
/// Stores the latest result list per query key as JSON in the Caches directory.
public actor ArticleCache {
    public struct Entry: Codable, Sendable {
        public var fetchedAt: Date
        public var articles: [ArticleReference]
    }

    private let directory: URL
    private let fileManager = FileManager.default

    public init(directory: URL? = nil) {
        let base = directory
            ?? FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask).first
            ?? FileManager.default.temporaryDirectory
        self.directory = base.appendingPathComponent("PubMedCache", isDirectory: true)
    }

    public func store(_ articles: [ArticleReference], for key: String, at date: Date = Date()) throws {
        try fileManager.createDirectory(at: directory, withIntermediateDirectories: true)
        let data = try JSONEncoder().encode(Entry(fetchedAt: date, articles: articles))
        try data.write(to: fileURL(for: key), options: .atomic)
    }

    public func entry(for key: String) -> Entry? {
        guard let data = try? Data(contentsOf: fileURL(for: key)) else { return nil }
        return try? JSONDecoder().decode(Entry.self, from: data)
    }

    public func clear() throws {
        if fileManager.fileExists(atPath: directory.path) {
            try fileManager.removeItem(at: directory)
        }
    }

    private func fileURL(for key: String) -> URL {
        let safe = key.unicodeScalars.map { CharacterSet.alphanumerics.contains($0) ? String($0) : "_" }.joined()
        return directory.appendingPathComponent(String(safe.prefix(120)) + ".json")
    }
}

public extension PubMedQuery {
    /// Stable key for caching this query's results.
    var cacheKey: String {
        [
            category?.rawValue ?? "all",
            topic ?? "",
            keywords.joined(separator: "+"),
            publishedAfter.map(PubMedQuery.entrezDate) ?? "",
            publishedBefore.map(PubMedQuery.entrezDate) ?? "",
            publicationTypes.map(\.rawValue).sorted().joined(separator: "+"),
            sort.rawValue,
        ].joined(separator: "|")
    }
}
