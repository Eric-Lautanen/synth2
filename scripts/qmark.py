# -*- coding: utf-8 -*-
"""qmark -- enforce the campaign's question-mark law over runs/synth2/raw/.

Law (root readme.md:326): "Questions end with `?`, never `.`  Imperatives,
exclamations, and deliberately broken proofreading-drill inputs are the only
exceptions. when in doubt, read the turn: if it asks, it takes `?`."

This exists because two of the three register files were written with almost no
terminal punctuation: on 2026-09-16 `casual` had 768 `?` in 5,950 turns, while
`ghetto` had 239 in 6,498 and `lazy` had 5 in 4,108. A writer appending to
`ghetto`/`lazy` drops the mark; a writer appending to `casual` does not.

    python runs/synth2/scripts/qmark.py          # report only, never writes
    python runs/synth2/scripts/qmark.py --fix    # mark, under the append lock

--fix takes add_rows.py's own lock, so it serializes against concurrent appends;
it backs the file up outside the campaign folder, re-validates every line as
JSON, asserts the row count is unchanged, and writes via temp-file + os.replace.
Only turn TEXT changes -- adding `?` cannot alter a word count, so
turn_structure / length_bucket / id / batch_no are untouched.

SCOPE / KNOWN LIMIT: the classifier is high-precision, not exhaustive. It fires
on wh-opens, auxiliary-opens, preposition+wh, "you <state>" fragments and
adj+noun ellipsis. It deliberately does NOT mark bare discourse prompts
("and", "so") -- see PROMPTS -- and it carries a BLOCK list of turns that read
as flat assertions in their register ("you right", "you got a work voice",
"nothing new"). Re-read the report after a run; if a question is still unmarked,
add its pattern here rather than widening the rules blindly.
"""
import importlib.util
import json
import os
import re
import shutil
import sys
from collections import Counter

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.abspath(os.path.join(SCRIPTS, os.pardir, "raw"))
ADD_ROWS = os.path.join(SCRIPTS, "add_rows.py")
BACKUP = os.path.join(os.environ.get("TEMP", r"C:\tmp"), "synth2_qmark_backup")

spec = importlib.util.spec_from_file_location("add_rows", ADD_ROWS)
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)

WH = {"what", "when", "where", "who", "whom", "whose", "why", "how", "which"}
AUX = {"is", "are", "was", "were", "am", "do", "does", "did", "have", "has", "had",
       "can", "could", "will", "would", "shall", "should", "may", "might", "must",
       "isnt", "arent", "wasnt", "werent", "dont", "doesnt", "didnt", "havent",
       "cant", "couldnt", "wont", "wouldnt", "shouldnt", "aint"}
SUBJ = {"it", "you", "they", "we", "he", "she", "i", "that", "this", "there", "anyone",
        "someone", "everyone", "anybody", "somebody", "nobody", "any", "all", "one",
        "those", "these", "us", "them", "me", "him", "her", "yall", "y"}
PREP = {"for", "from", "about", "of", "like", "to", "with", "at", "on", "in", "over",
        "into", "by", "after", "before", "between", "since", "than", "against"}
YOU_Q = {"busy", "sure", "ok", "okay", "good", "fine", "alright", "awake", "up", "in",
         "out", "back", "home", "free", "ready", "done", "finished", "serious",
         "joking", "hungry", "cold", "warm", "tired", "drunk", "mad", "upset", "happy",
         "sad", "bored", "lonely", "working", "sleeping", "watching", "listening",
         "coming", "going", "leaving", "eating", "still", "around", "there", "gonna",
         "think", "want", "need", "mean", "mind", "remember", "see", "hear", "feel",
         "got", "get", "ever", "too", "even", "know", "figure", "reckon", "managing"}
ADJ_NOUN = {"long", "good", "bad", "rough", "busy", "slow", "hard", "big", "quiet", "nice",
            "weird", "strange", "tough", "heavy", "short", "early", "late"}
