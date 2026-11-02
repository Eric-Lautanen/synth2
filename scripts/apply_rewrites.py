#!/usr/bin/env python3
"""apply_rewrites.py -- safe IN-PLACE text rewrite of a synth2 corpus file.

THE LAW THIS TOOL SERVES: "fix problems at the core, never dilute" -- edit the
rows that cause a bad frame or a drift in place; do not shout them down with
new rows. This is the only sanctioned in-place editor. It never changes the
row count, ids, batch numbers, categories or turn structure -- only the TEXT
of the turns you explicitly list, plus the derived length_bucket.

Input is a JSON file of CHANGES (compact form, old text is read from the
corpus so it can never be mistyped). A line may address ASSISTANT turns, USER
turns, or both. Both are needed: the US conversion measured 46% of the British
vocabulary sitting in USER turns (2026-10-10), and a row that needs a US swap
AND a frame-opener fix gets ONE combined rewrite, never two campaigns:

    {"<line>": {"<assistant_index>": "new text", ...}, ...}       # legacy: assistant
    {"<line>": {"a": {"<idx>": "..."}, "u": {"<idx>": "..."}}, ...}  # explicit role

or a full EDITS list (what the compact form compiles to; `role` defaults to
"assistant", so every pre-existing EDITS file still compiles unchanged):

    [{"line": N, "role": "user"|"assistant", "old": [...], "new": [...]}, ...]

Safety protocol, all of it load-bearing:
  * reads the corpus in BINARY and splits on \r\n (the file carries no CR pad
    since the 2026-10-07 normalisation, but binary reads stay the law);
  * round-trip check: every line must re-serialise byte-identical, so the
    writer can never reformat a row it did not intend to touch;
  * asserts each edited row's CURRENT assistant texts equal the recorded
    `old` before replacing -- a moved line is a HARD ABORT, never a clobber;
  * backs up FIRST to backups/<category>-<stamp>.bak -- NEVER inside raw/:
    the Rust loader globs raw/*.jsonl and a .jsonl backup there is silently
    trained on (found 2026-10-10: five .bak-casual-*.jsonl files had turned
    the repair gate red with 9935 phantom duplicates);
  * writes clean CRLF JSONL, row count and \r\n count asserted unchanged.

Usage (from the synth2 dir):
  python scripts/apply_rewrites.py changes.json --dry   # always dry first
  python scripts/apply_rewrites.py changes.json          # apply
  python scripts/apply_rewrites.py changes.json --file raw/small_talk_ghetto.jsonl
"""
import json
import os
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FILE = os.path.normpath(os.path.join(HERE, "..", "raw", "small_talk_casual.jsonl"))
BACKUP_DIR = os.path.normpath(os.path.join(HERE, "..", "backups"))


def bucket(n):
    return "short" if n < 15 else ("medium" if n < 60 else "long")


def load_lines(path):
    raw = open(path, "rb").read()
    parts = raw.split(b"\r\n")
    return [p for p in parts if p.strip()]


def texts(row, role="assistant"):
    return [t["text"] for t in row["turns"] if t["role"] == role]


def asst_texts(row):
    """Kept for any caller that imports it; identical to texts(row, "assistant")."""
    return texts(row, "assistant")


def compile_changes(changes, lines):
    """Compact {line: {...}} -> full edits with `old` read from the corpus.

    A line's change object addresses turns two ways:
      * a bare digit key  -> ASSISTANT turn index (legacy; every pre-2026-10-10
        changes file is assistant-only and must keep compiling byte-identically)
      * "a" / "u"         -> a {index: text} map for assistant / user turns
    A line may carry both, which yields one edit record per role -- so a row's
    US swap and its frame-opener fix land in a single rewrite pass.
    """
    edits = []
    for key, ch in changes.items():
        line = int(key)
        row = json.loads(lines[line - 1])
        if not isinstance(ch, dict):
            sys.exit(f"ABORT line {line}: change entry must be an object")
        per_role = {}
        for k, v in ch.items():
            if k in ("a", "u"):
                if not isinstance(v, dict):
                    sys.exit(f"ABORT line {line}: {k!r} must map index -> text")
                role = "assistant" if k == "a" else "user"
                for i, txt in v.items():
                    per_role.setdefault(role, {})[int(i)] = txt
            elif k.isdigit():
                if not isinstance(v, str):
                    sys.exit(f"ABORT line {line}: legacy key {k} must map to a string")
                per_role.setdefault("assistant", {})[int(k)] = v
            else:
                sys.exit(f"ABORT line {line}: unknown key {k!r} (use a digit, 'a' or 'u')")
        for role, idxmap in per_role.items():
            old = texts(row, role)
            if not old:
                sys.exit(f"ABORT line {line}: no {role} turns to edit")
            new = list(old)
            for i, txt in idxmap.items():
                if i < 0 or i >= len(new):
                    sys.exit(f"ABORT line {line}: {role} index {i} out of range ({len(new)} turns)")
                new[i] = txt
            edits.append({"line": line, "role": role, "old": old, "new": new})
    return edits


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    edits_path = sys.argv[1]
    rest = sys.argv[2:]
    dry = "--dry" in rest
    corpus = DEFAULT_FILE
    if "--file" in rest:
        corpus = rest[rest.index("--file") + 1]

    payload = json.load(open(edits_path, encoding="utf-8"))
    if isinstance(payload, dict):
        lines = load_lines(corpus)
        edits = compile_changes(payload, lines)
    else:
        edits = payload

    lines = load_lines(corpus)
    n_rows = len(lines)

    bad = 0
    for i, ln in enumerate(lines):
        r = json.loads(ln)
        if json.dumps(r, ensure_ascii=False).encode("utf-8") != ln:
            bad += 1
            if bad <= 3:
                print(f"  NOT ROUND-TRIP line {i + 1}")
        if bad > 3:
            break
    print(f"round-trip check: {bad} non-identical line(s) of {n_rows}")
    if bad:
        sys.exit("ABORT: serializer would reformat lines it did not intend to touch.")

    applied = 0
    for e in edits:
        idx = e["line"] - 1
        if idx < 0 or idx >= n_rows:
            sys.exit(f"ABORT line {e['line']}: out of range (file has {n_rows} rows)")
        role = e.get("role", "assistant")
        row = json.loads(lines[idx])
        have = texts(row, role)
        if have != e["old"]:
            sys.exit(f"ABORT line {e['line']} ({role}): text mismatch\n  have: {have}\n  want: {e['old']}")
        if len(e["new"]) != len(have):
            sys.exit(f"ABORT line {e['line']} ({role}): {len(e['new'])} new vs {len(have)} {role} turns")
        k = 0
        for t in row["turns"]:
            if t["role"] == role:
                t["text"] = e["new"][k]
                k += 1
        row["category"]["length_bucket"] = bucket(max(len(t["text"].split()) for t in row["turns"]))
        lines[idx] = json.dumps(row, ensure_ascii=False).encode("utf-8")
        applied += 1

    if dry:
        print(f"DRY: would rewrite {applied} row(s) of {n_rows}")
        return 0

    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    cat = os.path.splitext(os.path.basename(corpus))[0]
    bak = os.path.join(BACKUP_DIR, f"{cat}-{stamp}.bak")
    shutil.copy2(corpus, bak)

    body = b""
    for ln in lines:
        body += ln + b"\r\n"
    open(corpus, "wb").write(body)

    after = load_lines(corpus)
    assert len(after) == n_rows, "row count changed"
    print(f"rewrote {applied} row(s); rows {n_rows} -> {len(after)}; backup -> {bak}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
