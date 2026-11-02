# synth2 token-attractor map

Generated 2026-10-16 07:20  |  corpus 5118 rows, **7242 assistant turns**, 7242 user turns
Probe: `probe_out36_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T05:36:37

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | -0.0 |
| `the`-opener (user) | 12.5% | 12.7% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `get a` | - | 7% | - | 25x |
| `new one` | - | 5% | - | 33x |
| `a good` | 7% | 7% | 6x | 6x |
| `is it` | 7% | 7% | 5x | 5x |
| `it is` | 5% | 7% | 3x | 4x |
| `the real` | - | 5% | - | 8x |
| `a new` | - | 5% | - | 7x |
| `is the` | - | 8% | - | 2x |
| `new place` | - | 3% | - | 27x |
| `months of` | - | 3% | - | 27x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 12.7% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
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
| `get a` | 19 | 26.2 | 9.7 | 7% | 25x | casual 15, lazy 3, angry 1 |
| `new one` | 11 | 15.2 | 12.4 | 5% | 33x | casual 7, lazy 3, angry 1 |
| `a good` | 85 | 117.4 | 15.2 | 7% | 6x | casual 69, lazy 16 |
| `is it` | 106 | 146.4 | 30.4 | 7% | 5x | casual 100, angry 6 |
| `it is` | 116 | 160.2 | 69.0 | 7% | 4x | casual 79, lazy 36, angry 1 |
| `the real` | 44 | 60.8 | 12.4 | 5% | 8x | lazy 23, casual 21 |
| `a new` | 54 | 74.6 | 78.7 | 5% | 7x | casual 37, lazy 11, angry 6 |
| `is the` | 400 | 552.3 | 95.3 | 8% | 2x | casual 251, lazy 116, angry 33 |
| `new place` | 9 | 12.4 | 9.7 | 3% | 27x | casual 7, lazy 2 |
| `months of` | 9 | 12.4 | 8.3 | 3% | 27x | casual 6, angry 2, lazy 1 |
| `is in` | 9 | 12.4 | 12.4 | 3% | 27x | casual 5, lazy 3, angry 1 |
| `worth it` | 58 | 80.1 | 12.4 | 5% | 6x | casual 42, lazy 15, angry 1 |
| `the new` | 58 | 80.1 | 87.0 | 5% | 6x | casual 35, angry 12, lazy 11 |
| `it this` | 10 | 13.8 | 4.1 | 3% | 24x | casual 9, lazy 1 |
| `a gift` | 10 | 13.8 | 0.0 | 3% | 24x | lazy 5, casual 4, angry 1 |
| `to get` | 12 | 16.6 | 12.4 | 3% | 20x | casual 7, angry 3, lazy 2 |
| `was a` | 13 | 18.0 | 23.5 | 3% | 19x | casual 11, angry 1, lazy 1 |
| `still a` | 13 | 18.0 | 4.1 | 3% | 19x | casual 8, lazy 4, angry 1 |
| `you actually` | 16 | 22.1 | 2.8 | 3% | 15x | casual 11, lazy 5 |
| `on sunday` | 16 | 22.1 | 33.1 | 3% | 15x | casual 16 |
| `of them` | 16 | 22.1 | 23.5 | 3% | 15x | casual 11, lazy 4, angry 1 |
| `here too` | 17 | 23.5 | 0.0 | 3% | 14x | casual 17 |
| `a real` | 104 | 143.6 | 60.8 | 5% | 3x | casual 82, angry 12, lazy 10 |
| `what's the` | 21 | 29.0 | 16.6 | 3% | 11x | casual 21 |
| `it for` | 25 | 34.5 | 18.0 | 3% | 10x | casual 18, lazy 7 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.6 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.5 | casual 10, lazy 1 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `the front desk` | 3 | 12 | 13.4 | angry 7, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.8 | angry 4, casual 4 |
| `the post office` | 3 | 8 | 12.8 | casual 7, lazy 1 |
| `two hours of` | 3 | 9 | 12.5 | lazy 4, angry 3, casual 2 |
| `i have been` | 3 | 11 | 12.4 | casual 9, lazy 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `for an hour` | 3 | 10 | 12.0 | casual 8, angry 1, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.5 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 10.9 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.8 | casual 8 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `a lot of` | 3 | 10 | 10.1 | casual 7, lazy 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `get a` | 3 | casual 15, lazy 3, angry 1 |
| `new one` | 3 | casual 7, lazy 3, angry 1 |
| `a good` | 2 | casual 69, lazy 16 |
| `is it` | 2 | casual 100, angry 6 |
| `it is` | 3 | casual 79, lazy 36, angry 1 |
| `the real` | 2 | lazy 23, casual 21 |
| `a new` | 3 | casual 37, lazy 11, angry 6 |
| `is the` | 3 | casual 251, lazy 116, angry 33 |
| `new place` | 2 | casual 7, lazy 2 |
| `months of` | 3 | casual 6, angry 2, lazy 1 |
| `is in` | 3 | casual 5, lazy 3, angry 1 |
| `worth it` | 3 | casual 42, lazy 15, angry 1 |
| `the new` | 3 | casual 35, angry 12, lazy 11 |
| `it this` | 2 | casual 9, lazy 1 |
| `a gift` | 3 | lazy 5, casual 4, angry 1 |
| `to get` | 3 | casual 7, angry 3, lazy 2 |
| `was a` | 3 | casual 11, angry 1, lazy 1 |
| `still a` | 3 | casual 8, lazy 4, angry 1 |
| `you actually` | 2 | casual 11, lazy 5 |
| `on sunday` | 1 | casual 16 |
| `of them` | 3 | casual 11, lazy 4, angry 1 |
| `here too` | 1 | casual 17 |
| `a real` | 3 | casual 82, angry 12, lazy 10 |
| `what's the` | 1 | casual 21 |
| `it for` | 2 | casual 18, lazy 7 |

## 4. Opener maps

- assistant pos 0 (n=7242): a 7.7%, the 3.0%, did 2.6%, that 2.3%, was 2.2%, haha 1.8%
- assistant pos 1 (n=7242): the 12.4%, a 2.3%, you 2.3%, is 2.0%, it 1.1%, and 0.9%
- assistant pos 2 (n=7241): the 5.8%, is 3.5%, a 2.5%, are 2.3%, of 1.6%, for 1.3%
- assistant pos last (n=7242): it 4.6%, now 1.5%, time 1.4%, one 1.1%, again 1.0%, day 0.9%
- user pos 0 (n=7242): the 12.7%, my 10.3%, our 8.4%, i 6.9%, did 3.6%, a 3.0%
- user pos 1 (n=7179): the 4.3%, you 3.1%, a 2.5%, was 1.4%, did 1.4%, is 1.3%
- user pos 2 (n=7090): the 6.6%, a 2.9%, is 2.3%, you 1.8%, and 1.6%, got 1.4%
- user pos last (n=7242): again 2.8%, it 1.8%, now 1.7%, week 1.6%, today 1.4%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.1%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

