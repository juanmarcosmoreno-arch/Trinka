import XCTest
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
import TrinkaCore
@testable import TrinkaPubMed

final class PubMedXMLParserTests: XCTestCase {
    private func fixture(_ name: String) throws -> Data {
        let url = try XCTUnwrap(Bundle.module.url(forResource: name, withExtension: nil, subdirectory: "Fixtures"))
        return try Data(contentsOf: url)
    }

    func testParsesStructuredAbstractAndMetadata() throws {
        let articles = try PubMedXMLParser.parse(fixture("efetch-sample.xml"))
        XCTAssertEqual(articles.map(\.pmid), ["33301246", "7636184"])

        let vaccine = articles[0]
        XCTAssertEqual(vaccine.title, "Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine.")
        XCTAssertEqual(vaccine.journal, "The New England journal of medicine")
        XCTAssertEqual(vaccine.year, 2020)
        XCTAssertEqual(vaccine.doi, "10.1056/NEJMoa2034577")
        XCTAssertEqual(vaccine.authors.first, "Polack FP")
        XCTAssertTrue(vaccine.publicationTypes.contains("Randomized Controlled Trial"))
        let abstract = try XCTUnwrap(vaccine.abstract)
        XCTAssertTrue(abstract.hasPrefix("BACKGROUND: "))
        XCTAssertTrue(abstract.contains("\nCONCLUSIONS: "))
        XCTAssertTrue(EvidenceMatcher.source(vaccine, contains: "BNT162b2 was 95% effective in preventing Covid-19"))
    }

    func testDoesNotTakeIdentifiersFromReferenceList() throws {
        let articles = try PubMedXMLParser.parse(fixture("efetch-sample.xml"))
        let tregs = try XCTUnwrap(articles.first { $0.pmid == "7636184" })
        XCTAssertEqual(tregs.year, 1995)
        XCTAssertEqual(tregs.authors.count, 5)
    }

    func testDigest() throws {
        let vaccine = try XCTUnwrap(PubMedXMLParser.parse(fixture("efetch-sample.xml")).first)
        let digest = ArticleDigest(article: vaccine)
        XCTAssertEqual(digest.shortTitle, "Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine")
        XCTAssertEqual(digest.keyFinding,
                       "A two-dose regimen of BNT162b2 conferred 95% protection against Covid-19 in persons 16 years of age or older. Safety over a median of 2 months was similar to that of other viral vaccines.")
        let summary = try XCTUnwrap(digest.summary(maxCharacters: 200))
        XCTAssertFalse(summary.hasPrefix("BACKGROUND"))
        XCTAssertLessThanOrEqual(summary.count, 200)
    }

    func testShortTitleDropsSectionTag() {
        var article = ArticleReference(pmid: "26315443", title: "PSYCHOLOGY. Estimating the reproducibility of psychological science.",
                                       authors: [], journal: "Science", year: 2015)
        XCTAssertEqual(ArticleDigest(article: article).shortTitle, "Estimating the reproducibility of psychological science")
        article.title = "Ultra-Processed Diets Cause Excess Calorie Intake and Weight Gain: An Inpatient Randomized Controlled Trial."
        XCTAssertEqual(ArticleDigest(article: article).shortTitle, "Ultra-Processed Diets Cause Excess Calorie Intake and Weight Gain")
    }

    func testSentenceSplitterKeepsDecimalsAndAbbreviations() {
        let sentences = ArticleDigest.sentences(in: "Temperature fell 0.03°C per decade. We studied S. aureus strains. Results were clear.")
        XCTAssertEqual(sentences, ["Temperature fell 0.03°C per decade.", "We studied S. aureus strains.", "Results were clear."])
    }
}

final class PubMedQueryTests: XCTestCase {
    func testTermCombinesFilters() {
        let query = PubMedQuery(category: .nutrition, topic: "olive oil", keywords: ["cardiovascular"],
                                publicationTypes: [.randomizedControlledTrial, .metaAnalysis])
        let term = query.term
        XCTAssertTrue(term.hasPrefix("(\"Nutritional Sciences\"[MeSH] OR \"Diet\"[MeSH])"))
        XCTAssertTrue(term.contains(" AND (olive oil)"))
        XCTAssertTrue(term.contains(" AND \"cardiovascular\"[Title/Abstract]"))
        XCTAssertTrue(term.contains("(\"Meta-Analysis\"[pt] OR \"Randomized Controlled Trial\"[pt])"))
        XCTAssertTrue(term.contains(" AND hasabstract"))
        XCTAssertTrue(term.hasSuffix(" NOT \"Retracted Publication\"[pt]"))
    }

