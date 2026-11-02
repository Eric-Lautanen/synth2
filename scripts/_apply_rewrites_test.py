#!/usr/bin/env python3
"""Test harness for the extended apply_rewrites.py. Runs on a SCRATCH COPY only.

Asserts: (1) legacy assistant-only changes still compile and apply; (2) the new
"u" namespace edits USER turns; (3) a line with both roles lands in one pass;
(4) a moved/incorrect old text HARD-ABORTS rather than clobbering.
"""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
PY = sys.executable
EDITOR = os.path.join(HERE, "apply_rewrites.py")
SRC = os.path.join(ROOT, "raw", "small_talk_casual.jsonl")
SCRATCH = os.path.join(ROOT, "audit", "_applytest.jsonl")


def rows_of(path):
    return [json.loads(l) for l in open(path, "rb").read().split(b"\r\n") if l.strip()]


def run(changes, label, expect_rc=0):
    cf = os.path.join(ROOT, "audit", "_test_changes.json")
    with open(cf, "w", encoding="utf-8") as f:
        json.dump(changes, f)
    p = subprocess.run([PY, EDITOR, cf, "--file", SCRATCH, "--dry"],
                       capture_output=True, text=True)
    rc = p.returncode
    ok = (rc == expect_rc)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: rc={rc} (want {expect_rc})")
    if not ok:
        print("     " + (p.stdout + p.stderr).strip()[:400])
    return p, ok


def main():
    shutil.copy2(SRC, SCRATCH)
    base = rows_of(SCRATCH)
    print(f"scratch copy: {len(base)} rows")
    l7 = base[6]
    u0 = l7["turns"][0]["text"]
    a0 = [t["text"] for t in l7["turns"] if t["role"] == "assistant"][0]
    print(f"  line 7 user={u0!r}")
    print(f"  line 7 asst={a0!r}")

    allok = True

    # (1) legacy assistant-only form
    _, ok = run({"7": {"0": a0 + " anyway."}}, "legacy assistant-only compiles")
    allok &= ok

    # (2) new user namespace
    _, ok = run({"7": {"u": {"0": u0 + " man"}}}, "user-turn edit compiles")
    allok &= ok

    # (3) both roles on one line
    _, ok = run({"7": {"u": {"0": u0 + " man"}, "a": {"0": a0 + " anyway."}}},
                "both roles on one line compiles")
    allok &= ok

    # (4) bad old text must abort (point at a line whose assistant text we lie about)
    cf = os.path.join(ROOT, "audit", "_test_changes.json")
    with open(cf, "w", encoding="utf-8") as f:
        json.dump([{"line": 7, "role": "assistant", "old": ["NOT THE REAL TEXT"], "new": ["x"]}], f)
    p = subprocess.run([PY, EDITOR, cf, "--file", SCRATCH, "--dry"], capture_output=True, text=True)
    ok = p.returncode != 0 and "mismatch" in (p.stdout + p.stderr)
    print(f"  [{'PASS' if ok else 'FAIL'}] wrong old text HARD-ABORTS")
    allok &= ok

    # (5) actually APPLY the user edit and read it back
    cf = os.path.join(ROOT, "audit", "_test_changes.json")
    newu = u0 + " man"
    with open(cf, "w", encoding="utf-8") as f:
        json.dump({"7": {"u": {"0": newu}}}, f)
    p = subprocess.run([PY, EDITOR, cf, "--file", SCRATCH], capture_output=True, text=True)
    after = rows_of(SCRATCH)
    got = after[6]["turns"][0]["text"]
    ok = (got == newu) and (len(after) == len(base))
    print(f"  [{'PASS' if ok else 'FAIL'}] APPLIED user edit survives: {got!r}")
    if not ok:
        print("     " + (p.stdout + p.stderr).strip()[:400])
    allok &= ok

    # (6) the assistant turn on line 7 is untouched by the user-only edit
    gota = [t["text"] for t in after[6]["turns"] if t["role"] == "assistant"][0]
    ok = gota == a0
    print(f"  [{'PASS' if ok else 'FAIL'}] assistant turn untouched by user-only edit")
    allok &= ok

    os.remove(SCRATCH)
    print("\n" + ("ALL EDITOR TESTS PASS" if allok else "SOME TESTS FAILED"))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
