import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
import TrinkaCore

// On-demand questions about any topic.
//
// Flow: the app searches PubMed for the topic, sends each article (PMID + title + abstract) to
// TRINKA's own question service (Backend/question-service), which asks Claude for drafts and
// returns only those whose supporting excerpt is found verbatim in the abstract. The app then
// re-checks every draft with `QuestionVerificationPipeline`. Survivors are `.autoVerified`:
// playable, always labeled "generated automatically", never presented as expert-reviewed.
// AI credentials live only on the service — never in the iOS/watchOS binaries.

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

public enum QuestionGenerationError: Error, Equatable, Sendable {
    case offline
    case unauthorized
    case busy
    case service(Int)
    case invalidResponse
}

/// Anything that can propose questions for an article.
public protocol QuestionGenerating: Sendable {
    func generateDrafts(for article: ArticleReference, language: AppLanguage,
                        difficulty: Difficulty, count: Int) async throws -> [QuestionDraft]
}

/// Client for TRINKA's question service (contract: `Backend/README.md`).
public struct RemoteQuestionService: QuestionGenerating {
    public struct Configuration: Sendable {
        /// e.g. `https://trinka-question-service.example.workers.dev`
        public var baseURL: URL
        /// Optional shared token (`APP_TOKEN` on the service). Deters casual abuse; not a secret.
        public var appToken: String?

        public init(baseURL: URL, appToken: String? = nil) {
            self.baseURL = baseURL
            self.appToken = appToken
        }
    }

    public typealias Send = @Sendable (URLRequest) async throws -> (Data, URLResponse)

    public let configuration: Configuration
    private let send: Send

    public init(configuration: Configuration, send: Send? = nil) {
        self.configuration = configuration
        self.send = send ?? { request in try await URLSession.shared.data(for: request) }
    }

    /// Minimum abstract length the service accepts.
    public static let minimumAbstractLength = 200

    struct RequestBody: Codable, Equatable {
        var pmid: String
        var title: String
        var abstract: String
        var language: AppLanguage
        var difficulty: Difficulty
        var count: Int
    }

    struct ResponseBody: Decodable {
        var drafts: [QuestionDraft]
    }

    public func generateDrafts(for article: ArticleReference, language: AppLanguage,
                               difficulty: Difficulty, count: Int) async throws -> [QuestionDraft] {
        guard let abstract = article.abstract, abstract.count >= Self.minimumAbstractLength else { return [] }
        var request = URLRequest(url: configuration.baseURL.appendingPathComponent("v1/questions/drafts"))
        request.httpMethod = "POST"
        request.timeoutInterval = 120
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        if let token = configuration.appToken, !token.isEmpty {
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }
        request.httpBody = try JSONEncoder().encode(RequestBody(
            pmid: article.pmid, title: article.title, abstract: String(abstract.prefix(8000)),
            language: language, difficulty: difficulty, count: max(1, min(count, 5))
        ))

        let data: Data
        let response: URLResponse
        do {
            (data, response) = try await send(request)
        } catch let error as URLError where [.notConnectedToInternet, .networkConnectionLost, .dataNotAllowed, .timedOut].contains(error.code) {
            throw QuestionGenerationError.offline
        }
        guard let http = response as? HTTPURLResponse else { throw QuestionGenerationError.invalidResponse }
        switch http.statusCode {
        case 200: break
        case 401: throw QuestionGenerationError.unauthorized
        case 429, 503: throw QuestionGenerationError.busy
        default: throw QuestionGenerationError.service(http.statusCode)
        }
        do {
            return try JSONDecoder().decode(ResponseBody.self, from: data).drafts
                .filter { $0.pmid == article.pmid } // Never accept drafts attributed to another article.
        } catch {
            throw QuestionGenerationError.invalidResponse
        }
    }
}

