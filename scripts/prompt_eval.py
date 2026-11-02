#!/usr/bin/env python3
"""Prompt-probe the finished synth2 checkpoint with 60 small-talk prompts.

Runs gen_dump ONCE (single model load) with all prompts, saves raw output.
Usage:
  python runs/synth2/scripts/prompt_eval.py [--len 24] [--out runs/synth2/audit/probe_out.txt]

COVERAGE (2026-10-07): 60 prompts, TWO per category, over ALL 30 categories of
the fresh corpus (the old 50-prompt set named only 12 registers, so 18
categories had zero probe coverage). The probe is the drift instrument: the
point is to see whether the model, as the corpus fills, starts answering in the
plain everyday voice -- and does NOT slide back into the old "X is a Y"
aphorism attractor. `tokenmap.py` quantifies that on top of this output.
Scoring is by hand afterwards; the probe verdict is whatever the operator says
it is.
"""
import argparse
import os
import subprocess
import sys

# Repo root, derived from this file's own location (runs/synth2/scripts/ -> root).
REPO = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def repo_path(p):
    """Absolute path; a relative one is taken from the repo root, not the CWD.

    Python's subprocess CANNOT spawn a relative-path exe on Windows -- it raises
    FileNotFoundError [WinError 2] before the model ever loads -- and that has
    now cost two sessions. Nothing here is ever left relative.
    """
    return p if os.path.isabs(p) else os.path.join(REPO, p)

