import SwiftUI
import TrinkaCore
import TrinkaUI

/// Quick Quiz: short prompts, four large answers, haptics and a one-line explanation.
struct QuickQuizView: View {
    @Environment(WatchModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    let session: QuizSession
    @State private var result: QuizResult?

    var body: some View {
        Group {
            if let result {
                WatchResultView(result: result) { dismiss() }
            } else if let question = session.currentQuestion {
                if let answer = session.lastAnswer {
                    feedback(question: question, answer: answer)
                } else {
                    questionView(question)
                }
            }
        }
        .animation(reduceMotion ? nil : .easeOut(duration: 0.2), value: session.lastAnswer)
        .sensoryFeedback(.success, trigger: session.correctFeedback)
        .sensoryFeedback(.error, trigger: session.incorrectFeedback)
        .onChange(of: session.isFinished, initial: true) { _, finished in
            if finished, result == nil, !session.engine.questions.isEmpty {
                result = model.complete(session.engine)
            }
        }
    }

    private func questionView(_ question: Question) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                HStack {
                    Text("\(session.engine.questionNumber)/\(session.engine.questions.count)")
                        .font(.caption2.weight(.semibold))
                        .foregroundStyle(Theme.color(for: question.category))
                    Spacer()
                    if let remaining = session.remainingTime, let limit = session.engine.timeLimit {
                        Gauge(value: remaining, in: 0...limit) {
                            Image(systemName: "timer")
                        } currentValueLabel: {
                            Text("\(Int(remaining.rounded()))")
                        }
                        .gaugeStyle(.accessoryCircularCapacity)
                        .tint(remaining < 5 ? Theme.error : Theme.Brand.mint)
                        .scaleEffect(0.6)
                        .frame(width: 30, height: 30)
                    }
                }
                Text(question.prompt)
                    .font(.system(.headline, design: .rounded))
                    .fixedSize(horizontal: false, vertical: true)
                ForEach(question.options.indices, id: \.self) { index in
                    AnswerButton(index: index, text: question.options[index],
                                 state: session.state(forOption: index), compact: true) {
                        session.select(index)
                    }
                }
            }
        }
        .navigationTitle(L10n.name(of: question.category))
    }

    private func feedback(question: Question, answer: AnswerRecord) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                Label(answer.isCorrect ? L10n.tr("feedback.correct")
                      : (answer.timedOut ? L10n.tr("feedback.timeout") : L10n.tr("feedback.incorrect")),
                      systemImage: answer.isCorrect ? "checkmark.circle.fill" : "xmark.circle.fill")
                    .font(.headline)
                    .foregroundStyle(answer.isCorrect ? Theme.success : Theme.error)
                if !answer.isCorrect {
                    Text(question.correctAnswer)
                        .font(.footnote.weight(.semibold))
                }
                Text(question.shortExplanation ?? question.explanation)
                    .font(.footnote)
                    .fixedSize(horizontal: false, vertical: true)
                // Small bibliographic reference under the answer.
                Text(question.source.citation)
                    .font(.system(size: 10))
                    .foregroundStyle(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
                Button(session.engine.questionNumber == session.engine.questions.count
                       ? L10n.tr("quiz.seeResults") : L10n.tr("quiz.next")) {
                    session.next()
                }
                .buttonStyle(.borderedProminent)
                .tint(Theme.Brand.lagoon)
            }
        }
    }
}

/// End of a Quick Quiz.
struct WatchResultView: View {
    let result: QuizResult
    let onDone: () -> Void

    var body: some View {
        ScrollView {
            VStack(spacing: Theme.Spacing.s) {
                ZStack {
                    ProgressRing(progress: result.accuracy, lineWidth: 6, tint: Theme.Brand.mint)
                    Text("\(result.correctCount)/\(result.totalCount)")
                        .font(.system(.title3, design: .rounded).weight(.bold))
                }
                .frame(width: 70, height: 70)

                Text(L10n.tr(message))
                    .font(.headline)
                    .multilineTextAlignment(.center)

                Grid(alignment: .leading, verticalSpacing: 4) {
                    row("watch.result.correct", "\(result.correctCount)")
                    row("watch.result.score", L10n.percent(result.accuracy))
                    row("watch.result.time", L10n.duration(result.duration))
                    row("watch.result.points", "+\(result.xp.total) XP")
                }
                .font(.footnote)

                Text(L10n.tr("watch.result.openPhone"))
                    .font(.caption2)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)

                Button(L10n.tr("result.done"), action: onDone)
                    .buttonStyle(.borderedProminent)
                    .tint(Theme.Brand.lagoon)
            }
        }
    }

    private var message: String {
        switch result.accuracy {
        case 1: "result.message.perfect"
        case 0.6...: "result.message.great"
        case 0.01...: "result.message.good"
        default: "result.message.keepGoing"
        }
    }

    private func row(_ key: String, _ value: String) -> some View {
        GridRow {
            Text(L10n.tr(key)).foregroundStyle(.secondary)
            Text(value).fontWeight(.semibold).monospacedDigit()
        }
    }
}
