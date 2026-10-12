import Foundation
import Observation
import SwiftData
import TrinkaCore

/// Local, device-only store of the user's progress, preferences and achievements.
///
/// Wraps a SwiftData `ModelContext`, exposes an always-current `snapshot` for the UI and
/// merges sessions coming from the paired device without duplicates.
@MainActor
@Observable
public final class ProgressStore {
    public private(set) var snapshot: ProgressSnapshot = .empty
    public private(set) var unlocked: [Achievement: Date] = [:]
    /// Achievements unlocked by the most recent `record` call, for celebration UI.
    public private(set) var newlyUnlocked: [Achievement] = []

    /// User preferences. `UserSettings` is itself observable, so views can bind to it directly.
    public let settings: UserSettings

    private let context: ModelContext
    private let aggregator: ProgressAggregator
    @ObservationIgnored private var results: [QuizResult] = []
    private let now: () -> Date

    public init(context: ModelContext, calendar: Calendar = .current, now: @escaping () -> Date = Date.init) {
        self.context = context
        self.aggregator = ProgressAggregator(calendar: calendar)
        self.now = now
        if let existing = try? context.fetch(FetchDescriptor<UserSettings>()).first {
            settings = existing
        } else {
            settings = UserSettings()
            context.insert(settings)
            try? context.save()
        }
        reload()
    }

    // MARK: - Sessions

    /// All finished sessions, oldest first.
    public var allResults: [QuizResult] { results }

    /// Saves a finished session and returns achievements it unlocked.
    @discardableResult
    public func record(_ result: QuizResult) -> [Achievement] {
        insertIfNeeded(result)
        save()
        reload()
        newlyUnlocked = unlockAchievements()
        return newlyUnlocked
    }

    /// Merges sessions from the other device. Returns `true` if anything new was added.
    @discardableResult
    public func importSessions(_ incoming: [QuizResult]) -> Bool {
        let known = Set(results.map(\.id))
        let fresh = incoming.filter { !known.contains($0.id) }
        guard !fresh.isEmpty else { return false }
        fresh.forEach(insertIfNeeded)
        save()
        reload()
        _ = unlockAchievements()
        return true
    }

    public func scoringContext() -> ProgressAggregator.ScoringContext {
        aggregator.scoringContext(results: results, now: now())
    }

    public func recentlySeenKeys() -> Set<String> {
        aggregator.recentlySeenKeys(results: results, now: now())
    }

    /// Sessions finished in the last `days` days (for syncing to the watch).
    public func recentResults(days: Int = 30) -> [QuizResult] {
        let since = now().addingTimeInterval(-Double(days) * 86_400)
        return results.filter { $0.finishedAt >= since }
    }

    public func clearNewlyUnlocked() {
        newlyUnlocked = []
    }

    // MARK: - Articles

    public func markArticleOpened(_ article: ArticleReference) {
        let pmid = article.pmid
        let descriptor = FetchDescriptor<OpenedArticle>(predicate: #Predicate { $0.pmid == pmid })
        if let existing = try? context.fetch(descriptor).first {
            existing.lastOpenedAt = now()
        } else {
            context.insert(OpenedArticle(pmid: pmid, title: article.title, openedAt: now()))
        }
        save()
        reload()
        newlyUnlocked = unlockAchievements()
    }

    // MARK: - Settings

    public func saveSettings() {
        save()
    }

    // MARK: - Maintenance

    /// Deletes all local progress (sessions, opened articles, achievements). Keeps settings.
    public func resetProgress() {
        try? context.delete(model: StoredSession.self)
        try? context.delete(model: OpenedArticle.self)
        try? context.delete(model: UnlockedAchievement.self)
        save()
        reload()
    }

    /// Recomputes the snapshot (e.g. after midnight or when returning to the foreground).
    public func reload() {
        let sessions = (try? context.fetch(FetchDescriptor<StoredSession>(sortBy: [SortDescriptor(\.finishedAt)]))) ?? []
        results = sessions.compactMap(\.result)
        let openedCount = (try? context.fetchCount(FetchDescriptor<OpenedArticle>())) ?? 0
        snapshot = aggregator.snapshot(results: results, openedArticleCount: openedCount, now: now())
        let stored = (try? context.fetch(FetchDescriptor<UnlockedAchievement>())) ?? []
        unlocked = Dictionary(stored.compactMap { item in item.achievement.map { ($0, item.unlockedAt) } },
                              uniquingKeysWith: { first, second in Swift.min(first, second) })
    }

    // MARK: - Private

    private func insertIfNeeded(_ result: QuizResult) {
        let id = result.id
        let descriptor = FetchDescriptor<StoredSession>(predicate: #Predicate { $0.id == id })
        guard ((try? context.fetchCount(descriptor)) ?? 0) == 0,
              let session = try? StoredSession(result: result) else { return }
        context.insert(session)
    }

    private func unlockAchievements() -> [Achievement] {
        let earned = Achievement.unlocked(in: snapshot).subtracting(unlocked.keys)
        guard !earned.isEmpty else { return [] }
        let date = now()
        for achievement in earned {
            context.insert(UnlockedAchievement(achievement: achievement, unlockedAt: date))
            unlocked[achievement] = date
        }
        save()
        return Achievement.allCases.filter(earned.contains)
    }

    private func save() {
        do {
            try context.save()
        } catch {
            assertionFailure("TRINKA: failed to save progress: \(error)")
        }
    }
}
