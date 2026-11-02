#!/usr/bin/env python3
"""synth2 changes-file gate -- every rule a hand-written rewrite has to pass.

WHY THIS EXISTS
Pass 49 rewrites live in `audit/changes_*.json` (the compact apply_rewrites
form), not in a built batch. `synth2_stagecheck.py` cannot see them: it reads a
batch. So each chunk was being checked by an ad-hoc script in %TEMP% that got
rewritten every time, and two of those threw away a real error because the
validator was wrong rather than the chunk.

This is that script, once, with the rules as they were finally agreed:

  PARROT    no assistant turn shares a 6-gram with any user turn in its own row
  ECHO      every edited assistant turn shares a content word with the turn
            IMMEDIATELY before it (the house rule from lead msg 204 -- echoing
            any user turn in the row is not the rule, and cost 13 substitutions)
  BAND      edited assistant turns are 10-13 words
  STYLE     lowercase, ASCII, no hyphen, no em dash
  VOCAB     no British term, no British spelling stem, no banned word
  SCENE     warn on British scene vocabulary (pass 50 class) -- warning, not
            an error, because the scene pass is separate work
  DUP       5-grams against the corpus outside the row itself
  XSTAGE    edited lines against EACH OTHER: a staged chunk is invisible to the
            corpus index, so two of my own new lines can collide with each other
            and every other gate stays green

USAGE
    python runs/synth2/scripts/synth2_changefile_check.py audit/changes_pass49_chunk2.json
    python runs/synth2/scripts/synth2_changefile_check.py changes.json --lane angry
Exits 1 on any error.
"""
import argparse
import io
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
LANES = ["casual", "lazy", "angry", "sexy"]
BAND = (10, 13)

STOP = set("""a an the i you he she it we they me him her us them my your his its our their
this that these those is are was were be been being am do does did have has had will would
can could should shall may might must of in on at to for with from by about as into and or
but so if then than too very just not no yes up down out off over under again once here
there when where why how what which who whom whose before after until while during because
through between against above below both each few more most other some such only own same
all any every little much now ever never still even also""".split())


def content(s):
    """The house content() -- verify pattern STOP list, no length floor, then the
    conditioning.py len > 1. Adopted verbatim from the lead's msg 215 so this
    instrument and the house one cannot disagree about what counts as an echo.
    The old rule here was this checker's own shorter STOP plus a 4-char floor,
    which rejected `app` as an echo when the house rule accepts it (L1177)."""
    return {w for w in toks(s) if w not in STOP and len(w) > 1}


# The full house list: the verify pattern's nouns plus this checker's own
# additions. Adopted whole in msg 218 -- a partial list is how `brutal` and
# `nightmare` stayed in the corpus while `rough` was being caught.
BANNED = ["robbery", "theft", "scam", "bait", "nightmare", "stings", "rough",
          "brutal", "timing", "bold", "classic", "dirty", "sneaky", "underhanded",
          "british", "flu jab"]

# Phrases, matched as phrases rather than words.
BANNED_PHRASES = ["at all"]

# The house watchlist: openers the campaign found in every register.
WATCH = ["were you able to", "have you tried", "did you get", "is just", "a real"]

# British vocabulary with a UK-only referent. A hit here is an ERROR: these are
# the pass 47 terms, already swept, so a new one means a rewrite reintroduced it.
BRIT = ["satnav", "roadworks", "waistcoat", "promenade", "stallholder", "motorway",
        "car boot", "school run", "traffic warden", "dual carriageway", "faff", "hob",
        "loo", "gran", "chap", "pounds", "charity shop", "half six", "fiver", "tenner",
        "car park", "high street", "council tax", "payslip", "pence", "chemist",
        "allotment", "bonfire night", "boxing day", "bank holiday", "pancake day",
        "stag do", "hen do", "full english", "hire car", "primary school", "pub quiz",
        "national trust", "hmrc", "britain", "dressing gown", "trolley", "wheelie bin",
        "half term", "school fete", "guy fawkes", "harvest festival", "parish", "mot",
        "maths", "telly", "quid"]

