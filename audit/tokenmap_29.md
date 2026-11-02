# synth2 token-attractor map

Generated 2026-10-15 12:25  |  corpus 4374 rows, **6438 assistant turns**, 6438 user turns
Probe: `probe_out29_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T08:45:31

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.2% | 3.1% | -0.1 |
| `the`-opener (user) | 11.4% | 11.4% | +0.0 |
| copula-only | 0.6% | 0.5% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `to do` | - | 7% | - | 19x |
| `is gone` | - | 5% | - | 40x |
| `new place` | - | 5% | - | 36x |
| `a bit` | - | 7% | - | 11x |
| `you got` | - | 5% | - | 15x |
| `have you` | - | 7% | - | 4x |
| `do it` | - | 5% | - | 9x |
| `it the` | - | 5% | - | 8x |
| `the new` | - | 5% | - | 7x |
| `the worst` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.1% | < 12% |
| `the`-opener (user) | 11.4% | n/a |
| copula-only turns | 0.5% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 39 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `to do` | 23 | 35.7 | 35.7 | 7% | 19x | casual 21, angry 1, lazy 1 |
| `is gone` | 8 | 12.4 | 4.7 | 5% | 40x | lazy 5, casual 2, angry 1 |
| `new place` | 9 | 14.0 | 9.3 | 5% | 36x | casual 7, lazy 2 |
| `a bit` | 40 | 62.1 | 49.7 | 7% | 11x | casual 39, lazy 1 |
| `you got` | 22 | 34.2 | 7.8 | 5% | 15x | casual 21, angry 1 |
| `have you` | 101 | 156.9 | 37.3 | 7% | 4x | casual 80, angry 21 |
| `do it` | 35 | 54.4 | 10.9 | 5% | 9x | casual 24, lazy 11 |
| `it the` | 38 | 59.0 | 17.1 | 5% | 8x | casual 34, lazy 4 |
| `the new` | 47 | 73.0 | 82.3 | 5% | 7x | casual 35, lazy 11, angry 1 |
| `the worst` | 48 | 74.6 | 10.9 | 5% | 7x | casual 26, lazy 17, angry 5 |
| `for a week` | 8 | 12.4 | 14.0 | 3% | 27x | casual 4, lazy 3, angry 1 |
| `nothing on` | 9 | 14.0 | 1.6 | 3% | 24x | casual 8, lazy 1 |
| `you get` | 57 | 88.5 | 79.2 | 5% | 6x | casual 49, lazy 5, angry 3 |
| `feels like` | 12 | 18.6 | 4.7 | 3% | 18x | casual 8, lazy 4 |
| `the same` | 70 | 108.7 | 77.7 | 5% | 5x | casual 36, lazy 29, angry 5 |
| `the neighbor` | 13 | 20.2 | 7.8 | 3% | 17x | casual 9, lazy 3, angry 1 |
| `you going` | 17 | 26.4 | 7.8 | 3% | 13x | casual 15, angry 2 |
| `bit of` | 17 | 26.4 | 14.0 | 3% | 13x | casual 17 |
| `is it` | 102 | 158.4 | 34.2 | 5% | 3x | casual 100, angry 2 |
| `like that` | 21 | 32.6 | 3.1 | 3% | 10x | casual 17, angry 3, lazy 1 |
| `enjoy the` | 21 | 32.6 | 0.0 | 3% | 10x | casual 13, lazy 8 |
| `this morning` | 22 | 34.2 | 104.1 | 3% | 10x | casual 21, lazy 1 |
| `it is` | 115 | 178.6 | 74.6 | 5% | 3x | casual 79, lazy 36 |
| `going to` | 25 | 38.8 | 21.7 | 3% | 9x | casual 18, lazy 5, angry 2 |
| `is the` | 378 | 587.1 | 105.6 | 7% | 1x | casual 251, lazy 116, angry 11 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `have you tried` | 3 | 20 | 13.7 | casual 15, angry 5 |
| `the front desk` | 3 | 8 | 13.2 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.1 | casual 7, lazy 1 |
| `for an hour` | 3 | 9 | 12.3 | casual 8, lazy 1 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `how long did` | 3 | 12 | 11.6 | casual 9, angry 3 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `a lot of` | 3 | 10 | 10.3 | casual 7, lazy 3 |
| `group chat` | 2 | 8 | 10.2 | lazy 4, angry 2, casual 2 |
| `do you go` | 3 | 8 | 10.1 | casual 8 |
| `what did you` | 3 | 27 | 10.1 | casual 26, lazy 1 |
| `earn their` | 2 | 15 | 10.0 | lazy 14, casual 1 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `makes the whole` | 3 | 9 | 9.9 | lazy 6, casual 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `to do` | 3 | casual 21, angry 1, lazy 1 |
| `is gone` | 3 | lazy 5, casual 2, angry 1 |
| `new place` | 2 | casual 7, lazy 2 |
| `a bit` | 2 | casual 39, lazy 1 |
| `you got` | 2 | casual 21, angry 1 |
| `have you` | 2 | casual 80, angry 21 |
| `do it` | 2 | casual 24, lazy 11 |
| `it the` | 2 | casual 34, lazy 4 |
| `the new` | 3 | casual 35, lazy 11, angry 1 |
| `the worst` | 3 | casual 26, lazy 17, angry 5 |
| `for a week` | 3 | casual 4, lazy 3, angry 1 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `you get` | 3 | casual 49, lazy 5, angry 3 |
| `feels like` | 2 | casual 8, lazy 4 |
| `the same` | 3 | casual 36, lazy 29, angry 5 |
| `the neighbor` | 3 | casual 9, lazy 3, angry 1 |
| `you going` | 2 | casual 15, angry 2 |
| `bit of` | 1 | casual 17 |
| `is it` | 2 | casual 100, angry 2 |
| `like that` | 3 | casual 17, angry 3, lazy 1 |
| `enjoy the` | 2 | casual 13, lazy 8 |
| `this morning` | 2 | casual 21, lazy 1 |
| `it is` | 2 | casual 79, lazy 36 |
| `going to` | 3 | casual 18, lazy 5, angry 2 |
| `is the` | 3 | casual 251, lazy 116, angry 11 |

## 4. Opener maps

- assistant pos 0 (n=6438): a 7.4%, the 3.1%, that 2.5%, haha 2.1%, did 1.8%, i 1.7%
- assistant pos 1 (n=6438): the 9.7%, a 2.2%, is 2.2%, you 2.1%, it 1.3%, and 1.0%
- assistant pos 2 (n=6437): the 6.2%, is 3.9%, are 2.6%, a 2.3%, of 1.5%, for 1.2%
- assistant pos last (n=6438): it 5.0%, now 1.6%, time 1.4%, one 1.2%, again 1.1%, you 0.9%
- user pos 0 (n=6438): the 11.4%, my 9.0%, i 7.5%, our 7.0%, did 4.0%, a 3.0%
- user pos 1 (n=6375): the 4.8%, you 3.5%, a 2.8%, was 1.6%, did 1.5%, is 1.4%
- user pos 2 (n=6286): the 7.2%, a 3.1%, is 2.5%, you 2.0%, and 1.7%, has 1.3%
- user pos last (n=6438): again 2.9%, it 2.0%, week 1.6%, now 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.8%**; model outputs: **15.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