    func testUserInputIsSanitized() {
        let query = PubMedQuery(topic: "x\") OR (\"y", requireAbstract: false)
        XCTAssertFalse(query.term.contains("\")"))
    }
}

final class PubMedClientTests: XCTestCase {
    struct StubLoader: HTTPDataLoading {
        var responses: [String: Data]
        func data(from url: URL) async throws -> (Data, URLResponse) {
            let endpoint = url.lastPathComponent
            guard let data = responses[endpoint] else { throw URLError(.notConnectedToInternet) }
            return (data, HTTPURLResponse(url: url, statusCode: 200, httpVersion: nil, headerFields: nil)!)
        }
    }

    func testSearchThenFetch() async throws {
        let search = #"{"esearchresult":{"idlist":["7636184","33301246"]}}"#.data(using: .utf8)!
        let xml = try Data(contentsOf: XCTUnwrap(Bundle.module.url(forResource: "efetch-sample.xml", withExtension: nil, subdirectory: "Fixtures")))
        let client = PubMedClient(loader: StubLoader(responses: ["esearch.fcgi": search, "efetch.fcgi": xml]))
        let articles = try await client.searchArticles(PubMedQuery(category: .immunology))
        XCTAssertEqual(articles.map(\.pmid), ["7636184", "33301246"], "esearch ranking is preserved")
    }

    func testOfflineIsReported() async {
        let client = PubMedClient(loader: StubLoader(responses: [:]))
        do {
            _ = try await client.search(PubMedQuery(topic: "sleep"))
            XCTFail("Expected offline error")
        } catch {
            XCTAssertEqual(error as? PubMedError, .offline)
        }
    }

    func testRequestIdentifiesTool() {
        let client = PubMedClient(configuration: .init(email: "dev@example.com"))
        let url = client.url("esearch.fcgi", [URLQueryItem(name: "term", value: "a+b")])
        XCTAssertTrue(url.absoluteString.contains("tool=trinka"))
        XCTAssertTrue(url.absoluteString.contains("email=dev@example.com"))
        XCTAssertTrue(url.absoluteString.contains("term=a%2Bb"))
    }
}

final class QuestionVerificationPipelineTests: XCTestCase {
    private let article = ArticleReference(
        pmid: "27516602",
        title: "Eye lens radiocarbon reveals centuries of longevity in the Greenland shark (Somniosus microcephalus).",
        authors: ["Nielsen J"], journal: "Science", year: 2016,
        abstract: "Radiocarbon dating of eye lens nuclei from 28 female Greenland sharks (81 to 502 cm in total length) revealed a life span of at least 272 years."
    )

    private func draft(excerpt: String, pmid: String = "27516602", options: [String] = ["272 years", "50 years", "120 years", "1,000 years"]) -> QuestionDraft {
        QuestionDraft(pmid: pmid, language: .en, category: .generalScience, difficulty: .curious,
                      prompt: "How long do Greenland sharks live?", options: options, correctOptionIndex: 0,
                      explanation: "At least 272 years.", supportingExcerpt: excerpt)
    }

    func testOnlySourcedDraftsSurviveAndAreLabeledAutomatic() {
        let outcome = QuestionVerificationPipeline().verify([
            draft(excerpt: "revealed a life span of at least 272 years"),
            draft(excerpt: "Greenland sharks live 500 years"),
            draft(excerpt: "revealed a life span", pmid: "1"),
            draft(excerpt: "revealed a life span", options: ["A", "A", "B", "C"]),
        ], against: article)

        XCTAssertEqual(outcome.accepted.count, 1)
        XCTAssertEqual(outcome.rejected.count, 3)
        let accepted = outcome.accepted[0]
        XCTAssertEqual(accepted.verification.status, .autoVerified)
        XCTAssertEqual(accepted.verification.method, .automatedEvidenceMatch)
        XCTAssertTrue(accepted.isAutoGenerated)
        XCTAssertTrue(QuestionValidator.isPlayable(accepted), "Auto-verified questions are playable (and labeled in the UI)")
    }
}

