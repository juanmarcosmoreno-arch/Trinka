import XCTest
import TrinkaCore
@testable import TrinkaQuiz

final class SeedQuestionBankTests: XCTestCase {
    func testEverySeedQuestionIsPlayableAndSourced() throws {
        let bank = try SeedQuestionBank.load()
        XCTAssertTrue(bank.rejected.isEmpty, "Rejected seed questions: \(bank.rejected.map { ($0.question.id, $0.issues) })")
        for language in AppLanguage.allCases {
            let questions = bank.questions(in: language)
            XCTAssertEqual(questions.count, 30, "\(language)")
            XCTAssertEqual(Set(questions.map(\.category)), Set(ScienceCategory.allCases))
            for question in questions {
                XCTAssertNotNil(question.source.abstract, question.id)
                XCTAssertEqual(question.language, language)
            }
        }
    }

    func testEveryQuestionHasBothTranslationsWithTheSameAnswer() throws {
        let bank = try SeedQuestionBank.load()
        let english = Dictionary(uniqueKeysWithValues: bank.questions(in: .en).map { ($0.translationKey, $0) })
        let spanish = Dictionary(uniqueKeysWithValues: bank.questions(in: .es).map { ($0.translationKey, $0) })
        XCTAssertEqual(Set(english.keys), Set(spanish.keys))
        for (key, en) in english {
            let es = try XCTUnwrap(spanish[key])
            XCTAssertEqual(en.correctOptionIndex, es.correctOptionIndex, key)
            XCTAssertEqual(en.source.pmid, es.source.pmid, key)
            XCTAssertEqual(en.difficulty, es.difficulty, key)
        }
    }

    func testEveryDifficultyIsRepresented() throws {
        let bank = try SeedQuestionBank.load()
        XCTAssertEqual(Set(bank.questions(in: .en).map(\.difficulty)), Set(Difficulty.allCases))
    }
}

final class QuestionSelectorTests: XCTestCase {
    private let selector: QuestionSelector = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "UTC")!
        return QuestionSelector(calendar: calendar)
    }()

    func testDailyChallengeIsDeterministicPerDay() throws {
        let bank = try SeedQuestionBank.load()
        let morning = Date(timeIntervalSince1970: 1_760_000_000)
        let evening = morning.addingTimeInterval(3600 * 5)
        let first = selector.dailyChallenge(from: bank, language: .en, date: morning)
        XCTAssertEqual(first.map(\.id), selector.dailyChallenge(from: bank, language: .en, date: evening).map(\.id))
        XCTAssertEqual(first.count, QuestionSelector.dailyChallengeSize)
        XCTAssertEqual(Set(first.map(\.category)).count, first.count, "One question per category")

        let nextDay = selector.dailyChallenge(from: bank, language: .en, date: morning.addingTimeInterval(86_400))
        XCTAssertNotEqual(first.map(\.id), nextDay.map(\.id))
    }

    func testDailyChallengeIsOrderedByDifficulty() throws {
        let bank = try SeedQuestionBank.load()
        let questions = selector.dailyChallenge(from: bank, language: .es, date: Date(timeIntervalSince1970: 1_760_000_000))
        XCTAssertEqual(questions.map(\.difficulty), questions.map(\.difficulty).sorted())
    }

    func testCustomQuizRespectsFiltersAndPrefersUnseen() throws {
        let bank = try SeedQuestionBank.load()
        var generator = SeededGenerator(seed: 42)
        let all = bank.questions(in: .en, category: .microbiology)
        let seen = Set(all.prefix(2).map(\.translationKey))
        let quiz = selector.customQuiz(from: bank, language: .en, category: .microbiology, difficulty: nil,
                                       count: 1, recentlySeen: seen, using: &generator)
        XCTAssertEqual(quiz.count, 1)
        XCTAssertFalse(seen.contains(quiz[0].translationKey))

        let researcher = selector.customQuiz(from: bank, language: .en, category: nil, difficulty: .researcher,
                                             count: 20, using: &generator)
        XCTAssertFalse(researcher.isEmpty)
        XCTAssertTrue(researcher.allSatisfy { $0.difficulty == .researcher })
    }
}

final class QuizEngineTests: XCTestCase {
    private func makeEngine(timeLimit: TimeInterval? = nil, start: Date) throws -> QuizEngine {
        let bank = try SeedQuestionBank.load()
        let questions = Array(bank.questions(in: .en).prefix(3))
        return QuizEngine(questions: questions, kind: .daily, origin: .iPhone, language: .en,
                          timeLimit: timeLimit, startedAt: start)
    }

    func testFullSessionFlow() throws {
        let start = Date(timeIntervalSince1970: 1_000)
        var engine = try makeEngine(start: start)
        XCTAssertEqual(engine.phase, .answering)

        for (offset, question) in engine.questions.enumerated() {
            let pick = offset == 0 ? (question.correctOptionIndex + 1) % 4 : question.correctOptionIndex
            let record = try XCTUnwrap(engine.submit(optionIndex: pick, at: start.addingTimeInterval(Double(offset * 10 + 4))))
            XCTAssertEqual(record.isCorrect, offset != 0)
            // Second submission for the same question is ignored.
            XCTAssertNil(engine.submit(optionIndex: 0, at: start))
            engine.advance(at: start.addingTimeInterval(Double(offset * 10 + 10)))
        }

        XCTAssertTrue(engine.isFinished)
        XCTAssertEqual(engine.correctCount, 2)
        let result = try XCTUnwrap(engine.result(currentStreak: 1, isFirstSessionToday: true, previouslyPlayedCategories: []))
        XCTAssertEqual(result.totalCount, 3)
        XCTAssertEqual(result.accuracy, 2.0 / 3.0, accuracy: 0.0001)
        XCTAssertEqual(result.duration, 30)
        XCTAssertEqual(result.answers[0].responseTime, 4)
        XCTAssertEqual(result.answers[1].responseTime, 4)
        XCTAssertGreaterThan(result.xp.total, 0)
    }

    func testTimerExpiryRecordsTimeout() throws {
        let start = Date(timeIntervalSince1970: 1_000)
        var engine = try makeEngine(timeLimit: 15, start: start)
        XCTAssertEqual(engine.remainingTime(at: start.addingTimeInterval(5)), 10)
        let record = try XCTUnwrap(engine.submit(optionIndex: engine.currentQuestion!.correctOptionIndex,
                                                 at: start.addingTimeInterval(20)))
        XCTAssertTrue(record.timedOut)
        XCTAssertFalse(record.isCorrect)
    }

    func testUnverifiedQuestionsAreNeverPresented() throws {
        let bank = try SeedQuestionBank.load()
        var question = bank.questions(in: .en)[0]
        question.verification.status = .needsReview
        let engine = QuizEngine(questions: [question], kind: .explore, origin: .iPhone, language: .en)
        XCTAssertTrue(engine.isFinished)
        XCTAssertNil(engine.currentQuestion)
    }
}
