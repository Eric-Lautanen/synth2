# synth2 continuation prompt (FRESH START 2026-10-07; laws lifted 2026-10-10 22:11 UTC)

You are working on `synth2`, the everyday small-talk corpus. Read this
file, then `README.md` in this folder (the project's memory -- run ledger,
curation log, instruments, findings). The corpus was wiped on 2026-10-07 and
rebuilt from zero; on 2026-10-10 the operator lifted every rule: **there are
no laws. The only thing that matters is a good resulting model. Nothing is
static -- any method may be modified if it gets us a good English-speaking
model.** What follows is the current best-known method, not a constraint.

**Goal: a good English-speaking conversational model** -- one that holds a
natural everyday conversation (plain everyday English, questions answered,
follow-ups asked, natural endings). Small parameter count is a preference we
keep when we can, not a constraint. Two things the evidence says matter most:
make the model UNDERSTAND its input, and give it enough data that its
conditional next-word distribution is sharp (run-13 diagnosis: the corpus
is ~10x smaller than the model -- DATA is the binding constraint).

## 1. THE TARGET VOICE (what "good" sounds like)

**Plain, direct, straightforward everyday English. The words a normal person
actually types to a friend.**

- NO metaphors as statements ("a rattle is a confession"), aphorisms,
  fortune-cookie closers, "X is Y" riddle frames, poetic or cryptic prose,
  bible-like cadence. (The 2026-10-07 wipe happened because the old corpus
  taught exactly this voice.)
- A reply answers, asks a follow-up, jokes plainly, agrees, or sympathises --
  in ordinary words, then stops. Natural flow, natural ENDING.
- **NO SLOP (operator, 2026-10-11).** No stilted rewrites, no meme-speak, no
  mechanical template shapes, no dataset text, no slang. Every row must
  read like a real person typed it to a friend. Slow going is fine -- the
  harness runs for weeks or months with session handoffs -- as long as it
  is going and the data is high quality. No drift, no slop. Good curation
  and thoughtful row adding are the whole method.
- The test per turn: could this exact sentence appear in a real chat log? If
  not, rewrite it. Cleverness is the failure mode; ordinariness is the target.

Good: "ugh same. i gave up on that form and just called them instead."
Bad: "the form is a machine that wants to know you and never meet you."

## 2. The working method (all modifiable)

- **Data sources are OPEN.** Hand-written rows were the 2026-10-07..10
  method and remain the quality benchmark; synthetic data, augmentation,
  paraphrase, and distillation are now PERMITTED -- any source is fine if
  the text is good and the model gets better. Judge by the instruments
  (probe, tokenmap, gates), not provenance.
- **Depth first.** Attach rows to scenarios the file already has; more
  exchanges and reply shapes on existing scenarios is the highest-value
  work. Breadth is no longer banned -- add it when it serves the goal.
- **One file at a time** (the current file below). 2000 rows is a base, not
  a cap. `--category <name> --force` writes out of order on purpose.
- **Append through the script** (the door into `raw/`):
  `python runs/synth2/scripts/add_rows.py --rows-file <file> --by <your-name>`
  Rows as pipe lines (one row per line: `user | assistant | user | assistant`)
  or as a JSON list of `{"turns": [["user", "..."], ["assistant", "..."]]}`.
  Do NOT pass `--force` for normal work. `--by` is required.
- **Quality gates after every batch** (instruments, not rituals -- run them
  while they catch real defects): `repair --locations` (0 dups / 0 near dups),
  `integrity.py` (a DRIFT flag is a finder: hand-read it), `qmark.py`.
- **Scratch hygiene:** write batch files OUTSIDE runs/synth2 (project root
  tmp_* is fine), delete them after the append.
- **Say it:** one short post in the room per batch -- what landed, what did not.
  The room server (`http://127.0.0.1:5757`, room `synth2`) protocol is in
  README.md ("THE ROOM") -- ACCESS IT WITH CURL (operator 2026-10-24): auth
  once (POST /auth, keep the `agent_token` for the `X-Agent-Token` header),
  read before acting (GET /messages, keep the `X-Post-Token` header), post
  with both headers (POST /send), claim shared files before editing them.
- **FRAME FINDING (run-11):** when a reply echoes the user's noun, VARY the
  frame -- never open "the <noun>..." by default (the rewrite campaign
  over-used it, corpus the-opener hit 13.4%, and the model followed over the
  12% ceiling). Use a bare noun ("printer jamming again?"), a contraction
  ("boiler's sorted"), a verb-first ("coming along nicely"), or a question.
- **CONDITIONING SHAPE (run-10 design finding):** a tiny model can only
  learn input-dependence it can SEE -- lexical echo is the learnable signal
  at this size. Replies ECHO the user's specific noun, at MEDIUM length
  (~10-13 words), in VARIED frames. Corpus zero-overlap went 66.9% -> 5.5%
  on this shape and the swap arm rose monotonically 1.68 -> 3.75 -> 4.67.

## 3. Status table (count cells maintained by add_rows.py -- do not hand-edit)

