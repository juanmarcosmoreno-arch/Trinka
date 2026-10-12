import Foundation
import Observation
import SwiftData
import TrinkaCore
import TrinkaPersistence
import TrinkaQuiz
import TrinkaSync
import TrinkaUI

struct WatchQuizLaunch: Identifiable {
    let id = UUID()
    let session: QuizSession
}

/// State and services for the Apple Watch app.
///
/// Works fully offline: questions come from today's pack sent by the iPhone, or — if none
/// arrived — from the bundled bank using the same deterministic daily selection, so both
/// devices always show the same challenge.
@MainActor
@Observable
final class WatchModel {
    let store: ProgressStore
    var activeQuiz: WatchQuizLaunch?

    private let bank: StaticQuestionBank
    private let connectivity = ConnectivityService()
    private let packStore = ChallengePackStore()
    private let selector = QuestionSelector()
    private var pack: ChallengePack?

    init(container: ModelContainer) {
        bank = (try? SeedQuestionBank.load()) ?? StaticQuestionBank(questions: [])
        store = ProgressStore(context: container.mainContext)
        pack = packStore.load()
        L10n.language = store.settings.languageOverride ?? .preferred()

        connectivity.onMessage = { [weak self] message in self?.handle(message) }
        connectivity.activate()
    }

    /// Today's five questions, available offline.
    var todaysQuestions: [Question] {
        let now = Date()
        if let pack, pack.isValid(for: now), pack.language == L10n.language {
            return pack.questions
        }
        return selector.dailyChallenge(from: bank, language: L10n.language, date: now)
    }

    var dailyCompleted: Bool { store.snapshot.todayDailyCompleted }

    func play() {
        let questions = todaysQuestions
        guard !questions.isEmpty else { return }
        // After the daily challenge is done, replays are practice ("quick") sessions.
        let engine = QuizEngine(
            questions: questions,
            kind: dailyCompleted ? .quick : .daily,
            origin: .watch,
            language: L10n.language,
            timeLimit: store.settings.timeLimit
        )
        activeQuiz = WatchQuizLaunch(session: QuizSession(engine: engine))
    }

    func complete(_ engine: QuizEngine) -> QuizResult? {
        let context = store.scoringContext()
        guard let result = engine.result(
            currentStreak: context.streakIncludingToday,
            isFirstSessionToday: context.isFirstSessionToday,
            previouslyPlayedCategories: context.previouslyPlayedCategories
        ) else { return nil }
        store.record(result)
        // Queued and delivered when the iPhone is reachable.
        connectivity.send(session: result)
        return result
    }

    func setTimer(enabled: Bool) {
        store.settings.timerEnabled = enabled
        store.saveSettings()
    }

    func refresh() {
        store.reload()
    }

    private func handle(_ message: SyncMessage) {
        switch message {
        case let .state(pack, sessions):
            if let pack {
                self.pack = pack
                try? packStore.save(pack)
            }
            store.importSessions(sessions)
        case let .session(result):
            store.importSessions([result])
        }
    }
}
