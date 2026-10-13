import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaUI

/// Build a custom quiz (discipline, difficulty, length) and browse recent research.
struct ExploreView: View {
    @Environment(AppModel.self) private var model
    @State private var category: ScienceCategory?
    @State private var difficulty: Difficulty?
    @State private var count = 5
    @State private var didApplyLevel = false
    @State private var recent = DiscoverModel(recency: .lastYear, sortByDate: true)

    private let columns = [GridItem(.adaptive(minimum: 104), spacing: Theme.Spacing.s)]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                    disciplinePicker
                    difficultyPicker
                    lengthPicker
                    startButton
                    recentResearch
                }
                .padding(Theme.Spacing.l)
            }
            .trinkaBackground()
            .navigationTitle(L10n.tr("explore.title"))
            .task(id: category) { loadRecent() }
            .onAppear { if !didApplyLevel { difficulty = model.level; didApplyLevel = true } }
        }
    }

    private var available: Int { model.availableQuestionCount(category: category, difficulty: difficulty) }

    private var disciplinePicker: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("explore.discipline"))
            LazyVGrid(columns: columns, spacing: Theme.Spacing.s) {
                selectable(isSelected: category == nil) {
                    VStack(spacing: Theme.Spacing.xs) {
                        Image(systemName: "circle.grid.cross").font(.title3)
                        Text(L10n.tr("explore.allCategories")).font(.caption.weight(.semibold))
                    }
                } action: { category = nil }

                ForEach(ScienceCategory.allCases) { item in
                    selectable(isSelected: category == item) {
                        VStack(spacing: Theme.Spacing.xs) {
                            Image(systemName: item.symbolName).font(.title3)
                                .foregroundStyle(category == item ? Theme.onAccent : Theme.color(for: item))
                            Text(L10n.name(of: item)).font(.caption.weight(.semibold))
                                .lineLimit(2).multilineTextAlignment(.center)
                        }
                    } action: { category = item }
                }
            }
        }
    }

    private func selectable<Content: View>(isSelected: Bool, @ViewBuilder content: () -> Content, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            content()
                .frame(maxWidth: .infinity, minHeight: 72)
                .padding(Theme.Spacing.s)
                .foregroundStyle(isSelected ? Theme.onAccent : Theme.textPrimary)
                .background(isSelected ? Theme.accent : Theme.surface,
                            in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                .overlay(RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous)
                    .strokeBorder(Theme.separator, lineWidth: isSelected ? 0 : 0.5))
        }
        .buttonStyle(.plain)
        .accessibilityAddTraits(isSelected ? .isSelected : [])
    }

    private var difficultyPicker: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("explore.difficulty"))
            LevelPicker(selection: $difficulty, allowsMixed: true)
        }
    }

    private var lengthPicker: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("explore.length"))
            Picker(L10n.tr("explore.length"), selection: $count) {
                ForEach([3, 5, 10], id: \.self) { Text("\($0)").tag($0) }
            }
            .pickerStyle(.segmented)
            Text(L10n.tr("explore.available", available))
                .font(.footnote)
                .foregroundStyle(Theme.textSecondary)
        }
    }

    private var startButton: some View {
        Button {
            model.startCustomQuiz(category: category, difficulty: difficulty, count: count)
        } label: {
            Label(L10n.tr("explore.start"), systemImage: "play.fill")
        }
        .buttonStyle(.trinkaPrimary)
        .disabled(available == 0)
    }

    private var recentResearch: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            SectionHeader(L10n.tr("explore.recent"), subtitle: L10n.tr("explore.recent.subtitle"))
            switch recent.state {
            case .idle, .loading:
                ProgressView().frame(maxWidth: .infinity).padding()
            case .failed:
                MessageView(systemImage: "wifi.slash", title: L10n.tr("state.offline.title"), message: L10n.tr("state.offline.message"))
            case let .loaded(articles, _):
                ForEach(articles) { article in
                    NavigationLink {
                        ArticleDetailView(article: article, category: category)
                    } label: {
                        ArticleCard(article: article, category: category)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }

    private func loadRecent() {
        recent.category = category
        let fallback = model.bank.articles.filter { category == nil || model.category(of: $0) == category }
        recent.reload(using: model.pubMed, cache: model.articleCache, fallback: fallback, limit: 5)
    }
}
