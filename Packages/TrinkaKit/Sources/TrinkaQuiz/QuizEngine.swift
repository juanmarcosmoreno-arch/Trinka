import Foundation
import TrinkaCore

/// State machine for one quiz session.
///
/// A value type with no UI or timers of its own: callers pass the current time in, which
/// makes the engine deterministic and easy to test. The UI drives it as
/// `submit` → (show feedback) → `advance` until `isFinished`.
public struct QuizEngine: Sendable {
    public enum Phase: Equatable, Sendable {
        /// Waiting for an answer to `currentQuestion`.
        case answering
        /// The current question was answered; the record is available for feedback.
        case feedback(AnswerRecord)
        /// All questions done.
        case finished
    }

    public let kind: SessionKind
    public let origin: DeviceOrigin
    public let language: AppLanguage
    public let questions: [Question]
    /// Optional per-question time limit.
    public let timeLimit: TimeInterval?
    public let startedAt: Date

    public private(set) var currentIndex: Int = 0
    public private(set) var answers: [AnswerRecord] = []
    public private(set) var phase: Phase
    public private(set) var finishedAt: Date?
    private var questionShownAt: Date

    public init(
        questions: [Question],
        kind: SessionKind,
        origin: DeviceOrigin,
        language: AppLanguage,
        timeLimit: TimeInterval? = nil,
        startedAt: Date = Date()
    ) {
        // Defensive: never present a question that isn't verified against its source.
        self.questions = questions.filter(QuestionValidator.isPlayable)
        self.kind = kind
        self.origin = origin
        self.language = language
        self.timeLimit = timeLimit.flatMap { $0 > 0 ? $0 : nil }
        self.startedAt = startedAt
        self.questionShownAt = startedAt
        self.phase = self.questions.isEmpty ? .finished : .answering
        if self.questions.isEmpty { finishedAt = startedAt }
    }

    public var currentQuestion: Question? {
        questions.indices.contains(currentIndex) && phase != .finished ? questions[currentIndex] : nil
    }

    public var isFinished: Bool { phase == .finished }

    /// Answers given so far + 1 while a question is on screen; for "2 / 5" style labels.
    public var questionNumber: Int { min(currentIndex + 1, questions.count) }

    /// 0...1 progress through the session.
    public var progress: Double {
        questions.isEmpty ? 1 : Double(answers.count) / Double(questions.count)
    }

    public var correctCount: Int { answers.filter(\.isCorrect).count }

    /// Time left for the current question, or `nil` without a time limit.
    public func remainingTime(at now: Date) -> TimeInterval? {
        guard let timeLimit, phase == .answering else { return nil }
        return max(0, timeLimit - now.timeIntervalSince(questionShownAt))
    }

    /// Records an answer for the current question. Ignored outside the answering phase or
    /// for out-of-range indices. Answers arriving after the time limit count as timeouts.
    @discardableResult
    public mutating func submit(optionIndex: Int, at now: Date = Date()) -> AnswerRecord? {
        guard phase == .answering, let question = currentQuestion,
              question.options.indices.contains(optionIndex) else { return nil }
        if let remaining = remainingTime(at: now), remaining <= 0 {
            return timeOut(at: now)
        }
        return record(question: question, selected: optionIndex, at: now)
    }

    /// Records the current question as unanswered because time ran out.
    @discardableResult
    public mutating func timeOut(at now: Date = Date()) -> AnswerRecord? {
        guard phase == .answering, let question = currentQuestion else { return nil }
        return record(question: question, selected: nil, at: now)
    }

    /// Moves from feedback to the next question (or to `finished`).
    public mutating func advance(at now: Date = Date()) {
        guard case .feedback = phase else { return }
        currentIndex += 1
        if currentIndex >= questions.count {
            phase = .finished
            finishedAt = now
        } else {
            phase = .answering
            questionShownAt = now
        }
    }

    /// Builds the session result once finished.
    ///
    /// - Parameters:
    ///   - currentStreak: streak including today, after this session counts.
    ///   - isFirstSessionToday: whether this is the first completed session today.
    ///   - previouslyPlayedCategories: categories played in earlier sessions.
    public func result(
        rules: ScoringRules = .standard,
        currentStreak: Int,
        isFirstSessionToday: Bool,
        previouslyPlayedCategories: Set<ScienceCategory>,
        id: UUID = UUID()
    ) -> QuizResult? {
        guard isFinished, let finishedAt else { return nil }
        let xp = rules.xp(
            for: answers,
            completed: answers.count == questions.count,
            currentStreak: currentStreak,
            isFirstSessionToday: isFirstSessionToday,
            previouslyPlayedCategories: previouslyPlayedCategories
        )
        return QuizResult(
            id: id,
            kind: kind,
            origin: origin,
            language: language,
            startedAt: startedAt,
            finishedAt: finishedAt,
            answers: answers,
            xp: xp
        )
    }

    private mutating func record(question: Question, selected: Int?, at now: Date) -> AnswerRecord {
        let record = AnswerRecord(
            question: question,
            selectedOptionIndex: selected,
            answeredAt: now,
            responseTime: now.timeIntervalSince(questionShownAt)
        )
        answers.append(record)
        phase = .feedback(record)
        return record
    }
}