final class RemoteQuestionServiceTests: XCTestCase {
    private let article = ArticleReference(
        pmid: "27516602", title: "Eye lens radiocarbon reveals centuries of longevity in the Greenland shark.",
        authors: ["Nielsen J"], journal: "Science", year: 2016,
        abstract: String(repeating: "The Greenland shark lives in the Arctic seas and grows slowly. ", count: 5)
    )

    func testSendsContractAndToken() async throws {
        let captured = Captured()
        let service = RemoteQuestionService(
            configuration: .init(baseURL: URL(string: "https://svc.example")!, appToken: "abc"),
            send: { request in
                await captured.set(request)
                let body = #"{"drafts":[{"pmid":"27516602","language":"es","category":"generalScience","difficulty":"beginner","prompt":"¿Dónde vive?","options":["Ártico","Trópico","Lago","Río"],"correctOptionIndex":0,"explanation":"x","shortExplanation":"y","supportingExcerpt":"lives in the Arctic seas"},{"pmid":"999","language":"es","category":"generalScience","difficulty":"beginner","prompt":"p","options":["a","b","c","d"],"correctOptionIndex":0,"explanation":"x","supportingExcerpt":"z"}]}"#
                return (Data(body.utf8), HTTPURLResponse(url: request.url!, statusCode: 200, httpVersion: nil, headerFields: nil)!)
            }
        )
        let drafts = try await service.generateDrafts(for: article, language: .es, difficulty: .beginner, count: 9)
        XCTAssertEqual(drafts.count, 1, "Drafts for another PMID are dropped")
        let capturedRequest = await captured.request
        let request = try XCTUnwrap(capturedRequest)
        XCTAssertEqual(request.url?.absoluteString, "https://svc.example/v1/questions/drafts")
        XCTAssertEqual(request.value(forHTTPHeaderField: "Authorization"), "Bearer abc")
        let body = try JSONDecoder().decode(RemoteQuestionService.RequestBody.self, from: XCTUnwrap(request.httpBody))
        XCTAssertEqual(body.count, 5, "Count is capped at 5")
        XCTAssertEqual(body.difficulty, .beginner)
    }

    func testMapsErrors() async {
        for (status, expected) in [(401, QuestionGenerationError.unauthorized), (503, .busy), (500, .service(500))] {
            let service = RemoteQuestionService(configuration: .init(baseURL: URL(string: "https://svc.example")!), send: { request in
                (Data(), HTTPURLResponse(url: request.url!, statusCode: status, httpVersion: nil, headerFields: nil)!)
            })
            do {
                _ = try await service.generateDrafts(for: article, language: .en, difficulty: .curious, count: 3)
                XCTFail("Expected \(expected)")
            } catch {
                XCTAssertEqual(error as? QuestionGenerationError, expected)
            }
        }
    }

    func testSkipsArticlesWithoutEnoughAbstract() async throws {
        var short = article
        short.abstract = "Too short."
        let service = RemoteQuestionService(configuration: .init(baseURL: URL(string: "https://svc.example")!), send: { _ in
            XCTFail("Should not call the service"); throw URLError(.badURL)
        })
        let drafts = try await service.generateDrafts(for: short, language: .en, difficulty: .curious, count: 3)
        XCTAssertTrue(drafts.isEmpty)
    }
}

private actor Captured {
    var request: URLRequest?
    func set(_ request: URLRequest) { self.request = request }
}

final class TopicQuizBuilderTests: XCTestCase {
    struct StubSearch: ArticleSearching {
        var articles: [ArticleReference]
        var error: Error?
        func searchArticles(_ query: PubMedQuery) async throws -> [ArticleReference] {
            if let error { throw error }
            XCTAssertEqual(query.topic, "Staphylococcus aureus")
            XCTAssertTrue(query.requireAbstract)
            return articles
        }
    }

