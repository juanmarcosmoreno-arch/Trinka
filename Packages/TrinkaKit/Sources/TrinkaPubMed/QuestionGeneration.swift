import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
import TrinkaCore

// Question generation is prepared but not enabled in the MVP.
//
// Flow: the app sends an article (PMID + abstract) to TRINKA's own backend, which calls an AI
// model server-side and returns *drafts*. AI provider keys live only on that backend — never in
// the iOS/watchOS binaries. Every draft then goes through `QuestionVerificationPipeline`, and only
// drafts whose supporting excerpt is found verbatim in the source survive — as `.needsReview`,
// which is not playable until a reviewer marks it `.verified`.

/// A question proposed by the generation service, before verification.
public struct QuestionDraft: Codable, Hashable, Sendable {
    public var pmid: String
    public var language: AppLanguage
    public var category: ScienceCategory
    public var difficulty: Difficulty
    public var prompt: String
    public var options: [String]
    public var correctOptionIndex: Int
    public var explanation: String
    public var shortExplanation: String?
    /// Passage of the source the generator claims supports the correct answer.
    public var supportingExcerpt: String

    public init(pmid: String, language: AppLanguage, category: ScienceCategory, difficulty: Difficulty,
                prompt: String, options: [String], correctOptionIndex: Int, explanation: String,
                shortExplanation: String? = nil, supportingExcerpt: String) {
        self.pmid = pmid
        self.language = language
        self.category = category
        self.difficulty = difficulty
        self.prompt = prompt
        self.options = options
        self.correctOptionIndex = correctOptionIndex
        self.explanation = explanation
        self.shortExplanation = shortExplanation
        self.supportingExcerpt = supportingExcerpt
    }
}

/// Anything that can propose questions for an article.
public protocol QuestionGenerating: Sendable {
    func generateDrafts(for article: ArticleReference, language: AppLanguage,
                        difficulty: Difficulty, category: ScienceCategory) async throws -> [QuestionDraft]
}

/// Client for TRINKA's question service (see `Backend/README.md` for the contract).
/// Holds no AI credentials: authentication with AI providers happens server-side.
public struct RemoteQuestionService: QuestionGenerating {
    public var endpoint: URL
    private let session: URLSession

    public init(endpoint: URL, session: URLSession = .shared) {
        self.endpoint = endpoint
        self.session = session
    }

    struct RequestBody: Encodable {
        var pmid: String
        var title: String
        var abstract: String
        var language: AppLanguage
        var difficulty: Difficulty
        var category: ScienceCategory
    }

    struct ResponseBody: Decodable {
        var drafts: [QuestionDraft]
    }

    public func generateDrafts(for article: ArticleReference, language: AppLanguage,
                               difficulty: Difficulty, category: ScienceCategory) async throws -> [QuestionDraft] {
        guard let abstract = article.abstract, !abstract.isEmpty else { return [] }
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(RequestBody(
            pmid: article.pmid, title: article.title, abstract: abstract,
            language: language, difficulty: difficulty, category: category
        ))
        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            throw PubMedError.httpStatus((response as? HTTPURLResponse)?.statusCode ?? -1)
        }
        return try JSONDecoder().decode(ResponseBody.self, from: data).drafts
            .filter { $0.pmid == article.pmid } // Never accept drafts attributed to another article.
    }
}

/// Turns drafts into questions, discarding anything that can't be traced to the source.
public struct QuestionVerificationPipeline: Sendable {
    public struct Outcome: Sendable {
        /// Excerpt found in the source and structure valid. Status `.needsReview`.
        public var accepted: [Question]
        /// Discarded drafts with the reasons.
        public var rejected: [(draft: QuestionDraft, issues: [QuestionIssue])]
    }

    public init() {}

    public func verify(_ drafts: [QuestionDraft], against article: ArticleReference, now: Date = Date()) -> Outcome {
        var accepted: [Question] = []
        var rejected: [(QuestionDraft, [QuestionIssue])] = []

        for (index, draft) in drafts.enumerated() {
            guard draft.pmid == article.pmid else {
                rejected.append((draft, [.invalidPMID(draft.pmid)]))
                continue
            }
            let key = "gen-\(article.pmid)-\(draft.difficulty.rawValue)-\(index)"
            let candidate = Question(
                id: "\(key)-\(draft.language.rawValue)",
                translationKey: key,
                language: draft.language,
                category: draft.category,
                difficulty: draft.difficulty,
                prompt: draft.prompt,
                options: draft.options,
                correctOptionIndex: draft.correctOptionIndex,
                explanation: draft.explanation,
                shortExplanation: draft.shortExplanation,
                source: article,
                verification: SourceVerification(
                    status: .needsReview,
                    method: .automatedEvidenceMatch,
                    supportingExcerpt: draft.supportingExcerpt,
                    reviewedAt: now
                )
            )
            // Everything except the status must already be correct.
            let issues = QuestionValidator.issues(in: candidate).filter {
                if case .notVerified = $0 { return false }
                return true
            }
            if issues.isEmpty {
                accepted.append(candidate)
            } else {
                rejected.append((draft, issues))
            }
        }
        return Outcome(accepted: accepted, rejected: rejected)
    }
}
