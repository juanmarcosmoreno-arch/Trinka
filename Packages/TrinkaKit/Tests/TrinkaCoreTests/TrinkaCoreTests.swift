import XCTest
@testable import TrinkaCore

final class QuestionValidatorTests: XCTestCase {
    func testVerifiedQuestionWithMatchingExcerptIsPlayable() {
        XCTAssertTrue(QuestionValidator.isPlayable(.fixture()))
    }

    func testExcerptMatchingIgnoresCaseAndWhitespace() {
        let question = Question.fixture(excerpt: "bacteria   INTEGRATED\u{00A0}new spacers")
        XCTAssertTrue(QuestionValidator.isPlayable(question))
    }

    func testExcerptNotInSourceIsRejected() {
        let question = Question.fixture(excerpt: "CRISPR cures all viral infections")
        XCTAssertTrue(QuestionValidator.issues(in: question).contains(.excerptNotFoundInSource))
    }

    func testMissingExcerptIsRejected() {
        let question = Question.fixture(excerpt: nil)
        XCTAssertTrue(QuestionValidator.issues(in: question).contains(.missingSupportingExcerpt))
    }

    func testUnverifiedStatusesAreNotPlayable() {
        for status in [SourceVerification.Status.pending, .needsReview, .rejected] {
            var question = Question.fixture()
            question.verification.status = status
            XCTAssertFalse(QuestionValidator.isPlayable(question), "\(status)")
        }
    }

    func testStructuralProblems() {
        var question = Question.fixture()
        question.options = ["A", "a", "B", " "]
        question.correctOptionIndex = 7
        question.source.pmid = "0123"
        let issues = QuestionValidator.issues(in: question)
        XCTAssertTrue(issues.contains(.duplicateOptions))
        XCTAssertTrue(issues.contains(.emptyOption(index: 3)))
        XCTAssertTrue(issues.contains(.correctIndexOutOfRange(7)))
        XCTAssertTrue(issues.contains(.invalidPMID("0123")))
    }
}

final class ScoringTests: XCTestCase {
    func testPointsScaleWithDifficulty() {
        let rules = ScoringRules.standard
        XCTAssertEqual(rules.points(for: .curious), 10)
        XCTAssertEqual(rules.points(for: .explorer), 15)
        XCTAssertEqual(rules.points(for: .researcher), 20)
    }

    func testCompletedPerfectSessionGetsBonuses() {
        let answers = [AnswerRecord.fixture(correct: true, category: .genetics),
                       AnswerRecord.fixture(correct: true, category: .microbiology)]
        let xp = ScoringRules.standard.xp(for: answers, completed: true, currentStreak: 3,
                                          isFirstSessionToday: true, previouslyPlayedCategories: [.genetics])
        XCTAssertEqual(xp.correctAnswers, 20)
        XCTAssertEqual(xp.completion, 20)
        XCTAssertEqual(xp.perfectRun, 15)
        XCTAssertEqual(xp.streak, 10)
        XCTAssertEqual(xp.newCategories, 25)
        XCTAssertEqual(xp.total, 90)
    }

    func testAbandonedSessionOnlyCountsCorrectAnswers() {
        let answers = [AnswerRecord.fixture(correct: true), AnswerRecord.fixture(correct: false)]
        let xp = ScoringRules.standard.xp(for: answers, completed: false, currentStreak: 5,
                                          isFirstSessionToday: true, previouslyPlayedCategories: [])
        XCTAssertEqual(xp.total, 10)
    }

    func testResponseTimeDoesNotAffectScore() {
        let fast = AnswerRecord.fixture(correct: true, responseTime: 1)
        let slow = AnswerRecord.fixture(correct: true, responseTime: 60)
        let rules = ScoringRules.standard
        XCTAssertEqual(
            rules.xp(for: [fast], completed: true, currentStreak: 1, isFirstSessionToday: true, previouslyPlayedCategories: []),
            rules.xp(for: [slow], completed: true, currentStreak: 1, isFirstSessionToday: true, previouslyPlayedCategories: [])
        )
    }
}

