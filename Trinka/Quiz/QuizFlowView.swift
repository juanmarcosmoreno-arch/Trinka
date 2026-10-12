import SwiftUI
import TrinkaCore
import TrinkaUI

/// Plays a quiz: question → answer → feedback with explanation and source → next → results.
struct QuizFlowView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    let launch: QuizLaunch
    @State private var result: QuizResult?
    @State private var showSource = false
    @State private var confirmExit = false

    private var session: QuizSession { launch.session }

    var body: some View {
        NavigationStack {
            Group {
                if let result {
                    QuizResultView(result: result, questions: session.engine.questions,
                                   newAchievements: model.store.newlyUnlocked,
                                   challengeShareURL: launch.challenge.map { model.localEntry(for: result).resultURL(for: $0) }) {
                        model.store.clearNewlyUnlocked()
                        dismiss()
                    }
                } else if let question = session.currentQuestion {
                    questionView(question)
                        .id(question.id)
                        .transition(reduceMotion ? .opacity : .asymmetric(
                            insertion: .move(edge: .trailing).combined(with: .opacity),
                            removal: .move(edge: .leading).combined(with: .opacity)))
                } else {
                    MessageView(systemImage: "tray", title: L10n.tr("quiz.empty.title"), message: L10n.tr("quiz.empty.message"))
                }
            }
            .animation(reduceMotion ? nil : .easeInOut(duration: 0.3), value: session.engine.currentIndex)
            .trinkaBackground()
            .navigationTitle(result == nil ? launch.title : "")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                if result == nil {
                    ToolbarItem(placement: .cancellationAction) {
                        Button { confirmExit = true } label: { Image(systemName: "xmark") }
                            .accessibilityLabel(L10n.tr("quiz.exit"))
                    }
                }
            }
            .confirmationDialog(L10n.tr("quiz.exit.confirm"), isPresented: $confirmExit, titleVisibility: .visible) {
                Button(L10n.tr("quiz.exit"), role: .destructive) {
                    session.stop()
                    dismiss()
                }
            }
            .sheet(isPresented: $showSource) {
                if let question = session.currentQuestion {
                    NavigationStack {
                        ScrollView {
                            SourceReferenceView(article: question.source,
                                                supportingExcerpt: question.verification.supportingExcerpt,
                                                onOpen: model.didOpen)
                                .padding()
                        }
                        .trinkaBackground()
                        .navigationTitle(L10n.tr("source.title"))
                        .navigationBarTitleDisplayMode(.inline)
                    }
                    .presentationDetents([.medium, .large])
                }
            }
        }
        .sensoryFeedback(.success, trigger: session.correctFeedback)
        .sensoryFeedback(.error, trigger: session.incorrectFeedback)
        .onChange(of: session.isFinished, initial: true) { _, finished in
            if finished, result == nil, !session.engine.questions.isEmpty {
                result = model.complete(session.engine, challenge: launch.challenge)
            }
        }
        .interactiveDismissDisabled(result == nil)
    }

    @ViewBuilder
    private func questionView(_ question: Question) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.l) {
                progressHeader(question)

                Text(question.prompt)
                    .font(.trinkaHeadline(.title3))
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)
                    .accessibilityAddTraits(.isHeader)

                VStack(spacing: Theme.Spacing.m) {
                    ForEach(question.options.indices, id: \.self) { index in
                        AnswerButton(index: index, text: question.options[index],
                                     state: session.state(forOption: index)) {
                            session.select(index)
                        }
                    }
                }

                if let answer = session.lastAnswer {
                    FeedbackCard(question: question, answer: answer) { showSource = true }
                        .transition(.opacity.combined(with: .move(edge: .bottom)))

                    Button {
                        session.next()
                    } label: {
                        Text(session.engine.questionNumber == session.engine.questions.count
                             ? L10n.tr("quiz.seeResults") : L10n.tr("quiz.next"))
                    }
                    .buttonStyle(.trinkaPrimary)
                }
            }
            .padding(Theme.Spacing.l)
            .animation(reduceMotion ? nil : .easeOut(duration: 0.25), value: session.lastAnswer)
        }
    }

    private func progressHeader(_ question: Question) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            HStack {
                CategoryChip(question.category)
                Spacer()
                if let remaining = session.remainingTime {
                    Label(L10n.duration(remaining), systemImage: "timer")
                        .font(.subheadline.monospacedDigit().weight(.semibold))
                        .foregroundStyle(remaining < 5 ? Theme.error : Theme.textSecondary)
                        .accessibilityLabel(L10n.tr("a11y.timeLeft", Int(remaining.rounded())))
                }
                DifficultyBadge(question.difficulty)
            }
            ProgressView(value: session.engine.progress)
                .tint(Theme.accent)
            Text(L10n.tr("quiz.progress", session.engine.questionNumber, session.engine.questions.count))
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
    }
}

/// Correct/incorrect verdict with the scientific explanation and the source.
private struct FeedbackCard: View {
    let question: Question
    let answer: AnswerRecord
    let onShowSource: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            Label(title, systemImage: answer.isCorrect ? "checkmark.seal.fill" : (answer.timedOut ? "timer" : "xmark.seal.fill"))
                .font(.trinkaHeadline())
                .foregroundStyle(answer.isCorrect ? Theme.success : Theme.error)

            if !answer.isCorrect {
                Text(L10n.tr("feedback.correctAnswer", question.correctAnswer))
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.textPrimary)
            }

            Text(question.explanation)
                .font(.body)
                .foregroundStyle(Theme.textPrimary)
                .fixedSize(horizontal: false, vertical: true)

            Divider()

            // Small bibliographic reference right under the answer's explanation.
            Button(action: onShowSource) {
                HStack(alignment: .top, spacing: Theme.Spacing.s) {
                    Image(systemName: "doc.text")
                        .font(.caption)
                    Text(question.source.citation)
                        .font(.caption2)
                        .multilineTextAlignment(.leading)
                        .fixedSize(horizontal: false, vertical: true)
                    Spacer(minLength: 0)
                    Image(systemName: "chevron.right").font(.caption2)
                }
                .foregroundStyle(Theme.textSecondary)
            }
            .buttonStyle(.plain)
            .accessibilityLabel(L10n.tr("feedback.source"))
            .accessibilityValue(question.source.citation)
        }
        .trinkaCard()
        .accessibilityElement(children: .contain)
    }

    private var title: String {
        if answer.isCorrect { return L10n.tr("feedback.correct") }
        return answer.timedOut ? L10n.tr("feedback.timeout") : L10n.tr("feedback.incorrect")
    }
}
