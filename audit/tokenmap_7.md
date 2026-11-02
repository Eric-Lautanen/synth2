# synth2 token-attractor map

Generated 2026-10-07 15:29  |  corpus 1518 rows, **2862 assistant turns**, 2862 user turns
Probe: `probe_out7.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T15:01:30

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 13.1% | 6.3% | -6.8 |
| `the`-opener (user) | 7.7% | 7.5% | -0.2 |
| copula-only | 2.1% | 1.1% | -1.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the one` | 20% | 25% | 18x | 26x |
| `the best` | 10% | 27% | 6x | 18x |
| `the whole` | 22% | 25% | 15x | 19x |
| `i'm not` | 8% | 15% | 23x | 48x |
| `part of` | - | 15% | - | 39x |
| `got a` | - | 17% | - | 19x |
| `a good` | 28% | 18% | 15x | 10x |
| `i've got` | - | 12% | - | 20x |
| `you get` | 7% | 13% | 5x | 10x |
| `be the` | 5% | 10% | 14x | 24x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.3% | < 12% |
| `the`-opener (user) | 7.5% | n/a |
| copula-only turns | 1.1% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 57 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the one` | 28 | 97.8 | 38.4 | 25% | 26x | casual 28 |
| `the best` | 43 | 150.2 | 66.4 | 27% | 18x | casual 43 |
| `the whole` | 38 | 132.8 | 90.8 | 25% | 19x | casual 38 |
| `i'm not` | 9 | 31.4 | 7.0 | 15% | 48x | casual 9 |
| `part of` | 11 | 38.4 | 7.0 | 15% | 39x | casual 11 |
| `got a` | 25 | 87.4 | 101.3 | 17% | 19x | casual 25 |
| `a good` | 50 | 174.7 | 28.0 | 18% | 10x | casual 50 |
| `i've got` | 17 | 59.4 | 28.0 | 12% | 20x | casual 17 |
| `you get` | 38 | 132.8 | 125.8 | 13% | 10x | casual 38 |
| `be the` | 12 | 41.9 | 3.5 | 10% | 24x | casual 12 |
| `do the` | 19 | 66.4 | 7.0 | 10% | 15x | casual 19 |
| `a proper` | 39 | 136.3 | 83.9 | 12% | 9x | casual 39 |
| `how many` | 23 | 80.4 | 7.0 | 8% | 10x | casual 23 |
| `that is` | 62 | 216.6 | 24.5 | 10% | 5x | casual 62 |
| `how did` | 12 | 41.9 | 28.0 | 7% | 16x | casual 12 |
| `a bit` | 38 | 132.8 | 80.4 | 8% | 6x | casual 38 |
| `it's been` | 17 | 59.4 | 0.0 | 7% | 11x | casual 17 |
| `one of` | 18 | 62.9 | 41.9 | 7% | 11x | casual 18 |
| `in the` | 94 | 328.4 | 457.7 | 10% | 3x | casual 94 |
| `of the` | 60 | 209.6 | 167.7 | 8% | 4x | casual 60 |
| `what did` | 25 | 87.4 | 59.4 | 7% | 8x | casual 25 |
| `i've been` | 27 | 94.3 | 41.9 | 7% | 7x | casual 27 |
| `on the` | 70 | 244.6 | 314.5 | 8% | 3x | casual 70 |
| `to be` | 15 | 52.4 | 28.0 | 5% | 10x | casual 15 |
| `and i'm` | 16 | 55.9 | 21.0 | 5% | 9x | casual 16 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `an early night` | 3 | 8 | 16.2 | casual 8 |
| `that is a good` | 4 | 8 | 13.1 | casual 8 |
| `have you tried` | 3 | 14 | 13.0 | casual 14 |
| `one of those` | 3 | 9 | 12.3 | casual 9 |
| `the best kind` | 3 | 8 | 11.5 | casual 8 |
| `a couple of` | 3 | 8 | 11.5 | casual 8 |
| `are you going` | 3 | 13 | 10.8 | casual 13 |
| `have you got` | 3 | 12 | 10.7 | casual 12 |
| `did you get` | 3 | 28 | 10.6 | casual 28 |
| `a lot of` | 3 | 8 | 10.3 | casual 8 |
| `what did you` | 3 | 20 | 9.7 | casual 20 |
| `did you go` | 3 | 11 | 9.7 | casual 11 |
| `that's the best` | 3 | 8 | 9.4 | casual 8 |
| `in the end` | 3 | 14 | 9.2 | casual 14 |
| `twenty minutes` | 2 | 20 | 8.9 | casual 20 |
| `the end of` | 3 | 10 | 8.7 | casual 10 |
| `an hour` | 2 | 24 | 8.6 | casual 24 |
| `give it a` | 3 | 10 | 8.3 | casual 10 |
| `in the morning` | 3 | 8 | 8.2 | casual 8 |
| `same here` | 2 | 10 | 8.1 | casual 10 |
| `cheaper than` | 2 | 9 | 8.1 | casual 9 |
| `my mum` | 2 | 10 | 8.0 | casual 10 |
| `tell me` | 2 | 8 | 7.9 | casual 8 |
| `ten minutes` | 2 | 13 | 7.9 | casual 13 |
| `best kind` | 2 | 9 | 7.6 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the one` | 1 | casual 28 |
| `the best` | 1 | casual 43 |
| `the whole` | 1 | casual 38 |
| `i'm not` | 1 | casual 9 |
| `part of` | 1 | casual 11 |
| `got a` | 1 | casual 25 |
| `a good` | 1 | casual 50 |
| `i've got` | 1 | casual 17 |
| `you get` | 1 | casual 38 |
| `be the` | 1 | casual 12 |
| `do the` | 1 | casual 19 |
| `a proper` | 1 | casual 39 |
| `how many` | 1 | casual 23 |
| `that is` | 1 | casual 62 |
| `how did` | 1 | casual 12 |
| `a bit` | 1 | casual 38 |
| `it's been` | 1 | casual 17 |
| `one of` | 1 | casual 18 |
| `in the` | 1 | casual 94 |
| `of the` | 1 | casual 60 |
| `what did` | 1 | casual 25 |
| `i've been` | 1 | casual 27 |
| `on the` | 1 | casual 70 |
| `to be` | 1 | casual 15 |
| `and i'm` | 1 | casual 16 |

## 4. Opener maps

- assistant pos 0 (n=2862): ah 6.9%, the 6.3%, a 3.9%, that 2.5%, yeah 2.3%, how 2.3%
- assistant pos 1 (n=2833): the 12.7%, it 5.0%, is 3.5%, a 3.0%, you 2.8%, did 1.6%
- assistant pos 2 (n=2762): the 5.4%, is 3.6%, a 3.4%, it 2.1%, i 1.9%, you 1.8%
- assistant pos last (n=2862): it 6.4%, now 1.9%, time 1.5%, again 1.4%, you 1.3%, one 1.2%
- user pos 0 (n=2862): the 7.5%, i 4.4%, did 4.2%, a 3.6%, my 3.3%, how's 2.4%
- user pos 1 (n=2799): the 7.5%, a 4.1%, you 3.9%, is 1.8%, did 1.7%, was 1.7%
- user pos 2 (n=2716): the 6.0%, a 4.2%, and 2.6%, you 1.8%, is 1.7%, i 1.5%
- user pos last (n=2862): again 2.4%, it 2.1%, week 2.0%, today 1.9%, weekend 1.6%, now 1.6%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **16.6%**; model outputs: **45.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 476 / 2862 |

