#!/usr/bin/env python3
"""Build the ACCURATE merge worklist for the 63 frame-opener + US-conversion rows.

Why this exists: in a multi-turn row the frame violation and the US edit can sit
on DIFFERENT turns (L129 violates at assistant idx 0, its US edit is at idx 1), and
the US pass also edits USER turns. Hand-writing from a flattened dump would corrupt
rows. This emits, per line, a ready-to-fill changes entry:

    {"<line>": {"u": {<idx>: "<US text>"}, "a": {<idx>: "<US text or BLANK>"}}}

Every turn that only needs the mechanical US swap is PRE-FILLED. The single turn
that carries the frame violation is left BLANK for a hand-written text that must be
US English AND not open on `the <noun>` / the bare noun.

Read-only. Writes audit/frame_merge_worklist.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
us = json.load(open(os.path.join(ROOT, "audit", "changes_us_casual.json"), encoding="utf-8"))

rows = [json.loads(l) for l in
        open(os.path.join(ROOT, "raw", "small_talk_casual.jsonl"), "rb").read().split(b"\r\n")
        if l.strip()]

frame = []
for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6:
        continue
    frame.append({"line": int(f[0]), "pair": int(f[2]), "noun": f[3],
                  "user": f[4], "assist": f[5]})

out = {}
report = []
# group by line FIRST: a line can carry TWO frame violations (L425, L483, L1829,
# L1841), and every one of them must be blanked for hand-writing.
by_line = {}
for e in frame:
    by_line.setdefault(e["line"], []).append(e)

for ln, entries in by_line.items():
    if str(ln) not in us:
        continue
    row = rows[ln - 1]
    turns = row["turns"]
    ch = us[str(ln)]
    u_edit = ch.get("u", {}) if isinstance(ch, dict) else {}
    a_edit = ch.get("a", {}) if isinstance(ch, dict) else {}
    if isinstance(ch, dict) and not a_edit and not u_edit:
        a_edit = {k: v for k, v in ch.items() if k.isdigit()}

    entry = {"a": {}, "u": {}}
    for k, v in a_edit.items():
        entry["a"][str(k)] = v
    for k, v in u_edit.items():
        entry["u"][str(k)] = v

    asst_list = [t["text"] for t in turns if t["role"] == "assistant"]
    viol = []
    for e in entries:
        viol.append(e["pair"])
        entry["a"][str(e["pair"])] = ""          # blank EVERY violation turn
        ok = asst_list[e["pair"]] == e["assist"]
        report.append((ln, e["pair"], e["noun"], ok, len(turns),
                       sorted(entry["a"].keys()), sorted(entry.get("u", {}).keys())))
    if not entry["u"]:
        del entry["u"]
    out[str(ln)] = entry

p = os.path.join(ROOT, "audit", "frame_merge_worklist.json")
with open(p, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print(f"wrote {p}  ({len(out)} lines, {len(report)} violation turns)")

bad = [r for r in report if not r[3]]
print(f"violation-turn index verified against the corpus text: {len(report) - len(bad)}/{len(report)}")
if bad:
    print("  MISMATCHES:", bad[:5])

multi = [r for r in report if r[4] > 2]
print(f"multi-turn violation rows: {len(multi)}")
two_viol = [ln for ln, es in by_line.items() if len(es) > 1]
print(f"lines with TWO violation turns: {len(two_viol)}  {sorted(two_viol)}")
print()
print("shape check (line | viol_asst_idx | noun | turns | edited_asst | edited_user):")
for r in report[:18]:
    print(f"  L{r[0]:5d} a{r[1]} noun={r[2]:12s} turns={r[4]} asst{r[5]} user{r[6]}")
