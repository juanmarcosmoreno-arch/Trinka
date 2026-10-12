import SwiftUI
import TrinkaCore
import TrinkaUI

/// End-of-quiz summary: score, accuracy, XP and what was learned (with sources).
struct QuizResultView: View {
    @Environment(AppModel.self) private var model

    let result: QuizResult
    let questions: [Question]
    let newAchievements: [Achievement]
    /// Link to share this result with friends (friend challenges only).
    var challengeShareURL: URL?
    let onDone: () -> Void

    @State private var appeared = false

    var body: some View {
        ScrollView {
            VStack(spacing: Theme.Spacing.xl) {
                scoreHeader
                if let challengeShareURL {
                    ShareLink(item: challengeShareURL,
                              message: Text(L10n.tr("compete.share.resultMessage", result.correctCount, result.totalCount))) {
                        Label(L10n.tr("compete.share.result"), systemImage: "square.and.arrow.up")
                    }
                    .buttonStyle(.trinkaPrimary)
                }
                xpBreakdown
                if !newAchievements.isEmpty { achievements }
                learned
                Button(L10n.tr("result.done"), action: onDone)
                    .buttonStyle(.trinkaPrimary)
            }
            .padding(Theme.Spacing.l)
        }
        .onAppear { appeared = true }
    }

    private var scoreHeader: some View {
        VStack(spacing: Theme.Spacing.m) {
            ZStack {
                ProgressRing(progress: appeared ? result.accuracy : 0, lineWidth: 12)
                VStack(spacing: 0) {
                    Text("\(result.correctCount)/\(result.totalCount)")
                        .font(.trinkaDisplay(.largeTitle))
                    Text(L10n.percent(result.accuracy))
                        .font(.subheadline)
                        .foregroundStyle(Theme.textSecondary)
                }
            }
            .frame(width: 160, height: 160)

            Text(L10n.tr(message))
                .font(.trinkaHeadline(.title3))
                .multilineTextAlignment(.center)
            Text(L10n.tr("result.time", L10n.duration(result.duration)))
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
        }
        .frame(maxWidth: .infinity)
        .accessibilityElement(children: .combine)
    }

    private var message: String {
        switch result.accuracy {
        case 1: "result.message.perfect"
        case 0.6...: "result.message.great"
        case 0.01...: "result.message.good"
        default: "result.message.keepGoing"
        }
    }

    private var xpBreakdown: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            HStack {
                Text(L10n.tr("result.xp"))
                    .font(.trinkaHeadline())
                Spacer()
                Text("+\(result.xp.total) XP")
                    .font(.trinkaHeadline())
                    .foregroundStyle(Theme.accent)
            }
            xpRow("result.xp.answers", result.xp.correctAnswers)
            xpRow("result.xp.completion", result.xp.completion)
            xpRow("result.xp.perfect", result.xp.perfectRun)
            xpRow("result.xp.streak", result.xp.streak)
            xpRow("result.xp.newCategories", result.xp.newCategories)
        }
        .trinkaCard()
    }

    @ViewBuilder
    private func xpRow(_ key: String, _ value: Int) -> some View {
        if value > 0 {
            HStack {
                Text(L10n.tr(key)).foregroundStyle(Theme.textSecondary)
                Spacer()
                Text("+\(value)").monospacedDigit()
            }
            .font(.subheadline)
        }
    }

    private var achievements: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("result.newAchievements"))
            ForEach(newAchievements) { achievement in
                HStack(spacing: Theme.Spacing.m) {
                    Image(systemName: achievement.symbolName)
                        .font(.title2)
                        .foregroundStyle(Theme.accent)
                        .symbolEffect(.bounce, value: appeared)
                    VStack(alignment: .leading) {
                        Text(L10n.title(of: achievement)).font(.headline)
                        Text(L10n.detail(of: achievement)).font(.caption).foregroundStyle(Theme.textSecondary)
                    }
                }
                .trinkaCard(padding: Theme.Spacing.m)
            }
        }
    }

    /// "Knowledge gained": each question's key takeaway with its source.
    private var learned: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("result.learned"), subtitle: L10n.tr("result.learned.subtitle"))
            ForEach(questions) { question in
                let answer = result.answers.first { $0.questionID == question.id }
                NavigationLink {
                    ArticleDetailView(article: question.source, category: question.category)
                } label: {
                    HStack(alignment: .top, spacing: Theme.Spacing.m) {
                        Image(systemName: answer?.isCorrect == true ? "checkmark.circle.fill" : "xmark.circle")
                            .foregroundStyle(answer?.isCorrect == true ? Theme.success : Theme.error)
                        VStack(alignment: .leading, spacing: Theme.Spacing.xs) {
                            Text(question.shortExplanation ?? question.explanation)
                                .font(.subheadline.weight(.medium))
                                .foregroundStyle(Theme.textPrimary)
                                .multilineTextAlignment(.leading)
                            Text("\(question.source.shortAuthorList) · \(question.source.journal) · \(String(question.source.year))")
                                .font(.caption)
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
    }
}
