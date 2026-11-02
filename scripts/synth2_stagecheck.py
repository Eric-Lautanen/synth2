#!/usr/bin/env python3
"""synth2_stagecheck.py -- Fable2's pre-staging gate for a hand-written batch.

Runs on the BATCH JSON (the [{"turns": [[role, text], ...]}] form that
add_rows.py consumes) BEFORE it is handed to the lane lead. It is the layer on
top of synth2_preflight.py (shape / repeats / near-dup / mix) and encodes every
check the lead has asked Fable2 to fold in (lead msg #106, 2026-10-16):

  BAND      every assistant reply is 10-13 words (HARD law)
  ECHO      house cw() overlap on every (user, assistant) pair -- zero is a bug
  OPENERS   user turn-1 first word < 18 of 62; 'did' reply-openers <= 6
  WATCHLIST 'were you able to', 'have you tried', 'did you get', 'at all'
            endings, the 'is just X' verdict template (all ZERO in new batches)
  FRAMES    the 16 KNOWN_FRAMES from edit_plan.py
  5GRAMS    repeated assistant 5-grams inside the batch AND vs the live corpus
            (cross-batch, e.g. 'how are you supposed to' reached 4 batches)
  HYGIENE   non-ascii / dash / hyphen / apostrophe
            (apostrophes are LEGAL in the sexy and casual registers -- pass
             --register sexy|casual to allow them; angry carries zero, lazy one
             in 2155 turns, so both stay strict. no flag = strict.)
  SLOP      the 14 banned verdict nouns, 'a real', is-frame copulas
  PROBE     overlap of any turn against all 60 prompt_eval.py prompts

Usage: python synth2_stagecheck.py <batch.json> [--live raw/small_talk_angry.jsonl]
Read-only; never writes.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

# ---- the authoritative house content-word function (== _lane_preflight.py) ---
STOP = set("""a an the and or but if then than so as of to in on at for with from by about into over after
is are was were be been being am do does did doing have has had having i you he she it we they me him them
my your his its our their this that these those there here what which who whom when where why how not no nor
too very can will just should now would could oh ok okay yeah hey hi uh um well really much more most
get got go going went gone do done make made""".split())


def cw(t):
    return set(w for w in re.findall(r"[a-z']+", t.lower())
               if w not in STOP and len(w) > 1)


def words(t):
    return t.split()


def grams(t, n):
    w = re.findall(r"[a-z0-9]+", t.lower())
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]


def fw(t):
    m = re.findall(r"[a-z0-9']+", t.lower())
    return m[0] if m else ""


# ---- the project's canonical content-free frames (edit_plan.py FRAMES) -------
FRAMES = [
    ("monument", r"\bis a monument\b"), ("museum", r"\bis a museum\b"),
    ("photo_counter", r"\bphoto of the counter\b"), ("photo_crew", r"\bphoto of the crew\b"),
    ("is_a_crew", r"\bis a crew\b"), ("crew_is_a_crew", r"\bcrew is a crew\b"),
    ("whole_thing", r"\bthe whole (thing|point|time|street)\b"),
    ("been_going_to", r"\bi have been going to\b"),
    ("not_gonna_say", r"\bnot going to say it\b"),
    ("only_one", r"\byou are the only one\b"), ("only_thing", r"\bis the only (thing|one)\b"),
    ("been_told", r"\bi have been told\b"), ("that_is_the_whole", r"\bthat is the whole\b"),
    ("in_the_same_way", r"\bin the same way\b"),
    ("same_thing", r"\bthe same (thing|way|place)\b"),
    ("since_the_whole_time", r"\bsince the whole time\b"),
]
FRAME_RE = [(n, re.compile(p)) for n, p in FRAMES]

# ---- US SPELLING (lead msg #176; canonical list == tmp_verify_b4160.py) ------
# The verify pattern had no spelling check at all until it caught 'neighbours' and
# 'licence' in b4160 (and 'labelled' in b4145) by hand. Every row in this corpus
# is US English, so a British stem is a defect in ANY turn, user or assistant.
#
# Two stems are excluded outright, same reason the lead gives: 'fulfil' and
# 'distil', because 'fulfilled' and 'distillery' are the correct US forms and a
# bare-stem match would flag legal writing.
#
# Two more need the same protection but can keep their bare form, so they are
# matched with a lookahead instead of being dropped: 'appal' and 'enthral'. Their
# -ed/-ing forms are IDENTICAL in US and UK ('appalled', 'appalling',
# 'enthralled', 'enthralling'), and the US verb takes a double l ('appall',
# 'enthrall'), so the British spelling is only the bare stem and -s. Excluding
# them would lose 'appals'/'enthrals'; the lookahead keeps those and clears the
# shared inflections.
BRIT_STEMS = [
    "neighbour", "colour", "favour", "honour", "humour", "rumour", "labour", "endeavour",
    "behaviour", "armour", "harbour", "valour", "vigour", "saviour", "flavour", "odour", "parlour",
    "centre", "theatre", "metre", "litre", "fibre", "calibre", "lustre", "sombre", "sabre", "sceptre",
    "realise", "recognise", "organise", "apologise", "prioritise", "specialise", "criticise",
    "categorise", "emphasise", "memorise", "sympathise", "analyse", "paralyse",
    "licence", "practise", "defence", "offence", "pretence",
    "travelling", "travelled", "labelling", "labelled", "modelling", "modelled", "marvellous",
    "counsellor", "jewellery", "fuelled", "fuelling", "totalling", "signalling", "quarrelled", "quarrelling",
    "grey", "tyre", "kerb", "plough", "mould", "whilst", "amongst", "storey", "aeroplane",
    "aluminium", "sulphur", "manoeuvre", "paediatric", "instalment", "enrolment",
    "skilful", "wilful", "favourite", "cosy", "moustache",
    "cheque", "pyjamas", "programme", "gramme", "orientated", "lorry", "fortnight",
    # --- lead msg #180: the ten b4175 substitutions, the gate-able half of them ---
    # These are VOCABULARY, not spelling: no US suffix fixes them, the word itself is
    # British. They came from the lead hand-reading b4175, which is exactly the tier
    # this gate could not see -- so they go in the gate and stop costing a hand-read.
    "satnav", "roadworks", "waistcoat", "promenade", "stallholder", "motorway",
    "car boot",
    # --- msg #339: adopted from the lead's verify, which caught these three times ---
    # "queue" is US-legal only as "print queue"; in this register a line of people or
    # jobs is British and the US word is "line". The gate missed it on b4715 row 30.
    "queue",
]
# Deliberately NOT stems (lead msg #180), and the reasons are the useful part:
#   cupboard    legal US for kitchen cabinets; the b4175 L56 fix was a CONTEXT call
#   carriage    legal US (railroad carriage, baby carriage)
#   wafer       legal US (wafer cookie, wafer-thin)
#   services    "the services" is the British motorway term, but the word alone is not
#   burger van  two ordinary US words in sequence; only the COMPOUND is British
# Those five stay hand-read items. Adding them would flag legal US prose and train
# the reader to ignore the gate, which is worse than missing them.
BRIT_LOOKAHEAD = [r"appal(?!l|led|ling)", r"enthral(?!l|led|ling)"]
# "car boot" is the one multi-word stem: the join still works because \b anchors the
# start and \w* only has to cover a trailing s.
BRIT_RE = re.compile(r"\b(" + "|".join(BRIT_STEMS + BRIT_LOOKAHEAD) + r")\w*")

# ---- CONTEXT-GATED BRITISH (msg #339) ----------------------------------------
# `cupboard` stays OUT of BRIT_STEMS for the reason recorded above (#180): it is legal
# US for kitchen cabinets. But the lead's verify flagged it on b4700 and b4715, and in
# both cases it was a BRITISH COLLOCATION -- "lost property cupboard" -- not a kitchen
# cabinet. So gate the context, not the word: anything except "kitchen cupboard".
# A bare-word stem would have flagged legal US prose; this flags only what bit us.
CUPBOARD_RE = re.compile(r"(?<!kitchen )\bcupboard\b", re.I)

# ---- WATCHLIST (lead msg #106: keep these at ZERO in new angry batches) ------
WATCHLIST = [
    ("were_you_able_to", r"\bwere you able to\b"),      # PMI 22.6, still live
    ("have_you_tried", r"\bhave you tried\b"),
    ("did_you_get", r"\bdid you get\b"),
    ("at_all_ending", r"\bat all[.?!]?$"),
    ("is_just_x", r"\bis just\b"),
    # --- msg #339: adopted from the lead's verify ---
    ("the_one", r"\bthe one\b"),        # pronominal substitute; his verify caught it twice
    ("counts_as", r"\bcounts as\b"),
]
WATCH_RE = [(n, re.compile(p)) for n, p in WATCHLIST]

# ---- BANNED IS-FRAME REGEX (lead msg #106, sentence-initial) -----------------
# (the|a|an) then 2-40 chars with no .?! then (is|are) then (a|an|the).
IS_FRAME_RE = re.compile(
    r"(?:^|[.?!]\s+)(?:the|a|an)\s+[^.?!]{2,40}?\s(?:is|are)\s+(?:a|an|the)\s", re.I)

# ---- SENTENCE-INITIAL COPULA (lead msg #218) --------------------------------
# "the sentence initial is frame, any edited reply matching is are was were at
# position zero." The determiner regex above is the OLDER rule (#106) and does
# NOT catch a reply that simply OPENS on a copula -- that gap let 8 of them
# through b4430 while this gate reported isframe=0.
INIT_COPULA_RE = re.compile(r"^\s*(is|are|was|were)\b", re.I)

# ---- VERDICT-NOUN BAN (lead msg #106: 14, whole-word, any reply) -------------
VERDICT_NOUNS = {"robbery", "theft", "scam", "bait", "nightmare", "stings",
                 "rough", "brutal", "timing", "bold", "classic", "dirty",
                 "sneaky", "underhanded"}
VERDICT_RE = re.compile(r"\b(" + "|".join(sorted(VERDICT_NOUNS)) + r")\b")

# ---- the 60 prompt_eval.py prompts (probe-overlap screen) --------------------
PROBES = [
    "so what is going on with you this weekend?", "it rained the whole way in today.",
    "i still need to get groceries before the store closes.",
    "i could not fall asleep until like two last night.", "you up to anything today?",
    "the weekend came and went so fast.", "my order came cold and half missing.",
    "someone took my parking spot again.", "you have that look in your eyes tonight.",
    "save me a dance later, will you?", "lovely weather we are having this week.",
    "how was your commute in this morning?", "oh great, another meeting invite.",
    "my inbox has two hundred unread emails.", "guess what, i got the job!",
    "we are going away this weekend!", "dark by four again, winter is here.",
    "nothing good on tv ever anymore.", "my heart has been racing since three am.",
    "the review invite has no agenda attached.",
    "did you hear about apartment nine upstairs?",
    "word is the promotion is already decided.",
    "remember the candy store lines at recess?", "summers felt longer back then, right?",
    "do you ever wonder why time speeds up as you get older?",
    "what do you think actually matters in the end?",
    "nice haircut, did you do it yourself?",
    "you have been on that phone all day, haven't you?",
    "i am having a really rough week.", "i did not get the job, i am crushed.",
    "i am so bored i have cleaned the whole apartment.", "there is nothing to do tonight.",
    "what did you end up doing about the car?", "how did you two actually meet?",
    "did you ever send that message?", "so, about that thing we talked about.",
    "my bus was late again and then the driver just sat there.",
    "three parcels lost this month, three.", "you are trouble, you know that?",
    "buy me a drink and i might forgive you.", "fine.", "whatever, it does not matter.",
    "we finally finished the project!", "i passed my driving test first time!",
    "wait, so who is actually in charge?", "sorry, i do not follow, say that again?",
    "she still owes me twenty bucks from march.",
    "i am not inviting him, not after last time.",
    "i just sneezed and my lamp turned off, that is not normal.",
    "my toast came out shaped like a face.", "morning! how are you?",
    "hey, long time no see!", "no idea, honestly.", "i have no clue, sorry.",
    "thanks so much for the other day.", "that was really kind of you, thank you.",
    "sorry i am late, the traffic was awful.", "my bad, i completely forgot.",
    "right, i am off, see you later.", "anyway, i should go, take care!",
]
PROBE_CW = [(p, cw(p)) for p in PROBES]

# ---- VERIFY-PATTERN STOP LIST (lead msg #233) -------------------------------
# The house probe rule is: TWO OR MORE shared content words, where content means
# tokens minus THIS list, verbatim. No sig filter, no generic list of my own --
# the two instruments drifted precisely because I invented a second filter.
# Source: tmp_verify_bNNNN.py, the per-batch verify pattern.
VERIFY_STOP = set("""a an the i you he she it we they me him her us them my your his its our their
this that these those is are was were be been being am do does did have has had will would
can could should shall may might must of in on at to for with from by about as into and or
but so if then than too very just not no yes up down out off over under again once here
there when where why how what which who whom whose before after until while during because
through between against above below both each few more most other some such only own same
all any every little much now ever never still even also""".split())
VERIFY_STRONG = ["bus", "driver", "commute", "parking", "parcels", "inbox", "haircut",
                 "groceries", "toast", "lamp"]

def vcontent(t):
    """Content words exactly as the house verify pattern counts them."""
    return set(x for x in re.findall(r"[a-z0-9']+", t.lower()) if x not in VERIFY_STOP)

PROBE_VC = [(p, vcontent(p)) for p in PROBES]
# sharing ONLY these with a probe is mood overlap, not topic drift.
GENERIC = set("""again late whole way time day week weekend morning night evening
today tomorrow back right left still last first next good bad long short big small
new old same other thing things point matter while home over after before ever
anymore never nothing anything everything someone anyone everyone nobody really
actually honestly anyway sorry thanks thank fine whatever guess hear heard little
much more most less least only even just all up like another charge lost cleaned
crushed kind sort lot bit while""".split())
NUMERALS = set("""one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty
fifty sixty seventy eighty ninety hundred thousand""".split())
# An echo anchor must be a SUBSTANTIVE shared token. Sharing ONLY one of these
# (e.g. "again") does not satisfy the echo law -- the lead's b3875 row 61 passed
# on "again" alone while billed/billing was inflection-only (lead msg #109).
# EXTENDED per lead msg #116 (b3890 rows 47 + 57 passed my gate on a reflexive
# or indefinite alone): reflexives + indefinites + bare direction particles.
ECHO_TRIVIAL = set("""again before off now still even back just only then ever
never always maybe really quite very much more most too also around away here
there soon later early today tomorrow yesterday once twice together anyway
himself herself itself themselves anything nothing something everything anyone
nobody somebody everybody up down out one ones""".split())
# the probe's distinctive signature nouns -- a single one of these in a turn is
# enough to mark a phrasing mirror (the lead's b3860 rows 1 and 36).
STRONG = {"bus", "driver", "commute", "parking", "parcels", "inbox", "haircut",
          "groceries", "toast", "lamp"}


def norm_turns(row):
    out = []
    for t in row["turns"]:
        if isinstance(t, (list, tuple)):
            out.append((t[0], t[1]))
        else:
            out.append((t["role"], t["text"]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--live", default=None,
                    help="raw/*.jsonl to screen cross-batch 5-grams against")
    ap.add_argument("--raw", default=r"C:\github\DBllm\runs\synth2\raw")
    # Scaled thresholds for a PARTIAL batch (the 16-row finisher, lead msg #120).
    # Defaults are the 62-row law; pass these to gate a differently-sized batch.
    ap.add_argument("--u1cap", type=int, default=18,
                    help="user turn-1 opener cap: FAILS at >= this (house rule, lead #235)")
    ap.add_argument("--didcap", type=int, default=6, help="'did' reply-opener cap")
    ap.add_argument("--qmin", type=int, default=33)
    ap.add_argument("--qmax", type=int, default=38)
    ap.add_argument("--qset", action="store_true",
                    help="enforce the question band even when the batch is not 67 replies")
    ap.add_argument("--alwayscap", type=int, default=4)
    ap.add_argument("--wholecap", type=int, default=4)
    ap.add_argument("--thewcap", type=int, default=2)
    # Apostrophe register flag (lead msg #156 standing item). The corpus is not
    # uniform: sexy and casual legitimately carry contractions ("you've", "thats"),
    # angry carries ZERO in 2000 rows and lazy has one in 2155 turns. So the
    # apostrophe rule has to know which lane it is gating, or it either fails every
    # legal sexy batch or waves through an angry one.
    ap.add_argument("--register", choices=["sexy", "casual", "lazy", "angry"],
                    default=None,
                    help="lane being gated; sexy/casual allow contractions. "
                         "omit to keep the strict no-apostrophe rule")
    a = ap.parse_args()
    allow_apo = a.register in ("sexy", "casual")

    batch = json.load(open(a.path, encoding="utf-8"))
    if isinstance(batch, dict):
        batch = batch.get("rows") or [batch]
    rows = [norm_turns(r) for r in batch]
    n = len(rows)
    print(f"batch: {a.path}\nrows : {n}")

    # ---- BAND + HYGIENE -----------------------------------------------------
    band_bad, hy = [], []
    apo = []
    for i, turns in enumerate(rows, 1):
        for j, (role, txt) in enumerate(turns):
            # HYGIENE runs on EVERY turn, not just the assistant's: a hyphen in a
            # user turn is the same defect (caught 2026-10-18 by the lead's verify
            # on b4135 row 11, "drive-in", while this gate reported hyg=0).
            if not txt.isascii():
                hy.append((i, j, "nonascii", txt))
            if any(c in txt for c in "\u2013\u2014\u2015\u2012"):
                hy.append((i, j, "dash", txt))
            if "-" in txt:
                hy.append((i, j, "hyphen", txt))
            if "'" in txt:
                apo.append((i, j, txt))
                if not allow_apo:
                    hy.append((i, j, "apostrophe", txt))
            if role != "assistant":
                continue
            w = len(words(txt))
            if not (10 <= w <= 13):
                band_bad.append((i, j, w, txt))
    print(f"\n[BAND]   assistant replies off 10-13: {len(band_bad)}")
    for i, j, w, t in band_bad[:40]:
        print(f"    row {i} a{j}  {w}w  {t!r}")
    print(f"[HYGIENE] non-ascii/dash/hyphen/apostrophe: {len(hy)}")
    for it in hy[:20]:
        print("   ", it)
    print(f"[APOSTROPHE] register={a.register or 'strict'} "
          f"allowed={'yes' if allow_apo else 'no'} carriers={len(apo)}")
    for i, j, t in apo[:15]:
        print(f"    row {i} a{j}  {t!r}")

    # ---- US SPELLING (every turn) ------------------------------------------
    spell = []
    for i, turns in enumerate(rows, 1):
        for j, (role, txt) in enumerate(turns):
            for m in BRIT_RE.finditer(txt.lower()):
                spell.append((i, j, role, m.group(0), txt))
            for m in CUPBOARD_RE.finditer(txt.lower()):
                spell.append((i, j, role, m.group(0) + " (british collocation)", txt))
    print(f"\n[SPELL]  british stems (US English only): {len(spell)}")
    for i, j, role, w, t in spell[:20]:
        print(f"    row {i} {role[0]}{j}  {w!r}  {t!r}")

    # ---- ECHO (house cw; the anchor must be a NON-TRIVIAL shared token) ------
    zeros, weak = [], []
    for i, turns in enumerate(rows, 1):
        for j in range(0, len(turns) - 1, 2):
            u, a2 = turns[j], turns[j + 1]
            if u[0] != "user" or a2[0] != "assistant":
                continue
            shared = cw(u[1]) & cw(a2[1])
            if not shared:
                zeros.append((i, u[1], a2[1]))
            elif not (shared - ECHO_TRIVIAL):
                weak.append((i, sorted(shared), u[1], a2[1]))
    print(f"\n[ECHO]   zero-content pairs: {len(zeros)}")
    for i, u, a2 in zeros[:20]:
        print(f"    row {i}  U={u!r}  A={a2!r}")
    print(f"[ECHO]   weak (shared anchor is trivial-only): {len(weak)}")
    for i, sh, u, a2 in weak[:20]:
        print(f"    row {i}  shared={sh}  U={u!r}  A={a2!r}")

    # ---- OPENERS ------------------------------------------------------------
    u1 = collections.Counter(fw(t[0][1]) for t in rows if t and t[0][0] == "user")
    a1 = collections.Counter(fw(t[1][1]) for t in rows if len(t) > 1 and t[1][0] == "assistant")
    # house gate reads `max >= 18` as a FAIL, so 18 itself fails (#235). Every landed
    # batch was held to that reading, so this must match verbatim -- not `> cap`.
    over30 = {w: k for w, k in u1.items() if k >= a.u1cap}
    did_open = a1.get("did", 0)
    print(f"\n[OPENERS] user turn-1 (cap: FAILS at >= {a.u1cap} of {n})  OVER={over30}")
    for w, k in u1.most_common(8):
        print(f"    {w:<12} {k:>3}  {100 * k / n:5.1f}%")
    print(f"[OPENERS] assistant turn-1 (want flat ~13%); 'did' openers = {did_open} (cap 6)")
    for w, k in a1.most_common(8):
        print(f"    {w:<12} {k:>3}  {100 * k / n:5.1f}%")

    # ---- WATCHLIST + FRAMES + SLOP -----------------------------------------
    watch = collections.Counter()
    frame_hits, verdict_hits, isframe_hits = [], [], []
    a_real = 0
    always_n = 0
    whole_n = 0
    the_whole_n = 0
    for i, turns in enumerate(rows, 1):
        for j, (role, txt) in enumerate(turns):
            low = txt.lower()
            # lead #218 / house gate: the always + whole caps apply to EVERY turn,
            # not assistant-only. Counting assistant turns alone under-reported
            # b4430 as always=2 when the house gate saw 5.
            always_n += len(re.findall(r"\balways\b", low))   # lead msg #116: cap 4 per batch
            whole_n += len(re.findall(r"\bwhole\b", low))       # cap 4 per batch
            the_whole_n += len(re.findall(r"\bthe whole\b", low))  # cap 2 per batch
            if role != "assistant":
                continue
            for name, rx in WATCH_RE:
                if rx.search(low):
                    watch[name] += 1
            for name, rx in FRAME_RE:
                if rx.search(low):
                    frame_hits.append((i, j, name, txt))
            m = VERDICT_RE.search(low)
            if m:
                verdict_hits.append((i, j, m.group(0), txt))
            if IS_FRAME_RE.search(txt) or INIT_COPULA_RE.search(txt):
                isframe_hits.append((i, j, txt))
            a_real += len(re.findall(r"\ba real\b", low))   # word boundary: "umbrella really" is not a hit
            # lead msg #120: 'whole' as an intensifier is the same frame-repetition
            # shape that became the 'a good' attractor in r39 (b3905 carried 15).
            # (always / whole / the whole are counted above, across ALL turns)
    print(f"\n[WATCHLIST] {dict(watch)}  (all must be 0)")
    print(f"[FRAMES]    KNOWN_FRAMES hits: {len(frame_hits)}")
    for it in frame_hits[:15]:
        print("   ", it)
    print(f"[SLOP]      verdict nouns: {len(verdict_hits)}")
    for it in verdict_hits[:15]:
        print("   ", it)
    print(f"[SLOP]      is-frame copulas: {len(isframe_hits)}")
    for it in isframe_hits[:20]:
        print("   ", it)
    print(f"[SLOP]      'a real'={a_real}")
    print(f"[SLOP]      'always'={always_n} (cap 4)")
    print(f"[SLOP]      'whole'={whole_n} (cap 4)  'the whole'={the_whole_n} (cap 2)")

    # ---- 5-grams: within batch AND vs live corpus ---------------------------
    # ALL-TURNS is the failing count, because that is what the lead's referee
    # counts (tmp_verify: batch5 over every turn). This screen used to be
    # ASSISTANT-only on the theory that only a reply repeating a reply is the
    # defect -- and a unit test proved the cost: a user turn and an assistant
    # turn sharing one 5-gram reads 0 here and 3 at the referee. A CLEAN that
    # is weaker than the gate it is standing in for is worse than no CLEAN.
    # The assistant-only count stays as the sharper secondary signal.
    seen = collections.defaultdict(list)      # every turn  (matches referee)
    seen_a = collections.defaultdict(list)    # assistant only (sharper)
    intra = []
    for i, turns in enumerate(rows, 1):
        for j, (role, txt) in enumerate(turns):
            gl = grams(txt, 5)               # list, keeps intra-turn repeats
            for g in set(gl):
                seen[g].append((i, j))
                if role == "assistant":
                    seen_a[g].append((i, j))
            for g, c in collections.Counter(gl).items():
                if c > 1:
                    intra.append((i, j, role, g, c))
    rep = {g: v for g, v in seen.items() if len(v) > 1}
    rep_a = {g: v for g, v in seen_a.items() if len(v) > 1}
    print(f"\n[5GRAMS]  repeated within batch (ALL turns, referee scope): {len(rep)}")
    for g, v in sorted(rep.items(), key=lambda kv: -len(kv[1]))[:15]:
        print(f"    {len(v)}x  {g}  {v}")
    print(f"[5GRAMS]  of those, assistant-only: {len(rep_a)}")
    print(f"[5GRAMS]  repeated INSIDE one turn (set-based counters miss these): {len(intra)}")
    for i, j, role, g, c in intra[:10]:
        print(f"    {c}x  row {i} {role[0]}{j}  {g}")

    live_hits = []
    x5g = []
    if a.live:
        ref = collections.Counter()      # every corpus turn (matches the referee)
        ref_a = collections.Counter()    # assistant turns only (the sharper signal)
        root = r"C:\github\DBllm\runs\synth2"
        if a.live == "ALL":
            files = sorted(glob.glob(os.path.join(a.raw, "*.jsonl")))
        else:
            p = a.live if os.path.isabs(a.live) else os.path.join(root, a.live)
            files = [p]
        for f in files:
            for line in open(f, encoding="utf-8"):
                if not line.strip():
                    continue
                for t in json.loads(line).get("turns", []):
                    g5 = set(grams(t["text"], 5))
                    ref.update(g5)
                    if t["role"] == "assistant":
                        ref_a.update(g5)
        # The index used to be ASSISTANT-ONLY, which made this screen blind to a
        # reply mirroring a corpus USER turn: b4175 row 60 shipped 'not a word
        # until the' (a user line) with x5g=0 here and the lead's verify red. The
        # referee indexes every turn, so this does too. ref_a stays as a secondary
        # count so the sharper assistant-only signal is not lost.
        for i, turns in enumerate(rows, 1):
            for j, (role, txt) in enumerate(turns):
                for g in set(grams(txt, 5)):
                    if ref[g] >= 3:
                        live_hits.append((i, j, g, ref[g], role[0]))
        print(f"[5GRAMS]  batch 5-grams already >=3x in corpus: {len(live_hits)}")
        for i, j, g, c, rl in sorted(live_hits, key=lambda x: -x[3])[:20]:
            print(f"    corpus {c}x  row {i} {rl}{j}  {g!r}")

        # ---- X5G: a 5-gram shared with even ONE live row (lead msg #124) -----
        # b3920 shipped 3 of these at 1x (e.g. 'promised a refund and then just'
        # mirrored b3905 row 23). The >=3x screen is blind to a single mirror,
        # but one verbatim cross-batch frame IS the failure mode we watch for.
        x5g = []
        for i, turns in enumerate(rows, 1):
            for j, (role, txt) in enumerate(turns):
                for g in sorted(set(grams(txt, 5))):
                    if ref[g] >= 1:
                        x5g.append((i, j, g, ref[g], role[0]))
        print(f"[X5G]     batch 5-grams mirrored by ANY live row (1x): {len(x5g)}")
        for i, j, g, c, rl in sorted(x5g, key=lambda x: -x[3])[:20]:
            print(f"    corpus {c}x  row {i} {rl}{j}  {g!r}")
        asst_only = sum(1 for i, j, g, c, rl in x5g if ref_a[g] >= 1)
        print(f"[X5G]     of those, mirrored by an ASSISTANT turn: {asst_only}")

    # ---- PARROT: a reply echoing its OWN user turn verbatim (6+ grams) ------
    parrots = []
    for i, turns in enumerate(rows, 1):
        us = [t for r_, t in turns if r_ == "user"]
        for j, (role, txt) in enumerate(turns):
            if role != "assistant":
                continue
            for u in us:
                for n in (8, 7, 6):
                    sh = set(grams(txt, n)) & set(grams(u, n))
                    if sh:
                        parrots.append((i, j, n, sorted(sh)[0]))
                        break
    print(f"[PARROT]  replies echoing their own user turn at 6+ grams: {len(parrots)}")
    for it in parrots[:15]:
        print("   ", it)

    # ---- CAPITALS: the corpus is all-lowercase in EVERY turn ----------------
    caps = []
    for i, turns in enumerate(rows, 1):
        for j, (role, txt) in enumerate(turns):
            if re.search(r"[A-Z]", txt):
                caps.append((i, j, role, txt))
    print(f"[CAPS]    turns carrying a capital letter: {len(caps)}")
    for it in caps[:15]:
        print("   ", it)

    # ---- PROBE overlap ------------------------------------------------------
    print(f"\n[PROBE]   turns sharing a non-generic word with a prompt (topic drift):")
    hits = 0
    for i, turns in enumerate(rows, 1):
        rowtext = " ".join(t for _r, t in turns).lower()
        for w in VERIFY_STRONG:
            if re.search(r"\b" + w + r"\b", rowtext):
                hits += 1
                print(f"    row {i} STRONG probe word {w!r}")
        for j, (role, txt) in enumerate(turns):
            s = vcontent(txt)
            for p, ps in PROBE_VC:
                sh = (s & ps)
                # house rule (#233): two or more shared CONTENT words, where content
                # is tokens minus VERIFY_STOP. Particles and time words (out, off,
                # until, again, up, down, before, after) are STOP, so came/out or
                # turned/off is ONE shared word and passes. two/last is TWO and fails.
                if len(sh) >= 2:
                    hits += 1
                    print(f"    row {i} {role[:4]}{j}  {sorted(sh)}  <- {p!r}")
    if not hits:
        print("    none")

    # ---- SCENARIO CENSUS (report only, never fails) -------------------------
    # Lead msg #169: the method is DEPTH FIRST -- new beats on a covered scenario
    # are the preferred work, and the near-dup gates are the referee. So this
    # section judges nothing. It shows each row scenario neighbourhood so a manual
    # census cannot miss the heavy hitters (b3965, b3980), which mine did.
    # Hook = the RAREST content word the row shares with the live lane, ignoring
    # very common words (they name a topic, not a scene) and very short ones.
    if a.live:
        scen_live = []
        for f in files:
            for line in open(f, encoding="utf-8"):
                if not line.strip():
                    continue
                rec = json.loads(line)
                for t in rec.get("turns", []):
                    if t["role"] == "user":
                        scen_live.append((rec.get("batch_no"), t["text"],
                                          cw(t["text"])))
        scen_freq = collections.Counter()
        for _, _, sc_ws in scen_live:
            scen_freq.update(sc_ws)
        print("\n[SCEN]    scenario census (report only; depth-first is allowed):")
        scen_cov = []
        for i, turns in enumerate(rows, 1):
            sc_ws = cw(turns[0][1])
            scen_cand = [(scen_freq[x], x) for x in sc_ws
                         if 2 <= scen_freq[x] <= 20 and len(x) >= 5]
            if not scen_cand:
                print(f"    row {i:2d}  NEW          no content word shared with the lane")
                scen_cov.append((0, i, "new"))
                continue
            sc_n, sc_w = min(scen_cand)
            scen_hits = [(b, t) for b, t, lws in scen_live if sc_w in lws]
            scen_bs = sorted({b for b, _ in scen_hits if b is not None})
            scen_cov.append((len(scen_bs), i, sc_w))
            print(f"    row {i:2d}  {sc_w:<12s} {len(scen_bs):2d} batches /"
                  f" {len(scen_hits):3d} turns  {scen_bs[:6]}")
            if len(scen_hits) >= 4:
                print(f"              e.g. {scen_hits[0][1][:78]}")
        scen_cov.sort(reverse=True)
        print("    -- heaviest neighbourhoods: " + ", ".join(
            f"row {i}={x}({c})" for c, i, x in scen_cov[:5]))

    # ---- QUESTION SHARE (lead msg #109: count raw ? endings; band 33-38 of 67) --
    replies = [(i, j, txt) for i, turns in enumerate(rows, 1)
               for j, (role, txt) in enumerate(turns) if role == "assistant"]
    qn = sum(1 for _, _, t in replies if t.rstrip().endswith("?"))
    nrep = len(replies)
    q_ok = (a.qmin <= qn <= a.qmax) if nrep == 67 else (a.qmin <= qn <= a.qmax) if a.qset else True
    print(f"\n[QUESTIONS] replies ending with '?' = {qn} of {nrep} "
          f"({'in band %d-%d' % (a.qmin, a.qmax) if q_ok else 'OUT OF BAND %d-%d' % (a.qmin, a.qmax)})")

    # ---- verdict ------------------------------------------------------------
    watch_tot = sum(watch.values())
    print("\n==== STAGECHECK ====")
    print(f"band={len(band_bad)} hyg={len(hy)} spell={len(spell)} echo0={len(zeros)} weak={len(weak)} "
          f"over30={len(over30)} did={did_open} watch={watch_tot} frames={len(frame_hits)} "
          f"verdict={len(verdict_hits)} isframe={len(isframe_hits)} "
          f"5g={len(rep)} 5g_live={len(live_hits)} x5g={len(x5g)} parrot={len(parrots)} caps={len(caps)} probe={hits} a_real={a_real} "
          f"always={always_n} whole={whole_n}/{the_whole_n} q={qn}/{nrep}")
    clean = (not band_bad and not hy and not spell and not zeros and not weak and not over30
             and did_open <= a.didcap and watch_tot == 0 and not frame_hits
             and not verdict_hits and not isframe_hits and not rep and not intra
             and not live_hits
             and not x5g and not parrots and not caps
             and not hits and not a_real and always_n <= a.alwayscap
             and whole_n <= a.wholecap and the_whole_n <= a.thewcap and q_ok)
    print("VERDICT:", "CLEAN" if clean else "REVIEW -- see flagged sections above")
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
