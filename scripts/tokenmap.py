#!/usr/bin/env python3
"""tokenmap.py -- the token-attractor map for the synth2 corpus.

WHY THIS EXISTS
---------------
The campaign's failure mode is not noise, it is an ATTRACTOR.  Measured
2026-10-05 on 54,621 rows / 84,315 assistant turns against audit/probe_out7.txt:

  * 72% of the 50 probe outputs contain one of ~8 abstract frames
  * 60% open with "the"; 13/50 are literally "the X is a small thing ..."
  * the RAREST frames are the MOST amplified: "has ever been" is in 34 of
    84,315 assistant turns (0.04%) and 17 of 50 outputs -> 843x; "the whole"
    is in 2,440 turns and 8 outputs -> 6x

So the pathology is not common phrases, it is RARE, CONTENT-FREE frames -- the
only structure a 1.28M-param model can afford to memorise, because a frame fits
any prompt.  The readme's law, quantified: "a repeated CONTENT template trains
an attractor that leaks into unrelated prompts".

WHAT IT IS
----------
The CORPUS-SIDE instrument that puts the corpus and the MODEL on the SAME AXES.
edit_plan.py is row-level and model-agnostic; turn_delta.py is model-level and
corpus-agnostic.  tokenmap.py is the bridge: it counts what the corpus SAYS and
what the model REPEATS, and reports the ratio.

SIX VIEWS
  0. CHANGE       (only with --compare) the before/after delta per attractor
  1. ATTRACTORS   phrase, corpus share, model share, amplification, location
  2. OVER-USED    n-grams ranked by PMI (over-use relative to their parts)
  3. FAN-OUT      which registers carry each top attractor
  4. OPENER MAP   position x token, assistant and user, + copula-only
  5. STYLE LEAK   contraction rate, corpus vs model

ACCURACY NOTES (read these before quoting a number)
  * `n` / `corpus/10k` are TURN-CONTAINMENT: assistant turns containing the
    phrase at least once.  `user/10k` is the same over USER turns.
  * `model%` is the share of probe OUTPUTS containing the phrase.  Matching is
    case-insensitive for both phrases and frame regexes.
  * PMI uses OCCURRENCE counts: pmi = log2( (obs/total_n) /
    prod_i (count(w_i)/total_1) ).  n-gram counters are pruned to --min-count,
    so PMI is only defined at or above that count.
  * copula-only = turns that start with "the", contain " is ", and contain no
    action verb (the ACTION set below).  The plan quotes 8.9% from a different
    action-verb list; this is the reproducible definition.
  * the candidate phrases are KNOWN_FRAMES (today's collapse) + MAXIMAL frames
    DERIVED from the current probe (a phrase contained in a longer one is
    dropped) + every n-gram at or above --min-count, so the map follows the
    model as it changes instead of trusting a hardcoded list.
  * the `the`-opener is reported for BOTH roles.  31.7% of USER turns also
    start with "the" (2026-10-05), so the assistant's 22.9% is partly prompt
    mirroring -- fixing assistant turns alone will not clear it.

IT IS A FINDER, NEVER A VERDICT (editing law L2).  It ranks and locates; it
never deletes and never writes to raw/.  A phrase at the top of this table is a
CANDIDATE to hand-read, not a row to delete.

SCALING.  Everything is a small number of linear passes: tokenise once, count
n-grams once per n (pruned), and locate candidates by membership (cost is
independent of the number of candidates).  Measured 2026-10-05: 18.8s on
84,315 assistant turns, 32.1s on a doubled 168,630-turn corpus (~linear), and
every rate is IDENTICAL at 2x (22.9% / 31.7% / 7.4%) -- the map is
scale-invariant, so a number quoted today stays comparable as the corpus grows.

USAGE
  python runs/synth2/scripts/tokenmap.py
  python runs/synth2/scripts/tokenmap.py --probe runs/synth2/audit/probe_out7.txt
  python runs/synth2/scripts/tokenmap.py --md runs/synth2/audit/tokenmap.md \
                                         --json runs/synth2/audit/tokenmap.json
  python runs/synth2/scripts/tokenmap.py --compare runs/synth2/audit/tokenmap.json
"""
import argparse
import collections
import json
import math
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
AUDIT = os.path.normpath(os.path.join(HERE, "..", "audit"))
sys.path.insert(0, HERE)

