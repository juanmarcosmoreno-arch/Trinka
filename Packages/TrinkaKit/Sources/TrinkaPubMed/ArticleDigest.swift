import Foundation
import TrinkaCore

/// Reader-friendly view of an article for Discover cards.
///
/// Built only from the article's own text: no summarization model is involved, so nothing
/// is added that the authors didn't write. AI-written plain-language summaries can be plugged
/// in later through the question/summary service, subject to the same verification rules.
public struct ArticleDigest: Hashable, Identifiable, Sendable {
    public let article: ArticleReference

    public init(article: ArticleReference) {
        self.article = article
    }

    public var id: String { article.pmid }

    /// Title without trailing period, subtitle after a colon, or leading all-caps section tag
    /// (e.g. "PSYCHOLOGY. Estimating…" → "Estimating…").
    public var shortTitle: String {
        var title = article.title.trimmingCharacters(in: .whitespacesAndNewlines)
        if let dot = title.firstIndex(of: "."), title.distance(from: title.startIndex, to: dot) < 25 {
            let head = title[..<dot]
            if head == head.uppercased(), head.contains(where: \.isLetter) {
                title = String(title[title.index(after: dot)...]).trimmingCharacters(in: .whitespaces)
            }
        }
        if let colon = title.firstIndex(of: ":"), title.distance(from: title.startIndex, to: colon) >= 20 {
            title = String(title[..<colon])
        }
        while title.hasSuffix(".") { title.removeLast() }
        return title
    }

    /// The authors' own conclusion: the labeled CONCLUSIONS section of a structured abstract,
    /// otherwise the abstract's final sentence. `nil` without an abstract.
    public var keyFinding: String? {
        guard let abstract = article.abstract, !abstract.isEmpty else { return nil }
        let sections = abstract.components(separatedBy: "\n")
        for section in sections {
            for label in ["CONCLUSIONS:", "CONCLUSION:", "CONCLUSIONS AND RELEVANCE:", "INTERPRETATION:"]
            where section.uppercased().hasPrefix(label) {
                return Self.stripTrialRegistration(String(section.dropFirst(label.count)).trimmingCharacters(in: .whitespaces))
            }
        }
        let sentences = Self.sentences(in: abstract)
        return sentences.last
    }

    /// First sentences of the abstract (without section labels), up to `maxCharacters`.
    public func summary(maxCharacters: Int = 320) -> String? {
        guard let abstract = article.abstract, !abstract.isEmpty else { return nil }
        let unlabeled = abstract.components(separatedBy: "\n").map { line -> String in
            guard let colon = line.firstIndex(of: ":") else { return line }
            let label = line[..<colon]
            return label == label.uppercased() && label.count < 40
                ? String(line[line.index(after: colon)...]).trimmingCharacters(in: .whitespaces)
                : line
        }.joined(separator: " ")
        var result = ""
        for sentence in Self.sentences(in: unlabeled) {
            if !result.isEmpty, result.count + sentence.count + 1 > maxCharacters { break }
            result += result.isEmpty ? sentence : " " + sentence
        }
        return result.isEmpty ? nil : result
    }

    /// Splits text into sentences at ". ", "? " or "! " followed by an uppercase letter or digit.
    /// Deliberately simple and portable; keeps decimals ("0.03") and initials mid-sentence intact
    /// in the common cases found in abstracts.
    static func sentences(in text: String) -> [String] {
        let characters = Array(text)
        var sentences: [String] = []
        var current = ""
        var index = 0
        while index < characters.count {
            let character = characters[index]
            current.append(character)
            if ".?!".contains(character), index + 2 < characters.count, characters[index + 1] == " ",
               characters[index + 2].isUppercase || characters[index + 2].isNumber {
                // Skip single-letter abbreviations such as "S. aureus".
                let words = current.split(separator: " ")
                if let last = words.last, last.count > 2 {
                    sentences.append(current.trimmingCharacters(in: .whitespacesAndNewlines))
                    current = ""
                }
            }
            index += 1
        }
        let rest = current.trimmingCharacters(in: .whitespacesAndNewlines)
        if !rest.isEmpty { sentences.append(rest) }
        return sentences
    }

    /// Removes "(Funded by …; ClinicalTrials.gov number …)" trailers.
    static func stripTrialRegistration(_ text: String) -> String {
        guard let range = text.range(of: "(Funded by") ?? text.range(of: "(ClinicalTrials.gov") else { return text }
        return text[..<range.lowerBound].trimmingCharacters(in: .whitespaces)
    }
}
