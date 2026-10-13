#!/usr/bin/env python3
"""Finds StatPearls chapters (NCBI Bookshelf, indexed in PubMed) and prints their summaries.

Usage: python3 Scripts/seed/statpearls.py topics.txt
Each line of topics.txt is a title query (e.g. "Gram Staining" or "Staphylococcus aureus").
The best-matching StatPearls chapter for each line is fetched, cached and printed.
"""
import json, re, sys, time
import find_articles as fa

STOP = {"of", "the", "a", "an", "and", "in", "for", "to", "with", "by", "on"}


def find(topic):
    words = [w for w in re.findall(r"[A-Za-z0-9-]+", topic) if w.lower() not in STOP]
    term = " AND ".join(f"{w}[ti]" for w in words) + " AND StatPearls[book]"
    ids = json.loads(fa.get("esearch.fcgi", db="pubmed", retmode="json", retmax=1, term=term))["esearchresult"]["idlist"]
    time.sleep(0.35)
    return ids[0] if ids else None


def main():
    topics = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    pmids, missing = [], []
    for t in topics:
        pmid = find(t)
        (pmids if pmid else missing).append(pmid or t)
    seen = set()
    for a in fa.fetch(pmids):
        if a["pmid"] in seen:
            continue
        seen.add(a["pmid"])
        print(f"### {a['pmid']} | {a['title']}")
        print(a["abstract"])
        print()
    if missing:
        print("NOT FOUND:", "; ".join(missing), file=sys.stderr)




def list_titles(keywords, retmax=40):
    """Prints PMID | title of StatPearls chapters matching each keyword (title/abstract)."""
    for kw in keywords:
        term = (kw if "[" in kw else f"({kw}[ti])") + " AND StatPearls[book]"
        ids = json.loads(fa.get("esearch.fcgi", db="pubmed", retmode="json", retmax=retmax, sort="relevance", term=term))["esearchresult"]["idlist"]
        time.sleep(0.35)
        if not ids:
            print(f"== {kw}: none"); continue
        summ = json.loads(fa.get("esummary.fcgi", db="pubmed", retmode="json", id=",".join(ids)))["result"]
        time.sleep(0.35)
        print(f"== {kw}: " + " | ".join(f"{u}:{summ[u]['title']}" for u in summ.get("uids", [])))


def by_pmids(pmids):
    for a in fa.fetch(pmids):
        print(f"### {a['pmid']} | {a['title']}")
        print(a["abstract"])
        print()


if __name__ == "__main__":
    # --list kw1;kw2  → titles;  --pmids 1,2,3 → summaries;  file → best match per line
    if sys.argv[1] == "--list":
        list_titles([k.strip() for k in sys.argv[2].split(";") if k.strip()], int(sys.argv[3]) if len(sys.argv) > 3 else 40)
    elif sys.argv[1] == "--pmids":
        by_pmids([p.strip() for p in sys.argv[2].replace(" ", ",").split(",") if p.strip()])
    else:
        main()
