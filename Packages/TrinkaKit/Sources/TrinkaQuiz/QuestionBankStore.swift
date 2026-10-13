import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
import TrinkaCore

/// Describes the newest published question bank (`Content/manifest.json` in the repository).
public struct QuestionBankManifest: Codable, Equatable, Sendable {
    /// Content version; must equal the "version" inside the bank file.
    public var version: Int
    /// Bank file name, relative to the manifest's folder (e.g. "questions-4.json").
    public var file: String

    public init(version: Int, file: String) {
        self.version = version
        self.file = file
    }
}

/// Keeps the question bank up to date without an App Store release.
///
/// The app ships with `SeedQuestions.json`. When a newer bank is published (a manifest plus a
/// bank file on a static host), `update(from:currentVersion:)` downloads it, validates every
/// question exactly like the bundled bank (verified source + verbatim excerpt) and stores it.
/// `loadBest(bundled:)` then prefers it on the next launch, so the daily challenge never changes
/// mid-day. Any failure — offline, bad file, older version — leaves the current bank in place.
public actor QuestionBankStore {
    public typealias Fetch = @Sendable (URL) async throws -> Data

    public enum UpdateError: Error, Equatable {
        case versionMismatch(manifest: Int, file: Int)
        case invalidQuestions(count: Int)
        case missingLanguage(AppLanguage)
        case invalidFileName
    }

    private let fileURL: URL
    private let fetch: Fetch

    /// - Parameters:
    ///   - directory: Where the downloaded bank is kept (default: Application Support/TRINKA).
    ///   - fetch: Downloads a URL; injectable for tests.
    public init(directory: URL? = nil, fetch: Fetch? = nil) {
        let base = directory
            ?? FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first?
                .appendingPathComponent("TRINKA", isDirectory: true)
            ?? FileManager.default.temporaryDirectory
        self.fileURL = base.appendingPathComponent("QuestionBank.json")
        self.fetch = fetch ?? { url in
            var request = URLRequest(url: url)
            request.cachePolicy = .reloadIgnoringLocalCacheData
            request.timeoutInterval = 30
            let (data, response) = try await URLSession.shared.data(for: request)
            if let http = response as? HTTPURLResponse, !(200..<300).contains(http.statusCode) {
                throw URLError(.badServerResponse)
            }
            return data
        }
    }

    /// The downloaded bank if it is newer than `bundled` and still loads cleanly; otherwise `bundled`.
    public nonisolated func loadBest(bundled: StaticQuestionBank) -> StaticQuestionBank {
        guard let data = try? Data(contentsOf: fileURL),
              let stored = try? Self.accept(data, expectedVersion: nil),
              stored.version > bundled.version else { return bundled }
        return stored
    }

    /// Checks `baseURL/manifest.json` and, if it announces a version newer than `currentVersion`,
    /// downloads, validates and stores that bank.
    /// - Returns: The version stored, or `nil` when no newer bank is published.
    @discardableResult
    public func update(from baseURL: URL, currentVersion: Int) async throws -> Int? {
        let manifestData = try await fetch(baseURL.appendingPathComponent("manifest.json"))
        let manifest = try JSONDecoder().decode(QuestionBankManifest.self, from: manifestData)
        guard manifest.version > currentVersion, manifest.version > storedVersion() else { return nil }
        // Only a plain file name next to the manifest is accepted.
        guard !manifest.file.isEmpty, !manifest.file.contains("/"), !manifest.file.contains("..") else {
            throw UpdateError.invalidFileName
        }
        let data = try await fetch(baseURL.appendingPathComponent(manifest.file))
        let bank = try Self.accept(data, expectedVersion: manifest.version)
        try FileManager.default.createDirectory(at: fileURL.deletingLastPathComponent(), withIntermediateDirectories: true)
        try data.write(to: fileURL, options: .atomic)
        return bank.version
    }

    /// Content base URL from the `TrinkaQuestionBankBase` Info.plist key (host and path, no scheme).
    public static func configuredBaseURL(bundle: Bundle = .main) -> URL? {
        let value = (bundle.object(forInfoDictionaryKey: "TrinkaQuestionBankBase") as? String)?
            .trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
        guard !value.isEmpty, !value.hasPrefix("$(") else { return nil }
        return URL(string: value.hasPrefix("https://") ? value : "https://\(value)")
    }

    /// Removes the downloaded bank (e.g. after an app update ships a newer bundled bank).
    public func reset() {
        try? FileManager.default.removeItem(at: fileURL)
    }

    private func storedVersion() -> Int {
        guard let data = try? Data(contentsOf: fileURL),
              let bank = try? Self.accept(data, expectedVersion: nil) else { return 0 }
        return bank.version
    }

    /// Loads `data` as a bank and applies the same integrity rules as the bundled bank:
    /// every question must pass `QuestionValidator`, and both languages must be present.
    static func accept(_ data: Data, expectedVersion: Int?) throws -> StaticQuestionBank {
        let bank = try SeedQuestionBank.load(from: data)
        if let expectedVersion, bank.version != expectedVersion {
            throw UpdateError.versionMismatch(manifest: expectedVersion, file: bank.version)
        }
        guard bank.rejected.isEmpty else { throw UpdateError.invalidQuestions(count: bank.rejected.count) }
        for language in AppLanguage.allCases where bank.questions(in: language).isEmpty {
            throw UpdateError.missingLanguage(language)
        }
        return bank
    }
}
