import json, os, re, sys, glob, itertools
from collections import Counter

ROOT = r"C:\github\DBllm"
BATCH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "tmp_b4970.txt")
RAW = os.path.join(ROOT, "runs", "synth2", "raw")

STOP = set("""a an the i you he she it we they me him her us them my your his its our their
this that these those is are was were be been being am do does did have has had will would
can could should shall may might must of in on at to for with from by about as into and or
but so if then than too very just not no yes up down out off over under again once here
there when where why how what which who whom whose before after until while during because
through between against above below both each few more most other some such only own same
all any every little much now ever never still even also""".split())

STRONG = ["weekend", "morning", "phone", "weather", "traffic", "parking", "spot", "job", "apartment", "snow", "rain", "inbox", "parcels", "bus", "driver", "commute", "groceries", "haircut", "toast", "lamp", "dance", "drink", "heart", "review", "agenda", "message", "tv", "bored", "sneezed", "forgot", "test", "project", "bucks", "march", "winter", "dark", "summer", "today", "store", "car"]
BANNED = ["robbery", "theft", "scam", "bait", "nightmare", "stings", "rough", "brutal", "timing", "bold", "classic", "dirty", "sneaky", "underhanded"]
WATCH = ["were you able to", "have you tried", "did you get", "is just", "a real",
         "counts as", "ten minutes of", "minutes of", "the one", "never stood a chance",
         "the gift shop", "on the first try", "are you going to", "an early night",
         "at this point", "the front desk", "the post office", "did they say",
         "did they really", "i have been", "falling asleep", "ice cream", "did you find",
         "a couple of", "two hours of", "have you got", "was it worth the",
         "shall i add", "i will bring", "the office manager"]

