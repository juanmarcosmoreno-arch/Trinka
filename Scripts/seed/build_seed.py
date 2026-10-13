#!/usr/bin/env python3
"""Builds Packages/TrinkaKit/Sources/TrinkaQuiz/Resources/SeedQuestions.json.

Questions live in questions_core.py and questions_levels.py. Article metadata (title, authors,
journal, year, DOI, abstract, publication types) comes from PubMed: it is reused from the current
SeedQuestions.json, and any PMID not found there is fetched with NCBI E-utilities (efetch).

The build fails if any supporting excerpt is not found verbatim (whitespace/case-insensitive) in
its article's title + abstract, if options are not 4 distinct values, or if a translation is missing.

Usage: python3 Scripts/seed/build_seed.py
After changing which questions exist, bump `SeedQuestionBank.version` (friend-challenge codes).
"""
import collections
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "Packages/TrinkaKit/Sources/TrinkaQuiz/Resources/SeedQuestions.json")
VERSION = 2
sys.path.insert(0, HERE)
from questions_core import Q as CORE  # noqa: E402
from questions_levels import NEW, RELEVEL  # noqa: E402

LEVELS = ["beginner", "curious", "explorer", "researcher", "expert"]


def norm(text):
    return " ".join(text.split()).lower()


def fetch(pmids):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&tool=trinka&id=" + ",".join(pmids)
    root = ET.fromstring(urllib.request.urlopen(url, timeout=60).read())
    out = {}
    for a in root.findall("PubmedArticle"):
        m = a.find("MedlineCitation"); art = m.find("Article")
        sections = []
        for t in art.findall("Abstract/AbstractText"):
            text = "".join(t.itertext()).strip(); label = t.get("Label")
            sections.append((label + ": " if label else "") + text)
        authors = []
        for au in art.findall("AuthorList/Author"):
            authors.append(au.findtext("CollectiveName") or f"{au.findtext('LastName')} {au.findtext('Initials') or ''}".strip())
        year = art.findtext("Journal/JournalIssue/PubDate/Year") or (art.findtext("Journal/JournalIssue/PubDate/MedlineDate") or "0")[:4]
        doi = next((i.text for i in a.findall("PubmedData/ArticleIdList/ArticleId") if i.get("IdType") == "doi"), None)
        pmid = m.findtext("PMID")
        out[pmid] = dict(pmid=pmid, title="".join(art.find("ArticleTitle").itertext()).strip(), authors=authors,
                         journal=art.findtext("Journal/Title"), year=int(year), doi=doi, abstract="\n".join(sections),
                         publicationTypes=[p.text for p in art.findall("PublicationTypeList/PublicationType")])
    return out


def main():
    questions = CORE + NEW
    known = {}
    if os.path.exists(OUT):
        known = {a["pmid"]: a for a in json.load(open(OUT, encoding="utf-8"))["articles"]}
    missing = sorted({q["pmid"] for q in questions} - set(known))
    if missing:
        print("Fetching from PubMed:", ", ".join(missing))
        known.update(fetch(missing))

    errors, articles, entries, used = [], [], [], set()
    for q in questions:
        level = RELEVEL.get(q["id"], q["difficulty"])
        if level not in LEVELS:
            errors.append(f"{q['id']}: unknown level {level}")
        article = known.get(q["pmid"])
        if not article:
            errors.append(f"{q['id']}: PMID {q['pmid']} not found"); continue
        if norm(q["excerpt"]) not in norm(article["title"] + "\n" + (article["abstract"] or "")):
            errors.append(f"{q['id']}: excerpt not found in PMID {q['pmid']}")
        if q["pmid"] not in used:
            used.add(q["pmid"]); articles.append(article)
        for lang in ("en", "es"):
            t = q.get(lang)
            if not t:
                errors.append(f"{q['id']}: missing {lang}"); continue
            if len(t["options"]) != 4 or len({norm(o) for o in t["options"]}) != 4:
                errors.append(f"{q['id']}-{lang}: options must be 4 distinct values")
            entries.append(dict(id=f"{q['id']}-{lang}", translationKey=q["id"], language=lang, category=q["category"],
                                difficulty=level, prompt=t["prompt"], options=t["options"], correctOptionIndex=q["correct"],
                                explanation=t["explanation"], shortExplanation=t["short"], pmid=q["pmid"],
                                verification=dict(status="verified", method="editorialReview",
                                                  supportingExcerpt=q["excerpt"], reviewedAt="2026-10-13T00:00:00Z")))
    if errors:
        sys.exit("Seed build failed:\n  " + "\n  ".join(errors))

    json.dump(dict(version=VERSION, generatedAt="2026-10-13T00:00:00Z", articles=articles, questions=entries),
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    levels = collections.Counter(e["difficulty"] for e in entries if e["language"] == "en")
    print(f"Wrote {len(entries)} questions ({len(entries) // 2} per language) from {len(articles)} articles.")
    print("Per level:", ", ".join(f"{lvl} {levels[lvl]}" for lvl in LEVELS))


if __name__ == "__main__":
    main()
