#!/usr/bin/env python3
"""edit_plan.py -- design an IN-PLACE edit plan for the synth2 corpus.

WHY THIS EXISTS.  The campaign has been growing rows (fan-out) and the model
regressed: heldout went 3.9447 -> 3.9663 and the behaviour probe went
responsive 2/50 -> 2/50, in-register 30/50 -> 8/50, clean 17/50 -> 10/50, with
novel gibberish tokens proliferating.  The root readme says volume does not buy
understanding ("more-of-the-same rows buy almost nothing") and that retirement
is a first-class operation.  This script is the instrument that turns that law
into a concrete edit list: it READS `raw/` and REPORTS which rows to DELETE and
which to REWRITE, so the corpus gets SMALLER and SHARPER instead of bigger.

It is NOT a door into `raw/`.  `add_rows.py` remains the only way rows are
APPENDED.  This script only ever removes rows, and only under `--apply-deletes`
with `--confirm`, using the owner's OPS protocol (lock + backup + unique-text
replace), and it prints the re-validation gates it did NOT run so you run them.

THE LENSES (each is a corpus cause of the regression):

  G  GENERATOR   machine output that survived the purge, caught by TWO lenses:
                 (a) integrity.py's pair -- mean assistant words < 6.2 AND
                 no-function-word share > 40% (sarcastic b3725/b3800, 168 rows);
                 (b) the TELEGRAPHIC lens -- pervasive comma-separated 2-4 word
                 participle fragments with no finite clause (confused
                 b7820..b7970, 240 rows). Lens (a) MISSES (b) entirely: one
                 pronoun ("you") makes the no-function-word share read 0.0%.
                 Both are pure attractor -> DELETE.
  F  FRAME       the content-free shells the probe named as "the collapse
                 shape": "X is a monument / museum", "photo of the counter",
                 "the whole thing", "i have been going to", "i am not going to
                 say it", "you are the only one".  A SHORT assistant turn that
                 is nothing but a frame is anti-training data -> DELETE; a frame
                 sitting on top of real content -> REWRITE (cut the tail).
  L  LOOP        an assistant turn that repeats a 3-gram internally.  The probe
                 named looping as anti-training (probe #14, #21, #42, #48).
  S  SPLICE      THE UNDERSTANDING LENS.  turn_delta's swap arm, applied per
                 row: for each assistant turn, compare its content-token
                 Jaccard against the user turn it actually answers with its
                 Jaccard against K random user turns from the corpus.  If the
                 reply is no closer to its own turn than to a random one, the
                 row teaches the model to IGNORE the turn.  `margin <= 0` is a
                 turn-independent row -> REWRITE.
  A  ANCHOR      a multi-turn row where the numbers/days in the assistant turns
                 do not line up with the numbers/days in the user turns (the
                 "Friday -> Saturday" / "forty minutes -> forty minutes of not
                 going to do" failure) -> REWRITE.

USAGE
  python runs/synth2/scripts/edit_plan.py                    # human report
  python runs/synth2/scripts/edit_plan.py --md  out.md       # write markdown
  python runs/synth2/scripts/edit_plan.py --json out.json    # machine plan
  python runs/synth2/scripts/edit_plan.py -f sarcastic       # one file
  python runs/synth2/scripts/edit_plan.py --queue 500        # ranked rewrite queue

  # the only write path -- deletes GENERATOR + FRAME-SHELL + LOOP-SHELL rows:
  python runs/synth2/scripts/edit_plan.py --apply-deletes --confirm
"""
import argparse
import collections
import json
import math
import os
import random
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
LOCK_PATH = os.path.join(HERE, ".add_rows.lock")
SEED = 20261004

# ---------------------------------------------------------------- lens 1
# Identical to integrity.py so the two instruments agree row for row.
FUNC = set(
    "a an the i you he she it we they and or but if so of to in on for with is "
    "was were be been am are do did does not no yes my your his her that this "
    "there what when who how why".split()
)
WORD_CEIL = 6.2
NOFUNC_FLOOR = 40.0

