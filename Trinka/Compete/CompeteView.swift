import SwiftUI
import TrinkaCore
import TrinkaPersistence
import TrinkaQuiz
import TrinkaUI

/// Friend challenges: create or join with a code, play the same questions, compare results.
struct CompeteView: View {
    @Environment(AppModel.self) private var model
    @State private var path: [String] = []
    @State private var showCreate = false
    @State private var showJoin = false

    var body: some View {
        NavigationStack(path: $path) {
            ScrollView {
                VStack(alignment: .leading, spacing: Theme.Spacing.xl) {
                    intro
                    PlayerNameField()
                    HStack(spacing: Theme.Spacing.m) {
                        Button { showCreate = true } label: {
                            Label(L10n.tr("compete.create"), systemImage: "plus")
                        }
                        .buttonStyle(.trinkaPrimary)
                        Button { showJoin = true } label: {
                            Label(L10n.tr("compete.join"), systemImage: "number")
                        }
                        .buttonStyle(.trinkaSecondary)
                    }
                    list
                }
                .padding(Theme.Spacing.l)
            }
            .trinkaBackground()
            .navigationTitle(L10n.tr("compete.title"))
            .navigationDestination(for: String.self) { code in
                if let code = ChallengeCode(code) {
                    ChallengeDetailView(code: code)
                }
            }
            .sheet(isPresented: $showCreate) {
                CreateChallengeView { code in
                    path.append(code.code)
                }
            }
            .sheet(isPresented: $showJoin) {
                JoinChallengeView()
            }
            .onChange(of: model.openedChallenge, initial: true) { _, code in
                guard let code else { return }
                showJoin = false
                path = [code.code]
                model.openedChallenge = nil
            }
        }
    }

    private var intro: some View {
        HStack(alignment: .top, spacing: Theme.Spacing.m) {
            Image(systemName: "person.2.wave.2")
                .font(.title2)
                .foregroundStyle(Theme.accent)
            Text(L10n.tr("compete.intro"))
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
                .fixedSize(horizontal: false, vertical: true)
        }
    }

    @ViewBuilder
    private var list: some View {
        if model.challenges.challenges.isEmpty {
            MessageView(systemImage: "trophy", title: L10n.tr("compete.empty.title"), message: L10n.tr("compete.empty.message"))
        } else {
            VStack(alignment: .leading, spacing: Theme.Spacing.m) {
                SectionHeader(L10n.tr("compete.mine"))
                ForEach(model.challenges.challenges, id: \.code) { challenge in
                    NavigationLink(value: challenge.code) {
                        ChallengeRow(challenge: challenge)
                    }
                    .buttonStyle(.plain)
                    .contextMenu {
                        Button(L10n.tr("compete.delete"), systemImage: "trash", role: .destructive) {
                            model.challenges.delete(challenge)
                        }
                    }
                }
            }
        }
    }
}

private struct ChallengeRow: View {
    let challenge: StoredChallenge

    var body: some View {
        let ranked = Leaderboard.ranked(challenge.entries)
        HStack(spacing: Theme.Spacing.m) {
            Image(systemName: "trophy.fill")
                .foregroundStyle(Theme.Brand.lagoon)
                .frame(width: 36, height: 36)
                .background(Theme.accentSoft, in: Circle())
            VStack(alignment: .leading, spacing: 2) {
                Text(challenge.title)
                    .font(.headline)
                    .foregroundStyle(Theme.textPrimary)
                Text(challenge.code)
                    .font(.caption.monospaced())
                    .foregroundStyle(Theme.textSecondary)
            }
            Spacer()
            VStack(alignment: .trailing, spacing: 2) {
                Text(L10n.tr("compete.players", ranked.count))
                    .font(.caption)
                    .foregroundStyle(Theme.textSecondary)
                if let leader = ranked.first {
                    Label(leader.isLocalPlayer ? L10n.tr("compete.you") : leader.playerName, systemImage: "crown.fill")
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(Theme.accent)
                        .lineLimit(1)
                }
            }
        }
        .trinkaCard(padding: Theme.Spacing.m)
        .accessibilityElement(children: .combine)
    }
}

