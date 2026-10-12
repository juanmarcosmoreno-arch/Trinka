import Foundation

/// Daily-streak computation from a set of activity dates.
public struct StreakCalculator: Sendable {
    public var calendar: Calendar

    public init(calendar: Calendar = .current) {
        self.calendar = calendar
    }

    /// Consecutive active days ending today — or ending yesterday, so the streak
    /// isn't shown as lost before the user has had a chance to play today.
    public func currentStreak(activityDates: [Date], now: Date = Date()) -> Int {
        let days = Set(activityDates.map { calendar.startOfDay(for: $0) })
        let today = calendar.startOfDay(for: now)
        guard let yesterday = calendar.date(byAdding: .day, value: -1, to: today) else { return 0 }

        var cursor: Date
        if days.contains(today) {
            cursor = today
        } else if days.contains(yesterday) {
            cursor = yesterday
        } else {
            return 0
        }

        var streak = 0
        while days.contains(cursor) {
            streak += 1
            guard let previous = calendar.date(byAdding: .day, value: -1, to: cursor) else { break }
            cursor = previous
        }
        return streak
    }

    /// Longest run of consecutive active days ever.
    public func longestStreak(activityDates: [Date]) -> Int {
        let days = Set(activityDates.map { calendar.startOfDay(for: $0) }).sorted()
        var longest = 0
        var run = 0
        var previous: Date?
        for day in days {
            if let previous, let expected = calendar.date(byAdding: .day, value: 1, to: previous),
               calendar.isDate(day, inSameDayAs: expected) {
                run += 1
            } else {
                run = 1
            }
            longest = max(longest, run)
            previous = day
        }
        return longest
    }
}
