# synth2 token-attractor map

Generated 2026-10-23 02:17  |  corpus 8420 rows, **10810 assistant turns**, 10810 user turns
Probe: `probe_out81_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T22:22:46

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.2% | 5.3% | +0.1 |
| `the`-opener (user) | 14.3% | 14.4% | +0.1 |
| copula-only | 0.7% | 0.7% | +0.1 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `have been` | 3% | 8% | 19x | 47x |
| `i have` | 5% | 7% | 11x | 14x |
| `out of the` | - | 5% | - | 32x |
| `this week` | 3% | 5% | 11x | 16x |
| `much better` | - | 3% | - | 45x |
| `for a` | - | 7% | - | 3x |
| `the wait` | - | 3% | - | 36x |
| `no idea` | 3% | 3% | 28x | 28x |
| `i got` | - | 3% | - | 26x |
| `i would` | - | 3% | - | 23x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.3% | < 12% |
| `the`-opener (user) | 14.4% | n/a |
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
| `have been` | 19 | 17.6 | 39.8 | 8% | 47x | casual 12, lazy 4, sexy 2 |
| `i have` | 50 | 46.3 | 80.5 | 7% | 14x | casual 34, lazy 12, sexy 4 |
| `out of the` | 17 | 15.7 | 17.6 | 5% | 32x | casual 12, lazy 3, angry 2 |
| `this week` | 33 | 30.5 | 44.4 | 5% | 16x | casual 22, angry 4, lazy 4 |
| `much better` | 8 | 7.4 | 0.9 | 3% | 45x | casual 7, lazy 1 |
| `for a` | 210 | 194.3 | 162.8 | 7% | 3x | angry 93, casual 66, lazy 23 |
| `the wait` | 10 | 9.3 | 7.4 | 3% | 36x | lazy 4, casual 3, sexy 3 |
| `no idea` | 13 | 12.0 | 7.4 | 3% | 28x | casual 11, lazy 2 |
| `i got` | 14 | 13.0 | 44.4 | 3% | 26x | casual 12, lazy 1, sexy 1 |
| `i would` | 16 | 14.8 | 3.7 | 3% | 23x | casual 8, angry 4, lazy 2 |
| `to you` | 21 | 19.4 | 0.9 | 3% | 17x | angry 9, sexy 7, casual 2 |
| `to do` | 24 | 22.2 | 21.3 | 3% | 15x | casual 20, angry 2, lazy 1 |
| `should i` | 40 | 37.0 | 5.6 | 3% | 9x | sexy 40 |
| `more than` | 46 | 42.6 | 36.1 | 3% | 8x | casual 18, lazy 11, sexy 11 |
| `i will` | 55 | 50.9 | 8.3 | 3% | 7x | casual 31, lazy 14, sexy 10 |
| `how many` | 61 | 56.4 | 5.6 | 3% | 6x | casual 35, angry 13, sexy 8 |
| `a good` | 65 | 60.1 | 13.0 | 3% | 6x | casual 50, lazy 12, sexy 3 |
| `i am` | 68 | 62.9 | 36.1 | 3% | 5x | casual 46, lazy 11, sexy 10 |
| `at least` | 72 | 66.6 | 12.0 | 3% | 5x | casual 31, angry 20, sexy 12 |
| `on the` | 360 | 333.0 | 302.5 | 5% | 2x | casual 138, sexy 111, lazy 51 |
| `was it` | 83 | 76.8 | 19.4 | 3% | 4x | casual 68, sexy 11, angry 4 |
| `the same` | 121 | 111.9 | 113.8 | 3% | 3x | angry 34, casual 34, lazy 29 |
| `is it` | 124 | 114.7 | 22.2 | 3% | 3x | casual 103, formal 10, angry 7 |
| `and the` | 147 | 136.0 | 194.3 | 3% | 2x | formal 56, casual 55, lazy 15 |
| `my sister` | 8 | 7.4 | 18.5 | 2% | 23x | casual 7, lazy 1 |

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
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `the front desk` | 3 | 13 | 12.7 | angry 8, lazy 4, casual 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `counts as a` | 3 | 12 | 12.4 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `how long has` | 3 | 9 | 12.2 | formal 4, casual 3, angry 2 |
| `an hour of` | 3 | 15 | 12.2 | angry 6, casual 3, sexy 3 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `have been` | 4 | casual 12, lazy 4, sexy 2, angry 1 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `out of the` | 3 | casual 12, lazy 3, angry 2 |
| `this week` | 5 | casual 22, angry 4, lazy 4, sexy 2 |
| `much better` | 2 | casual 7, lazy 1 |
| `for a` | 5 | angry 93, casual 66, lazy 23, sexy 23 |
| `the wait` | 3 | lazy 4, casual 3, sexy 3 |
| `no idea` | 2 | casual 11, lazy 2 |
| `i got` | 3 | casual 12, lazy 1, sexy 1 |
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `to you` | 5 | angry 9, sexy 7, casual 2, formal 2 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `should i` | 1 | sexy 40 |
| `more than` | 5 | casual 18, lazy 11, sexy 11, angry 3 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `how many` | 5 | casual 35, angry 13, sexy 8, formal 3 |
| `a good` | 3 | casual 50, lazy 12, sexy 3 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `at least` | 4 | casual 31, angry 20, sexy 12, lazy 9 |
| `on the` | 5 | casual 138, sexy 111, lazy 51, angry 50 |
| `was it` | 3 | casual 68, sexy 11, angry 4 |
| `the same` | 5 | angry 34, casual 34, lazy 29, sexy 14 |
| `is it` | 4 | casual 103, formal 10, angry 7, sexy 4 |
| `and the` | 5 | formal 56, casual 55, lazy 15, angry 13 |
| `my sister` | 2 | casual 7, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=10810): a 10.1%, the 5.3%, did 2.3%, how 2.2%, that 1.7%, why 1.6%
- assistant pos 1 (n=10810): the 11.0%, a 2.0%, is 1.8%, you 1.7%, does 1.2%, on 1.0%
- assistant pos 2 (n=10809): the 7.0%, a 2.8%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10810): it 3.9%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10810): the 14.4%, my 9.8%, our 8.4%, i 6.2%, we 6.1%, you 5.5%
- user pos 1 (n=10747): the 3.2%, you 2.1%, a 1.7%, was 1.0%, got 1.0%, did 0.9%
- user pos 2 (n=10657): the 7.8%, a 3.4%, is 1.7%, my 1.4%, you 1.4%, was 1.2%
- user pos last (n=10810): again 2.2%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.9%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

