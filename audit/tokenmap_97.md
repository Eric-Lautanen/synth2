# synth2 token-attractor map

Generated 2026-10-25 11:06  |  corpus 9500 rows, **11977 assistant turns**, 11977 user turns
Probe: `probe_out97_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T08:19:58

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.5% | 6.8% | +0.3 |
| `the`-opener (user) | 14.8% | 14.9% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `to do` | - | 5% | - | 25x |
| `is still` | - | 5% | - | 24x |
| `kind of` | - | 5% | - | 23x |
| `you asked` | - | 3% | - | 40x |
| `no idea` | - | 3% | - | 31x |
| `i do` | - | 3% | - | 31x |
| `still a` | - | 3% | - | 29x |
| `and i'm` | - | 3% | - | 29x |
| `a real` | - | 5% | - | 6x |
| `it on` | - | 3% | - | 21x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.8% | < 12% |
| `the`-opener (user) | 14.9% | n/a |
| copula-only turns | 0.8% | < 4% |
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
| `to do` | 24 | 20.0 | 19.2 | 5% | 25x | casual 20, angry 2, lazy 1 |
| `is still` | 25 | 20.9 | 14.2 | 5% | 24x | casual 12, lazy 8, angry 2 |
| `kind of` | 26 | 21.7 | 4.2 | 5% | 23x | casual 7, lazy 6, angry 5 |
| `you asked` | 10 | 8.3 | 4.2 | 3% | 40x | casual 4, angry 3, sexy 2 |
| `no idea` | 13 | 10.9 | 6.7 | 3% | 31x | casual 11, lazy 2 |
| `i do` | 13 | 10.9 | 10.9 | 3% | 31x | lazy 7, casual 5, sexy 1 |
| `still a` | 14 | 11.7 | 3.3 | 3% | 29x | casual 7, lazy 4, sexy 2 |
| `and i'm` | 14 | 11.7 | 10.0 | 3% | 29x | casual 13, sexy 1 |
| `a real` | 98 | 81.8 | 33.4 | 5% | 6x | casual 75, angry 13, lazy 10 |
| `it on` | 19 | 15.9 | 5.0 | 3% | 21x | casual 11, lazy 3, formal 2 |
| `it is` | 141 | 117.7 | 51.8 | 5% | 4x | casual 82, lazy 36, angry 10 |
| `a year` | 28 | 23.4 | 20.9 | 3% | 14x | formal 9, casual 8, lazy 7 |
| `going to` | 32 | 26.7 | 11.7 | 3% | 12x | casual 18, angry 6, lazy 5 |
| `is the` | 510 | 425.8 | 78.5 | 7% | 2x | casual 292, lazy 116, angry 50 |
| `this week` | 37 | 30.9 | 45.1 | 3% | 11x | casual 22, formal 5, angry 4 |
| `do it` | 37 | 30.9 | 8.3 | 3% | 11x | casual 24, lazy 11, formal 1 |
| `the car` | 53 | 44.3 | 40.9 | 3% | 8x | casual 26, sexy 14, lazy 9 |
| `about the` | 86 | 71.8 | 55.1 | 3% | 5x | casual 34, angry 25, sexy 14 |
| `the best` | 92 | 76.8 | 33.4 | 3% | 4x | casual 53, lazy 26, sexy 12 |
| `have you` | 113 | 94.3 | 20.0 | 3% | 4x | casual 80, angry 27, formal 3 |
| `are you` | 114 | 95.2 | 56.8 | 3% | 4x | casual 91, angry 12, sexy 10 |
| `yet the` | 8 | 6.7 | 0.0 | 2% | 25x | casual 6, lazy 2 |
| `people who` | 8 | 6.7 | 10.0 | 2% | 25x | formal 5, lazy 2, angry 1 |
| `once and` | 8 | 6.7 | 5.0 | 2% | 25x | casual 5, formal 2, sexy 1 |
| `nothing else` | 8 | 6.7 | 5.8 | 2% | 25x | lazy 4, casual 2, angry 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `shall i add` | 3 | 8 | 17.3 | formal 8 |
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 15.9 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the office manager` | 3 | 9 | 12.5 | formal 9 |
| `i have been` | 3 | 10 | 12.5 | casual 8, lazy 2 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `the front desk` | 3 | 14 | 12.0 | angry 8, lazy 4, casual 1 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.3 | casual 9, angry 3, formal 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `is still` | 5 | casual 12, lazy 8, angry 2, sexy 2 |
| `kind of` | 5 | casual 7, lazy 6, angry 5, formal 4 |
| `you asked` | 4 | casual 4, angry 3, sexy 2, lazy 1 |
| `no idea` | 2 | casual 11, lazy 2 |
| `i do` | 3 | lazy 7, casual 5, sexy 1 |
| `still a` | 4 | casual 7, lazy 4, sexy 2, angry 1 |
| `and i'm` | 2 | casual 13, sexy 1 |
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `it on` | 5 | casual 11, lazy 3, formal 2, sexy 2 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `a year` | 5 | formal 9, casual 8, lazy 7, angry 3 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 36 |
| `this week` | 5 | casual 22, formal 5, angry 4, lazy 4 |
| `do it` | 4 | casual 24, lazy 11, formal 1, sexy 1 |
| `the car` | 5 | casual 26, sexy 14, lazy 9, formal 3 |
| `about the` | 5 | casual 34, angry 25, sexy 14, formal 11 |
| `the best` | 4 | casual 53, lazy 26, sexy 12, angry 1 |
| `have you` | 4 | casual 80, angry 27, formal 3, sexy 3 |
| `are you` | 4 | casual 91, angry 12, sexy 10, lazy 1 |
| `yet the` | 2 | casual 6, lazy 2 |
| `people who` | 3 | formal 5, lazy 2, angry 1 |
| `once and` | 3 | casual 5, formal 2, sexy 1 |
| `nothing else` | 4 | lazy 4, casual 2, angry 1, sexy 1 |

## 4. Opener maps

- assistant pos 0 (n=11977): a 10.0%, the 6.8%, does 2.7%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=11977): the 11.3%, a 2.1%, is 1.7%, does 1.6%, you 1.6%, on 0.9%
- assistant pos 2 (n=11976): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11977): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11977): the 14.9%, my 9.4%, our 9.0%, i 6.6%, we 5.8%, you 5.0%
- user pos 1 (n=11914): the 3.3%, you 2.0%, a 1.6%, is 1.2%, got 1.0%, was 0.9%
- user pos 2 (n=11824): the 8.1%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=11977): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

