#!/usr/bin/env python3
"""synth2 row appender -- the one door into runs/synth2/raw/.

Agents hand-write rows as JSON and pipe or pass them here. The script:
  * routes rows to the CURRENT category file (one file at a time; 2000 rows
    is the first-pass base target, not a cap -- a complete file stays open
    for later top-ups through --category)
  * fixes up everything derivable: interaction_type, tone, turn_structure,
    length_bucket, batch_no, unique ids
  * validates the row shape the way prepare.rs will (alternation, roles,
    ASCII, turn caps, ends-on-assistant)
  * preflights the exact near-dup gate prepare.rs runs (3-shingle Jaccard
    >= 0.60, corpus-wide), so nothing lands that a later prepare would drop
  * gates are PER ROW: rows that fail a gate are skipped and reported, the
    rest of the batch appends as normal
  * pins the intended file when the command starts; a batch queued behind the
    lock never gets rerouted to the next file -- batches overfill their file
    or fail loudly, they are never split
  * holds a lock so several agents can append concurrently without trampling
  * recounts every category, rewrites the CONTINUE.md status table, and
    keeps scripts/status.json as the machine-readable ledger

THE ROWS MUST BE HAND-WRITTEN. This script is a serializer, not an author.
No generators, no slot-filling, no phrase pools (see readme.md).
PROSE ACCURACY IS THE SURVIVAL CONDITION: every reply must genuinely answer,
rebut or continue the turn before it. The gates check structure, not sense;
the owner audits batches by hand and pulls the plug on agents whose batches
fail the read -- access revoked, no appeal.

Usage:
  python add_rows.py --rows-file rows.json [--dry-run] [--category casual]
  python add_rows.py --stdin < rows.json
  python add_rows.py --status

Scratch hygiene: write your batch JSON to a temp location OUTSIDE
runs/synth2/ (e.g. the system temp dir) and DELETE it once the append
succeeds. The campaign folder never holds scratch files.

Row JSON (any of these shapes; the only required field is turns):
  [{"turns": [["user", "hey"], ["assistant", "hey yourself"]]}, ...]
  {"rows": [{"turns": [{"role": "user", "text": "..."}, ...]}, ...]}
  {"user": "hi", "assistant": "hello"}                     (single exchange)
  {"exchanges": [["u...", "a..."], ["u...", "a..."]]}       (multi-turn)

Plain-text alternative (no JSON at all): one row per line, turns separated
by " | ", alternating user/assistant, starting with user:
  you up? | barely. why. | wanna get breakfast? | too much outside for this hour.

Optional per-row overrides: category, turn_structure, length_bucket.
Everything else is derived. An exchange is one user+assistant pair.
"""

import argparse
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # runs/synth2
RAW = os.path.join(ROOT, "raw")
SCRIPTS = os.path.join(ROOT, "scripts")
CONTINUE_MD = os.path.join(ROOT, "CONTINUE.md")
STATUS_JSON = os.path.join(SCRIPTS, "status.json")
LOCK_PATH = os.path.join(SCRIPTS, ".add_rows.lock")
MIN_ROWS = 2000                # first-pass base target per file -- a file at
                               # 2000 is COMPLETE, not closed; it stays open
                               # for later top-ups (--category, no --force)
MAX_TURN_CHARS = 4000          # loader cap (load_corpus call site)
NEAR_DUP_MIN_DISTANCE = 0.60   # prepare.rs global gate
MAX_EXCHANGES = 5              # charter: short_multi_turn = 2-5 exchanges
BATCH_GAP = 15

