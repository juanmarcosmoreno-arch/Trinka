import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaQuiz
import TrinkaUI

struct HomeView: View {
    @Environment(AppModel.self) private var model
    @State private var showSettings = false

    private let columns = [GridItem(.adaptive(minimum: 150), spacing: Theme.Spacing.m)]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                    header
                    DailyChallengeCard()
                    LevelCard()
                    stats
                    quickPlay
                    categories
                    if let article = model.featuredArticle() {
                        FeaturedDiscoveryCard(article: article)
                    }
                }
                .padding(.horizontal, Theme.Spacing.l)
                .padding(.bottom, Theme.Spacing.xxl)
            }
            .trinkaBackground()
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    AppearanceMenu()
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button { showSettings = true } label: {
                        Image(systemName: "gearshape")
                    }
                    .accessibilityLabel(L10n.tr("settings.title"))
                }
            }
            .sheet(isPresented: $showSettings) { SettingsView() }
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            TrinkaLogo(height: 40)
            Text(L10n.tr("app.tagline"))
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
        }
        .padding(.top, Theme.Spacing.s)
    }

    private var stats: some View {
        HStack(spacing: Theme.Spacing.m) {
            StatTile(title: L10n.tr("stats.streak"), value: "\(model.store.snapshot.currentStreak)",
                     systemImage: "flame.fill", tint: Theme.error)
            StatTile(title: L10n.tr("stats.xp"), value: model.store.snapshot.totalXP.formatted(),
                     systemImage: "star.fill", tint: Theme.Brand.lagoon)
            StatTile(title: L10n.tr("stats.today"), value: "\(model.store.snapshot.todayXP)",
                     systemImage: "sun.max.fill", tint: Theme.accent)
        }
    }

    private var quickPlay: some View {
        Button {
            model.startQuickPlay()
        } label: {
            Label(L10n.tr("home.quickPlay"), systemImage: "bolt.fill")
        }
        .buttonStyle(.trinkaSecondary)
    }

    private var categories: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("home.categories"), subtitle: L10n.tr("home.categories.subtitle"))
            LazyVGrid(columns: columns, spacing: Theme.Spacing.m) {
                ForEach(ScienceCategory.allCases) { category in
                    Button {
                        model.startCustomQuiz(category: category, difficulty: model.level, count: 3, fillWithNearestLevels: true)
                    } label: {
                        HStack(spacing: Theme.Spacing.s) {
                            CategoryIcon(category, size: 32)
                            Text(L10n.name(of: category))
                                .font(.subheadline.weight(.medium))
                                .foregroundStyle(Theme.textPrimary)
                                .lineLimit(2)
                                .multilineTextAlignment(.leading)
                            Spacer(minLength: 0)
                        }
                        .trinkaCard(padding: Theme.Spacing.m)
                    }
                    .buttonStyle(.plain)
                    .accessibilityHint(L10n.tr("home.categories.hint"))
                }
            }
        }
    }
}

/// "Your level": Basic → Expert. Changes today's challenge and quick play.
private struct LevelCard: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            HStack {
                Text(L10n.tr("home.level"))
                    .font(.trinkaHeadline())
                    .foregroundStyle(Theme.textPrimary)
                Spacer()
                Text(model.level.map(L10n.name(of:)) ?? L10n.tr("difficulty.mixed"))
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.accent)
            }
            LevelPicker(selection: Binding(get: { model.level }, set: { model.setLevel($0) }), allowsMixed: true)
        }
        .trinkaCard()
    }
}

