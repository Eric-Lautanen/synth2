# synth2 token-attractor map

Generated 2026-10-10 14:43  |  corpus 2030 rows, **3971 assistant turns**, 3971 user turns
Probe: `probe_out11_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T18:21:33

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.7% | 13.2% | +6.5 |
| `the`-opener (user) | 8.1% | 8.0% | -0.0 |
| copula-only | 0.6% | 2.4% | +1.8 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `you get` | - | 13% | - | 9x |
| `i've been` | 18% | 10% | 24x | 18x |
| `the whole` | 10% | 12% | 7x | 9x |
| `going to` | 13% | 8% | 29x | 16x |
| `have been` | - | 7% | - | 29x |
| `the day` | - | 7% | - | 14x |
| `did you` | - | 12% | - | 2x |
| `i have` | - | 7% | - | 11x |
| `to get` | - | 5% | - | 25x |
| `they get` | - | 5% | - | 25x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 13.2% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 2.4% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 50 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `you get` | 60 | 151.1 | 100.7 | 13% | 9x | casual 60 |
| `i've been` | 22 | 55.4 | 40.3 | 10% | 18x | casual 22 |
| `the whole` | 53 | 133.5 | 118.4 | 12% | 9x | casual 51, ghetto 2 |
| `going to` | 21 | 52.9 | 17.6 | 8% | 16x | casual 21 |
| `have been` | 9 | 22.7 | 37.8 | 7% | 29x | casual 9 |
| `the day` | 19 | 47.8 | 27.7 | 7% | 14x | casual 19 |
| `did you` | 218 | 549.0 | 357.6 | 12% | 2x | casual 216, ghetto 2 |
| `i have` | 25 | 63.0 | 118.4 | 7% | 11x | casual 25 |
| `to get` | 8 | 20.1 | 20.1 | 5% | 25x | casual 8 |
| `they get` | 8 | 20.1 | 2.5 | 5% | 25x | casual 8 |
| `the same` | 36 | 90.7 | 88.1 | 7% | 7x | casual 34, ghetto 2 |
| `a bit` | 42 | 105.8 | 83.1 | 7% | 6x | casual 42 |
| `get the` | 18 | 45.3 | 40.3 | 5% | 11x | casual 18 |
| `get a` | 19 | 47.8 | 7.6 | 5% | 10x | casual 18, ghetto 1 |
| `the best` | 67 | 168.7 | 63.0 | 7% | 4x | casual 66, ghetto 1 |
| `haha a` | 21 | 52.9 | 5.0 | 5% | 9x | casual 21 |
| `a good` | 78 | 196.4 | 22.7 | 7% | 3x | casual 77, ghetto 1 |
| `for it` | 25 | 63.0 | 27.7 | 5% | 8x | casual 25 |
| `the worst` | 26 | 65.5 | 10.1 | 5% | 8x | casual 26 |
| `the first` | 37 | 93.2 | 95.7 | 5% | 5x | casual 35, ghetto 2 |
| `it a` | 39 | 98.2 | 20.1 | 5% | 5x | casual 39 |
| `did they` | 40 | 100.7 | 10.1 | 5% | 5x | casual 40 |
| `good one` | 8 | 20.1 | 7.6 | 3% | 17x | casual 8 |
| `is a` | 137 | 345.0 | 85.6 | 7% | 2x | casual 137 |
| `this time` | 48 | 120.9 | 25.2 | 5% | 4x | casual 47, ghetto 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 8 | 17.5 | casual 8 |
| `are you going to` | 4 | 9 | 16.4 | casual 9 |
| `an early night` | 3 | 9 | 15.9 | casual 9 |
| `best kind of` | 3 | 10 | 14.1 | casual 9, ghetto 1 |
| `did you get it` | 4 | 8 | 13.4 | casual 8 |
| `for an hour` | 3 | 8 | 13.4 | casual 8 |
| `have you tried` | 3 | 16 | 12.9 | casual 16 |
| `was it worth the` | 4 | 8 | 12.7 | casual 8 |
| `one of those` | 3 | 8 | 12.0 | casual 8 |
| `a couple of` | 3 | 10 | 11.5 | casual 10 |
| `the best kind` | 3 | 13 | 11.4 | casual 13 |
| `have you got` | 3 | 19 | 11.1 | casual 19 |
| `how long did` | 3 | 9 | 10.9 | casual 9 |
| `did you find` | 3 | 10 | 10.9 | casual 10 |
| `did you get` | 3 | 48 | 10.7 | casual 47 |
| `are you going` | 3 | 17 | 10.4 | casual 17 |
| `these days` | 2 | 8 | 10.0 | casual 8 |
| `a bit of` | 3 | 16 | 9.9 | casual 16 |
| `do you go` | 3 | 11 | 9.8 | casual 11 |
| `what did you` | 3 | 29 | 9.4 | casual 28 |
| `did you go` | 3 | 15 | 9.3 | casual 15 |
| `in the end` | 3 | 19 | 9.2 | casual 19 |
| `was it worth` | 3 | 10 | 9.2 | casual 10 |
| `you going to` | 3 | 9 | 9.0 | casual 9 |
| `that's the whole` | 3 | 14 | 9.0 | casual 13, ghetto 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `you get` | 1 | casual 60 |
| `i've been` | 1 | casual 22 |
| `the whole` | 2 | casual 51, ghetto 2 |
| `going to` | 1 | casual 21 |
| `have been` | 1 | casual 9 |
| `the day` | 1 | casual 19 |
| `did you` | 2 | casual 216, ghetto 2 |
| `i have` | 1 | casual 25 |
| `to get` | 1 | casual 8 |
| `they get` | 1 | casual 8 |
| `the same` | 2 | casual 34, ghetto 2 |
| `a bit` | 1 | casual 42 |
| `get the` | 1 | casual 18 |
| `get a` | 2 | casual 18, ghetto 1 |
| `the best` | 2 | casual 66, ghetto 1 |
| `haha a` | 1 | casual 21 |
| `a good` | 2 | casual 77, ghetto 1 |
| `for it` | 1 | casual 25 |
| `the worst` | 1 | casual 26 |
| `the first` | 2 | casual 35, ghetto 2 |
| `it a` | 1 | casual 39 |
| `did they` | 1 | casual 40 |
| `good one` | 1 | casual 8 |
| `is a` | 1 | casual 137 |
| `this time` | 2 | casual 47, ghetto 1 |

## 4. Opener maps

- assistant pos 0 (n=3971): the 13.2%, a 6.9%, haha 3.5%, i 2.5%, how 1.7%, did 1.7%
- assistant pos 1 (n=3970): the 12.3%, is 3.1%, you 2.9%, a 2.8%, it 2.7%, are 1.2%
- assistant pos 2 (n=3959): the 6.0%, is 5.5%, a 2.6%, of 1.7%, you 1.5%, for 1.5%
- assistant pos last (n=3971): it 6.3%, now 1.9%, time 1.6%, one 1.6%, then 1.4%, again 1.4%
- user pos 0 (n=3971): the 8.0%, i 3.9%, my 3.9%, a 3.7%, did 3.6%, how's 2.2%
- user pos 1 (n=3908): the 7.2%, a 4.6%, you 3.2%, did 1.8%, is 1.5%, was 1.5%
- user pos 2 (n=3822): the 6.0%, a 4.0%, and 2.7%, you 1.8%, is 1.7%, one 1.6%
- user pos last (n=3971): it 2.5%, again 2.2%, week 1.8%, now 1.7%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **14.9%**; model outputs: **43.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 556 / 3881 |
| ghetto | 35 / 90 |

