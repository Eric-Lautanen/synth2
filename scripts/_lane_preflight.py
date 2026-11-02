#!/usr/bin/env python3
"""_lane_preflight.py <changes.json> <batch_no> [corpus]
Validates a conditioning-lane change-set against the LIVE corpus BEFORE apply:
  * 10-13 words, ASCII, no dash/hyphen, no emoji, index in range
  * near-dup gate (3-shingle Jaccard < 0.60) with edits applied IN MEMORY
  * simulated conditioning for the batch (zero share) + lists any residual zero
  * qmark classifier (real fix_line)
Read-only."""
import json, re, sys, math, importlib.util, os

STOP = set("""a an the and or but if then than so as of to in on at for with from by about into over after
is are was were be been being am do does did doing have has had having i you he she it we they me him her them
my your his its our their this that these those there here what which who whom when where why how not no nor
too very can will just should now would could oh ok okay yeah hey hi uh um well really much more most
get got go going went gone do done make made""".split())
GRAMMAR = {"tools","memory","distillation","injection_resist","self_direction","succession",
           "stream","emotion","identity","injection"}
MIN_DIST = 0.60

def cw(t): return set(w for w in re.findall(r"[a-z']+", t.lower()) if w not in STOP and len(w) > 1)

def load_lines(p):
    return [l for l in open(p, "rb").read().split(b"\r\n") if l.strip()]

def convo(row): return " ".join(t["text"] for t in row["turns"] if t["text"])

def shingles(text):
    ws = text.split()
    if len(ws) < 3: return set(ws)
    return set(" ".join(ws[i:i+3]) for i in range(len(ws)-2))

def bound(k): return max(0, math.ceil(k / (1.0 - MIN_DIST)) - 1)

def main():
    ch_path, batch = sys.argv[1], int(sys.argv[2])
    corpus = sys.argv[3] if len(sys.argv) > 3 else "raw/small_talk_casual.jsonl"
    lines = load_lines(corpus)
    rows = [json.loads(l) for l in lines]
    ch = json.load(open(ch_path, encoding="utf-8"))

    # ---- structural validation + apply in memory ----
    issues = []; n = 0
    for key, c in ch.items():
        ln = int(key)
        if ln < 1 or ln > len(rows): issues.append((key, "line-oob")); continue
        row = rows[ln-1]
        asst = [t for t in row["turns"] if t["role"] == "assistant"]
        for idx, txt in c.items():
            i = int(idx); n += 1
            w = len(txt.split())
            if not (10 <= w <= 13): issues.append((key, idx, "wordcount", w, txt))
            if any(ord(x) > 127 for x in txt): issues.append((key, idx, "nonascii", txt))
            if any(d in txt for d in ["\u2013","\u2014","\u2012","\u2015"]): issues.append((key, idx, "dash", txt))
            if "-" in txt: issues.append((key, idx, "hyphen", txt))
            if any(0x2600 <= ord(x) <= 0x1FAFF for x in txt): issues.append((key, idx, "emoji", txt))
            if i >= len(asst): issues.append((key, idx, "index-oob", len(asst)))
    print(f"[structure] replies={n} issues={len(issues)}")
    for it in issues[:30]: print("   ", it)

    # apply
    for key, c in ch.items():
        row = rows[int(key)-1]; k = 0
        for t in row["turns"]:
            if t["role"] == "assistant":
                if str(k) in c: t["text"] = c[str(k)]
                k += 1

    # ---- near-dup (grammar exempt) ----
    idxs = [i for i, r in enumerate(rows)
            if r.get("category", {}).get("interaction_type", "") not in GRAMMAR]
    sets = [shingles(convo(rows[i])) for i in idxs]
    sizes = [len(s) for s in sets]
    pairs = 0
    for a in range(len(idxs)):
        for b in range(a):
            sa, sb = sizes[a], sizes[b]
            if max(sa, sb) > bound(min(sa, sb)): continue
            A, B = sets[a], sets[b]
            d = 0.0 if (not A and not B) else 1.0 - len(A & B)/len(A | B)
            if d < MIN_DIST: pairs += 1
    print(f"[near-dup] pairs(dist<{MIN_DIST}) = {pairs}")

    # ---- simulated conditioning for the batch ----
    n2 = z = 0; ov = 0; resid = []
    for r in rows:
        if r["batch_no"] != batch: continue
        ts = r["turns"]
        for i in range(0, len(ts)-1, 2):
            u, a = ts[i], ts[i+1]
            if u["role"] != "user" or a["role"] != "assistant": continue
            o = cw(u["text"]) & cw(a["text"]); n2 += 1; ov += len(o)
            if not o:
                z += 1
                resid.append((u["text"], a["text"], sorted(cw(u["text"]))))
    print(f"[conditioning b{batch}] n={n2} zero={z/n2*100:.1f}% mean_ov={ov/n2:.2f}")
    for u, a, uc in resid[:12]:
        print(f"    ZERO  U={u!r}  Uc={uc}  A={a!r}")

    # ---- qmark ----
    spec = importlib.util.spec_from_file_location("qmark", "scripts/qmark.py")
    qm = importlib.util.module_from_spec(spec); spec.loader.exec_module(qm)
    flagged = 0
    for key, c in ch.items():
        r = json.loads(lines[int(key)-1]); k = 0
        for t in r["turns"]:
            if t["role"] == "assistant":
                if str(k) in c: t["text"] = c[str(k)]
                k += 1
        _, m = qm.fix_line(json.dumps(r, ensure_ascii=True))
        if m: flagged += 1
    print(f"[qmark] flagged rows = {flagged}")

if __name__ == "__main__":
    main()
