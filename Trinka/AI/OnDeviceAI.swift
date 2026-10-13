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
    @Guide(description: "A multiple-choice question that can be answered using only the abstract")
    var prompt: String
    @Guide(description: "The correct answer, short")
    var correctAnswer: String
    @Guide(description: "Three short wrong but plausible answers")
    var wrongAnswers: [String]
    @Guide(description: "One or two sentences explaining why the correct answer is right")
    var explanation: String
    @Guide(description: "One sentence copied word for word, in English, from the abstract, that proves the correct answer")
    var supportingSentence: String
}

@available(iOS 26.0, *)
@Generable
struct GeneratedQuestionSet {
    @Guide(description: "The questions")
    var questions: [GeneratedQuestion]
}

/// Generates quiz drafts from one abstract with the on-device model. Drafts go through
/// `QuestionVerificationPipeline` like any other, so anything not backed by the abstract is dropped.
@available(iOS 26.0, *)
struct OnDeviceQuestionGenerator: QuestionGenerating {
    let category: ScienceCategory

    func generateDrafts(for article: ArticleReference, language: AppLanguage,
                        difficulty: Difficulty, count: Int) async throws -> [QuestionDraft] {
        guard let abstract = article.abstract, abstract.count >= 200 else { return [] }
        let generated: GeneratedQuestionSet
        do {
            generated = try await generate(article: article, abstract: abstract, language: language,
                                           difficulty: difficulty, count: max(1, min(count, 3)), abstractLimit: 1500)
        } catch {
            // Retry once with a smaller request (shorter abstract, one question).
            do {
                generated = try await generate(article: article, abstract: abstract, language: language,
                                               difficulty: difficulty, count: 1, abstractLimit: 900)
            } catch {
                throw QuestionGenerationError.onDevice(OnDeviceAI.describe(error))
            }
        }

        return generated.questions.compactMap { item -> QuestionDraft? in
            let wrong = Array(item.wrongAnswers.map { $0.trimmingCharacters(in: .whitespaces) }
                .filter { !$0.isEmpty && $0.caseInsensitiveCompare(item.correctAnswer) != .orderedSame }
                .prefix(3))
            guard wrong.count == 3,
                  let excerpt = AbstractQuote.snap(item.supportingSentence, to: abstract) else { return nil }
            var options = wrong
            let correctIndex = Int.random(in: 0...3)
            options.insert(item.correctAnswer.trimmingCharacters(in: .whitespaces), at: correctIndex)
            return QuestionDraft(pmid: article.pmid, language: language, category: category, difficulty: difficulty,
                                 prompt: item.prompt, options: options, correctOptionIndex: correctIndex,
                                 explanation: item.explanation, supportingExcerpt: excerpt)
        }
    }

    private func generate(article: ArticleReference, abstract: String, language: AppLanguage,
                          difficulty: Difficulty, count: Int, abstractLimit: Int) async throws -> GeneratedQuestionSet {
        let languageName = language == .es ? "Spanish" : "English"
        let session = LanguageModelSession(instructions: """
            You write multiple-choice quiz questions for students from a scientific abstract. \
            Write the question, answers and explanation in \(languageName). \
            Level: \(Self.levelDescription(difficulty)). \
            Every question must be answerable from the abstract alone. The supporting sentence must be \
            copied exactly from the abstract, in English, without changes.
            """)
        let prompt = "Write \(count) questions.\n\nTitle: \(article.title)\n\nAbstract:\n\(abstract.prefix(abstractLimit))"
        return try await session.respond(to: prompt, generating: GeneratedQuestionSet.self).content
    }

    private static func levelDescription(_ difficulty: Difficulty) -> String {
        switch difficulty {
        case .beginner: "very basic, for someone new to the subject"
        case .curious: "basic, introductory university level"
        case .explorer: "intermediate university level"
        case .researcher: "advanced, for graduate students"
        case .expert: "expert, for researchers in the field"
        }
    }
}

#endif
