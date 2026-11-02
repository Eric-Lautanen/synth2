# synth2 token-attractor map

Generated 2026-10-07 15:01  |  corpus 1364 rows, **2519 assistant turns**, 2519 user turns
Probe: `probe_out6.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T14:35:21

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 10.7% | 13.1% | +2.4 |
| `the`-opener (user) | 7.3% | 7.7% | +0.4 |
| copula-only | 2.1% | 2.1% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 60% | 28% | 31x | 15x |
| `the first` | - | 22% | - | 19x |
| `the whole` | 55% | 22% | 38x | 15x |
| `the one` | 23% | 20% | 21x | 18x |
| `one of` | 8% | 15% | 13x | 22x |
| `to do` | 7% | 13% | 10x | 21x |
| `of those` | - | 12% | - | 27x |
| `it's been` | 28% | 12% | 36x | 17x |
| `on the` | 18% | 15% | 7x | 6x |
| `do it` | 8% | 12% | 7x | 10x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 13.1% | < 12% |
| `the`-opener (user) | 7.7% | n/a |
| copula-only turns | 2.1% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 55 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a good` | 49 | 194.5 | 31.8 | 28% | 15x | casual 49 |
| `the first` | 29 | 115.1 | 79.4 | 22% | 19x | casual 29 |
| `the whole` | 36 | 142.9 | 83.4 | 22% | 15x | casual 36 |
| `the one` | 28 | 111.2 | 39.7 | 20% | 18x | casual 28 |
| `one of` | 17 | 67.5 | 39.7 | 15% | 22x | casual 17 |
| `to do` | 16 | 63.5 | 27.8 | 13% | 21x | casual 16 |
| `of those` | 11 | 43.7 | 15.9 | 12% | 27x | casual 11 |
| `it's been` | 17 | 67.5 | 0.0 | 12% | 17x | casual 17 |
| `on the` | 63 | 250.1 | 301.7 | 15% | 6x | casual 63 |
| `do it` | 29 | 115.1 | 23.8 | 12% | 10x | casual 29 |
| `i'm not` | 9 | 35.7 | 7.9 | 8% | 23x | casual 9 |
| `i've been` | 27 | 107.2 | 47.6 | 10% | 9x | casual 27 |
| `going to` | 15 | 59.5 | 19.8 | 8% | 14x | casual 15 |
| `the best` | 39 | 154.8 | 67.5 | 10% | 6x | casual 39 |
| `it's a` | 11 | 43.7 | 43.7 | 7% | 15x | casual 11 |
| `a bit` | 38 | 150.9 | 59.5 | 8% | 6x | casual 38 |
| `will be` | 15 | 59.5 | 15.9 | 7% | 11x | casual 15 |
| `for it` | 16 | 63.5 | 27.8 | 7% | 10x | casual 16 |
| `be the` | 9 | 35.7 | 4.0 | 5% | 14x | casual 9 |
| `you get` | 33 | 131.0 | 142.9 | 7% | 5x | casual 33 |
| `of them` | 13 | 51.6 | 31.8 | 5% | 10x | casual 13 |
| `and it` | 43 | 170.7 | 107.2 | 7% | 4x | casual 43 |
| `or just` | 15 | 59.5 | 0.0 | 5% | 8x | casual 15 |
| `is always` | 15 | 59.5 | 7.9 | 5% | 8x | casual 15 |
| `was it` | 48 | 190.6 | 23.8 | 7% | 3x | casual 48 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `an early night` | 3 | 8 | 16.2 | casual 8 |
| `that is a good` | 4 | 8 | 13.1 | casual 8 |
| `one of those` | 3 | 9 | 12.2 | casual 9 |
| `the best kind` | 3 | 8 | 11.7 | casual 8 |
| `a couple of` | 3 | 8 | 11.4 | casual 8 |
| `are you going` | 3 | 12 | 11.0 | casual 12 |
| `did you get` | 3 | 26 | 10.9 | casual 26 |
| `have you got` | 3 | 9 | 10.7 | casual 9 |
| `a lot of` | 3 | 8 | 10.4 | casual 8 |
| `did you go` | 3 | 11 | 10.1 | casual 11 |
| `what did you` | 3 | 14 | 9.6 | casual 14 |
| `in the end` | 3 | 11 | 9.1 | casual 11 |
| `twenty minutes` | 2 | 20 | 8.8 | casual 20 |
| `an hour` | 2 | 22 | 8.6 | casual 22 |
| `the end of` | 3 | 8 | 8.6 | casual 8 |
| `give it a` | 3 | 10 | 8.4 | casual 10 |
| `in the morning` | 3 | 8 | 8.2 | casual 8 |
| `same here` | 2 | 10 | 8.1 | casual 10 |
| `ten minutes` | 2 | 13 | 7.9 | casual 13 |
| `my mum` | 2 | 10 | 7.9 | casual 10 |
| `best kind` | 2 | 9 | 7.8 | casual 9 |
| `tell me` | 2 | 8 | 7.8 | casual 8 |
| `is the best` | 3 | 13 | 7.8 | casual 13 |
| `oh no` | 2 | 15 | 7.6 | casual 15 |
| `how many` | 2 | 18 | 7.5 | casual 18 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 1 | casual 49 |
| `the first` | 1 | casual 29 |
| `the whole` | 1 | casual 36 |
| `the one` | 1 | casual 28 |
| `one of` | 1 | casual 17 |
| `to do` | 1 | casual 16 |
| `of those` | 1 | casual 11 |
| `it's been` | 1 | casual 17 |
| `on the` | 1 | casual 63 |
| `do it` | 1 | casual 29 |
| `i'm not` | 1 | casual 9 |
| `i've been` | 1 | casual 27 |
| `going to` | 1 | casual 15 |
| `the best` | 1 | casual 39 |
| `it's a` | 1 | casual 11 |
| `a bit` | 1 | casual 38 |
| `will be` | 1 | casual 15 |
| `for it` | 1 | casual 16 |
| `be the` | 1 | casual 9 |
| `you get` | 1 | casual 33 |
| `of them` | 1 | casual 13 |
| `and it` | 1 | casual 43 |
| `or just` | 1 | casual 15 |
| `is always` | 1 | casual 15 |
| `was it` | 1 | casual 48 |

## 4. Opener maps

- assistant pos 0 (n=2519): the 13.1%, a 3.8%, yeah 2.6%, that 2.4%, haha 2.4%, how 2.4%
- assistant pos 1 (n=2490): the 5.8%, it 5.3%, is 3.5%, a 3.1%, you 2.5%, did 1.6%
- assistant pos 2 (n=2419): the 5.2%, is 3.8%, a 3.5%, i 2.1%, it 2.1%, and 1.9%
- assistant pos last (n=2519): it 6.4%, now 1.8%, again 1.5%, time 1.5%, one 1.3%, you 1.3%
- user pos 0 (n=2519): the 7.7%, did 4.8%, i 4.4%, a 3.5%, my 3.4%, how's 2.8%
- user pos 1 (n=2456): the 7.9%, you 4.4%, a 3.9%, was 1.9%, did 1.9%, is 1.8%
- user pos 2 (n=2373): the 6.0%, a 4.3%, and 2.8%, you 2.1%, is 1.7%, one 1.6%
- user pos last (n=2519): again 2.1%, it 2.0%, week 1.9%, weekend 1.7%, today 1.7%, now 1.7%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **18.1%**; model outputs: **55.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 457 / 2519 |