/// Turns drafts into questions, discarding anything that can't be traced to the source.
public struct QuestionVerificationPipeline: Sendable {
    public struct Outcome: Sendable {
        /// Excerpt found in the source and structure valid. Status `.autoVerified`.
        public var accepted: [Question]
        /// Discarded drafts with the reasons.
        public var rejected: [(draft: QuestionDraft, issues: [QuestionIssue])]
    }

    public init() {}

    /// - Parameter idPrefix: makes question IDs unique across generated quizzes.
    public func verify(_ drafts: [QuestionDraft], against article: ArticleReference,
                       idPrefix: String = "gen", now: Date = Date()) -> Outcome {
        var accepted: [Question] = []
        var rejected: [(QuestionDraft, [QuestionIssue])] = []

        for (index, draft) in drafts.enumerated() {
            guard draft.pmid == article.pmid else {
                rejected.append((draft, [.invalidPMID(draft.pmid)]))
                continue
            }
            let key = "\(idPrefix)-\(article.pmid)-\(draft.difficulty.rawValue)-\(index)"
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
                    status: .autoVerified,
                    method: .automatedEvidenceMatch,
                    supportingExcerpt: draft.supportingExcerpt,
                    reviewedAt: now
                )
            )
            let issues = QuestionValidator.issues(in: candidate)
            if issues.isEmpty {
                accepted.append(candidate)
            } else {
                rejected.append((draft, issues))
            }
        }
        return Outcome(accepted: accepted, rejected: rejected)
    }
}

// MARK: - Topic quizzes

/// A quiz generated on demand about a topic the user typed (e.g. "Staphylococcus aureus").
public struct TopicQuiz: Codable, Hashable, Identifiable, Sendable {
    public var id: UUID
    public var topic: String
    public var language: AppLanguage
    public var level: Difficulty
    public var createdAt: Date
    public var questions: [Question]
    /// Articles the questions come from.
    public var articles: [ArticleReference]

    public init(id: UUID = UUID(), topic: String, language: AppLanguage, level: Difficulty,
                createdAt: Date = Date(), questions: [Question], articles: [ArticleReference]) {
        self.id = id
        self.topic = topic
        self.language = language
        self.level = level
        self.createdAt = createdAt
        self.questions = questions
        self.articles = articles
    }
}

public enum TopicQuizProgress: Equatable, Sendable {
    case searching
    case generating(articles: Int)
    case done
}

public enum TopicQuizError: Error, Equatable, Sendable {
    /// The question service isn't configured in this build.
    case notConfigured
    case offline
    /// PubMed returned no articles with an abstract for the topic.
    case noArticles
    /// Articles were found, but no question passed verification.
    case noQuestions
    case service
}

/// Search seam so the builder can be tested without the network.
public protocol ArticleSearching: Sendable {
    func searchArticles(_ query: PubMedQuery) async throws -> [ArticleReference]
}

extension PubMedClient: ArticleSearching {}

/// Builds a `TopicQuiz`: PubMed search → per-article generation (in parallel) → verification.
public struct TopicQuizBuilder: Sendable {
    public let search: ArticleSearching
    public let generator: QuestionGenerating
    /// Articles used per quiz; questions are spread across them.
    public var maxArticles = 5
    /// Turns the topic into PubMed search terms (e.g. translates "estafilococo" to English).
    /// When `nil` or when it returns nothing, the topic is searched as typed.
    public var searchTerms: (@Sendable (String) async -> String?)?

    public init(search: ArticleSearching, generator: QuestionGenerating) {
        self.search = search
        self.generator = generator
    }

