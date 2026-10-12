import Foundation
import TrinkaCore

/// Localized strings for TRINKA (English and Spanish).
///
/// UI and question content always share one language: the user's override from Settings,
/// or the best match for the system language. Adding a language means adding an `.lproj`
/// folder here, a case to `AppLanguage`, and translated seed questions.
public enum L10n {
    /// Active language. Set at launch and when the user changes it in Settings.
    public nonisolated(unsafe) static var language: AppLanguage = .preferred() {
        didSet { cachedBundle = nil }
    }

    private nonisolated(unsafe) static var cachedBundle: Bundle?

    private static var bundle: Bundle {
        if let cachedBundle { return cachedBundle }
        let resolved = Bundle.module.path(forResource: language.rawValue, ofType: "lproj").flatMap(Bundle.init(path:)) ?? .module
        cachedBundle = resolved
        return resolved
    }

    /// Localized string for `key`.
    public static func tr(_ key: String) -> String {
        bundle.localizedString(forKey: key, value: nil, table: nil)
    }

    /// Localized format string for `key`, filled with `arguments`.
    public static func tr(_ key: String, _ arguments: CVarArg...) -> String {
        String(format: tr(key), locale: locale, arguments: arguments)
    }

    public static var locale: Locale { Locale(identifier: language.rawValue) }

    // MARK: Domain names

    public static func name(of category: ScienceCategory) -> String { tr(category.localizationKey) }
    public static func name(of difficulty: Difficulty) -> String { tr(difficulty.localizationKey) }
    public static func title(of achievement: Achievement) -> String { tr(achievement.titleKey) }
    public static func detail(of achievement: Achievement) -> String { tr(achievement.detailKey) }

    // MARK: Formatting

    public static func percent(_ value: Double) -> String {
        value.formatted(.percent.precision(.fractionLength(0)).locale(locale))
    }

    public static func duration(_ interval: TimeInterval) -> String {
        let seconds = Int(interval.rounded())
        return String(format: "%d:%02d", seconds / 60, seconds % 60)
    }
}