| # | file | rows | status |
|---|---|---|---|
| 1 | small_talk_casual.jsonl | 2001 | complete -- warm everyday chat (conditioning campaign done: 5.5% zero) |
| 2 | small_talk_lazy.jsonl | 2001 | complete -- minimum-effort chat |
| 3 | small_talk_angry.jsonl | 2000 | complete -- venting, snapping, rants |
| 4 | small_talk_sexy.jsonl | 2046 | complete -- flirtation, innuendo, adults only |
| 5 | small_talk_formal.jsonl | 1677 | CURRENT -- stiff office niceties |
| 6 | small_talk_sarcastic.jsonl | 0 | deadpan snark |
| 7 | small_talk_excited.jsonl | 0 | good news, big energy |
| 8 | small_talk_gloomy.jsonl | 0 | gray-day commiseration |
| 9 | small_talk_anxious.jsonl | 0 | overthinking out loud |
| 10 | small_talk_gossip.jsonl | 0 | did-you-hear energy |
| 11 | small_talk_nostalgic.jsonl | 0 | remember-whens |
| 12 | small_talk_philosophical.jsonl | 0 | shower thoughts in PLAIN words |
| 13 | small_talk_teasing.jsonl | 0 | roasting people you love |
| 14 | small_talk_supportive.jsonl | 0 | small kind words |
| 15 | small_talk_bored.jsonl | 0 | boredom talking to boredom |
| 16 | small_talk_curious.jsonl | 0 | follow-up questions as a lifestyle |
| 17 | small_talk_deflecting.jsonl | 0 | dodging with charm, plainly |
| 18 | small_talk_ranting.jsonl | 0 | the monologue, listener says right?? |
| 19 | small_talk_flirty.jsonl | 0 | light banter, the game of it |
| 20 | small_talk_sullen.jsonl | 0 | one-word walls, fine. |
| 21 | small_talk_celebratory.jsonl | 0 | congrats, small wins as championships |
| 22 | small_talk_confused.jsonl | 0 | wait, what |
| 23 | small_talk_petty.jsonl | 0 | grudge sports, keeping count |
| 24 | small_talk_weird.jsonl | 0 | mildly cursed observations, plain words |
| 25 | small_talk_greetings.jsonl | 0 | hellos, no names |
| 26 | small_talk_dont_know.jsonl | 0 | the honest shrug |
| 27 | small_talk_thanks.jsonl | 0 | gratitude and its receipt |
| 28 | small_talk_apology.jsonl | 0 | sorry, my bad, and moving on |
| 29 | small_talk_goodbye.jsonl | 0 | signing off warmly |

**The ghetto register was REMOVED by operator order (2026-10-11): no slang,
plain straightforward everyday English only.** `small_talk_ghetto.jsonl` is
deleted from raw/ and the category is gone from `add_rows.py` and the probe.

Tones are fixed per file (see `scripts/add_rows.py` CATEGORIES). The current
file is the first one under 2000 rows.

## 4. The loop (detail in README.md)

1. ADD rows to the CURRENT file (or generate/augment them -- sources are
   open; quality is judged by the instruments). Gate after every batch.
2. GATES: `repair --locations`, `integrity.py`, `qmark.py`.
3. TRAIN in background -- the CURRENT DEFAULT COMMAND (modifiable when a
   better configuration is measured; until then copy verbatim so runs stay
   comparable):
   `target\release\train.exe --data runs\synth2 --loss-log runs/synth2/loss.log --capture runs/synth2/capture.bin --log-every 500 --register-col 4 --select patience --gen-bar 0.050 --no-dyn-steps`
   - `--select patience` picks the checkpoint on heldout GENERATION overlap,
     not heldout loss: on this corpus the two DISSOCIATE (the checkpoint
     finding, README.md).
   - `--gen-bar 0.050` is the run-9 latch fix -- do not omit it casually.
   - **HOW TO LAUNCH HERE:** `schtasks.exe` is blacklisted and a
     `Start-Process` child is reaped -- use the agent's background runner,
     then VERIFY: `train_stdout.log` GROWING + `train.pid` present.
4. While it trains, prepare the next data.
5. EVAL when it ends -- three instruments, exact commands:
   1. `python runs/synth2/scripts/prompt_eval.py --exe target/release/gen_dump.exe --out runs/synth2/audit/probe_outN.txt`
      (60 prompts; ALSO probe `--ckpt runs/synth2/final.bin --out .../probe_outN_final.txt`).
   2. `python reference/turn_delta.py --data runs/synth2 --ckpt runs/synth2/best.bin --register-col 4`
   3. `python runs/synth2/scripts/tokenmap.py --md runs/synth2/audit/tokenmap_N.md --json runs/synth2/audit/tokenmap_N.json --compare runs/synth2/audit/tokenmap_{N-1}.json`
   Plus the Phase-0 diagnostics (README.md run-13 line): `gen_dump --topk N
   --escape` for per-step top-k/entropy/escape-mass, and the neuron sweep
   (`eval/src/bin/neuron_sweep.rs`).
6. RECORD one line in the RUN LEDGER (README.md). No archives, no backups.
7. Repeat.

**The other lever -- EDIT in place.** Adding is half the loop; fixing the rows
already there is the other half (fix at the core, never dilute). Status lives
in `add_rows.py --status`, NOT in this file's table. The safe in-place editor
(`scripts/apply_rewrites.py`), the conditioning metric
(`scripts/conditioning.py`), and the whole-file audit are in README.md
("THE OTHER LEVER"); record each pass in the CORPUS CURATION LOG.
