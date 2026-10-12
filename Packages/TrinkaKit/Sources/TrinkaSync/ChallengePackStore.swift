import Foundation
import TrinkaCore

/// Persists the most recent `ChallengePack` received from the iPhone so the watch can play
/// it without a connection.
public struct ChallengePackStore: Sendable {
    private let fileURL: URL

    public init(directory: URL? = nil) {
        let base = directory
            ?? FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
            ?? FileManager.default.temporaryDirectory
        fileURL = base.appendingPathComponent("ChallengePack.json")
    }

    public func save(_ pack: ChallengePack) throws {
        try FileManager.default.createDirectory(at: fileURL.deletingLastPathComponent(), withIntermediateDirectories: true)
        try JSONEncoder().encode(pack).write(to: fileURL, options: .atomic)
    }

    public func load() -> ChallengePack? {
        guard let data = try? Data(contentsOf: fileURL) else { return nil }
        return try? JSONDecoder().decode(ChallengePack.self, from: data)
    }
}