# Order IS the charter order; the first category under MIN_ROWS is current.
CATEGORIES = [
    ("casual",       "warm_casual"),
    ("lazy",         "flat_lazy"),
    ("angry",        "hostile_raw"),
    ("sexy",         "flirty_hot"),
    ("formal",       "formal_polite"),
    ("sarcastic",    "dry_snark"),
    ("excited",      "hyped_up"),
    ("gloomy",       "low_gloomy"),
    ("anxious",      "wired_anxious"),
    ("gossip",       "conspiratorial"),
    ("nostalgic",    "wistful_warm"),
    ("philosophical","musing_odd"),
    ("teasing",      "ribbing_playful"),
    ("supportive",   "kind_steady"),
    ("bored",        "listless_bored"),
    ("curious",      "nosy_curious"),
    ("deflecting",   "slippery_evasive"),
    ("ranting",      "exasperated_vent"),
    ("flirty",       "playful_flirty"),
    ("sullen",       "sullen_withdrawn"),
    ("celebratory",  "toasting_joy"),
    ("confused",     "lost_confused"),
    ("petty",        "petty_scorekeeping"),
    ("weird",        "offbeat_surreal"),
    ("greetings",    "warm_greeting"),
    ("dont_know",    "honest_unsure"),
    ("thanks",       "warm_thanks"),
    ("apology",      "rueful_sorry"),
    ("goodbye",      "easy_farewell"),
]
TONES = dict(CATEGORIES)

class RowError(Exception):
    pass


# ---------------------------------------------------------------------------
# locking (Windows-safe: O_EXCL spin with stale-break)
# ---------------------------------------------------------------------------

class Lock:
    def __init__(self, path, stale_seconds=120):
        self.path = path
        self.stale = stale_seconds
        self.fd = None

    def __enter__(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        while True:
            try:
                self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, f"{os.getpid()} {time.time()}".encode())
                return self
            except FileExistsError:
                try:
                    age = time.time() - os.path.getmtime(self.path)
                    if age > self.stale:
                        print(f"lock: breaking stale lock ({int(age)}s old)", file=sys.stderr)
                        os.unlink(self.path)
                        continue
                except FileNotFoundError:
                    continue
                time.sleep(0.2)

    def __exit__(self, *exc):
        try:
            os.close(self.fd)
            os.unlink(self.path)
        except OSError:
            pass
        return False


# ---------------------------------------------------------------------------
# sketch + shingles -- mirrors prepare.rs (near-dup gate parity)
# ---------------------------------------------------------------------------

def sketch(text: str) -> str:
    flat = re.sub(r"\d", "#", text.lower())
    flat = re.sub(r"(#)+", "#", flat)
    flat = re.sub(r"(\s)+", " ", flat)
    return flat.strip()


def shingle_set(convo_text: str) -> frozenset:
    words = convo_text.split()
    if len(words) < 3:
        return frozenset(words)
    return frozenset(" ".join(w) for w in zip(words, words[1:], words[2:]))


def row_shingles(turns) -> frozenset:
    joined = " ".join(t for _, t in turns if t)
    return shingle_set(sketch(joined))


def jaccard_distance(a: frozenset, b: frozenset) -> float:
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return 1.0 - inter / union


def near_dup_partner(a: frozenset, b: frozenset) -> bool:
    """True if the gate would fire on this pair (distance < 0.60).

    prepare.rs prunes pairs where min/max <= 1 - min_distance; mirror that:
    inter <= min(|a|,|b|) and union >= max(|a|,|b|), so distance > 0.60 is
    guaranteed when min/max <= 0.40.
    """
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return False
    if min(la, lb) <= 0.40 * max(la, lb):
        return False
    return jaccard_distance(a, b) < NEAR_DUP_MIN_DISTANCE


# ---------------------------------------------------------------------------
# corpus state
# ---------------------------------------------------------------------------

def raw_files():
    if not os.path.isdir(RAW):
        return []
    out = []
    for name in sorted(os.listdir(RAW)):
        m = re.fullmatch(r"small_talk_(\w+)\.jsonl", name)
        if m:
            out.append((m.group(1), os.path.join(RAW, name)))
    return out


def load_existing():
    """(count per category, [(category, shingles)]) over all raw rows."""
    counts = {}
    sets = []
    for cat, path in raw_files():
        n = 0
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    turns = [(t.get("role", ""), t.get("text", "")) for t in rec.get("turns", [])]
                    sets.append((cat, row_shingles(turns)))
                except (json.JSONDecodeError, AttributeError):
                    pass  # a broken line someone else wrote; prepare will name it
                n += 1
        counts[cat] = n
    return counts, sets


