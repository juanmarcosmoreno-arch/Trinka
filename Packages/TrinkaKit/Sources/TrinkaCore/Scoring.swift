import Foundation

/// Experience points earned in one session, itemized so the UI can explain them.
public struct XPBreakdown: Codable, Hashable, Sendable {
    public var correctAnswers: Int
    public var completion: Int
    public var perfectRun: Int
    public var streak: Int
    public var newCategories: Int

    public init(correctAnswers: Int = 0, completion: Int = 0, perfectRun: Int = 0, streak: Int = 0, newCategories: Int = 0) {
        self.correctAnswers = correctAnswers
        self.completion = completion
        self.perfectRun = perfectRun
        self.streak = streak
        self.newCategories = newCategories
    }

    public var total: Int { correctAnswers + completion + perfectRun + streak + newCategories }
}

/// TRINKA's XP rules.
///
/// Points reward learning — correct answers, finishing challenges, coming back daily and
/// exploring new disciplines — not speed. Response time never changes the score.
public struct ScoringRules: Sendable {
    public var pointsPerCorrectAnswer: Int = 10
    public var completionBonus: Int = 20
    public var perfectRunBonus: Int = 15
    public var streakBonusPerDay: Int = 5
    public var maxStreakBonus: Int = 50
    public var newCategoryBonus: Int = 25

    public static let standard = ScoringRules()

    public init() {}

    /// Points for one correct answer: 10 at beginner, +5 per level (up to 30 at expert).
    public func points(for difficulty: Difficulty) -> Int {
        pointsPerCorrectAnswer + (difficulty.level - 1) * pointsPerCorrectAnswer / 2
    }

    /// Computes the XP for a finished session.
    ///
    /// - Parameters:
    ///   - answers: answers given in the session.
    ///   - completed: whether every question was answered (or timed out) — abandoned sessions get no bonus.
    ///   - currentStreak: consecutive active days including today, after this session.
    ///   - isFirstSessionToday: streak XP is granted once per day.
    ///   - previouslyPlayedCategories: categories the user had already played before this session.
    public func xp(
        for answers: [AnswerRecord],
        completed: Bool,
        currentStreak: Int,
        isFirstSessionToday: Bool,
        previouslyPlayedCategories: Set<ScienceCategory>
    ) -> XPBreakdown {
        var breakdown = XPBreakdown()
        breakdown.correctAnswers = answers.filter(\.isCorrect).map { points(for: $0.difficulty) }.reduce(0, +)

        guard completed, !answers.isEmpty else { return breakdown }

        breakdown.completion = completionBonus
        if answers.allSatisfy(\.isCorrect) { breakdown.perfectRun = perfectRunBonus }
        if isFirstSessionToday, currentStreak > 1 {
            breakdown.streak = min(maxStreakBonus, (currentStreak - 1) * streakBonusPerDay)
        }
        let newCategories = Set(answers.map(\.category)).subtracting(previouslyPlayedCategories)
        breakdown.newCategories = newCategories.count * newCategoryBonus
        return breakdown
    }
}
