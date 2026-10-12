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

    func testOnlySourcedDraftsSurviveAndNeedReview() {
        let outcome = QuestionVerificationPipeline().verify([
            draft(excerpt: "revealed a life span of at least 272 years"),
            draft(excerpt: "Greenland sharks live 500 years"),
            draft(excerpt: "revealed a life span", pmid: "1"),
            draft(excerpt: "revealed a life span", options: ["A", "A", "B", "C"]),
        ], against: article)

        XCTAssertEqual(outcome.accepted.count, 1)
        XCTAssertEqual(outcome.rejected.count, 3)
        let accepted = outcome.accepted[0]
        XCTAssertEqual(accepted.verification.status, .needsReview)
        XCTAssertFalse(QuestionValidator.isPlayable(accepted), "Generated questions need human review before play")
    }
}
