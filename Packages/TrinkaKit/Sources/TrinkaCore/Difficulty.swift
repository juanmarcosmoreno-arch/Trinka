import Foundation

/// Question difficulty levels.
///
/// - `curious`: general scientific knowledge.
/// - `explorer`: intermediate knowledge.
/// - `researcher`: advanced questions about results and methodology.
public enum Difficulty: String, CaseIterable, Codable, Hashable, Identifiable, Comparable, Sendable {
    case curious
    case explorer
    case researcher

    public var id: String { rawValue }

    public var localizationKey: String { "difficulty.\(rawValue)" }

    /// Ordinal used for ordering and for the XP multiplier.
    public var level: Int {
        switch self {
        case .curious: 1
        case .explorer: 2
        case .researcher: 3
        }
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