def max_batch_no():
    best = 0
    for _, path in raw_files():
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    b = json.loads(line).get("batch_no") or 0
                    best = max(best, int(b))
                except (json.JSONDecodeError, ValueError):
                    pass
    return best


def max_id_seq(cat: str) -> int:
    path = os.path.join(RAW, f"small_talk_{cat}.jsonl")
    best = 0
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.search(rf'"st2_{cat}_(\d+)"', line)
                if m:
                    best = max(best, int(m.group(1)))
    return best


def current_category(counts):
    for cat, _ in CATEGORIES:
        if counts.get(cat, 0) < MIN_ROWS:
            return cat
    return None


# ---------------------------------------------------------------------------
# row parsing + validation
# ---------------------------------------------------------------------------

def coerce_turns(obj):
    if isinstance(obj, list) and obj and isinstance(obj[0], list):
        return [tuple(t) for t in obj]
    if isinstance(obj, list) and obj and isinstance(obj[0], dict):
        return [(t.get("role"), t.get("text")) for t in obj]
    if isinstance(obj, dict):
        if "turns" in obj:
            return coerce_turns(obj["turns"])
        if "exchanges" in obj:
            out = []
            for ex in obj["exchanges"]:
                if isinstance(ex, list) and len(ex) == 2 and all(isinstance(s, str) for s in ex):
                    out.extend([("user", ex[0]), ("assistant", ex[1])])
                else:
                    out.extend(coerce_turns(ex))
            return out
        keys = list(obj.keys())
        if keys and all(k in ("user", "assistant") for k in keys):
            return [(k, obj[k]) for k in keys if obj[k]]
    raise RowError("row has no turns I can read (need turns/exchanges/user+assistant)")


def validate_row(row, idx):
    """Return a normalized dict; raise RowError with a human reason."""
    if not isinstance(row, dict):
        raise RowError(f"row {idx}: not a JSON object")
    turns = coerce_turns(row)
    if not (2 <= len(turns) <= 2 * MAX_EXCHANGES):
        raise RowError(
            f"row {idx}: {len(turns)} turns (need 2..{2 * MAX_EXCHANGES}, i.e. 1..{MAX_EXCHANGES} exchanges)"
        )
    if turns[0][0] != "user":
        raise RowError(f"row {idx}: first turn must be 'user'")
    if turns[-1][0] != "assistant":
        raise RowError(f"row {idx}: rows end on an 'assistant' turn")
    for i, (role, text) in enumerate(turns):
        want = "user" if i % 2 == 0 else "assistant"
        if role != want:
            raise RowError(f"row {idx}: turn {i} is '{role}', alternation wants '{want}'")
        if not isinstance(text, str) or not text.strip():
            raise RowError(f"row {idx}: turn {i} text is empty")
        text = text.strip()
        if any(ord(c) > 127 for c in text):
            bad = next(c for c in text if ord(c) > 127)
            raise RowError(f"row {idx}: turn {i} has non-ASCII {bad!r} (English/ASCII only)")
        if any(ord(c) < 32 and c != "\t" for c in text):
            raise RowError(f"row {idx}: turn {i} has a control character")
        if len(text) > MAX_TURN_CHARS:
            raise RowError(f"row {idx}: turn {i} is {len(text)} chars (cap {MAX_TURN_CHARS})")
        turns[i] = (role, text)

    n_exchanges = len(turns) // 2
    structure = row.get("turn_structure")
    if structure is None:
        structure = "single_turn" if n_exchanges == 1 else "short_multi_turn"
    if structure == "single_turn" and n_exchanges != 1:
        raise RowError(f"row {idx}: turn_structure=single_turn but {n_exchanges} exchanges")
    if structure == "short_multi_turn" and not (2 <= n_exchanges <= MAX_EXCHANGES):
        raise RowError(f"row {idx}: turn_structure=short_multi_turn but {n_exchanges} exchanges")
    if structure not in ("single_turn", "short_multi_turn"):
        raise RowError(f"row {idx}: bad turn_structure {structure!r}")

    bucket = row.get("length_bucket")
    if bucket is None:
        longest = max(len(t.split()) for _, t in turns)
        bucket = "short" if longest < 15 else ("medium" if longest < 60 else "long")
    if bucket not in ("short", "medium", "long"):
        raise RowError(f"row {idx}: bad length_bucket {bucket!r}")

    return {
        "turns": turns,
        "turn_structure": structure,
        "length_bucket": bucket,
        "category": row.get("category"),
    }


