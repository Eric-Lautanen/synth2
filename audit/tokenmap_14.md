# synth2 token-attractor map

Generated 2026-10-10 19:55  |  corpus 2063 rows, **4070 assistant turns**, 4070 user turns
Probe: `probe_out14_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-10T17:28:04

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 9.2% | 9.1% | -0.2 |
| `the`-opener (user) | 8.0% | 8.0% | -0.1 |
| copula-only | 1.6% | 1.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i've got` | - | 7% | - | 34x |
| `you go` | - | 7% | - | 10x |
| `it is` | - | 8% | - | 5x |
| `to the` | - | 8% | - | 4x |
| `meaning to` | - | 5% | - | 20x |
| `an early` | - | 5% | - | 18x |
| `a couple` | - | 5% | - | 18x |
| `i got` | - | 5% | - | 15x |
| `the weekend` | - | 5% | - | 11x |
| `is a` | - | 8% | - | 2x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 9.1% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 1.6% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 45 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i've got` | 8 | 19.7 | 29.5 | 7% | 34x | casual 8 |
| `you go` | 28 | 68.8 | 12.3 | 7% | 10x | casual 27, ghetto 1 |
| `it is` | 72 | 176.9 | 100.7 | 8% | 5x | casual 72 |
| `to the` | 76 | 186.7 | 184.3 | 8% | 4x | casual 74, ghetto 2 |
| `meaning to` | 10 | 24.6 | 22.1 | 5% | 20x | casual 10 |
| `an early` | 11 | 27.0 | 7.4 | 5% | 18x | casual 11 |
| `a couple` | 11 | 27.0 | 9.8 | 5% | 18x | casual 11 |
| `i got` | 14 | 34.4 | 41.8 | 5% | 15x | casual 13, ghetto 1 |
| `the weekend` | 18 | 44.2 | 76.2 | 5% | 11x | casual 18 |
| `is a` | 147 | 361.2 | 83.5 | 8% | 2x | casual 146, ghetto 1 |
| `a good` | 67 | 164.6 | 22.1 | 7% | 4x | casual 66, ghetto 1 |
| `a proper` | 70 | 172.0 | 98.3 | 7% | 4x | casual 70 |
| `got a` | 22 | 54.1 | 120.4 | 5% | 9x | casual 21, ghetto 1 |
| `this week` | 29 | 71.3 | 90.9 | 5% | 7x | casual 26, ghetto 3 |
| `did it` | 34 | 83.5 | 17.2 | 5% | 6x | casual 34 |
| `at the` | 104 | 255.5 | 272.7 | 7% | 3x | casual 103, ghetto 1 |
| `a new` | 37 | 90.9 | 100.7 | 5% | 6x | casual 37 |
| `i am` | 40 | 98.3 | 61.4 | 5% | 5x | casual 40 |
| `you did` | 8 | 19.7 | 2.5 | 3% | 17x | casual 7, ghetto 1 |
| `luck with` | 8 | 19.7 | 7.4 | 3% | 17x | casual 8 |
| `it's a` | 8 | 19.7 | 41.8 | 3% | 17x | casual 8 |
| `in one` | 8 | 19.7 | 24.6 | 3% | 17x | casual 8 |
| `same as` | 9 | 22.1 | 4.9 | 3% | 15x | casual 7, ghetto 2 |
| `good luck` | 9 | 22.1 | 0.0 | 3% | 15x | casual 9 |
| `it at` | 10 | 24.6 | 12.3 | 3% | 14x | casual 10 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 8 | 16.5 | casual 8 |
| `an early night` | 3 | 10 | 15.5 | casual 10 |
| `best kind of` | 3 | 10 | 14.2 | casual 8, ghetto 2 |
| `the post office` | 3 | 8 | 13.6 | casual 7, ghetto 1 |
| `have you tried` | 3 | 15 | 13.2 | casual 15 |
| `for an hour` | 3 | 8 | 12.8 | casual 8 |
| `i have been` | 3 | 8 | 11.5 | casual 8 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `the best kind` | 3 | 12 | 11.4 | casual 12 |
| `have you got` | 3 | 16 | 11.1 | casual 16 |
| `how long did` | 3 | 9 | 11.1 | casual 9 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 40 | 10.9 | casual 40 |
| `has it been` | 3 | 8 | 10.7 | casual 8 |
| `are you going` | 3 | 15 | 10.5 | casual 15 |
| `these days` | 2 | 8 | 10.0 | casual 8 |
| `post office` | 2 | 9 | 9.9 | casual 8, ghetto 1 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `do you go` | 3 | 8 | 9.8 | casual 8 |
| `washing machine` | 2 | 10 | 9.6 | casual 10 |
| `what did you` | 3 | 26 | 9.5 | casual 26 |
| `on a saturday` | 3 | 9 | 9.4 | casual 9 |
| `did you go` | 3 | 13 | 9.4 | casual 13 |
| `was it worth` | 3 | 9 | 9.3 | casual 9 |
| `in the end` | 3 | 14 | 9.0 | casual 14 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i've got` | 1 | casual 8 |
| `you go` | 2 | casual 27, ghetto 1 |
| `it is` | 1 | casual 72 |
| `to the` | 2 | casual 74, ghetto 2 |
| `meaning to` | 1 | casual 10 |
| `an early` | 1 | casual 11 |
| `a couple` | 1 | casual 11 |
| `i got` | 2 | casual 13, ghetto 1 |
| `the weekend` | 1 | casual 18 |
| `is a` | 2 | casual 146, ghetto 1 |
| `a good` | 2 | casual 66, ghetto 1 |
| `a proper` | 1 | casual 70 |
| `got a` | 2 | casual 21, ghetto 1 |
| `this week` | 2 | casual 26, ghetto 3 |
| `did it` | 1 | casual 34 |
| `at the` | 2 | casual 103, ghetto 1 |
| `a new` | 1 | casual 37 |
| `i am` | 1 | casual 40 |
| `you did` | 2 | casual 7, ghetto 1 |
| `luck with` | 1 | casual 8 |
| `it's a` | 1 | casual 8 |
| `in one` | 1 | casual 8 |
| `same as` | 2 | casual 7, ghetto 2 |
| `good luck` | 1 | casual 9 |
| `it at` | 1 | casual 10 |

## 4. Opener maps

- assistant pos 0 (n=4070): the 9.1%, a 7.7%, haha 3.6%, i 2.0%, is 1.4%, did 1.4%
- assistant pos 1 (n=4070): the 11.5%, a 3.0%, is 2.8%, you 2.3%, it 1.7%, and 1.3%
- assistant pos 2 (n=4068): the 6.5%, is 4.9%, a 2.8%, of 1.9%, for 1.7%, and 1.5%
- assistant pos last (n=4070): it 5.6%, now 1.8%, one 1.6%, time 1.5%, then 1.4%, again 1.3%
- user pos 0 (n=4070): the 8.0%, i 4.0%, my 3.9%, a 3.6%, did 3.5%, how's 2.1%
- user pos 1 (n=4007): the 7.1%, a 4.5%, you 3.1%, did 1.8%, is 1.5%, was 1.4%
- user pos 2 (n=3921): the 6.0%, a 3.9%, and 2.7%, you 1.8%, is 1.7%, one 1.6%
- user pos last (n=4070): it 2.5%, again 2.1%, week 1.8%, now 1.7%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **13.3%**; model outputs: **31.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 467 / 3881 |
| ghetto | 75 / 189 |