    /// Returns `count` drafts per article; the first is unsupported by the abstract and must be dropped.
    struct StubGenerator: QuestionGenerating {
        var fail = false
        func generateDrafts(for article: ArticleReference, language: AppLanguage, difficulty: Difficulty, count: Int) async throws -> [QuestionDraft] {
            if fail { throw QuestionGenerationError.offline }
            let bad = QuestionDraft(pmid: article.pmid, language: language, category: .microbiology, difficulty: difficulty,
                                    prompt: "Bad?", options: ["a", "b", "c", "d"], correctOptionIndex: 0,
                                    explanation: "x", supportingExcerpt: "not in the abstract at all")
            let good = (0..<count).map { i in
                QuestionDraft(pmid: article.pmid, language: language, category: .microbiology, difficulty: difficulty,
                              prompt: "Q\(i) about \(article.pmid)?", options: ["Right \(i)", "W1", "W2", "W3"], correctOptionIndex: 0,
                              explanation: "Because.", supportingExcerpt: "Staphylococcus aureus causes infections")
            }
            return [bad] + good
        }
    }

    private func article(_ pmid: String, abstractLength: Int = 400) -> ArticleReference {
        let sentence = "Staphylococcus aureus causes infections in hospitals and the community. "
        return ArticleReference(pmid: pmid, title: "S. aureus study \(pmid)", authors: ["A B"], journal: "J", year: 2024,
                                abstract: String(String(repeating: sentence, count: 10).prefix(abstractLength)))
    }

    func testBuildsQuizSpreadAcrossArticles() async throws {
        let builder = TopicQuizBuilder(search: StubSearch(articles: [article("1"), article("2"), article("3", abstractLength: 50)]),
                                       generator: StubGenerator())
        let quiz = try await builder.build(topic: "  Staphylococcus aureus ", language: .es, level: .beginner, questionCount: 4)
        XCTAssertEqual(quiz.topic, "Staphylococcus aureus")
        XCTAssertEqual(quiz.questions.count, 4)
        XCTAssertEqual(Set(quiz.questions.map(\.source.pmid)), ["1", "2"], "Article 3's abstract is too short")
        XCTAssertEqual(Array(quiz.questions.map(\.source.pmid).prefix(2)).sorted(), ["1", "2"], "Round-robin across articles")
        XCTAssertTrue(quiz.questions.allSatisfy { $0.isAutoGenerated && QuestionValidator.isPlayable($0) })
        XCTAssertFalse(quiz.questions.contains { $0.prompt == "Bad?" })
        XCTAssertEqual(Set(quiz.questions.map(\.id)).count, 4, "Unique IDs")
        XCTAssertEqual(quiz.articles.map(\.pmid).sorted(), ["1", "2"])
    }

    func testErrors() async {
        let cases: [(TopicQuizBuilder, TopicQuizError)] = [
            (TopicQuizBuilder(search: StubSearch(articles: []), generator: StubGenerator()), .noArticles),
            (TopicQuizBuilder(search: StubSearch(articles: [], error: PubMedError.offline), generator: StubGenerator()), .offline),
            (TopicQuizBuilder(search: StubSearch(articles: [article("1")]), generator: StubGenerator(fail: true)), .offline),
        ]
        for (builder, expected) in cases {
            do {
                _ = try await builder.build(topic: "Staphylococcus aureus", language: .en, level: .curious)
                XCTFail("Expected \(expected)")
            } catch {
                XCTAssertEqual(error as? TopicQuizError, expected)
            }
        }
    }

    func testStoreKeepsRecentQuizzes() async throws {
        let directory = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        let store = TopicQuizStore(directory: directory, limit: 2)
        let builder = TopicQuizBuilder(search: StubSearch(articles: [article("1")]), generator: StubGenerator())
        var ids: [UUID] = []
        for _ in 0..<3 {
            let quiz = try await builder.build(topic: "Staphylococcus aureus", language: .en, level: .curious, questionCount: 2)
            ids.append(quiz.id)
            try await store.save(quiz)
        }
        let saved = await store.all()
        XCTAssertEqual(saved.map(\.id), [ids[2], ids[1]])
        XCTAssertTrue(saved[0].questions.allSatisfy(QuestionValidator.isPlayable), "Round-trips with abstracts intact")
    }
}