# Reuse edit_plan.py's frame list and generator lens so the two instruments
# agree row for row (edit_plan says the same about integrity.py).  Fall back to
# a local copy if edit_plan cannot be imported, so the map never dies on an
# unrelated import error.
try:
    import edit_plan as EP
    FRAMES = list(EP.FRAMES)
    FUNC = set(EP.FUNC)
    WORD_CEIL = EP.WORD_CEIL
    NOFUNC_FLOOR = EP.NOFUNC_FLOOR
except Exception:  # pragma: no cover - defensive
    FRAMES = [
        ("whole_thing", r"\bthe whole (thing|point|time|street)\b"),
        ("only_thing", r"\bis the only (thing|one)\b"),
        ("that_is_the_whole", r"\bthat is the whole\b"),
        ("same_thing", r"\bthe same (thing|way|place)\b"),
        ("in_the_same_way", r"\bin the same way\b"),
    ]
    FUNC = set("a an the i you he she it we they and or but if so of to in on "
               "for with is was were be been am are do did does not no yes my "
               "your his her that this there what when who how why".split())
    WORD_CEIL, NOFUNC_FLOOR = 6.2, 40.0

FRAME_RE = [(n, re.compile(p)) for n, p in FRAMES]
FRAME_SET = set(n for n, _ in FRAMES)

# The collapse family observed 2026-10-05.  Kept as a curated seed; frames the
# CURRENT probe emits are DERIVED automatically on top of it, and a stale entry
# self-drops (its model share is 0).
KNOWN_FRAMES = [
    "small thing", "only thing", "has ever been", "the whole", "whole street",
    "never once", "and that is the", "is the only thing", "that is the whole",
    "it is the only",
]

# Verbs that make a "the X is Y" turn an ACTION, not a bare copula observation.
ACTION = set(
    "do did does get got go going gone went come came take took give gave make "
    "made say said tell told call called try tried put keep kept run ran buy "
    "bought send sent bring brought find found show showed leave left start "
    "started stop stopped turn turned look looked ask asked help helped work "
    "worked need needed want wanted use used move moved open opened close "
    "closed pick picked hold held sit sat stand stood walk walked drive drove "
    "read write wrote eat ate drink drank sleep slept wake woke pay paid play "
    "played wait waited watch watched listen listened speak spoke talk talked "
    "think thought know knew feel felt see saw hear heard".split()
)

CON_RE = re.compile(
    r"\b(it's|i'm|don't|can't|that's|you're|isn't|doesn't|didn't|won't|ain't|"
    r"i've|we're|they're|let's|there's)\b", re.I)


def words(text):
    """Same tokenizer as check.py / edit_plan.py."""
    return re.findall(r"[a-z0-9']+", str(text).lower())