# ---------------------------------------------------------------- lens 2
# The content-free frames.  Only a SHORT turn that is nothing but a frame is a
# DELETE; a frame on top of real content is a REWRITE (cut the tail).
FRAMES = [
    ("monument", r"\bis a monument\b"),
    ("museum", r"\bis a museum\b"),
    ("photo_counter", r"\bphoto of the counter\b"),
    ("photo_crew", r"\bphoto of the crew\b"),
    ("is_a_crew", r"\bis a crew\b"),
    ("crew_is_a_crew", r"\bcrew is a crew\b"),
    ("whole_thing", r"\bthe whole (thing|point|time|street)\b"),
    ("been_going_to", r"\bi have been going to\b"),
    ("not_gonna_say", r"\bnot going to say it\b"),
    ("only_one", r"\byou are the only one\b"),
    ("only_thing", r"\bis the only (thing|one)\b"),
    ("been_told", r"\bi have been told\b"),
    ("that_is_the_whole", r"\bthat is the whole\b"),
    ("in_the_same_way", r"\bin the same way\b"),
    ("same_thing", r"\bthe same (thing|way|place)\b"),
    ("since_the_whole_time", r"\bsince the whole time\b"),
]
FRAME_RE = [(n, re.compile(p)) for n, p in FRAMES]

# ---------------------------------------------------------------- content
PLACEHOLDERS = set(
    "thing stuff week place work night mess friend guy business situation one "
    "way time day whole only same lot bit kind sort while".split()
)
STOP = set(
    """a an the i you he she it we they me my your his her our their us them
    and or but if so then than of to in on at for with from by as into over
    under about is are was were be been being am do does did have has had will
    would shall should can could may might must not no yes yeah yep nope nah
    huh oh ok okay well just very too this that these those there here what
    when where why who whom how which up out down off again back now still even
    also own such get got go going gone went come came like know think say said
    tell told see saw look want need make made take took give gave put let
    anything everything something nothing anyone everyone someone nobody
    maybe really quite much many more most some any all""".split()
)
NUMWORD = set(
    "one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty "
    "fifty sixty seventy eighty ninety hundred thousand".split()
)
DAYS = set(
    "monday tuesday wednesday thursday friday saturday sunday weekday weekend "
    "today tomorrow morning evening afternoon night".split()
)
SHELL_WORDS = 6       # a frame in a turn this short or shorter is a shell
SHELL_CONTENT = 1     # ... and this few content tokens left after the frame
MARGIN = 2.0          # IDF-weighted splice margin above which a reply is
                      # "turn-specific" (a shared rare noun scores ~5-8; a
                      # shared common word scores ~1, same as a random turn)


def words(text):
    return re.findall(r"[a-z']+", str(text).lower())


def content_tokens(text):
    out = []
    for t in re.findall(r"[a-z0-9']+", str(text).lower()):
        if t in STOP or t in PLACEHOLDERS:
            continue
        if len(t) < 3 and not t.isdigit():
            continue
        out.append(t)
    return out


def anchors(text):
    s = str(text).lower()
    a = set(re.findall(r"\b\d+\b", s))
    a |= {w for w in re.findall(r"[a-z]+", s) if w in NUMWORD or w in DAYS}
    return a


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def loop_gram(text, n=3):
    w = words(text)
    seen = set()
    for i in range(len(w) - n + 1):
        g = tuple(w[i:i + n])
        if g in seen:
            return " ".join(g)
        seen.add(g)
    return None


def read_rows(path):
    with open(path, "rb") as fh:
        blob = fh.read()
    rows = []
    for line in blob.split(b"\n"):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line.decode("utf-8")))
        except Exception:
            pass
    return rows


