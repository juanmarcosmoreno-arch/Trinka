import SwiftUI
import TrinkaCore

// MARK: - Surfaces

public struct CardModifier: ViewModifier {
    var padding: CGFloat

    public func body(content: Content) -> some View {
        content
            .padding(padding)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.Radius.large, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: Theme.Radius.large, style: .continuous)
                    .strokeBorder(Theme.separator, lineWidth: 0.5)
            )
    }
}

public extension View {
    /// Rounded, softly outlined card.
    func trinkaCard(padding: CGFloat = Theme.Spacing.l) -> some View {
        modifier(CardModifier(padding: padding))
    }

    /// Screen background used across the iPhone app.
    func trinkaBackground() -> some View {
        background(Theme.background.ignoresSafeArea())
    }
}

// MARK: - Buttons

/// Filled, full-width primary action.
public struct PrimaryButtonStyle: ButtonStyle {
    @Environment(\.isEnabled) private var isEnabled

    public init() {}

    public func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.trinkaHeadline())
            .frame(maxWidth: .infinity)
            .padding(.vertical, Theme.Spacing.l)
            .foregroundStyle(Theme.onAccent)
            .background(Theme.accent.opacity(isEnabled ? 1 : 0.4),
                        in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
            .scaleEffect(configuration.isPressed ? 0.98 : 1)
            .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}

/// Tinted secondary action.
public struct SecondaryButtonStyle: ButtonStyle {
    public init() {}

    public func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.trinkaHeadline(.subheadline))
            .frame(maxWidth: .infinity)
            .padding(.vertical, Theme.Spacing.m)
            .foregroundStyle(Theme.accent)
            .background(Theme.accentSoft, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
            .opacity(configuration.isPressed ? 0.7 : 1)
    }
}

public extension ButtonStyle where Self == PrimaryButtonStyle {
    static var trinkaPrimary: PrimaryButtonStyle { PrimaryButtonStyle() }
}

public extension ButtonStyle where Self == SecondaryButtonStyle {
    static var trinkaSecondary: SecondaryButtonStyle { SecondaryButtonStyle() }
}

// MARK: - Category

/// Round icon in the category's color.
public struct CategoryIcon: View {
    let category: ScienceCategory
    var size: CGFloat

    public init(_ category: ScienceCategory, size: CGFloat = 36) {
        self.category = category
        self.size = size
    }

    public var body: some View {
        Image(systemName: category.symbolName)
            .font(.system(size: size * 0.45, weight: .semibold))
            .foregroundStyle(Theme.color(for: category))
            .frame(width: size, height: size)
            .background(Theme.color(for: category).opacity(0.14), in: Circle())
            .accessibilityHidden(true)
    }
}

/// Compact capsule label: icon + category name.
public struct CategoryChip: View {
    let category: ScienceCategory
    var isSelected: Bool

    public init(_ category: ScienceCategory, isSelected: Bool = false) {
        self.category = category
        self.isSelected = isSelected
    }

    public var body: some View {
        Label(L10n.name(of: category), systemImage: category.symbolName)
            .font(.footnote.weight(.semibold))
            .lineLimit(1)
            .padding(.horizontal, Theme.Spacing.m)
            .padding(.vertical, Theme.Spacing.s)
            .foregroundStyle(isSelected ? Theme.onAccent : Theme.color(for: category))
            .background(isSelected ? Theme.color(for: category) : Theme.color(for: category).opacity(0.12), in: Capsule())
            .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}

/// Difficulty indicator: 1–3 filled dots plus the level name.
public struct DifficultyBadge: View {
    let difficulty: Difficulty

    public init(_ difficulty: Difficulty) {
        self.difficulty = difficulty
    }

    public var body: some View {
        HStack(spacing: 4) {
            ForEach(1...3, id: \.self) { level in
                Circle()
                    .fill(level <= difficulty.level ? Theme.accent : Theme.separator)
                    .frame(width: 6, height: 6)
            }
            Text(L10n.name(of: difficulty))
                .font(.caption.weight(.medium))
                .foregroundStyle(Theme.textSecondary)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(L10n.tr("a11y.difficulty", L10n.name(of: difficulty)))
    }
}

// MARK: - Stats

/// Small labeled metric.
public struct StatTile: View {
    let title: String
    let value: String
    let systemImage: String
    var tint: Color

    public init(title: String, value: String, systemImage: String, tint: Color = Theme.accent) {
        self.title = title
        self.value = value
        self.systemImage = systemImage
        self.tint = tint
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.s) {
            Image(systemName: systemImage)
                .font(.body.weight(.semibold))
                .foregroundStyle(tint)
            Text(value)
                .font(.trinkaDisplay(.title2))
                .foregroundStyle(Theme.textPrimary)
                .contentTransition(.numericText())
                .lineLimit(1)
                .minimumScaleFactor(0.6)
            Text(title)
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
                .lineLimit(2)
        }
        .trinkaCard(padding: Theme.Spacing.m)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("\(title): \(value)")
    }
}

/// Circular progress indicator.
public struct ProgressRing: View {
    let progress: Double
    var lineWidth: CGFloat
    var tint: Color

    public init(progress: Double, lineWidth: CGFloat = 8, tint: Color = Theme.accent) {
        self.progress = progress
        self.lineWidth = lineWidth
        self.tint = tint
    }

    public var body: some View {
        ZStack {
            Circle().stroke(tint.opacity(0.18), lineWidth: lineWidth)
            Circle()
                .trim(from: 0, to: max(0, min(1, progress)))
                .stroke(tint, style: StrokeStyle(lineWidth: lineWidth, lineCap: .round))
                .rotationEffect(.degrees(-90))
                .animation(.easeOut(duration: 0.5), value: progress)
        }
        .accessibilityElement()
        .accessibilityValue(L10n.percent(progress))
    }
}

/// Flame + streak count.
public struct StreakBadge: View {
    let days: Int

    public init(days: Int) {
        self.days = days
    }

    public var body: some View {
        Label {
            Text(L10n.tr("streak.days", days))
                .font(.subheadline.weight(.semibold))
                .contentTransition(.numericText())
        } icon: {
            Image(systemName: days > 0 ? "flame.fill" : "flame")
                .foregroundStyle(days > 0 ? Theme.error : Theme.textSecondary)
                .symbolEffect(.bounce, value: days)
        }
        .foregroundStyle(Theme.textPrimary)
        .accessibilityElement(children: .combine)
    }
}

/// Section title used on iPhone screens.
public struct SectionHeader: View {
    let title: String
    var subtitle: String?

    public init(_ title: String, subtitle: String? = nil) {
        self.title = title
        self.subtitle = subtitle
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: 2) {
            Text(title)
                .font(.trinkaHeadline(.title3))
                .foregroundStyle(Theme.textPrimary)
                .accessibilityAddTraits(.isHeader)
            if let subtitle {
                Text(subtitle)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

/// Neutral message for empty, error and offline states.
public struct MessageView: View {
    let systemImage: String
    let title: String
    let message: String

    public init(systemImage: String, title: String, message: String) {
        self.systemImage = systemImage
        self.title = title
        self.message = message
    }

    public var body: some View {
        VStack(spacing: Theme.Spacing.m) {
            Image(systemName: systemImage)
                .font(.system(size: 36, weight: .light))
                .foregroundStyle(Theme.accent)
            Text(title)
                .font(.trinkaHeadline())
                .foregroundStyle(Theme.textPrimary)
            Text(message)
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
                .multilineTextAlignment(.center)
        }
        .padding(Theme.Spacing.xl)
        .frame(maxWidth: .infinity)
        .accessibilityElement(children: .combine)
    }
}
