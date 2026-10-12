import SwiftUI
import TrinkaUI

struct RootView: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        @Bindable var model = model
        TabView(selection: $model.selectedTab) {
            HomeView()
                .tabItem { Label(L10n.tr("tab.home"), systemImage: "sparkles") }
                .tag(AppTab.home)
            ExploreView()
                .tabItem { Label(L10n.tr("tab.explore"), systemImage: "square.grid.2x2") }
                .tag(AppTab.explore)
            DiscoverView()
                .tabItem { Label(L10n.tr("tab.discover"), systemImage: "doc.text.magnifyingglass") }
                .tag(AppTab.discover)
            CompeteView()
                .tabItem { Label(L10n.tr("tab.compete"), systemImage: "person.2") }
                .tag(AppTab.compete)
            ProgressDashboardView()
                .tabItem { Label(L10n.tr("tab.progress"), systemImage: "chart.line.uptrend.xyaxis") }
                .tag(AppTab.progress)
        }
        .fullScreenCover(item: $model.activeQuiz) { launch in
            QuizFlowView(launch: launch)
        }
        .onOpenURL { url in _ = model.handle(url: url) }
        .alert(L10n.tr("compete.link.title"), isPresented: Binding(
            get: { model.linkError != nil },
            set: { if !$0 { model.linkError = nil } }
        )) {
            Button(L10n.tr("common.ok"), role: .cancel) {}
        } message: {
            Text(model.linkError ?? "")
        }
    }
}