def batch_stats(rows):
    asst_words, nofunc, total = [], 0, 0
    for row in rows:
        for turn in row.get("turns", []):
            if turn.get("role") != "assistant":
                continue
            toks = words(turn.get("text", ""))
            if not toks:
                continue
            total += 1
            asst_words.append(len(toks))
            if not (set(toks) & FUNC):
                nofunc += 1
    n = max(1, len(asst_words))
    return {"n": len(rows), "words": sum(asst_words) / n,
            "nofunc": 100.0 * nofunc / n}


def is_generator(st):
    return st["words"] < WORD_CEIL and st["nofunc"] > NOFUNC_FLOOR


# ---------------------------------------------------------------- lens 1b
# The SECOND generator family, which integrity.py's lens misses entirely.
# It writes "telegraphic fragment chains": comma-separated 2-4 word fragments
# ending in a participle, with no finite clause. One pronoun ("you") is enough
# to defeat the no-function-word lens, so it read 0.0% nofunc and passed.
#   "name unnecessary, recognition issued at the gate, you both holding a
#    formal moment, salute credited, round documented, greeting kept, route
#    continued, home reached, effort logged."
# Found 2026-10-04: 240 rows in small_talk_confused.jsonl (b7820..b7970), a
# splice campaign whose assistant turns were machine-written.
IRREG = set(
    "kept held made done sent told left met put run set cut got gone seen known "
    "shown given taken written spoken broken chosen driven eaten fallen "
    "forgotten hidden ridden risen shaken stolen woken worn built found paid "
    "said".split()
)


def frag_count(text):
    """Comma-separated 2-4 word fragments ending in a participle."""
    n = 0
    for seg in str(text).split(","):
        w = words(seg)
        if not w or len(w) > 4:
            continue
        last = w[-1]
        if last.endswith("ed") or last.endswith("ing") or last in IRREG:
            n += 1
    return n


def is_telegraphic(row):
    """True when the row's assistant side is a pervasive fragment chain.

    A single fragment is rhetoric ("stamped, addressed, DONE"); six or more
    across the row's assistant turns is the generator. Calibrated so the
    hand-written celebratory/nostalgic rows that use one such turn fall out.
    """
    tot = 0
    for t in row.get("turns", []):
        if t.get("role") == "assistant":
            tot += frag_count(t.get("text", ""))
    return tot >= 6


# ---------------------------------------------------------------- lens 1c
# The THIRD generator family: CHAINED-NOUN suffixing -- BOTH SIDES chain.
#   "the saturday lie in ended at six by internal alarm || the internal alarm
#    keeps weekday hours || the hours owe me a weekend || the weekend never
#    repays"
# Note the user turns chain too ("the hours owe me a weekend" continues the
# assistant's "hours").  A human chat turn does not do that, so a USER-side
# chain is the discriminator between the generator and ordinary dialogue where
# the assistant merely picks up the noun the user just used.
#
# BUG FOUND 2026-10-04 (this is why Phase 2 was rolled back).  The original
# rule counted an assistant turn as chained whenever it echoed the noun of the
# IMMEDIATELY PRECEDING turn -- which is almost always a USER turn.  So it
# fired on responsive dialogue ("the farm lad?" -> "the lad from the farm, and
# he was quick") and deleted 3,278 rows, of which only 645 were true double
# chains.  A later test disproved the causal claim outright: the deleted rows
# contained the collapse frames ("is the only thing") at 1.1%, the same as the
# live corpus at 1.0% -- so they were never the cause of the collapse shape.
#
# Corrected rule: chain GENERATOR  <=>  >= 2 chained ASSISTANT turns
#                                     AND >= 1 chained USER turn.
def last_content_noun(text):
    ct = content_tokens(text)
    return ct[-1] if ct else None


def chain_count(row):
    """(chained assistant turns, chained user turns)."""
    turns = row.get("turns", [])
    ca = cu = 0
    for i, t in enumerate(turns):
        if i == 0:
            continue
        prev = last_content_noun(turns[i - 1].get("text", ""))
        if not prev:
            continue
        w = words(t.get("text", ""))
        if len(w) >= 3 and w[0] == "the" and w[1] == prev:
            if t.get("role") == "assistant":
                ca += 1
            elif t.get("role") == "user":
                cu += 1
    return ca, cu


