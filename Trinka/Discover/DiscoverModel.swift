import Foundation
import Observation
import TrinkaCore
import TrinkaPubMed

/// Loads research for Discover (and Explore's "recent research"), with offline fallbacks.
@MainActor
@Observable
final class DiscoverModel {
    enum Recency: String, CaseIterable, Identifiable {
        case any, lastYear, last5Years
        var id: String { rawValue }

        var startDate: Date? {
            switch self {
            case .any: nil
            case .lastYear: Calendar.current.date(byAdding: .year, value: -1, to: Date())
            case .last5Years: Calendar.current.date(byAdding: .year, value: -5, to: Date())
            }
        }
    }

    enum Source: Equatable {
        /// Fresh results from PubMed.
        case live
        /// Offline: results cached at the given date.
        case cached(Date)
        /// Offline and nothing cached: the articles behind TRINKA's bundled questions.
        case bundled
    }

    enum State: Equatable {
        case idle
        case loading
        case loaded([ArticleReference], Source)
        case failed
    }

    var category: ScienceCategory?
    var topic = ""
    var recency: Recency = .any
    var publicationTypes: Set<PublicationType> = []
    var sortByDate = false
    private(set) var state: State = .idle

    @ObservationIgnored private var task: Task<Void, Never>?

    init(category: ScienceCategory? = nil, recency: Recency = .any, sortByDate: Bool = false) {
        self.category = category
        self.recency = recency
        self.sortByDate = sortByDate
    }

    var query: PubMedQuery {
        PubMedQuery(
            category: category,
            topic: topic.isEmpty ? nil : topic,
            publishedAfter: recency.startDate,
            publicationTypes: publicationTypes,
            sort: sortByDate ? .publicationDate : .relevance,
            maxResults: 20
        )
    }

    /// Starts (or restarts) a search.
    func reload(using client: PubMedClient, cache: ArticleCache, fallback: [ArticleReference], limit: Int? = nil) {
        task?.cancel()
        state = .loading
        let query = query
        task = Task {
            let state = await Self.fetch(query: query, client: client, cache: cache, fallback: fallback, limit: limit)
            guard !Task.isCancelled else { return }
            self.state = state
        }
    }

    private static func fetch(query: PubMedQuery, client: PubMedClient, cache: ArticleCache,
                              fallback: [ArticleReference], limit: Int?) async -> State {
        func trimmed(_ articles: [ArticleReference]) -> [ArticleReference] {
            limit.map { Array(articles.prefix($0)) } ?? articles
        }
        do {
            let articles = try await client.searchArticles(query)
            try? await cache.store(articles, for: query.cacheKey)
            return .loaded(trimmed(articles), .live)
        } catch {
            if let entry = await cache.entry(for: query.cacheKey), !entry.articles.isEmpty {
                return .loaded(trimmed(entry.articles), .cached(entry.fetchedAt))
            }
            if !fallback.isEmpty {
                return .loaded(trimmed(fallback), .bundled)
            }
            return .failed
        }
    }
}