IS_FRAME_RE = re.compile(r"(?:^|[.?!]\s+)(?:the|a|an)\s+[^.?!]{2,40}?\s(?:is|are)\s+(?:a|an|the)\s", re.I)
KNOWN_FRAMES = [
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
FRAME_RE = [(n, re.compile(p)) for n, p in KNOWN_FRAMES]

BRIT_STEMS = ["neighbour", "colour", "favour", "honour", "humour", "rumour", "labour", "endeavour",
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
    "satnav", "roadworks", "waistcoat", "promenade", "stallholder", "motorway", "car boot",
    "queue", "canteen", "cupboard", "plasters", "trousers", "fortnight"]
BRIT_RE = re.compile(r"\b(?:" + "|".join(BRIT_STEMS) + r")\w*|\bappal(?!l|led|ling)\w*|\benthral(?!l|led|ling)\w*")

GERUND_NOUNS = {"nothing", "something", "everything", "anything", "thing", "things", "morning", "wedding", "during", "ring", "king", "ceiling", "evening"}
DETS = {"the", "a", "an", "that", "this", "these", "those", "our", "your", "my", "their", "his", "her", "its", "one", "some", "every", "each", "another", "both"}

PROMPTS = [
    "so what is going on with you this weekend?",
    "it rained the whole way in today.",
    "i still need to get groceries before the store closes.",
    "i could not fall asleep until like two last night.",
    "you up to anything today?",
    "the weekend came and went so fast.",
    "my order came cold and half missing.",
    "someone took my parking spot again.",
    "you have that look in your eyes tonight.",
    "save me a dance later, will you?",
    "lovely weather we are having this week.",
    "how was your commute in this morning?",
    "oh great, another meeting invite.",
    "my inbox has two hundred unread emails.",
    "guess what, i got the job!",
    "we are going away this weekend!",
    "dark by four again, winter is here.",
    "nothing good on tv ever anymore.",
    "my heart has been racing since three am.",
    "the review invite has no agenda attached.",
    "did you hear about apartment nine upstairs?",
    "word is the promotion is already decided.",
    "remember the candy store lines at recess?",
    "summers felt longer back then, right?",
    "do you ever wonder why time speeds up as you get older?",
    "what do you think actually matters in the end?",
    "nice haircut, did you do it yourself?",
    "you have been on that phone all day, haven't you?",
    "i am having a really rough week.",
    "i did not get the job, i am crushed.",
    "i am so bored i have cleaned the whole apartment.",
    "there is nothing to do tonight.",
    "what did you end up doing about the car?",
    "how did you two actually meet?",
    "did you ever send that message?",
    "so, about that thing we talked about.",
    "my bus was late again and then the driver just sat there.",
    "three parcels lost this month, three.",
    "you are trouble, you know that?",
    "buy me a drink and i might forgive you.",
    "fine.",
    "whatever, it does not matter.",
    "we finally finished the project!",
    "i passed my driving test first time!",
    "wait, so who is actually in charge?",
    "sorry, i do not follow, say that again?",
    "she still owes me twenty bucks from march.",
    "i am not inviting him, not after last time.",
    "i just sneezed and my lamp turned off, that is not normal.",
    "my toast came out shaped like a face.",
    "morning! how are you?",
    "hey, long time no see!",
    "no idea, honestly.",
    "i have no clue, sorry.",
    "thanks so much for the other day.",
    "that was really kind of you, thank you.",
    "sorry i am late, the traffic was awful.",
    "my bad, i completely forgot.",
    "right, i am off, see you later!",
    "anyway, i should go, take care!",
]

def toks(s):
    return re.findall(r"[a-z0-9']+", s.lower())

def content(s):
    return [t for t in toks(s) if t not in STOP]

def shingles(s, n=3):
    t = toks(s)
    return set(tuple(t[i:i+n]) for i in range(len(t)-n+1))

def ngrams(s, n):
    t = toks(s)
    return set(tuple(t[i:i+n]) for i in range(len(t)-n+1))

def stem(t):
    for suf in ("ing", "ed", "s", "es"):
        if t.endswith(suf) and len(t) > len(suf) + 2:
            return t[: -len(suf)]
    return t

errors = []
warns = []

lines = [l.strip() for l in open(BATCH, encoding="ascii").read().splitlines() if l.strip()]
rows = []
for i, l in enumerate(lines, 1):
    turns = [t.strip() for t in l.split("|")]
    if len(turns) not in (2, 4):
        errors.append(f"row {i}: {len(turns)} turns (expected 2 or 4)")
    rows.append(turns)

two = [r for r in rows if len(r) == 2]
four = [r for r in rows if len(r) == 4]
replies = [r[j] for r in rows for j in range(1, len(r), 2)]
print(f"rows={len(rows)} two_turn={len(two)} four_turn={len(four)} replies={len(replies)}")
if len(rows) != 25: errors.append(f"row count {len(rows)} != 25")
if len(two) != 23: errors.append(f"two-turn {len(two)} != 23")
if len(four) != 2: errors.append(f"four-turn {len(four)} != 2")
if len(replies) != 27: errors.append(f"replies {len(replies)} != 27")

qcount = 0
did_open = 0
always_n = ofcourse_n = thewhole_n = whole_n = means_n = 0
should_q = 0
did_q = 0
two_part = 0
ger_np = 0
opener_first = {}
for ri, r in enumerate(rows, 1):
    for j, t in enumerate(r):
        if re.search(r"[A-Z]", t): errors.append(f"row {ri} turn {j}: capital letter: {t!r}")
        if any(ord(c) > 127 for c in t): errors.append(f"row {ri} turn {j}: non-ascii")
        if "-" in t: errors.append(f"row {ri} turn {j}: dash: {t!r}")
        if "'" in t: errors.append(f"row {ri} turn {j}: apostrophe: {t!r}")
    w0 = toks(r[0])[0]
    opener_first[w0] = opener_first.get(w0, 0) + 1
    for j in range(1, len(r), 2):
        rep = r[j]
        n = len(toks(rep))
        if not (10 <= n <= 13): errors.append(f"row {ri} reply {j//2}: {n} words: {rep!r}")
        if rep.endswith("?"):
            qcount += 1
            qclause = rep.rsplit(",", 1)[-1].strip()
            qc0 = toks(qclause)[0]
            if qc0 == "should": should_q += 1
            if qc0 == "did": did_q += 1
            if "," in rep: two_part += 1
        if toks(rep)[0] == "did": did_open += 1
        if re.match(r"^(is|are|was|were)\b", rep): errors.append(f"row {ri} reply {j//2}: sentence-initial is-frame: {rep!r}")
        if IS_FRAME_RE.search(rep): errors.append(f"row {ri} reply {j//2}: is-frame copula: {rep!r}")
        for fn, fx in FRAME_RE:
            if fx.search(rep): errors.append(f"row {ri} reply {j//2}: KNOWN_FRAME {fn}: {rep!r}")
        uc = set(content(r[j-1]))
        rc = set(content(rep))
        exact = uc & rc
        if not exact:
            stems = {stem(x) for x in uc} & {stem(x) for x in rc}
            tag = "INFLECTION-ONLY" if stems else "NO ECHO"
            errors.append(f"row {ri} reply {j//2}: {tag} overlap: user={sorted(uc)} reply={sorted(rc)}")
        if ngrams(rep, 6) & ngrams(r[j-1], 6):
            errors.append(f"row {ri} reply {j//2}: verbatim 6-gram parrot: {rep!r}")
        rt = toks(rep)
        f = rt[0]
        if f.endswith("ing") and f not in GERUND_NOUNS:
            if {stem(f)} & {stem(x) for x in toks(r[j-1])}:
                ger_np += 1
        elif f in DETS:
            head = set(content(" ".join(rt[:5])))
            if head & uc:
                ger_np += 1
    rowtext = " ".join(r).lower()
    for w in WATCH:
        if w in rowtext: errors.append(f"row {ri}: watchlist phrase {w!r}")
    if re.search(r"at all\b", rowtext): errors.append(f"row {ri}: 'at all'")
    for b in BANNED:
        if re.search(r"\b" + b + r"\b", rowtext): errors.append(f"row {ri}: banned noun {b!r}")
    for m in BRIT_RE.finditer(rowtext):
        errors.append(f"row {ri}: british spelling {m.group(0)!r}")
    for w in STRONG:
        if re.search(r"\b" + w + r"\b", rowtext): errors.append(f"row {ri}: STRONG probe word {w!r}")
    always_n += rowtext.count("always")
    ofcourse_n += rowtext.count("of course")
    thewhole_n += rowtext.count("the whole")
    whole_n += len(re.findall(r"\bwhole\b", rowtext))
    means_n += len(re.findall(r"\bmeans\b", rowtext))

print(f"qmark_ending={qcount} did_openers={did_open} always={always_n} of_course={ofcourse_n} the_whole={thewhole_n} whole={whole_n} means={means_n}")
print(f"R5: should_questions={should_q} did_questions={did_q} two_part_mold={two_part} ger_np_openers={ger_np}")
if not (13 <= qcount <= 15): errors.append(f"qmark ending count {qcount} outside 13-15")
if did_open > 2: errors.append(f"did openers {did_open} > 2")
if always_n > 2: errors.append(f"always {always_n} > 2")
if ofcourse_n > 1: errors.append(f"of course {ofcourse_n} > 1")
if thewhole_n > 1: errors.append(f"the whole {thewhole_n} > 1")
if whole_n > 2: errors.append(f"whole {whole_n} > 2")
if means_n >= 3: errors.append(f"means frames {means_n} >= 3")
if should_q > 2: errors.append(f"R5 should-questions {should_q} > 2")
if did_q > max(1, int(0.20 * qcount)): errors.append(f"did-questions {did_q} > 20 pct of {qcount} (the did-watch cap)")
if two_part > 16: errors.append(f"R5 two-part mold {two_part} > 16")
if ger_np > 14: errors.append(f"R5 ger+np openers {ger_np} > 14")
mx = max(opener_first.items(), key=lambda kv: kv[1])
print(f"user opener first words: {sorted(opener_first.items(), key=lambda kv: -kv[1])}")
if mx[1] >= 7: errors.append(f"opener '{mx[0]}' x{mx[1]} >= 7")

for ri, r in enumerate(rows, 1):
    for j, t in enumerate(r):
        tc = set(content(t))
        for pi, p in enumerate(PROMPTS):
            shared = tc & set(content(p))
            if len(shared) >= 2:
                errors.append(f"row {ri} turn {j}: probe overlap {sorted(shared)} with prompt {pi}: {p!r}")

batch5 = Counter()
for ri, r in enumerate(rows, 1):
    for j, t in enumerate(r):
        for g in ngrams(t, 5):
            batch5[g] += 1
rep5 = [g for g, c in batch5.items() if c > 1]
if rep5:
    errors.append(f"within-batch repeated 5-grams: {len(rep5)}")
    for g in rep5[:10]: errors.append(f"  repeated 5-gram: {' '.join(g)}")

corpus_ngrams = set()
corpus_types = set()
corpus_lines = 0
for f in glob.glob(os.path.join(RAW, "*.jsonl")):
    data = open(f, "rb").read().decode("utf-8")
    for l in data.splitlines():
        if not l.strip(): continue
        corpus_lines += 1
        obj = json.loads(l)
        for t in obj["turns"]:
            corpus_ngrams |= ngrams(t["text"], 5)
            corpus_types |= set(content(t["text"]))
print(f"corpus lines={corpus_lines} corpus 5-grams={len(corpus_ngrams)} corpus content types={len(corpus_types)}")

batch_types = Counter()
for r in rows:
    for t in r:
        for w in content(t):
            batch_types[w] += 1
rare = sorted(w for w in batch_types if w not in corpus_types)
rare_tok = sum(batch_types[w] for w in rare)
tot_types = len(batch_types)
tot_tok = sum(batch_types.values())
print(f"RARE-TYPE report: {len(rare)}/{tot_types} types ({100*len(rare)/max(1,tot_types):.1f} pct), {rare_tok}/{tot_tok} content tokens ({100*rare_tok/max(1,tot_tok):.1f} pct)")
print("  rare types:", " ".join(rare))
for ri, r in enumerate(rows, 1):
    for j, t in enumerate(r):
        hit = ngrams(t, 5) & corpus_ngrams
        if hit:
            errors.append(f"row {ri} turn {j}: corpus 5-gram collision {sorted(hit)}: {t!r}")

reps = [(ri, j, r[j]) for ri, r in enumerate(rows, 1) for j in range(1, len(r), 2)]
for (r1, j1, t1), (r2, j2, t2) in itertools.combinations(reps, 2):
    s1, s2 = shingles(t1), shingles(t2)
    if not s1 or not s2: continue
    jac = len(s1 & s2) / len(s1 | s2)
    if jac > 0.40:
        errors.append(f"near-dup rows {r1}/{r2} replies: jaccard {jac:.2f}: {t1!r} vs {t2!r}")

print()
if warns:
    print("WARNINGS:")
    for w in warns: print("  " + w)
if errors:
    print(f"DEFECTS ({len(errors)}):")
    for e in errors: print("  " + e)
    sys.exit(1)
print("ALL GREEN")
