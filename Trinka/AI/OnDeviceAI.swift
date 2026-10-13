import Foundation
import TrinkaCore
import TrinkaPubMed
import TrinkaUI
#if canImport(FoundationModels)
import FoundationModels
#endif

/// Apple's on-device language model (Apple Intelligence), used for free, offline-capable
/// generation: questions from abstracts and answers grounded in PubMed. Nothing is sent to a
/// server and no keys are needed. Every output still goes through TRINKA's checks (verbatim
/// excerpts for questions, valid citations for answers).
enum OnDeviceAI {
    enum Status: Equatable {
        case available
        /// The device can't run Apple Intelligence (needs iPhone 15 Pro or newer).
        case deviceNotEligible
        /// Apple Intelligence is turned off in Settings.
        case notEnabled
        /// The model is still downloading.
        case modelNotReady
        /// iOS older than 26, or built with an SDK without Foundation Models.
        case unsupportedOS
    }

    static var status: Status {
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *) {
            switch SystemLanguageModel.default.availability {
            case .available:
                return .available
            case .unavailable(.deviceNotEligible):
                return .deviceNotEligible
            case .unavailable(.appleIntelligenceNotEnabled):
                return .notEnabled
            case .unavailable(.modelNotReady):
                return .modelNotReady
            case .unavailable:
                return .unsupportedOS
            }
        }
        #endif
        return .unsupportedOS
    }

    static var isAvailable: Bool { status == .available }

    /// Localization key explaining why on-device AI can't be used.
    static var statusMessageKey: String {
        switch status {
        case .available: "ai.status.available"
        case .deviceNotEligible: "ai.status.deviceNotEligible"
        case .notEnabled: "ai.status.notEnabled"
        case .modelNotReady: "ai.status.modelNotReady"
        case .unsupportedOS: "ai.status.unsupportedOS"
        }
    }

    static func composer() -> EvidenceComposing? {
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *), isAvailable { return OnDeviceEvidenceComposer() }
        #endif
        return nil
    }

    static func questionGenerator(category: ScienceCategory) -> QuestionGenerating? {
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *), isAvailable { return OnDeviceQuestionGenerator(category: category) }
        #endif
        return nil
    }

    /// Short, user-readable reason for a model error (shown so failures can be diagnosed).
    static func describe(_ error: Error) -> String {
        let detail = String(String(describing: error).prefix(140))
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *), let generationError = error as? LanguageModelSession.GenerationError {
            let reason: String
            switch generationError {
            case .guardrailViolation: reason = L10n.tr("ai.error.guardrail")
            case .exceededContextWindowSize: reason = L10n.tr("ai.error.context")
            case .unsupportedLanguageOrLocale: reason = L10n.tr("ai.error.language")
            case .rateLimited: reason = L10n.tr("ai.error.busy")
            case .assetsUnavailable: reason = L10n.tr("ai.error.assets")
            default: reason = generationError.localizedDescription
            }
            return "\(reason) (\(detail))"
        }
        #endif
        // Bridged form: "FoundationModels.LanguageModelSession.GenerationError", code = case index.
        let nsError = error as NSError
        if nsError.domain.contains("GenerationError") {
            let reasons = [0: "ai.error.context", 1: "ai.error.assets", 2: "ai.error.guardrail",
                           4: "ai.error.language", 6: "ai.error.busy", 7: "ai.error.busy"]
            if let key = reasons[nsError.code] { return "\(L10n.tr(key)) (code \(nsError.code))" }
        }
        return detail
    }

    /// English PubMed search terms for a topic or question typed in any language.
    static func searchTerms(for text: String) async -> String? {
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *), isAvailable {
            return try? await OnDeviceEvidenceComposer().searchTerms(for: text)
        }
        #endif
        return nil
    }
}

#if canImport(FoundationModels)

