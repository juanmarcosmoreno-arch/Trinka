import Foundation

/// Question difficulty levels, from very basic to expert.
///
/// - `beginner`: core concepts anyone can answer (what a study was about).
/// - `curious`: general scientific knowledge.
/// - `explorer`: intermediate knowledge; key results of a study.
/// - `researcher`: advanced questions about results and methodology.
/// - `expert`: specialist detail — exact figures, methods and mechanisms.
public enum Difficulty: String, CaseIterable, Codable, Hashable, Identifiable, Comparable, Sendable {
    case beginner
    case curious
    case explorer
    case researcher
    case expert

    public var id: String { rawValue }

    public var localizationKey: String { "difficulty.\(rawValue)" }

    /// 1 (beginner) … 5 (expert). Used for ordering and the XP multiplier.
    public var level: Int {
        switch self {
        case .beginner: 1
        case .curious: 2
        case .explorer: 3
        case .researcher: 4
        case .expert: 5
        }
    }

    public init?(level: Int) {
        guard let match = Difficulty.allCases.first(where: { $0.level == level }) else { return nil }
        self = match
    }

    public static func < (lhs: Difficulty, rhs: Difficulty) -> Bool { lhs.level < rhs.level }
}

/// Languages TRINKA content and UI are available in.
public enum AppLanguage: String, CaseIterable, Codable, Hashable, Identifiable, Sendable {
    case en
    case es

    public var id: String { rawValue }

    /// Best match for the user's preferred languages, falling back to English.
    public static func preferred(from identifiers: [String] = Locale.preferredLanguages) -> AppLanguage {
        for identifier in identifiers {
            let code = String(identifier.prefix(2)).lowercased()
            if let match = AppLanguage(rawValue: code) { return match }
        }
        return .en
    }
}

/// Light/dark appearance preference. `system` follows the device setting.
public enum AppearanceMode: String, CaseIterable, Codable, Hashable, Identifiable, Sendable {
    case system
    case light
    case dark

    public var id: String { rawValue }
    public var localizationKey: String { "appearance.\(rawValue)" }

    public var symbolName: String {
        switch self {
        case .system: "circle.lefthalf.filled"
        case .light: "sun.max"
        case .dark: "moon"
        }
    }
}
