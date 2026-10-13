import XCTest
import TrinkaCore
@testable import TrinkaQuiz

final class SeedQuestionBankTests: XCTestCase {
    func testEverySeedQuestionIsPlayableAndSourced() throws {
        let bank = try SeedQuestionBank.load()
        XCTAssertTrue(bank.rejected.isEmpty, "Rejected seed questions: \(bank.rejected.map { ($0.question.id, $0.issues) })")
        for language in AppLanguage.allCases {
            let questions = bank.questions(in: language)
            XCTAssertEqual(questions.count, 70, "\(language)")
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
        // Every discipline has at least one basic question.
        XCTAssertEqual(Set(bank.questions(in: .en, difficulty: .beginner).map(\.category)), Set(ScienceCategory.allCases))
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

    func testDailyChallengeFollowsTheChosenLevel() throws {
        let bank = try SeedQuestionBank.load()
        let date = Date(timeIntervalSince1970: 1_760_000_000)
        let basic = selector.dailyChallenge(from: bank, language: .es, date: date, level: .beginner)
        XCTAssertEqual(basic.count, 5)
        XCTAssertTrue(basic.allSatisfy { $0.difficulty == .beginner })
        XCTAssertEqual(Set(basic.map(\.category)).count, 5)

        // Few questions at this level: the nearest levels fill in, never jumping far.
        for level in Difficulty.allCases {
            let questions = selector.dailyChallenge(from: bank, language: .en, date: date, level: level)
            XCTAssertEqual(questions.count, 5, "\(level)")
            XCTAssertTrue(questions.allSatisfy { abs($0.difficulty.level - level.level) <= 1 }, "\(level)")
        }
    }

    func testClosenessOrderingPrefersEasierNeighbors() throws {
        let bank = try SeedQuestionBank.load()
        let ordered = QuestionSelector.orderedByCloseness(bank.questions(in: .en), to: .explorer)
        let levels = ordered.map(\.difficulty)
        let firstCurious = try XCTUnwrap(levels.firstIndex(of: .curious))
        let firstResearcher = try XCTUnwrap(levels.firstIndex(of: .researcher))
        XCTAssertEqual(levels.first, .explorer)
        XCTAssertLessThan(firstCurious, firstResearcher)
        XCTAssertGreaterThan(try XCTUnwrap(levels.firstIndex(of: .beginner)), firstResearcher)
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

final class FriendChallengeTests: XCTestCase {
    func testCodeRoundTrip() throws {
        for category in [nil] + ScienceCategory.allCases.map(Optional.some) {
            for difficulty in [nil] + Difficulty.allCases.map(Optional.some) {
                let code = ChallengeCode(bankVersion: 2, category: category, difficulty: difficulty, questionCount: 15, seed: 0x3F_FFFF)
                XCTAssertTrue(code.code.hasPrefix("TRK-"))
                XCTAssertEqual(code.code.count, 15)
                XCTAssertEqual(ChallengeCode(code.code), code)
            }
        }
    }

    func testParsingIsForgivingButCatchesTypos() throws {
        let code = ChallengeCode(bankVersion: 1, category: .genetics, difficulty: .explorer, questionCount: 3, seed: 12345)
        let text = code.code
        XCTAssertEqual(ChallengeCode(text.lowercased().replacingOccurrences(of: "-", with: " ")), code)
        XCTAssertEqual(ChallengeCode(String(text.dropFirst(4))), code)

        var corrupted = Array(text)
        corrupted[6] = corrupted[6] == "Z" ? "Y" : "Z"
        XCTAssertNil(ChallengeCode(String(corrupted)))
        XCTAssertNil(ChallengeCode("TRK-12345"))
    }

    func testFriendsGetTheSameQuestionsInTheirLanguage() throws {
        let bank = try SeedQuestionBank.load()
        let code = ChallengeCode.random(bankVersion: SeedQuestionBank.version, category: nil, difficulty: nil, questionCount: 5)
        let english = code.questions(from: bank, bankVersion: SeedQuestionBank.version, language: .en)
        let spanish = code.questions(from: bank, bankVersion: SeedQuestionBank.version, language: .es)
        XCTAssertEqual(english.count, 5)
        XCTAssertEqual(english.map(\.translationKey), spanish.map(\.translationKey))
        XCTAssertTrue(spanish.allSatisfy { $0.language == .es })
        XCTAssertEqual(english.map(\.id), code.questions(from: bank, bankVersion: SeedQuestionBank.version, language: .en).map(\.id))
        XCTAssertTrue(code.questions(from: bank, bankVersion: SeedQuestionBank.version + 1, language: .en).isEmpty)
    }

    func testLinksRoundTrip() throws {
        let code = ChallengeCode(bankVersion: 1, category: .nutrition, difficulty: nil, questionCount: 3, seed: 99)
        XCTAssertEqual(FriendLink(url: code.inviteURL(title: "Lab group")), .challenge(code, title: "Lab group"))

        let entry = ChallengeEntry(playerName: "Ana María", correct: 2, total: 3, duration: 41,
                                   playedAt: Date(timeIntervalSince1970: 1_760_000_000), isLocalPlayer: true)
        guard case let .result(parsedCode, parsed) = FriendLink(url: entry.resultURL(for: code)) else {
            return XCTFail("Result link not parsed")
        }
        XCTAssertEqual(parsedCode, code)
        XCTAssertEqual(parsed.playerName, "Ana María")
        XCTAssertEqual(parsed.correct, 2)
        XCTAssertEqual(parsed.duration, 41)
        XCTAssertFalse(parsed.isLocalPlayer, "Received results are never the local player")

        XCTAssertNil(FriendLink(url: URL(string: "trinka://result?code=\(code.code)&name=X&correct=9&total=3&seconds=1")!))
        XCTAssertNil(FriendLink(url: URL(string: "https://example.com/challenge?code=\(code.code)")!))
    }

    func testLeaderboardRanksByCorrectThenTimeAndKeepsBestAttempt() {
        let base = Date(timeIntervalSince1970: 0)
        let entries = [
            ChallengeEntry(playerName: "Ana", correct: 4, total: 5, duration: 90, playedAt: base, isLocalPlayer: false),
            ChallengeEntry(playerName: "ana", correct: 5, total: 5, duration: 120, playedAt: base, isLocalPlayer: false),
            ChallengeEntry(playerName: "Leo", correct: 5, total: 5, duration: 60, playedAt: base, isLocalPlayer: false),
            ChallengeEntry(playerName: "Me", correct: 3, total: 5, duration: 30, playedAt: base, isLocalPlayer: true),
        ]
        XCTAssertEqual(Leaderboard.ranked(entries).map(\.playerName), ["Leo", "ana", "Me"])
    }
}

final class LevelFillTests: XCTestCase {
    func testCategoryQuizAtALevelFillsWithNearestLevels() throws {
        let bank = try SeedQuestionBank.load()
        var generator = SeededGenerator(seed: 7)
        // Immunology has no "curious" question in the seed bank.
        XCTAssertTrue(bank.questions(in: .en, category: .immunology, difficulty: .curious).count < 3)
        let quiz = QuestionSelector().customQuiz(from: bank, language: .en, category: .immunology, difficulty: .curious,
                                                 count: 3, fillWithNearestLevels: true, using: &generator)
        XCTAssertEqual(quiz.count, 3)
        XCTAssertTrue(quiz.allSatisfy { $0.category == .immunology })
        XCTAssertEqual(quiz.first?.difficulty, quiz.map(\.difficulty).min { abs($0.level - 2) < abs($1.level - 2) })
    }
}