@available(iOS 26.0, *)
struct OnDeviceEvidenceComposer: EvidenceComposing {
    func searchTerms(for question: String) async throws -> String {
        let session = LanguageModelSession(instructions: """
            You turn a question or topic, in any language, into a short PubMed search in English. \
            Reply with 2 to 6 English keywords separated by spaces. No quotes, no punctuation, no explanation.
            """)
        let response = try await session.respond(to: question)
        let line = response.content.components(separatedBy: .newlines).first ?? ""
        let cleaned = line.filter { $0.isLetter || $0.isNumber || $0 == " " || $0 == "-" }
        return cleaned.trimmingCharacters(in: .whitespaces)
    }

    func answer(question: String, language: AppLanguage, sources: [ArticleReference]) async throws -> String {
        let languageName = language == .es ? "Spanish" : "English"
        let session = LanguageModelSession(instructions: """
            You answer questions for students using ONLY the numbered PubMed abstracts you are given. \
            Write 2 to 5 short sentences in \(languageName). End every sentence with the number of the \
            abstract that supports it in square brackets, for example [1] or [2]. \
            Never use knowledge that is not in the abstracts and never invent numbers. \
            If the abstracts do not answer the question, reply exactly: \(PubMedAnswerer.noEvidenceMarker)
            """)
        var prompt = "Question: \(question)\n\nAbstracts:\n"
        for (index, source) in sources.enumerated() {
            prompt += "[\(index + 1)] \(source.title)\n\(source.abstract ?? "")\n\n"
        }
        return try await session.respond(to: prompt).content
    }
}

@available(iOS 26.0, *)
@Generable
struct GeneratedQuestion {
    @Guide(description: "The question. It tests the key fact of the sentence and makes sense on its own, without the sentence")
    var prompt: String
    @Guide(description: "The correct answer: a short phrase stated in the sentence")
    var correctAnswer: String
    @Guide(description: "Three wrong answers of the same kind as the correct one, plausible for a student, each different, each about as long and as detailed as the correct answer")
    var wrongAnswers: [String]
    @Guide(description: "One or two sentences explaining why the correct answer is right")
    var explanation: String
}

@available(iOS 26.0, *)
@Generable
struct TranslatedQuestion {
    @Guide(description: "The question, translated")
    var prompt: String
    @Guide(description: "The correct answer, translated")
    var correctAnswer: String
    @Guide(description: "The three wrong answers, translated, in the same order")
    var wrongAnswers: [String]
    @Guide(description: "The explanation, translated")
    var explanation: String
}

/// Generates quiz drafts from one abstract with the on-device model.
///
/// Small models do best with small tasks, so TRINKA does the hard part itself:
/// 1. `KeySentences` picks the abstract's findings/conclusions (verbatim — they become the
///    supporting excerpt, so every question is anchored to real source text).
/// 2. The model writes one question per sentence, in English, following a worked example.
/// 3. For Spanish, a second short request translates it.
/// 4. `QuestionQuality` drops weak drafts; `QuestionVerificationPipeline` checks the rest.
@available(iOS 26.0, *)
struct OnDeviceQuestionGenerator: QuestionGenerating {
    let category: ScienceCategory

    func generateDrafts(for article: ArticleReference, language: AppLanguage,
                        difficulty: Difficulty, count: Int) async throws -> [QuestionDraft] {
        guard let abstract = article.abstract, abstract.count >= 200 else { return [] }
        let sentences = KeySentences.pick(from: abstract, limit: max(1, min(count, 3)))
        guard !sentences.isEmpty else { return [] }

        var drafts: [QuestionDraft] = []
        var lastError: Error?
        for sentence in sentences {
            do {
                if let draft = try await draft(from: sentence, article: article, language: language, difficulty: difficulty) {
                    drafts.append(draft)
                }
            } catch {
                lastError = error
            }
        }
        if drafts.isEmpty, let lastError {
            throw QuestionGenerationError.onDevice(OnDeviceAI.describe(lastError))
        }
        return drafts
    }

