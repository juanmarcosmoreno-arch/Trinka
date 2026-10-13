import Foundation
import TrinkaCore

/// Source of playable questions.
public protocol QuestionBank: Sendable {
    /// All playable questions in `language`. Implementations must only return questions
    /// that pass `QuestionValidator.isPlayable`.
    func questions(in language: AppLanguage) -> [Question]

    /// Source articles referenced by the bank.
    var articles: [ArticleReference] { get }
}

public extension QuestionBank {
    func questions(
        in language: AppLanguage,
        category: ScienceCategory? = nil,
        difficulty: Difficulty? = nil
    ) -> [Question] {
        questions(in: language).filter { question in
            (category == nil || question.category == category)
                && (difficulty == nil || question.difficulty == difficulty)
        }
    }

    func question(withTranslationKey key: String, language: AppLanguage) -> Question? {
        questions(in: language).first { $0.translationKey == key }
    }
}

/// In-memory bank that validates everything it is given and keeps only playable questions.
public struct StaticQuestionBank: QuestionBank {
    public let articles: [ArticleReference]
    /// Content version of the bank (`SeedQuestions.json` "version"); friend-challenge codes embed it.
    public let version: Int
    private let byLanguage: [AppLanguage: [Question]]
    /// Questions that failed validation, with the reasons. Useful for tests and diagnostics.
    public let rejected: [(question: Question, issues: [QuestionIssue])]

    public init(questions: [Question], articles: [ArticleReference] = [], version: Int = 0) {
        self.version = version
        var accepted: [AppLanguage: [Question]] = [:]
        var rejected: [(Question, [QuestionIssue])] = []
        for question in questions {
            let issues = QuestionValidator.issues(in: question)
            if issues.isEmpty {
                accepted[question.language, default: []].append(question)
            } else {
                rejected.append((question, issues))
            }
        }
        self.byLanguage = accepted
        self.rejected = rejected
        self.articles = articles.isEmpty
            ? Array(Set(questions.map(\.source))).sorted { $0.pmid < $1.pmid }
            : articles
    }

    public func questions(in language: AppLanguage) -> [Question] {
        byLanguage[language] ?? []
    }

    /// Disciplines with at least `minimumQuestions` playable questions in `language`,
    /// in `ScienceCategory` order. Used to hide disciplines that don't have enough content yet.
    public func categories(in language: AppLanguage, minimumQuestions: Int = 20) -> [ScienceCategory] {
        var counts: [ScienceCategory: Int] = [:]
        for question in questions(in: language) { counts[question.category, default: 0] += 1 }
        return ScienceCategory.allCases.filter { (counts[$0] ?? 0) >= minimumQuestions }
    }
}

/// The question bank shipped inside the app (`SeedQuestions.json`).
///
/// Every seed question cites a real PubMed article retrieved through NCBI E-utilities,
/// and stores a verbatim excerpt of its abstract supporting the correct answer.
public enum SeedQuestionBank {
    /// Version of the bank bundled with the app. Must match the "version" in `SeedQuestions.json`;
    /// `Scripts/seed/build_seed.py` bumps both whenever the questions change. Newer banks can be
    /// downloaded later (see `QuestionBankStore`), so use `StaticQuestionBank.version` at runtime.
    public static let version = 11

    public enum LoadError: Error {
        case resourceMissing
        case unknownArticle(pmid: String, questionID: String)
    }

    /// Loads the bundled seed bank.
    public static func load() throws -> StaticQuestionBank {
        guard let url = Bundle.module.url(forResource: "SeedQuestions", withExtension: "json") else {
            throw LoadError.resourceMissing
        }
        return try load(from: Data(contentsOf: url))
    }

    /// Loads a bank from seed-format JSON.
    public static func load(from data: Data) throws -> StaticQuestionBank {
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        let file = try decoder.decode(SeedFile.self, from: data)

        let articlesByPMID = Dictionary(uniqueKeysWithValues: file.articles.map { ($0.pmid, $0) })
        let questions = try file.questions.compactMap { entry -> Question? in
            // Banks downloaded later may use languages, disciplines or levels this build doesn't
            // know yet; those questions are skipped instead of rejecting the whole file.
            guard let language = AppLanguage(rawValue: entry.language),
                  let category = ScienceCategory(rawValue: entry.category),
                  let difficulty = Difficulty(rawValue: entry.difficulty) else { return nil }
            guard let source = articlesByPMID[entry.pmid] else {
                throw LoadError.unknownArticle(pmid: entry.pmid, questionID: entry.id)
            }
            return Question(
                id: entry.id,
                translationKey: entry.translationKey,
                language: language,
                category: category,
                difficulty: difficulty,
                prompt: entry.prompt,
                options: entry.options,
                correctOptionIndex: entry.correctOptionIndex,
                explanation: entry.explanation,
                shortExplanation: entry.shortExplanation,
                source: source,
                verification: entry.verification
            )
        }
        return StaticQuestionBank(questions: questions, articles: file.articles, version: file.version)
    }

    /// On-disk format: articles are stored once and referenced by PMID.
    struct SeedFile: Decodable {
        var version: Int
        var articles: [ArticleReference]
        var questions: [Entry]
    }

    struct Entry: Decodable {
        var id: String
        var translationKey: String
        var language: String
        var category: String
        var difficulty: String
        var prompt: String
        var options: [String]
        var correctOptionIndex: Int
        var explanation: String
        var shortExplanation: String?
        var pmid: String
        var verification: SourceVerification
    }
}
