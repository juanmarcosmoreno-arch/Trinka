import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaUI

/// "Create questions about a topic": searches PubMed and generates source-checked questions.
struct TopicQuizView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss

    @State private var topic: String
    @State private var level: Difficulty?
    @State private var count = 5
    @State private var state: Phase = .idle
    @State private var task: Task<Void, Never>?
    @FocusState private var topicFocused: Bool

    enum Phase: Equatable {
        case idle
        case working(TopicQuizProgress)
        case ready(TopicQuiz)
        case failed(TopicQuizError)
    }

    init(topic: String = "") {
        _topic = State(initialValue: topic)
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                    Text(L10n.tr("topic.intro"))
                        .font(.subheadline)
                        .foregroundStyle(Theme.textSecondary)

                    VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                        Text(L10n.tr("topic.field")).font(.caption.weight(.semibold)).foregroundStyle(Theme.textSecondary)
                        TextField(L10n.tr("topic.placeholder"), text: $topic)
                            .font(.title3.weight(.semibold))
                            .padding(Theme.Spacing.m)
                            .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                            .focused($topicFocused)
                            .submitLabel(.go)
                            .onSubmit(generate)
                            .autocorrectionDisabled()
                    }

                    VStack(alignment: .leading, spacing: Theme.Spacing.m) {
                        SectionHeader(L10n.tr("explore.difficulty"))
                        LevelPicker(selection: $level)
                    }

                    VStack(alignment: .leading, spacing: Theme.Spacing.m) {
                        SectionHeader(L10n.tr("explore.length"))
                        Picker(L10n.tr("explore.length"), selection: $count) {
                            ForEach([3, 5, 10], id: \.self) { Text("\($0)").tag($0) }
                        }
                        .pickerStyle(.segmented)
                    }

                    phaseView

                    Label(L10n.tr("topic.disclaimer"), systemImage: "info.circle")
                        .font(.footnote)
                        .foregroundStyle(Theme.textSecondary)
                }
                .padding(Theme.Spacing.l)
            }
            .trinkaBackground()
            .navigationTitle(L10n.tr("topic.title"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(L10n.tr("common.cancel")) {
                        task?.cancel()
                        dismiss()
                    }
                }
            }
            .onAppear {
                if level == nil { level = model.level ?? .curious }
                if topic.isEmpty { topicFocused = true }
            }
        }
    }

    @ViewBuilder
    private var phaseView: some View {
        switch state {
        case .idle, .failed:
            if case let .failed(error) = state {
                MessageView(systemImage: icon(for: error), title: L10n.tr("topic.error.title"), message: detailedMessage(for: error))
            }
            Button(action: generate) {
                Label(L10n.tr("topic.generate"), systemImage: "sparkles")
            }
            .buttonStyle(.trinkaPrimary)
            .disabled(topic.trimmingCharacters(in: .whitespaces).count < 3 || !model.canGenerateTopicQuizzes)
            if !model.canGenerateTopicQuizzes {
                Text(L10n.tr("topic.notConfigured")).font(.footnote).foregroundStyle(Theme.error)
            }
        case let .working(progress):
            HStack(spacing: Theme.Spacing.m) {
                ProgressView()
                Text(progressText(progress))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .trinkaCard()
        case let .ready(quiz):
            VStack(alignment: .leading, spacing: Theme.Spacing.m) {
                Label(L10n.tr("topic.ready", quiz.questions.count, quiz.articles.count), systemImage: "checkmark.seal")
                    .font(.trinkaHeadline())
                    .foregroundStyle(Theme.success)
                ForEach(quiz.articles) { article in
                    Text("• \(ArticleDigest(article: article).shortTitle) (\(article.journal), \(String(article.year)))")
                        .font(.caption)
                        .foregroundStyle(Theme.textSecondary)
                }
                Button {
                    dismiss()
                    model.startTopicQuiz(quiz)
                } label: {
                    Label(L10n.tr("topic.play"), systemImage: "play.fill")
                }
                .buttonStyle(.trinkaPrimary)
            }
            .trinkaCard()
        }
    }

    private func generate() {
        let topic = topic.trimmingCharacters(in: .whitespacesAndNewlines)
        guard topic.count >= 3, model.canGenerateTopicQuizzes else { return }
        topicFocused = false
        state = .working(.searching)
        let level = level ?? .curious
        task = Task {
            do {
                let quiz = try await model.buildTopicQuiz(topic: topic, level: level, count: count) { progress in
                    Task { @MainActor in
                        if case .working = state { state = .working(progress) }
                    }
                }
                state = .ready(quiz)
            } catch is CancellationError {
                state = .idle
            } catch {
                state = .failed(error as? TopicQuizError ?? .service)
            }
        }
    }

    private func progressText(_ progress: TopicQuizProgress) -> String {
        switch progress {
        case .searching: L10n.tr("topic.progress.searching")
        case let .generating(articles): L10n.tr("topic.progress.generating", articles)
        case .done: L10n.tr("topic.progress.checking")
        }
    }

    private func icon(for error: TopicQuizError) -> String {
        error == .offline ? "wifi.slash" : "exclamationmark.magnifyingglass"
    }

    private func detailedMessage(for error: TopicQuizError) -> String {
        if case let .generation(reason) = error { return L10n.tr("topic.error.generation", reason) }
        return L10n.tr(message(for: error))
    }

    private func message(for error: TopicQuizError) -> String {
        switch error {
        case .notConfigured: "topic.notConfigured"
        case .offline: "state.offline.message"
        case .noArticles: "topic.error.noArticles"
        case .noQuestions: "topic.error.noQuestions"
        case .service: "topic.error.service"
        case .search: "topic.error.search"
        case .generation: "topic.error.generation"
        }
    }
}

