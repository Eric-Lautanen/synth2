# synth2 token-attractor map

Generated 2026-10-10 15:58  |  corpus 2030 rows, **3971 assistant turns**, 3971 user turns
Probe: `probe_out12_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-10T14:43:04

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 13.2% | 9.7% | -3.5 |
| `the`-opener (user) | 8.0% | 8.0% | +0.0 |
| copula-only | 2.4% | 1.6% | -0.7 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `you get` | 13% | 17% | 9x | 12x |
| `a bit` | 7% | 15% | 6x | 15x |
| `get it` | - | 10% | - | 33x |
| `the new` | - | 12% | - | 12x |
| `you got` | - | 10% | - | 17x |
| `i am` | - | 10% | - | 10x |
| `that is` | - | 10% | - | 6x |
| `do you` | - | 10% | - | 5x |
| `get a` | 5% | 7% | 10x | 16x |
| `did you` | 12% | 12% | 2x | 2x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 9.7% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 1.6% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 51 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `you get` | 53 | 133.5 | 100.7 | 17% | 12x | casual 53 |
| `a bit` | 39 | 98.2 | 83.1 | 15% | 15x | casual 39 |
| `get it` | 12 | 30.2 | 2.5 | 10% | 33x | casual 12 |
| `the new` | 39 | 98.2 | 88.1 | 12% | 12x | casual 39 |
| `you got` | 23 | 57.9 | 12.6 | 10% | 17x | casual 23 |
| `i am` | 40 | 100.7 | 63.0 | 10% | 10x | casual 40 |
| `that is` | 67 | 168.7 | 17.6 | 10% | 6x | casual 67 |
| `do you` | 77 | 193.9 | 17.6 | 10% | 5x | casual 76, ghetto 1 |
| `get a` | 17 | 42.8 | 7.6 | 7% | 16x | casual 16, ghetto 1 |
| `did you` | 212 | 533.9 | 357.6 | 12% | 2x | casual 210, ghetto 2 |
| `a proper` | 69 | 173.8 | 100.7 | 8% | 5x | casual 69 |
| `of the` | 83 | 209.0 | 178.8 | 8% | 4x | casual 83 |
| `or just` | 34 | 85.6 | 5.0 | 7% | 8x | casual 34 |
| `did it` | 37 | 93.2 | 17.6 | 7% | 7x | casual 37 |
| `one of` | 11 | 27.7 | 37.8 | 5% | 18x | casual 11 |
| `my mum` | 14 | 35.3 | 25.2 | 5% | 14x | casual 14 |
| `and i'm` | 14 | 35.3 | 30.2 | 5% | 14x | casual 14 |
| `on it` | 16 | 40.3 | 22.7 | 5% | 12x | casual 15, ghetto 1 |
| `going to` | 18 | 45.3 | 17.6 | 5% | 11x | casual 18 |
| `got a` | 23 | 57.9 | 118.4 | 5% | 9x | casual 22, ghetto 1 |
| `it is` | 74 | 186.4 | 103.2 | 7% | 4x | casual 74 |
| `have you` | 83 | 209.0 | 42.8 | 7% | 3x | casual 83 |
| `or a` | 27 | 68.0 | 2.5 | 5% | 7x | casual 27 |
| `do the` | 29 | 73.0 | 20.1 | 5% | 7x | casual 29 |
| `how did` | 32 | 80.6 | 22.7 | 5% | 6x | casual 32 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 8 | 16.5 | casual 8 |
| `an early night` | 3 | 10 | 15.6 | casual 10 |
| `best kind of` | 3 | 9 | 14.1 | casual 8, ghetto 1 |
| `have you tried` | 3 | 15 | 13.1 | casual 15 |
| `for an hour` | 3 | 8 | 12.9 | casual 8 |
| `the best kind` | 3 | 12 | 11.5 | casual 12 |
| `a couple of` | 3 | 11 | 11.4 | casual 11 |
| `i have been` | 3 | 8 | 11.4 | casual 8 |
| `have you got` | 3 | 17 | 11.0 | casual 17 |
| `did you find` | 3 | 10 | 11.0 | casual 10 |
| `how long did` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 45 | 10.9 | casual 44 |
| `has it been` | 3 | 8 | 10.6 | casual 8 |
| `are you going` | 3 | 15 | 10.4 | casual 15 |
| `these days` | 2 | 8 | 10.0 | casual 8 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `do you go` | 3 | 8 | 9.7 | casual 8 |
| `what did you` | 3 | 28 | 9.6 | casual 27 |
| `washing machine` | 2 | 10 | 9.5 | casual 10 |
| `on a saturday` | 3 | 9 | 9.5 | casual 9 |
| `did you go` | 3 | 14 | 9.4 | casual 14 |
| `was it worth` | 3 | 9 | 9.2 | casual 9 |
| `that's the whole` | 3 | 13 | 9.1 | casual 12, ghetto 1 |
| `you going to` | 3 | 8 | 9.0 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `you get` | 1 | casual 53 |
| `a bit` | 1 | casual 39 |
| `get it` | 1 | casual 12 |
| `the new` | 1 | casual 39 |
| `you got` | 1 | casual 23 |
| `i am` | 1 | casual 40 |
| `that is` | 1 | casual 67 |
| `do you` | 2 | casual 76, ghetto 1 |
| `get a` | 2 | casual 16, ghetto 1 |
| `did you` | 2 | casual 210, ghetto 2 |
| `a proper` | 1 | casual 69 |
| `of the` | 1 | casual 83 |
| `or just` | 1 | casual 34 |
| `did it` | 1 | casual 37 |
| `one of` | 1 | casual 11 |
| `my mum` | 1 | casual 14 |
| `and i'm` | 1 | casual 14 |
| `on it` | 2 | casual 15, ghetto 1 |
| `going to` | 1 | casual 18 |
| `got a` | 2 | casual 22, ghetto 1 |
| `it is` | 1 | casual 74 |
| `have you` | 1 | casual 83 |
| `or a` | 1 | casual 27 |
| `do the` | 1 | casual 29 |
| `how did` | 1 | casual 32 |

## 4. Opener maps

- assistant pos 0 (n=3971): the 9.7%, a 7.6%, haha 3.4%, i 2.1%, did 1.4%, is 1.4%
- assistant pos 1 (n=3971): the 11.8%, a 3.1%, is 2.9%, you 2.1%, it 1.8%, and 1.2%
- assistant pos 2 (n=3970): the 6.7%, is 5.1%, a 2.8%, of 1.9%, for 1.6%, and 1.5%
- assistant pos last (n=3971): it 5.6%, now 1.7%, one 1.6%, time 1.6%, then 1.4%, again 1.3%
- user pos 0 (n=3971): the 8.0%, i 3.9%, my 3.9%, a 3.7%, did 3.6%, how's 2.2%
- user pos 1 (n=3908): the 7.2%, a 4.6%, you 3.2%, did 1.8%, is 1.5%, was 1.5%
- user pos 2 (n=3822): the 6.0%, a 4.0%, and 2.7%, you 1.8%, is 1.7%, one 1.6%
- user pos last (n=3971): it 2.5%, again 2.2%, week 1.8%, now 1.7%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **13.0%**; model outputs: **23.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 480 / 3881 |
| ghetto | 35 / 90 |

