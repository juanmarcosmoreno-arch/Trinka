import Charts
import SwiftUI
import TrinkaCore
import TrinkaUI

/// Personal learning statistics. Describes quiz activity only — not a measure of intelligence.
struct ProgressDashboardView: View {
    @Environment(AppModel.self) private var model

    private let columns = [GridItem(.flexible(), spacing: Theme.Spacing.m), GridItem(.flexible(), spacing: Theme.Spacing.m)]

    var body: some View {
        let snapshot = model.store.snapshot
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                    LazyVGrid(columns: columns, spacing: Theme.Spacing.m) {
                        StatTile(title: L10n.tr("progress.answered"), value: "\(snapshot.totalAnswered)", systemImage: "questionmark.circle")
                        StatTile(title: L10n.tr("progress.accuracy"), value: L10n.percent(snapshot.accuracy),
                                 systemImage: "target", tint: Theme.success)
                        StatTile(title: L10n.tr("progress.streak", snapshot.longestStreak), value: "\(snapshot.currentStreak)",
                                 systemImage: "flame.fill", tint: Theme.error)
                        StatTile(title: L10n.tr("stats.xp"), value: snapshot.totalXP.formatted(), systemImage: "star.fill",
                                 tint: Theme.Brand.lagoon)
                    }

                    performanceChart(snapshot)
                    categoryBreakdown(snapshot)
                    achievements(snapshot)

                    Label(L10n.tr("progress.disclaimer"), systemImage: "info.circle")
                        .font(.footnote)
                        .foregroundStyle(Theme.textSecondary)
                }
                .padding(Theme.Spacing.l)
            }
            .trinkaBackground()
            .navigationTitle(L10n.tr("progress.title"))
        }
    }

    private func performanceChart(_ snapshot: ProgressSnapshot) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("progress.evolution"), subtitle: L10n.tr("progress.evolution.subtitle"))
            Chart(snapshot.history) { day in
                // Stacked: correct + incorrect = answered that day.
                BarMark(
                    x: .value(L10n.tr("progress.chart.day"), day.day, unit: .day),
                    y: .value(L10n.tr("progress.chart.correct"), day.correct)
                )
                .foregroundStyle(Theme.accent)
                BarMark(
                    x: .value(L10n.tr("progress.chart.day"), day.day, unit: .day),
                    y: .value(L10n.tr("progress.chart.incorrect"), day.answered - day.correct)
                )
                .foregroundStyle(Theme.accentSoft)
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: .day, count: 3)) { _ in
                    AxisValueLabel(format: .dateTime.day().month(.abbreviated).locale(L10n.locale))
                }
            }
            .frame(height: 180)
            .accessibilityLabel(L10n.tr("progress.evolution"))

            HStack(spacing: Theme.Spacing.l) {
                legend(color: Theme.accent, key: "progress.chart.correct")
                legend(color: Theme.accentSoft, key: "progress.chart.incorrect")
            }
            .font(.caption)
            .foregroundStyle(Theme.textSecondary)
        }
        .trinkaCard()
    }

    private func legend(color: Color, key: String) -> some View {
        HStack(spacing: Theme.Spacing.xs) {
            RoundedRectangle(cornerRadius: 2).fill(color).frame(width: 10, height: 10)
            Text(L10n.tr(key))
        }
    }

    private func categoryBreakdown(_ snapshot: ProgressSnapshot) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("progress.categories"))
            let favorites = snapshot.favoriteCategories()
            if favorites.isEmpty {
                Text(L10n.tr("progress.categories.empty"))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            } else {
                Text(L10n.tr("progress.favorites", favorites.map(L10n.name(of:)).formatted(.list(type: .and).locale(L10n.locale))))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            }
            ForEach(ScienceCategory.allCases.filter { (snapshot.answeredByCategory[$0] ?? 0) > 0 }) { category in
                let answered = snapshot.answeredByCategory[category] ?? 0
                let correct = snapshot.correctByCategory[category] ?? 0
                HStack(spacing: Theme.Spacing.m) {
                    CategoryIcon(category, size: 28)
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            Text(L10n.name(of: category)).font(.subheadline.weight(.medium))
                            Spacer()
                            Text("\(correct)/\(answered)").font(.caption.monospacedDigit()).foregroundStyle(Theme.textSecondary)
                        }
                        ProgressView(value: Double(correct), total: Double(max(answered, 1)))
                            .tint(Theme.color(for: category))
                    }
                }
                .accessibilityElement(children: .combine)
            }
        }
        .trinkaCard()
    }

    private func achievements(_ snapshot: ProgressSnapshot) -> some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("progress.achievements"))
            LazyVGrid(columns: columns, spacing: Theme.Spacing.m) {
                ForEach(Achievement.allCases) { achievement in
                    let unlocked = model.store.unlocked[achievement] != nil
                    VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                        Image(systemName: achievement.symbolName)
                            .font(.title2)
                            .foregroundStyle(unlocked ? Theme.accent : Theme.textSecondary.opacity(0.5))
                        Text(L10n.title(of: achievement))
                            .font(.subheadline.weight(.semibold))
                            .foregroundStyle(Theme.textPrimary)
                        Text(L10n.detail(of: achievement))
                            .font(.caption)
                            .foregroundStyle(Theme.textSecondary)
                            .fixedSize(horizontal: false, vertical: true)
                        ProgressView(value: Double(achievement.progress(in: snapshot)), total: Double(achievement.target))
                            .tint(unlocked ? Theme.success : Theme.accent)
                    }
                    .trinkaCard(padding: Theme.Spacing.m)
                    .opacity(unlocked ? 1 : 0.8)
                    .accessibilityElement(children: .combine)
                    .accessibilityValue(unlocked ? L10n.tr("a11y.unlocked")
                                        : "\(achievement.progress(in: snapshot))/\(achievement.target)")
                }
            }
        }
    }
}