PROMPTS = [
    # (register, family, prompt) -- 2 per category, all 30 categories.
    # 2026-10-11: ghetto register removed by operator order (no slang, plain
    # everyday English only) -> replaced with 2 casual prompts; British
    # vocabulary US-converted (run-15 finding: the probe set was the last
    # British text the model ever sees).
    ("casual", "time+plans", "so what is going on with you this weekend?"),
    ("casual", "weather", "it rained the whole way in today."),
    ("casual", "errands", "i still need to get groceries before the store closes."),
    ("casual", "sleep", "i could not fall asleep until like two last night."),
    ("lazy", "general", "you up to anything today?"),
    ("lazy", "weekend", "the weekend came and went so fast."),
    ("angry", "food", "my order came cold and half missing."),
    ("angry", "parking", "someone took my parking spot again."),
    ("sexy", "flirt", "you have that look in your eyes tonight."),
    ("sexy", "general", "save me a dance later, will you?"),
    ("formal", "weather", "lovely weather we are having this week."),
    ("formal", "general", "how was your commute in this morning?"),
    ("sarcastic", "work", "oh great, another meeting invite."),
    ("sarcastic", "work", "my inbox has two hundred unread emails."),
    ("excited", "news", "guess what, i got the job!"),
    ("excited", "social", "we are going away this weekend!"),
    ("gloomy", "weather", "dark by four again, winter is here."),
    ("gloomy", "general", "nothing good on tv ever anymore."),
    ("anxious", "health", "my heart has been racing since three am."),
    ("anxious", "work", "the review invite has no agenda attached."),
    ("gossip", "neighbors", "did you hear about apartment nine upstairs?"),
    ("gossip", "work", "word is the promotion is already decided."),
    ("nostalgic", "school", "remember the candy store lines at recess?"),
    ("nostalgic", "summers", "summers felt longer back then, right?"),
    ("philosophical", "time", "do you ever wonder why time speeds up as you get older?"),
    ("philosophical", "life", "what do you think actually matters in the end?"),
    ("teasing", "appearance", "nice haircut, did you do it yourself?"),
    ("teasing", "habits", "you have been on that phone all day, haven't you?"),
    ("supportive", "hard day", "i am having a really rough week."),
    ("supportive", "bad news", "i did not get the job, i am crushed."),
    ("bored", "nothing to do", "i am so bored i have cleaned the whole apartment."),
    ("bored", "evening", "there is nothing to do tonight."),
    ("curious", "follow-up", "what did you end up doing about the car?"),
    ("curious", "people", "how did you two actually meet?"),
    ("deflecting", "dodge", "did you ever send that message?"),
    ("deflecting", "dodge", "so, about that thing we talked about."),
    ("ranting", "commute", "my bus was late again and then the driver just sat there."),
    ("ranting", "delivery", "three parcels lost this month, three."),
    ("flirty", "banter", "you are trouble, you know that?"),
    ("flirty", "drinks", "buy me a drink and i might forgive you."),
    ("sullen", "withdrawn", "fine."),
    ("sullen", "withdrawn", "whatever, it does not matter."),
    ("celebratory", "win", "we finally finished the project!"),
    ("celebratory", "win", "i passed my driving test first time!"),
    ("confused", "lost", "wait, so who is actually in charge?"),
    ("confused", "lost", "sorry, i do not follow, say that again?"),
    ("petty", "grudge", "she still owes me twenty bucks from march."),
    ("petty", "grudge", "i am not inviting him, not after last time."),
    ("weird", "offbeat", "i just sneezed and my lamp turned off, that is not normal."),
    ("weird", "offbeat", "my toast came out shaped like a face."),
    ("greetings", "hello", "morning! how are you?"),
    ("greetings", "hello", "hey, long time no see!"),
    ("dont_know", "shrug", "no idea, honestly."),
    ("dont_know", "shrug", "i have no clue, sorry."),
    ("thanks", "gratitude", "thanks so much for the other day."),
    ("thanks", "gratitude", "that was really kind of you, thank you."),
    ("apology", "sorry", "sorry i am late, the traffic was awful."),
    ("apology", "sorry", "my bad, i completely forgot."),
    ("goodbye", "farewell", "right, i am off, see you later."),
    ("goodbye", "farewell", "anyway, i should go, take care!"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--len", type=int, default=24)
    ap.add_argument("--ckpt", default="runs/synth2/best.bin")
    ap.add_argument("--data", default="runs/synth2")
    ap.add_argument("--out", default="runs/synth2/audit/probe_out.txt")
    ap.add_argument("--exe", default="target/release/gen_dump.exe")
    args = ap.parse_args()

    args.exe = repo_path(args.exe)
    args.data = repo_path(args.data)
    args.ckpt = repo_path(args.ckpt)
    args.out = repo_path(args.out)

    # Fail with the actual path rather than WinError 2 from deep inside subprocess.
    for label, path in (("exe", args.exe), ("ckpt", args.ckpt)):
        if not os.path.exists(path):
            sys.exit(f"{label} not found: {path}\n"
                     f"(build with: cargo build --release)")

    # The fresh start removed runs/synth2/audit/, and this script never created
    # its own --out dir, so the documented probe command used to crash on a
    # fresh corpus with FileNotFoundError on open(). Create it here.
    out_dir = os.path.dirname(args.out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Probing mid-train reads a moving checkpoint -- see CONTINUE.md section 5
    # step 6. This is a warning, not a block: the operator owns that call.
    print(f"probing {args.ckpt} -- confirm no train.exe is running on this data dir")

    assert len(PROMPTS) == 60, f"want exactly 60 prompts, have {len(PROMPTS)}"
    cmd = [args.exe, "--data", args.data, "--ckpt", args.ckpt,
           "--len", str(args.len)]
    for _, _, p in PROMPTS:
        cmd += ["--prompt", p]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        print(r.stderr[-3000:], file=sys.stderr)
        sys.exit(1)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(f"# synth2 prompt probe: {len(PROMPTS)} prompts, ckpt={args.ckpt}\n\n")
        for (reg, fam, p), block in zip(PROMPTS, r.stdout.split("PROMPT: ")[1:]):
            f.write(f"## [{reg} / {fam}] {p}\n{block.strip()}\n\n")
    print(f"wrote {args.out} ({len(PROMPTS)} prompt outputs)")


if __name__ == "__main__":
    main()
