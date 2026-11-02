# synth2 token-attractor map

Generated 2026-10-16 04:11  |  corpus 4994 rows, **7108 assistant turns**, 7108 user turns
Probe: `probe_out34_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T02:48:16

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.1% | 3.1% | -0.1 |
| `the`-opener (user) | 12.2% | 12.5% | +0.3 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 5% | 8% | 4x | 7x |
| `i am` | - | 7% | - | 8x |
| `that is a` | - | 5% | - | 21x |
| `this week` | - | 5% | - | 11x |
| `of you` | - | 3% | - | 30x |
| `or the` | - | 5% | - | 6x |
| `was not` | - | 3% | - | 26x |
| `seem to` | - | 3% | - | 26x |
| `new place` | - | 3% | - | 26x |
| `two hundred` | - | 3% | - | 24x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.1% | < 12% |
| `the`-opener (user) | 12.5% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 43 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a good` | 85 | 119.6 | 15.5 | 8% | 7x | casual 69, lazy 16 |
| `i am` | 56 | 78.8 | 47.8 | 7% | 8x | casual 44, lazy 11, angry 1 |
| `that is a` | 17 | 23.9 | 0.0 | 5% | 21x | casual 14, angry 2, lazy 1 |
| `this week` | 33 | 46.4 | 63.3 | 5% | 11x | casual 26, lazy 4, angry 3 |
| `of you` | 8 | 11.3 | 0.0 | 3% | 30x | casual 5, lazy 2, angry 1 |
| `or the` | 55 | 77.4 | 2.8 | 5% | 6x | casual 49, angry 3, lazy 3 |
| `was not` | 9 | 12.7 | 4.2 | 3% | 26x | casual 7, angry 1, lazy 1 |
| `seem to` | 9 | 12.7 | 0.0 | 3% | 26x | lazy 8, casual 1 |
| `new place` | 9 | 12.7 | 9.8 | 3% | 26x | casual 7, lazy 2 |
| `two hundred` | 10 | 14.1 | 14.1 | 3% | 24x | casual 9, angry 1 |
| `at all` | 63 | 88.6 | 23.9 | 5% | 6x | casual 36, angry 21, lazy 6 |
| `the neighbors` | 11 | 15.5 | 19.7 | 3% | 22x | casual 7, lazy 4 |
| `you want` | 12 | 16.9 | 7.0 | 3% | 20x | casual 7, lazy 4, angry 1 |
| `did you` | 216 | 303.9 | 346.1 | 7% | 2x | casual 192, angry 19, lazy 5 |
| `and i'm` | 13 | 18.3 | 16.9 | 3% | 18x | casual 13 |
| `the same` | 81 | 114.0 | 81.6 | 5% | 4x | casual 36, lazy 29, angry 16 |
| `the game` | 16 | 22.5 | 25.3 | 3% | 15x | casual 12, lazy 4 |
| `i was` | 16 | 22.5 | 35.2 | 3% | 15x | casual 14, lazy 2 |
| `you do` | 18 | 25.3 | 21.1 | 3% | 13x | casual 17, angry 1 |
| `what was` | 19 | 26.7 | 9.8 | 3% | 12x | casual 17, angry 1, lazy 1 |
| `the night` | 19 | 26.7 | 7.0 | 3% | 12x | lazy 9, casual 7, angry 3 |
| `you tried` | 22 | 31.0 | 4.2 | 3% | 11x | casual 15, angry 7 |
| `out the` | 23 | 32.4 | 35.2 | 3% | 10x | lazy 11, casual 9, angry 3 |
| `to the` | 124 | 174.5 | 170.2 | 5% | 3x | casual 75, lazy 32, angry 17 |
| `worth the` | 34 | 47.8 | 11.3 | 3% | 7x | casual 21, lazy 13 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.7 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.5 | casual 10, lazy 1 |
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.9 | angry 4, casual 4 |
| `the post office` | 3 | 8 | 12.8 | casual 7, lazy 1 |
| `two hours of` | 3 | 8 | 12.5 | lazy 4, angry 2, casual 2 |
| `you able to` | 3 | 8 | 12.4 | angry 8 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `for an hour` | 3 | 10 | 12.1 | casual 8, angry 1, lazy 1 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.5 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.8 | casual 8 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.3 | lazy 4, angry 2, casual 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 2 | casual 69, lazy 16 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `that is a` | 3 | casual 14, angry 2, lazy 1 |
| `this week` | 3 | casual 26, lazy 4, angry 3 |
| `of you` | 3 | casual 5, lazy 2, angry 1 |
| `or the` | 3 | casual 49, angry 3, lazy 3 |
| `was not` | 3 | casual 7, angry 1, lazy 1 |
| `seem to` | 2 | lazy 8, casual 1 |
| `new place` | 2 | casual 7, lazy 2 |
| `two hundred` | 2 | casual 9, angry 1 |
| `at all` | 3 | casual 36, angry 21, lazy 6 |
| `the neighbors` | 2 | casual 7, lazy 4 |
| `you want` | 3 | casual 7, lazy 4, angry 1 |
| `did you` | 3 | casual 192, angry 19, lazy 5 |
| `and i'm` | 1 | casual 13 |
| `the same` | 3 | casual 36, lazy 29, angry 16 |
| `the game` | 2 | casual 12, lazy 4 |
| `i was` | 2 | casual 14, lazy 2 |
| `you do` | 2 | casual 17, angry 1 |
| `what was` | 3 | casual 17, angry 1, lazy 1 |
| `the night` | 3 | lazy 9, casual 7, angry 3 |
| `you tried` | 2 | casual 15, angry 7 |
| `out the` | 3 | lazy 11, casual 9, angry 3 |
| `to the` | 3 | casual 75, lazy 32, angry 17 |
| `worth the` | 2 | casual 21, lazy 13 |

## 4. Opener maps

- assistant pos 0 (n=7108): a 7.7%, the 3.1%, did 2.5%, that 2.3%, was 2.1%, haha 1.9%
- assistant pos 1 (n=7108): the 12.4%, a 2.4%, you 2.3%, is 2.0%, it 1.2%, and 0.9%
- assistant pos 2 (n=7107): the 5.8%, is 3.6%, are 2.4%, a 2.3%, of 1.6%, for 1.3%
- assistant pos last (n=7108): it 4.6%, now 1.5%, time 1.5%, one 1.1%, again 1.0%, day 0.9%
- user pos 0 (n=7108): the 12.5%, my 10.3%, our 8.5%, i 6.9%, did 3.6%, a 3.0%
- user pos 1 (n=7045): the 4.4%, you 3.2%, a 2.6%, was 1.4%, did 1.4%, is 1.3%
- user pos 2 (n=6956): the 6.7%, a 2.9%, is 2.3%, you 1.8%, and 1.6%, got 1.4%
- user pos last (n=7108): again 2.8%, it 1.8%, now 1.7%, week 1.6%, today 1.4%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.2%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

