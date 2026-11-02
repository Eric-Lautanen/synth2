# synth2 token-attractor map

Generated 2026-10-16 18:23  |  corpus 5800 rows, **7979 assistant turns**, 7979 user turns
Probe: `probe_out42_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T15:45:34

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 2.9% | -0.1 |
| `the`-opener (user) | 12.8% | 12.8% | +0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `did you` | 8% | 10% | 3x | 4x |
| `i am` | - | 7% | - | 9x |
| `night before` | - | 3% | - | 27x |
| `least the` | - | 3% | - | 27x |
| `no idea` | 3% | 3% | 22x | 22x |
| `is on` | - | 3% | - | 20x |
| `the first` | - | 5% | - | 5x |
| `they are` | - | 3% | - | 17x |
| `the washing` | - | 3% | - | 17x |
| `you the` | - | 3% | - | 15x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.9% | < 12% |
| `the`-opener (user) | 12.8% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
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
| `did you` | 225 | 282.0 | 308.3 | 10% | 4x | casual 192, angry 28, lazy 5 |
| `i am` | 56 | 70.2 | 43.9 | 7% | 9x | casual 44, lazy 11, angry 1 |
| `night before` | 10 | 12.5 | 5.0 | 3% | 27x | casual 6, angry 2, lazy 2 |
| `least the` | 10 | 12.5 | 1.3 | 3% | 27x | casual 6, lazy 4 |
| `no idea` | 12 | 15.0 | 10.0 | 3% | 22x | casual 10, lazy 2 |
| `is on` | 13 | 16.3 | 21.3 | 3% | 20x | casual 11, lazy 2 |
| `the first` | 85 | 106.5 | 75.2 | 5% | 5x | casual 40, lazy 38, angry 7 |
| `they are` | 16 | 20.1 | 3.8 | 3% | 17x | casual 11, lazy 5 |
| `the washing` | 16 | 20.1 | 16.3 | 3% | 17x | casual 15, lazy 1 |
| `you the` | 18 | 22.6 | 1.3 | 3% | 15x | angry 8, casual 8, lazy 2 |
| `have been` | 18 | 22.6 | 41.4 | 3% | 15x | casual 13, lazy 4, angry 1 |
| `for once` | 19 | 23.8 | 11.3 | 3% | 14x | casual 17, lazy 2 |
| `the night` | 20 | 25.1 | 10.0 | 3% | 13x | lazy 9, casual 7, angry 4 |
| `you tried` | 21 | 26.3 | 3.8 | 3% | 13x | casual 15, angry 6 |
| `it is` | 119 | 149.1 | 65.2 | 5% | 3x | casual 79, lazy 36, angry 4 |
| `the fridge` | 24 | 30.1 | 30.1 | 3% | 11x | casual 12, lazy 10, angry 2 |
| `about it` | 25 | 31.3 | 31.3 | 3% | 11x | casual 19, lazy 4, angry 2 |
| `a single` | 25 | 31.3 | 18.8 | 3% | 11x | angry 24, casual 1 |
| `or a` | 30 | 37.6 | 1.3 | 3% | 9x | casual 25, lazy 4, angry 1 |
| `in one` | 35 | 43.9 | 28.8 | 3% | 8x | lazy 15, angry 13, casual 7 |
| `is not` | 45 | 56.4 | 11.3 | 3% | 6x | angry 27, casual 12, lazy 6 |
| `i have` | 47 | 58.9 | 91.5 | 3% | 6x | casual 35, lazy 12 |
| `what did` | 60 | 75.2 | 51.4 | 3% | 4x | casual 41, angry 18, lazy 1 |
| `at least` | 62 | 77.7 | 16.3 | 3% | 4x | casual 33, angry 20, lazy 9 |
| `at all` | 63 | 79.0 | 22.6 | 3% | 4x | casual 36, angry 21, lazy 6 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.5 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.6 | angry 8 |
| `an early night` | 3 | 11 | 14.4 | casual 10, lazy 1 |
| `have you tried` | 3 | 21 | 13.9 | casual 15, angry 6 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.6 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `two hours of` | 3 | 10 | 12.3 | angry 4, lazy 4, casual 2 |
| `you able to` | 3 | 8 | 12.2 | angry 8 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `an hour of` | 3 | 10 | 12.1 | angry 6, casual 2, lazy 2 |
| `for an hour` | 3 | 10 | 11.7 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.6 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.2 | casual 9, angry 3 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 10.8 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.8 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `did you` | 3 | casual 192, angry 28, lazy 5 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `night before` | 3 | casual 6, angry 2, lazy 2 |
| `least the` | 2 | casual 6, lazy 4 |
| `no idea` | 2 | casual 10, lazy 2 |
| `is on` | 2 | casual 11, lazy 2 |
| `the first` | 3 | casual 40, lazy 38, angry 7 |
| `they are` | 2 | casual 11, lazy 5 |
| `the washing` | 2 | casual 15, lazy 1 |
| `you the` | 3 | angry 8, casual 8, lazy 2 |
| `have been` | 3 | casual 13, lazy 4, angry 1 |
| `for once` | 2 | casual 17, lazy 2 |
| `the night` | 3 | lazy 9, casual 7, angry 4 |
| `you tried` | 2 | casual 15, angry 6 |
| `it is` | 3 | casual 79, lazy 36, angry 4 |
| `the fridge` | 3 | casual 12, lazy 10, angry 2 |
| `about it` | 3 | casual 19, lazy 4, angry 2 |
| `a single` | 2 | angry 24, casual 1 |
| `or a` | 3 | casual 25, lazy 4, angry 1 |
| `in one` | 3 | lazy 15, angry 13, casual 7 |
| `is not` | 3 | angry 27, casual 12, lazy 6 |
| `i have` | 2 | casual 35, lazy 12 |
| `what did` | 3 | casual 41, angry 18, lazy 1 |
| `at least` | 3 | casual 33, angry 20, lazy 9 |
| `at all` | 3 | casual 36, angry 21, lazy 6 |

## 4. Opener maps

- assistant pos 0 (n=7979): a 8.0%, the 2.9%, did 2.6%, how 2.4%, was 2.1%, that 2.1%
- assistant pos 1 (n=7979): the 11.7%, a 2.3%, you 2.2%, is 2.1%, does 1.4%, it 1.0%
- assistant pos 2 (n=7978): the 6.0%, a 3.2%, is 3.2%, are 2.1%, of 1.7%, for 1.6%
- assistant pos last (n=7979): it 4.3%, now 1.4%, time 1.3%, you 1.0%, one 1.0%, again 0.9%
- user pos 0 (n=7979): the 12.8%, my 10.8%, our 8.1%, i 6.6%, did 3.2%, they 3.0%
- user pos 1 (n=7916): the 4.0%, you 2.8%, a 2.3%, was 1.4%, did 1.2%, is 1.1%
- user pos 2 (n=7827): the 6.7%, a 2.9%, is 2.1%, you 1.6%, and 1.4%, my 1.3%
- user pos last (n=7979): again 2.6%, it 1.9%, now 1.5%, week 1.5%, today 1.3%, night 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.5%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| lazy | 1 / 2155 |

