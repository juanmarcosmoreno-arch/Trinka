"""Detects questions whose correct option gives itself away by length.

A well-built question has four options of similar length and detail, so that "pick the
longest" (or "pick the shortest") is no better than chance. A question is flagged when, in
either language, the correct option is clearly longer than every distractor or clearly
shorter than every distractor.

Usage:
  python3 Scripts/seed/length_bias.py            # summary per bank file
  python3 Scripts/seed/length_bias.py FILE.py    # flagged questions in one bank file
"""
import glob
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# The correct option may be at most this much longer than the longest distractor...
MAX_LONGER = 1.10
# ...and at least this fraction of the shortest distractor.
MIN_SHORTER = 0.75


def issues(options, correct):
    """Returns a description of the length cue in one language, or None."""
    lengths = [len(o) for o in options]
    c = lengths[correct]
    others = [n for i, n in enumerate(lengths) if i != correct]
    if c > MAX_LONGER * max(others):
        return f"correct is longest ({c} vs ≤{max(others)} chars)"
    if c < MIN_SHORTER * min(others):
        return f"correct is shortest ({c} vs ≥{min(others)} chars)"
    return None


def question_issues(q):
    """q is a bank tuple: (pmid, level, correct, excerpt, en, es)."""
    _, _, correct, _, en, es = q
    found = []
    for lang, block in (("en", en), ("es", es)):
        problem = issues(block[1], correct)
        if problem:
            found.append(f"{lang}: {problem}")
    return found


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def stats(questions):
    """Share of questions where the correct option is the strictly longest (EN)."""
    longest = sum(1 for q in questions
                  if len(q[4][1][q[2]]) > max(len(o) for i, o in enumerate(q[4][1]) if i != q[2]))
    return longest, len(questions)


def main():
    if len(sys.argv) > 1:
        module = load(sys.argv[1])
        for n, q in enumerate(module.Q):
            found = question_issues(q)
            if found:
                print(f"#{n} pmid {q[0]} correct={q[2]} :: {q[4][0]}")
                for line in found:
                    print(f"     {line}")
                for i, opt in enumerate(q[4][1]):
                    mark = "*" if i == q[2] else " "
                    print(f"   {mark}{i} ({len(opt)}) {opt}")
        return
    total_flagged = total = total_longest = 0
    for path in sorted(glob.glob(os.path.join(HERE, "bank", "*.py"))):
        module = load(path)
        flagged = sum(1 for q in module.Q if question_issues(q))
        longest, n = stats(module.Q)
        total_flagged += flagged; total += n; total_longest += longest
        print(f"{os.path.basename(path):45s} flagged {flagged:3d}/{n:3d}   correct-is-longest {longest / n:4.0%}")
    print(f"TOTAL flagged {total_flagged}/{total}; correct is the longest option in {total_longest / total:.0%} (chance: 25%)")


if __name__ == "__main__":
    main()
