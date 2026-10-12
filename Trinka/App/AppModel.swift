import Foundation
import Observation
import SwiftData
import TrinkaCore
import TrinkaPersistence
import TrinkaPubMed
import TrinkaQuiz
import TrinkaSync
import TrinkaUI

/// A quiz being presented, with its own session state.
struct QuizLaunch: Identifiable {
    let id = UUID()
    let session: QuizSession
    let title: String
    /// Set when playing a friend challenge.
    var challenge: ChallengeCode?
}

enum AppTab: Hashable {
    case home, explore, discover, compete, progress
}

/// App-wide state and services for the iPhone app.
///
/// Views talk to this model; it coordinates the question bank, local progress, PubMed and
/// the Apple Watch connection, keeping business logic out of the views.
@MainActor
@Observable
final class AppModel {
    let bank: StaticQuestionBank
    let store: ProgressStore
    let pubMed: PubMedClient
    let articleCache = ArticleCache()
    let challenges: ChallengeStore

    /// Quiz currently on screen (drives a full-screen cover).
    var activeQuiz: QuizLaunch?
    var selectedTab: AppTab = .home
    /// Challenge to show after opening an invitation or result link.
    var openedChallenge: ChallengeCode?
    /// Message for links that can't be used (invalid, or made with a different question bank).
    var linkError: String?
    /// Bumped when the language changes so the view tree reloads its strings.
    private(set) var languageRevision = 0

    private let connectivity = ConnectivityService()
    private let selector = QuestionSelector()

    init(container: ModelContainer) {
        bank = (try? SeedQuestionBank.load()) ?? StaticQuestionBank(questions: [])
        store = ProgressStore(context: container.mainContext)
        challenges = ChallengeStore(context: container.mainContext)

        let email = (Bundle.main.object(forInfoDictionaryKey: "NCBIContactEmail") as? String).flatMap { $0.isEmpty ? nil : $0 }
        let apiKey = (Bundle.main.object(forInfoDictionaryKey: "NCBIAPIKey") as? String).flatMap { $0.isEmpty ? nil : $0 }
        pubMed = PubMedClient(configuration: .init(email: email, apiKey: apiKey))

        L10n.language = store.settings.languageOverride ?? .preferred()

        connectivity.onMessage = { [weak self] message in self?.handle(message) }
        connectivity.activate()
    }

    var language: AppLanguage { L10n.language }

    // MARK: - Language

    func setLanguageOverride(_ language: AppLanguage?) {
        store.settings.languageOverride = language
        store.saveSettings()
        L10n.language = language ?? .preferred()
        languageRevision += 1
        publishWatchState()
    }

    // MARK: - Appearance

    func setAppearance(_ mode: AppearanceMode) {
        store.settings.appearance = mode
        store.saveSettings()
    }

    // MARK: - Daily challenge

    func dailyQuestions(on date: Date = Date()) -> [Question] {
        selector.dailyChallenge(from: bank, language: language, date: date)
    }

    /// Starts today's challenge. Once completed, replays count as practice.
    func startDailyChallenge() {
        let kind: SessionKind = store.snapshot.todayDailyCompleted ? .explore : .daily
        launch(dailyQuestions(), kind: kind, title: L10n.tr("daily.title"))
    }

    /// Five questions across categories, honoring the preferred difficulty.
    func startQuickPlay() {
        startCustomQuiz(category: nil, difficulty: store.settings.preferredDifficulty, count: QuestionSelector.dailyChallengeSize)
    }

    func startCustomQuiz(category: ScienceCategory?, difficulty: Difficulty?, count: Int) {
        let questions = selector.customQuiz(
            from: bank, language: language, category: category, difficulty: difficulty,
            count: count, recentlySeen: store.recentlySeenKeys()
        )
        let title = category.map(L10n.name(of:)) ?? L10n.tr("explore.allCategories")
        launch(questions, kind: .explore, title: title)
    }

    func availableQuestionCount(category: ScienceCategory?, difficulty: Difficulty?) -> Int {
        bank.questions(in: language, category: category, difficulty: difficulty).count
    }

    private func launch(_ questions: [Question], kind: SessionKind, title: String, challenge: ChallengeCode? = nil) {
        guard !questions.isEmpty else { return }
        let engine = QuizEngine(
            questions: questions, kind: kind, origin: .iPhone, language: language,
            timeLimit: store.settings.timeLimit
        )
        activeQuiz = QuizLaunch(session: QuizSession(engine: engine), title: title, challenge: challenge)
    }

    // MARK: - Friend challenges

    /// Name shown to friends; falls back to a localized "Player".
    var playerName: String {
        let name = store.settings.playerName.trimmingCharacters(in: .whitespacesAndNewlines)
        return name.isEmpty ? L10n.tr("compete.defaultName") : name
    }

    func setPlayerName(_ name: String) {
        store.settings.playerName = String(name.prefix(30))
        store.saveSettings()
    }