# Ordinary vocabulary used in the UK sense -- the pass 50 class. Nothing exotic,
# which is why the pass 47 list never caught it. Warning tier: relocating the
# scene is separate work, but a NEW one in a rewrite should be seen.
SCENE = ["airing cupboard", "washing up", "optician", "bypass", "snooker", "rounders",
         "wellington", "single yellow", "bin collection", "premium bonds", "joiner",
         "mates rates", "queue", "cashpoint", "chippy", "off licence", "biscuit",
         "gutted", "knackered", "dodgy", "blimey", "hoover", "nappy", "pram",
         "pushchair", "last bus", "the rec", "dales", "clocks going back"]

# "ring" is British only in the phone sense. L1131 is an heirloom ring.
RING = re.compile(r"\bring\s+(them|him|her|me|us|the|about|hmrc)\b|\bgive\b.*\bring\b", re.I)

# British spelling stems. `appal`/`enthral` need a lookahead or they hit `appalled`
# in US text, which is correct.
SPELL = [r"colour", r"favour", r"honour", r"neighbour", r"rumour", r"humour",
         r"behaviour", r"flavour", r"labour", r"odour", r"vapour", r"savour",
         r"organis", r"realis", r"recognis", r"apologis", r"criticis", r"memoris",
         r"specialis", r"prioritis", r"summaris", r"emphasis(?:e|ed|ing)\b",
         r"centre", r"metre", r"litre", r"theatre", r"fibre", r"calibre",
         r"defence", r"licence", r"offence", r"pretence", r"grey", r"programme",
         r"catalogue", r"dialogue", r"whilst", r"amongst", r"learnt", r"spelt",
         r"travelled", r"travelling", r"cancelled", r"modelled", r"signalled",
         r"jewellery", r"pyjamas", r"tyre", r"kerb", r"plough", r"draught",
         r"appal(?=s|led|ling)", r"enthral(?=s|led|ling)", r"mum\b", r"nan\b"]

VOCAB = re.compile(r"\b(" + "|".join(re.escape(b) for b in BRIT) + r")(?:s|es)?\b", re.I)
SCENERE = re.compile(r"\b(" + "|".join(re.escape(b) for b in SCENE) + r")(?:s|es|ed|ing)?\b", re.I)
BANRE = re.compile(r"\b(" + "|".join(re.escape(b) for b in BANNED) + r")\b", re.I)
PHRASERE = re.compile(r"\b(" + "|".join(re.escape(b) for b in BANNED_PHRASES) + r")\b", re.I)
# Sentence-initial is-frame: a reply that opens is/are/was/were is not a reply.
ISFRAME = re.compile(r"^(is|are|was|were)\b", re.I)
SPELLRE = re.compile(r"\b(" + "|".join(SPELL) + r")", re.I)


def toks(s):
    return re.findall(r"[a-z0-9']+", s.lower())


def grams(s, n):
    w = toks(s)
    return set(" ".join(w[i:i + n]) for i in range(len(w) - n + 1))


def load_lane(lane, priors=()):
    """The lane, optionally with other change files already applied.

    Pass 50 exists because pass 49 is not landed yet, and a pass 50 row that
    pass 49 also rewrites has to be authored against what pass 49 will LEAVE,
    not what the raw file holds today. --prior simulates that: apply the named
    change files to the lane in order, then check against the result. Without
    it, every check on a blocked row is a check against text that is about to
    disappear."""
    p = os.path.join(RAW, "small_talk_%s.jsonl" % lane)
    with io.open(p, encoding="utf-8") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
    for path in priors:
        ch = json.load(open(path, encoding="utf-8"))
        for k, change in ch.items():
            i = int(k) - 1
            if i >= len(lines):
                continue
            row = json.loads(lines[i])
            row["turns"] = apply_changes(row["turns"], change)
            lines[i] = json.dumps(row, ensure_ascii=False)
    return lines


