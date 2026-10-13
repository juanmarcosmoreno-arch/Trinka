import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaUI

/// Full view of one publication: what it reports, how strong that evidence is, and links.
struct ArticleDetailView: View {
    @Environment(AppModel.self) private var model
    let article: ArticleReference
    let category: ScienceCategory?

    @State private var quizPhase: QuizPhase = .idle

    enum QuizPhase: Equatable {
        case idle, working
        case failed(TopicQuizError)
    }

    var body: some View {
        let digest = ArticleDigest(article: article)
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.l) {
                HStack {
                    if let category { CategoryChip(category) }
                    EvidenceBadge(article.evidenceKind)
                }

                Text(article.title)
                    .font(.trinkaHeadline(.title2))
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)

                Text("\(article.authors.prefix(6).joined(separator: ", "))\(article.authors.count > 6 ? ", et al." : "")")
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)

                Text("\(article.journal) · \(String(article.year))")
                    .font(.footnote.weight(.medium))
                    .foregroundStyle(Theme.textSecondary)

                if let finding = digest.keyFinding {
                    VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                        Text(L10n.tr("article.reportedFinding"))
                            .font(.caption.weight(.semibold))
                            .foregroundStyle(Theme.accent)
                        Text(finding)
                            .font(.body)
                            .foregroundStyle(Theme.textPrimary)
                            .fixedSize(horizontal: false, vertical: true)
                        EvidenceNote(article.evidenceKind)
                    }
                    .trinkaCard()
                }

                if let abstract = article.abstract {
                    VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                        SectionHeader(L10n.tr("article.abstract"))
                        Text(abstract)
                            .font(.callout)
                            .foregroundStyle(Theme.textPrimary)
                            .textSelection(.enabled)
                            .fixedSize(horizontal: false, vertical: true)
                        Text(L10n.tr("article.abstractLanguage"))
                            .font(.caption)
                            .foregroundStyle(Theme.textSecondary)
                    }
                }

                if (article.abstract?.count ?? 0) >= 200 {
                    makeQuizSection
                }

                SourceReferenceView(article: article, onOpen: model.didOpen)
            }
            .padding(Theme.Spacing.l)
        }
        .trinkaBackground()
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                ShareLink(item: article.pubMedURL, subject: Text(article.title), message: Text(article.citation))
            }
        }
    }

    /// "Create questions from this article", with the on-device model or the question service.
    @ViewBuilder
    private var makeQuizSection: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            switch quizPhase {
            case .working:
                HStack(spacing: Theme.Spacing.m) {
                    ProgressView()
                    Text(L10n.tr("article.quiz.working")).font(.subheadline).foregroundStyle(Theme.textSecondary)
                }
            case .idle, .failed:
                Button(action: makeQuiz) {
                    Label(L10n.tr("article.quiz.button"), systemImage: "sparkles")
                }
                .buttonStyle(.trinkaSecondary)
                .disabled(!model.canGenerateTopicQuizzes)
                if case let .failed(error) = quizPhase {
                    Text(errorText(error))
                        .font(.footnote).foregroundStyle(Theme.error)
                }
                if !model.canGenerateTopicQuizzes {
                    Text(L10n.tr(OnDeviceAI.statusMessageKey)).font(.footnote).foregroundStyle(Theme.textSecondary)
                }
            }
        }
    }

    private func errorText(_ error: TopicQuizError) -> String {
        switch error {
        case .noQuestions: L10n.tr("article.quiz.noQuestions")
        case .offline: L10n.tr("state.offline.message")
        case let .generation(reason): L10n.tr("topic.error.generation", reason)
        default: L10n.tr("topic.error.service")
        }
    }

    private func makeQuiz() {
        quizPhase = .working
        Task {
            do {
                let quiz = try await model.buildArticleQuiz(article, level: model.level ?? .curious)
                quizPhase = .idle
                model.startTopicQuiz(quiz)
            } catch {
                quizPhase = .failed(error as? TopicQuizError ?? .service)
            }
        }
    }
}
