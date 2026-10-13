import Foundation
import TrinkaCore

// "Ask PubMed": answers a question using only PubMed abstracts, citing them.
//
// Flow: the question is (optionally) rewritten into an English PubMed search, the most relevant
// articles with abstracts are fetched, and a composer writes an answer from those abstracts only,
// citing them as [1], [2]… Every sentence must carry a citation to one of the articles it was
// given; sentences without a valid citation are dropped. If nothing survives — or no composer
// (on-device model) is available — the answer falls back to quoting the most relevant sentences
// of the abstracts verbatim, each with its citation. Nothing is invented: when the abstracts
// don't cover the question, the answer says so.

/// Writes answers from numbered abstracts (e.g. Apple's on-device model).
public protocol EvidenceComposing: Sendable {
    /// English PubMed search terms for a question asked in any language.
    func searchTerms(for question: String) async throws -> String
    /// An answer to `question` in `language` that uses only `sources` (numbered from 1) and cites
    /// them inline as [1], [2]…; or text stating that the sources don't answer it.
    func answer(question: String, language: AppLanguage, sources: [ArticleReference]) async throws -> String
}

public struct EvidenceAnswer: Hashable, Sendable {
    public enum Kind: String, Hashable, Sendable {
        /// Written by the composer from the abstracts; every sentence carries a verified citation.
        case synthesized
        /// Sentences quoted verbatim from the abstracts (in their original language).
        case quoted
        /// PubMed returned articles, but none addressed the question.
        case noEvidence
    }

    public struct Statement: Hashable, Sendable {
        /// Sentence text without citation markers.
        public var text: String
        /// 1-based indexes into `sources`.
        public var citations: [Int]
    }

    public var question: String
    public var kind: Kind
    public var statements: [Statement]
    /// Articles cited by `statements`, numbered in order of first citation.
    public var sources: [ArticleReference]
    /// PubMed search actually used.
    public var searchTerms: String
}

public enum EvidenceAnswerError: Error, Equatable, Sendable {
    case tooShort
    case offline
    case service
    case noArticles
}

/// Answers questions from PubMed abstracts only.
public struct PubMedAnswerer: Sendable {
    public let search: ArticleSearching
    public let composer: EvidenceComposing?
    /// Articles given to the composer; small, because on-device context windows are small.
    public var maxSources = 5
    /// Characters of each abstract given to the composer.
    public var abstractLimit = 900

    public init(search: ArticleSearching, composer: EvidenceComposing?) {
        self.search = search
        self.composer = composer
    }

    public func answer(_ rawQuestion: String, language: AppLanguage) async throws -> EvidenceAnswer {
        let question = rawQuestion.trimmingCharacters(in: .whitespacesAndNewlines)
        guard question.count >= 3 else { throw EvidenceAnswerError.tooShort }

        var terms = question
        if let composer, let rewritten = try? await composer.searchTerms(for: question),
           !rewritten.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
            terms = rewritten.trimmingCharacters(in: .whitespacesAndNewlines)
        }

        let found: [ArticleReference]
        do {
            found = try await search.searchArticles(PubMedQuery(topic: terms, requireAbstract: true, sort: .relevance, maxResults: 12))
        } catch PubMedError.offline {
            throw EvidenceAnswerError.offline
        } catch {
            throw EvidenceAnswerError.service
        }
        let usable = found.filter { ($0.abstract?.count ?? 0) >= 150 }
        guard !usable.isEmpty else { throw EvidenceAnswerError.noArticles }
        let sources = Array(usable.prefix(maxSources))

        if let composer {
            let trimmed = sources.map { article -> ArticleReference in
                var copy = article
                copy.abstract = article.abstract.map { String($0.prefix(abstractLimit)) }
                return copy
            }
            if let text = try? await composer.answer(question: question, language: language, sources: trimmed) {
                if text.contains(Self.noEvidenceMarker) {
                    return EvidenceAnswer(question: question, kind: .noEvidence, statements: [], sources: sources, searchTerms: terms)
                }
                let statements = Self.citedStatements(in: text, sourceCount: sources.count)
                if !statements.isEmpty {
                    return Self.numbered(question: question, kind: .synthesized, statements: statements,
                                         sources: sources, terms: terms)
                }
            }
        }

