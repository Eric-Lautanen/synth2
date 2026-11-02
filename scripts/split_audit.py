#!/usr/bin/env python3
"""synth2 SPLIT AUDIT (D3) -- the packed split the TRAINER reads.

WHY THIS EXISTS. `integrity.py` audits `raw/*.jsonl` -- the SOURCE. This audits
`train.ids` / `train.mask` -- the ARTIFACT, the bytes `load_split` hands the
model. Those are different objects, and the standing law in this campaign is
that a claim about the source is not a claim about the consumer. Two questions
this closes:

1. "REPETITION IN, REPETITION OUT." If the packed split itself repeats turns or
   n-grams, the model is being trained to repeat and the degeneration is partly
   a corpus property, not a circuit property. This measures it on the packed
   split, where it actually matters.
2. MASK ALIGNMENT. The loss is computed only where mask==1. If the mask is
   misaligned by even one token, the model is trained to predict the wrong
   thing and every downstream instrument reads a corrupted number.

THE LAYOUT, read off the live file (not assumed):

    BOS0 <user>0 SEP0 <assistant>1 SEP0 <user>0 SEP0 <assistant>1 EOS1

i.e. mask 0 on BOS, on every user turn, and on EVERY SEP; mask 1 on every
assistant turn and on the trailing EOS. Turn count is even (SEP count is odd).
The checks below assert exactly this and name the example + offset on failure.

Usage:
  python runs/synth2/scripts/split_audit.py [--data runs/synth2]
                                           [--split train,heldout] [--top 15]
                                           [--out PATH]

Exit status is non-zero when a structural invariant fails, so this can be wired
into a gate. The repetition numbers are a FINDER, never a verdict -- a repeated
turn may be legitimate (a register that says "fine." twice) and is HAND-READ.
"""
import argparse
import collections
import json
import os
import sys

BOS, EOS, SEP = 1, 2, 3
REPO = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def _bytes_to_unicode():
    """GPT-2 byte-level alphabet, mirrored from the `tokenizers` library."""
    bs = (list(range(ord("!"), ord("~") + 1))
          + list(range(ord("\u00a1"), ord("\u00ac") + 1))
          + list(range(ord("\u00ae"), ord("\u00ff") + 1)))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, [chr(c) for c in cs]))


BYTE_DECODER = {v: k for k, v in _bytes_to_unicode().items()}


class Decoder:
    """id -> text for the frozen BPE. Specials (<pad>/<bos>/...) are skipped.

    A flagged row is meant to be HAND-READ, so the audit has to print English,
    not ids. The vocab is a plain token->id map, so this needs no dependencies.
    """

    def __init__(self, path):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        self.inv = {i: t for t, i in d["model"]["vocab"].items()}

    def decode(self, ids):
        s = ""
        for i in ids:
            t = self.inv.get(i)
            if t is None:
                continue
            if t.startswith("<") and t.endswith(">"):
                continue
            s += t
        out = bytearray()
        for ch in s:
            b = BYTE_DECODER.get(ch)
            if b is None:
                out.extend(ch.encode("utf-8"))
            else:
                out.append(b)
        return out.decode("utf-8", errors="replace")


def repo_path(p):
    return p if os.path.isabs(p) else os.path.join(REPO, p)


def read_pair(data, split):
    """Return (ids, mask) as lists of int lists; None when the split is absent."""
    ip = os.path.join(data, "%s.ids" % split)
    mp = os.path.join(data, "%s.mask" % split)
    if not (os.path.exists(ip) and os.path.exists(mp)):
        return None, None
    with open(ip, encoding="utf-8") as fh:
        ids = [[int(x) for x in ln.split()] for ln in fh if ln.strip()]
    with open(mp, encoding="utf-8") as fh:
        mask = [[int(x) for x in ln.split()] for ln in fh if ln.strip()]
    return ids, mask


def decompose(a):
    """Split an example into turns on SEP, dropping the leading BOS / trailing
    EOS. Returns [(start, end)] spans over the ORIGINAL index space, in order:
    turn 0 is user, turn 1 assistant, turn 2 user, ..."""
    spans = []
    start = 1  # skip BOS
    end = len(a) - 1  # stop before EOS
    cur = start
    for j in range(start, end):
        if a[j] == SEP:
            spans.append((cur, j))
            cur = j + 1
    if cur < end:
        spans.append((cur, end))
    return spans


