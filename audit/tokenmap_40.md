# synth2 token-attractor map

Generated 2026-10-16 14:00  |  corpus 5490 rows, **7644 assistant turns**, 7644 user turns
Probe: `probe_out40_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T12:22:00

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.9% | 2.9% | +0.0 |
| `the`-opener (user) | 13.0% | 13.0% | -0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the worst` | - | 7% | - | 10x |
| `you tried` | - | 5% | - | 17x |
| `with the` | - | 7% | - | 6x |
| `part of` | - | 5% | - | 16x |
| `is it` | - | 7% | - | 5x |
| `how long` | 5% | 5% | 10x | 10x |
| `to the` | - | 7% | - | 4x |
| `i have` | - | 5% | - | 8x |
| `does it` | - | 5% | - | 7x |
| `to do it` | - | 3% | - | 32x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.9% | < 12% |
| `the`-opener (user) | 13.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 40 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the worst` | 49 | 64.1 | 9.2 | 7% | 10x | casual 26, lazy 17, angry 6 |
| `you tried` | 22 | 28.8 | 3.9 | 5% | 17x | casual 15, angry 7 |
| `with the` | 83 | 108.6 | 77.2 | 7% | 6x | casual 55, angry 16, lazy 12 |
| `part of` | 24 | 31.4 | 5.2 | 5% | 16x | lazy 13, casual 11 |
| `is it` | 106 | 138.7 | 28.8 | 7% | 5x | casual 100, angry 6 |
| `how long` | 38 | 49.7 | 18.3 | 5% | 10x | casual 30, angry 7, lazy 1 |
| `to the` | 131 | 171.4 | 163.5 | 7% | 4x | casual 75, lazy 32, angry 24 |
| `i have` | 47 | 61.5 | 87.7 | 5% | 8x | casual 35, lazy 12 |
| `does it` | 53 | 69.3 | 5.2 | 5% | 7x | casual 44, lazy 5, angry 4 |
| `to do it` | 8 | 10.5 | 1.3 | 3% | 32x | casual 8 |
| `much better` | 8 | 10.5 | 1.3 | 3% | 32x | casual 7, lazy 1 |
| `it take` | 8 | 10.5 | 1.3 | 3% | 32x | casual 8 |
| `been a` | 8 | 10.5 | 5.2 | 3% | 32x | casual 7, angry 1 |
| `what did` | 54 | 70.6 | 53.6 | 5% | 7x | casual 41, angry 12, lazy 1 |
| `of a` | 59 | 77.2 | 30.1 | 5% | 6x | casual 30, lazy 15, angry 14 |
| `the job` | 12 | 15.7 | 5.2 | 3% | 21x | casual 6, angry 5, lazy 1 |
| `long did` | 12 | 15.7 | 6.5 | 3% | 21x | casual 9, angry 3 |
| `i would` | 14 | 18.3 | 5.2 | 3% | 18x | casual 8, angry 4, lazy 2 |
| `go for` | 14 | 18.3 | 3.9 | 3% | 18x | casual 13, lazy 1 |
| `you need` | 15 | 19.6 | 1.3 | 3% | 17x | casual 10, lazy 5 |
| `too much` | 18 | 23.5 | 7.8 | 3% | 14x | casual 9, lazy 9 |
| `the weekend` | 19 | 24.9 | 49.7 | 3% | 13x | casual 15, lazy 4 |
| `have you` | 113 | 147.8 | 31.4 | 5% | 3x | casual 80, angry 33 |
| `i keep` | 23 | 30.1 | 39.2 | 3% | 11x | casual 17, lazy 6 |
| `well the` | 25 | 32.7 | 0.0 | 3% | 10x | casual 24, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.6 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.4 | casual 10, lazy 1 |
| `have you tried` | 3 | 22 | 13.9 | casual 15, angry 7 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.8 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.5 | casual 9, lazy 2 |
| `two hours of` | 3 | 9 | 12.3 | lazy 4, angry 3, casual 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `for an hour` | 3 | 10 | 11.8 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.8 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.5 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.4 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.3 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 10.9 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.7 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |
| `how do you` | 3 | 20 | 10.2 | angry 17, casual 2, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the worst` | 3 | casual 26, lazy 17, angry 6 |
| `you tried` | 2 | casual 15, angry 7 |
| `with the` | 3 | casual 55, angry 16, lazy 12 |
| `part of` | 2 | lazy 13, casual 11 |
| `is it` | 2 | casual 100, angry 6 |
| `how long` | 3 | casual 30, angry 7, lazy 1 |
| `to the` | 3 | casual 75, lazy 32, angry 24 |
| `i have` | 2 | casual 35, lazy 12 |
| `does it` | 3 | casual 44, lazy 5, angry 4 |
| `to do it` | 1 | casual 8 |
| `much better` | 2 | casual 7, lazy 1 |
| `it take` | 1 | casual 8 |
| `been a` | 2 | casual 7, angry 1 |
| `what did` | 3 | casual 41, angry 12, lazy 1 |
| `of a` | 3 | casual 30, lazy 15, angry 14 |
| `the job` | 3 | casual 6, angry 5, lazy 1 |
| `long did` | 2 | casual 9, angry 3 |
| `i would` | 3 | casual 8, angry 4, lazy 2 |
| `go for` | 2 | casual 13, lazy 1 |
| `you need` | 2 | casual 10, lazy 5 |
| `too much` | 2 | casual 9, lazy 9 |
| `the weekend` | 2 | casual 15, lazy 4 |
| `have you` | 2 | casual 80, angry 33 |
| `i keep` | 2 | casual 17, lazy 6 |
| `well the` | 2 | casual 24, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=7644): a 8.0%, the 2.9%, did 2.5%, how 2.2%, that 2.1%, was 2.1%
- assistant pos 1 (n=7644): the 11.9%, a 2.3%, you 2.2%, is 2.1%, does 1.3%, it 1.1%
- assistant pos 2 (n=7643): the 6.1%, is 3.3%, a 3.2%, are 2.2%, of 1.7%, for 1.5%
- assistant pos last (n=7644): it 4.4%, now 1.4%, time 1.4%, one 1.0%, you 1.0%, again 0.9%
- user pos 0 (n=7644): the 13.0%, my 10.8%, our 8.3%, i 6.6%, did 3.4%, a 2.9%
- user pos 1 (n=7581): the 4.2%, you 3.0%, a 2.4%, was 1.3%, did 1.3%, is 1.2%
- user pos 2 (n=7492): the 6.5%, a 2.9%, is 2.2%, you 1.7%, and 1.5%, got 1.3%
- user pos last (n=7644): again 2.7%, it 1.8%, now 1.6%, week 1.5%, today 1.3%, night 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.7%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| lazy | 1 / 2155 |

