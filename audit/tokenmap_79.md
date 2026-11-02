# synth2 token-attractor map

Generated 2026-10-22 18:48  |  corpus 8296 rows, **10676 assistant turns**, 10676 user turns
Probe: `probe_out79_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T13:59:25

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.8% | 5.0% | +0.2 |
| `the`-opener (user) | 14.2% | 14.3% | +0.1 |
| copula-only | 0.7% | 0.7% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `it is` | 3% | 7% | 3x | 5x |
| `a nice` | - | 3% | - | 40x |
| `the wait` | - | 3% | - | 36x |
| `is a` | 10% | 8% | 2x | 2x |
| `about the` | - | 5% | - | 7x |
| `did you` | - | 7% | - | 3x |
| `the point` | - | 3% | - | 24x |
| `with it` | - | 3% | - | 22x |
| `a real` | 5% | 5% | 5x | 5x |
| `with the` | 3% | 5% | 3x | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.0% | < 12% |
| `the`-opener (user) | 14.3% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 34 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `it is` | 135 | 126.5 | 50.6 | 7% | 5x | casual 82, lazy 36, angry 10 |
| `a nice` | 9 | 8.4 | 1.9 | 3% | 40x | casual 8, lazy 1 |
| `the wait` | 10 | 9.4 | 7.5 | 3% | 36x | lazy 4, casual 3, sexy 3 |
| `is a` | 505 | 473.0 | 59.9 | 8% | 2x | angry 222, casual 147, lazy 116 |
| `about the` | 75 | 70.3 | 46.8 | 5% | 7x | casual 34, angry 25, sexy 14 |
| `did you` | 280 | 262.3 | 230.4 | 7% | 3x | casual 187, sexy 57, angry 28 |
| `the point` | 15 | 14.1 | 4.7 | 3% | 24x | casual 6, lazy 4, angry 2 |
| `with it` | 16 | 15.0 | 7.5 | 3% | 22x | casual 10, sexy 4, formal 1 |
| `a real` | 98 | 91.8 | 37.5 | 5% | 5x | casual 75, angry 13, lazy 10 |
| `with the` | 105 | 98.4 | 78.7 | 5% | 5x | casual 50, sexy 22, angry 18 |
| `oh no` | 18 | 16.9 | 6.6 | 3% | 20x | casual 18 |
| `if it` | 18 | 16.9 | 5.6 | 3% | 20x | casual 13, lazy 3, angry 2 |
| `so far` | 24 | 22.5 | 10.3 | 3% | 15x | casual 17, lazy 4, angry 2 |
| `did anyone` | 25 | 23.4 | 6.6 | 3% | 14x | angry 8, casual 6, formal 5 |
| `to be` | 28 | 26.2 | 18.7 | 3% | 13x | casual 13, lazy 8, sexy 4 |
| `how did the` | 29 | 27.2 | 6.6 | 3% | 12x | casual 12, angry 10, sexy 6 |
| `that is` | 166 | 155.5 | 12.2 | 5% | 3x | casual 96, lazy 26, sexy 25 |
| `is the` | 485 | 454.3 | 72.1 | 7% | 1x | casual 292, lazy 116, angry 50 |
| `a bit` | 36 | 33.7 | 30.0 | 3% | 10x | casual 34, angry 1, lazy 1 |
| `than the` | 42 | 39.3 | 65.6 | 3% | 8x | casual 15, sexy 12, lazy 8 |
| `the worst` | 52 | 48.7 | 8.4 | 3% | 7x | casual 26, lazy 17, angry 6 |
| `this time` | 54 | 50.6 | 15.9 | 3% | 7x | casual 43, angry 6, sexy 3 |
| `you get` | 55 | 51.5 | 46.8 | 3% | 6x | casual 45, angry 5, lazy 5 |
| `i will` | 55 | 51.5 | 8.4 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `and i` | 62 | 58.1 | 91.8 | 3% | 6x | casual 31, lazy 25, sexy 6 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `the front desk` | 3 | 13 | 12.8 | angry 8, lazy 4, casual 1 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `counts as a` | 3 | 10 | 12.4 | formal 3, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 15 | 12.1 | angry 6, casual 3, sexy 3 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 14 | 11.2 | casual 9, angry 3, formal 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.8 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.6 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `it is` | 5 | casual 82, lazy 36, angry 10, sexy 4 |
| `a nice` | 2 | casual 8, lazy 1 |
| `the wait` | 3 | lazy 4, casual 3, sexy 3 |
| `is a` | 5 | angry 222, casual 147, lazy 116, sexy 15 |
| `about the` | 4 | casual 34, angry 25, sexy 14, lazy 2 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `the point` | 5 | casual 6, lazy 4, angry 2, sexy 2 |
| `with it` | 4 | casual 10, sexy 4, formal 1, lazy 1 |
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `with the` | 5 | casual 50, sexy 22, angry 18, lazy 12 |
| `oh no` | 1 | casual 18 |
| `if it` | 3 | casual 13, lazy 3, angry 2 |
| `so far` | 4 | casual 17, lazy 4, angry 2, sexy 1 |
| `did anyone` | 5 | angry 8, casual 6, formal 5, sexy 5 |
| `to be` | 5 | casual 13, lazy 8, sexy 4, angry 2 |
| `how did the` | 4 | casual 12, angry 10, sexy 6, formal 1 |
| `that is` | 5 | casual 96, lazy 26, sexy 25, angry 17 |
| `is the` | 5 | casual 292, lazy 116, angry 50, sexy 16 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `than the` | 5 | casual 15, sexy 12, lazy 8, angry 5 |
| `the worst` | 5 | casual 26, lazy 17, angry 6, sexy 2 |
| `this time` | 4 | casual 43, angry 6, sexy 3, lazy 2 |
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `and i` | 3 | casual 31, lazy 25, sexy 6 |

## 4. Opener maps

- assistant pos 0 (n=10676): a 10.1%, the 5.0%, did 2.3%, how 2.1%, that 1.7%, was 1.6%
- assistant pos 1 (n=10676): the 10.8%, a 2.0%, is 1.8%, you 1.7%, does 1.2%, on 1.0%
- assistant pos 2 (n=10675): the 7.0%, a 2.8%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10676): it 3.8%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10676): the 14.3%, my 9.8%, our 8.3%, i 6.1%, we 6.1%, you 5.6%
- user pos 1 (n=10613): the 3.2%, you 2.2%, a 1.7%, was 1.0%, got 1.0%, did 1.0%
- user pos 2 (n=10523): the 7.8%, a 3.3%, is 1.7%, you 1.4%, my 1.3%, was 1.3%
- user pos last (n=10676): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.9%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

