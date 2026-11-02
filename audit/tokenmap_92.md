# synth2 token-attractor map

Generated 2026-10-24 14:33  |  corpus 9102 rows, **11547 assistant turns**, 11547 user turns
Probe: `probe_out92_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T11:41:38

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.0% | 6.0% | -0.0 |
| `the`-opener (user) | 14.8% | 14.7% | -0.1 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `worth it` | - | 7% | - | 11x |
| `was it` | - | 7% | - | 9x |
| `the same` | - | 7% | - | 6x |
| `that is` | - | 7% | - | 5x |
| `to sleep` | - | 3% | - | 48x |
| `the old one` | - | 3% | - | 48x |
| `i never` | - | 3% | - | 48x |
| `nothing on` | - | 3% | - | 43x |
| `are a` | - | 5% | - | 9x |
| `is the` | 8% | 8% | 2x | 2x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.0% | < 12% |
| `the`-opener (user) | 14.7% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 36 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `worth it` | 68 | 58.9 | 9.5 | 7% | 11x | casual 43, lazy 15, sexy 9 |
| `was it` | 83 | 71.9 | 19.1 | 7% | 9x | casual 68, sexy 11, angry 4 |
| `the same` | 127 | 110.0 | 120.4 | 7% | 6x | angry 34, casual 34, lazy 29 |
| `that is` | 166 | 143.8 | 13.9 | 7% | 5x | casual 96, lazy 26, sexy 25 |
| `to sleep` | 8 | 6.9 | 7.8 | 3% | 48x | angry 3, casual 2, lazy 2 |
| `the old one` | 8 | 6.9 | 5.2 | 3% | 48x | lazy 4, casual 2, angry 1 |
| `i never` | 8 | 6.9 | 32.0 | 3% | 48x | casual 3, lazy 2, sexy 2 |
| `nothing on` | 9 | 7.8 | 0.9 | 3% | 43x | casual 8, lazy 1 |
| `are a` | 67 | 58.0 | 7.8 | 5% | 9x | lazy 45, angry 11, casual 8 |
| `is the` | 500 | 433.0 | 79.7 | 8% | 2x | casual 292, lazy 116, angry 50 |
| `how you` | 10 | 8.7 | 0.9 | 3% | 38x | casual 5, sexy 3, lazy 2 |
| `and never` | 10 | 8.7 | 11.3 | 3% | 38x | casual 6, lazy 3, formal 1 |
| `the apartment` | 12 | 10.4 | 12.1 | 3% | 32x | casual 7, sexy 4, lazy 1 |
| `do the` | 82 | 71.0 | 8.7 | 5% | 7x | formal 30, casual 28, sexy 13 |
| `are worth` | 13 | 11.3 | 0.0 | 3% | 30x | lazy 6, casual 3, sexy 3 |
| `a real` | 98 | 84.9 | 34.6 | 5% | 6x | casual 75, angry 13, lazy 10 |
| `they are` | 19 | 16.5 | 5.2 | 3% | 20x | casual 11, lazy 5, sexy 2 |
| `is how` | 22 | 19.1 | 0.0 | 3% | 17x | angry 8, casual 7, lazy 4 |
| `a walk` | 22 | 19.1 | 10.4 | 3% | 17x | casual 16, angry 2, lazy 2 |
| `a quiet` | 33 | 28.6 | 4.3 | 3% | 12x | casual 13, formal 7, lazy 7 |
| `a long` | 33 | 28.6 | 7.8 | 3% | 12x | casual 21, lazy 8, angry 3 |
| `is a` | 525 | 454.7 | 68.4 | 7% | 1x | angry 222, casual 147, lazy 116 |
| `the whole` | 190 | 164.5 | 112.6 | 5% | 3x | lazy 83, casual 57, angry 32 |
| `it the` | 45 | 39.0 | 11.3 | 3% | 9x | casual 34, sexy 5, lazy 4 |
| `it a` | 45 | 39.0 | 10.4 | 3% | 9x | casual 35, lazy 4, sexy 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.9 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `the front desk` | 3 | 14 | 12.3 | angry 8, lazy 4, casual 1 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `and i am` | 3 | 11 | 11.0 | casual 9, lazy 1, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `worth it` | 4 | casual 43, lazy 15, sexy 9, angry 1 |
| `was it` | 3 | casual 68, sexy 11, angry 4 |
| `the same` | 5 | angry 34, casual 34, lazy 29, formal 16 |
| `that is` | 5 | casual 96, lazy 26, sexy 25, angry 17 |
| `to sleep` | 4 | angry 3, casual 2, lazy 2, sexy 1 |
| `the old one` | 4 | lazy 4, casual 2, angry 1, formal 1 |
| `i never` | 4 | casual 3, lazy 2, sexy 2, angry 1 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `are a` | 4 | lazy 45, angry 11, casual 8, sexy 3 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 26 |
| `how you` | 3 | casual 5, sexy 3, lazy 2 |
| `and never` | 3 | casual 6, lazy 3, formal 1 |
| `the apartment` | 3 | casual 7, sexy 4, lazy 1 |
| `do the` | 5 | formal 30, casual 28, sexy 13, angry 6 |
| `are worth` | 4 | lazy 6, casual 3, sexy 3, formal 1 |
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `they are` | 4 | casual 11, lazy 5, sexy 2, angry 1 |
| `is how` | 4 | angry 8, casual 7, lazy 4, formal 3 |
| `a walk` | 5 | casual 16, angry 2, lazy 2, formal 1 |
| `a quiet` | 4 | casual 13, formal 7, lazy 7, angry 6 |
| `a long` | 4 | casual 21, lazy 8, angry 3, formal 1 |
| `is a` | 5 | angry 222, casual 147, lazy 116, formal 25 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `it the` | 5 | casual 34, sexy 5, lazy 4, angry 1 |
| `it a` | 5 | casual 35, lazy 4, sexy 3, angry 2 |

## 4. Opener maps

- assistant pos 0 (n=11547): a 10.2%, the 6.0%, how 2.3%, does 2.3%, did 2.2%, why 1.8%
- assistant pos 1 (n=11547): the 11.1%, a 2.0%, is 1.7%, you 1.6%, does 1.6%, on 0.9%
- assistant pos 2 (n=11546): the 7.3%, a 3.0%, is 2.6%, on 1.9%, of 1.9%, for 1.9%
- assistant pos last (n=11547): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.8%
- user pos 0 (n=11547): the 14.7%, my 9.6%, our 8.9%, i 6.6%, we 6.0%, you 5.2%
- user pos 1 (n=11484): the 3.1%, you 2.0%, a 1.6%, is 1.0%, got 1.0%, was 1.0%
- user pos 2 (n=11394): the 8.0%, a 3.7%, is 1.6%, my 1.4%, you 1.3%, in 1.2%
- user pos last (n=11547): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.6%**; model outputs: **16.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