def structural(ids, mask, split):
    """Assert the layout + mask invariants. Returns (errors, stats)."""
    errs = []
    st = collections.Counter()
    turn_hist = collections.Counter()
    sep_mask = collections.Counter()
    if len(ids) != len(mask):
        errs.append("%s: ids/mask line count %d vs %d" % (split, len(ids), len(mask)))
        return errs, st
    for i, (a, b) in enumerate(zip(ids, mask)):
        tag = "%s ex%d" % (split, i)
        if len(a) != len(b):
            errs.append("%s: ids/mask length %d vs %d" % (tag, len(a), len(b)))
            continue
        if a[0] != BOS:
            errs.append("%s: first id %d != BOS" % (tag, a[0]))
        if b[0] != 0:
            errs.append("%s: mask[0] = %d != 0" % (tag, b[0]))
        if a[-1] != EOS:
            errs.append("%s: last id %d != EOS" % (tag, a[-1]))
        if b[-1] != 1:
            errs.append("%s: mask[-1] = %d != 1" % (tag, b[-1]))
        # specials must not appear inside
        for j in range(1, len(a) - 1):
            if a[j] in (BOS, EOS):
                errs.append("%s: special id %d inside at %d" % (tag, a[j], j))
        spans = decompose(a)
        turn_hist[len(spans)] += 1
        if len(spans) % 2 != 0:
            errs.append("%s: ODD turn count %d" % (tag, len(spans)))
        for k, (s, e) in enumerate(spans):
            want = 0 if k % 2 == 0 else 1
            for j in range(s, e):
                if b[j] != want:
                    errs.append("%s: turn %d (role %s) mask[%d] = %d, want %d"
                                % (tag, k, "user" if want == 0 else "assistant", j, b[j], want))
                    break
            st["user_tokens" if want == 0 else "assistant_tokens"] += (e - s)
        for j, t in enumerate(a):
            if t == SEP:
                sep_mask[b[j]] += 1
        st["tokens"] += len(a)
        st["scored"] += sum(b)
        st["turns"] += len(spans)
    if sep_mask and set(sep_mask) != {0}:
        errs.append("%s: SEP carries mask values %s, want all 0"
                    % (split, dict(sep_mask)))
    st["examples"] = len(ids)
    st["turn_hist"] = dict(sorted(turn_hist.items()))
    st["sep_mask"] = dict(sep_mask)
    return errs, st


def ngrams(seq, n):
    return [tuple(seq[i:i + n]) for i in range(len(seq) - n + 1)]


