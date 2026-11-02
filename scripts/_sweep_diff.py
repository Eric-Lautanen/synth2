#!/usr/bin/env python3
"""Diff run 14's --sample-sweep against run 13's (the noise-floor read).

Run 14 = a REPEAT of run 13's config on the b2750-fixed corpus, so every
difference here is NOISE. The point is to establish the noise floor: which of
the four observables is stable enough to rank an intervention on.

Read-only. Writes audit/sample_sweep_diff_13_14.md.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))


def parse(p):
    cells, greedy, best = {}, None, None
    for ln in open(p, encoding="utf-8"):
        m = re.match(r"\s*(\d\.\d\d)\s+(\d+|-)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([\d.]+)\s*$", ln)
        if m:
            cells[(m.group(1), m.group(2))] = tuple(float(x) for x in m.groups()[2:])
        g = re.match(r"GREEDY baseline: loops (\d+)/(\d+)\s+eos (\d+)\s+echo ([\d.]+)\s+selfrep ([\d.]+)", ln)
        if g:
            greedy = tuple(float(x) for x in g.groups())
        b = re.match(r"BEST cell with loops <= greedy: temp ([\d.]+) topk (\d+) -> echo ([\d.]+)", ln)
        if b:
            best = b.groups()
    return cells, greedy, best


c13, g13, b13 = parse(os.path.join(ROOT, "audit", "sample_sweep_best.txt"))
c14, g14, b14 = parse(os.path.join(ROOT, "audit", "sample_sweep14_best.txt"))

out = []
out.append("# run 14 --sample-sweep vs run 13 (NOISE-FLOOR read)\n")
out.append("run 13 = best.bin sha256 `821c9cfe...` (pre-run-14 reference)")
out.append("run 14 = best.bin sha256 `748b63b5...` (final step 16596; best.bin == final.bin)\n")
out.append("Run 14 is a REPEAT of run 13's config on the b2750-fixed corpus. Every")
out.append("difference below is therefore NOISE, and its SIZE is the floor any real")
out.append("effect must clear.\n")
out.append("## Greedy baseline (the apples-to-apples cell)\n")
out.append("| observable | run 13 | run 14 | delta |")
out.append("|---|---|---|---|")
names = ["loops", "of 60", "eos", "echo", "selfrep"]
for i, n in enumerate(names):
    a, b = g13[i], g14[i]
    d = b - a
    out.append(f"| {n} | {a:g} | {b:g} | {d:+g} |")

out.append("\n## Per-cell echo (sampled decoding, 16 cells)\n")
out.append("| temp/topk | run 13 | run 14 | delta |")
out.append("|---|---|---|---|")
deltas = []
for k in sorted(set(c13) & set(c14)):
    a, b = c13[k][2], c14[k][2]
    deltas.append(abs(b - a))
    out.append(f"| {k[0]} / {k[1]} | {a:.3f} | {b:.3f} | {b-a:+.3f} |")
out.append(f"\nmean |delta echo| = **{sum(deltas)/len(deltas):.4f}**, max = **{max(deltas):.3f}**")

out.append("\n## Best cell (selected by the tool)\n")
out.append(f"- run 13: temp {b13[0]} topk {b13[1]} -> echo {b13[2]}")
out.append(f"- run 14: temp {b14[0]} topk {b14[1]} -> echo {b14[2]}")

out.append("\n## VERDICT\n")
out.append("- **echo is STABLE**: greedy 0.097 -> 0.096 (delta -0.001) on two same-config runs.")
out.append("  So the ~90% ungrounded gap is NOT noise -- it is a real property of the model.")
out.append("- **loops is NOT stable**: greedy 3/60 -> 8/60 (+5) on the SAME config. On n=60 that")
out.append("  is the floor: a loop-count change must exceed ~5 probes to be visible at all.")
out.append("  DO NOT rank runs or interventions on loop count alone (this is the third time this")
out.append("  has bitten: run 13's own sweep found `loops` had 3 distinct values across 2,304 neurons).")
out.append("- **selfrep is noisy at this scale**: 0.019 -> 0.013 (+-0.006 on the same config).")
out.append("- **The winning CELL is noise-driven**: run 13 picked 0.70/100, run 14 picked 0.50/10.")
out.append("  Which cell 'wins' carries no information at this sample size.")
out.append("- The decoded samples are the SAME failure mode in both runs (word salad, e.g.")
out.append("  'do the gardenenenenenengege anything good then, then?'). The b2750 fix changed nothing")
out.append("  measurable -- consistent with run 13 vs 14 being a genuine noise-floor pair.")

txt = "\n".join(out) + "\n"
p = os.path.join(ROOT, "audit", "sample_sweep_diff_13_14.md")
open(p, "w", encoding="utf-8").write(txt)
print(txt)
