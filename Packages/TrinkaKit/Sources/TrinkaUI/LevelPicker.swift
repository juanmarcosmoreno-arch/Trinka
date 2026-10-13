import SwiftUI
import TrinkaCore

/// Five-step level selector, from Basic to Expert, drawn as rising bars.
/// Optionally offers "Mixed" (all levels), represented by `nil`.
public struct LevelPicker: View {
    @Binding private var selection: Difficulty?
    private let allowsMixed: Bool

    public init(selection: Binding<Difficulty?>, allowsMixed: Bool = false) {
        _selection = selection
        self.allowsMixed = allowsMixed
    }

    public var body: some View {
        VStack(alignment: .leading, spacing: Theme.Spacing.m) {
            HStack(alignment: .bottom, spacing: Theme.Spacing.s) {
                ForEach(Difficulty.allCases) { level in
                    Button {
                        selection = level
                    } label: {
                        VStack(spacing: Theme.Spacing.xs) {
                            RoundedRectangle(cornerRadius: 5, style: .continuous)
                                .fill(isFilled(level) ? Theme.accent : Theme.surfaceMuted)
                                .frame(height: 14 + CGFloat(level.level) * 8)
                            Text(L10n.name(of: level))
                                .font(.caption2.weight(selection == level ? .bold : .medium))
                                .foregroundStyle(selection == level ? Theme.textPrimary : Theme.textSecondary)
                                .lineLimit(1)
                                .minimumScaleFactor(0.7)
                        }
                        .frame(maxWidth: .infinity)
                        .contentShape(Rectangle())
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel(L10n.name(of: level))
                    .accessibilityAddTraits(selection == level ? .isSelected : [])
                }
            }
            .frame(height: 70, alignment: .bottom)
            .animation(.easeOut(duration: 0.2), value: selection)

            HStack(alignment: .firstTextBaseline) {
                Text(L10n.tr(selection.map { "difficulty.\($0.rawValue).detail" } ?? "difficulty.mixed.detail"))
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)
                    .fixedSize(horizontal: false, vertical: true)
                Spacer(minLength: Theme.Spacing.s)
                if allowsMixed {
                    Button {
                        selection = nil
                    } label: {
                        Text(L10n.tr("difficulty.mixed"))
                            .font(.caption.weight(.semibold))
                            .padding(.horizontal, Theme.Spacing.m)
                            .padding(.vertical, Theme.Spacing.xs + 2)
                            .foregroundStyle(selection == nil ? Theme.onAccent : Theme.accent)
                            .background(selection == nil ? Theme.accent : Theme.accentSoft, in: Capsule())
                    }
                    .buttonStyle(.plain)
                    .accessibilityAddTraits(selection == nil ? .isSelected : [])
                }
            }
        }
    }

    /// Bars up to the selected level are filled; with "Mixed" all are filled.
    private func isFilled(_ level: Difficulty) -> Bool {
        guard let selection else { return true }
        return level.level <= selection.level
    }
}
