import Foundation
import Observation
import SwiftData
import TrinkaCore
import TrinkaQuiz

/// Local list of friend challenges and their leaderboards.
///
/// Everything stays on the device: invitations and results travel as `trinka://` links the
/// players share themselves (Messages, WhatsApp…). An online backend (Game Center / CloudKit)
/// can later implement automatic group leaderboards behind the same model.
@MainActor
@Observable
public final class ChallengeStore {
    public private(set) var challenges: [StoredChallenge] = []

    private let context: ModelContext
    private let now: () -> Date

    public init(context: ModelContext, now: @escaping () -> Date = Date.init) {
        self.context = context
        self.now = now
        reload()
    }

    public func challenge(for code: ChallengeCode) -> StoredChallenge? {
        challenges.first { $0.code == code.code }
    }

    /// Adds a challenge (or returns the existing one with the same code).
    @discardableResult
    public func add(_ code: ChallengeCode, title: String) -> StoredChallenge {
        if let existing = challenge(for: code) {
            if existing.title.isEmpty, !title.isEmpty { existing.title = title; save() }
            return existing
        }
        let challenge = StoredChallenge(code: code, title: title, createdAt: now())
        context.insert(challenge)
        save()
        reload()
        return challenge
    }

    /// Records a result. Results from friends are de-duplicated by name and time.
    public func addEntry(_ entry: ChallengeEntry, to code: ChallengeCode, defaultTitle: String) {
        let challenge = add(code, title: defaultTitle)
        var entries = challenge.entries
        guard !entries.contains(where: { $0.id == entry.id && $0.isLocalPlayer == entry.isLocalPlayer }) else { return }
        entries.append(entry)
        challenge.entries = entries
        save()
        reload()
    }

    public func delete(_ challenge: StoredChallenge) {
        context.delete(challenge)
        save()
        reload()
    }

    public func reload() {
        challenges = (try? context.fetch(FetchDescriptor<StoredChallenge>(sortBy: [SortDescriptor(\.createdAt, order: .reverse)]))) ?? []
    }

    private func save() {
        do {
            try context.save()
        } catch {
            assertionFailure("TRINKA: failed to save challenge: \(error)")
        }
    }
}
