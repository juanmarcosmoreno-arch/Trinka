import AVFoundation
import SwiftUI
import TrinkaUI
import UIKit

/// The animated TRINKA logo shown when the app starts (`Resources/TrinkaIntro.mp4`).
///
/// - Plays once, then fades into the app. Tap anywhere to skip.
/// - Uses the `.ambient` audio category: respects the silent switch and doesn't stop the
///   user's music.
/// - With Reduce Motion on, shows the final frame briefly instead of the animation.
/// - The static launch screen uses the same background color (`LaunchBackground`, #F1F1F1),
///   so the transition from launch screen to video is seamless.
struct LaunchIntroView: View {
    static let background = Color(hex: 0xF1F1F1)

    let onFinish: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var player: AVPlayer?
    @State private var finished = false

    var body: some View {
        ZStack {
            Self.background.ignoresSafeArea()

            Group {
                if let player, !reduceMotion {
                    PlayerLayerView(player: player)
                } else {
                    Image("IntroFinalFrame")
                        .resizable()
                        .scaledToFit()
                }
            }
            .aspectRatio(16 / 9, contentMode: .fit)
            // Soften the video's left/right edges into the background.
            .mask(
                LinearGradient(stops: [
                    .init(color: .clear, location: 0),
                    .init(color: .black, location: 0.06),
                    .init(color: .black, location: 0.94),
                    .init(color: .clear, location: 1),
                ], startPoint: .leading, endPoint: .trailing)
            )
            .accessibilityHidden(true)

            VStack {
                Spacer()
                Text(L10n.tr("intro.skip"))
                    .font(.footnote)
                    .foregroundStyle(Color(hex: 0x101418).opacity(0.45))
                    .padding(.bottom, Theme.Spacing.xl)
            }
        }
        .contentShape(Rectangle())
        .onTapGesture(perform: finish)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("TRINKA")
        .accessibilityAddTraits(.isButton)
        .accessibilityHint(L10n.tr("intro.skip"))
        .accessibilityAction(perform: finish)
        .task { await start() }
        .onReceive(NotificationCenter.default.publisher(for: AVPlayerItem.didPlayToEndTimeNotification)) { notification in
            if (notification.object as? AVPlayerItem) === player?.currentItem { finish() }
        }
    }

    private func start() async {
        guard let url = Bundle.main.url(forResource: "TrinkaIntro", withExtension: "mp4"), !reduceMotion else {
            // No video (or Reduce Motion): show the final frame for a moment.
            try? await Task.sleep(nanoseconds: 900_000_000)
            finish()
            return
        }
        try? AVAudioSession.sharedInstance().setCategory(.ambient, mode: .default, options: [.mixWithOthers])
        let player = AVPlayer(url: url)
        player.isMuted = false
        self.player = player
        player.play()

        // Safety net: never keep the user waiting if playback stalls.
        try? await Task.sleep(nanoseconds: 8_000_000_000)
        finish()
    }

    private func finish() {
        guard !finished else { return }
        finished = true
        player?.pause()
        onFinish()
    }
}

/// `AVPlayerLayer` without playback controls.
private struct PlayerLayerView: UIViewRepresentable {
    let player: AVPlayer

    func makeUIView(context: Context) -> PlayerUIView {
        let view = PlayerUIView()
        view.playerLayer.player = player
        view.playerLayer.videoGravity = .resizeAspect
        view.backgroundColor = .clear
        return view
    }

    func updateUIView(_ view: PlayerUIView, context: Context) {
        view.playerLayer.player = player
    }

    final class PlayerUIView: UIView {
        override class var layerClass: AnyClass { AVPlayerLayer.self }
        var playerLayer: AVPlayerLayer { layer as! AVPlayerLayer }
    }
}
