import Foundation

/// The user's answer to a single question.
public struct AnswerRecord: Codable, Hashable, Identifiable, Sendable {
    public var id: String { questionID }
    public var questionID: String
    public var translationKey: String
    public var pmid: String
    public var category: ScienceCategory
    public var difficulty: Difficulty
    /// `nil` when the timer ran out before answering.
    public var selectedOptionIndex: Int?
    public var isCorrect: Bool
    public var answeredAt: Date
    public var responseTime: TimeInterval

    public init(
        question: Question,
        selectedOptionIndex: Int?,
        answeredAt: Date,
        responseTime: TimeInterval
    ) {
        self.questionID = question.id
        self.translationKey = question.translationKey
        self.pmid = question.source.pmid
        self.category = question.category
        self.difficulty = question.difficulty
        self.selectedOptionIndex = selectedOptionIndex
        self.isCorrect = selectedOptionIndex.map(question.isCorrect) ?? false
        self.answeredAt = answeredAt
        self.responseTime = max(0, responseTime)
    }

    public var timedOut: Bool { selectedOptionIndex == nil }
}

/// Where a quiz session was played.
public enum DeviceOrigin: String, Codable, Hashable, Sendable {
    case iPhone
    case watch
}

/// Kind of quiz session.
public enum SessionKind: String, Codable, Hashable, Sendable {
    /// The daily challenge (one per day counts toward the daily score).
    case daily
    /// A custom quiz from Explore.
    case explore
    /// The Apple Watch Quick Quiz.
    case quick
    /// A friend challenge started from a shared code.
    case challenge
}

/// Summary of a finished quiz, shared between devices and stored locally.
public struct QuizResult: Codable, Hashable, Identifiable, Sendable {
    public var id: UUID
    public var kind: SessionKind
    public var origin: DeviceOrigin
    public var language: AppLanguage
    public var startedAt: Date
    public var finishedAt: Date
    public var answers: [AnswerRecord]
    public var xp: XPBreakdown

    public init(
        id: UUID = UUID(),
        kind: SessionKind,
        origin: DeviceOrigin,
        language: AppLanguage,
        startedAt: Date,
        finishedAt: Date,
        answers: [AnswerRecord],
        xp: XPBreakdown
    ) {
        self.id = id
        self.kind = kind
        self.origin = origin
        self.language = language
        self.startedAt = startedAt
        self.finishedAt = finishedAt
        self.answers = answers
        self.xp = xp
    }

    public var correctCount: Int { answers.filter(\.isCorrect).count }
    public var totalCount: Int { answers.count }

    /// 0...1
    public var accuracy: Double {
        totalCount == 0 ? 0 : Double(correctCount) / Double(totalCount)
    }

    public var duration: TimeInterval { max(0, finishedAt.timeIntervalSince(startedAt)) }

    public var categories: Set<ScienceCategory> { Set(answers.map(\.category)) }
}
