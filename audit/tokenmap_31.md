# synth2 token-attractor map

Generated 2026-10-15 16:14  |  corpus 4560 rows, **6639 assistant turns**, 6639 user turns
Probe: `probe_out31_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T14:30:14

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.2% | 3.2% | -0.0 |
| `the`-opener (user) | 11.7% | 11.9% | +0.2 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `part of` | - | 7% | - | 18x |
| `i have` | - | 7% | - | 9x |
| `on the` | - | 8% | - | 3x |
| `do it` | - | 5% | - | 9x |
| `the end` | - | 5% | - | 9x |
| `of the` | - | 7% | - | 3x |
| `out of` | - | 5% | - | 6x |
| `to get` | - | 3% | - | 22x |
| `it's been` | - | 3% | - | 22x |
| `early night` | - | 3% | - | 18x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.2% | < 12% |
| `the`-opener (user) | 11.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 40 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `part of` | 24 | 36.2 | 4.5 | 7% | 18x | lazy 13, casual 11 |
| `i have` | 47 | 70.8 | 96.4 | 7% | 9x | casual 35, lazy 12 |
| `on the` | 217 | 326.9 | 298.2 | 8% | 3x | casual 151, lazy 51, angry 15 |
| `do it` | 35 | 52.7 | 10.5 | 5% | 9x | casual 24, lazy 11 |
| `the end` | 38 | 57.2 | 37.7 | 5% | 9x | casual 26, lazy 7, angry 5 |
| `of the` | 135 | 203.3 | 131.0 | 7% | 3x | casual 84, lazy 39, angry 12 |
| `out of` | 55 | 82.8 | 79.8 | 5% | 6x | casual 34, lazy 14, angry 7 |
| `to get` | 10 | 15.1 | 12.1 | 3% | 22x | casual 7, lazy 2, angry 1 |
| `it's been` | 10 | 15.1 | 7.5 | 3% | 22x | casual 10 |
| `early night` | 12 | 18.1 | 4.5 | 3% | 18x | casual 11, lazy 1 |
| `is fine` | 13 | 19.6 | 6.0 | 3% | 17x | casual 8, lazy 5 |
| `an early` | 13 | 19.6 | 4.5 | 3% | 17x | casual 11, lazy 2 |
| `the wind` | 15 | 22.6 | 9.0 | 3% | 15x | casual 8, lazy 7 |
| `a good` | 85 | 128.0 | 16.6 | 5% | 4x | casual 69, lazy 16 |
| `to a` | 18 | 27.1 | 21.1 | 3% | 12x | casual 9, lazy 5, angry 4 |
| `get a` | 18 | 27.1 | 10.5 | 3% | 12x | casual 15, lazy 3 |
| `which is` | 20 | 30.1 | 51.2 | 3% | 11x | lazy 11, casual 9 |
| `it is` | 115 | 173.2 | 72.3 | 5% | 3x | casual 79, lazy 36 |
| `going to` | 26 | 39.2 | 21.1 | 3% | 9x | casual 18, lazy 5, angry 3 |
| `what did you` | 27 | 40.7 | 48.2 | 3% | 8x | casual 26, lazy 1 |
| `you go` | 28 | 42.2 | 12.1 | 3% | 8x | casual 27, lazy 1 |
| `next time` | 28 | 42.2 | 1.5 | 3% | 8x | casual 15, lazy 11, angry 2 |
| `the phone` | 30 | 45.2 | 31.6 | 3% | 7x | casual 14, lazy 12, angry 4 |
| `ten minutes` | 33 | 49.7 | 45.2 | 3% | 7x | casual 20, lazy 13 |
| `worth the` | 34 | 51.2 | 12.1 | 3% | 7x | casual 21, lazy 13 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `have you tried` | 3 | 22 | 13.7 | casual 15, angry 7 |
| `the front desk` | 3 | 8 | 13.1 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `for an hour` | 3 | 9 | 12.3 | casual 8, lazy 1 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.6 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.3 | lazy 4, angry 2, casual 2 |
| `a lot of` | 3 | 10 | 10.2 | casual 7, lazy 3 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `earn their` | 2 | 15 | 10.0 | lazy 14, casual 1 |
| `what did you` | 3 | 27 | 10.0 | casual 26, lazy 1 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `washing machine` | 2 | 12 | 9.9 | casual 11, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `part of` | 2 | lazy 13, casual 11 |
| `i have` | 2 | casual 35, lazy 12 |
| `on the` | 3 | casual 151, lazy 51, angry 15 |
| `do it` | 2 | casual 24, lazy 11 |
| `the end` | 3 | casual 26, lazy 7, angry 5 |
| `of the` | 3 | casual 84, lazy 39, angry 12 |
| `out of` | 3 | casual 34, lazy 14, angry 7 |
| `to get` | 3 | casual 7, lazy 2, angry 1 |
| `it's been` | 1 | casual 10 |
| `early night` | 2 | casual 11, lazy 1 |
| `is fine` | 2 | casual 8, lazy 5 |
| `an early` | 2 | casual 11, lazy 2 |
| `the wind` | 2 | casual 8, lazy 7 |
| `a good` | 2 | casual 69, lazy 16 |
| `to a` | 3 | casual 9, lazy 5, angry 4 |
| `get a` | 2 | casual 15, lazy 3 |
| `which is` | 2 | lazy 11, casual 9 |
| `it is` | 2 | casual 79, lazy 36 |
| `going to` | 3 | casual 18, lazy 5, angry 3 |
| `what did you` | 2 | casual 26, lazy 1 |
| `you go` | 2 | casual 27, lazy 1 |
| `next time` | 3 | casual 15, lazy 11, angry 2 |
| `the phone` | 3 | casual 14, lazy 12, angry 4 |
| `ten minutes` | 2 | casual 20, lazy 13 |
| `worth the` | 2 | casual 21, lazy 13 |

## 4. Opener maps

- assistant pos 0 (n=6639): a 7.5%, the 3.2%, that 2.4%, did 2.1%, haha 2.0%, i 1.6%
- assistant pos 1 (n=6639): the 10.5%, you 2.2%, a 2.2%, is 2.1%, it 1.3%, and 1.0%
- assistant pos 2 (n=6638): the 6.1%, is 3.8%, are 2.5%, a 2.3%, of 1.5%, for 1.2%
- assistant pos last (n=6639): it 4.9%, now 1.6%, time 1.5%, one 1.1%, again 1.0%, you 0.9%
- user pos 0 (n=6639): the 11.9%, my 9.4%, our 7.6%, i 7.3%, did 3.9%, we 3.0%
- user pos 1 (n=6576): the 4.7%, you 3.4%, a 2.7%, was 1.5%, did 1.5%, is 1.4%
- user pos 2 (n=6487): the 7.1%, a 3.1%, is 2.5%, you 1.9%, and 1.6%, got 1.2%
- user pos last (n=6639): again 2.9%, it 1.9%, now 1.6%, week 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.6%**; model outputs: **18.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