NOUNS = {"day", "night", "week", "weekend", "one", "thing", "time", "shift", "morning",
         "evening", "afternoon", "year", "month", "plans", "plan", "news", "mood"}
ANY_OPEN = {"anything", "anyone", "anybody", "everything", "everyone", "everybody",
            "something", "someone", "somebody", "nothing", "nobody"}
# the whole turn is one of these -> an invitation to continue, i.e. it asks
PROMPTS = {"and", "and then", "and now", "or what", "or not", "then what", "what else",
           "anything else", "anything new", "so what"}
WH_NOT_Q = ("what a ", "what an ", "what the ", "how nice", "how lovely", "how kind",
            "how sweet", "how good", "whatever ", "whats ", "who knows")
GREETING = ("good morning", "good evening", "good afternoon", "good night")
TAG_END = re.compile(r",\s*(right|is it|isn't it|isnt it|aren't you|arent you|didn't it|didnt it|"
                     r"didn't you|didnt you|weren't you|werent you|wasn't it|wasnt it|"
                     r"don't you|dont you|won't you|wont you|huh|innit|eh|or not|or what)\s*[.!]?$",
                     re.I)

# Verified NON-questions -- read in context 2026-09-16. Each is a flat assertion
# in its register; a '?' would turn a statement into a question. Keep this list
# short and justified; it is not a dumping ground for inconvenient matches.
BLOCK = {
    "you right", "you right, i'm beat",
    "you know", "you know when they sleep", "you know you do it",
    "you know that's disrespectful", "you know you want to", "you know what you did",
    "you got a work voice", "you got hands that remember", "you got more than moments",
    "you got the last one", "you got me",
    "why is a question that cost energy and give back nothin",
    "nothing new", "long one", "nobody else do", "when i can",
    "whatever", "whatever's closest",
    # Verified NON-question 2026-09-25 (workbuddy, teasing b5735, read in
    # context): a flat report of what the room did -- the credit changed hands
    # in private and no witness saw it. Fires the ANY_OPEN branch on "nobody".
    # A '?' would turn a plain statement into a question nobody asked.
    "nobody else noticed",
    # Verified NON-questions 2026-09-20 (muse-spark rewritten gossip b4835/4865,
    # read in context by buffy): statement fragments and one aphorism that fire
    # the wh-open / prep+wh branches. A '?' would turn each into a question.
    "over what the login represented, apparently",
    "which explains why the last bus always smells faintly of wet coats",
    "where the lemon sugar verdict gets overturned hourly",
    "what goes in as a whisper comes out as minutes",
    # Verified NON-question 2026-09-20 (buffy, philosophical b5480, read in
    # context): completes the user's own thought -- a declarative that fires
    # the subject-copula fragment branch because of the SUBJ-set "everything".
    "everything else is marketing",
    # Verified NON-question 2026-09-20 (buffy, gossip b4820, read in context):
    # free-relative declarative -- "which month it was" is a noun clause, not a
    # question. Fires the wh-open branch.
    "which month it was is the clue",
}


