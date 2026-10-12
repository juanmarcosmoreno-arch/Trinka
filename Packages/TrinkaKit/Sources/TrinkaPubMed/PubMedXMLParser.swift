import Foundation
#if canImport(FoundationXML)
import FoundationXML
#endif
import TrinkaCore

/// Parses `efetch` PubMed XML (`<PubmedArticleSet>`) into `ArticleReference`s.
///
/// Matching is done on full element paths so that nested lists — such as the PMIDs and DOIs
/// of an article's reference list — are not mistaken for the article's own identifiers.
public final class PubMedXMLParser: NSObject, XMLParserDelegate {
    public static func parse(_ data: Data) throws -> [ArticleReference] {
        let delegate = PubMedXMLParser()
        let parser = XMLParser(data: data)
        parser.delegate = delegate
        guard parser.parse() else {
            throw PubMedError.parsing(parser.parserError.map { "\($0)" } ?? "efetch XML")
        }
        return delegate.articles
    }

    private enum Path {
        static let article = "PubmedArticleSet/PubmedArticle"
        static let pmid = article + "/MedlineCitation/PMID"
        static let title = article + "/MedlineCitation/Article/ArticleTitle"
        static let abstractText = article + "/MedlineCitation/Article/Abstract/AbstractText"
        static let journal = article + "/MedlineCitation/Article/Journal/Title"
        static let pubDate = article + "/MedlineCitation/Article/Journal/JournalIssue/PubDate"
        static let author = article + "/MedlineCitation/Article/AuthorList/Author"
        static let publicationType = article + "/MedlineCitation/Article/PublicationTypeList/PublicationType"
        static let articleID = article + "/PubmedData/ArticleIdList/ArticleId"
    }

    private var articles: [ArticleReference] = []
    private var stack: [String] = []
    private var path: String { stack.joined(separator: "/") }

    // Current article
    private var pmid = ""
    private var title = ""
    private var abstractSections: [String] = []
    private var journal = ""
    private var year: Int?
    private var authors: [String] = []
    private var doi: String?
    private var publicationTypes: [String] = []

    // Current author
    private var lastName = ""
    private var initials = ""
    private var collectiveName = ""

    // Text capture: the path being captured and its label (for structured abstracts).
    private var capturePath: String?
    private var captureLabel: String?
    private var captureIDType: String?
    private var buffer = ""

    public func parser(_ parser: XMLParser, didStartElement elementName: String, namespaceURI: String?,
                       qualifiedName qName: String?, attributes attributeDict: [String: String] = [:]) {
        stack.append(elementName)
        let current = path

        if current == Path.article {
            resetArticle()
        } else if current == Path.author {
            lastName = ""; initials = ""; collectiveName = ""
        }

        guard capturePath == nil else { return } // Nested markup (<i>, <sup>…) inside a captured element.

        switch current {
        case Path.pmid, Path.title, Path.journal, Path.publicationType,
             Path.pubDate + "/Year", Path.pubDate + "/MedlineDate",
             Path.author + "/LastName", Path.author + "/Initials", Path.author + "/CollectiveName":
            beginCapture(current)
        case Path.abstractText:
            beginCapture(current)
            captureLabel = attributeDict["Label"]
        case Path.articleID:
            beginCapture(current)
            captureIDType = attributeDict["IdType"]
        default:
            break
        }
    }

    public func parser(_ parser: XMLParser, foundCharacters string: String) {
        if capturePath != nil { buffer += string }
    }

    public func parser(_ parser: XMLParser, didEndElement elementName: String, namespaceURI: String?, qualifiedName qName: String?) {
        let current = path
        defer { stack.removeLast() }

        if current == capturePath {
            let text = buffer.trimmingCharacters(in: .whitespacesAndNewlines)
            store(text, at: current)
            capturePath = nil
            captureLabel = nil
            captureIDType = nil
            buffer = ""
        }

        if current == Path.author {
            if !collectiveName.isEmpty {
                authors.append(collectiveName)
            } else if !lastName.isEmpty {
                authors.append(initials.isEmpty ? lastName : "\(lastName) \(initials)")
            }
        } else if current == Path.article {
            finishArticle()
        }
    }

    private func beginCapture(_ path: String) {
        capturePath = path
        buffer = ""
    }

    private func store(_ text: String, at path: String) {
        switch path {
        case Path.pmid: pmid = text
        case Path.title: title = text
        case Path.journal: journal = text
        case Path.publicationType: if !text.isEmpty { publicationTypes.append(text) }
        case Path.pubDate + "/Year": year = Int(text)
        case Path.pubDate + "/MedlineDate":
            // e.g. "1998 Nov-Dec"
            if year == nil { year = Int(text.prefix(4)) }
        case Path.author + "/LastName": lastName = text
        case Path.author + "/Initials": initials = text
        case Path.author + "/CollectiveName": collectiveName = text
        case Path.abstractText:
            guard !text.isEmpty else { return }
            if let label = captureLabel, !label.isEmpty, label.uppercased() != "UNLABELLED" {
                abstractSections.append("\(label): \(text)")
            } else {
                abstractSections.append(text)
            }
        case Path.articleID:
            if captureIDType == "doi", doi == nil, !text.isEmpty { doi = text }
        default:
            break
        }
    }

    private func resetArticle() {
        pmid = ""; title = ""; abstractSections = []; journal = ""; year = nil
        authors = []; doi = nil; publicationTypes = []
    }

    private func finishArticle() {
        guard QuestionValidator.isValidPMID(pmid), !title.isEmpty else { return }
        articles.append(ArticleReference(
            pmid: pmid,
            title: title,
            authors: authors,
            journal: journal,
            year: year ?? 0,
            doi: doi,
            abstract: abstractSections.isEmpty ? nil : abstractSections.joined(separator: "\n"),
            publicationTypes: publicationTypes
        ))
    }
}
