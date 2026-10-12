import SwiftUI
import UIKit
import TrinkaCore
import TrinkaQuiz
import TrinkaUI

/// One friend challenge: its code, how to invite others, play, and the leaderboard.
struct ChallengeDetailView: View {
    @Environment(AppModel.self) private var model
    let code: ChallengeCode
    @State private var copied = false

    var body: some View {
        let stored = model.challenges.challenge(for: code)
        let title = stored?.title ?? model.defaultTitle(for: code)
        let entries = Leaderboard.ranked(stored?.entries ?? [])
        let myBest = entries.first { $0.isLocalPlayer }
        let playable = !model.challengeQuestions(code).isEmpty

        ScrollView {
            VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                codeCard(title: title)

                if playable {
                    Button {
                        model.startChallenge(code)
                    } label: {
                        Label(L10n.tr(myBest == nil ? "compete.play" : "compete.playAgain"), systemImage: "play.fill")
                    }
                    .buttonStyle(.trinkaPrimary)
                } else {
                    MessageView(systemImage: "exclamationmark.triangle", title: L10n.tr("compete.link.title"),
                                message: L10n.tr("compete.link.incompatible"))
                }

                leaderboard(entries)

                if let myBest {
                    ShareLink(item: myBest.resultURL(for: code),
                              message: Text(L10n.tr("compete.share.resultMessage", myBest.correct, myBest.total))) {
                        Label(L10n.tr("compete.share.result"), systemImage: "square.and.arrow.up")
                    }
                    .buttonStyle(.trinkaSecondary)
                }

                Text(L10n.tr("compete.howResults"))
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)
            }
            .padding(Theme.Spacing.l)
        }
        .trinkaBackground()
        .navigationTitle(title)
        .navigationBarTitleDisplayMode(.inline)
    }

    private func codeCard(title: String) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            Text(L10n.tr("compete.code"))
                .font(.caption.weight(.semibold))
                .opacity(0.8)
            Text(code.code)
                .font(.system(.title, design: .monospaced).weight(.semibold))
                .minimumScaleFactor(0.6)
                .lineLimit(1)
                .textSelection(.enabled)
                .accessibilityLabel(code.code.map(String.init).joined(separator: " "))

            HStack(spacing: Theme.Spacing.s) {
                summaryChip(code.category.map(L10n.name(of:)) ?? L10n.tr("explore.allCategories"))
                summaryChip(code.difficulty.map(L10n.name(of:)) ?? L10n.tr("difficulty.mixed"))
                summaryChip(L10n.tr("compete.questions", code.questionCount))
            }

            HStack(spacing: Theme.Spacing.s) {
                Button {
                    UIPasteboard.general.string = code.code
                    copied = true
                } label: {
                    Label(L10n.tr(copied ? "compete.copied" : "compete.copy"), systemImage: copied ? "checkmark" : "doc.on.doc")
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, Theme.Spacing.m)
                        .background(.white.opacity(0.16), in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                }
                ShareLink(item: code.inviteURL(title: title),
                          message: Text(L10n.tr("compete.share.inviteMessage", title, code.code))) {
                    Label(L10n.tr("compete.invite"), systemImage: "square.and.arrow.up")
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, Theme.Spacing.m)
                        .background(Theme.Brand.ivory, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                        .foregroundStyle(Theme.Brand.ink)
                }
            }
            .font(.subheadline.weight(.semibold))
            .buttonStyle(.plain)
        }
        .padding(Theme.Spacing.xl)
        .foregroundStyle(Theme.Brand.ivory)
        .background(Theme.heroGradient, in: RoundedRectangle(cornerRadius: Theme.Radius.large, style: .continuous))
    }

    private func summaryChip(_ text: String) -> some View {
        Text(text)
            .font(.caption.weight(.semibold))
            .padding(.horizontal, Theme.Spacing.s)
            .padding(.vertical, Theme.Spacing.xs)
            .background(.white.opacity(0.16), in: Capsule())
    }

    private func leaderboard(_ entries: [ChallengeEntry]) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("compete.leaderboard"))
            if entries.isEmpty {
                Text(L10n.tr("compete.leaderboard.empty"))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            }
            ForEach(Array(entries.enumerated()), id: \.element.id) { index, entry in
                HStack(spacing: Theme.Spacing.m) {
                    rankBadge(index + 1)
                    Text(entry.isLocalPlayer ? "\(entry.playerName) (\(L10n.tr("compete.you")))" : entry.playerName)
                        .font(.body.weight(entry.isLocalPlayer ? .semibold : .regular))
                        .foregroundStyle(Theme.textPrimary)
                        .lineLimit(1)
                    Spacer()
                    VStack(alignment: .trailing, spacing: 0) {
                        Text("\(entry.correct)/\(entry.total)")
                            .font(.headline.monospacedDigit())
                        Text(L10n.duration(entry.duration))
                            .font(.caption.monospacedDigit())
                            .foregroundStyle(Theme.textSecondary)
                    }
                }
                .padding(.vertical, Theme.Spacing.xs)
                .accessibilityElement(children: .combine)
                if index < entries.count - 1 { Divider() }
            }
        }
        .trinkaCard()
    }

    private func rankBadge(_ rank: Int) -> some View {
        Text("\(rank)")
            .font(.subheadline.weight(.bold).monospacedDigit())
            .frame(width: 30, height: 30)
            .foregroundStyle(rank <= 3 ? Theme.onAccent : Theme.textSecondary)
            .background(rank == 1 ? Theme.accent : (rank <= 3 ? Theme.Brand.lagoon : Theme.surfaceMuted), in: Circle())
    }
}
