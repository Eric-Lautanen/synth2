# synth2 token-attractor map

Generated 2026-10-22 13:59  |  corpus 8234 rows, **10609 assistant turns**, 10609 user turns
Probe: `probe_out78_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T10:04:50

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.6% | 4.8% | +0.2 |
| `the`-opener (user) | 14.1% | 14.2% | +0.1 |
| copula-only | 0.7% | 0.7% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the one` | - | 7% | - | 11x |
| `is a` | - | 10% | - | 2x |
| `at least` | - | 5% | - | 7x |
| `the job` | - | 3% | - | 25x |
| `did you go` | - | 3% | - | 25x |
| `a real` | - | 5% | - | 5x |
| `the night` | - | 3% | - | 13x |
| `the coffee` | - | 3% | - | 12x |
| `are the` | - | 5% | - | 3x |
| `the whole` | - | 5% | - | 3x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.8% | < 12% |
| `the`-opener (user) | 14.2% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `the one` | 65 | 61.3 | 23.6 | 7% | 11x | lazy 34, casual 23, angry 6 |
| `is a` | 504 | 475.1 | 60.3 | 10% | 2x | angry 222, casual 147, lazy 116 |
| `at least` | 72 | 67.9 | 12.3 | 5% | 7x | casual 31, angry 20, sexy 12 |
| `the job` | 14 | 13.2 | 5.7 | 3% | 25x | casual 6, angry 5, formal 1 |
| `did you go` | 14 | 13.2 | 4.7 | 3% | 25x | casual 14 |
| `a real` | 98 | 92.4 | 37.7 | 5% | 5x | casual 75, angry 13, lazy 10 |
| `the night` | 28 | 26.4 | 13.2 | 3% | 13x | lazy 9, sexy 8, casual 6 |
| `the coffee` | 30 | 28.3 | 21.7 | 3% | 12x | lazy 12, sexy 7, casual 6 |
| `are the` | 160 | 150.8 | 14.1 | 5% | 3x | lazy 92, casual 61, angry 5 |
| `the whole` | 185 | 174.4 | 120.7 | 5% | 3x | lazy 83, casual 57, angry 32 |
| `it the` | 45 | 42.4 | 12.3 | 3% | 8x | casual 34, sexy 5, lazy 4 |
| `a whole` | 46 | 43.4 | 24.5 | 3% | 8x | angry 19, lazy 16, casual 10 |
| `and it` | 48 | 45.2 | 60.3 | 3% | 7x | casual 40, lazy 5, sexy 2 |
| `i will` | 55 | 51.8 | 8.5 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `the real` | 60 | 56.6 | 10.4 | 3% | 6x | lazy 23, casual 22, sexy 12 |
| `how did` | 65 | 61.3 | 8.5 | 3% | 5x | casual 29, sexy 18, angry 17 |
| `in the` | 380 | 358.2 | 342.2 | 5% | 1x | casual 164, sexy 73, angry 67 |
| `with the` | 105 | 99.0 | 79.2 | 3% | 3x | casual 50, sexy 22, angry 18 |
| `is the` | 482 | 454.3 | 72.6 | 5% | 1x | casual 292, lazy 116, angry 50 |
| `is it` | 122 | 115.0 | 22.6 | 3% | 3x | casual 103, formal 8, angry 7 |
| `it is` | 135 | 127.3 | 50.0 | 3% | 3x | casual 82, lazy 36, angry 10 |
| `worse than` | 8 | 7.5 | 2.8 | 2% | 22x | casual 5, angry 2, sexy 1 |
| `was fine` | 8 | 7.5 | 3.8 | 2% | 22x | casual 6, lazy 2 |
| `the order` | 8 | 7.5 | 0.9 | 2% | 22x | angry 6, casual 1, lazy 1 |
| `the bags` | 8 | 7.5 | 0.9 | 2% | 22x | lazy 4, casual 2, angry 1 |

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
| `the front desk` | 3 | 13 | 12.9 | angry 8, lazy 4, casual 1 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 15 | 12.1 | angry 6, casual 3, sexy 3 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `feel like a` | 3 | 11 | 11.2 | lazy 6, casual 4, sexy 1 |
| `how long did` | 3 | 14 | 11.1 | casual 9, angry 3, formal 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.8 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.6 | casual 15, angry 2 |
| `did you get` | 3 | 41 | 10.5 | casual 37, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the one` | 4 | lazy 34, casual 23, angry 6, sexy 2 |
| `is a` | 5 | angry 222, casual 147, lazy 116, sexy 15 |
| `at least` | 4 | casual 31, angry 20, sexy 12, lazy 9 |
| `the job` | 5 | casual 6, angry 5, formal 1, lazy 1 |
| `did you go` | 1 | casual 14 |
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `the night` | 4 | lazy 9, sexy 8, casual 6, angry 5 |
| `the coffee` | 5 | lazy 12, sexy 7, casual 6, formal 4 |
| `are the` | 4 | lazy 92, casual 61, angry 5, sexy 2 |
| `the whole` | 4 | lazy 83, casual 57, angry 32, sexy 13 |
| `it the` | 5 | casual 34, sexy 5, lazy 4, angry 1 |
| `a whole` | 4 | angry 19, lazy 16, casual 10, sexy 1 |
| `and it` | 4 | casual 40, lazy 5, sexy 2, formal 1 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `the real` | 4 | lazy 23, casual 22, sexy 12, angry 3 |
| `how did` | 4 | casual 29, sexy 18, angry 17, formal 1 |
| `in the` | 5 | casual 164, sexy 73, angry 67, lazy 67 |
| `with the` | 5 | casual 50, sexy 22, angry 18, lazy 12 |
| `is the` | 5 | casual 292, lazy 116, angry 50, sexy 16 |
| `is it` | 4 | casual 103, formal 8, angry 7, sexy 4 |
| `it is` | 5 | casual 82, lazy 36, angry 10, sexy 4 |
| `worse than` | 3 | casual 5, angry 2, sexy 1 |
| `was fine` | 2 | casual 6, lazy 2 |
| `the order` | 3 | angry 6, casual 1, lazy 1 |
| `the bags` | 4 | lazy 4, casual 2, angry 1, sexy 1 |

## 4. Opener maps

- assistant pos 0 (n=10609): a 10.2%, the 4.8%, did 2.3%, how 2.1%, that 1.7%, was 1.6%
- assistant pos 1 (n=10609): the 10.6%, a 2.0%, is 1.8%, you 1.7%, does 1.2%, on 1.0%
- assistant pos 2 (n=10608): the 6.9%, a 2.8%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10609): it 3.8%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10609): the 14.2%, my 9.8%, our 8.2%, we 6.1%, i 6.1%, you 5.6%
- user pos 1 (n=10546): the 3.2%, you 2.2%, a 1.7%, was 1.0%, got 1.0%, did 1.0%
- user pos 2 (n=10456): the 7.8%, a 3.3%, is 1.7%, you 1.4%, my 1.3%, was 1.3%
- user pos last (n=10609): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.0%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