# ---------------------------------------------------------------------------
# writing
# ---------------------------------------------------------------------------

def serialize(norm, batch_no, row_id):
    rec = {
        "id": row_id,
        "batch_no": batch_no,
        "category": {
            "interaction_type": "small_talk",
            "tone": TONES[norm["category"]],
            "turn_structure": norm["turn_structure"],
            "length_bucket": norm["length_bucket"],
        },
        "turns": [{"role": r, "text": t} for r, t in norm["turns"]],
    }
    return json.dumps(rec, ensure_ascii=True)


def update_continue_md(counts):
    """Rewrite the count cell of each status-table row; leave notes alone."""
    if not os.path.isfile(CONTINUE_MD):
        return
    with open(CONTINUE_MD, encoding="utf-8") as f:
        text = f.read()
    changed = False
    for idx, (cat, _) in enumerate(CATEGORIES, start=1):
        fname = f"small_talk_{cat}.jsonl"
        pat = re.compile(rf"^(\|\s*{idx}\s*\|\s*{re.escape(fname)}\s*\|)\s*\d+\s*(\|.*)$", re.M)
        new_text, n = pat.subn(rf"\g<1> {counts.get(cat, 0)} \g<2>", text)
        if n:
            changed = changed or new_text != text
            text = new_text
    if changed:
        with open(CONTINUE_MD, "w", encoding="utf-8") as f:
            f.write(text)


def write_status(counts, current, appended):
    os.makedirs(SCRIPTS, exist_ok=True)
    status = {
        "updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "current_category": current,
        "counts": {c: counts.get(c, 0) for c, _ in CATEGORIES},
        "min_rows_per_file": MIN_ROWS,
        "last_append": appended,
    }
    old = {}
    if os.path.isfile(STATUS_JSON):
        try:
            with open(STATUS_JSON, encoding="utf-8") as f:
                old = json.load(f)
        except json.JSONDecodeError:
            pass
    history = old.get("history", [])
    if appended:
        history.append(appended)
        history = history[-500:]
    status["history"] = history
    with open(STATUS_JSON, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=1)
    return status


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------

def cmd_status():
    counts, _ = load_existing()
    cur = current_category(counts)
    total = sum(counts.values())
    print(f"{'#':>2}  {'file':34} {'rows':>5}  status")
    for idx, (cat, _) in enumerate(CATEGORIES, start=1):
        n = counts.get(cat, 0)
        mark = f"  <-- CURRENT (tone: {TONES[cat]})" if cat == cur else ("  complete" if n >= MIN_ROWS else "")
        print(f"{idx:>2}  small_talk_{cat + '.jsonl':<24} {n:>5}{mark}")
    print(f"\ncorpus total: {total} rows; current file: {cur and 'small_talk_' + cur + '.jsonl'}"
          + (f" (tone: {TONES[cur]} -- write in this register)" if cur else ""))
    return 0