    private func draft(from sentence: String, article: ArticleReference, language: AppLanguage,
                       difficulty: Difficulty) async throws -> QuestionDraft? {
        let writer = LanguageModelSession(instructions: Self.writerInstructions(difficulty))
        let prompt = "Article title: \(article.title)\n\nSentence: \(sentence)"
        let generated = try await writer.respond(to: prompt, generating: GeneratedQuestion.self).content
        var questionText = generated.prompt
        var correctAnswer = generated.correctAnswer
        var wrongAnswers = generated.wrongAnswers
        var explanation = generated.explanation

        if language == .es {
            let translator = LanguageModelSession(instructions: """
                You translate quiz questions from English to Spanish for university students. \
                Use neutral Latin American Spanish and correct scientific terminology. \
                Keep organism names, gene names and drug names as used in Spanish textbooks. \
                Keep the meaning exactly; do not add or remove information.
                """)
            let source = """
                Question: \(questionText)
                Correct answer: \(correctAnswer)
                Wrong answers: \(wrongAnswers.joined(separator: " | "))
                Explanation: \(explanation)
                """
            let translated = try await translator.respond(to: source, generating: TranslatedQuestion.self).content
            questionText = translated.prompt
            correctAnswer = translated.correctAnswer
            wrongAnswers = translated.wrongAnswers
            explanation = translated.explanation
        }

        let correct = correctAnswer.trimmingCharacters(in: .whitespacesAndNewlines)
        var wrong: [String] = []
        for answer in wrongAnswers.map({ $0.trimmingCharacters(in: .whitespacesAndNewlines) })
        where !answer.isEmpty && answer.caseInsensitiveCompare(correct) != .orderedSame
            && !wrong.contains(where: { $0.caseInsensitiveCompare(answer) == .orderedSame }) {
            wrong.append(answer)
        }
        guard !correct.isEmpty, wrong.count >= 3 else { return nil }

        var options = Array(wrong.prefix(3))
        let correctIndex = Int.random(in: 0...3)
        options.insert(correct, at: correctIndex)
        guard QuestionQuality.issues(prompt: questionText, options: options, correctIndex: correctIndex).isEmpty else {
            return nil
        }
        return QuestionDraft(pmid: article.pmid, language: language, category: category, difficulty: difficulty,
                             prompt: questionText, options: options, correctOptionIndex: correctIndex,
                             explanation: explanation, supportingExcerpt: sentence)
    }

    private static func writerInstructions(_ difficulty: Difficulty) -> String {
        """
        You write one multiple-choice exam question for university science students, in English.
        You get one sentence from a scientific abstract. The question must test the key fact in that sentence.
        Level: \(levelDescription(difficulty)).

        Rules:
        - Ask about the finding, mechanism or concept, never about trivia (year, journal, authors, sample size).
        - The question must make sense on its own. Do not write "according to the sentence" or "in this study".
        - The correct answer must be stated in the sentence. Do not put the answer in the question.
        - Wrong answers: same kind as the correct answer (all drugs, all organisms, all numbers…), plausible, clearly wrong.
        - Never use "all of the above" or "none of the above".

        Example
        Sentence: Vancomycin remains a first-line option for severe MRSA infections in hospitals.
        Question: Which antibiotic remains a first-line option for severe MRSA infections in hospitals?
        Correct answer: Vancomycin
        Wrong answers: Amoxicillin; Penicillin G; Cephalexin
        Explanation: Vancomycin, a glycopeptide, stays active against methicillin-resistant S. aureus, unlike most beta-lactams.
        """
    }

    private static func levelDescription(_ difficulty: Difficulty) -> String {
        switch difficulty {
        case .beginner: "very basic: test one simple fact with everyday wording"
        case .curious: "introductory university level"
        case .explorer: "intermediate university level"
        case .researcher: "advanced: test mechanisms or interpretation"
        case .expert: "expert: test precise mechanisms, numbers or implications"
        }
    }
}

#endif
