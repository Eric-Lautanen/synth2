# synth2 token-attractor map

Generated 2026-10-23 20:12  |  corpus 8730 rows, **11145 assistant turns**, 11145 user turns
Probe: `probe_out86_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T17:01:57

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.5% | 5.5% | +0.0 |
| `the`-opener (user) | 14.5% | 14.5% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i am` | 7% | 10% | 11x | 16x |
| `it is` | - | 8% | - | 7x |
| `you get` | 8% | 7% | 17x | 14x |
| `nothing else` | - | 3% | - | 46x |
| `a nice` | - | 3% | - | 41x |
| `how long` | - | 5% | - | 8x |
| `whole day` | - | 3% | - | 27x |
| `the three` | - | 3% | - | 27x |
| `the best` | - | 5% | - | 6x |
| `get it` | 3% | 3% | 22x | 22x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.5% | < 12% |
| `the`-opener (user) | 14.5% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 41 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i am` | 68 | 61.0 | 35.0 | 10% | 16x | casual 46, lazy 11, sexy 10 |
| `it is` | 136 | 122.0 | 53.8 | 8% | 7x | casual 82, lazy 36, angry 10 |
| `you get` | 55 | 49.3 | 44.9 | 7% | 14x | casual 45, angry 5, lazy 5 |
| `nothing else` | 8 | 7.2 | 5.4 | 3% | 46x | lazy 4, casual 2, angry 1 |
| `a nice` | 9 | 8.1 | 1.8 | 3% | 41x | casual 8, lazy 1 |
| `how long` | 68 | 61.0 | 16.2 | 5% | 8x | casual 31, sexy 15, formal 12 |
| `whole day` | 14 | 12.6 | 6.3 | 3% | 27x | angry 4, casual 4, lazy 4 |
| `the three` | 14 | 12.6 | 0.9 | 3% | 27x | angry 7, formal 3, lazy 2 |
| `the best` | 92 | 82.5 | 35.0 | 5% | 6x | casual 53, lazy 26, sexy 12 |
| `get it` | 17 | 15.3 | 1.8 | 3% | 22x | casual 11, lazy 3, sexy 2 |
| `doing the` | 18 | 16.2 | 9.9 | 3% | 21x | casual 15, sexy 2, lazy 1 |
| `the most` | 20 | 17.9 | 6.3 | 3% | 19x | lazy 11, casual 6, angry 2 |
| `enjoy the` | 23 | 20.6 | 0.0 | 3% | 16x | casual 14, lazy 8, sexy 1 |
| `the way` | 33 | 29.6 | 22.4 | 3% | 11x | casual 20, sexy 7, lazy 4 |
| `a bit` | 36 | 32.3 | 28.7 | 3% | 10x | casual 34, angry 1, lazy 1 |
| `through the` | 39 | 35.0 | 35.9 | 3% | 10x | sexy 15, casual 13, angry 7 |
| `should i` | 40 | 35.9 | 5.4 | 3% | 9x | sexy 40 |
| `not a` | 41 | 36.8 | 8.1 | 3% | 9x | angry 21, casual 12, lazy 7 |
| `a whole` | 48 | 43.1 | 25.1 | 3% | 8x | angry 19, lazy 16, casual 10 |
| `i will` | 55 | 49.3 | 8.1 | 3% | 7x | casual 31, lazy 14, sexy 10 |
| `did you` | 280 | 251.2 | 220.7 | 5% | 2x | casual 187, sexy 57, angry 28 |
| `that's the` | 60 | 53.8 | 18.8 | 3% | 6x | casual 60 |
| `a good` | 66 | 59.2 | 12.6 | 3% | 6x | casual 50, lazy 12, sexy 3 |
| `worth it` | 68 | 61.0 | 9.9 | 3% | 5x | casual 43, lazy 15, sexy 9 |
| `do you` | 107 | 96.0 | 47.6 | 3% | 3x | casual 73, angry 25, sexy 8 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 8 | 15.9 | angry 4, lazy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the front desk` | 3 | 14 | 12.5 | angry 8, lazy 4, casual 1 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.0 | lazy 6, casual 4, sexy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 4 |
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `nothing else` | 4 | lazy 4, casual 2, angry 1, sexy 1 |
| `a nice` | 2 | casual 8, lazy 1 |
| `how long` | 5 | casual 31, sexy 15, formal 12, angry 9 |
| `whole day` | 5 | angry 4, casual 4, lazy 4, formal 1 |
| `the three` | 5 | angry 7, formal 3, lazy 2, casual 1 |
| `the best` | 4 | casual 53, lazy 26, sexy 12, angry 1 |
| `get it` | 4 | casual 11, lazy 3, sexy 2, angry 1 |
| `doing the` | 3 | casual 15, sexy 2, lazy 1 |
| `the most` | 4 | lazy 11, casual 6, angry 2, sexy 1 |
| `enjoy the` | 3 | casual 14, lazy 8, sexy 1 |
| `the way` | 5 | casual 20, sexy 7, lazy 4, angry 1 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `through the` | 4 | sexy 15, casual 13, angry 7, lazy 4 |
| `should i` | 1 | sexy 40 |
| `not a` | 4 | angry 21, casual 12, lazy 7, sexy 1 |
| `a whole` | 5 | angry 19, lazy 16, casual 10, formal 2 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `that's the` | 1 | casual 60 |
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 1 |
| `worth it` | 4 | casual 43, lazy 15, sexy 9, angry 1 |
| `do you` | 4 | casual 73, angry 25, sexy 8, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=11145): a 10.2%, the 5.5%, how 2.3%, did 2.3%, does 1.9%, why 1.7%
- assistant pos 1 (n=11145): the 10.9%, a 2.0%, is 1.8%, you 1.6%, does 1.4%, on 0.9%
- assistant pos 2 (n=11144): the 7.2%, a 3.0%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=11145): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11145): the 14.5%, my 9.6%, our 8.5%, i 6.4%, we 6.1%, you 5.3%
- user pos 1 (n=11082): the 3.2%, you 2.1%, a 1.7%, got 1.0%, is 1.0%, was 1.0%
- user pos 2 (n=10992): the 7.9%, a 3.6%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11145): again 2.1%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.8%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