/// Hero card for today's challenge.
private struct DailyChallengeCard: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let snapshot = model.store.snapshot
        let questions = model.dailyQuestions()

        VStack(alignment: .leading, spacing: Theme.Spacing.l) {
            HStack(alignment: .top) {
                VStack(alignment: .leading, spacing: Theme.Spacing.xs) {
                    Text(L10n.tr("daily.title"))
                        .font(.trinkaDisplay(.title2))
                    Text(Date.now.formatted(.dateTime.weekday(.wide).day().month(.wide).locale(L10n.locale)))
                        .font(.subheadline)
                        .opacity(0.8)
                }
                Spacer()
                ZStack {
                    ProgressRing(progress: snapshot.todayDailyCompleted ? 1 : 0, lineWidth: 6, tint: Theme.Brand.mint)
                    Image(systemName: snapshot.todayDailyCompleted ? "checkmark" : "atom")
                        .font(.headline)
                }
                .frame(width: 52, height: 52)
            }

            HStack(spacing: Theme.Spacing.s) {
                ForEach(Array(Set(questions.map(\.category))).sorted { $0.rawValue < $1.rawValue }) { category in
                    Image(systemName: category.symbolName)
                        .font(.caption.weight(.semibold))
                        .frame(width: 28, height: 28)
                        .background(.white.opacity(0.16), in: Circle())
                        .accessibilityLabel(L10n.name(of: category))
                }
            }

            if snapshot.todayDailyCompleted {
                Text(L10n.tr("daily.completed", snapshot.todayDailyCorrect, snapshot.todayDailyAnswered))
                    .font(.subheadline.weight(.medium))
            } else {
                Text(L10n.tr("daily.subtitle", questions.count))
                    .font(.subheadline)
                    .opacity(0.9)
            }

            Button {
                model.startDailyChallenge()
            } label: {
                Text(snapshot.todayDailyCompleted ? L10n.tr("daily.replay") : L10n.tr("daily.play"))
                    .font(.trinkaHeadline())
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, Theme.Spacing.m)
                    .background(Theme.Brand.ivory, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                    .foregroundStyle(Theme.Brand.ink)
            }
            .buttonStyle(.plain)
            .disabled(questions.isEmpty)
        }
        .padding(Theme.Spacing.xl)
        .foregroundStyle(Theme.Brand.ivory)
        .background(Theme.heroGradient, in: RoundedRectangle(cornerRadius: Theme.Radius.large, style: .continuous))
        .accessibilityElement(children: .contain)
    }
}

/// Highlighted research from the verified bank.
private struct FeaturedDiscoveryCard: View {
    @Environment(AppModel.self) private var model
    let article: ArticleReference

    var body: some View {
        let digest = ArticleDigest(article: article)
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("home.featured"))
            NavigationLink {
                ArticleDetailView(article: article, category: model.category(of: article))
            } label: {
                VStack(alignment: .leading, spacing: Theme.Spacing.s) {
                    HStack {
                        if let category = model.category(of: article) { CategoryChip(category) }
                        Spacer()
                        EvidenceBadge(article.evidenceKind)
                    }
                    Text(digest.shortTitle)
                        .font(.trinkaHeadline())
                        .foregroundStyle(Theme.textPrimary)
                        .multilineTextAlignment(.leading)
                    if let finding = digest.keyFinding {
                        Text(finding)
                            .font(.subheadline)
                            .foregroundStyle(Theme.textSecondary)
                            .lineLimit(4)
                            .multilineTextAlignment(.leading)
                    }
                    Text("\(article.journal) · \(String(article.year))")
                        .font(.caption)
                        .foregroundStyle(Theme.textSecondary)
                }
                .trinkaCard()
            }
            .buttonStyle(.plain)
        }
    }
}

/// One-tap switch between following the device, light and dark.
struct AppearanceMenu: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let current = model.store.settings.appearance
        Menu {
            Picker(L10n.tr("settings.appearance"), selection: Binding(
                get: { current },
                set: { model.setAppearance($0) }
            )) {
                ForEach(AppearanceMode.allCases) { mode in
                    Label(L10n.tr(mode.localizationKey), systemImage: mode.symbolName).tag(mode)
                }
            }
        } label: {
            Image(systemName: current.symbolName)
        }
        .accessibilityLabel(L10n.tr("settings.appearance"))
        .accessibilityValue(L10n.tr(current.localizationKey))
    }
}
