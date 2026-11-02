# synth2 token-attractor map

Generated 2026-10-15 08:45  |  corpus 4312 rows, **6371 assistant turns**, 6371 user turns
Probe: `probe_out28_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T06:18:22

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.3% | 3.2% | -0.1 |
| `the`-opener (user) | 11.2% | 11.4% | +0.2 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 8% | 12% | 6x | 9x |
| `is a` | - | 12% | - | 3x |
| `a known` | - | 5% | - | 40x |
| `are you` | - | 8% | - | 6x |
| `it's been` | - | 5% | - | 32x |
| `i have been` | 8% | 5% | 47x | 29x |
| `i am` | - | 7% | - | 8x |
| `you going` | - | 5% | - | 19x |
| `going to` | - | 5% | - | 13x |
| `all day` | - | 5% | - | 11x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.2% | < 12% |
| `the`-opener (user) | 11.4% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a good` | 85 | 133.4 | 17.3 | 12% | 9x | casual 69, lazy 16 |
| `is a` | 295 | 463.0 | 78.5 | 12% | 3x | casual 147, lazy 116, angry 32 |
| `a known` | 8 | 12.6 | 0.0 | 5% | 40x | lazy 6, casual 2 |
| `are you` | 95 | 149.1 | 102.0 | 8% | 6x | casual 92, angry 2, lazy 1 |
| `it's been` | 10 | 15.7 | 7.8 | 5% | 32x | casual 10 |
| `i have been` | 11 | 17.3 | 25.1 | 5% | 29x | casual 9, lazy 2 |
| `i am` | 56 | 87.9 | 51.8 | 7% | 8x | casual 44, lazy 11, angry 1 |
| `you going` | 17 | 26.7 | 7.8 | 5% | 19x | casual 15, angry 2 |
| `going to` | 25 | 39.2 | 22.0 | 5% | 13x | casual 18, lazy 5, angry 2 |
| `all day` | 28 | 43.9 | 26.7 | 5% | 11x | lazy 15, casual 11, angry 2 |
| `for it` | 31 | 48.7 | 18.8 | 5% | 10x | casual 24, lazy 7 |
| `the old` | 32 | 50.2 | 23.5 | 5% | 10x | casual 18, lazy 13, angry 1 |
| `it is` | 115 | 180.5 | 75.3 | 7% | 4x | casual 79, lazy 36 |
| `i will` | 45 | 70.6 | 12.6 | 5% | 7x | casual 31, lazy 14 |
| `and i` | 54 | 84.8 | 124.0 | 5% | 6x | casual 29, lazy 25 |
| `an hour` | 54 | 84.8 | 72.2 | 5% | 6x | casual 34, lazy 16, angry 4 |
| `is just a` | 9 | 14.1 | 0.0 | 3% | 24x | angry 7, lazy 2 |
| `good one` | 9 | 14.1 | 4.7 | 3% | 24x | casual 8, lazy 1 |
| `worth it` | 58 | 91.0 | 14.1 | 5% | 5x | casual 42, lazy 15, angry 1 |
| `old one` | 10 | 15.7 | 6.3 | 3% | 21x | casual 6, lazy 4 |
| `was it` | 67 | 105.2 | 33.0 | 5% | 5x | casual 65, angry 2 |
| `with the` | 68 | 106.7 | 84.8 | 5% | 5x | casual 54, lazy 12, angry 2 |
| `their own` | 12 | 18.8 | 3.1 | 3% | 18x | lazy 11, casual 1 |
| `but it` | 13 | 20.4 | 14.1 | 3% | 16x | casual 11, lazy 2 |
| `i've been` | 15 | 23.5 | 25.1 | 3% | 14x | casual 15 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `best kind of` | 3 | 9 | 13.9 | casual 8, lazy 1 |
| `have you tried` | 3 | 19 | 13.7 | casual 15, angry 4 |
| `the front desk` | 3 | 8 | 13.2 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.2 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `for an hour` | 3 | 9 | 12.3 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `how long did` | 3 | 11 | 11.7 | casual 9, angry 2 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.3 | casual 9 |
| `the best kind` | 3 | 12 | 11.2 | casual 12 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `did you get` | 3 | 44 | 11.2 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `a lot of` | 3 | 10 | 10.3 | casual 7, lazy 3 |
| `are you going` | 3 | 17 | 10.2 | casual 15, angry 2 |
| `what did you` | 3 | 27 | 10.2 | casual 26, lazy 1 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `earn their` | 2 | 15 | 10.0 | lazy 14, casual 1 |
| `makes the whole` | 3 | 9 | 9.9 | lazy 6, casual 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 2 | casual 69, lazy 16 |
| `is a` | 3 | casual 147, lazy 116, angry 32 |
| `a known` | 2 | lazy 6, casual 2 |
| `are you` | 3 | casual 92, angry 2, lazy 1 |
| `it's been` | 1 | casual 10 |
| `i have been` | 2 | casual 9, lazy 2 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `you going` | 2 | casual 15, angry 2 |
| `going to` | 3 | casual 18, lazy 5, angry 2 |
| `all day` | 3 | lazy 15, casual 11, angry 2 |
| `for it` | 2 | casual 24, lazy 7 |
| `the old` | 3 | casual 18, lazy 13, angry 1 |
| `it is` | 2 | casual 79, lazy 36 |
| `i will` | 2 | casual 31, lazy 14 |
| `and i` | 2 | casual 29, lazy 25 |
| `an hour` | 3 | casual 34, lazy 16, angry 4 |
| `is just a` | 2 | angry 7, lazy 2 |
| `good one` | 2 | casual 8, lazy 1 |
| `worth it` | 3 | casual 42, lazy 15, angry 1 |
| `old one` | 2 | casual 6, lazy 4 |
| `was it` | 2 | casual 65, angry 2 |
| `with the` | 3 | casual 54, lazy 12, angry 2 |
| `their own` | 2 | lazy 11, casual 1 |
| `but it` | 2 | casual 11, lazy 2 |
| `i've been` | 1 | casual 15 |

## 4. Opener maps

- assistant pos 0 (n=6371): a 7.4%, the 3.2%, that 2.5%, haha 2.1%, i 1.7%, did 1.4%
- assistant pos 1 (n=6371): the 9.2%, a 2.4%, is 2.2%, you 1.9%, it 1.3%, and 1.0%
- assistant pos 2 (n=6370): the 6.0%, is 4.0%, are 2.6%, a 2.3%, of 1.5%, for 1.3%
- assistant pos last (n=6371): it 5.0%, now 1.6%, time 1.4%, one 1.2%, again 1.0%, you 0.9%
- user pos 0 (n=6371): the 11.4%, my 8.9%, i 7.5%, our 6.8%, did 4.1%, a 3.0%
- user pos 1 (n=6308): the 4.9%, you 3.6%, a 2.8%, was 1.6%, did 1.6%, is 1.4%
- user pos 2 (n=6219): the 7.3%, a 3.2%, is 2.5%, you 2.0%, and 1.7%, got 1.2%
- user pos last (n=6371): again 2.8%, it 2.0%, now 1.6%, week 1.5%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.9%**; model outputs: **21.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 2155 |

