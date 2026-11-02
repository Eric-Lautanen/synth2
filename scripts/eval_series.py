#!/usr/bin/env python3
"""eval_series.py -- archive one run's per-eval heldout series OUT of train_stdout.log.

WHY THIS EXISTS: `train_stdout.log` is OVERWRITTEN at the start of every run, so the
previous run's eval series is destroyed the moment the next run is fired. This must be
run in the window between a run exiting and the next run starting.

    python runs/synth2/scripts/eval_series.py 102

Writes `runs/synth2/audit/eval_series_r<N>.txt`: a short provenance header, then every
`eval step ...` block copied VERBATIM (including the per-register lines and the
`heldout gen` patience line) so the archived file is a faithful slice, not a summary.

Replaces the swept `tmp_eval_series.py` (hygiene sweep, 2026-10-25 22:53-23:09 UTC).
Same output shape as eval_series_r90..r101 so the series stay comparable.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SYNTH = os.path.normpath(os.path.join(HERE, ".."))
LOG = os.path.join(SYNTH, "train_stdout.log")
AUDIT = os.path.join(SYNTH, "audit")

HEADER = """# run {run} per-eval heldout series (extracted from train_stdout.log before the next run overwrites it)
# extracted {stamp} UTC
# NOTE: the frozen tail RE-EVALUATES THE SAME CHECKPOINT -- the last eval line(s) repeat
# the final measurement, one measurement printed twice, not a flat plateau.
# Dedupe on the checkpoint, not the step, when reading the series.
# Standing tool: `runs/synth2/scripts/eval_series.py <run>`; run it in the gap between
# a run exiting and the next run firing. The other agent verifies it landed.

"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run = sys.argv[1].lstrip("r")
    if not run.isdigit():
        sys.exit(f"ABORT: run must be an integer or rN, got {sys.argv[1]!r}")
    if not os.path.exists(LOG):
        sys.exit(f"ABORT: no {LOG}")

    with open(LOG, "r", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()

    start = next((i for i, l in enumerate(lines) if l.startswith("eval step")), None)
    if start is None:
        sys.exit("ABORT: no 'eval step' line in train_stdout.log -- wrong run or empty log")

    # Keep ONLY the eval blocks. The log interleaves `step NNNN ...` progress lines and
    # `sample N: ...` dumps between evals; copying the raw tail made a 187-line file where
    # the r90-r101 archives are 87. Match their shape: `eval step` + indented `heldout(...)`.
    body = [l for l in lines[start:]
            if l.startswith("eval step") or l.startswith("  heldout")]
    evals = sum(1 for l in body if l.startswith("eval step"))
    if evals == 0:
        sys.exit("ABORT: eval block found but contained no eval lines")

    os.makedirs(AUDIT, exist_ok=True)
    out = os.path.join(AUDIT, f"eval_series_r{run}.txt")
    if os.path.exists(out):
        sys.exit(f"ABORT: {out} already exists -- refusing to clobber an archive")

    stamp = time.strftime("%Y-%m-%d %H:%M")
    text = HEADER.format(run=run, stamp=stamp) + "\n".join(body).rstrip() + "\n"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    last = [l for l in body if l.startswith("eval step")][-1]
    print(f"wrote {out}")
    print(f"  evals archived: {evals}")
    print(f"  last: {last}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
