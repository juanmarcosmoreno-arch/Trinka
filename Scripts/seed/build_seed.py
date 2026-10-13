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
import re
import glob
import importlib.util
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

from length_bias import issues as length_cue

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "Packages/TrinkaKit/Sources/TrinkaQuiz/Resources/SeedQuestions.json")
VERSION = 3  # first published version; later versions are tracked in Content/manifest.json
CONTENT = os.path.join(ROOT, "Content")
SWIFT_BANK = os.path.join(ROOT, "Packages/TrinkaKit/Sources/TrinkaQuiz/QuestionBank.swift")


def publish(articles, entries):
    """Writes Content/manifest.json + Content/questions-<version>.json for installed apps to download.

    The version is bumped automatically whenever the questions change (compared by fingerprint),
    and SeedQuestionBank.version in Swift is kept equal to it. Returns the version to bundle.
    """
    import hashlib
    fingerprint = hashlib.sha256(json.dumps([articles, entries], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    manifest_path = os.path.join(CONTENT, "manifest.json")
    previous = json.load(open(manifest_path)) if os.path.exists(manifest_path) else None
    if previous is None:
        version = VERSION
    elif previous.get("fingerprint") == fingerprint:
        version = previous["version"]
    else:
        version = previous["version"] + 1
    os.makedirs(CONTENT, exist_ok=True)
    name = f"questions-{version}.json"
    for old in os.listdir(CONTENT):
        if old.startswith("questions-") and old != name:
            os.remove(os.path.join(CONTENT, old))
    json.dump(dict(version=version, generatedAt="2026-10-13T00:00:00Z", articles=articles, questions=entries),
              open(os.path.join(CONTENT, name), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    json.dump(dict(version=version, file=name, fingerprint=fingerprint,
                   questionsPerLanguage=sum(1 for e in entries if e["language"] == "en")),
              open(manifest_path, "w", encoding="utf-8"), indent=1)
    swift = open(SWIFT_BANK, encoding="utf-8").read()
    swift = re.sub(r"public static let version = \d+", f"public static let version = {version}", swift)
    open(SWIFT_BANK, "w", encoding="utf-8").write(swift)
    if previous and version != previous["version"]:
        print(f"Questions changed: published bank version {version}.")
    return version
sys.path.insert(0, HERE)
from questions_core import Q as CORE  # noqa: E402
from questions_levels import NEW, RELEVEL  # noqa: E402

LEVELS = ["beginner", "curious", "explorer", "researcher", "expert"]
CACHE = os.path.join(HERE, ".cache", "articles.json")
ABBR = {"microbiology": "micro", "immunology": "immuno", "genetics": "genetics", "neuroscience": "neuro",
        "humanPhysiology": "physio", "medicine": "medicine", "biotechnology": "biotech", "nutrition": "nutrition",
        "veterinaryScience": "vet", "generalScience": "general", "infectiousDiseases": "infect",
        "diagnosticMethods": "dx", "foodAnalysis": "food", "historyOfScience": "history",
        "bovineMastitis": "mastitis"}


def load_bank():
    """Questions in bank/<category>.py, compact tuples:
    (pmid, level, correctIndex, excerpt, (en prompt, [4 options], explanation, short), (es …))."""
    out = []
    per_pmid = collections.Counter()
    for path in sorted(glob.glob(os.path.join(HERE, "bank", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        for pmid, level, correct, excerpt, en, es in module.Q:
            per_pmid[(module.CATEGORY, pmid)] += 1
            out.append(dict(id=f"{ABBR[module.CATEGORY]}-{pmid}-{per_pmid[(module.CATEGORY, pmid)]}", pmid=pmid, category=module.CATEGORY,
                            difficulty=level, correct=correct, excerpt=excerpt, method="aiAuthored",
                            en=dict(prompt=en[0], options=list(en[1]), explanation=en[2], short=en[3]),
                            es=dict(prompt=es[0], options=list(es[1]), explanation=es[2], short=es[3])))
    return out


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
    questions = CORE + NEW + load_bank()
    known = {}
    if os.path.exists(CACHE):
        known.update(json.load(open(CACHE, encoding="utf-8")))
    if os.path.exists(OUT):
        known.update({a["pmid"]: a for a in json.load(open(OUT, encoding="utf-8"))["articles"]})
    missing = sorted({q["pmid"] for q in questions} - set(known))
    if missing:
        print("Fetching from PubMed:", ", ".join(missing))
        known.update(fetch(missing))

    errors, articles, entries, used = [], [], [], set()
    ids = collections.Counter(q["id"] for q in questions)
    errors += [f"duplicate id {i}" for i, n in ids.items() if n > 1]
    prompts = collections.Counter(norm(q["en"]["prompt"]) for q in questions)
    errors += [f"duplicate prompt: {p[:70]}" for p, n in prompts.items() if n > 1]
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
            if not 0 <= q["correct"] < 4:
                errors.append(f"{q['id']}: correct index out of range")
            elif len(t["options"]) == 4 and (cue := length_cue(t["options"], q["correct"])):
                # "Pick the longest option" must not beat chance (see length_bias.py).
                errors.append(f"{q['id']}-{lang}: {cue}")
            entries.append(dict(id=f"{q['id']}-{lang}", translationKey=q["id"], language=lang, category=q["category"],
                                difficulty=level, prompt=t["prompt"], options=t["options"], correctOptionIndex=q["correct"],
                                explanation=t["explanation"], shortExplanation=t["short"], pmid=q["pmid"],
                                verification=dict(status="verified", method=q.get("method", "aiAuthored"),
                                                  supportingExcerpt=q["excerpt"], reviewedAt="2026-10-13T00:00:00Z")))
    if errors:
        sys.exit("Seed build failed:\n  " + "\n  ".join(errors))

    version = publish(articles, entries)
    json.dump(dict(version=version, generatedAt="2026-10-13T00:00:00Z", articles=articles, questions=entries),
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    english = [e for e in entries if e["language"] == "en"]
    levels = collections.Counter(e["difficulty"] for e in english)
    cats = collections.Counter(e["category"] for e in english)
    answers = collections.Counter(e["correctOptionIndex"] for e in english)
    print(f"Wrote {len(entries)} questions ({len(english)} per language) from {len(articles)} articles.")
    print("Per level:", ", ".join(f"{lvl} {levels[lvl]}" for lvl in LEVELS))
    print("Per discipline:", ", ".join(f"{c} {n}" for c, n in sorted(cats.items())))
    print("Correct option A/B/C/D:", "/".join(str(answers[i]) for i in range(4)))
    longest = sum(1 for e in english
                  if len(e["options"][e["correctOptionIndex"]]) == max(len(o) for o in e["options"]))
    print(f"Correct option is the longest in {longest / len(english):.0%} of questions (chance: 25%).")


if __name__ == "__main__":
    main()