def is_chained(row):
    ca, cu = chain_count(row)
    if not (ca >= 2 and cu >= 1):
        return False
    # Length guard: the chain generator emits SHORT turns ("the plaster kept
    # the shelf company").  A long hand-written row can chain by accident
    # (st2_sexy_000758 is a 10-turn stairwell story that echoes its own nouns);
    # those are keepers.  Mean assistant turn <= 12 words keeps the lens sharp.
    asst = [t.get("text", "") for t in row.get("turns", [])
            if t.get("role") == "assistant"]
    if not asst:
        return False
    return sum(len(words(x)) for x in asst) / len(asst) <= 12


# ---------------------------------------------------------------- row scan
def analyze_row(row, fname, line_no, gen_batch, user_pool, idf, rng, k):
    turns = row.get("turns", [])
    asst = [(i, t.get("text", "")) for i, t in enumerate(turns)
            if t.get("role") == "assistant"]
    user = [(i, t.get("text", "")) for i, t in enumerate(turns)
            if t.get("role") == "user"]

    frame_shell, frame_soft, loops, loop_shell = [], [], [], []
    for i, txt in asst:
        w = words(txt)
        for name, rx in FRAME_RE:
            if rx.search(txt):
                body = content_tokens(rx.sub(" ", txt))
                if len(body) == 0 or (len(w) <= SHELL_WORDS and len(body) <= SHELL_CONTENT):
                    frame_shell.append((name, i))
                else:
                    frame_soft.append((name, i))
        g = loop_gram(txt)
        if g:
            loops.append((g, i))
            if len(w) <= 8:
                loop_shell.append((g, i))

    # ---- the splice test: is each reply closer to its own turn than to a
    # random one?  (turn_delta's swap arm, per row).  Overlap is IDF-weighted
    # so a shared RARE noun counts as dependence and a shared common word
    # ("work", "money") does not.
    def dep_score(ct, other):
        return sum(idf.get(t, 1.0) for t in (ct & other))

    margins = []
    for i, txt in asst:
        if i - 1 < 0:
            continue
        ct = set(content_tokens(txt))
        if not ct:
            continue
        own = set(content_tokens(turns[i - 1].get("text", "")))
        s_own = dep_score(ct, own)
        js = [dep_score(ct, user_pool[rng.randrange(len(user_pool))])
              for _ in range(k)]
        margins.append(s_own - (sum(js) / len(js)))
    specific = sum(1 for m in margins if m > MARGIN)
    max_margin = max(margins) if margins else None
    flat_dep = bool(margins) and specific == 0

    # ---- anchor drift
    ua, aa = set(), set()
    for _, txt in user:
        ua |= anchors(txt)
    for _, txt in asst:
        aa |= anchors(txt)
    drift = bool(ua) and len(asst) >= 1 and not (ua & aa) and len(turns) > 2

    allw = words(" ".join(x for _, x in asst))
    ph_share = sum(1 for t in allw if t in PLACEHOLDERS) / max(1, len(allw))
    tele = bool(asst) and all(len(words(x)) < 4 for _, x in asst)

    # ---- action
    teleg = is_telegraphic(row)
    chained = is_chained(row)
    if gen_batch or teleg or chained:
        action, reason = "DELETE", "generator"
    elif frame_shell:
        action, reason = "DELETE", "frame_shell"
    elif loop_shell:
        action, reason = "DELETE", "loop_shell"
    elif frame_soft or loops or flat_dep or drift:
        action, reason = "REWRITE", ""
    else:
        action, reason = "KEEP", ""
    gen_kind = ("batch" if gen_batch else "") + ("+telegraphic" if teleg else "") \
        + ("+chained" if chained else "")

    # ---- severity for the rewrite queue (higher = worse / do first)
    sev = 0.0
    if flat_dep:
        sev += 3.0
    elif max_margin is not None and max_margin <= 4.0:
        sev += 1.5
    if drift:
        sev += 1.5
    if frame_soft:
        sev += 1.0
    if loops:
        sev += 1.0
    if tele:
        sev += 0.5
    if action == "DELETE":
        sev += 5.0

    return {
        "file": fname, "line": line_no, "id": row.get("id", ""),
        "batch_no": row.get("batch_no"), "action": action,
        "delete_reason": reason, "gen_kind": gen_kind,
        "severity": round(sev, 2),
        "specific": specific, "dep_turns": len(margins),
        "max_margin": None if max_margin is None else round(max_margin, 3),
        "frames": sorted({f[0] for f in frame_shell + frame_soft}),
        "frame_shell": sorted({f[0] for f in frame_shell}),
        "loops": sorted({l[0] for l in loops}),
        "loop_shell": sorted({l[0] for l in loop_shell}),
        "anchor_drift": drift, "flat_dep": flat_dep, "telegraphic": tele,
        "ph_share": round(ph_share, 3), "turns": len(turns),
        "sample": " | ".join(t.get("text", "") for t in turns)[:220],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="only files whose name contains this")
    ap.add_argument("--md", help="write the human report here")
    ap.add_argument("--json", dest="json_out", help="write the machine plan here")
    ap.add_argument("--top", type=int, default=10, help="samples per class")
    ap.add_argument("--queue", type=int, default=0,
                    help="also print a ranked rewrite queue of N rows")
    ap.add_argument("--k", type=int, default=8, help="random user turns per splice test")
    ap.add_argument("--apply-deletes", action="store_true")
    ap.add_argument("--confirm", action="store_true")
    ap.add_argument("--delete-classes", default="generator",
                    help="comma list of delete reasons to apply: generator, "
                         "frame_shell, loop_shell (default: generator ONLY -- the "
                         "shell lenses are ~93%% false positives on hand-read, so "
                         "opt into them only after reading the candidates)")
    ap.add_argument("--backup-dir", default=None)
    a = ap.parse_args()

    names = sorted(n for n in os.listdir(RAW) if n.endswith(".jsonl"))
    if a.file:
        names = [n for n in names if a.file in n]
    if not names:
        print("no raw files matched")
        return 2

    # corpus-wide pool of user-turn content-token sets (the splice control)
    # plus IDF over those tokens so a shared RARE noun counts and a shared
    # common word does not.
    user_pool = []
    df = collections.Counter()
    for name in names:
        for r in read_rows(os.path.join(RAW, name)):
            for t in r.get("turns", []):
                if t.get("role") == "user":
                    ct = set(content_tokens(t.get("text", "")))
                    if ct:
                        user_pool.append(ct)
                        for tok in ct:
                            df[tok] += 1
    if not user_pool:
        print("no user turns found")
        return 2
    n_docs = len(user_pool)
    idf = {tok: math.log(n_docs / (1.0 + c)) for tok, c in df.items()}
    rng = random.Random(SEED)

    all_ops = []
    per_file = {}
    grand = collections.Counter()
    for name in names:
        rows = read_rows(os.path.join(RAW, name))
        by_batch = collections.defaultdict(list)
        for r in rows:
            by_batch[r.get("batch_no")].append(r)
        gen_batches = {b for b, v in by_batch.items() if is_generator(batch_stats(v))}
        ops = [analyze_row(r, name, i, r.get("batch_no") in gen_batches,
                           user_pool, idf, rng, a.k)
               for i, r in enumerate(rows, 1)]
        per_file[name] = {"rows": len(rows),
                          "generator_batches": sorted(b for b in gen_batches if b is not None),
                          "ops": ops}
        for o in ops:
            grand[o["action"]] += 1
        all_ops.extend(ops)

    total = len(all_ops)
    multi = sum(1 for o in all_ops if o["turns"] > 2)
    n_flag = collections.Counter()
    spec = sum(o["specific"] for o in all_ops)
    dep = sum(o["dep_turns"] for o in all_ops)
    for o in all_ops:
        if o["flat_dep"]:
            n_flag["flat_dep"] += 1
        if o["anchor_drift"]:
            n_flag["anchor_drift"] += 1
        if o["frames"]:
            n_flag["frame"] += 1
        if o["loops"]:
            n_flag["loop"] += 1
        if o["telegraphic"]:
            n_flag["telegraphic"] += 1
        if o["frame_shell"]:
            n_flag["frame_shell"] += 1
        if o["loop_shell"]:
            n_flag["loop_shell"] += 1
    gen_rows = sum(1 for o in all_ops if o["batch_no"] in
                   set(b for f in per_file.values() for b in f["generator_batches"]))

    L = []
    L.append("# synth2 edit plan (in-place, no new rows)")
    L.append("")
    L.append("Files: %d   rows: %d   multi-turn: %d (%.0f%%)"
             % (len(names), total, multi, 100.0 * multi / max(1, total)))
    L.append("")
    L.append("## Actions")
    L.append("")
    L.append("| action | rows | meaning |")
    L.append("|---|---|---|")
    L.append("| DELETE | %d | machine output or a content-free shell |" % grand["DELETE"])
    L.append("| REWRITE | %d | real content, but frame/loop/turn-independent/anchor-drift |" % grand["REWRITE"])
    L.append("| KEEP | %d | passes every lens |" % grand["KEEP"])
    L.append("")
    L.append("## Flags (rows touched)")
    L.append("")
    L.append("| flag | rows |")
    L.append("|---|---|")
    for k in ("flat_dep", "anchor_drift", "frame", "frame_shell", "loop",
              "loop_shell", "telegraphic"):
        L.append("| %s | %d |" % (k, n_flag[k]))
    L.append("")
    gk = collections.Counter(o["gen_kind"] for o in all_ops
                             if o["delete_reason"] == "generator")
    L.append("Generator breakdown (DELETE rows): %s"
             % ", ".join("%s %d" % (k or "(none)", v)
                         for k, v in sorted(gk.items(), key=lambda x: -x[1])))
    L.append("")
    L.append("## The understanding number (IDF-weighted splice test)")
    L.append("")
    L.append("For each assistant turn, the IDF-weighted overlap with the user")
    L.append("turn it actually answers, minus the mean overlap with %d random"
             % a.k)
    L.append("user turns. Assistant turns that clear the margin (%.1f): **%d / %d"
             % (MARGIN, spec, dep))
    L.append("(%.1f%%)**. The other %.1f%% are no closer to their own turn than"
             % (100.0 * spec / max(1, dep),
                100.0 * (dep - spec) / max(1, dep)))
    L.append("to a random one -- the rows turn_delta is made of. A reply that")
    L.append("survives a different user turn spliced in front of it teaches the")
    L.append("model to ignore the turn. (Screen, not verdict: a reply can be")
    L.append("responsive by paraphrase with no shared token. Hand-read before")
    L.append("deleting; turn_delta.py is the model-level instrument.)")
    L.append("")
    L.append("## Per file")
    L.append("")
    L.append("| file | rows | DELETE | REWRITE | KEEP | flat_dep | drift | gen batches |")
    L.append("|---|---|---|---|---|---|---|---|")
    for name in names:
        ops = per_file[name]["ops"]
        c = collections.Counter(o["action"] for o in ops)
        fd = sum(1 for o in ops if o["flat_dep"])
        dr = sum(1 for o in ops if o["anchor_drift"])
        gb = per_file[name]["generator_batches"]
        L.append("| %s | %d | %d | %d | %d | %d | %d | %s |"
                 % (name.replace("small_talk_", "").replace(".jsonl", ""),
                    per_file[name]["rows"], c["DELETE"], c["REWRITE"], c["KEEP"],
                    fd, dr, ",".join("b%s" % b for b in gb) or "-"))
    L.append("")
    for action in ("DELETE", "REWRITE"):
        sel = [o for o in all_ops if o["action"] == action]
        if not sel:
            continue
        L.append("## %s samples (%d total)" % (action, len(sel)))
        L.append("")
        for o in sel[:a.top]:
            L.append("- `%s:%d` %s  sev=%.1f spec=%d/%d margin=%s"
                     % (o["file"], o["line"], o["id"][:10], o["severity"],
                        o["specific"], o["dep_turns"], o["max_margin"]))
            L.append("  - %s" % o["sample"])
        L.append("")

    if a.queue:
        q = sorted((o for o in all_ops if o["action"] == "REWRITE"),
                   key=lambda o: -o["severity"])[:a.queue]
        L.append("## Ranked rewrite queue (%d rows)" % len(q))
        L.append("")
        for o in q:
            L.append("- `%s:%d` sev=%.1f spec=%d/%d margin=%s"
                     % (o["file"], o["line"], o["severity"], o["specific"],
                        o["dep_turns"], o["max_margin"]))
    report = "\n".join(L)

    if a.md:
        with open(a.md, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(report + "\n")
        print("wrote %s" % a.md)
    if a.json_out:
        plan = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "totals": {"rows": total, "actions": dict(grand),
                           "flags": dict(n_flag), "specific": spec, "dep": dep},
                "per_file": per_file}
        with open(a.json_out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(plan, fh, indent=1)
        print("wrote %s" % a.json_out)
    if not a.md and not a.json_out:
        print(report)

    if a.apply_deletes:
        if not a.confirm:
            print("\nrefusing: --apply-deletes needs --confirm", file=sys.stderr)
            return 2
        return apply_deletes(all_ops, a)
    return 0


def apply_deletes(all_ops, a):
    wanted = {c.strip() for c in a.delete_classes.split(",") if c.strip()}
    dels = [o for o in all_ops if o["action"] == "DELETE"
            and o.get("delete_reason") in wanted]
    if not dels:
        print("nothing to delete for classes %s" % ",".join(sorted(wanted)))
        return 0
    print("applying delete classes: %s (%d rows)" % (",".join(sorted(wanted)), len(dels)))
    import tempfile
    backup = a.backup_dir or os.path.join(
        tempfile.gettempdir(), "synth2_edit_backup_%d" % int(time.time()))
    os.makedirs(backup, exist_ok=True)

    deadline = time.time() + 60
    while True:
        try:
            fd = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, b"edit_plan")
            os.close(fd)
            break
        except FileExistsError:
            if time.time() > deadline:
                print("could not take the lock", file=sys.stderr)
                return 2
            time.sleep(0.5)
    try:
        by_file = collections.defaultdict(set)
        for o in dels:
            by_file[o["file"]].add(o["line"])
        total_gone = 0
        for fname, lines in by_file.items():
            path = os.path.join(RAW, fname)
            shutil.copy2(path, os.path.join(backup, fname))
            with open(path, "rb") as fh:
                rows = fh.read().split(b"\n")
            keep, gone = [], 0
            for i, line in enumerate(rows, 1):
                if i in lines and line.strip():
                    gone += 1
                    continue
                keep.append(line)
            with open(path, "wb") as fh:
                fh.write(b"\n".join(keep))
            print("  %s: deleted %d rows" % (fname, gone))
            total_gone += gone
        print("backup: %s" % backup)
        print("deleted %d rows total" % total_gone)
    finally:
        try:
            os.unlink(LOCK_PATH)
        except OSError:
            pass
    print()
    print("NOW RUN THE GATES (this script does not):")
    print("  cargo run --release -p train --bin repair -- --data runs/synth2 --locations")
    print("  python runs/synth2/scripts/integrity.py")
    print("  python runs/synth2/scripts/qmark.py")
    print("  python runs/synth2/scripts/add_rows.py --status")
    print("  python runs/synth2/scripts/edit_plan.py   # re-scan, expect 0 generator")
    return 0


if __name__ == "__main__":
    sys.exit(main())