def repetition(ids, mask, split, top, dec=None):
    """Packed-split repetition census. Returns (report_lines, summary dict)."""
    out = []
    user_turns = []
    asst_turns = []
    asst_where = []
    for ex, (a, b) in enumerate(zip(ids, mask)):
        for k, (s, e) in enumerate(decompose(a)):
            t = tuple(a[s:e])
            if k % 2 == 0:
                user_turns.append(t)
            else:
                asst_turns.append(t)
                asst_where.append((ex, k))

    full = collections.Counter(tuple(a) for a in ids)
    du_ex = sum(v - 1 for v in full.values() if v > 1)
    uc = collections.Counter(user_turns)
    ac = collections.Counter(asst_turns)
    du_u = sum(v - 1 for v in uc.values() if v > 1)
    du_a = sum(v - 1 for v in ac.values() if v > 1)

    # 5-gram census: within a single assistant span (self-repetition in the
    # TARGET) and across the whole split.
    self_rep_spans = 0
    self_rep_grams = 0
    for t in asst_turns:
        g = ngrams(t, 5)
        if len(g) != len(set(g)):
            self_rep_spans += 1
            self_rep_grams += len(g) - len(set(g))
    allg = collections.Counter()
    for t in asst_turns:
        allg.update(ngrams(t, 5))
    total_g = sum(allg.values())
    dup_g = sum(v - 1 for v in allg.values() if v > 1)

    out.append("  rows                  %6d" % len(ids))
    out.append("  exact duplicate rows  %6d  (%.2f%%)"
               % (du_ex, 100.0 * du_ex / max(len(ids), 1)))
    out.append("  user turns            %6d  unique %6d  dup %6d (%.2f%%)"
               % (len(user_turns), len(uc), du_u, 100.0 * du_u / max(len(user_turns), 1)))
    out.append("  assistant turns       %6d  unique %6d  dup %6d (%.2f%%)"
               % (len(asst_turns), len(ac), du_a, 100.0 * du_a / max(len(asst_turns), 1)))
    out.append("  assistant 5-grams     %6d  repeated %6d (%.2f%%)"
               % (total_g, dup_g, 100.0 * dup_g / max(total_g, 1)))
    out.append("  spans with an internal repeated 5-gram: %d / %d (%.2f%%)"
               % (self_rep_spans, len(asst_turns),
                  100.0 * self_rep_spans / max(len(asst_turns), 1)))

    if du_u:
        out.append("  -- most repeated USER turns (the 'reply does not depend on")
        out.append("     the prompt' signature) --")
        for t, v in uc.most_common(top):
            if v < 2:
                break
            txt = dec.decode(t) if dec else " ".join(str(x) for x in t[:18])
            out.append("     %3dx  %s" % (v, txt.replace("\n", " ")))
    if self_rep_spans:
        out.append("  -- assistant spans that repeat a 5-gram internally (the")
        out.append("     'repetition in, repetition out' signature) --")
        shown = 0
        for t, (ex, k) in zip(asst_turns, asst_where):
            g = ngrams(t, 5)
            if len(g) != len(set(g)):
                txt = dec.decode(t) if dec else " ".join(str(x) for x in t[:20])
                out.append("     ex%-5d turn%d  %s" % (ex, k, txt.replace("\n", " ")))
                shown += 1
                if shown >= top:
                    break
    summ = dict(rows=len(ids), dup_rows=du_ex, user_turns=len(user_turns),
                uniq_user=len(uc), dup_user=du_u, asst_turns=len(asst_turns),
                uniq_asst=len(ac), dup_asst=du_a, grams=total_g, dup_grams=dup_g,
                self_rep_spans=self_rep_spans)
    return out, summ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="runs/synth2")
    ap.add_argument("--split", default="train,heldout")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    data = repo_path(args.data)
    if not os.path.isdir(data):
        sys.exit("data dir not found: %s" % data)

    lines = []
    lines.append("synth2 SPLIT AUDIT (D3)")
    lines.append("data = %s" % os.path.relpath(data, REPO))
    lines.append("")

    dec = None
    tokp = os.path.join(data, "tokenizer.json")
    if os.path.exists(tokp):
        dec = Decoder(tokp)
    else:
        lines.append("(no tokenizer.json -- rows print as ids)")

    all_errs = []
    for split in [s.strip() for s in args.split.split(",") if s.strip()]:
        ids, mask = read_pair(data, split)
        if ids is None:
            lines.append("## %s: MISSING (skipped)" % split)
            lines.append("")
            continue
        lines.append("## %s" % split)
        errs, st = structural(ids, mask, split)
        all_errs.extend(errs)
        lines.append("  examples %d  tokens %d  scored(mask=1) %d (%.1f%%)"
                     % (st["examples"], st["tokens"], st["scored"],
                        100.0 * st["scored"] / max(st["tokens"], 1)))
        lines.append("  user tokens %d  assistant tokens %d"
                     % (st["user_tokens"], st["assistant_tokens"]))
        lines.append("  turns per example %s   SEP masks %s"
                     % (st["turn_hist"], st["sep_mask"]))
        lines.append("  structural errors: %d" % len(errs))
        for e in errs[:10]:
            lines.append("    !! %s" % e)
        if len(errs) > 10:
            lines.append("    ... %d more" % (len(errs) - 10))
        lines.append("  repetition census:")
        rep, _ = repetition(ids, mask, split, args.top, dec)
        lines.extend(rep)
        lines.append("")

    # exids line-count agreement (the split's own index sidecar).
    for split in ("train", "heldout"):
        p = os.path.join(data, "%s.exids" % split)
        ip = os.path.join(data, "%s.ids" % split)
        if os.path.exists(p) and os.path.exists(ip):
            n = sum(1 for ln in open(p, encoding="utf-8") if ln.strip())
            m = sum(1 for ln in open(ip, encoding="utf-8") if ln.strip())
            ok = "ok" if n == m else "MISMATCH"
            lines.append("%s.exids %d vs %s.ids %d  -> %s" % (split, n, split, m, ok))
            if n != m:
                all_errs.append("%s.exids count %d != %s.ids %d" % (split, n, split, m))

    lines.append("")
    lines.append("VERDICT: %s" % ("STRUCTURE FAILED" if all_errs else "structure ok"))
    text = "\n".join(lines) + "\n"
    print(text)
    if args.out:
        op = repo_path(args.out)
        os.makedirs(os.path.dirname(op), exist_ok=True)
        with open(op, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(op, REPO))
    sys.exit(1 if all_errs else 0)


if __name__ == "__main__":
    main()
