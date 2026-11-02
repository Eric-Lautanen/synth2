# synth2 token-attractor map

Generated 2026-10-17 18:06  |  corpus 6312 rows, **8532 assistant turns**, 8532 user turns
Probe: `probe_out47_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T15:06:39

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | -0.0 |
| `the`-opener (user) | 13.3% | 13.3% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `you get` | - | 7% | - | 10x |
| `did you` | - | 8% | - | 3x |
| `way to` | - | 5% | - | 13x |
| `time for` | - | 3% | - | 32x |
| `for a` | - | 7% | - | 3x |
| `to get` | - | 3% | - | 28x |
| `the work` | - | 3% | - | 20x |
| `a bit of` | - | 3% | - | 20x |
| `with the` | - | 5% | - | 5x |
| `still a` | 3% | 3% | 19x | 19x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 13.3% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 35 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `you get` | 59 | 69.2 | 59.8 | 7% | 10x | casual 49, angry 5, lazy 5 |
| `did you` | 236 | 276.6 | 289.5 | 8% | 3x | casual 192, angry 28, sexy 11 |
| `way to` | 34 | 39.8 | 2.3 | 5% | 13x | casual 17, angry 11, lazy 6 |
| `time for` | 9 | 10.5 | 2.3 | 3% | 32x | casual 6, lazy 2, sexy 1 |
| `for a` | 191 | 223.9 | 178.2 | 7% | 3x | angry 93, casual 72, lazy 23 |
| `to get` | 10 | 11.7 | 10.5 | 3% | 28x | casual 7, lazy 2, angry 1 |
| `the work` | 14 | 16.4 | 3.5 | 3% | 20x | lazy 8, casual 5, angry 1 |
| `a bit of` | 14 | 16.4 | 9.4 | 3% | 20x | casual 14 |
| `with the` | 88 | 103.1 | 73.8 | 5% | 5x | casual 55, angry 18, lazy 12 |
| `still a` | 15 | 17.6 | 3.5 | 3% | 19x | casual 8, lazy 4, sexy 2 |
| `i would` | 16 | 18.8 | 4.7 | 3% | 18x | casual 8, angry 4, lazy 2 |
| `is the whole` | 19 | 22.3 | 3.5 | 3% | 15x | casual 8, lazy 7, angry 4 |
| `all week` | 20 | 23.4 | 23.4 | 3% | 14x | casual 13, angry 4, lazy 3 |
| `all the` | 20 | 23.4 | 8.2 | 3% | 14x | casual 10, angry 8, lazy 2 |
| `a phone` | 22 | 25.8 | 11.7 | 3% | 13x | angry 10, casual 6, lazy 5 |
| `this morning` | 24 | 28.1 | 79.7 | 3% | 12x | casual 21, angry 2, lazy 1 |
| `it for` | 26 | 30.5 | 15.2 | 3% | 11x | casual 18, lazy 7, sexy 1 |
| `get the` | 28 | 32.8 | 21.1 | 3% | 10x | casual 17, lazy 8, angry 2 |
| `a small` | 33 | 38.7 | 11.7 | 3% | 9x | lazy 16, casual 13, angry 4 |
| `this week` | 34 | 39.8 | 53.9 | 3% | 8x | casual 26, angry 4, lazy 4 |
| `do it` | 35 | 41.0 | 8.2 | 3% | 8x | casual 24, lazy 11 |
| `at the` | 205 | 240.3 | 226.2 | 5% | 2x | casual 104, lazy 52, angry 38 |
| `does it` | 55 | 64.5 | 4.7 | 3% | 5x | casual 44, lazy 5, angry 4 |
| `and i` | 57 | 66.8 | 96.1 | 3% | 5x | casual 29, lazy 25, sexy 3 |
| `worth it` | 60 | 70.3 | 10.5 | 3% | 5x | casual 42, lazy 15, sexy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.2 | casual 10, lazy 1 |
| `at this point` | 3 | 11 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.2 | angry 6, casual 2, lazy 2 |
| `fell asleep` | 2 | 8 | 11.9 | casual 4, lazy 4 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 11 | 11.6 | casual 8, angry 1, lazy 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.4 | casual 11, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.7 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `did you` | 4 | casual 192, angry 28, sexy 11, lazy 5 |
| `way to` | 3 | casual 17, angry 11, lazy 6 |
| `time for` | 3 | casual 6, lazy 2, sexy 1 |
| `for a` | 4 | angry 93, casual 72, lazy 23, sexy 3 |
| `to get` | 3 | casual 7, lazy 2, angry 1 |
| `the work` | 3 | lazy 8, casual 5, angry 1 |
| `a bit of` | 1 | casual 14 |
| `with the` | 4 | casual 55, angry 18, lazy 12, sexy 3 |
| `still a` | 4 | casual 8, lazy 4, sexy 2, angry 1 |
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `is the whole` | 3 | casual 8, lazy 7, angry 4 |
| `all week` | 3 | casual 13, angry 4, lazy 3 |
| `all the` | 3 | casual 10, angry 8, lazy 2 |
| `a phone` | 4 | angry 10, casual 6, lazy 5, sexy 1 |
| `this morning` | 3 | casual 21, angry 2, lazy 1 |
| `it for` | 3 | casual 18, lazy 7, sexy 1 |
| `get the` | 4 | casual 17, lazy 8, angry 2, sexy 1 |
| `a small` | 3 | lazy 16, casual 13, angry 4 |
| `this week` | 3 | casual 26, angry 4, lazy 4 |
| `do it` | 2 | casual 24, lazy 11 |
| `at the` | 4 | casual 104, lazy 52, angry 38, sexy 11 |
| `does it` | 4 | casual 44, lazy 5, angry 4, sexy 2 |
| `and i` | 3 | casual 29, lazy 25, sexy 3 |
| `worth it` | 4 | casual 42, lazy 15, sexy 2, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=8532): a 8.0%, the 3.0%, did 2.6%, how 2.4%, was 2.0%, that 2.0%
- assistant pos 1 (n=8532): the 11.7%, a 2.4%, is 2.0%, you 2.0%, does 1.4%, your 1.1%
- assistant pos 2 (n=8531): the 6.3%, a 3.1%, is 3.0%, are 2.0%, of 1.7%, for 1.7%
- assistant pos last (n=8532): it 4.2%, now 1.4%, time 1.3%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8532): the 13.3%, my 10.6%, our 8.1%, i 6.7%, they 3.3%, we 3.2%
- user pos 1 (n=8469): the 3.8%, you 2.7%, a 2.2%, was 1.3%, did 1.2%, is 1.1%
- user pos 2 (n=8380): the 6.7%, a 3.0%, is 2.0%, you 1.7%, my 1.5%, and 1.4%
- user pos last (n=8532): again 2.6%, it 1.9%, now 1.5%, week 1.4%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.2%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 335 |
| lazy | 1 / 2155 |