    public func build(
        topic rawTopic: String,
        language: AppLanguage,
        level: Difficulty,
        questionCount: Int = 5,
        progress: @Sendable (TopicQuizProgress) -> Void = { _ in }
    ) async throws -> TopicQuiz {
        let topic = rawTopic.trimmingCharacters(in: .whitespacesAndNewlines)
        progress(.searching)

        let found: [ArticleReference]
        do {
            var terms = topic
            if let searchTerms, let rewritten = await searchTerms(topic)?.trimmingCharacters(in: .whitespacesAndNewlines),
               !rewritten.isEmpty {
                terms = rewritten
            }
            found = try await search.searchArticles(PubMedQuery(topic: terms, requireAbstract: true, sort: .relevance, maxResults: 15))
        } catch PubMedError.offline {
            throw TopicQuizError.offline
        } catch {
            throw TopicQuizError.service
        }
        let usable = found.filter { ($0.abstract?.count ?? 0) >= RemoteQuestionService.minimumAbstractLength }
        guard !usable.isEmpty else { throw TopicQuizError.noArticles }

        let articles = Array(usable.prefix(maxArticles))
        // Ask each article for its share of questions, plus one spare in case some are discarded.
        let perArticle = min(5, Int((Double(questionCount) / Double(articles.count)).rounded(.up)) + 1)
        progress(.generating(articles: articles.count))

        let batch = String(UUID().uuidString.prefix(8)).lowercased()
        let pipeline = QuestionVerificationPipeline()
        var perArticleQuestions: [[Question]] = Array(repeating: [], count: articles.count)
        var failures: [Error] = []

        await withTaskGroup(of: (Int, Result<[QuestionDraft], Error>).self) { group in
            for (index, article) in articles.enumerated() {
                group.addTask {
                    do {
                        return (index, .success(try await generator.generateDrafts(
                            for: article, language: language, difficulty: level, count: perArticle)))
                    } catch {
                        return (index, .failure(error))
                    }
                }
            }
            for await (index, result) in group {
                switch result {
                case let .success(drafts):
                    perArticleQuestions[index] = pipeline.verify(drafts, against: articles[index], idPrefix: "gen-\(batch)").accepted
                case let .failure(error):
                    failures.append(error)
                }
            }
        }

        // Round-robin across articles so one paper doesn't dominate the quiz.
        var questions: [Question] = []
        var round = 0
        while questions.count < questionCount {
            var added = false
            for list in perArticleQuestions where round < list.count {
                questions.append(list[round])
                added = true
                if questions.count == questionCount { break }
            }
            if !added { break }
            round += 1
        }

        guard !questions.isEmpty else {
            if failures.count == articles.count {
                throw failures.contains { ($0 as? QuestionGenerationError) == .offline } ? TopicQuizError.offline : TopicQuizError.service
            }
            throw TopicQuizError.noQuestions
        }
        progress(.done)
        let usedPMIDs = Set(questions.map(\.source.pmid))
        return TopicQuiz(topic: topic, language: language, level: level, questions: questions,
                         articles: articles.filter { usedPMIDs.contains($0.pmid) })
    }
}

/// Keeps recent topic quizzes on the device so they can be replayed offline.
public actor TopicQuizStore {
    private let fileURL: URL
    private let limit: Int

    public init(directory: URL? = nil, limit: Int = 20) {
        let base = directory
            ?? FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
            ?? FileManager.default.temporaryDirectory
        fileURL = base.appendingPathComponent("TopicQuizzes.json")
        self.limit = limit
    }

    /// Most recent first.
    public func all() -> [TopicQuiz] {
        guard let data = try? Data(contentsOf: fileURL) else { return [] }
        return (try? JSONDecoder().decode([TopicQuiz].self, from: data)) ?? []
    }

    @discardableResult
    public func save(_ quiz: TopicQuiz) throws -> [TopicQuiz] {
        var quizzes = all().filter { $0.id != quiz.id }
        quizzes.insert(quiz, at: 0)
        quizzes = Array(quizzes.prefix(limit))
        try write(quizzes)
        return quizzes
    }

    @discardableResult
    public func delete(_ id: UUID) throws -> [TopicQuiz] {
        let quizzes = all().filter { $0.id != id }
        try write(quizzes)
        return quizzes
    }

    private func write(_ quizzes: [TopicQuiz]) throws {
        try FileManager.default.createDirectory(at: fileURL.deletingLastPathComponent(), withIntermediateDirectories: true)
        try JSONEncoder().encode(quizzes).write(to: fileURL, options: .atomic)
    }
}
