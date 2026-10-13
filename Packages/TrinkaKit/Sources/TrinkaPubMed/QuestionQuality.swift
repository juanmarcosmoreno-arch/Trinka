import Foundation
import TrinkaCore

/// Picks the sentences of an abstract worth asking about: findings and conclusions rather than
/// background, aims or methods. Small on-device models write much better questions when they get
/// one informative sentence instead of a whole abstract, and the sentence doubles as the verbatim
/// supporting excerpt.
public enum KeySentences {
    private static let findingCues = [
        "found", "showed", "shows", "demonstrated", "revealed", "identified", "associated", "increased",
        "decreased", "reduced", "higher", "lower", "significant", "resulted", "caused", "causes", "is a",
        "are the", "remains", "most common", "leading cause", "conclude", "suggest", "indicate", "%",
        "p <", "p=", "required", "essential", "inhibit", "produce", "mediate", "responsible for",
    ]
    private static let skipCues = [
        "the aim", "this study aimed", "we aimed", "objective", "we performed", "we conducted", "were enrolled",
        "were recruited", "this review", "in this article", "this activity", "we searched", "we describe",
        "we review", "we discuss", "here we", "were included", "retrospective", "data were collected",
        "funded by", "clinicaltrials.gov", "further research", "more studies", "is needed", "are needed",
    ]

    /// Up to `limit` sentences, best first. Each is copied verbatim from the abstract.
    public static func pick(from abstract: String, limit: Int = 3) -> [String] {
        let sections = labeledSections(abstract)
        var scored: [(score: Int, index: Int, text: String)] = []
        for (index, item) in sections.enumerated() {
            let sentence = item.text
            let lower = sentence.lowercased()
            guard (60...320).contains(sentence.count), !skipCues.contains(where: lower.contains) else { continue }
            var score = findingCues.filter { lower.contains($0) }.count
            if let label = item.label?.uppercased() {
                if label.contains("RESULT") || label.contains("CONCLUSION") || label.contains("FINDING") { score += 3 }
                if label.contains("METHOD") || label.contains("BACKGROUND") || label.contains("OBJECTIVE") { score -= 3 }
            }
            if score > 0 { scored.append((score, index, sentence)) }
        }
        return scored.sorted { $0.score != $1.score ? $0.score > $1.score : $0.index < $1.index }
            .prefix(limit).map(\.text)
    }

    /// Sentences with the structured-abstract label ("RESULTS:", "CONCLUSIONS:"…) they fall under.
    static func labeledSections(_ abstract: String) -> [(label: String?, text: String)] {
        var result: [(String?, String)] = []
        for line in abstract.components(separatedBy: "\n") where !line.trimmingCharacters(in: .whitespaces).isEmpty {
            var label: String?
            var body = line
            if let colon = line.firstIndex(of: ":") {
                let candidate = String(line[..<colon])
                if candidate == candidate.uppercased(), candidate.count < 40, candidate.contains(where: \.isLetter) {
                    label = candidate
                    body = String(line[line.index(after: colon)...]).trimmingCharacters(in: .whitespaces)
                }
            }
            for sentence in ArticleDigest.sentences(in: body) {
                // Keep the exact text so it can be found verbatim in the abstract.
                result.append((label, sentence))
            }
        }
        return result
    }
}

/// Cheap checks that discard weak multiple-choice drafts before verification.
public enum QuestionQuality {
    public enum Issue: Equatable, Sendable {
        case promptTooShort
        case answerInPrompt
        case catchAllOption
        case duplicateOptions
        case trivia
        case unbalancedOptions
    }

    private static let catchAll = ["all of the above", "none of the above", "todas las anteriores",
                                   "ninguna de las anteriores", "all of these", "todas las opciones"]
    private static let triviaCues = ["what year", "which year", "how many authors", "which journal",
                                     "qué año", "en qué año", "cuántos autores", "qué revista", "how many participants",
                                     "cuántos participantes", "cuántos pacientes", "how many patients"]

    public static func issues(prompt: String, options: [String], correctIndex: Int) -> [Issue] {
        var issues: [Issue] = []
        let cleanPrompt = prompt.trimmingCharacters(in: .whitespacesAndNewlines)
        let lowerPrompt = cleanPrompt.lowercased()
        let normalized = options.map { $0.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() }

        if cleanPrompt.count < 20 { issues.append(.promptTooShort) }
        if options.indices.contains(correctIndex) {
            let answer = normalized[correctIndex]
            if answer.count >= 4, lowerPrompt.contains(answer) { issues.append(.answerInPrompt) }
            // "Pick the longest (or shortest) option" must not beat chance: the correct option may be
            // at most ~30% longer than the longest distractor and not much shorter than the shortest.
            let others = normalized.enumerated().filter { $0.offset != correctIndex }.map(\.element.count)
            if let longest = others.max(), let shortest = others.min(), longest > 0 {
                let tooLong = Double(answer.count) > max(Double(longest) * 1.3, Double(longest + 12))
                let tooShort = Double(answer.count) < min(Double(shortest) * 0.6, Double(shortest - 12))
                if tooLong || tooShort { issues.append(.unbalancedOptions) }
            }
        }
        if normalized.contains(where: { option in catchAll.contains { option.contains($0) } }) { issues.append(.catchAllOption) }
        if Set(normalized).count != normalized.count || normalized.contains(where: \.isEmpty) { issues.append(.duplicateOptions) }
        if triviaCues.contains(where: lowerPrompt.contains) { issues.append(.trivia) }
        return issues
    }
}
