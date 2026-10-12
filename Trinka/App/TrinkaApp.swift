import SwiftData
import SwiftUI
import TrinkaPersistence
import TrinkaUI

@main
struct TrinkaApp: App {
    private let container: ModelContainer
    @State private var model: AppModel
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
        _model = State(initialValue: AppModel(container: container))
    }

    var body: some Scene {
        WindowGroup {
            RootView()
                .environment(model)
                .id(model.languageRevision)
                .environment(\.locale, L10n.locale)
                .tint(Theme.accent)
                .preferredColorScheme(model.store.settings.appearance.colorScheme)
        }
        .modelContainer(container)
        .onChange(of: scenePhase) { _, phase in
            if phase == .active { model.refresh() }
        }
    }
}
