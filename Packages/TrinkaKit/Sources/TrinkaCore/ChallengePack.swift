import Foundation

/// A self-contained set of questions that can be played offline (e.g. on Apple Watch).
public struct ChallengePack: Codable, Hashable, Identifiable, Sendable {
    public var id: String
    /// Calendar day the pack is meant for (start of day in the sender's time zone).
    public var day: Date
    public var language: AppLanguage
    /// Level the challenge was built for (`nil` = all levels).
    public var level: Difficulty?
    public var questions: [Question]
    public var createdAt: Date

    public init(id: String, day: Date, language: AppLanguage, level: Difficulty? = nil, questions: [Question], createdAt: Date = Date()) {
        self.id = id
        self.day = day
        self.language = language
        self.level = level
        // Only verified questions may travel to another device.
        self.questions = questions.filter(QuestionValidator.isPlayable)
        self.createdAt = createdAt
    }

    public func isValid(for date: Date, calendar: Calendar = .current) -> Bool {
        calendar.isDate(day, inSameDayAs: date) && !questions.isEmpty
    }
}

/// Messages exchanged between iPhone and Apple Watch.
public enum SyncMessage: Codable, Hashable, Sendable {
    /// iPhone → Watch: today's challenge and an up-to-date copy of the session history.
    case state(ChallengePack?, sessions: [QuizResult])
    /// Either direction: a newly finished session.
    case session(QuizResult)

    // Default (numeric) date coding keeps sub-second precision, so round trips are lossless.
    public func encoded() throws -> Data {
        try JSONEncoder().encode(self)
    }

    public static func decode(_ data: Data) throws -> SyncMessage {
        try JSONDecoder().decode(SyncMessage.self, from: data)
    }
}
