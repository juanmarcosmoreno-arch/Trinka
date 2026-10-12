import Foundation
import Observation
import TrinkaCore
import TrinkaQuiz

/// Observable wrapper around `QuizEngine` for SwiftUI, shared by iPhone and Apple Watch.
///
/// Owns the optional countdown and exposes counters that views use as triggers for
/// haptics (`.sensoryFeedback`) and animations.
@MainActor
@Observable
public final class QuizSession {
    public private(set) var engine: QuizEngine
    /// Seconds left for the current question when the timer is on.
    public private(set) var remainingTime: TimeInterval?
    /// Incremented on every correct answer — use as a `.sensoryFeedback(.success, trigger:)` trigger.
    public private(set) var correctFeedback = 0
    /// Incremented on every wrong answer or timeout.
    public private(set) var incorrectFeedback = 0

    @ObservationIgnored private var timerTask: Task<Void, Never>?
    private let clock: () -> Date

    public init(engine: QuizEngine, clock: @escaping () -> Date = Date.init) {
        self.engine = engine
        self.clock = clock
        restartTimer()
    }

    public var currentQuestion: Question? { engine.currentQuestion }
    public var isFinished: Bool { engine.isFinished }

    /// The answer just given, while its feedback is on screen.
    public var lastAnswer: AnswerRecord? {
        if case let .feedback(record) = engine.phase { return record }
        return nil
    }

    /// State for option `index` of the current question.
    public func state(forOption index: Int) -> AnswerState {
        guard let question = currentQuestion, let answer = lastAnswer else { return .idle }
        if answer.selectedOptionIndex == index {
            return answer.isCorrect ? .correct : .incorrect
        }
        return question.isCorrect(index) ? .revealedCorrect : .dimmed
    }

    public func select(_ index: Int) {
        guard let record = engine.submit(optionIndex: index, at: clock()) else { return }
        stopTimer()
        if record.isCorrect { correctFeedback += 1 } else { incorrectFeedback += 1 }
    }

    public func next() {
        engine.advance(at: clock())
        restartTimer()
    }

    public func stop() {
        stopTimer()
    }

    private func restartTimer() {
        stopTimer()
        guard engine.timeLimit != nil, engine.phase == .answering else { return }
        remainingTime = engine.remainingTime(at: clock())
        // Holds `self` weakly, so the loop ends on its own if the session goes away.
        timerTask = Task { [weak self] in
            while !Task.isCancelled {
                try? await Task.sleep(nanoseconds: 250_000_000)
                guard let self, !Task.isCancelled else { return }
                self.tick()
            }
        }
    }

    private func tick() {
        let remaining = engine.remainingTime(at: clock())
        remainingTime = remaining
        if let remaining, remaining <= 0 {
            if engine.timeOut(at: clock()) != nil { incorrectFeedback += 1 }
            stopTimer()
        }
    }

    private func stopTimer() {
        timerTask?.cancel()
        timerTask = nil
        remainingTime = nil
    }
}
