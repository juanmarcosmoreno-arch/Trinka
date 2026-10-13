import SwiftUI
import TrinkaCore
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

/// TRINKA's design tokens.
///
/// The palette comes from the brand mark: ink, ivory, mint, lagoon and fjord blue —
/// calm Scandinavian tones with one clear accent per mode.
public enum Theme {
    // MARK: Brand palette (fixed)

    public enum Brand {
        public static let ink = Color(hex: 0x101418)
        public static let ivory = Color(hex: 0xF2EEE6)
        public static let mint = Color(hex: 0xA8E0CB)
        public static let lagoon = Color(hex: 0x4FA9AE)
        public static let fjord = Color(hex: 0x17607F)
        public static let deepFjord = Color(hex: 0x0E3F5C)
    }

    // MARK: Semantic colors (adapt to light / dark)

    public static let background = Color(light: 0xF7F5F0, dark: 0x0D1114)
    public static let surface = Color(light: 0xFFFFFF, dark: 0x172027)
    public static let surfaceMuted = Color(light: 0xEFEBE3, dark: 0x1F2A31)
    public static let textPrimary = Color(light: 0x101418, dark: 0xF2EEE6)
    public static let textSecondary = Color(light: 0x56616A, dark: 0xA5AFB5)
    public static let accent = Color(light: 0x17607F, dark: 0xA8E0CB)
    public static let accentSoft = Color(light: 0xDCEFEA, dark: 0x1D3A40)
    public static let onAccent = Color(light: 0xF7F5F0, dark: 0x101418)
    public static let success = Color(light: 0x2C8A68, dark: 0x7FD6B3)
    public static let successSoft = Color(light: 0xDDF2E9, dark: 0x173A2E)
    public static let error = Color(light: 0xC0533F, dark: 0xF0907C)
    public static let errorSoft = Color(light: 0xF8E3DE, dark: 0x40221D)
    public static let separator = Color(light: 0xE3DED4, dark: 0x26323A)

    /// Brand gradient (fjord → lagoon → mint) for hero surfaces.
    public static let heroGradient = LinearGradient(
        colors: [Brand.deepFjord, Brand.fjord, Brand.lagoon],
        startPoint: .bottomLeading,
        endPoint: .topTrailing
    )

    // MARK: Metrics

    public enum Radius {
        public static let small: CGFloat = 10
        public static let medium: CGFloat = 16
        public static let large: CGFloat = 24
    }

    public enum Spacing {
        public static let xs: CGFloat = 4
        public static let s: CGFloat = 8
        public static let m: CGFloat = 12
        public static let l: CGFloat = 16
        public static let xl: CGFloat = 24
        public static let xxl: CGFloat = 32
    }

    // MARK: Category colors

    public static func color(for category: ScienceCategory) -> Color {
        switch category {
        case .microbiology: Color(light: 0x2F8F86, dark: 0x7FCFC4)
        case .immunology: Color(light: 0x17607F, dark: 0x7DB8D4)
        case .genetics: Color(light: 0x3E8FA0, dark: 0x8FD0DC)
        case .neuroscience: Color(light: 0x5A6A9C, dark: 0xA8B4E0)
        case .humanPhysiology: Color(light: 0xC0684F, dark: 0xF0A48F)
        case .medicine: Color(light: 0x2D7A9E, dark: 0x86C3E0)
        case .biotechnology: Color(light: 0x4E9E7C, dark: 0x9BDCBE)
        case .nutrition: Color(light: 0x6E9448, dark: 0xB5D68F)
        case .veterinaryScience: Color(light: 0xA77B3F, dark: 0xE3BF8A)
        case .generalScience: Color(light: 0x66737D, dark: 0xB7C2CA)
        case .infectiousDiseases: Color(light: 0xB25A6B, dark: 0xF0A0B0)
        case .diagnosticMethods: Color(light: 0x3F7F8C, dark: 0x92CFDA)
        case .foodAnalysis: Color(light: 0x9A7A2E, dark: 0xE6CB7E)
        case .historyOfScience: Color(light: 0x7A6A58, dark: 0xCDBBA6)
        case .bovineMastitis: Color(light: 0x8A5A7A, dark: 0xD9A8C8)
        }
    }
}

public extension AppearanceMode {
    /// Value for `.preferredColorScheme`; `nil` follows the device.
    var colorScheme: ColorScheme? {
        switch self {
        case .system: nil
        case .light: .light
        case .dark: .dark
        }
    }
}

public extension Font {
    /// Large display titles: rounded, light-weight, generous.
    static func trinkaDisplay(_ style: Font.TextStyle = .largeTitle) -> Font {
        .system(style, design: .rounded).weight(.semibold)
    }

    static func trinkaHeadline(_ style: Font.TextStyle = .headline) -> Font {
        .system(style, design: .rounded).weight(.semibold)
    }
}

public extension Color {
    init(hex: UInt32, opacity: Double = 1) {
        self.init(
            .sRGB,
            red: Double((hex >> 16) & 0xFF) / 255,
            green: Double((hex >> 8) & 0xFF) / 255,
            blue: Double(hex & 0xFF) / 255,
            opacity: opacity
        )
    }

    /// A color that adapts to light and dark appearance. watchOS is always dark.
    init(light: UInt32, dark: UInt32) {
        #if os(watchOS)
        self.init(hex: dark)
        #elseif canImport(UIKit)
        self.init(uiColor: UIColor { traits in
            UIColor(hex: traits.userInterfaceStyle == .dark ? dark : light)
        })
        #elseif canImport(AppKit)
        self.init(nsColor: NSColor(name: nil) { appearance in
            let isDark = appearance.bestMatch(from: [.darkAqua, .aqua]) == .darkAqua
            return NSColor(hex: isDark ? dark : light)
        })
        #else
        self.init(hex: light)
        #endif
    }
}

#if canImport(UIKit) && !os(watchOS)
extension UIColor {
    convenience init(hex: UInt32) {
        self.init(
            red: CGFloat((hex >> 16) & 0xFF) / 255,
            green: CGFloat((hex >> 8) & 0xFF) / 255,
            blue: CGFloat(hex & 0xFF) / 255,
            alpha: 1
        )
    }
}
#elseif canImport(AppKit)
extension NSColor {
    convenience init(hex: UInt32) {
        self.init(
            srgbRed: CGFloat((hex >> 16) & 0xFF) / 255,
            green: CGFloat((hex >> 8) & 0xFF) / 255,
            blue: CGFloat(hex & 0xFF) / 255,
            alpha: 1
        )
    }
}
#endif
