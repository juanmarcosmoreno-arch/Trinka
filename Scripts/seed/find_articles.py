#!/usr/bin/env python3
"""Finds candidate PubMed articles (with abstracts) for writing seed questions.

Usage: python3 Scripts/seed/find_articles.py "<entrez query>" [max] [--exclude pmid,pmid]
Prints PMID, year, journal, publication types, title and full abstract for reading.
Fetched records are cached in Scripts/seed/.cache/articles.json (git-ignored) for build_seed.py.
"""
import json, os, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, ".cache", "articles.json")
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def get(endpoint, **params):
    params.update(tool="trinka")
    url = EUTILS + endpoint + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            return urllib.request.urlopen(url, timeout=60).read()
        except Exception:
            time.sleep(2 ** attempt)
    raise RuntimeError("PubMed request failed: " + url)


def parse_books(root):
    """StatPearls and other NCBI Bookshelf chapters indexed in PubMed (PubmedBookArticle)."""
    out = {}
    for b in root.findall("PubmedBookArticle"):
        d = b.find("BookDocument")
        sections = []
        for t in d.findall("Abstract/AbstractText"):
            text = "".join(t.itertext()).strip(); label = t.get("Label")
            if text:
                sections.append((label + ": " if label and label.upper() != "UNLABELLED" else "") + text)
        authors = [f"{au.findtext('LastName')} {au.findtext('Initials') or ''}".strip()
                   for au in d.findall("AuthorList/Author") if au.findtext("LastName")]
        pmid = d.findtext("PMID")
        book = d.findtext("Book/BookTitle") or "NCBI Bookshelf"
        year = d.findtext("Book/PubDate/Year") or "0"
        out[pmid] = dict(pmid=pmid, title="".join(d.find("ArticleTitle").itertext()).strip(), authors=authors,
                         journal=f"{book} [Internet]", year=int(year) if year.isdigit() else 0, doi=None,
                         abstract="\n".join(sections),
                         publicationTypes=[p.text for p in d.findall("PublicationType")] or ["Review"],
                         bookshelfID=next((i.text for i in d.findall("ArticleIdList/ArticleId") if i.get("IdType") == "bookaccession"), None))
    return out


def parse(xml_bytes):
    out = {}
    root = ET.fromstring(xml_bytes)
    out.update(parse_books(root))
    for a in root.findall("PubmedArticle"):
        m = a.find("MedlineCitation"); art = m.find("Article")
        sections = []
        for t in art.findall("Abstract/AbstractText"):
            text = "".join(t.itertext()).strip(); label = t.get("Label")
            if text:
                sections.append((label + ": " if label and label.upper() != "UNLABELLED" else "") + text)
        authors = []
        for au in art.findall("AuthorList/Author"):
            authors.append(au.findtext("CollectiveName") or f"{au.findtext('LastName')} {au.findtext('Initials') or ''}".strip())
        year = art.findtext("Journal/JournalIssue/PubDate/Year") or (art.findtext("Journal/JournalIssue/PubDate/MedlineDate") or "0")[:4]
        doi = next((i.text for i in a.findall("PubmedData/ArticleIdList/ArticleId") if i.get("IdType") == "doi"), None)
        pmid = m.findtext("PMID")
        out[pmid] = dict(pmid=pmid, title="".join(art.find("ArticleTitle").itertext()).strip(), authors=authors,
                         journal=art.findtext("Journal/Title"), year=int(year) if year.isdigit() else 0, doi=doi,
                         abstract="\n".join(sections),
                         publicationTypes=[p.text for p in art.findall("PublicationTypeList/PublicationType")])
    return out


def load_cache():
    return json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)


def fetch(pmids):
    cache = load_cache()
    missing = [p for p in pmids if p not in cache]
    for i in range(0, len(missing), 100):
        cache.update(parse(get("efetch.fcgi", db="pubmed", retmode="xml", id=",".join(missing[i:i + 100]))))
        time.sleep(0.4)
    save_cache(cache)
    return [cache[p] for p in pmids if p in cache]


def main():
    query = sys.argv[1]
    retmax = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 20
    exclude = set()
    if "--exclude" in sys.argv:
        exclude = set(sys.argv[sys.argv.index("--exclude") + 1].split(","))
    ids = json.loads(get("esearch.fcgi", db="pubmed", retmode="json", retmax=retmax, sort="relevance",
                         term=f"({query}) AND hasabstract NOT \"Retracted Publication\"[pt]"))["esearchresult"]["idlist"]
    ids = [i for i in ids if i not in exclude]
    for a in fetch(ids):
        if len(a["abstract"]) < 400:
            continue
        print(f"### {a['pmid']} | {a['year']} | {a['journal']} | {', '.join(a['publicationTypes'][:3])}")
        print(a["title"])
        print(a["abstract"])
        print()


if __name__ == "__main__":
    main()
