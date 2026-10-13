import Foundation
import SwiftData
import TrinkaCore
import TrinkaQuiz

/// A finished quiz session. The full `QuizResult` (answers and XP breakdown) is stored as
/// JSON; the indexed columns support sorting and de-duplication across devices.
@Model
public final class StoredSession {
    @Attribute(.unique) public var id: UUID
    public var kindRaw: String
    public var originRaw: String
    public var startedAt: Date
    public var finishedAt: Date
    public var correctCount: Int
    public var totalCount: Int
    public var xpTotal: Int
    @Attribute(.externalStorage) public var payload: Data

    public init(result: QuizResult) throws {
        id = result.id
        kindRaw = result.kind.rawValue
        originRaw = result.origin.rawValue
        startedAt = result.startedAt
        finishedAt = result.finishedAt
        correctCount = result.correctCount
        totalCount = result.totalCount
        xpTotal = result.xp.total
        payload = try JSONEncoder().encode(result)
    }

    public var result: QuizResult? {
        try? JSONDecoder().decode(QuizResult.self, from: payload)
    }
}

/// A PubMed article the user opened from a question or from Discover.
@Model
public final class OpenedArticle {
    @Attribute(.unique) public var pmid: String
    public var title: String
    public var firstOpenedAt: Date
    public var lastOpenedAt: Date

    public init(pmid: String, title: String, openedAt: Date) {
        self.pmid = pmid
        self.title = title
        firstOpenedAt = openedAt
        lastOpenedAt = openedAt
    }
}

/// An achievement and when it was first unlocked.
@Model
public final class UnlockedAchievement {
    @Attribute(.unique) public var achievementID: String
    public var unlockedAt: Date

    public init(achievement: Achievement, unlockedAt: Date) {
        achievementID = achievement.rawValue
        self.unlockedAt = unlockedAt
    }

    public var achievement: Achievement? { Achievement(rawValue: achievementID) }
}

/// A friend challenge (shared by code) and the results collected for it.
@Model
public final class StoredChallenge {
    @Attribute(.unique) public var code: String
    public var title: String
    public var createdAt: Date
    /// JSON-encoded `[ChallengeEntry]`.
    public var entriesData: Data

    public init(code: ChallengeCode, title: String, createdAt: Date) {
        self.code = code.code
        self.title = title
        self.createdAt = createdAt
        self.entriesData = (try? JSONEncoder().encode([ChallengeEntry]())) ?? Data()
    }

    public var challengeCode: ChallengeCode? { ChallengeCode(code) }

    public var entries: [ChallengeEntry] {
        get { (try? JSONDecoder().decode([ChallengeEntry].self, from: entriesData)) ?? [] }
        set { entriesData = (try? JSONEncoder().encode(newValue)) ?? entriesData }
    }
}

/// User preferences (single row).
@Model
public final class UserSettings {
    /// `nil` follows the system language.
    public var languageOverrideRaw: String?
    /// The player's level. `nil` means "mixed" (all levels). New players start at Curious.
    public var preferredDifficultyRaw: String?
    public var timerEnabled: Bool
    public var timerSeconds: Int
    public var hapticsEnabled: Bool
    /// Light / dark / follow the system. Defaults to following the system.
    public var appearanceRaw: String = AppearanceMode.system.rawValue
    /// Name shown to friends in shared challenge results. Empty until the user sets one.
    public var playerName: String = ""
    /// Play the animated logo when the app starts.
    public var showIntro: Bool = true

    public init() {
        languageOverrideRaw = nil
        preferredDifficultyRaw = Difficulty.curious.rawValue
        timerEnabled = false
        timerSeconds = 20
        hapticsEnabled = true
        appearanceRaw = AppearanceMode.system.rawValue
        playerName = ""
        showIntro = true
    }

    public var languageOverride: AppLanguage? {
        get { languageOverrideRaw.flatMap(AppLanguage.init(rawValue:)) }
        set { languageOverrideRaw = newValue?.rawValue }
    }

    public var preferredDifficulty: Difficulty? {
        get { preferredDifficultyRaw.flatMap(Difficulty.init(rawValue:)) }
        set { preferredDifficultyRaw = newValue?.rawValue }
    }

    public var appearance: AppearanceMode {
        get { AppearanceMode(rawValue: appearanceRaw) ?? .system }
        set { appearanceRaw = newValue.rawValue }
    }

    /// Per-question limit when the optional timer is on.
    public var timeLimit: TimeInterval? { timerEnabled ? TimeInterval(timerSeconds) : nil }
}

public enum TrinkaSchema {
    public static let models: [any PersistentModel.Type] = [
        StoredSession.self, OpenedArticle.self, UnlockedAchievement.self, UserSettings.self, StoredChallenge.self,
    ]

    /// The app's model container. Data stays on the device (no CloudKit).
    public static func makeContainer(inMemory: Bool = false) throws -> ModelContainer {
        let configuration = ModelConfiguration(
            "Trinka",
            schema: Schema(models),
            isStoredInMemoryOnly: inMemory,
            cloudKitDatabase: .none
        )
        return try ModelContainer(for: Schema(models), configurations: configuration)
    }
}
