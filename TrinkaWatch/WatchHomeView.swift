import SwiftUI
import TrinkaCore
import TrinkaQuiz
import TrinkaUI

/// Watch home: brand, PLAY, and today's status at a glance.
struct WatchHomeView: View {
    @Environment(WatchModel.self) private var model

    var body: some View {
        @Bindable var model = model
        let snapshot = model.store.snapshot
        NavigationStack {
            ScrollView {
                VStack(spacing: Theme.Spacing.m) {
                    VStack(spacing: Theme.Spacing.xs) {
                        TrinkaMark().frame(width: 34, height: 34)
                        TrinkaWordmark(size: 16, color: Theme.Brand.ivory)
                        Text(L10n.tr("watch.tagline"))
                            .font(.footnote)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }

                    Button(action: model.play) {
                        Text(L10n.tr(snapshot.todayDailyCompleted ? "watch.playAgain" : "watch.play"))
                            .font(.system(.title3, design: .rounded).weight(.bold))
                            .frame(maxWidth: .infinity, minHeight: 50)
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(Theme.Brand.mint)
                    .foregroundStyle(Theme.Brand.ink)
                    .disabled(model.todaysQuestions.isEmpty)

                    VStack(spacing: Theme.Spacing.s) {
                        statusRow(icon: "flame.fill", tint: Theme.error,
                                  title: L10n.tr("stats.streak"), value: "\(snapshot.currentStreak)")
                        statusRow(icon: "star.fill", tint: Theme.Brand.lagoon,
                                  title: L10n.tr("watch.dailyScore"), value: "\(snapshot.todayXP) XP")
                        statusRow(icon: snapshot.todayDailyCompleted ? "checkmark.circle.fill" : "circle.dashed",
                                  tint: Theme.Brand.mint,
                                  title: L10n.tr("watch.challenge"),
                                  value: snapshot.todayDailyCompleted
                                      ? "\(snapshot.todayDailyCorrect)/\(snapshot.todayDailyAnswered)"
                                      : "0/\(model.todaysQuestions.count)")
                    }
                }
                .padding(.horizontal, Theme.Spacing.xs)
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    NavigationLink {
                        WatchSettingsView()
                    } label: {
                        Image(systemName: "gearshape")
                    }
                    .accessibilityLabel(L10n.tr("settings.title"))
                }
            }
        }
        .fullScreenCover(item: $model.activeQuiz) { launch in
            QuickQuizView(session: launch.session)
        }
    }

    private func statusRow(icon: String, tint: Color, title: String, value: String) -> some View {
        HStack {
            Image(systemName: icon).foregroundStyle(tint)
            Text(title).font(.footnote).foregroundStyle(.secondary)
            Spacer()
            Text(value).font(.footnote.weight(.semibold)).monospacedDigit()
        }
        .accessibilityElement(children: .combine)
    }
}

private struct WatchSettingsView: View {
    @Environment(WatchModel.self) private var model

    var body: some View {
        let settings = model.store.settings
        List {
            Picker(L10n.tr("home.level"), selection: Binding(
                get: { settings.preferredDifficulty },
                set: { model.setLevel($0) }
            )) {
                Text(L10n.tr("difficulty.mixed")).tag(Difficulty?.none)
                ForEach(Difficulty.allCases) { Text(L10n.name(of: $0)).tag(Difficulty?.some($0)) }
            }
            Toggle(L10n.tr("settings.timer"), isOn: Binding(
                get: { settings.timerEnabled },
                set: { model.setTimer(enabled: $0) }
            ))
            Text(L10n.tr("watch.settings.note"))
                .font(.footnote)
                .foregroundStyle(.secondary)
        }
        .navigationTitle(L10n.tr("settings.title"))
    }
}
