import Foundation

/// Activity of one calendar day, used for the performance chart.
public struct DailyPerformance: Codable, Hashable, Identifiable, Sendable {
    public var day: Date
    public var answered: Int
    public var correct: Int
    public var xp: Int

    public var id: Date { day }

    public init(day: Date, answered: Int, correct: Int, xp: Int) {
        self.day = day
        self.answered = answered
        self.correct = correct
        self.xp = xp
    }

    public var accuracy: Double { answered == 0 ? 0 : Double(correct) / Double(answered) }
}

/// Aggregated, read-only view of the user's learning activity.
///
/// These are quiz activity statistics only. They are not — and must never be presented
/// as — clinical measures of intelligence or cognitive ability.
public struct ProgressSnapshot: Codable, Hashable, Sendable {
    public var totalAnswered: Int
    public var totalCorrect: Int
    public var totalXP: Int
    public var sessionsCompleted: Int
    public var currentStreak: Int
    public var longestStreak: Int
    public var answeredByCategory: [ScienceCategory: Int]
    public var correctByCategory: [ScienceCategory: Int]
    public var openedArticleCount: Int
    public var history: [DailyPerformance]
    public var todayXP: Int
    /// Answers given in today's daily challenge (0...questions in challenge).
    public var todayDailyAnswered: Int
    public var todayDailyCorrect: Int
    public var todayDailyCompleted: Bool

    public init(
        totalAnswered: Int = 0,
        totalCorrect: Int = 0,
        totalXP: Int = 0,
        sessionsCompleted: Int = 0,
        currentStreak: Int = 0,
        longestStreak: Int = 0,
        answeredByCategory: [ScienceCategory: Int] = [:],
        correctByCategory: [ScienceCategory: Int] = [:],
        openedArticleCount: Int = 0,
        history: [DailyPerformance] = [],
        todayXP: Int = 0,
        todayDailyAnswered: Int = 0,
        todayDailyCorrect: Int = 0,
        todayDailyCompleted: Bool = false
    ) {
        self.totalAnswered = totalAnswered
        self.totalCorrect = totalCorrect
        self.totalXP = totalXP
        self.sessionsCompleted = sessionsCompleted
        self.currentStreak = currentStreak
        self.longestStreak = longestStreak
        self.answeredByCategory = answeredByCategory
        self.correctByCategory = correctByCategory
        self.openedArticleCount = openedArticleCount
        self.history = history
        self.todayXP = todayXP
        self.todayDailyAnswered = todayDailyAnswered
        self.todayDailyCorrect = todayDailyCorrect
        self.todayDailyCompleted = todayDailyCompleted
    }

    public static let empty = ProgressSnapshot()

    public var accuracy: Double {
        totalAnswered == 0 ? 0 : Double(totalCorrect) / Double(totalAnswered)
    }

    public var playedCategories: Set<ScienceCategory> {
        Set(answeredByCategory.filter { $0.value > 0 }.keys)
    }

    /// Most-played categories, highest first.
    public func favoriteCategories(limit: Int = 3) -> [ScienceCategory] {
        answeredByCategory
            .filter { $0.value > 0 }
            .sorted { $0.value == $1.value ? $0.key.rawValue < $1.key.rawValue : $0.value > $1.value }
            .prefix(limit)
            .map(\.key)
    }
}

/// Achievements reward curiosity and learning, never speed.
public enum Achievement: String, CaseIterable, Codable, Hashable, Identifiable, Sendable {
    case firstDiscovery
    case curiousMind
    case scienceExplorer
    case sevenDayStreak
    case microbiologyMaster
    case researchEnthusiast

    public var id: String { rawValue }
    public var titleKey: String { "achievement.\(rawValue).title" }
    public var detailKey: String { "achievement.\(rawValue).detail" }

    public var symbolName: String {
        switch self {
        case .firstDiscovery: "lightbulb.max"
        case .curiousMind: "questionmark.bubble"
        case .scienceExplorer: "map"
        case .sevenDayStreak: "flame"
        case .microbiologyMaster: "allergens"
        case .researchEnthusiast: "books.vertical"
        }
    }

    /// Target value for the achievement.
    public var target: Int {
        switch self {
        case .firstDiscovery: 1
        case .curiousMind: 50
        case .scienceExplorer: ScienceCategory.allCases.count
        case .sevenDayStreak: 7
        case .microbiologyMaster: 15
        case .researchEnthusiast: 10
        }
    }

    /// Current value toward `target`.
    public func progress(in snapshot: ProgressSnapshot) -> Int {
        let value: Int = switch self {
        case .firstDiscovery: snapshot.totalCorrect
        case .curiousMind: snapshot.totalAnswered
        case .scienceExplorer: snapshot.playedCategories.count
        case .sevenDayStreak: snapshot.longestStreak
        case .microbiologyMaster: snapshot.correctByCategory[.microbiology] ?? 0
        case .researchEnthusiast: snapshot.openedArticleCount
        }
        return min(value, target)
    }

    public func isUnlocked(in snapshot: ProgressSnapshot) -> Bool {
        progress(in: snapshot) >= target
    }

    public static func unlocked(in snapshot: ProgressSnapshot) -> Set<Achievement> {
        Set(allCases.filter { $0.isUnlocked(in: snapshot) })
    }
}
