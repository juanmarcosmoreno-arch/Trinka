import Foundation

/// Problems that disqualify a question from being shown.
public enum QuestionIssue: Equatable, Sendable {
    case emptyPrompt
    case wrongOptionCount(Int)
    case emptyOption(index: Int)
    case duplicateOptions
    case correctIndexOutOfRange(Int)
    case emptyExplanation
    case invalidPMID(String)
    case missingSourceTitle
    case notVerified(SourceVerification.Status)
    case missingSupportingExcerpt
    case excerptNotFoundInSource
}

/// Gatekeeper that decides whether a question may be presented to users.
///
/// TRINKA's core rule: a question is only playable when its correct answer is backed by a
/// verbatim excerpt of the cited source and its verification status is `.verified`.
/// Ambiguous, malformed or unverifiable questions are discarded.
public enum QuestionValidator {
    /// All issues found in `question`. Empty means playable.
    public static func issues(in question: Question) -> [QuestionIssue] {
        var issues: [QuestionIssue] = []

        if question.prompt.trimmed.isEmpty { issues.append(.emptyPrompt) }

        if question.options.count != Question.optionCount {
            issues.append(.wrongOptionCount(question.options.count))
        }
        for (index, option) in question.options.enumerated() where option.trimmed.isEmpty {
            issues.append(.emptyOption(index: index))
        }
        let normalizedOptions = question.options.map(EvidenceMatcher.normalize)
        if Set(normalizedOptions).count != normalizedOptions.count {
            issues.append(.duplicateOptions)
        }
        if !question.options.indices.contains(question.correctOptionIndex) {
            issues.append(.correctIndexOutOfRange(question.correctOptionIndex))
        }
        if question.explanation.trimmed.isEmpty { issues.append(.emptyExplanation) }

        if !isValidPMID(question.source.pmid) { issues.append(.invalidPMID(question.source.pmid)) }
        if question.source.title.trimmed.isEmpty { issues.append(.missingSourceTitle) }

        if question.verification.status != .verified {
            issues.append(.notVerified(question.verification.status))
        }

        if let excerpt = question.verification.supportingExcerpt, !excerpt.trimmed.isEmpty {
            // When the abstract is available we can check the excerpt ourselves.
            if !EvidenceMatcher.source(question.source, contains: excerpt) {
                issues.append(.excerptNotFoundInSource)
            }
        } else {
            issues.append(.missingSupportingExcerpt)
        }

        return issues
    }

    public static func isPlayable(_ question: Question) -> Bool {
        issues(in: question).isEmpty
    }

    /// PMIDs are positive integers.
    public static func isValidPMID(_ pmid: String) -> Bool {
        !pmid.isEmpty && pmid.allSatisfy(\.isASCIIDigit) && pmid.first != "0"
    }
}

/// Checks that a supporting excerpt literally appears in a source's title or abstract.
public enum EvidenceMatcher {
    /// Lowercases and collapses all whitespace (including non-breaking spaces) to single spaces.
    public static func normalize(_ text: String) -> String {
        text.lowercased()
            .components(separatedBy: .whitespacesAndNewlines)
            .filter { !$0.isEmpty }
            .joined(separator: " ")
    }

    /// `true` when `excerpt` appears in the title or abstract.
    /// Without an abstract, only the title can be checked.
    public static func source(_ source: ArticleReference, contains excerpt: String) -> Bool {
        let needle = normalize(excerpt)
        guard !needle.isEmpty else { return false }
        let haystack = normalize(source.title + "\n" + (source.abstract ?? ""))
        return haystack.contains(needle)
    }
}

extension Character {
    var isASCIIDigit: Bool { ("0"..."9").contains(self) }
}

extension String {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}
