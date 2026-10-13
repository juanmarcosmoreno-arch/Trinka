import SwiftUI
import TrinkaCore
import TrinkaUI

struct SettingsView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var confirmReset = false
    @State private var sentToWatch = false

    var body: some View {
        @Bindable var settings = model.store.settings
        NavigationStack {
            Form {
                Section {
                    Picker(L10n.tr("settings.appearance"), selection: Binding(
                        get: { settings.appearance },
                        set: { model.setAppearance($0) }
                    )) {
                        ForEach(AppearanceMode.allCases) { mode in
                            Text(L10n.tr(mode.localizationKey)).tag(mode)
                        }
                    }
                    .pickerStyle(.segmented)
                    Toggle(L10n.tr("settings.intro"), isOn: $settings.showIntro)
                } header: {
                    Text(L10n.tr("settings.appearance"))
                } footer: {
                    Text(L10n.tr("settings.appearance.footer"))
                }

                Section(L10n.tr("settings.language")) {
                    Picker(L10n.tr("settings.language"), selection: Binding(
                        get: { settings.languageOverride },
                        set: { model.setLanguageOverride($0) }
                    )) {
                        Text(L10n.tr("settings.language.system")).tag(AppLanguage?.none)
                        Text("English").tag(AppLanguage?.some(.en))
                        Text("Español").tag(AppLanguage?.some(.es))
                    }
                }

                Section {
                    Picker(L10n.tr("settings.difficulty"), selection: Binding(
                        get: { settings.preferredDifficulty },
                        set: { model.setLevel($0) }
                    )) {
                        Text(L10n.tr("difficulty.mixed")).tag(Difficulty?.none)
                        ForEach(Difficulty.allCases) { Text(L10n.name(of: $0)).tag(Difficulty?.some($0)) }
                    }
                    Toggle(L10n.tr("settings.timer"), isOn: $settings.timerEnabled)
                    if settings.timerEnabled {
                        Stepper(L10n.tr("settings.timer.seconds", settings.timerSeconds), value: $settings.timerSeconds, in: 10...60, step: 5)
                    }
                } header: {
                    Text(L10n.tr("settings.quiz"))
                } footer: {
                    Text(L10n.tr("settings.timer.footer"))
                }

                Section(L10n.tr("settings.watch")) {
                    Button {
                        model.publishWatchState()
                        sentToWatch = true
                    } label: {
                        Label(L10n.tr(sentToWatch ? "settings.watch.sent" : "settings.watch.send"), systemImage: "applewatch")
                    }
                    .disabled(!model.isWatchAvailable)
                    if !model.isWatchAvailable {
                        Text(L10n.tr("settings.watch.unavailable")).font(.footnote).foregroundStyle(Theme.textSecondary)
                    }
                }

                Section(L10n.tr("settings.about")) {
                    Text(L10n.tr("settings.about.sources"))
                    Text(L10n.tr("settings.about.privacy"))
                    Link(L10n.tr("settings.about.ncbi"), destination: URL(string: "https://www.ncbi.nlm.nih.gov/home/about/policies/")!)
                }
                .font(.footnote)

                Section {
                    Button(L10n.tr("settings.reset"), role: .destructive) { confirmReset = true }
                }
            }
            .navigationTitle(L10n.tr("settings.title"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button(L10n.tr("result.done")) {
                        model.store.saveSettings()
                        dismiss()
                    }
                }
            }
            .confirmationDialog(L10n.tr("settings.reset.confirm"), isPresented: $confirmReset, titleVisibility: .visible) {
                Button(L10n.tr("settings.reset"), role: .destructive) {
                    model.store.resetProgress()
                    model.publishWatchState()
                }
            }
        }
    }
}