        let quoted = Self.quotedStatements(for: question + " " + terms, sources: sources)
        guard !quoted.isEmpty else {
            return EvidenceAnswer(question: question, kind: .noEvidence, statements: [], sources: sources, searchTerms: terms)
        }
        return Self.numbered(question: question, kind: .quoted, statements: quoted, sources: sources, terms: terms)
    }

    /// What a composer replies when the abstracts don't answer the question.
    public static let noEvidenceMarker = "NO_EVIDENCE"

    // MARK: - Citation checking

    /// Splits `text` into sentences and keeps only those citing at least one valid source.
    static func citedStatements(in text: String, sourceCount: Int) -> [EvidenceAnswer.Statement] {
        let pattern = try! NSRegularExpression(pattern: #"\[(\d+(?:\s*[,–-]\s*\d+)*)\]"#)
        var statements: [EvidenceAnswer.Statement] = []
        for sentence in ArticleDigest.sentences(in: text.replacingOccurrences(of: "\n", with: " ")) {
            let range = NSRange(sentence.startIndex..., in: sentence)
            var citations: [Int] = []
            for match in pattern.matches(in: sentence, range: range) {
                guard let inner = Range(match.range(at: 1), in: sentence) else { continue }
                let parts = sentence[inner].split(whereSeparator: { ",–-".contains($0) })
                    .compactMap { Int($0.trimmingCharacters(in: .whitespaces)) }
                citations += parts.filter { (1...sourceCount).contains($0) }
            }
            let clean = pattern.stringByReplacingMatches(in: sentence, range: range, withTemplate: "")
                .replacingOccurrences(of: " .", with: ".")
                .replacingOccurrences(of: "  ", with: " ")
                .trimmingCharacters(in: .whitespaces)
            if !citations.isEmpty, clean.count > 8 {
                var unique: [Int] = []
                for c in citations where !unique.contains(c) { unique.append(c) }
                statements.append(.init(text: clean, citations: unique))
            }
        }
        return statements
    }

    /// Renumbers citations by order of first appearance and keeps only cited sources.
    static func numbered(question: String, kind: EvidenceAnswer.Kind, statements: [EvidenceAnswer.Statement],
                         sources: [ArticleReference], terms: String) -> EvidenceAnswer {
        var order: [Int] = []
        for statement in statements { for c in statement.citations where !order.contains(c) { order.append(c) } }
        let remap = Dictionary(uniqueKeysWithValues: order.enumerated().map { ($1, $0 + 1) })
        let renumbered = statements.map { EvidenceAnswer.Statement(text: $0.text, citations: $0.citations.compactMap { remap[$0] }) }
        return EvidenceAnswer(question: question, kind: kind, statements: renumbered,
                              sources: order.map { sources[$0 - 1] }, searchTerms: terms)
    }

    // MARK: - Extractive fallback

    private static let stopwords: Set<String> = [
        "what", "which", "when", "where", "does", "with", "from", "that", "this", "these", "those", "have",
        "into", "about", "there", "their", "they", "were", "been", "being", "than", "then", "also", "such",
        "como", "cual", "cuál", "cuales", "cuáles", "cuando", "donde", "dónde", "para", "porque", "sobre",
        "entre", "tiene", "tienen", "esta", "este", "estos", "estas", "puede", "pueden", "qué", "quien",
        "quién", "hace", "hacen", "causa", "sirve", "funciona",
    ]

    static func keywords(in text: String) -> Set<String> {
        Set(text.lowercased().split(whereSeparator: { !$0.isLetter && !$0.isNumber })
            .map(String.init)
            .filter { $0.count >= 4 && !stopwords.contains($0) })
    }

    /// Up to three abstract sentences sharing the most keywords with the question, quoted verbatim.
    static func quotedStatements(for query: String, sources: [ArticleReference]) -> [EvidenceAnswer.Statement] {
        let words = keywords(in: query)
        guard !words.isEmpty else { return [] }
        var scored: [(score: Int, source: Int, text: String)] = []
        for (index, article) in sources.enumerated() {
            guard let abstract = article.abstract else { continue }
            for sentence in ArticleDigest.sentences(in: abstract) where sentence.count >= 40 {
                let score = keywords(in: sentence).intersection(words).count
                if score > 0 { scored.append((score, index + 1, sentence)) }
            }
        }
        let best = scored.sorted { $0.score != $1.score ? $0.score > $1.score : $0.source < $1.source }
        var picked: [EvidenceAnswer.Statement] = []
        var perSource: [Int: Int] = [:]
        for candidate in best where perSource[candidate.source, default: 0] < 1 {
            picked.append(.init(text: candidate.text, citations: [candidate.source]))
            perSource[candidate.source, default: 0] += 1
            if picked.count == 3 { break }
        }
        return picked
    }
}

/// Helpers for on-device generators, whose "verbatim" quotes are often slightly paraphrased.
public enum AbstractQuote {
    /// Returns `excerpt` if it already appears in `abstract`; otherwise the abstract sentence that
    /// shares most of its words (Jaccard similarity ≥ `minimumSimilarity`), or `nil`. The result
    /// is always text taken from the abstract, so verification still runs on real source text.
    public static func snap(_ excerpt: String, to abstract: String, minimumSimilarity: Double = 0.6) -> String? {
        let trimmed = excerpt.trimmingCharacters(in: .whitespacesAndNewlines.union(CharacterSet(charactersIn: "\"“”")))
        if !trimmed.isEmpty, abstract.range(of: trimmed, options: [.caseInsensitive]) != nil { return trimmed }
        let target = PubMedAnswerer.keywords(in: trimmed)
        guard !target.isEmpty else { return nil }
        var best: (score: Double, sentence: String)?
        for sentence in ArticleDigest.sentences(in: abstract) {
            let words = PubMedAnswerer.keywords(in: sentence)
            let union = words.union(target).count
            guard union > 0 else { continue }
            let score = Double(words.intersection(target).count) / Double(union)
            if score > (best?.score ?? 0) { best = (score, sentence) }
        }
        guard let best, best.score >= minimumSimilarity else { return nil }
        return best.sentence
    }
}
