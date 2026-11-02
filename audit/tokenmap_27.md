# synth2 token-attractor map

Generated 2026-10-15 06:18  |  corpus 4126 rows, **6170 assistant turns**, 6170 user turns
Probe: `probe_out27_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T04:25:10

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.3% | +0.2 |
| `the`-opener (user) | 10.5% | 11.2% | +0.7 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | - | 12% | - | 18x |
| `i have been` | - | 8% | - | 47x |
| `a good` | - | 8% | - | 6x |
| `no plans` | - | 5% | - | 34x |
| `a new` | 5% | 7% | 6x | 9x |
| `the rain` | - | 5% | - | 11x |
| `a real` | - | 7% | - | 4x |
| `like it` | - | 3% | - | 26x |
| `it's a` | - | 3% | - | 26x |
| `on a` | - | 5% | - | 6x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.3% | < 12% |
| `the`-opener (user) | 11.2% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 45 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a bit` | 40 | 64.8 | 51.9 | 12% | 18x | casual 39, lazy 1 |
| `i have been` | 11 | 17.8 | 25.9 | 8% | 47x | casual 9, lazy 2 |
| `a good` | 85 | 137.8 | 17.8 | 8% | 6x | casual 69, lazy 16 |
| `no plans` | 9 | 14.6 | 1.6 | 5% | 34x | casual 7, lazy 2 |
| `a new` | 48 | 77.8 | 84.3 | 7% | 9x | casual 37, lazy 11 |
| `the rain` | 29 | 47.0 | 34.0 | 5% | 11x | casual 21, lazy 8 |
| `a real` | 97 | 157.2 | 71.3 | 7% | 4x | casual 82, lazy 10, angry 5 |
| `like it` | 8 | 13.0 | 22.7 | 3% | 26x | casual 8 |
| `it's a` | 8 | 13.0 | 27.6 | 3% | 26x | casual 8 |
| `on a` | 56 | 90.8 | 55.1 | 5% | 6x | casual 37, lazy 17, angry 2 |
| `with the` | 66 | 107.0 | 87.5 | 5% | 5x | casual 54, lazy 12 |
| `did you` | 197 | 319.3 | 398.7 | 7% | 2x | casual 192, lazy 5 |
| `i do` | 12 | 19.4 | 16.2 | 3% | 17x | lazy 7, casual 5 |
| `how did the` | 12 | 19.4 | 11.3 | 3% | 17x | casual 12 |
| `an early` | 13 | 21.1 | 4.9 | 3% | 16x | casual 11, lazy 2 |
| `get it` | 14 | 22.7 | 3.2 | 3% | 15x | casual 11, lazy 3 |
| `i've been` | 15 | 24.3 | 25.9 | 3% | 14x | casual 15 |
| `yeah the` | 17 | 27.6 | 3.2 | 3% | 12x | casual 16, lazy 1 |
| `doing the` | 17 | 27.6 | 17.8 | 3% | 12x | casual 15, angry 1, lazy 1 |
| `bit of` | 17 | 27.6 | 14.6 | 3% | 12x | casual 17 |
| `have a` | 18 | 29.2 | 21.1 | 3% | 11x | casual 11, lazy 7 |
| `for a` | 104 | 168.6 | 123.2 | 5% | 3x | casual 74, lazy 23, angry 7 |
| `the weather` | 21 | 34.0 | 17.8 | 3% | 10x | casual 18, lazy 3 |
| `to the` | 108 | 175.0 | 173.4 | 5% | 3x | casual 75, lazy 32, angry 1 |
| `this year` | 24 | 38.9 | 76.2 | 3% | 9x | casual 23, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 8 | 16.2 | casual 8 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `at this point` | 3 | 9 | 14.0 | lazy 5, casual 4 |
| `best kind of` | 3 | 9 | 13.9 | casual 8, lazy 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the post office` | 3 | 8 | 13.2 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.4 | casual 9, lazy 2 |
| `for an hour` | 3 | 9 | 12.3 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `a couple of` | 3 | 11 | 11.6 | casual 11 |
| `how long did` | 3 | 9 | 11.5 | casual 9 |
| `did you find` | 3 | 9 | 11.4 | casual 9 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `the best kind` | 3 | 12 | 11.2 | casual 12 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `what did you` | 3 | 27 | 10.4 | casual 26, lazy 1 |
| `a lot of` | 3 | 10 | 10.3 | casual 7, lazy 3 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `are you going` | 3 | 15 | 10.1 | casual 15 |
| `makes the whole` | 3 | 9 | 10.0 | lazy 6, casual 3 |
| `earn their` | 2 | 15 | 10.0 | lazy 14, casual 1 |
| `did you go` | 3 | 13 | 10.0 | casual 13 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 2 | casual 39, lazy 1 |
| `i have been` | 2 | casual 9, lazy 2 |
| `a good` | 2 | casual 69, lazy 16 |
| `no plans` | 2 | casual 7, lazy 2 |
| `a new` | 2 | casual 37, lazy 11 |
| `the rain` | 2 | casual 21, lazy 8 |
| `a real` | 3 | casual 82, lazy 10, angry 5 |
| `like it` | 1 | casual 8 |
| `it's a` | 1 | casual 8 |
| `on a` | 3 | casual 37, lazy 17, angry 2 |
| `with the` | 2 | casual 54, lazy 12 |
| `did you` | 2 | casual 192, lazy 5 |
| `i do` | 2 | lazy 7, casual 5 |
| `how did the` | 1 | casual 12 |
| `an early` | 2 | casual 11, lazy 2 |
| `get it` | 2 | casual 11, lazy 3 |
| `i've been` | 1 | casual 15 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `doing the` | 3 | casual 15, angry 1, lazy 1 |
| `bit of` | 1 | casual 17 |
| `have a` | 2 | casual 11, lazy 7 |
| `for a` | 3 | casual 74, lazy 23, angry 7 |
| `the weather` | 2 | casual 18, lazy 3 |
| `to the` | 3 | casual 75, lazy 32, angry 1 |
| `this year` | 2 | casual 23, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=6170): a 7.4%, the 3.3%, that 2.5%, haha 2.2%, i 1.8%, did 1.0%
- assistant pos 1 (n=6170): the 8.9%, a 2.4%, is 2.2%, you 1.4%, it 1.2%, and 1.0%
- assistant pos 2 (n=6169): the 5.9%, is 4.1%, are 2.7%, a 2.3%, of 1.6%, for 1.3%
- assistant pos last (n=6170): it 5.1%, now 1.6%, time 1.4%, one 1.2%, again 1.0%, you 0.9%
- user pos 0 (n=6170): the 11.2%, my 8.3%, i 7.6%, our 6.7%, did 4.2%, we 3.0%
- user pos 1 (n=6107): the 5.0%, you 3.7%, a 2.9%, was 1.6%, did 1.6%, is 1.5%
- user pos 2 (n=6018): the 7.4%, a 3.2%, is 2.6%, you 2.1%, and 1.8%, has 1.2%
- user pos last (n=6170): again 2.7%, it 2.0%, week 1.6%, now 1.5%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **7.1%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 2155 |

