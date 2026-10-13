import Foundation
import TrinkaCore

/// A shareable code that lets friends play exactly the same quiz — no accounts or servers.
///
/// The code packs the quiz settings and a random seed into 10 Crockford base-32 characters
/// (`TRK-XXXXX-XXXXX`). Anyone with the same bundled question bank rebuilds the identical
/// question list from it, each in their own language.
///
/// Bit layout (46 bits): version 4 · bank 4 · category 4 · difficulty 3 · count 4 · seed 22 · checksum 5.
public struct ChallengeCode: Hashable, Codable, Sendable, CustomStringConvertible {
    public static let formatVersion = 2
    public static let maxQuestions = 15

    public var bankVersion: Int
    public var category: ScienceCategory?
    public var difficulty: Difficulty?
    public var questionCount: Int
    public var seed: UInt32

    public init(bankVersion: Int, category: ScienceCategory?, difficulty: Difficulty?, questionCount: Int, seed: UInt32) {
        self.bankVersion = bankVersion & 0xF
        self.category = category
        self.difficulty = difficulty
        self.questionCount = max(1, min(questionCount, Self.maxQuestions))
        self.seed = seed & 0x3F_FFFF
    }

    /// A new challenge with a random seed.
    public static func random(bankVersion: Int, category: ScienceCategory?, difficulty: Difficulty?, questionCount: Int) -> ChallengeCode {
        ChallengeCode(bankVersion: bankVersion, category: category, difficulty: difficulty,
                      questionCount: questionCount, seed: UInt32.random(in: 0...0x3F_FFFF))
    }

    // MARK: Encoding

    private static let alphabet = Array("0123456789ABCDEFGHJKMNPQRSTVWXYZ")

    public var code: String {
        let categoryIndex = category.flatMap { ScienceCategory.allCases.firstIndex(of: $0) }.map { $0 + 1 } ?? 0
        let difficultyIndex = difficulty.map(\.level) ?? 0
        var payload: UInt64 = UInt64(Self.formatVersion & 0xF)
        payload = payload << 4 | UInt64(bankVersion & 0xF)
        payload = payload << 4 | UInt64(categoryIndex)
        payload = payload << 3 | UInt64(difficultyIndex)
        payload = payload << 4 | UInt64(questionCount & 0xF)
        payload = payload << 22 | UInt64(seed)
        let value = payload << 5 | UInt64(Self.checksum(payload))

        var characters: [Character] = []
        for index in (0..<10).reversed() {
            characters.append(Self.alphabet[Int((value >> (UInt64(index) * 5)) & 0x1F)])
        }
        return "TRK-" + String(characters[0..<5]) + "-" + String(characters[5..<10])
    }

    public var description: String { code }

    /// Parses a code, tolerating lowercase, missing prefix/dashes and the usual look-alikes (O/0, I/L/1).
    public init?(_ text: String) {
        var cleaned = text.uppercased().filter { !$0.isWhitespace && $0 != "-" }
        if cleaned.hasPrefix("TRK") { cleaned.removeFirst(3) }
        cleaned = String(cleaned.map { character -> Character in
            switch character {
            case "O": "0"
            case "I", "L": "1"
            default: character
            }
        })
        guard cleaned.count == 10 else { return nil }

        var value: UInt64 = 0
        for character in cleaned {
            guard let digit = Self.alphabet.firstIndex(of: character) else { return nil }
            value = value << 5 | UInt64(digit)
        }
        let payload = value >> 5
        guard UInt8(value & 0x1F) == Self.checksum(payload) else { return nil }

        let seed = UInt32(payload & 0x3F_FFFF)
        let count = Int((payload >> 22) & 0xF)
        let difficultyIndex = Int((payload >> 26) & 0x7)
        let categoryIndex = Int((payload >> 29) & 0xF)
        let bank = Int((payload >> 33) & 0xF)
        let version = Int((payload >> 37) & 0xF)

        guard version == Self.formatVersion, count > 0,
              categoryIndex <= ScienceCategory.allCases.count,
              difficultyIndex <= Difficulty.allCases.count else { return nil }
        self.init(
            bankVersion: bank,
            category: categoryIndex == 0 ? nil : ScienceCategory.allCases[categoryIndex - 1],
            difficulty: difficultyIndex == 0 ? nil : Difficulty(level: difficultyIndex),
            questionCount: count,
            seed: seed
        )
    }

    /// 5-bit checksum so typos are caught instead of silently loading another quiz.
    private static func checksum(_ payload: UInt64) -> UInt8 {
        var hash: UInt64 = 0xcbf2_9ce4_8422_2325
        for shift in stride(from: 0, to: 64, by: 8) {
            hash ^= (payload >> UInt64(shift)) & 0xFF
            hash = hash &* 0x0000_0100_0000_01b3
        }
        return UInt8(hash & 0x1F)
    }

    // MARK: Questions

