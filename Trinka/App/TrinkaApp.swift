import SwiftData
import SwiftUI
import TrinkaPersistence
import TrinkaUI

@main
struct TrinkaApp: App {
    private let container: ModelContainer
    @State private var model: AppModel
    @State private var showIntro: Bool
    @Environment(\.scenePhase) private var scenePhase

    init() {
        let container: ModelContainer
        do {
            container = try TrinkaSchema.makeContainer()
        } catch {
            // Fall back to an in-memory store so the app stays usable; progress won't persist.
            container = try! TrinkaSchema.makeContainer(inMemory: true)
        }
        self.container = container
        let model = AppModel(container: container)
        _model = State(initialValue: model)
        _showIntro = State(initialValue: model.store.settings.showIntro)
    }

    var body: some Scene {
        WindowGroup {
            ZStack {
                RootView()
                    .environment(model)
                    .id(model.languageRevision)
                    .environment(\.locale, L10n.locale)
                    .tint(Theme.accent)

                // Animated logo on cold launch; outside `.id` so language changes don't replay it.
                if showIntro {
                    LaunchIntroView {
                        withAnimation(.easeOut(duration: 0.45)) { showIntro = false }
                    }
                    .transition(.opacity)
                    .zIndex(1)
                }
            }
            .preferredColorScheme(model.store.settings.appearance.colorScheme)
        }
        .modelContainer(container)
        .onChange(of: scenePhase) { _, phase in
            if phase == .active { model.refresh() }
        }
    }
}
