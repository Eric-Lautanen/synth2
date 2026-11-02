# synth2 token-attractor map

Generated 2026-10-17 06:09  |  corpus 5924 rows, **8113 assistant turns**, 8113 user turns
Probe: `probe_out43_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T18:23:55

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.9% | 3.0% | +0.0 |
| `the`-opener (user) | 12.8% | 13.0% | +0.2 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i know` | - | 7% | - | 30x |
| `and i` | - | 8% | - | 13x |
| `i've been` | - | 5% | - | 29x |
| `you tried` | 3% | 5% | 13x | 27x |
| `did the` | - | 8% | - | 3x |
| `the old` | - | 5% | - | 11x |
| `good the` | - | 3% | - | 34x |
| `i am` | 7% | 5% | 9x | 7x |
| `with one` | - | 3% | - | 30x |
| `week and` | - | 3% | - | 30x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 13.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
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
| `i know` | 18 | 22.2 | 16.0 | 7% | 30x | casual 16, lazy 2 |
| `and i` | 54 | 66.6 | 98.6 | 8% | 13x | casual 29, lazy 25 |
| `i've been` | 14 | 17.3 | 19.7 | 5% | 29x | casual 14 |
| `you tried` | 15 | 18.5 | 3.7 | 5% | 27x | casual 15 |
| `did the` | 256 | 315.5 | 86.3 | 8% | 3x | angry 128, casual 125, lazy 3 |
| `the old` | 36 | 44.4 | 29.6 | 5% | 11x | casual 18, lazy 13, angry 5 |
| `good the` | 8 | 9.9 | 0.0 | 3% | 34x | casual 8 |
| `i am` | 56 | 69.0 | 44.4 | 5% | 7x | casual 44, lazy 11, angry 1 |
| `with one` | 9 | 11.1 | 6.2 | 3% | 30x | casual 4, lazy 4, angry 1 |
| `week and` | 9 | 11.1 | 9.9 | 3% | 30x | casual 9 |
| `my sister` | 9 | 11.1 | 23.4 | 3% | 30x | casual 8, lazy 1 |
| `a time` | 10 | 12.3 | 2.5 | 3% | 27x | lazy 5, casual 4, angry 1 |
| `old one` | 11 | 13.6 | 8.6 | 3% | 25x | casual 6, lazy 4, angry 1 |
| `i do` | 12 | 14.8 | 13.6 | 3% | 23x | lazy 7, casual 5 |
| `good luck` | 12 | 14.8 | 0.0 | 3% | 23x | casual 9, lazy 2, angry 1 |
| `the washing` | 16 | 19.7 | 16.0 | 3% | 17x | casual 15, lazy 1 |
| `is it` | 107 | 131.9 | 27.1 | 5% | 4x | casual 100, angry 7 |
| `you do` | 20 | 24.7 | 18.5 | 3% | 14x | casual 17, angry 3 |
| `i did` | 23 | 28.3 | 37.0 | 3% | 12x | casual 19, lazy 4 |
| `to a` | 26 | 32.0 | 37.0 | 3% | 10x | angry 12, casual 9, lazy 5 |
| `do not` | 26 | 32.0 | 7.4 | 3% | 10x | casual 13, lazy 12, angry 1 |
| `the last` | 35 | 43.1 | 33.3 | 3% | 8x | casual 21, lazy 10, angry 4 |
| `a day` | 35 | 43.1 | 24.7 | 3% | 8x | casual 19, lazy 11, angry 5 |
| `when the` | 44 | 54.2 | 7.4 | 3% | 6x | angry 19, lazy 18, casual 7 |
| `did you` | 225 | 277.3 | 303.2 | 5% | 2x | casual 192, angry 28, lazy 5 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.3 | casual 10, lazy 1 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 12 | 13.2 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.6 | angry 4, casual 4 |
| `feels like a` | 3 | 8 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.3 | angry 4, lazy 4, casual 2 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `an hour of` | 3 | 10 | 12.1 | angry 6, casual 2, lazy 2 |
| `for an hour` | 3 | 10 | 11.6 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.6 | casual 5, lazy 2, angry 1 |
| `did they really` | 3 | 8 | 11.6 | angry 8 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.1 | casual 9, angry 3 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `did you find` | 3 | 9 | 10.9 | casual 9 |
| `did you get` | 3 | 44 | 10.8 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.8 | casual 7, lazy 1 |
| `why would a` | 3 | 8 | 10.6 | angry 8 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i know` | 2 | casual 16, lazy 2 |
| `and i` | 2 | casual 29, lazy 25 |
| `i've been` | 1 | casual 14 |
| `you tried` | 1 | casual 15 |
| `did the` | 3 | angry 128, casual 125, lazy 3 |
| `the old` | 3 | casual 18, lazy 13, angry 5 |
| `good the` | 1 | casual 8 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `with one` | 3 | casual 4, lazy 4, angry 1 |
| `week and` | 1 | casual 9 |
| `my sister` | 2 | casual 8, lazy 1 |
| `a time` | 3 | lazy 5, casual 4, angry 1 |
| `old one` | 3 | casual 6, lazy 4, angry 1 |
| `i do` | 2 | lazy 7, casual 5 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `the washing` | 2 | casual 15, lazy 1 |
| `is it` | 2 | casual 100, angry 7 |
| `you do` | 2 | casual 17, angry 3 |
| `i did` | 2 | casual 19, lazy 4 |
| `to a` | 3 | angry 12, casual 9, lazy 5 |
| `do not` | 3 | casual 13, lazy 12, angry 1 |
| `the last` | 3 | casual 21, lazy 10, angry 4 |
| `a day` | 3 | casual 19, lazy 11, angry 5 |
| `when the` | 3 | angry 19, lazy 18, casual 7 |
| `did you` | 3 | casual 192, angry 28, lazy 5 |

## 4. Opener maps

- assistant pos 0 (n=8113): a 7.9%, the 3.0%, did 2.6%, how 2.5%, was 2.1%, that 2.0%
- assistant pos 1 (n=8113): the 11.8%, a 2.4%, is 2.1%, you 2.0%, does 1.4%, it 1.0%
- assistant pos 2 (n=8112): the 6.2%, a 3.2%, is 3.2%, are 2.1%, of 1.7%, for 1.7%
- assistant pos last (n=8113): it 4.3%, now 1.4%, time 1.3%, you 1.1%, one 1.0%, again 0.9%
- user pos 0 (n=8113): the 13.0%, my 10.7%, our 8.2%, i 6.5%, did 3.2%, they 3.2%
- user pos 1 (n=8050): the 4.0%, you 2.8%, a 2.3%, was 1.3%, did 1.2%, is 1.1%
- user pos 2 (n=7961): the 6.7%, a 2.9%, is 2.1%, you 1.6%, and 1.4%, my 1.3%
- user pos last (n=8113): again 2.6%, it 1.9%, now 1.5%, week 1.5%, today 1.2%, night 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.4%**; model outputs: **18.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| lazy | 1 / 2155 |