def cmd_add(rows, want_category, dry_run, writer, intended=None, force=False):
    counts, existing_sets = load_existing()
    cur = current_category(counts)
    if want_category and (force or want_category != cur):
        if want_category not in [c for c, _ in CATEGORIES]:
            print(f"unknown category {want_category!r}; valid: {', '.join(c for c, _ in CATEGORIES)}", file=sys.stderr)
            return 1
        n = counts.get(want_category, 0)
        if not force and n < MIN_ROWS:
            print(f"refusing: {want_category} has {n}/{MIN_ROWS} rows; the CURRENT file is "
                  f"{cur} (one file at a time). Finish {cur} first, pass its rows to it, "
                  f"or pass --force to write this file anyway.", file=sys.stderr)
            return 1
        # --force: write to the named category whatever the charter pointer says --
        # including a file that does not exist yet, or one already at MIN_ROWS.
        cur = want_category
    if cur is None:
        print("all categories are complete; pass --force --category <name> to top one up", file=sys.stderr)
        return 1

    # Batches are never split or rerouted: the intended file was pinned when
    # this command STARTED (before the lock wait). If another writer completed
    # that file while this batch queued, fail loudly instead of landing rows
    # composed for one register into the next file's register.
    if want_category is None and intended is not None and cur != intended:
        print(f"aborting batch: it was composed for {intended}, but {intended} was completed "
              f"by another writer before this append took the lock; the current file is now "
              f"{cur}. Resubmit the batch in the {cur} register (batches are never split "
              f"across files).", file=sys.stderr)
        return 1

    # per-row gates: offending rows are skipped and reported; the rest append
    valid, reasons = [], []
    for i, row in enumerate(rows, start=1):
        try:
            norm = validate_row(row, i)
            norm["category"] = norm["category"] or cur
            if norm["category"] != cur:
                raise RowError(f"row {i}: category {norm['category']!r} != current {cur!r} "
                               f"(one file at a time; drop the per-row category)")
            valid.append((i, norm))
        except RowError as e:
            reasons.append((i, str(e)))

    # near-dup gate, row by row -- offenders are skipped, not fatal:
    #   pass 1: within the batch, first of a near-dup pair survives
    #   pass 2: against the whole existing corpus
    sets = [(i, n, row_shingles(n["turns"])) for i, n in valid]
    alive = [True] * len(sets)
    for a in range(len(sets)):
        if not alive[a]:
            continue
        ia, _, sa = sets[a]
        for b in range(a + 1, len(sets)):
            ib, _, sb = sets[b]
            if alive[b] and near_dup_partner(sa, sb):
                alive[b] = False
                reasons.append((ib, f"row {ib}: near-dup of row {ia} in this batch "
                                    f"(shingle Jaccard < {NEAR_DUP_MIN_DISTANCE})"))
    for a, (ia, _, sa) in enumerate(sets):
        if not alive[a]:
            continue
        for j, (cat, t) in enumerate(existing_sets):
            if near_dup_partner(sa, t):
                alive[a] = False
                reasons.append((ia, f"row {ia}: near-dup of existing {cat} row #{j + 1} "
                                    f"(shingle Jaccard < {NEAR_DUP_MIN_DISTANCE})"))
                break

    norms = [s[1] for s, a in zip(sets, alive) if a]
    for _, why in sorted(reasons):
        print(f"SKIP {why} -- rewrite it by hand", file=sys.stderr)
    if not norms:
        print("REJECT: no rows survived the gates; nothing appended", file=sys.stderr)
        return 1

    batch_no = max_batch_no() + BATCH_GAP if raw_files() else 2000
    seq = max_id_seq(cur)
    lines = []
    for norm in norms:
        seq += 1
        lines.append(serialize(norm, batch_no, f"st2_{cur}_{seq:06d}"))

    if dry_run:
        print(f"DRY RUN ok: {len(lines)} row(s) -> small_talk_{cur}.jsonl, batch_no={batch_no}")
        for ln in lines[:3]:
            print("  " + (ln[:150] + ("..." if len(ln) > 150 else "")))
        if len(lines) > 3:
            print(f"  ... and {len(lines) - 3} more")
        return 0

    target = os.path.join(RAW, f"small_talk_{cur}.jsonl")
    os.makedirs(RAW, exist_ok=True)
    with open(target, "a", encoding="utf-8") as f:
        for ln in lines:
            f.write(ln + "\n")

    counts, _ = load_existing()
    update_continue_md(counts)
    status = write_status(counts, current_category(counts), {
        "category": cur, "rows": len(lines), "batch_no": batch_no,
        "writer": writer,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
    })
    print(f"appended {len(lines)} row(s) -> small_talk_{cur}.jsonl "
          f"({counts[cur]}/{MIN_ROWS}), batch_no={batch_no}, writer={writer}")
    if reasons:
        print(f"skipped {len(reasons)} offending row(s) above -- rewrite them and resubmit")
    print(f"next validation: cargo run --release -p train --bin repair -- --data runs/synth2 --locations")
    print("hygiene: delete your temp rows file now -- scratch does not belong in runs/synth2/")
    print("quality: every reply must genuinely answer its turn -- sloppy batches get their writer's access pulled")
    if counts[cur] >= MIN_ROWS:
        nxt = current_category(counts)
        print(f"{cur} is COMPLETE for the first pass. Next file opens: {nxt} "
              f"(completed files stay open for top-ups; status table updated).")
    return 0


