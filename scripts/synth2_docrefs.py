#!/usr/bin/env python3
"""synth2_docrefs.py -- the doc/code link checker.

Why this exists: on 2026-10-18 the instruments were moved out of the skill's
assets/ into runs/synth2/scripts/ so every agent could use them. A path rewrite
across a 477KB SKILL.md looks clean and is not: it left one tool named in prose
that no longer existed anywhere (`synth2_g16_audit.py`) and one tool that shipped
with no mention at all (`synth2_regmeasure.py`). Neither would ever have been
noticed by a gate, and both would have sent the next agent hunting.

What it checks, in order of how much it saves you:
  1. DEAD MENTION   a synth2_*.py named in a doc that exists nowhere on disk
  2. ORPHAN         a tool in the scripts folder that no doc mentions
  3. STALE PATH     a `$SK/x.py` that does not resolve, or any `assets/x.py`
  4. SUMMARY        per-tool reference counts (path form vs bare prose)

Exit 1 on 1-3, so it works as a pre-commit / pre-handoff gate.

Usage:
    python synth2_docrefs.py                      # default: skill SKILL.md + repo docs
    python synth2_docrefs.py --docs a.md b.md     # explicit
    python synth2_docrefs.py --quiet              # only problems + exit code
"""
import argparse
import glob
import io
import os
import re
import sys

SCRIPTS = r"C:\github\DBllm\runs\synth2\scripts"
SKILL = r"C:\Users\ericl\.workbuddy-ai\skills\synth2-row-batch\SKILL.md"
REPO_DOCS = [r"C:\github\DBllm\runs\synth2\*.md",
             r"C:\github\DBllm\runs\synth2\research\*.md"]


def default_docs():
    docs = [SKILL] if os.path.exists(SKILL) else []
    for pat in REPO_DOCS:
        docs.extend(sorted(glob.glob(pat)))
    return [d for d in docs if os.path.exists(d)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", nargs="+", default=None)
    ap.add_argument("--scripts", default=SCRIPTS)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    docs = a.docs or default_docs()
    tools = sorted(os.path.basename(p) for p in glob.glob(os.path.join(a.scripts, "synth2_*.py")))
    if not tools:
        print("no synth2_*.py found in %s" % a.scripts)
        return 1

    # every .py that exists anywhere we might legitimately mean
    on_disk = set()
    for root in (a.scripts, os.path.dirname(SKILL)):
        for p in glob.glob(os.path.join(root, "**", "*.py"), recursive=True):
            on_disk.add(os.path.basename(p))

    texts = {}
    for d in docs:
        texts[d] = io.open(d, encoding="utf-8", errors="replace").read()

    dead, stale = [], []
    for d, s in texts.items():
        for m in sorted(set(re.findall(r"\b(synth2_[a-z0-9_]+\.py)\b", s))):
            if m not in on_disk:
                dead.append((m, os.path.basename(d)))
        for m in sorted(set(re.findall(r"\$SK/([A-Za-z0-9_]+\.py)", s))):
            if not os.path.exists(os.path.join(a.scripts, m)):
                stale.append(("$SK/" + m, os.path.basename(d)))
        for m in sorted(set(re.findall(r"assets/([A-Za-z0-9_]+\.py)", s))):
            stale.append(("assets/" + m, os.path.basename(d)))

    sk = texts.get(SKILL, "")
    orphans = [t for t in tools if sk and t not in sk]

    if not a.quiet:
        print("docs: %d   tools: %d" % (len(docs), len(tools)))
    print("\n1. dead mentions (named, exists nowhere): %d" % len(dead))
    for m, d in dead:
        print("     %-28s <- %s" % (m, d))
    print("2. orphans (shipped, never mentioned): %d" % len(orphans))
    for t in orphans:
        print("     %s" % t)
    print("3. stale paths: %d" % len(stale))
    for m, d in stale:
        print("     %-28s <- %s" % (m, d))

    if not a.quiet:
        print("\n4. reference form per tool (path = `$SK/name`, bare = prose):")
        for t in tools:
            p = sk.count("$SK/" + t)
            b = len(re.findall(r"(?<!\$SK/)\b%s\b" % re.escape(t), sk)) - p
            print("     %-28s path=%-3d bare=%-3d %s" % (t, p, max(b, 0), "OK" if (p or b) else "UNREFERENCED"))

    bad = len(dead) + len(orphans) + len(stale)
    print("\nDOCREFS:", "CLEAN" if not bad else "REVIEW -- %d problem(s)" % bad)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
