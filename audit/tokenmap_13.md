# synth2 token-attractor map

Generated 2026-10-10 17:28  |  corpus 2030 rows, **3971 assistant turns**, 3971 user turns
Probe: `probe_out13_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-10T15:58:43

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 9.7% | 9.2% | -0.5 |
| `the`-opener (user) | 8.0% | 8.0% | +0.0 |
| copula-only | 1.6% | 1.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `is the` | - | 17% | - | 3x |
| `the whole` | - | 8% | - | 6x |
| `all that` | - | 5% | - | 25x |
| `a small` | - | 5% | - | 17x |
| `the first` | - | 7% | - | 6x |
| `my mum` | 5% | 5% | 14x | 14x |
| `i know` | - | 5% | - | 12x |
| `the best` | - | 7% | - | 4x |
| `a proper` | 8% | 7% | 5x | 4x |
| `i am` | 10% | 5% | 10x | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 9.2% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 1.6% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 44 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `is the` | 244 | 614.5 | 115.8 | 17% | 3x | casual 242, ghetto 2 |
| `the whole` | 58 | 146.1 | 118.4 | 8% | 6x | casual 56, ghetto 2 |
| `all that` | 8 | 20.1 | 5.0 | 5% | 25x | casual 8 |
| `a small` | 12 | 30.2 | 20.1 | 5% | 17x | casual 12 |
| `the first` | 43 | 108.3 | 95.7 | 7% | 6x | casual 41, ghetto 2 |
| `my mum` | 14 | 35.3 | 25.2 | 5% | 14x | casual 14 |
| `i know` | 17 | 42.8 | 42.8 | 5% | 12x | casual 16, ghetto 1 |
| `the best` | 63 | 158.7 | 63.0 | 7% | 4x | casual 62, ghetto 1 |
| `a proper` | 70 | 176.3 | 100.7 | 7% | 4x | casual 70 |
| `i am` | 40 | 100.7 | 63.0 | 5% | 5x | casual 40 |
| `makes the` | 8 | 20.1 | 5.0 | 3% | 17x | casual 8 |
| `on your` | 11 | 27.7 | 7.6 | 3% | 12x | casual 11 |
| `all day` | 12 | 30.2 | 12.6 | 3% | 11x | casual 11, ghetto 1 |
| `was it` | 65 | 163.7 | 22.7 | 5% | 3x | casual 65 |
| `a good` | 67 | 168.7 | 22.7 | 5% | 3x | casual 66, ghetto 1 |
| `and i'm` | 14 | 35.3 | 30.2 | 3% | 9x | casual 14 |
| `a bit of` | 15 | 37.8 | 20.1 | 3% | 9x | casual 15 |
| `on it` | 16 | 40.3 | 22.7 | 3% | 8x | casual 15, ghetto 1 |
| `i've been` | 16 | 40.3 | 40.3 | 3% | 8x | casual 16 |
| `what was` | 17 | 42.8 | 15.1 | 3% | 8x | casual 17 |
| `up to` | 18 | 45.3 | 37.8 | 3% | 7x | casual 18 |
| `so far` | 18 | 45.3 | 22.7 | 3% | 7x | casual 18 |
| `is it` | 100 | 251.8 | 42.8 | 5% | 2x | casual 100 |
| `the door` | 23 | 57.9 | 57.9 | 3% | 6x | casual 23 |
| `or a` | 25 | 63.0 | 2.5 | 3% | 5x | casual 25 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 8 | 16.5 | casual 8 |
| `an early night` | 3 | 10 | 15.5 | casual 10 |
| `best kind of` | 3 | 9 | 14.1 | casual 8, ghetto 1 |
| `have you tried` | 3 | 15 | 13.2 | casual 15 |
| `for an hour` | 3 | 8 | 12.8 | casual 8 |
| `i have been` | 3 | 8 | 11.5 | casual 8 |
| `the best kind` | 3 | 12 | 11.5 | casual 12 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `have you got` | 3 | 16 | 11.1 | casual 16 |
| `how long did` | 3 | 9 | 11.0 | casual 9 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 41 | 10.9 | casual 40 |
| `has it been` | 3 | 8 | 10.7 | casual 8 |
| `are you going` | 3 | 15 | 10.5 | casual 15 |
| `these days` | 2 | 8 | 9.9 | casual 8 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `do you go` | 3 | 8 | 9.8 | casual 8 |
| `what did you` | 3 | 27 | 9.6 | casual 26 |
| `washing machine` | 2 | 10 | 9.5 | casual 10 |
| `on a saturday` | 3 | 9 | 9.5 | casual 9 |
| `did you go` | 3 | 13 | 9.4 | casual 13 |
| `was it worth` | 3 | 9 | 9.3 | casual 9 |
| `that's the whole` | 3 | 13 | 9.1 | casual 12, ghetto 1 |
| `you going to` | 3 | 8 | 9.0 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `is the` | 2 | casual 242, ghetto 2 |
| `the whole` | 2 | casual 56, ghetto 2 |
| `all that` | 1 | casual 8 |
| `a small` | 1 | casual 12 |
| `the first` | 2 | casual 41, ghetto 2 |
| `my mum` | 1 | casual 14 |
| `i know` | 2 | casual 16, ghetto 1 |
| `the best` | 2 | casual 62, ghetto 1 |
| `a proper` | 1 | casual 70 |
| `i am` | 1 | casual 40 |
| `makes the` | 1 | casual 8 |
| `on your` | 1 | casual 11 |
| `all day` | 2 | casual 11, ghetto 1 |
| `was it` | 1 | casual 65 |
| `a good` | 2 | casual 66, ghetto 1 |
| `and i'm` | 1 | casual 14 |
| `a bit of` | 1 | casual 15 |
| `on it` | 2 | casual 15, ghetto 1 |
| `i've been` | 1 | casual 16 |
| `what was` | 1 | casual 17 |
| `up to` | 1 | casual 18 |
| `so far` | 1 | casual 18 |
| `is it` | 1 | casual 100 |
| `the door` | 1 | casual 23 |
| `or a` | 1 | casual 25 |

## 4. Opener maps

- assistant pos 0 (n=3971): the 9.2%, a 7.9%, haha 3.4%, i 2.0%, is 1.5%, did 1.4%
- assistant pos 1 (n=3971): the 11.7%, a 3.1%, is 2.8%, you 2.1%, it 1.7%, and 1.2%
- assistant pos 2 (n=3970): the 6.6%, is 5.1%, a 2.8%, of 2.0%, for 1.7%, and 1.5%
- assistant pos last (n=3971): it 5.6%, now 1.7%, one 1.6%, time 1.5%, then 1.4%, again 1.3%
- user pos 0 (n=3971): the 8.0%, i 3.9%, my 3.9%, a 3.7%, did 3.6%, how's 2.2%
- user pos 1 (n=3908): the 7.2%, a 4.6%, you 3.2%, did 1.8%, is 1.5%, was 1.5%
- user pos 2 (n=3822): the 6.0%, a 4.0%, and 2.7%, you 1.8%, is 1.7%, one 1.6%
- user pos last (n=3971): it 2.5%, again 2.2%, week 1.8%, now 1.7%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **12.6%**; model outputs: **26.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 467 / 3881 |
| ghetto | 35 / 90 |