    @discardableResult
    func createChallenge(title: String, category: ScienceCategory?, difficulty: Difficulty?, count: Int) -> ChallengeCode {
        let code = ChallengeCode.random(bankVersion: SeedQuestionBank.version, category: category,
                                        difficulty: difficulty, questionCount: count)
        challenges.add(code, title: title.isEmpty ? defaultTitle(for: code) : title)
        return code
    }

    func challengeQuestions(_ code: ChallengeCode) -> [Question] {
        code.questions(from: bank, bankVersion: SeedQuestionBank.version, language: language)
    }

    func startChallenge(_ code: ChallengeCode) {
        let title = challenges.challenge(for: code)?.title ?? defaultTitle(for: code)
        launch(challengeQuestions(code), kind: .challenge, title: title, challenge: code)
    }

    func defaultTitle(for code: ChallengeCode) -> String {
        code.category.map { L10n.tr("compete.defaultTitle.category", L10n.name(of: $0)) } ?? L10n.tr("compete.defaultTitle")
    }

    /// Handles `trinka://challenge` invitations and `trinka://result` shared results.
    @discardableResult
    func handle(url: URL) -> Bool {
        guard let link = FriendLink(url: url) else {
            if url.scheme == FriendLink.scheme { linkError = L10n.tr("compete.link.invalid") }
            return false
        }
        switch link {
        case let .challenge(code, title):
            guard !challengeQuestions(code).isEmpty else {
                linkError = L10n.tr("compete.link.incompatible")
                return false
            }
            challenges.add(code, title: title ?? defaultTitle(for: code))
            openedChallenge = code
        case let .result(code, entry):
            challenges.addEntry(entry, to: code, defaultTitle: defaultTitle(for: code))
            openedChallenge = code
        }
        selectedTab = .compete
        return true
    }

    /// Accepts a typed code or a pasted `trinka://` link.
    func join(_ text: String) -> Bool {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        if let url = URL(string: trimmed), url.scheme == FriendLink.scheme {
            return handle(url: url)
        }
        guard let code = ChallengeCode(trimmed) else {
            linkError = L10n.tr("compete.link.invalid")
            return false
        }
        guard !challengeQuestions(code).isEmpty else {
            linkError = L10n.tr("compete.link.incompatible")
            return false
        }
        challenges.add(code, title: defaultTitle(for: code))
        openedChallenge = code
        return true
    }

    // MARK: - Finishing

    /// Scores and stores a finished session, then shares it with the watch.
    /// Friend-challenge results are also added to that challenge's leaderboard.
    func complete(_ engine: QuizEngine, challenge: ChallengeCode? = nil) -> QuizResult? {
        let context = store.scoringContext()
        guard let result = engine.result(
            currentStreak: context.streakIncludingToday,
            isFirstSessionToday: context.isFirstSessionToday,
            previouslyPlayedCategories: context.previouslyPlayedCategories
        ) else { return nil }
        store.record(result)
        if let challenge {
            challenges.addEntry(localEntry(for: result), to: challenge, defaultTitle: defaultTitle(for: challenge))
        }
        connectivity.send(session: result)
        publishWatchState()
        return result
    }

    func localEntry(for result: QuizResult) -> ChallengeEntry {
        ChallengeEntry(playerName: playerName, correct: result.correctCount, total: result.totalCount,
                       duration: result.duration, playedAt: result.finishedAt, isLocalPlayer: true)
    }

    // MARK: - Articles

    func didOpen(_ article: ArticleReference) {
        store.markArticleOpened(article)
    }

    /// A bundled, source-verified article to feature on Home; changes daily.
    func featuredArticle(on date: Date = Date()) -> ArticleReference? {
        let articles = bank.articles.sorted { $0.pmid < $1.pmid }
        guard !articles.isEmpty else { return nil }
        let day = Calendar.current.ordinality(of: .day, in: .era, for: date) ?? 0
        return articles[day % articles.count]
    }

    /// Category a bundled article belongs to (from the questions that cite it).
    func category(of article: ArticleReference) -> ScienceCategory? {
        bank.questions(in: language).first { $0.source.pmid == article.pmid }?.category
    }

    // MARK: - Apple Watch

    func publishWatchState() {
        let today = Date()
        let pack = ChallengePack(
            id: "daily-\(Calendar.current.startOfDay(for: today).timeIntervalSince1970)-\(language.rawValue)",
            day: Calendar.current.startOfDay(for: today),
            language: language,
            questions: dailyQuestions(on: today)
        )
        connectivity.publishState(pack: pack, sessions: store.recentResults())
    }

    var isWatchAvailable: Bool { connectivity.isCounterpartAvailable }

    private func handle(_ message: SyncMessage) {
        switch message {
        case let .session(result):
            if store.importSessions([result]) { publishWatchState() }
        case let .state(_, sessions):
            // The iPhone is the source of truth for the pack; still merge any sessions.
            store.importSessions(sessions)
        }
    }

    /// Call when the app returns to the foreground (date may have changed).
    func refresh() {
        store.reload()
        publishWatchState()
    }
}
