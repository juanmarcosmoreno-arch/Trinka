import SwiftUI
import TrinkaCore
import TrinkaPubMed
import TrinkaUI

/// Research feed from PubMed, filterable by discipline, topic, date and publication type.
struct DiscoverView: View {
    @Environment(AppModel.self) private var model
    @State private var discover = DiscoverModel()
    @State private var showFilters = false

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.l) {
                    categoryPicker
                    content
                }
                .padding(Theme.Spacing.l)
            }
            .trinkaBackground()
            .navigationTitle(L10n.tr("discover.title"))
            .searchable(text: $discover.topic, prompt: L10n.tr("discover.search"))
            .onSubmit(of: .search) { reload() }
            .refreshable { reload() }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button { showFilters = true } label: {
                        Image(systemName: "line.3.horizontal.decrease.circle")
                    }
                    .accessibilityLabel(L10n.tr("discover.filters"))
                }
            }
            .sheet(isPresented: $showFilters, onDismiss: reload) {
                DiscoverFiltersView(discover: discover)
            }
            .task { if discover.state == .idle { reload() } }
        }
    }

    private func reload() {
        let fallback = model.bank.articles.filter { article in
            discover.category == nil || model.category(of: article) == discover.category
        }
        discover.reload(using: model.pubMed, cache: model.articleCache, fallback: fallback)
    }

    private var categoryPicker: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: Theme.Spacing.s) {
                Button {
                    discover.category = nil
                    reload()
                } label: {
                    Text(L10n.tr("explore.allCategories"))
                        .font(.footnote.weight(.semibold))
                        .padding(.horizontal, Theme.Spacing.m)
                        .padding(.vertical, Theme.Spacing.s)
                        .foregroundStyle(discover.category == nil ? Theme.onAccent : Theme.accent)
                        .background(discover.category == nil ? Theme.accent : Theme.accentSoft, in: Capsule())
                }
                ForEach(ScienceCategory.allCases) { category in
                    Button {
                        discover.category = category
                        reload()
                    } label: {
                        CategoryChip(category, isSelected: discover.category == category)
                    }
                }
            }
            .buttonStyle(.plain)
        }
    }

    @ViewBuilder
    private var content: some View {
        switch discover.state {
        case .idle, .loading:
            VStack(spacing: Theme.Spacing.m) {
                ForEach(0..<3, id: \.self) { _ in
                    RoundedRectangle(cornerRadius: Theme.Radius.large).fill(Theme.surfaceMuted).frame(height: 160)
                }
            }
            .redacted(reason: .placeholder)
            .accessibilityLabel(L10n.tr("state.loading"))
        case .failed:
            MessageView(systemImage: "wifi.slash", title: L10n.tr("state.offline.title"), message: L10n.tr("state.offline.message"))
        case let .loaded(articles, source):
            if articles.isEmpty {
                MessageView(systemImage: "magnifyingglass", title: L10n.tr("discover.empty.title"), message: L10n.tr("discover.empty.message"))
            } else {
                sourceBanner(source)
                LazyVStack(spacing: Theme.Spacing.m) {
                    ForEach(articles) { article in
                        NavigationLink {
                            ArticleDetailView(article: article, category: model.category(of: article) ?? discover.category)
                        } label: {
                            ArticleCard(article: article, category: model.category(of: article) ?? discover.category)
                        }
                        .buttonStyle(.plain)
                    }
                }
                Text(L10n.tr("discover.attribution"))
                    .font(.caption2)
                    .foregroundStyle(Theme.textSecondary)
            }
        }
    }

    @ViewBuilder
    private func sourceBanner(_ source: DiscoverModel.Source) -> some View {
        switch source {
        case .live:
            EmptyView()
        case let .cached(date):
            Label(L10n.tr("discover.cached", date.formatted(.relative(presentation: .named).locale(L10n.locale))), systemImage: "clock.arrow.circlepath")
                .font(.footnote).foregroundStyle(Theme.textSecondary)
        case .bundled:
            Label(L10n.tr("discover.bundled"), systemImage: "wifi.slash")
                .font(.footnote).foregroundStyle(Theme.textSecondary)
        }
    }
}

/// Card summarizing an article: simplified title, the authors' conclusion, topic, year, journal.
struct ArticleCard: View {
    let article: ArticleReference
    let category: ScienceCategory?

    var body: some View {
        let digest = ArticleDigest(article: article)
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            HStack {
                if let category { CategoryChip(category) }
                Spacer()
                EvidenceBadge(article.evidenceKind)
            }
            Text(digest.shortTitle)
                .font(.trinkaHeadline())
                .foregroundStyle(Theme.textPrimary)
                .multilineTextAlignment(.leading)
            if let finding = digest.keyFinding {
                VStack(alignment: .leading, spacing: 2) {
                    Text(L10n.tr("article.reportedFinding"))
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(Theme.textSecondary)
                    Text(finding)
                        .font(.subheadline)
                        .foregroundStyle(Theme.textPrimary)
                        .lineLimit(4)
                        .multilineTextAlignment(.leading)
                }
            }
            Text("\(article.journal) · \(String(article.year))")
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
        .trinkaCard()
        .accessibilityElement(children: .combine)
    }
}

/// Filters for date range and publication type.
private struct DiscoverFiltersView: View {
    @Bindable var discover: DiscoverModel
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            Form {
                Section(L10n.tr("discover.filter.date")) {
                    Picker(L10n.tr("discover.filter.date"), selection: $discover.recency) {
                        ForEach(DiscoverModel.Recency.allCases) { recency in
                            Text(L10n.tr("discover.recency.\(recency.rawValue)")).tag(recency)
                        }
                    }
                    .pickerStyle(.inline)
                    .labelsHidden()
                    Toggle(L10n.tr("discover.filter.newestFirst"), isOn: $discover.sortByDate)
                }
                Section(L10n.tr("discover.filter.type")) {
                    ForEach(PublicationType.allCases) { type in
                        Toggle(L10n.tr(type.localizationKey), isOn: Binding(
                            get: { discover.publicationTypes.contains(type) },
                            set: { isOn in
                                if isOn { discover.publicationTypes.insert(type) } else { discover.publicationTypes.remove(type) }
                            }
                        ))
                    }
                }
            }
            .navigationTitle(L10n.tr("discover.filters"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button(L10n.tr("common.apply")) { dismiss() }
                }
            }
        }
        .presentationDetents([.medium, .large])
    }
}
