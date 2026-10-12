import SwiftData
import SwiftUI
import TrinkaPersistence
import TrinkaUI

@main
struct TrinkaWatchApp: App {
    private let container: ModelContainer
    @State private var model: WatchModel
    @Environment(\.scenePhase) private var scenePhase

    init() {
        let container = (try? TrinkaSchema.makeContainer()) ?? (try! TrinkaSchema.makeContainer(inMemory: true))
        self.container = container
        _model = State(initialValue: WatchModel(container: container))
    }

    var body: some Scene {
        WindowGroup {
            WatchHomeView()
                .environment(model)
                .environment(\.locale, L10n.locale)
                .tint(Theme.Brand.mint)
        }
        .modelContainer(container)
        .onChange(of: scenePhase) { _, phase in
            if phase == .active { model.refresh() }
        }
    }
}
