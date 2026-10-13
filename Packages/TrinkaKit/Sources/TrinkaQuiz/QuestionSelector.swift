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
    /// Deterministic: the same day, language and level always yield the same questions, so
    /// iPhone and Apple Watch build identical challenges even when offline. Questions come from
    /// as many different categories as possible and are ordered from easiest to hardest.
    ///
    /// - Parameter level: the player's chosen level. Questions at that level come first; if
    ///   there aren't enough, the nearest levels fill in (one step easier before one step
    ///   harder). `nil` mixes all levels.
    public func dailyChallenge(
        from bank: QuestionBank,
        language: AppLanguage,
        date: Date,
        level: Difficulty? = nil,
        count: Int = QuestionSelector.dailyChallengeSize
    ) -> [Question] {
        var generator = SeededGenerator(seed: daySeed(for: date, salt: language.rawValue + (level?.rawValue ?? "")))
        let pool = bank.questions(in: language).sorted { $0.id < $1.id }.shuffled(using: &generator)
        let ordered = level.map { Self.orderedByCloseness(pool, to: $0) } ?? pool
        return Self.spreadAcrossCategories(ordered, count: count).sorted { $0.difficulty < $1.difficulty }
    }

    /// Stable ordering by distance from `level`: same level first, then one step easier,
    /// one step harder, and so on. Keeps the input order within each group.
    static func orderedByCloseness(_ questions: [Question], to level: Difficulty) -> [Question] {
        func rank(_ question: Question) -> Int {
            let distance = question.difficulty.level - level.level
            if distance == 0 { return 0 }
            return distance < 0 ? -distance * 2 - 1 : distance * 2 // easier: 1, 3…; harder: 2, 4…
        }
        return questions.enumerated()
            .sorted { lhs, rhs in
                let (l, r) = (rank(lhs.element), rank(rhs.element))
                return l == r ? lhs.offset < rhs.offset : l < r
            }
            .map(\.element)
    }

    /// A custom quiz for Explore.
    ///
    /// - Parameters:
    ///   - category: `nil` for all categories.
    ///   - difficulty: `nil` for all difficulties.
    ///   - recentlySeen: translation keys to de-prioritize (shown last if the pool is small).
    ///   - fillWithNearestLevels: when there aren't enough questions at exactly `difficulty`,
    ///     complete the quiz with the closest levels instead of returning fewer questions.
    public func customQuiz<G: RandomNumberGenerator>(
        from bank: QuestionBank,
        language: AppLanguage,
        category: ScienceCategory?,
        difficulty: Difficulty?,
        count: Int,
        recentlySeen: Set<String> = [],
        fillWithNearestLevels: Bool = false,
        using generator: inout G
    ) -> [Question] {
        let useNearest = fillWithNearestLevels && difficulty != nil
        let shuffled = bank.questions(in: language, category: category, difficulty: useNearest ? nil : difficulty)
            .sorted { $0.id < $1.id }
            .shuffled(using: &generator)
        let fresh = shuffled.filter { !recentlySeen.contains($0.translationKey) }
        let seen = shuffled.filter { recentlySeen.contains($0.translationKey) }
        var ordered = fresh + seen
        if useNearest, let difficulty {
            // Closeness first; unseen before seen within the same level.
            ordered = Self.orderedByCloseness(ordered, to: difficulty)
        }
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
        recentlySeen: Set<String> = [],
        fillWithNearestLevels: Bool = false
    ) -> [Question] {
        var generator = SystemRandomNumberGenerator()
        return customQuiz(
            from: bank, language: language, category: category, difficulty: difficulty,
            count: count, recentlySeen: recentlySeen, fillWithNearestLevels: fillWithNearestLevels,
            using: &generator
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