/// Explore entry point plus the list of recent topic quizzes.
struct TopicQuizSection: View {
    @Environment(AppModel.self) private var model
    @State private var showBuilder = false

    var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            Button { showBuilder = true } label: {
                HStack(spacing: Theme.Spacing.m) {
                    Image(systemName: "sparkles")
                        .font(.title2)
                        .foregroundStyle(Theme.Brand.ivory)
                        .frame(width: 44, height: 44)
                        .background(Theme.heroGradient, in: RoundedRectangle(cornerRadius: Theme.Radius.small, style: .continuous))
                    VStack(alignment: .leading, spacing: 2) {
                        Text(L10n.tr("topic.title")).font(.trinkaHeadline()).foregroundStyle(Theme.textPrimary)
                        Text(L10n.tr("topic.example")).font(.caption).foregroundStyle(Theme.textSecondary)
                    }
                    Spacer()
                    Image(systemName: "chevron.right").foregroundStyle(Theme.textSecondary)
                }
                .trinkaCard()
            }
            .buttonStyle(.plain)

            if !model.topicQuizzes.isEmpty {
                SectionHeader(L10n.tr("topic.recent"))
                ForEach(model.topicQuizzes) { quiz in
                    Button { model.startTopicQuiz(quiz) } label: {
                        HStack {
                            VStack(alignment: .leading, spacing: 2) {
                                Text(quiz.topic).font(.subheadline.weight(.semibold)).foregroundStyle(Theme.textPrimary)
                                Text("\(L10n.name(of: quiz.level)) · \(L10n.tr("compete.questions", quiz.questions.count))")
                                    .font(.caption).foregroundStyle(Theme.textSecondary)
                            }
                            Spacer()
                            Image(systemName: "play.circle.fill").font(.title2).foregroundStyle(Theme.accent)
                        }
                        .trinkaCard(padding: Theme.Spacing.m)
                    }
                    .buttonStyle(.plain)
                    .contextMenu {
                        Button(L10n.tr("compete.delete"), systemImage: "trash", role: .destructive) { model.deleteTopicQuiz(quiz) }
                    }
                }
            }
        }
        .sheet(isPresented: $showBuilder) { TopicQuizView() }
    }
}
