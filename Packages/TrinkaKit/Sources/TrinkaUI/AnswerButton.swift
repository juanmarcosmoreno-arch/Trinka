import SwiftUI

/// Visual state of an answer option.
public enum AnswerState: Equatable {
    /// Selectable.
    case idle
    /// The option the user picked, and it was right.
    case correct
    /// The option the user picked, and it was wrong.
    case incorrect
    /// Not picked, but it's the right answer (revealed after answering).
    case revealedCorrect
    /// Not picked and not correct, after answering.
    case dimmed
}

/// A tappable answer option with letter, text and result styling.
/// Large touch target, works on iPhone and Apple Watch.
public struct AnswerButton: View {
    let index: Int
    let text: String
    let state: AnswerState
    var compact: Bool
    let action: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    public init(index: Int, text: String, state: AnswerState, compact: Bool = false, action: @escaping () -> Void) {
        self.index = index
        self.text = text
        self.state = state
        self.compact = compact
        self.action = action
    }

    private var letter: String { ["A", "B", "C", "D", "E", "F"][min(max(index, 0), 5)] }

    public var body: some View {
        Button(action: action) {
            HStack(spacing: compact ? Theme.Spacing.s : Theme.Spacing.m) {
                if !compact {
                    Text(letter)
                        .font(.subheadline.weight(.bold).monospaced())
                        .frame(width: 28, height: 28)
                        .background(badgeBackground, in: Circle())
                        .foregroundStyle(badgeForeground)
                }
                Text(text)
                    .font(compact ? .footnote.weight(.medium) : .body.weight(.medium))
                    .multilineTextAlignment(.leading)
                    .foregroundStyle(textColor)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .fixedSize(horizontal: false, vertical: true)
                if let icon {
                    Image(systemName: icon)
                        .font(.body.weight(.bold))
                        .foregroundStyle(state == .incorrect ? Theme.error : Theme.success)
                        .transition(.scale.combined(with: .opacity))
                }
            }
            .padding(.horizontal, compact ? Theme.Spacing.m : Theme.Spacing.l)
            .padding(.vertical, compact ? Theme.Spacing.s + 2 : Theme.Spacing.m + 2)
            .frame(minHeight: compact ? 44 : 56)
            .background(background, in: RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: Theme.Radius.medium, style: .continuous)
                    .strokeBorder(border, lineWidth: state == .idle ? 1 : 2)
            )
            .opacity(state == .dimmed ? 0.55 : 1)
            .animation(reduceMotion ? nil : .spring(response: 0.3, dampingFraction: 0.8), value: state)
        }
        .buttonStyle(.plain)
        .disabled(state != .idle)
        .accessibilityLabel("\(letter). \(text)")
        .accessibilityValue(accessibilityValue)
    }

    private var icon: String? {
        switch state {
        case .correct, .revealedCorrect: "checkmark.circle.fill"
        case .incorrect: "xmark.circle.fill"
        case .idle, .dimmed: nil
        }
    }

    private var background: Color {
        switch state {
        case .idle, .dimmed: Theme.surface
        case .correct, .revealedCorrect: Theme.successSoft
        case .incorrect: Theme.errorSoft
        }
    }

    private var border: Color {
        switch state {
        case .idle, .dimmed: Theme.separator
        case .correct, .revealedCorrect: Theme.success
        case .incorrect: Theme.error
        }
    }

    private var badgeBackground: Color {
        switch state {
        case .idle, .dimmed: Theme.surfaceMuted
        case .correct, .revealedCorrect: Theme.success
        case .incorrect: Theme.error
        }
    }

    private var badgeForeground: Color {
        state == .idle || state == .dimmed ? Theme.textSecondary : Theme.onAccent
    }

    private var textColor: Color { Theme.textPrimary }

    private var accessibilityValue: String {
        switch state {
        case .idle, .dimmed: ""
        case .correct: L10n.tr("a11y.answer.correct")
        case .incorrect: L10n.tr("a11y.answer.incorrect")
        case .revealedCorrect: L10n.tr("a11y.answer.revealed")
        }
    }
}
