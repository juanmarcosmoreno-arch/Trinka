import Foundation

/// Builds `ProgressSnapshot`s from raw session history. Pure and storage-agnostic.
public struct ProgressAggregator: Sendable {
    public var calendar: Calendar
    /// Days of history included in `ProgressSnapshot.history`.
    public var historyDays: Int

    public init(calendar: Calendar = .current, historyDays: Int = 14) {
        self.calendar = calendar
        self.historyDays = historyDays
    }

    public func snapshot(results: [QuizResult], openedArticleCount: Int, now: Date = Date()) -> ProgressSnapshot {
        var snapshot = ProgressSnapshot()
        let today = calendar.startOfDay(for: now)
        let streaks = StreakCalculator(calendar: calendar)
        let activityDates = results.map(\.finishedAt)

        snapshot.sessionsCompleted = results.count
        snapshot.currentStreak = streaks.currentStreak(activityDates: activityDates, now: now)
        snapshot.longestStreak = streaks.longestStreak(activityDates: activityDates)
        snapshot.openedArticleCount = openedArticleCount

        var perDay: [Date: DailyPerformance] = [:]
        for result in results {
            snapshot.totalXP += result.xp.total
            snapshot.totalAnswered += result.totalCount
            snapshot.totalCorrect += result.correctCount
            for answer in result.answers {
                snapshot.answeredByCategory[answer.category, default: 0] += 1
                if answer.isCorrect { snapshot.correctByCategory[answer.category, default: 0] += 1 }
            }

            let day = calendar.startOfDay(for: result.finishedAt)
            var performance = perDay[day] ?? DailyPerformance(day: day, answered: 0, correct: 0, xp: 0)
            performance.answered += result.totalCount
            performance.correct += result.correctCount
            performance.xp += result.xp.total
            perDay[day] = performance

            if day == today {
                snapshot.todayXP += result.xp.total
                if result.kind == .daily, !snapshot.todayDailyCompleted {
                    snapshot.todayDailyCompleted = true
                    snapshot.todayDailyAnswered = result.totalCount
                    snapshot.todayDailyCorrect = result.correctCount
                }
            }
        }

        snapshot.history = (0..<historyDays).reversed().compactMap { offset in
            guard let day = calendar.date(byAdding: .day, value: -offset, to: today) else { return nil }
            return perDay[day] ?? DailyPerformance(day: day, answered: 0, correct: 0, xp: 0)
        }
        return snapshot
    }

    /// Inputs needed to score a session that is about to be saved.
    public struct ScoringContext: Sendable {
        /// Streak including today once the new session is counted.
        public var streakIncludingToday: Int
        public var isFirstSessionToday: Bool
        public var previouslyPlayedCategories: Set<ScienceCategory>
    }

    public func scoringContext(results: [QuizResult], now: Date = Date()) -> ScoringContext {
        let streaks = StreakCalculator(calendar: calendar)
        let dates = results.map(\.finishedAt) + [now]
        return ScoringContext(
            streakIncludingToday: streaks.currentStreak(activityDates: dates, now: now),
            isFirstSessionToday: !results.contains { calendar.isDate($0.finishedAt, inSameDayAs: now) },
            previouslyPlayedCategories: Set(results.flatMap(\.answers).map(\.category))
        )
    }

    /// Translation keys answered in the last `days` days, to avoid immediate repeats.
    public func recentlySeenKeys(results: [QuizResult], days: Int = 2, now: Date = Date()) -> Set<String> {
        guard let since = calendar.date(byAdding: .day, value: -days, to: calendar.startOfDay(for: now)) else { return [] }
        return Set(results.filter { $0.finishedAt >= since }.flatMap(\.answers).map(\.translationKey))
    }
}