    /// The challenge's questions in `language`.
    ///
    /// Selection works on translation keys, so friends playing in English and Spanish get the
    /// same questions. Returns an empty list if the bank version doesn't match.
    public func questions(from bank: QuestionBank, bankVersion currentBankVersion: Int, language: AppLanguage) -> [Question] {
        guard bankVersion == currentBankVersion & 0xF else { return [] }
        // Reference pool: English, which every seed question has.
        let keys = bank.questions(in: .en, category: category, difficulty: difficulty)
            .map(\.translationKey)
            .sorted()
        var generator = SeededGenerator(seed: UInt64(seed) | 0x5452_4B00_0000_0000)
        let chosen = keys.shuffled(using: &generator).prefix(questionCount)
        return chosen.compactMap { bank.question(withTranslationKey: $0, language: language) }
    }

    /// Link that opens the challenge in TRINKA.
    public func inviteURL(title: String?) -> URL {
        var components = URLComponents()
        components.scheme = FriendLink.scheme
        components.host = "challenge"
        components.queryItems = [URLQueryItem(name: "code", value: code)]
            + (title.map { [URLQueryItem(name: "title", value: $0)] } ?? [])
        return components.url!
    }
}

/// One player's result in a friend challenge.
public struct ChallengeEntry: Codable, Hashable, Identifiable, Sendable {
    public var id: String { "\(playerName.lowercased())|\(playedAt.timeIntervalSince1970)" }
    public var playerName: String
    public var correct: Int
    public var total: Int
    public var duration: TimeInterval
    public var playedAt: Date
    public var isLocalPlayer: Bool

    public init(playerName: String, correct: Int, total: Int, duration: TimeInterval, playedAt: Date, isLocalPlayer: Bool) {
        self.playerName = playerName
        self.correct = correct
        self.total = total
        self.duration = duration
        self.playedAt = playedAt
        self.isLocalPlayer = isLocalPlayer
    }

    /// Link a player shares so others can add this result to their leaderboard.
    public func resultURL(for code: ChallengeCode) -> URL {
        var components = URLComponents()
        components.scheme = FriendLink.scheme
        components.host = "result"
        components.queryItems = [
            URLQueryItem(name: "code", value: code.code),
            URLQueryItem(name: "name", value: playerName),
            URLQueryItem(name: "correct", value: String(correct)),
            URLQueryItem(name: "total", value: String(total)),
            URLQueryItem(name: "seconds", value: String(Int(duration.rounded()))),
            URLQueryItem(name: "at", value: String(Int(playedAt.timeIntervalSince1970))),
        ]
        return components.url!
    }
}

/// Ranking: most correct answers first; equal scores are separated by time.
public enum Leaderboard {
    public static func ranked(_ entries: [ChallengeEntry]) -> [ChallengeEntry] {
        // Keep each player's best attempt only.
        var best: [String: ChallengeEntry] = [:]
        for entry in entries {
            let key = entry.isLocalPlayer ? "\u{0}me" : entry.playerName.lowercased()
            if let current = best[key], !isBetter(entry, than: current) { continue }
            best[key] = entry
        }
        return best.values.sorted { isBetter($0, than: $1) }
    }

    static func isBetter(_ lhs: ChallengeEntry, than rhs: ChallengeEntry) -> Bool {
        if lhs.correct != rhs.correct { return lhs.correct > rhs.correct }
        if lhs.duration != rhs.duration { return lhs.duration < rhs.duration }
        return lhs.playedAt < rhs.playedAt
    }
}

/// `trinka://` links for challenge invitations and shared results.
public enum FriendLink: Equatable, Sendable {
    public static let scheme = "trinka"

    case challenge(ChallengeCode, title: String?)
    case result(ChallengeCode, ChallengeEntry)

    public init?(url: URL) {
        guard url.scheme?.lowercased() == Self.scheme,
              let components = URLComponents(url: url, resolvingAgainstBaseURL: false) else { return nil }
        let items = Dictionary((components.queryItems ?? []).map { ($0.name, $0.value ?? "") }, uniquingKeysWith: { first, _ in first })
        guard let code = items["code"].flatMap(ChallengeCode.init) else { return nil }

        switch url.host?.lowercased() {
        case "challenge":
            let title = items["title"].flatMap { $0.isEmpty ? nil : String($0.prefix(60)) }
            self = .challenge(code, title: title)
        case "result":
            guard let name = items["name"].map({ String($0.trimmingCharacters(in: .whitespacesAndNewlines).prefix(30)) }), !name.isEmpty,
                  let correct = items["correct"].flatMap(Int.init), let total = items["total"].flatMap(Int.init),
                  total == code.questionCount, (0...total).contains(correct),
                  let seconds = items["seconds"].flatMap(Int.init), seconds >= 0 else { return nil }
            let playedAt = items["at"].flatMap(TimeInterval.init).map(Date.init(timeIntervalSince1970:)) ?? Date()
            self = .result(code, ChallengeEntry(playerName: name, correct: correct, total: total,
                                                duration: TimeInterval(seconds), playedAt: playedAt, isLocalPlayer: false))
        default:
            return nil
        }
    }
}
