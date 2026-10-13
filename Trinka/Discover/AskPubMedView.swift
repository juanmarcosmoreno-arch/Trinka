import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaUI

/// "Ask PubMed": type a question or topic and get an answer built only from PubMed abstracts,
/// with every sentence citing its article.
struct AskPubMedView: View {
    @Environment(AppModel.self) private var model
    @State private var question = ""
    @State private var phase: Phase = .idle
    @State private var task: Task<Void, Never>?
    @State private var topicQuizTopic: DiscoverView.TopicSeed?
    @FocusState private var focused: Bool

    enum Phase: Equatable {
        case idle
        case working
        case answered(EvidenceAnswer)
        case failed(EvidenceAnswerError)
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.l) {
                Text(L10n.tr("ask.intro"))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)

                TextField(L10n.tr("ask.placeholder"), text: $question, axis: .vertical)
                    .font(.title3.weight(.semibold))
                    .lineLimit(1...4)
                    .padding(Theme.Spacing.m)
                    .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                    .focused($focused)
                    .submitLabel(.search)
                    .onSubmit(ask)

                Button(action: ask) {
                    Label(L10n.tr("ask.button"), systemImage: "text.magnifyingglass")
                }
                .buttonStyle(.trinkaPrimary)
                .disabled(question.trimmingCharacters(in: .whitespaces).count < 3 || phase == .working)

                modeNote
                phaseView
            }
            .padding(Theme.Spacing.l)
        }
        .trinkaBackground()
        .navigationTitle(L10n.tr("ask.title"))
        .navigationBarTitleDisplayMode(.inline)
        .sheet(item: $topicQuizTopic) { seed in TopicQuizView(topic: seed.topic) }
        .onDisappear { task?.cancel() }
    }

    @ViewBuilder
    private var modeNote: some View {
        if OnDeviceAI.isAvailable {
            Label(L10n.tr("ask.mode.onDevice"), systemImage: "apple.intelligence")
                .font(.footnote)
                .foregroundStyle(Theme.textSecondary)
        } else {
            Label(L10n.tr("ask.mode.quotes", L10n.tr(OnDeviceAI.statusMessageKey)), systemImage: "quote.opening")
                .font(.footnote)
                .foregroundStyle(Theme.textSecondary)
        }
    }

    @ViewBuilder
    private var phaseView: some View {
        switch phase {
        case .idle:
            EmptyView()
        case .working:
            HStack(spacing: Theme.Spacing.m) {
                ProgressView()
                Text(L10n.tr("ask.working")).font(.subheadline).foregroundStyle(Theme.textSecondary)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .trinkaCard()
        case let .failed(error):
            MessageView(systemImage: error == .offline ? "wifi.slash" : "exclamationmark.magnifyingglass",
                        title: L10n.tr("ask.error.title"), message: L10n.tr(message(for: error)))
        case let .answered(answer):
            answerView(answer)
        }
    }

    @ViewBuilder
    private func answerView(_ answer: EvidenceAnswer) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            switch answer.kind {
            case .noEvidence:
                MessageView(systemImage: "doc.text.magnifyingglass", title: L10n.tr("ask.noEvidence.title"),
                            message: L10n.tr("ask.noEvidence.message"))
            case .synthesized, .quoted:
                VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                    Label(L10n.tr(answer.kind == .synthesized ? "ask.kind.synthesized" : "ask.kind.quoted"),
                          systemImage: answer.kind == .synthesized ? "sparkles" : "quote.opening")
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(Theme.accent)
                    ForEach(Array(answer.statements.enumerated()), id: \.offset) { _, statement in
                        Text(statementText(statement, quoted: answer.kind == .quoted))
                            .font(.body)
                            .foregroundStyle(Theme.textPrimary)
                            .fixedSize(horizontal: false, vertical: true)
                    }
                    Text(L10n.tr("ask.disclaimer"))
                        .font(.caption)
                        .foregroundStyle(Theme.textSecondary)
                }
                .trinkaCard()
            }

            if !answer.sources.isEmpty {
                SectionHeader(L10n.tr("ask.sources"))
                ForEach(Array(answer.sources.enumerated()), id: \.element.pmid) { index, article in
                    NavigationLink {
                        ArticleDetailView(article: article, category: model.category(of: article))
                    } label: {
                        HStack(alignment: .top, spacing: Theme.Spacing.s) {
                            Text("[\(index + 1)]")
                                .font(.footnote.weight(.bold).monospacedDigit())
                                .foregroundStyle(Theme.accent)
                            VStack(alignment: .leading, spacing: 2) {
                                Text(article.title)
                                    .font(.footnote.weight(.semibold))
                                    .foregroundStyle(Theme.textPrimary)
                                    .multilineTextAlignment(.leading)
                                Text(article.citation)
                                    .font(.caption2)
                                    .foregroundStyle(Theme.textSecondary)
                                    .multilineTextAlignment(.leading)
                            }
                            Spacer(minLength: 0)
                            Image(systemName: "chevron.right").font(.caption).foregroundStyle(Theme.textSecondary)
                        }
                        .trinkaCard(padding: Theme.Spacing.m)
                    }
                    .buttonStyle(.plain)
                }
            }

            if model.canGenerateTopicQuizzes, answer.kind != .noEvidence {
                Button {
                    topicQuizTopic = DiscoverView.TopicSeed(topic: answer.question)
                } label: {
                    Label(L10n.tr("ask.makeQuiz"), systemImage: "questionmark.bubble")
                }
                .buttonStyle(.trinkaSecondary)
            }
        }
    }

    private func statementText(_ statement: EvidenceAnswer.Statement, quoted: Bool) -> String {
        let marks = statement.citations.map { "[\($0)]" }.joined()
        return quoted ? "“\(statement.text)” \(marks)" : "\(statement.text) \(marks)"
    }

    private func ask() {
        let text = question.trimmingCharacters(in: .whitespacesAndNewlines)
        guard text.count >= 3 else { return }
        focused = false
        task?.cancel()
        phase = .working
        task = Task {
            do {
                let answer = try await model.askPubMed(text)
                guard !Task.isCancelled else { return }
                phase = .answered(answer)
            } catch {
                guard !Task.isCancelled else { return }
                phase = .failed(error as? EvidenceAnswerError ?? .service)
            }
        }
    }

    private func message(for error: EvidenceAnswerError) -> String {
        switch error {
        case .tooShort: "ask.error.tooShort"
        case .offline: "state.offline.message"
        case .noArticles: "ask.error.noArticles"
        case .service: "ask.error.service"
        }
    }
}

/// Entry card for Discover.
struct AskPubMedCard: View {
    var body: some View {
        NavigationLink {
            AskPubMedView()
        } label: {
            HStack(spacing: Theme.Spacing.m) {
                Image(systemName: "text.magnifyingglass")
                    .font(.title2)
                    .foregroundStyle(Theme.onAccent)
                    .frame(width: 44, height: 44)
                    .background(Theme.accent, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                VStack(alignment: .leading, spacing: 2) {
                    Text(L10n.tr("ask.title")).font(.trinkaHeadline()).foregroundStyle(Theme.textPrimary)
                    Text(L10n.tr("ask.card.subtitle")).font(.footnote).foregroundStyle(Theme.textSecondary)
                        .multilineTextAlignment(.leading)
                }
                Spacer(minLength: 0)
                Image(systemName: "chevron.right").foregroundStyle(Theme.textSecondary)
            }
            .trinkaCard()
        }
        .buttonStyle(.plain)
    }
}