final class StreakTests: XCTestCase {
    private var calendar: Calendar = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "UTC")!
        return calendar
    }()

    private func day(_ offset: Int, from now: Date) -> Date {
        calendar.date(byAdding: .day, value: offset, to: now)!
    }

    func testStreakCountsConsecutiveDaysIncludingToday() {
        let now = Date(timeIntervalSince1970: 1_760_000_000)
        let dates = [day(0, from: now), day(-1, from: now), day(-2, from: now), day(-4, from: now)]
        XCTAssertEqual(StreakCalculator(calendar: calendar).currentStreak(activityDates: dates, now: now), 3)
    }

    func testStreakSurvivesUntilTheEndOfToday() {
        let now = Date(timeIntervalSince1970: 1_760_000_000)
        let dates = [day(-1, from: now), day(-2, from: now)]
        XCTAssertEqual(StreakCalculator(calendar: calendar).currentStreak(activityDates: dates, now: now), 2)
    }

    func testStreakBreaksAfterMissedDay() {
        let now = Date(timeIntervalSince1970: 1_760_000_000)
        XCTAssertEqual(StreakCalculator(calendar: calendar).currentStreak(activityDates: [day(-2, from: now)], now: now), 0)
    }

    func testLongestStreak() {
        let now = Date(timeIntervalSince1970: 1_760_000_000)
        let dates = (0..<4).map { day(-$0, from: now) } + (10..<17).map { day(-$0, from: now) } + [day(-10, from: now)]
        XCTAssertEqual(StreakCalculator(calendar: calendar).longestStreak(activityDates: dates), 7)
    }
}

final class AchievementTests: XCTestCase {
    func testAchievementsUnlockFromSnapshot() {
        var snapshot = ProgressSnapshot(totalAnswered: 50, totalCorrect: 1, longestStreak: 7, openedArticleCount: 3)
        snapshot.answeredByCategory = Dictionary(uniqueKeysWithValues: ScienceCategory.allCases.map { ($0, 1) })
        let unlocked = Achievement.unlocked(in: snapshot)
        XCTAssertEqual(unlocked, [.firstDiscovery, .curiousMind, .scienceExplorer, .sevenDayStreak])
        XCTAssertEqual(Achievement.researchEnthusiast.progress(in: snapshot), 3)
    }
}

final class ArticleReferenceTests: XCTestCase {
    func testLinksAndCitation() {
        let article = ArticleReference.fixture
        XCTAssertEqual(article.pubMedURL.absoluteString, "https://pubmed.ncbi.nlm.nih.gov/17379808/")
        XCTAssertEqual(article.doiURL?.absoluteString, "https://doi.org/10.1126/science.1138140")
        XCTAssertTrue(article.citation.contains("Barrangou R, Fremaux C, et al."))
        XCTAssertTrue(article.citation.hasSuffix("PMID: 17379808."))
    }

    func testEvidenceKind() {
        XCTAssertEqual(EvidenceKind(publicationTypes: ["Journal Article"]), .singleStudy)
        XCTAssertEqual(EvidenceKind(publicationTypes: ["Journal Article", "Review"]), .narrativeReview)
        XCTAssertEqual(EvidenceKind(publicationTypes: ["Meta-Analysis", "Review"]), .evidenceSynthesis)
    }

    func testSyncMessageRoundTrip() throws {
        let pack = ChallengePack(id: "p", day: Date(timeIntervalSince1970: 1_760_000_000), language: .es,
                                 questions: [.fixture(), .fixture(excerpt: nil)])
        XCTAssertEqual(pack.questions.count, 1, "Unverified questions must not be packed")
        let message = SyncMessage.state(pack, sessions: [])
        let decoded = try SyncMessage.decode(message.encoded())
        XCTAssertEqual(decoded, message)
    }
}

// MARK: - Fixtures

extension ArticleReference {
    static let fixture = ArticleReference(
        pmid: "17379808",
        title: "CRISPR provides acquired resistance against viruses in prokaryotes.",
        authors: ["Barrangou R", "Fremaux C", "Deveau H"],
        journal: "Science",
        year: 2007,
        doi: "10.1126/science.1138140",
        abstract: "We found that, after viral challenge, bacteria integrated new spacers derived from phage genomic sequences.",
        publicationTypes: ["Journal Article"]
    )
}

extension Question {
    static func fixture(excerpt: String? = "bacteria integrated new spacers") -> Question {
        Question(
            id: "q-en", translationKey: "q", language: .en, category: .microbiology, difficulty: .curious,
            prompt: "What did bacteria integrate after viral challenge?",
            options: ["New spacers", "Plasmids", "Ribosomes", "Nothing"], correctOptionIndex: 0,
            explanation: "They integrated spacers derived from phage sequences.",
            source: .fixture,
            verification: SourceVerification(status: .verified, method: .editorialReview, supportingExcerpt: excerpt)
        )
    }
}

extension AnswerRecord {
    static func fixture(correct: Bool, category: ScienceCategory = .microbiology, responseTime: TimeInterval = 5) -> AnswerRecord {
        var question = Question.fixture()
        question.category = category
        return AnswerRecord(question: question, selectedOptionIndex: correct ? 0 : 1,
                            answeredAt: Date(), responseTime: responseTime)
    }
}
