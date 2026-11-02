# synth2 token-attractor map

Generated 2026-10-24 02:06  |  corpus 8854 rows, **11279 assistant turns**, 11279 user turns
Probe: `probe_out88_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T23:45:59

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.6% | 5.7% | +0.1 |
| `the`-opener (user) | 14.6% | 14.6% | +0.1 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `or is it` | - | 5% | - | 25x |
| `to be` | - | 5% | - | 19x |
| `for it` | - | 5% | - | 14x |
| `not a` | - | 5% | - | 14x |
| `did you get` | - | 5% | - | 14x |
| `do that` | - | 3% | - | 42x |
| `is the` | - | 8% | - | 2x |
| `it's been` | - | 3% | - | 38x |
| `a new` | - | 5% | - | 8x |
| `the three` | - | 3% | - | 25x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.7% | < 12% |
| `the`-opener (user) | 14.6% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 44 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `or is it` | 23 | 20.4 | 2.7 | 5% | 25x | formal 11, casual 7, angry 5 |
| `to be` | 29 | 25.7 | 19.5 | 5% | 19x | casual 13, lazy 8, sexy 4 |
| `for it` | 39 | 34.6 | 16.8 | 5% | 14x | casual 23, lazy 7, formal 4 |
| `not a` | 41 | 36.4 | 8.0 | 5% | 14x | angry 21, casual 12, lazy 7 |
| `did you get` | 41 | 36.4 | 36.4 | 5% | 14x | casual 37, angry 2, lazy 2 |
| `do that` | 9 | 8.0 | 1.8 | 3% | 42x | casual 8, sexy 1 |
| `is the` | 497 | 440.6 | 78.0 | 8% | 2x | casual 292, lazy 116, angry 50 |
| `it's been` | 10 | 8.9 | 4.4 | 3% | 38x | casual 10 |
| `a new` | 70 | 62.1 | 60.3 | 5% | 8x | casual 33, angry 13, lazy 11 |
| `the three` | 15 | 13.3 | 0.9 | 3% | 25x | angry 7, formal 4, lazy 2 |
| `you tried` | 16 | 14.2 | 4.4 | 3% | 23x | casual 15, sexy 1 |
| `you actually` | 18 | 16.0 | 3.5 | 3% | 21x | casual 11, lazy 5, angry 2 |
| `of your` | 19 | 16.8 | 4.4 | 3% | 20x | angry 7, sexy 6, casual 5 |
| `on my` | 20 | 17.7 | 50.5 | 3% | 19x | sexy 8, casual 7, lazy 5 |
| `to do` | 24 | 21.3 | 20.4 | 3% | 16x | casual 20, angry 2, lazy 1 |
| `i did` | 25 | 22.2 | 30.1 | 3% | 15x | casual 20, lazy 4, sexy 1 |
| `take the` | 31 | 27.5 | 9.8 | 3% | 12x | casual 15, lazy 7, formal 4 |
| `all day` | 31 | 27.5 | 16.8 | 3% | 12x | lazy 15, casual 9, angry 4 |
| `what did you` | 33 | 29.3 | 28.4 | 3% | 11x | casual 26, sexy 6, lazy 1 |
| `better than` | 39 | 34.6 | 20.4 | 3% | 10x | casual 22, lazy 8, sexy 5 |
| `a day` | 39 | 34.6 | 21.3 | 3% | 10x | casual 21, lazy 11, angry 5 |
| `the room` | 41 | 36.4 | 23.1 | 3% | 9x | sexy 19, formal 9, angry 6 |
| `your own` | 49 | 43.4 | 6.2 | 3% | 8x | angry 24, casual 11, sexy 9 |
| `than the` | 49 | 43.4 | 67.4 | 3% | 8x | casual 15, sexy 12, formal 9 |
| `the car` | 51 | 45.2 | 39.9 | 3% | 7x | casual 26, sexy 14, lazy 9 |

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
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 9 | 11.7 | angry 5, formal 4 |
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
| `or is it` | 3 | formal 11, casual 7, angry 5 |
| `to be` | 5 | casual 13, lazy 8, sexy 4, angry 2 |
| `for it` | 5 | casual 23, lazy 7, formal 4, sexy 3 |
| `not a` | 4 | angry 21, casual 12, lazy 7, sexy 1 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `do that` | 2 | casual 8, sexy 1 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 23 |
| `it's been` | 1 | casual 10 |
| `a new` | 5 | casual 33, angry 13, lazy 11, formal 8 |
| `the three` | 5 | angry 7, formal 4, lazy 2, casual 1 |
| `you tried` | 2 | casual 15, sexy 1 |
| `you actually` | 3 | casual 11, lazy 5, angry 2 |
| `of your` | 4 | angry 7, sexy 6, casual 5, lazy 1 |
| `on my` | 3 | sexy 8, casual 7, lazy 5 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `i did` | 3 | casual 20, lazy 4, sexy 1 |
| `take the` | 5 | casual 15, lazy 7, formal 4, sexy 3 |
| `all day` | 5 | lazy 15, casual 9, angry 4, sexy 2 |
| `what did you` | 3 | casual 26, sexy 6, lazy 1 |
| `better than` | 4 | casual 22, lazy 8, sexy 5, formal 4 |
| `a day` | 4 | casual 21, lazy 11, angry 5, formal 2 |
| `the room` | 5 | sexy 19, formal 9, angry 6, casual 6 |
| `your own` | 5 | angry 24, casual 11, sexy 9, lazy 3 |
| `than the` | 5 | casual 15, sexy 12, formal 9, lazy 8 |
| `the car` | 5 | casual 26, sexy 14, lazy 9, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=11279): a 10.2%, the 5.7%, how 2.3%, did 2.3%, does 2.0%, why 1.8%
- assistant pos 1 (n=11279): the 10.9%, a 2.0%, is 1.8%, you 1.6%, does 1.6%, on 0.9%
- assistant pos 2 (n=11278): the 7.3%, a 3.1%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=11279): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11279): the 14.6%, my 9.7%, our 8.6%, i 6.5%, we 6.0%, you 5.3%
- user pos 1 (n=11216): the 3.1%, you 2.0%, a 1.6%, got 1.0%, is 1.0%, was 1.0%
- user pos 2 (n=11126): the 7.9%, a 3.6%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11279): it 2.2%, again 2.1%, now 1.2%, week 1.2%, night 1.0%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.7%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