def corpus_index():
    """5-grams over EVERY turn of every lane, not assistant-only: the gate has to
    be as wide as the thing it protects against."""
    idx = {}
    for lane in LANES:
        p = os.path.join(RAW, "small_talk_%s.jsonl" % lane)
        if not os.path.exists(p):
            continue
        for i, line in enumerate(io.open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            for t in json.loads(line)["turns"]:
                for g in grams(t["text"], 5):
                    idx.setdefault(g, set()).add((lane, i))
    return idx


def apply_changes(turns, change):
    """Return the row's turns with this changes entry applied. Keys are
    ROLE-RELATIVE indices: a0 is the first assistant turn, u1 the second user turn."""
    new = [dict(t) for t in turns]
    for rk, idx in change.items():
        role = "assistant" if rk == "a" else "user"
        pos = [i for i, t in enumerate(new) if t["role"] == role]
        for i, txt in idx.items():
            new[pos[int(i)]]["text"] = txt
    return new


def check(path, lane, corpus, show=False, priors=()):
    lines = load_lane(lane, priors)
    ch = json.load(open(path, encoding="utf-8"))
    errs, warns = [], []
    edited = []          # (line, role, text) for the cross-staged scan
    q_before = q_after = turns_seen = 0

    for k, change in ch.items():
        ln = int(k)
        row = json.loads(lines[ln - 1])
        try:
            new = apply_changes(row["turns"], change)
        except IndexError:
            errs.append("L%d INDEX OUT OF RANGE -- row has %d turns, file asks for a higher index"
                        % (ln, len(row["turns"])))
            continue

        # 1 residual parrot, against every user turn of the row
        users = [t["text"] for t in new if t["role"] == "user"]
        for t in new:
            if t["role"] != "assistant":
                continue
            shared = set()
            for u in users:
                shared |= grams(t["text"], 6) & grams(u, 6)
            if shared:
                errs.append("L%d RESIDUAL PARROT %r" % (ln, sorted(shared)[0]))

        # 2 echo, only for assistant turns this file actually edits
        edited_a = {int(i) for i in change.get("a", {})}
        for j, t in enumerate(new):
            if t["role"] != "assistant" or j == 0:
                continue
            if new[j - 1]["role"] != "user":
                continue
            if (j // 2) not in edited_a:
                continue
            prev = new[j - 1]["text"]
            pt = content(prev)
            at = content(t["text"])
            if pt and not (pt & at):
                errs.append("L%d a%d NO ECHO FROM PREVIOUS TURN (prev: %s)"
                            % (ln, j // 2, sorted(pt)[:5]))
            if not pt:
                warns.append("L%d a%d previous turn content-free (pass-20 class, legal)"
                             % (ln, j // 2))

        # 2b knock-on echo: an UNEDITED assistant turn whose own user turn this
        # file just rewrote. The house rule applies to it too, and a change file
        # that relocates the user turn without relocating the reply breaks it
        # silently -- the parrot gate stays green because no 6-gram is shared.
        edited_pos = set()
        for rk, idx in change.items():
            role = "assistant" if rk == "a" else "user"
            pos = [i for i, t in enumerate(new) if t["role"] == role]
            for i in idx:
                edited_pos.add(pos[int(i)])
        for j, t in enumerate(new):
            if t["role"] != "assistant" or j == 0 or j in edited_pos:
                continue
            if new[j - 1]["role"] != "user" or (j - 1) not in edited_pos:
                continue
            pt = content(new[j - 1]["text"])
            at = content(t["text"])
            if pt and not (pt & at):
                # Did this reply echo the turn BEFORE the edit? If it did, this
                # file broke a working echo and that is a regression to fix. If
                # it never echoed, the gap predates the edit and is corpus
                # history, not this change file's fault. The two need different
                # responses, so they get different words.
                old_pt = content(row["turns"][j - 1]["text"])
                old_at = content(row["turns"][j]["text"])
                if old_pt & old_at:
                    warns.append("L%d a%d ECHO BROKEN by edited u%d -- it used to echo "
                                 "(%s), now shares nothing with (%s)"
                                 % (ln, j // 2, (j - 1) // 2,
                                    sorted(old_pt & old_at)[:4], sorted(pt)[:4]))
                else:
                    warns.append("L%d a%d ORPHANED by edited u%d, no echo, pre-existing gap "
                                 "(prev: %s)"
                                 % (ln, j // 2, (j - 1) // 2, sorted(pt)[:5]))


        # 3 style / vocab on every edited turn, both roles
        for rk, idx in change.items():
            role = "assistant" if rk == "a" else "user"
            arr = [t["text"] for t in new if t["role"] == role]
            for i, txt in idx.items():
                edited.append((ln, "%s:L%d" % (rk + i, ln), txt))
                tag = "L%d %s%s" % (ln, rk, i)
                if txt != txt.lower():
                    errs.append("%s NOT LOWERCASE" % tag)
                if any(ord(c) > 127 for c in txt):
                    errs.append("%s NON-ASCII" % tag)
                if "-" in txt:
                    errs.append("%s HYPHEN %r" % (tag, re.search(r"\S*-\S*", txt).group(0)))
                if "\u2014" in txt:
                    errs.append("%s EM DASH" % tag)
                m = VOCAB.search(txt)
                if m:
                    errs.append("%s BRIT %r" % (tag, m.group(0)))
                if RING.search(txt):
                    errs.append("%s BRIT RING %r" % (tag, RING.search(txt).group(0)))
                m = BANRE.search(txt)
                if m:
                    errs.append("%s BANNED %r" % (tag, m.group(0)))
                m = SPELLRE.search(txt)
                if m:
                    errs.append("%s UK SPELLING %r" % (tag, m.group(0)))
                m = SCENERE.search(txt)
                if m:
                    warns.append("%s SCENE %r (pass 50 class)" % (tag, m.group(0)))
                for w in WATCH:
                    if w in txt.lower():
                        errs.append("%s WATCHLIST %r" % (tag, w))
                m = PHRASERE.search(txt)
                if m:
                    errs.append("%s BANNED %r" % (tag, m.group(0)))
                if role == "assistant":
                    if ISFRAME.match(txt):
                        errs.append("%s IS FRAME (reply opens with is/are/was/were)" % tag)
                    n = len(toks(txt))
                    if not (BAND[0] <= n <= BAND[1]):
                        errs.append("%s BAND words=%d" % (tag, n))
                    # Every location, not the first one found. The old index
                    # kept a single (lane, line) per 5-gram, so a row that was
                    # the FIRST place a phrase appeared could never collide
                    # with the second -- which is exactly how 1239 read clean.
                    for g in grams(txt, 5):
                        others = [loc for loc in corpus.get(g, ()) if loc != (lane, ln)]
                        if others:
                            errs.append("%s CORPUS 5G %r (at %s:%d)"
                                        % (tag, g, others[0][0], others[0][1]))
                            break
                if show:
                    olds = [t["text"] for t in row["turns"] if t["role"] == role]
                    print("  %s\n    old: %s\n    new: %s"
                          % (tag, olds[int(i)], txt))
                # arr[i] is the applied text; guard against a stale index
                if arr[int(i)] != txt:
                    errs.append("%s INDEX MISMATCH" % tag)

        for t in row["turns"]:
            if t["role"] == "assistant":
                turns_seen += 1
                q_before += t["text"].rstrip().endswith("?")
        for t in new:
            if t["role"] == "assistant":
                q_after += t["text"].rstrip().endswith("?")

    # 4 the edited lines against each other
    for (l1, t1, a), (l2, t2, b) in itertools.combinations(edited, 2):
        s = grams(a, 5) & grams(b, 5)
        if s:
            errs.append("XSTAGE 5G %s / %s %r" % (t1, t2, sorted(s)[0]))
    for (l1, t1, a), (l2, t2, b) in itertools.combinations(edited, 2):
        x, y = grams(a, 3), grams(b, 3)
        j = len(x & y) / len(x | y) if (x or y) else 0.0
        if j >= 0.60:
            errs.append("XSTAGE NEARDUP %s / %s j=%.2f" % (t1, t2, j))

    print("lane=%s rows=%d edited_lines=%d errors=%d warnings=%d"
          % (lane, len(ch), len(edited), len(errs), len(warns)))
    print("questions in these rows: %d -> %d of %d assistant turns"
          % (q_before, q_after, turns_seen))
    for e in errs:
        print("  ERR", e)
    for w in warns:
        print("  warn", w)
    return 1 if errs else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("changes", help="an audit/changes_*.json in apply_rewrites form")
    ap.add_argument("--lane", default="casual", choices=LANES)
    ap.add_argument("--prior", default="",
                    help="comma-separated change files to apply to the lane first, "
                         "for rows another unlanded pass also rewrites")
    ap.add_argument("--show", action="store_true",
                    help="print old -> new for every edit, so a wrong role-relative index is visible")
    a = ap.parse_args()
    priors = [x for x in a.prior.split(",") if x.strip()]
    return check(a.changes, a.lane, corpus_index(), show=a.show, priors=priors)


if __name__ == "__main__":
    sys.exit(main())
