import Foundation

/// Bibliographic metadata for a PubMed article.
///
/// Every question in TRINKA points to one of these, so users can always open the
/// original source. Instances are only created from data retrieved from PubMed
/// (or bundled copies of it) — never invented.
public struct ArticleReference: Codable, Hashable, Identifiable, Sendable {
    public var pmid: String
    public var title: String
    public var authors: [String]
    public var journal: String
    public var year: Int
    public var doi: String?
    public var abstract: String?
    public var publicationTypes: [String]

    public var id: String { pmid }

    public init(
        pmid: String,
        title: String,
        authors: [String],
        journal: String,
        year: Int,
        doi: String? = nil,
        abstract: String? = nil,
        publicationTypes: [String] = []
    ) {
        self.pmid = pmid
        self.title = title
        self.authors = authors
        self.journal = journal
        self.year = year
        self.doi = doi
        self.abstract = abstract
        self.publicationTypes = publicationTypes
    }

    /// Canonical PubMed page for the article.
    public var pubMedURL: URL {
        URL(string: "https://pubmed.ncbi.nlm.nih.gov/\(pmid)/")!
    }

    /// Publisher link resolved through doi.org, when a DOI is available.
    public var doiURL: URL? {
        guard let doi, !doi.isEmpty else { return nil }
        return URL(string: "https://doi.org/\(doi)")
    }

    /// "Smith J, Doe A, et al." style author line.
    public var shortAuthorList: String {
        switch authors.count {
        case 0: return ""
        case 1: return authors[0]
        case 2: return "\(authors[0]), \(authors[1])"
        default: return "\(authors[0]), \(authors[1]), et al."
        }
    }

    /// Vancouver-like citation, e.g. "Barrangou R, Fremaux C, et al. CRISPR provides… Science. 2007. PMID: 17379808."
    public var citation: String {
        var parts: [String] = []
        if !shortAuthorList.isEmpty { parts.append(shortAuthorList + ".") }
        parts.append(title.hasSuffix(".") ? title : title + ".")
        parts.append("\(journal). \(year).")
        if let doi, !doi.isEmpty { parts.append("doi:\(doi).") }
        parts.append("PMID: \(pmid).")
        return parts.joined(separator: " ")
    }

    /// Kind of evidence the publication represents, derived from its PubMed publication types.
    public var evidenceKind: EvidenceKind {
        EvidenceKind(publicationTypes: publicationTypes)
    }
}

/// Distinguishes what a single study reports from syntheses of a body of evidence.
///
/// Used by Discover so that one study's findings are never presented as scientific consensus.
public enum EvidenceKind: String, Codable, Hashable, Sendable {
    /// Original research: findings reported by one study.
    case singleStudy
    /// Systematic reviews, meta-analyses and guidelines that synthesize many studies.
    case evidenceSynthesis
    /// Narrative reviews: summaries of a field, not systematic.
    case narrativeReview

    public init(publicationTypes: [String]) {
        let types = Set(publicationTypes.map { $0.lowercased() })
        if types.contains("meta-analysis") || types.contains("systematic review")
            || types.contains("practice guideline") || types.contains("guideline") {
            self = .evidenceSynthesis
        } else if types.contains("review") {
            self = .narrativeReview
        } else {
            self = .singleStudy
        }
    }

    public var localizationKey: String { "evidence.\(rawValue)" }
}