final class PubMedAnswererTests: XCTestCase {
    struct Search: ArticleSearching {
        var articles: [ArticleReference]
        func searchArticles(_ query: PubMedQuery) async throws -> [ArticleReference] { articles }
    }

    struct Composer: EvidenceComposing {
        var text: String
        func searchTerms(for question: String) async throws -> String { "MRSA treatment" }
        func answer(question: String, language: AppLanguage, sources: [ArticleReference]) async throws -> String { text }
    }

    private let articles = [
        ArticleReference(pmid: "1", title: "MRSA review", authors: ["A B"], journal: "J", year: 2020,
                         abstract: "Methicillin-resistant Staphylococcus aureus is a leading cause of skin infections. Vancomycin remains a first-line option for severe MRSA infections in hospitals."),
        ArticleReference(pmid: "2", title: "Other", authors: ["C D"], journal: "K", year: 2021,
                         abstract: "Daptomycin is an alternative for MRSA bacteremia when vancomycin fails or is not tolerated by the patient. Outcomes were compared across several hospitals over five years."),
        ArticleReference(pmid: "3", title: "Unrelated", authors: ["E F"], journal: "L", year: 2022,
                         abstract: "Coffee consumption was studied in a large cohort of adults living in several European countries. Sleep quality and cardiovascular outcomes were recorded every year."),
    ]

    func testKeepsOnlySentencesWithValidCitationsAndRenumbersSources() async throws {
        let composer = Composer(text: "Vancomycin is first-line for severe MRSA [1]. Daptomycin is an alternative [2, 9]. MRSA is always fatal. Made-up claim [7].")
        let answer = try await PubMedAnswerer(search: Search(articles: articles), composer: composer)
            .answer("¿Cómo se trata el MRSA?", language: .es)
        XCTAssertEqual(answer.kind, .synthesized)
        XCTAssertEqual(answer.searchTerms, "MRSA treatment")
        XCTAssertEqual(answer.statements.map(\.text), ["Vancomycin is first-line for severe MRSA.", "Daptomycin is an alternative."])
        XCTAssertEqual(answer.statements.map(\.citations), [[1], [2]])
        XCTAssertEqual(answer.sources.map(\.pmid), ["1", "2"])
    }

    func testFallsBackToVerbatimQuotesWithoutAComposer() async throws {
        let answer = try await PubMedAnswerer(search: Search(articles: articles), composer: nil)
            .answer("vancomycin MRSA treatment", language: .en)
        XCTAssertEqual(answer.kind, .quoted)
        XCTAssertFalse(answer.statements.isEmpty)
        for statement in answer.statements {
            let source = answer.sources[statement.citations[0] - 1]
            XCTAssertTrue(source.abstract!.contains(statement.text), "Quotes must be verbatim")
        }
        XCTAssertFalse(answer.sources.contains { $0.pmid == "3" })
    }

    func testUncitedComposerOutputFallsBackToQuotes() async throws {
        let answer = try await PubMedAnswerer(search: Search(articles: articles), composer: Composer(text: "MRSA is treated with love."))
            .answer("vancomycin MRSA", language: .en)
        XCTAssertEqual(answer.kind, .quoted)
    }

    func testNoEvidenceWhenAbstractsDoNotMatch() async throws {
        let answer = try await PubMedAnswerer(search: Search(articles: [articles[2]]), composer: nil)
            .answer("zebrafish regeneration", language: .en)
        XCTAssertEqual(answer.kind, .noEvidence)
        XCTAssertTrue(answer.statements.isEmpty)
    }
}

final class AbstractQuoteTests: XCTestCase {
    let abstract = "Methicillin-resistant Staphylococcus aureus is a leading cause of skin infections. Vancomycin remains a first-line option for severe MRSA infections in hospitals."

    func testKeepsExactQuotesAndSnapsCloseParaphrases() {
        XCTAssertEqual(AbstractQuote.snap("leading cause of skin infections", to: abstract), "leading cause of skin infections")
        XCTAssertEqual(AbstractQuote.snap("Vancomycin remains the first-line option for severe MRSA infections in hospital", to: abstract),
                       "Vancomycin remains a first-line option for severe MRSA infections in hospitals.")
        XCTAssertNil(AbstractQuote.snap("Penicillin cures every infection quickly", to: abstract))
    }
}
