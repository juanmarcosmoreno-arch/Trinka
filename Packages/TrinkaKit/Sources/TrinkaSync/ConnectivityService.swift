import Foundation
import TrinkaCore
#if canImport(WatchConnectivity)
import WatchConnectivity
#endif

/// Bridges iPhone and Apple Watch with WatchConnectivity.
///
/// Delivery strategy:
/// - **State** (today's challenge pack + recent sessions), iPhone → Watch, goes through
///   `updateApplicationContext`: only the latest copy matters and it is delivered even if the
///   watch app isn't running.
/// - **Finished sessions**, either direction, go through `transferUserInfo`: queued and
///   guaranteed, so nothing is lost while the counterpart is unreachable.
///
/// Received messages are handed to `onMessage` on the main actor. Both sides de-duplicate
/// sessions by ID, so re-deliveries are harmless.
@MainActor
public final class ConnectivityService: NSObject {
    public static let payloadKey = "trinka.sync.v1"

    /// Called on the main actor for every decoded message.
    public var onMessage: ((SyncMessage) -> Void)?

    public private(set) var isActivated = false

    public override init() {
        super.init()
    }

    /// Activates the session. Call once at launch.
    public func activate() {
        #if canImport(WatchConnectivity)
        guard WCSession.isSupported() else { return }
        let session = WCSession.default
        session.delegate = self
        session.activate()
        #endif
    }

    /// Whether a counterpart app is installed and can receive data.
    public var isCounterpartAvailable: Bool {
        #if os(iOS)
        let session = WCSession.default
        return WCSession.isSupported() && session.activationState == .activated && session.isPaired && session.isWatchAppInstalled
        #elseif os(watchOS)
        return WCSession.default.activationState == .activated && WCSession.default.isCompanionAppInstalled
        #else
        return false
        #endif
    }

    /// iPhone → Watch: publishes the latest state. Replaces any previously queued state.
    public func publishState(pack: ChallengePack?, sessions: [QuizResult]) {
        #if canImport(WatchConnectivity)
        guard isCounterpartAvailable, let data = try? SyncMessage.state(pack, sessions: sessions).encoded() else { return }
        do {
            try WCSession.default.updateApplicationContext([Self.payloadKey: data])
        } catch {
            // Application context is best effort; it's re-sent on the next change.
        }
        #endif
    }

    /// Sends a finished session to the paired device (guaranteed, queued delivery).
    public func send(session result: QuizResult) {
        #if canImport(WatchConnectivity)
        guard isCounterpartAvailable, let data = try? SyncMessage.session(result).encoded() else { return }
        WCSession.default.transferUserInfo([Self.payloadKey: data])
        #endif
    }

    fileprivate func handle(_ payload: [String: Any]) {
        guard let data = payload[Self.payloadKey] as? Data,
              let message = try? SyncMessage.decode(data) else { return }
        onMessage?(message)
    }
}

#if canImport(WatchConnectivity)
extension ConnectivityService: WCSessionDelegate {
    public nonisolated func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        let context = session.receivedApplicationContext
        Task { @MainActor in
            self.isActivated = activationState == .activated
            // Apply any state that arrived while the app wasn't running.
            if !context.isEmpty { self.handle(context) }
        }
    }

    public nonisolated func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String: Any]) {
        let data = applicationContext[Self.payloadKey] as? Data
        Task { @MainActor in
            if let data { self.handle([Self.payloadKey: data]) }
        }
    }

    public nonisolated func session(_ session: WCSession, didReceiveUserInfo userInfo: [String: Any] = [:]) {
        let data = userInfo[Self.payloadKey] as? Data
        Task { @MainActor in
            if let data { self.handle([Self.payloadKey: data]) }
        }
    }

    #if os(iOS)
    public nonisolated func sessionDidBecomeInactive(_ session: WCSession) {}

    public nonisolated func sessionDidDeactivate(_ session: WCSession) {
        // Support switching between multiple paired watches.
        session.activate()
    }
    #endif
}
#endif