/// The local player's display name for shared results.
private struct PlayerNameField: View {
    @Environment(AppModel.self) private var model
    @State private var name = ""

    var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.xs) {
            Text(L10n.tr("compete.name"))
                .font(.caption.weight(.semibold))
                .foregroundStyle(Theme.textSecondary)
            TextField(L10n.tr("compete.name.placeholder"), text: $name)
                .textContentType(.nickname)
                .submitLabel(.done)
                .padding(Theme.Spacing.m)
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.Radius.small, style: .continuous))
                .onSubmit { model.setPlayerName(name) }
                .onChange(of: name) { _, value in model.setPlayerName(value) }
        }
        .onAppear { name = model.store.settings.playerName }
    }
}

/// Pick the quiz everyone will play.
private struct CreateChallengeView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    let onCreate: (ChallengeCode) -> Void

    @State private var title = ""
    @State private var category: ScienceCategory?
    @State private var difficulty: Difficulty?
    @State private var count = 5

    var body: some View {
        NavigationStack {
            Form {
                Section {
                    TextField(L10n.tr("compete.create.titlePlaceholder"), text: $title)
                } header: {
                    Text(L10n.tr("compete.create.name"))
                }
                Section {
                    Picker(L10n.tr("explore.discipline"), selection: $category) {
                        Text(L10n.tr("explore.allCategories")).tag(ScienceCategory?.none)
                        ForEach(ScienceCategory.allCases) { Text(L10n.name(of: $0)).tag(ScienceCategory?.some($0)) }
                    }
                    Picker(L10n.tr("explore.difficulty"), selection: $difficulty) {
                        Text(L10n.tr("difficulty.mixed")).tag(Difficulty?.none)
                        ForEach(Difficulty.allCases) { Text(L10n.name(of: $0)).tag(Difficulty?.some($0)) }
                    }
                    Picker(L10n.tr("explore.length"), selection: $count) {
                        ForEach([3, 5, 10], id: \.self) { Text("\($0)").tag($0) }
                    }
                    .pickerStyle(.segmented)
                } footer: {
                    Text(L10n.tr("explore.available", available))
                }
            }
            .navigationTitle(L10n.tr("compete.create"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(L10n.tr("common.cancel")) { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button(L10n.tr("compete.create.action")) {
                        let code = model.createChallenge(title: title, category: category, difficulty: difficulty,
                                                         count: min(count, available))
                        dismiss()
                        onCreate(code)
                    }
                    .disabled(available == 0)
                }
            }
        }
        .presentationDetents([.large])
    }

    private var available: Int { model.availableQuestionCount(category: category, difficulty: difficulty) }
}

/// Enter a code (or paste an invitation / result link).
private struct JoinChallengeView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var text = ""

    var body: some View {
        NavigationStack {
            VStack(spacing: Theme.Spacing.l) {
                Text(L10n.tr("compete.join.message"))
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
                    .multilineTextAlignment(.center)
                TextField("TRK-XXXXX-XXXXX", text: $text)
                    .font(.title3.monospaced())
                    .multilineTextAlignment(.center)
                    .textInputAutocapitalization(.characters)
                    .autocorrectionDisabled()
                    .padding(Theme.Spacing.l)
                    .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
                    .submitLabel(.join)
                    .onSubmit(join)
                Button(L10n.tr("compete.join.action"), action: join)
                    .buttonStyle(.trinkaPrimary)
                    .disabled(text.trimmingCharacters(in: .whitespaces).isEmpty)
                Spacer()
            }
            .padding(Theme.Spacing.l)
            .trinkaBackground()
            .navigationTitle(L10n.tr("compete.join"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(L10n.tr("common.cancel")) { dismiss() }
                }
            }
        }
        .presentationDetents([.medium])
    }

    private func join() {
        if model.join(text) { dismiss() }
    }
}
