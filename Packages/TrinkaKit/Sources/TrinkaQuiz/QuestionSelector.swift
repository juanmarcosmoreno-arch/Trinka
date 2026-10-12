import Foundation
import TrinkaCore

/// Picks questions for daily challenges and custom quizzes.
public struct QuestionSelector: Sendable {
    public static let dailyChallengeSize = 5

    public var calendar: Calendar

    public init(calendar: Calendar = .current) {
        self.calendar = calendar
    }

    /// The daily challenge for `date`.
    ///
    /// Deterministic: the same day and language always yield the same questions, so iPhone
    /// and Apple Watch build identical challenges even when offline. Questions come from
    /// as many different categories as possible and are ordered from easiest to hardest.
    public func dailyChallenge(
        from bank: QuestionBank,
        language: AppLanguage,
        date: Date,
        count: Int = QuestionSelector.dailyChallengeSize
    ) -> [Question] {
        var generator = SeededGenerator(seed: daySeed(for: date, salt: language.rawValue))
        let pool = bank.questions(in: language).sorted { $0.id < $1.id }.shuffled(using: &generator)
        return Self.spreadAcrossCategories(pool, count: count).sorted { $0.difficulty < $1.difficulty }
    }

    /// A custom quiz for Explore.
    ///
    /// - Parameters:
    ///   - category: `nil` for all categories.
    ///   - difficulty: `nil` for all difficulties.
    ///   - recentlySeen: translation keys to de-prioritize (shown last if the pool is small).
    public func customQuiz<G: RandomNumberGenerator>(
        from bank: QuestionBank,
        language: AppLanguage,
        category: ScienceCategory?,
        difficulty: Difficulty?,
        count: Int,
        recentlySeen: Set<String> = [],
        using generator: inout G
    ) -> [Question] {
        let pool = bank.questions(in: language, category: category, difficulty: difficulty)
            .sorted { $0.id < $1.id }
            .shuffled(using: &generator)
        let fresh = pool.filter { !recentlySeen.contains($0.translationKey) }
        let seen = pool.filter { recentlySeen.contains($0.translationKey) }
        let ordered = fresh + seen
        return category == nil
            ? Self.spreadAcrossCategories(ordered, count: count)
            : Array(ordered.prefix(count))
    }

    public func customQuiz(
        from bank: QuestionBank,
        language: AppLanguage,
        category: ScienceCategory?,
        difficulty: Difficulty?,
        count: Int,
        recentlySeen: Set<String> = []
    ) -> [Question] {
        var generator = SystemRandomNumberGenerator()
        return customQuiz(
            from: bank, language: language, category: category, difficulty: difficulty,
            count: count, recentlySeen: recentlySeen, using: &generator
        )
    }

    /// Round-robin over categories (keeping the input order within each category) so a
    /// short quiz touches as many disciplines as possible.
    static func spreadAcrossCategories(_ questions: [Question], count: Int) -> [Question] {
        guard count > 0 else { return [] }
        var buckets: [ScienceCategory: [Question]] = [:]
        var categoryOrder: [ScienceCategory] = []
        for question in questions {
            if buckets[question.category] == nil { categoryOrder.append(question.category) }
            buckets[question.category, default: []].append(question)
        }
        var result: [Question] = []
        var round = 0
        while result.count < count {
            var addedThisRound = false
            for category in categoryOrder {
                guard let bucket = buckets[category], round < bucket.count else { continue }
                result.append(bucket[round])
                addedThisRound = true
                if result.count == count { break }
            }
            if !addedThisRound { break }
            round += 1
        }
        return result
    }

    /// Stable seed for a calendar day (independent of time of day).
    func daySeed(for date: Date, salt: String) -> UInt64 {
        let components = calendar.dateComponents([.year, .month, .day], from: date)
        let year = components.year ?? 0
        let month = components.month ?? 0
        let day = components.day ?? 0
        let dayNumber = UInt64(year * 10_000 + month * 100 + day)
        // FNV-1a over the salt keeps languages independent but stable across launches
        // (unlike `Hasher`, which is randomly seeded per process).
        var hash: UInt64 = 0xcbf2_9ce4_8422_2325
        for byte in salt.utf8 {
            hash ^= UInt64(byte)
            hash = hash &* 0x0000_0100_0000_01b3
        }
        return dayNumber ^ hash
    }
}

/// SplitMix64: small, fast, deterministic random generator.
public struct SeededGenerator: RandomNumberGenerator, Sendable {
    private var state: UInt64

    public init(seed: UInt64) {
        state = seed
    }

    public mutating func next() -> UInt64 {
        state &+= 0x9e37_79b9_7f4a_7c15
        var z = state
        z = (z ^ (z >> 30)) &* 0xbf58_476d_1ce4_e5b9
        z = (z ^ (z >> 27)) &* 0x94d0_49bb_1331_11eb
        return z ^ (z >> 31)
    }
}