def asks(text):
    t = text.strip()
    low = t.lower()
    if low in BLOCK:
        return False
    for bad in WH_NOT_Q:
        if low.startswith(bad):
            return False
    for g in GREETING:
        if low.startswith(g):
            return False
    if TAG_END.search(low):
        return True
    # An ECHO opener followed by a statement is not a question. "which one, the
    # long one, i saw the subject line and i closed it, ..." opens with a wh-word
    # but is prose: the wh-clause is just picking up the previous turn's word.
    # Signature: a short first clause (<=4 words) plus a long tail (>=8 words).
    # A real ask with a comma keeps the wh-clause long ("how long have you been on
    # the sofa, honestly" -> head is 8 words and is not suppressed).
    if "," in low:
        head, _, tail = low.partition(",")
        if len(head.split()) <= 4 and len(tail.split()) >= 8:
            return False
    words = re.findall(r"[a-z]+", low.rstrip(".!? ").strip())
    if not words:
        return False
    n = len(words)
    f = words[0]
    if " ".join(words) in PROMPTS:
        return True
    if f in WH:
        if f == "what" and n > 1 and words[1] in ("a", "an"):
            return False
        if f == "when":
            return True if n <= 3 else (n > 1 and words[1] in AUX)
        if f == "which" and n > 1 and words[1] in AUX:
            return False
        return True
    if f in AUX:
        if n > 1 and words[1] in ("a", "an", "the") and f in ("do", "have", "did"):
            return False
        if n > 1 and (words[1] in SUBJ or words[1] in ("any", "much", "many", "long", "far", "old", "often")):
            return True
        return False
    if f in PREP and n > 1 and words[1] in WH:
        return True
    if f == "you" and 2 <= n <= 5 and words[1] in YOU_Q:
        return True
    if f in ADJ_NOUN and 2 <= n <= 3 and words[1] in NOUNS:
        return True
    if f in ANY_OPEN and 2 <= n <= 4 and words[1] in ("new", "else", "wrong", "good",
                                                      "ok", "okay", "fun", "exciting",
                                                      "interesting", "happening", "going"):
        return True
    return False


def fix_line(line):
    """(new_line, [texts_marked]) -- [] when the line is already compliant."""
    rec = json.loads(line)
    marked = []
    for turn in rec.get("turns", []):
        txt = turn["text"].strip()
        if txt.endswith("?") or "?" in txt or txt.endswith("!") or txt.endswith("."):
            # Verified 2026-09-16: no question in this corpus ends with a full
            # stop. Every '.'-ending turn that opens with a wh-word or auxiliary
            # is an imperative ("do it.", "have one.", "will do.") or an
            # exclamation ("what a day.", "must be nice."). Leave them alone.
            continue
        if asks(txt):
            turn["text"] = txt + "?"
            marked.append(txt)
    if not marked:
        return line, []
    return json.dumps(rec, ensure_ascii=True), marked


def main():
    fix = "--fix" in sys.argv
    files = sorted(f for f in os.listdir(RAW)
                   if f.startswith("small_talk_") and f.endswith(".jsonl"))
    if not files:
        print("no corpus files in", RAW)
        return 1

    total = 0
    report = {}
    ctx = ar.Lock(ar.LOCK_PATH) if fix else None
    if ctx:
        ctx.__enter__()
    try:
        for fn in files:
            path = os.path.join(RAW, fn)
            with open(path, encoding="utf-8", newline="") as f:
                raw = f.read()
            lines = raw.split("\r\n")
            trailing = lines.pop() if lines[-1] == "" else None

            out, hits, rows = [], [], 0
            for line in lines:
                if not line:
                    out.append(line)
                    continue
                new, marked = fix_line(line)
                if marked:
                    rows += 1
                    hits.extend(marked)
                out.append(new)
            assert len(out) == len(lines), f"{fn}: line count changed"
            report[fn] = (rows, hits)
            total += len(hits)

            if fix and hits:
                os.makedirs(BACKUP, exist_ok=True)
                shutil.copy2(path, os.path.join(BACKUP, fn))
                tmp = path + ".qmark.tmp"
                with open(tmp, "w", encoding="utf-8", newline="") as f:
                    f.write("\r\n".join(out) + ("\r\n" if trailing is not None else ""))
                os.replace(tmp, path)
    finally:
        if ctx:
            ctx.__exit__(None, None, None)

    print(f"{'FIXED' if fix else 'REPORT'} -- {len(files)} file(s)")
    for fn, (rows, hits) in report.items():
        print(f"  {fn:34s} {rows:5d} rows, {len(hits):5d} turn(s) unmarked")
    print(f"\ntotal unmarked questions: {total}")
    if total:
        c = Counter()
        for _, hits in report.values():
            c.update(hits)
        for k, v in c.most_common(40):
            print(f"   {v:3d}  {k!r}")
    if fix and total:
        print(f"\nbackup -> {BACKUP}")
    if not fix and total:
        print("\nre-run with --fix to mark them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
