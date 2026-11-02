# synth2 token-attractor map

Generated 2026-10-11 14:29  |  corpus 2387 rows, **4296 assistant turns**, 4296 user turns
Probe: `probe_out17_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-11T13:01:07

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.6% | 2.7% | +0.1 |
| `the`-opener (user) | 7.9% | 8.0% | +0.1 |
| copula-only | 0.4% | 0.4% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | - | 8% | - | 9x |
| `bit of` | - | 7% | - | 17x |
| `take it` | - | 5% | - | 17x |
| `the best` | - | 7% | - | 4x |
| `to do` | - | 5% | - | 10x |
| `well the` | - | 5% | - | 9x |
| `of a` | - | 5% | - | 7x |
| `did you get` | - | 5% | - | 5x |
| `the same` | - | 5% | - | 5x |
| `i have` | - | 5% | - | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 0.4% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
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
| `a bit` | 39 | 90.8 | 74.5 | 8% | 9x | casual 39 |
| `bit of` | 17 | 39.6 | 20.9 | 7% | 17x | casual 17 |
| `take it` | 13 | 30.3 | 4.7 | 5% | 17x | casual 13 |
| `the best` | 67 | 156.0 | 60.5 | 7% | 4x | casual 60, lazy 7 |
| `to do` | 22 | 51.2 | 41.9 | 5% | 10x | casual 21, lazy 1 |
| `well the` | 25 | 58.2 | 0.0 | 5% | 9x | casual 25 |
| `of a` | 30 | 69.8 | 34.9 | 5% | 7x | casual 30 |
| `did you get` | 40 | 93.1 | 83.8 | 5% | 5x | casual 40 |
| `the same` | 42 | 97.8 | 79.1 | 5% | 5x | casual 36, lazy 6 |
| `i have` | 44 | 102.4 | 118.7 | 5% | 5x | casual 35, lazy 9 |
| `does he` | 8 | 18.6 | 4.7 | 3% | 18x | casual 8 |
| `you know` | 10 | 23.3 | 4.7 | 3% | 14x | casual 10 |
| `enjoy it` | 10 | 23.3 | 4.7 | 3% | 14x | casual 9, lazy 1 |
| `the whole` | 62 | 144.3 | 111.7 | 5% | 3x | casual 55, lazy 7 |
| `was it the` | 13 | 30.3 | 4.7 | 3% | 11x | casual 13 |
| `one is` | 13 | 30.3 | 14.0 | 3% | 11x | casual 13 |
| `to it` | 16 | 37.2 | 18.6 | 3% | 9x | casual 15, lazy 1 |
| `to the` | 83 | 193.2 | 202.5 | 5% | 3x | casual 75, lazy 8 |
| `a real` | 83 | 193.2 | 97.8 | 5% | 3x | casual 82, lazy 1 |
| `you do` | 17 | 39.6 | 32.6 | 3% | 8x | casual 17 |
| `yeah the` | 17 | 39.6 | 4.7 | 3% | 8x | casual 16, lazy 1 |
| `get the` | 17 | 39.6 | 39.6 | 3% | 8x | casual 17 |
| `up to` | 18 | 41.9 | 37.2 | 3% | 8x | casual 18 |
| `of the` | 91 | 211.8 | 172.3 | 5% | 2x | casual 84, lazy 7 |
| `a day` | 19 | 44.2 | 27.9 | 3% | 8x | casual 18, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 9 | 17.9 | casual 7, lazy 2 |
| `are you going to` | 4 | 8 | 16.4 | casual 8 |
| `an early night` | 3 | 10 | 15.4 | casual 10 |
| `best kind of` | 3 | 11 | 14.2 | casual 8, lazy 3 |
| `have you tried` | 3 | 15 | 13.1 | casual 15 |
| `for an hour` | 3 | 8 | 12.6 | casual 8 |
| `the best kind` | 3 | 14 | 11.7 | casual 12, lazy 2 |
| `i have been` | 3 | 10 | 11.5 | casual 9, lazy 1 |
| `a couple of` | 3 | 11 | 11.4 | casual 11 |
| `how long did` | 3 | 9 | 11.2 | casual 9 |
| `have you got` | 3 | 16 | 11.2 | casual 16 |
| `did you get` | 3 | 40 | 11.1 | casual 40 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `has it been` | 3 | 8 | 10.6 | casual 8 |
| `are you going` | 3 | 15 | 10.4 | casual 15 |
| `a lot of` | 3 | 8 | 10.4 | casual 7, lazy 1 |
| `and i am` | 3 | 8 | 10.0 | casual 7, lazy 1 |
| `do you go` | 3 | 8 | 10.0 | casual 8 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `these days` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.8 | casual 15 |
| `what did you` | 3 | 26 | 9.7 | casual 26 |
| `washing machine` | 2 | 11 | 9.7 | casual 11 |
| `did you go` | 3 | 13 | 9.6 | casual 13 |
| `on a saturday` | 3 | 9 | 9.5 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 1 | casual 39 |
| `bit of` | 1 | casual 17 |
| `take it` | 1 | casual 13 |
| `the best` | 2 | casual 60, lazy 7 |
| `to do` | 2 | casual 21, lazy 1 |
| `well the` | 1 | casual 25 |
| `of a` | 1 | casual 30 |
| `did you get` | 1 | casual 40 |
| `the same` | 2 | casual 36, lazy 6 |
| `i have` | 2 | casual 35, lazy 9 |
| `does he` | 1 | casual 8 |
| `you know` | 1 | casual 10 |
| `enjoy it` | 2 | casual 9, lazy 1 |
| `the whole` | 2 | casual 55, lazy 7 |
| `was it the` | 1 | casual 13 |
| `one is` | 1 | casual 13 |
| `to it` | 2 | casual 15, lazy 1 |
| `to the` | 2 | casual 75, lazy 8 |
| `a real` | 2 | casual 82, lazy 1 |
| `you do` | 1 | casual 17 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `get the` | 1 | casual 17 |
| `up to` | 1 | casual 18 |
| `of the` | 2 | casual 84, lazy 7 |
| `a day` | 2 | casual 18, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=4296): a 7.7%, that 3.4%, haha 3.1%, the 2.7%, i 2.1%, is 1.4%
- assistant pos 1 (n=4296): the 11.9%, is 2.9%, a 2.9%, you 1.9%, it 1.6%, and 1.3%
- assistant pos 2 (n=4295): the 7.3%, is 4.7%, a 2.6%, of 1.9%, for 1.6%, are 1.6%
- assistant pos last (n=4296): it 5.5%, now 1.7%, time 1.5%, one 1.4%, then 1.3%, again 1.2%
- user pos 0 (n=4296): the 8.0%, did 5.0%, i 4.7%, my 4.1%, a 3.4%, how 2.7%
- user pos 1 (n=4233): the 6.9%, you 4.6%, a 4.2%, was 2.1%, to 2.1%, did 2.0%
- user pos 2 (n=4145): the 6.5%, a 3.9%, you 2.6%, and 2.5%, is 1.8%, one 1.4%
- user pos last (n=4296): it 2.3%, again 2.2%, week 1.7%, now 1.6%, today 1.5%, weekend 1.5%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **10.2%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 415 |