def parse_pipe_lines(text):
    """Plain-text fallback: one row per line, turns separated by ' | ',
    alternating user/assistant starting with user. Blank lines and lines
    starting with '#' are skipped. Use this when JSON is more trouble than
    it is worth; the row content is still hand-written either way."""
    rows = []
    for ln, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) < 2 or len(parts) % 2 != 0 or any(not p for p in parts):
            raise RowError(
                f"line {ln}: need an even number of non-empty turns separated by ' | ' "
                f"(user | assistant | user | assistant ...)")
        rows.append({"turns": [["user" if i % 2 == 0 else "assistant", p]
                               for i, p in enumerate(parts)]})
    return rows


def load_rows(args):
    if args.rows_file:
        with open(args.rows_file, encoding="utf-8") as f:
            raw = f.read()
    elif args.stdin:
        raw = sys.stdin.read()
    else:
        return None
    stripped = raw.lstrip()
    if not stripped:
        raise RowError("rows input is empty")
    if stripped[0] not in "[{":
        return parse_pipe_lines(raw)
    data = json.loads(raw)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "rows" in data:
            return data["rows"]
        return [data]  # single row
    raise RowError("rows JSON must be a list, a {rows: [...]}, or a single row object")


def main():
    ap = argparse.ArgumentParser(description="synth2 row appender (rows must be hand-written; see readme.md)")
    ap.add_argument("--rows-file", help="JSON file of rows (list, {rows:[...]}, or one row)")
    ap.add_argument("--stdin", action="store_true", help="read rows JSON from stdin")
    ap.add_argument("--category", choices=[c for c, _ in CATEGORIES],
                    help="route explicitly (defaults to the CURRENT file; refuses non-current unless "
                         "complete, or unless --force is given)")
    ap.add_argument("--by", help="your writer name, recorded in the ledger -- REQUIRED for audits; "
                    "batches written as 'unknown-agent' are first in line for the plug")
    ap.add_argument("--dry-run", action="store_true", help="validate + preflight, write nothing")
    ap.add_argument("--status", action="store_true", help="print per-category counts and exit")
    ap.add_argument("--force", action="store_true",
                    help="write to ANY category named by --category, even if it is not the current "
                         "file, does not exist yet, or is already complete (bypasses the "
                         "one-file-at-a-time routing)")
    args = ap.parse_args()

    if args.force and not args.category:
        print("error: --force needs --category <name> (which file to force)", file=sys.stderr)
        return 1

    if args.status:
        return cmd_status()

    try:
        rows = load_rows(args)
    except (RowError, json.JSONDecodeError, OSError) as e:
        print(f"error reading rows: {e}", file=sys.stderr)
        return 1
    if rows is None:
        ap.print_usage()
        print("\nnothing to do: pass --rows-file, --stdin, or --status", file=sys.stderr)
        return 1

    # pin the intended file BEFORE waiting on the lock: the batch was composed
    # for whatever file was current at command start, and must never be
    # silently rerouted to a later file that opened while the agent queued.
    intended = args.category or current_category(load_existing()[0])

    with Lock(LOCK_PATH):
        writer = args.by or os.environ.get("AGENT_NAME", "unknown-agent")
        if writer == "unknown-agent" and not args.dry_run:
            print("warning: writer identity unknown -- pass --by <your-name> (or set AGENT_NAME). "
                  "Anonymous batches are the first the owner audits.", file=sys.stderr)
        return cmd_add(rows, args.category, args.dry_run, writer, intended=intended, force=args.force)


if __name__ == "__main__":
    sys.exit(main())
