# synth2 token-attractor map

Generated 2026-10-24 05:24  |  corpus 8916 rows, **11346 assistant turns**, 11346 user turns
Probe: `probe_out89_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T02:06:33

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.7% | 5.8% | +0.1 |
| `the`-opener (user) | 14.6% | 14.7% | +0.1 |
| copula-only | 0.8% | 0.7% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the first` | - | 7% | - | 7x |
| `this week` | - | 5% | - | 17x |
| `and it` | - | 5% | - | 11x |
| `yet the` | - | 3% | - | 47x |
| `is never` | - | 3% | - | 47x |
| `so i` | - | 3% | - | 38x |
| `was not` | - | 3% | - | 27x |
| `for the` | - | 7% | - | 3x |
| `yeah the` | - | 3% | - | 22x |
| `is not a` | - | 3% | - | 22x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.8% | < 12% |
| `the`-opener (user) | 14.7% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 37 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the first` | 113 | 99.6 | 82.0 | 7% | 7x | lazy 38, casual 36, sexy 22 |
| `this week` | 34 | 30.0 | 43.2 | 5% | 17x | casual 22, angry 4, lazy 4 |
| `and it` | 50 | 44.1 | 67.0 | 5% | 11x | casual 40, lazy 5, formal 3 |
| `yet the` | 8 | 7.1 | 0.0 | 3% | 47x | casual 6, lazy 2 |
| `is never` | 8 | 7.1 | 1.8 | 3% | 47x | casual 5, formal 1, lazy 1 |
| `so i` | 10 | 8.8 | 11.5 | 3% | 38x | casual 8, lazy 1, sexy 1 |
| `was not` | 14 | 12.3 | 4.4 | 3% | 27x | casual 7, sexy 5, angry 1 |
| `for the` | 298 | 262.6 | 268.8 | 7% | 3x | casual 120, sexy 70, angry 61 |
| `yeah the` | 17 | 15.0 | 1.8 | 3% | 22x | casual 16, lazy 1 |
| `is not a` | 17 | 15.0 | 0.9 | 3% | 22x | angry 11, casual 3, lazy 3 |
| `the weekend` | 19 | 16.7 | 34.4 | 3% | 20x | casual 14, lazy 4, sexy 1 |
| `of your` | 19 | 16.7 | 4.4 | 3% | 20x | angry 7, sexy 6, casual 5 |
| `are you` | 114 | 100.5 | 59.9 | 5% | 5x | casual 91, angry 12, sexy 10 |
| `the same` | 126 | 111.1 | 119.9 | 5% | 5x | angry 34, casual 34, lazy 29 |
| `a walk` | 22 | 19.4 | 10.6 | 3% | 17x | casual 16, angry 2, lazy 2 |
| `if you` | 23 | 20.3 | 6.2 | 3% | 16x | lazy 11, casual 9, angry 1 |
| `a two` | 24 | 21.2 | 13.2 | 3% | 16x | angry 8, casual 8, lazy 4 |
| `it for` | 28 | 24.7 | 14.1 | 3% | 14x | casual 18, lazy 7, sexy 3 |
| `to be` | 29 | 25.6 | 19.4 | 3% | 13x | casual 13, lazy 8, sexy 4 |
| `do not` | 29 | 25.6 | 7.9 | 3% | 13x | casual 12, lazy 12, angry 3 |
| `to the` | 181 | 159.5 | 166.6 | 5% | 3x | casual 70, sexy 34, lazy 32 |
| `of the` | 201 | 177.2 | 135.7 | 5% | 3x | casual 80, lazy 39, sexy 35 |
| `the phone` | 41 | 36.1 | 26.4 | 3% | 9x | casual 14, lazy 12, angry 10 |
| `for a` | 224 | 197.4 | 168.3 | 5% | 3x | angry 93, casual 66, lazy 23 |
| `the car` | 51 | 44.9 | 39.7 | 3% | 7x | casual 26, sexy 14, lazy 9 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.9 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.7 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the front desk` | 3 | 14 | 12.4 | angry 8, lazy 4, casual 1 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.7 | angry 5, formal 5 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.0 | lazy 6, casual 4, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the first` | 5 | lazy 38, casual 36, sexy 22, formal 10 |
| `this week` | 5 | casual 22, angry 4, lazy 4, formal 2 |
| `and it` | 4 | casual 40, lazy 5, formal 3, sexy 2 |
| `yet the` | 2 | casual 6, lazy 2 |
| `is never` | 4 | casual 5, formal 1, lazy 1, sexy 1 |
| `so i` | 3 | casual 8, lazy 1, sexy 1 |
| `was not` | 4 | casual 7, sexy 5, angry 1, lazy 1 |
| `for the` | 5 | casual 120, sexy 70, angry 61, lazy 24 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `is not a` | 3 | angry 11, casual 3, lazy 3 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `of your` | 4 | angry 7, sexy 6, casual 5, lazy 1 |
| `are you` | 4 | casual 91, angry 12, sexy 10, lazy 1 |
| `the same` | 5 | angry 34, casual 34, lazy 29, formal 15 |
| `a walk` | 5 | casual 16, angry 2, lazy 2, formal 1 |
| `if you` | 5 | lazy 11, casual 9, angry 1, formal 1 |
| `a two` | 4 | angry 8, casual 8, lazy 4, sexy 4 |
| `it for` | 3 | casual 18, lazy 7, sexy 3 |
| `to be` | 5 | casual 13, lazy 8, sexy 4, angry 2 |
| `do not` | 5 | casual 12, lazy 12, angry 3, formal 1 |
| `to the` | 5 | casual 70, sexy 34, lazy 32, angry 27 |
| `of the` | 5 | casual 80, lazy 39, sexy 35, angry 31 |
| `the phone` | 5 | casual 14, lazy 12, angry 10, formal 3 |
| `for a` | 5 | angry 93, casual 66, lazy 23, sexy 23 |
| `the car` | 5 | casual 26, sexy 14, lazy 9, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=11346): a 10.2%, the 5.8%, how 2.4%, did 2.2%, does 2.1%, why 1.8%
- assistant pos 1 (n=11346): the 11.0%, a 2.0%, is 1.7%, you 1.6%, does 1.6%, on 0.9%
- assistant pos 2 (n=11345): the 7.4%, a 3.0%, is 2.6%, on 2.0%, of 1.9%, for 1.8%
- assistant pos last (n=11346): it 3.8%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11346): the 14.7%, my 9.7%, our 8.7%, i 6.5%, we 6.0%, you 5.3%
- user pos 1 (n=11283): the 3.1%, you 2.0%, a 1.6%, got 1.0%, is 1.0%, was 1.0%
- user pos 2 (n=11193): the 7.9%, a 3.6%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11346): it 2.2%, again 2.1%, now 1.2%, week 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.7%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