def read_rows(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("id"):
            rows.append(r)
    return rows


def raw_files(data_dir):
    out = []
    for fn in sorted(os.listdir(data_dir)):
        if fn.endswith(".jsonl"):
            out.append((fn[len("small_talk_"):-len(".jsonl")], os.path.join(data_dir, fn)))
    return out


def load_corpus(data_dir):
    """(assistant turns, user turns, rows per file); a turn is (cat, batch, text)."""
    asst, user = [], []
    per_file = collections.Counter()
    for cat, path in raw_files(data_dir):
        for r in read_rows(path):
            per_file[cat] += 1
            for t in r.get("turns", []):
                role = t.get("role", "")
                txt = t.get("text", "")
                if role == "assistant":
                    asst.append((cat, r.get("batch_no"), txt))
                elif role == "user":
                    user.append((cat, r.get("batch_no"), txt))
    return asst, user, per_file


def latest_probe(audit_dir):
    """Newest probe_outN.txt by mtime, or None.  The probe number in the name
    is not reliable -- a re-probe can reuse a name -- so sort on mtime."""
    if not os.path.isdir(audit_dir):
        return None
    best = None
    for fn in os.listdir(audit_dir):
        if re.match(r"probe_out\d+.*\.txt$", fn):
            p = os.path.join(audit_dir, fn)
            if best is None or os.path.getmtime(p) > os.path.getmtime(best):
                best = p
    return best


def parse_probe(path):
    if not path or not os.path.exists(path):
        return []
    txt = open(path, encoding="utf-8").read()
    return re.findall(r'^\s*OUT:\s*"(.*)"\s*$', txt, re.M)


def ngram_counts(toks, max_n, keep_min):
    """Count n-grams over PRE-TOKENISED turns, with BOUNDED memory: one counter
    is live at a time and each n is pruned to count >= keep_min before the next
    starts.  (The naive all-n-at-once version OOM-killed the host.)  Returns
    (counters, totals); totals[n] is the TOTAL n-gram occurrences, which the
    pruned counter can no longer supply and PMI needs."""
    cnt, totals = {}, {}
    for n in range(1, max_n + 1):
        c = collections.Counter()
        tot = 0
        for w in toks:
            for i in range(len(w) - n + 1):
                c[" ".join(w[i:i + n])] += 1
                tot += 1
        totals[n] = tot
        if n > 1:
            c = collections.Counter({k: v for k, v in c.items() if v >= keep_min})
        cnt[n] = c
    return cnt, totals


def pmi(gram, cnt, totals):
    """log2( observed / expected-under-independence ).  Occurrence based."""
    ws = gram.split()
    obs = cnt[len(ws)].get(gram, 0)
    total = totals.get(len(ws), 0)
    uni_total = totals.get(1, 0)
    if obs == 0 or total == 0 or uni_total == 0:
        return 0.0
    exp = total
    for w in ws:
        p = cnt[1].get(w, 0) / uni_total
        if p <= 0:
            return 0.0
        exp *= p
    if exp <= 0:
        return 0.0
    return math.log2(obs / exp)


def locate(phrases, turns, is_regex=False):
    """phrase -> Counter(file) over turns CONTAINING it (at least once).

    Membership, not scan-per-phrase: the inner loop enumerates the turn's own
    n-grams and tests set membership, so the cost is O(turns x max_phrase_len)
    and is INDEPENDENT of how many candidates there are.  That is what keeps
    this flat as the corpus grows."""
    phrases = list(phrases)
    out = {ph: collections.Counter() for ph in phrases}
    if not phrases:
        return out
    if is_regex:
        rxs = {ph: dict(FRAME_RE)[ph] for ph in phrases}
        for cat, _b, txt in turns:
            lo = txt.lower()
            for ph, rx in rxs.items():
                if rx.search(lo):
                    out[ph][cat] += 1
        return out
    pset = set(phrases)
    maxlen = max(len(p.split()) for p in phrases)
    for cat, _b, txt in turns:
        w = words(txt)
        seen = set()
        for n in range(1, maxlen + 1):
            for i in range(len(w) - n + 1):
                g = " ".join(w[i:i + n])
                if g in pset:
                    seen.add(g)
        for g in seen:
            out[g][cat] += 1
    return out


def out_hits(phrase, out_norm):
    needle = " " + phrase + " "
    return sum(1 for s in out_norm if needle in " " + s + " ")


def out_hits_re(rx, outs_lower):
    """outs_lower MUST be pre-lowercased: the frame regexes are lowercase, and
    an un-lowered output silently misses an uppercase frame."""
    return sum(1 for s in outs_lower if rx.search(s))


def copula_only(text):
    """A bare copula observation: starts with "the", carries " is ", and has no
    action verb anywhere.  Documented because the plan's 8.9% used a different
    action-verb list -- this is the reproducible one."""
    lo = text.lower().strip()
    if not lo.startswith("the ") or " is " not in lo:
        return False
    return not (set(words(lo)) & ACTION)


def opener_map(turns):
    pos = {0: collections.Counter(), 1: collections.Counter(),
           2: collections.Counter(), "last": collections.Counter()}
    denom = collections.Counter()
    for _cat, _b, txt in turns:
        w = words(txt)
        if not w:
            continue
        denom[0] += 1
        pos[0][w[0]] += 1
        if len(w) > 1:
            denom[1] += 1
            pos[1][w[1]] += 1
        if len(w) > 2:
            denom[2] += 1
            pos[2][w[2]] += 1
        denom["last"] += 1
        pos["last"][w[-1]] += 1
    return pos, denom


def model_ngram_share(outs, max_n):
    """n-gram -> number of OUTPUTS containing it (deduped within an output).
    Built once, so scoring candidates is a dict lookup, not a rescan."""
    c = collections.Counter()
    for o in outs:
        w = words(o)
        seen = set()
        for n in range(1, max_n + 1):
            for i in range(len(w) - n + 1):
                seen.add(" ".join(w[i:i + n]))
        for g in seen:
            c[g] += 1
    return c


def derive_probe_frames(mshare, min_out, limit, max_words=4):
    """The top multi-word phrases the MODEL actually emits, as candidates.  This
    is what keeps the map honest as the model changes: the collapse family is
    read off the probe, not trusted from a list.

    Only MAXIMAL phrases are returned -- a phrase contained in a longer one is
    dropped, so the list is frames ("is a small thing"), not every nested
    sub-phrase ("a small", "small thing").  Capped at max_words so a derived
    candidate is frame-sized, not a whole sentence."""
    cands = [g for g, cnt in mshare.items()
             if cnt >= min_out and 2 <= len(g.split()) <= max_words]
    kept = [g for g in cands if not any(g != k and g in k for k in cands)]
    kept = sorted(set(kept), key=lambda g: (-mshare[g], -len(g), g))
    return kept[:limit]


def main():
    ap = argparse.ArgumentParser(description="synth2 token-attractor map")
    ap.add_argument("--data", default=RAW)
    ap.add_argument("--audit", default=AUDIT, help="where to find probe_outN.txt")
    ap.add_argument("--probe", default=None,
                    help="probe file; default = newest probe_out*.txt in --audit")
    ap.add_argument("--md", default=None)
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--compare", default=None,
                    help="a previous tokenmap.json; prints the per-attractor delta")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--min-count", type=int, default=8,
                    help="minimum corpus occurrence count for an n-gram candidate")
    ap.add_argument("--max-n", type=int, default=5)
    ap.add_argument("--candidates", type=int, default=80,
                    help="how many candidates to measure precisely")
    ap.add_argument("--no-derive", action="store_true",
                    help="do not derive frames from the probe")
    a = ap.parse_args()

    data_dir = os.path.normpath(a.data)
    asst, user, per_file = load_corpus(data_dir)
    N = len(asst)
    Nu = len(user)
    probe_path = a.probe or latest_probe(a.audit)
    outs = parse_probe(probe_path)
    if probe_path and not outs:
        # Concurrent writers rewrite the probe; a truncated read looks exactly
        # like "the model emits nothing".  Say so instead of reporting an empty
        # model layer as if it were a finding.
        print("WARN: no probe outputs parsed from %s -- model layer skipped "
              "(probe mid-write, or the OUT: format changed)" % probe_path,
              file=sys.stderr)
    outs_lower = [o.lower() for o in outs]
    out_norm = [" ".join(words(o)) for o in outs]
    n_out = len(outs) or 1

    # one tokenisation, reused by the counter and the locator
    asst_toks = [words(t) for _c, _b, t in asst]
    cnt, totals = ngram_counts(asst_toks, a.max_n, a.min_count)
    mshare = model_ngram_share(outs, a.max_n) if outs else collections.Counter()

    # ---- candidate set ----------------------------------------------------
    ng_cand = [(n, g, c) for n in range(2, a.max_n + 1) for g, c in cnt[n].items()]
    derived = [] if a.no_derive else derive_probe_frames(
        mshare, max(2, int(0.08 * n_out)), 15)
    plain_cands = [p for p in dict.fromkeys(KNOWN_FRAMES + derived + [g for _n, g, _c in ng_cand])
                   if p not in FRAME_SET]

    # ---- measure every candidate the same way: turns containing it --------
    loc_a = locate(plain_cands, asst, False)
    loc_a.update(locate(sorted(FRAME_SET), asst, True))

    def model_share_of(ph):
        if ph in FRAME_SET:
            return out_hits_re(dict(FRAME_RE)[ph], outs_lower) / n_out
        return mshare.get(ph, 0) / n_out

    pre = []
    for ph in list(loc_a.keys()):
        c = sum(loc_a[ph].values())
        cs = c / max(1, N)
        ms = model_share_of(ph)
        if ms <= 0 or c < a.min_count:
            continue
        amp = ms / cs if cs > 0 else 0.0
        pre.append((ms * (1.0 + math.log2(1.0 + amp)), ph, c, cs, ms, amp))
    pre.sort(reverse=True)
    pre = pre[:a.candidates]

    att = [{"phrase": ph, "count": c, "corpus": round(cs * 10000, 1),
            "model": round(ms * 100, 0), "amplify": round(amp, 0),
            "score": round(sc, 4),
            "files": ", ".join("%s %d" % (f, k) for f, k in loc_a[ph].most_common(3))}
           for sc, ph, c, cs, ms, amp in pre]

    # collapse each containment family to its best-scoring member
    kept = []
    for d in att:
        if any(d["phrase"] in k["phrase"] or k["phrase"] in d["phrase"] for k in kept):
            continue
        kept.append(d)
    att = kept[:a.top]

    # user side: is the phrase a shared frame (in the PROMPTS too)?
    loc_u = locate([d["phrase"] for d in att if d["phrase"] not in FRAME_SET], user, False)
    loc_u.update(locate([d["phrase"] for d in att if d["phrase"] in FRAME_SET], user, True))
    for d in att:
        d["user"] = round(10000.0 * sum(loc_u.get(d["phrase"], {}).values()) / max(1, Nu), 1)

    # ---- 2. over-used n-grams by PMI --------------------------------------
    over = sorted(((pmi(g, cnt, totals), g, c, n) for n, g, c in ng_cand), reverse=True)
    over = over[:a.top]

    # ---- 3. attractor fan-out ---------------------------------------------
    files = [f for f, _ in raw_files(data_dir)]
    fan_files = {d["phrase"]: sum(1 for f in files if loc_a[d["phrase"]][f] > 0)
                 for d in att}
    covered = {f for d in att for f in files if loc_a[d["phrase"]][f] > 0}

    # ---- 4. opener maps + copula-only -------------------------------------
    pos, denom = opener_map(asst)
    upos, udenom = opener_map(user)
    the_open = pos[0]["the"] / max(1, denom[0])
    the_open_u = upos[0]["the"] / max(1, udenom[0])
    cop = sum(1 for _c, _b, t in asst if copula_only(t))
    cop_rate = cop / max(1, N)

    # ---- 5. style leak: contractions --------------------------------------
    con_hits, con_tot = collections.Counter(), collections.Counter()
    for cat, _b, txt in asst:
        con_tot[cat] += 1
        if CON_RE.search(txt.lower()):
            con_hits[cat] += 1
    corpus_con = sum(con_hits.values()) / max(1, N)
    model_con = (sum(1 for o in outs if CON_RE.search(o)) / n_out) if outs else 0.0

    # ---- report ------------------------------------------------------------
    L = []
    P = L.append
    P("# synth2 token-attractor map")
    P("")
    P("Generated %s  |  corpus %d rows, **%d assistant turns**, %d user turns"
      % (time.strftime("%Y-%m-%d %H:%M"), sum(per_file.values()), N, Nu))
    P("Probe: `%s` (%d outputs)"
      % (os.path.basename(probe_path) if probe_path else "none", len(outs)))
    P("")
    P("**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to")
    P("hand-read. Nothing here is deleted; nothing here is written to `raw/`.")
    P("")

    if a.compare and os.path.exists(a.compare):
        try:
            old = json.load(open(a.compare, encoding="utf-8"))
        except Exception as exc:
            old = None
            print("WARN: could not read --compare %s (%s)" % (a.compare, exc),
                  file=sys.stderr)
        if old:
            oh = old.get("headline", {})
            oatt = {d["phrase"]: d for d in old.get("attractors", [])}
            P("## 0. Change since %s" % old.get("generated", "?"))
            P("")
            P("| metric | was | now | delta |")
            P("|---|---|---|---|")
            for label, key, now in (
                    ("`the`-opener (assistant)", "the_opener", the_open),
                    ("`the`-opener (user)", "the_opener_user", the_open_u),
                    ("copula-only", "copula_only", cop_rate)):
                was = oh.get(key)
                if was is None:
                    continue
                P("| %s | %.1f%% | %.1f%% | %+.1f |"
                  % (label, was * 100, now * 100, (now - was) * 100))
            P("")
            P("| attractor | model% was | model% now | amplify was | amplify now |")
            P("|---|---|---|---|---|")
            for d in att[:10]:
                o = oatt.get(d["phrase"])
                if not o:
                    P("| `%s` | - | %d%% | - | %dx |" % (d["phrase"], d["model"], d["amplify"]))
                else:
                    P("| `%s` | %d%% | %d%% | %dx | %dx |"
                      % (d["phrase"], o.get("model", 0), d["model"],
                         o.get("amplify", 0), d["amplify"]))
            P("")

    P("## Headline")
    P("")
    P("| metric | value | target |")
    P("|---|---|---|")
    P("| `the`-opener (assistant) | %.1f%% | < 12%% |" % (the_open * 100))
    P("| `the`-opener (user) | %.1f%% | n/a |" % (the_open_u * 100))
    P("| copula-only turns | %.1f%% | < 4%% |" % (cop_rate * 100))
    P("| registers carrying a top attractor | %d / %d | n/a |"
      % (len(covered), len(files)))
    if outs:
        P("| probe outputs carrying a top attractor | %d / %d | 0 |"
          % (sum(1 for s in out_norm
                 if any((" " + d["phrase"] + " ") in (" " + s + " ")
                        for d in att if d["phrase"] not in FRAME_SET)), len(outs)))
    P("")

    P("## 1. Attractors (corpus says it vs model repeats it)")
    P("")
    P("Ranked by priority = model share x (1 + log2(amplification)), so a")
    P("phrase must BOTH be over-represented AND actually be emitted to rank")
    P("high. `n` is the raw count of assistant turns containing it, `corpus/10k`")
    P("per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase")
    P("high on both is a shared frame), `model%` the share of probe outputs")
    P("containing it, `amplify` = model share / corpus share. One row per family.")
    P("")
    P("| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |")
    P("|---|---|---|---|---|---|---|")
    for d in att:
        P("| `%s` | %d | %s | %s | %d%% | %dx | %s |"
          % (d["phrase"], d["count"], d["corpus"], d["user"], d["model"],
             d["amplify"], d["files"] or "-"))
    P("")

    P("## 2. Over-used n-grams (ranked by PMI, count >= %d)" % a.min_count)
    P("")
    P("PMI = how much more often the phrase occurs than its parts predict. This")
    P("finds phrases the corpus over-uses that may not have surfaced in the")
    P("probe yet.")
    P("")
    P("| n-gram | n | count | PMI | files (top 3) |")
    P("|---|---|---|---|---|")
    oloc = locate([g for _p, g, _c, _n in over], asst, False)
    for p, g, c, n in over:
        cf = oloc.get(g, collections.Counter())
        P("| `%s` | %d | %d | %.1f | %s |"
          % (g, n, c, p, ", ".join("%s %d" % (f, k) for f, k in cf.most_common(3)) or "-"))
    P("")

    P("## 3. Attractor fan-out (which registers carry each top attractor)")
    P("")
    P("A phrase in one register is a voice; a phrase in twenty is the fan-out")
    P("that leaks into unrelated prompts.")
    P("")
    P("| attractor | registers | worst registers |")
    P("|---|---|---|")
    for d in att:
        c = loc_a[d["phrase"]]
        worst = ", ".join("%s %d" % (f, n) for f, n in c.most_common(4) if n)
        P("| `%s` | %d | %s |" % (d["phrase"], fan_files[d["phrase"]], worst or "-"))
    P("")

    P("## 4. Opener maps")
    P("")
    for label, pp, dd in (("assistant", pos, denom), ("user", upos, udenom)):
        for k in (0, 1, 2, "last"):
            d = max(1, dd.get(k, 0))
            top = ", ".join("%s %.1f%%" % (w, 100.0 * c / d)
                            for w, c in pp[k].most_common(6))
            P("- %s pos %s (n=%d): %s" % (label, k, dd.get(k, 0), top))
    P("")

    P("## 5. Style leak: contractions")
    P("")
    P("Corpus assistant turns with a contraction: **%.1f%%**; model outputs: "
      "**%.1f%%**. The corpus keeps them almost entirely in two registers -- if "
      "the model uses them everywhere, the register boundary has leaked (the "
      "same failure as a frame fan-out, one level down: style, not phrase)."
      % (corpus_con * 100, model_con * 100))
    P("")
    P("| register | turns with a contraction |")
    P("|---|---|")
    for cat, n in con_hits.most_common(8):
        P("| %s | %d / %d |" % (cat, n, con_tot[cat]))
    P("")

    md = "\n".join(L) + "\n"
    if a.md:
        open(a.md, "w", encoding="utf-8").write(md)
        print("wrote %s" % a.md)
    else:
        print(md)

    if a.json_out:
        payload = {
            "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "corpus": {"rows": sum(per_file.values()), "assistant_turns": N,
                       "user_turns": Nu, "files": per_file},
            "probe": {"path": probe_path, "outputs": len(outs)},
            "params": {"top": a.top, "min_count": a.min_count, "max_n": a.max_n,
                       "candidates": a.candidates, "derived_frames": derived},
            "headline": {"the_opener": round(the_open, 4),
                         "the_opener_user": round(the_open_u, 4),
                         "copula_only": round(cop_rate, 4),
                         "registers_with_attractor": len(covered),
                         "registers": len(files)},
            "attractors": att,
            "over_used": [{"ngram": g, "n": n, "count": c, "pmi": round(p, 2)}
                          for p, g, c, n in over],
            "fanout": {d["phrase"]: {"registers": fan_files[d["phrase"]],
                                     "per_register": dict(loc_a[d["phrase"]])}
                       for d in att},
            "openers": {"assistant": {str(k): dict(pos[k].most_common(20)) for k in pos},
                        "user": {str(k): dict(upos[k].most_common(20)) for k in upos}},
            "contractions": {"corpus": round(corpus_con, 4),
                             "model": round(model_con, 4),
                             "per_register": dict(con_hits)},
        }
        open(a.json_out, "w", encoding="utf-8").write(json.dumps(payload, indent=2))
        print("wrote %s" % a.json_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
