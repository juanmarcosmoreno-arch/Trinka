import SwiftUI
#if canImport(UIKit)
import UIKit
#endif

/// The TRINKA brand mark — an ivory sphere, a mint wave and a fjord-blue droplet.
///
/// Drawn as vectors so it stays crisp from watch complications to the iPad. If the app's asset
/// catalog contains an image named `TrinkaMark` (the official artwork, see `Design/Brand`),
/// that image is used instead.
public struct TrinkaMark: View {
    @Environment(\.colorScheme) private var colorScheme

    public init() {}

    public var body: some View {
        #if canImport(UIKit)
        if UIImage(named: "TrinkaMark") != nil {
            Image("TrinkaMark").resizable().scaledToFit()
        } else {
            vectorMark
        }
        #else
        vectorMark
        #endif
    }

    private var vectorMark: some View {
        GeometryReader { proxy in
            let side = min(proxy.size.width, proxy.size.height)
            ZStack {
                // On light backgrounds the ivory sphere gets a soft shade so it keeps its shape,
                // matching the light-mode version of the logo.
                Circle()
                    .fill(colorScheme == .dark
                          ? AnyShapeStyle(Theme.Brand.ivory)
                          : AnyShapeStyle(LinearGradient(colors: [Color(hex: 0xF6F3EC), Color(hex: 0xE4DFD3)],
                                                         startPoint: .topLeading, endPoint: .bottomTrailing)))
                    .shadow(color: .black.opacity(colorScheme == .dark ? 0 : 0.08), radius: side * 0.03, y: side * 0.01)
                    .frame(width: side * 0.64, height: side * 0.64)
                    .position(x: side * 0.33, y: side * 0.33)
                MarkShape(kind: .droplet)
                    .fill(LinearGradient(colors: [Color(hex: 0x2A7F9A), Theme.Brand.fjord], startPoint: .top, endPoint: .bottom))
                MarkShape(kind: .wave)
                    .fill(LinearGradient(colors: [Theme.Brand.lagoon, Theme.Brand.mint], startPoint: .leading, endPoint: .trailing))
                    .opacity(0.86)
            }
            .frame(width: side, height: side)
        }
        .aspectRatio(1, contentMode: .fit)
        .accessibilityHidden(true)
    }
}

/// "TRINKA" wordmark, with the crossbar-less A of the logo.
public struct TrinkaWordmark: View {
    private let size: CGFloat
    private let color: Color

    public init(size: CGFloat = 28, color: Color = Theme.textPrimary) {
        self.size = size
        self.color = color
    }

    public var body: some View {
        Text(verbatim: "TRINK\u{039B}")
            .font(.system(size: size, weight: .regular, design: .default))
            .tracking(size * 0.32)
            .foregroundStyle(color)
            .accessibilityLabel("TRINKA")
    }
}

/// Mark + wordmark lockup.
public struct TrinkaLogo: View {
    public enum Layout { case horizontal, vertical }

    private let layout: Layout
    private let height: CGFloat

    public init(layout: Layout = .horizontal, height: CGFloat = 36) {
        self.layout = layout
        self.height = height
    }

    public var body: some View {
        Group {
            switch layout {
            case .horizontal:
                HStack(spacing: height * 0.35) {
                    TrinkaMark().frame(width: height, height: height)
                    TrinkaWordmark(size: height * 0.62)
                }
            case .vertical:
                VStack(spacing: height * 0.18) {
                    TrinkaMark().frame(width: height, height: height)
                    TrinkaWordmark(size: height * 0.3)
                }
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("TRINKA")
    }
}

/// Bézier geometry of the mark, in unit coordinates.
/// Shared with `Scripts/render_brand_icons.py`, which renders the interim app icons.
struct MarkShape: Shape {
    enum Kind { case wave, droplet }

    let kind: Kind

    func path(in rect: CGRect) -> Path {
        let side = min(rect.width, rect.height)
        func p(_ x: CGFloat, _ y: CGFloat) -> CGPoint { CGPoint(x: rect.minX + x * side, y: rect.minY + y * side) }

        var path = Path()
        switch kind {
        case .wave:
            path.move(to: p(0.45, 0.66))
            path.addCurve(to: p(0.62, 0.17), control1: p(0.52, 0.45), control2: p(0.50, 0.20))
            path.addCurve(to: p(0.80, 0.27), control1: p(0.70, 0.16), control2: p(0.74, 0.26))
            path.addCurve(to: p(0.99, 0.48), control1: p(0.92, 0.28), control2: p(1.00, 0.38))
            path.addCurve(to: p(0.80, 0.66), control1: p(0.98, 0.60), control2: p(0.90, 0.68))
            path.addCurve(to: p(0.62, 0.60), control1: p(0.72, 0.65), control2: p(0.68, 0.58))
            path.addCurve(to: p(0.45, 0.66), control1: p(0.55, 0.62), control2: p(0.50, 0.64))
        case .droplet:
            path.move(to: p(0.61, 0.61))
            path.addCurve(to: p(0.55, 0.70), control1: p(0.57, 0.63), control2: p(0.55, 0.66))
            path.addCurve(to: p(0.34, 1.00), control1: p(0.56, 0.90), control2: p(0.46, 1.00))
            path.addCurve(to: p(0.14, 0.80), control1: p(0.22, 1.00), control2: p(0.14, 0.91))
            path.addCurve(to: p(0.34, 0.61), control1: p(0.14, 0.69), control2: p(0.22, 0.64))
            path.addCurve(to: p(0.61, 0.61), control1: p(0.45, 0.58), control2: p(0.55, 0.57))
        }
        path.closeSubpath()
        return path
    }
}
