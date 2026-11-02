# synth2 token-attractor map

Generated 2026-10-11 17:28  |  corpus 2697 rows, **4631 assistant turns**, 4631 user turns
Probe: `probe_out19_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-11T15:58:34

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | -0.0 |
| `the`-opener (user) | 8.0% | 8.1% | +0.1 |
| copula-only | 0.5% | 0.5% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `no plans` | - | 5% | - | 29x |
| `is the` | - | 12% | - | 2x |
| `a bit of` | - | 5% | - | 15x |
| `have you got` | - | 5% | - | 14x |
| `was it` | - | 7% | - | 5x |
| `got a` | - | 5% | - | 11x |
| `the whole` | - | 7% | - | 4x |
| `just a` | - | 5% | - | 10x |
| `in the` | 7% | 8% | 2x | 2x |
| `the end` | - | 5% | - | 8x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 8.1% | n/a |
| copula-only turns | 0.5% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `no plans` | 8 | 17.3 | 0.0 | 5% | 29x | casual 7, lazy 1 |
| `is the` | 299 | 645.6 | 123.1 | 12% | 2x | casual 252, lazy 47 |
| `a bit of` | 15 | 32.4 | 17.3 | 5% | 15x | casual 15 |
| `have you got` | 16 | 34.5 | 2.2 | 5% | 14x | casual 16 |
| `was it` | 65 | 140.4 | 23.8 | 7% | 5x | casual 65 |
| `got a` | 21 | 45.3 | 108.0 | 5% | 11x | casual 21 |
| `the whole` | 71 | 153.3 | 129.6 | 7% | 4x | casual 55, lazy 16 |
| `just a` | 24 | 51.8 | 28.1 | 5% | 10x | casual 22, lazy 2 |
| `in the` | 194 | 418.9 | 438.4 | 8% | 2x | casual 171, lazy 23 |
| `the end` | 28 | 60.5 | 49.7 | 5% | 8x | casual 26, lazy 2 |
| `of the` | 94 | 203.0 | 159.8 | 7% | 3x | casual 84, lazy 10 |
| `a new` | 40 | 86.4 | 97.2 | 5% | 6x | casual 37, lazy 3 |
| `you on` | 8 | 17.3 | 4.3 | 3% | 19x | casual 8 |
| `have to` | 8 | 17.3 | 19.4 | 3% | 19x | casual 7, lazy 1 |
| `the first` | 54 | 116.6 | 90.7 | 5% | 4x | casual 40, lazy 14 |
| `you know` | 10 | 21.6 | 4.3 | 3% | 15x | casual 10 |
| `is good` | 12 | 25.9 | 4.3 | 3% | 13x | casual 11, lazy 1 |
| `is a` | 199 | 429.7 | 84.2 | 7% | 2x | casual 147, lazy 52 |
| `you will` | 13 | 28.1 | 0.0 | 3% | 12x | casual 9, lazy 4 |
| `i got` | 13 | 28.1 | 56.1 | 3% | 12x | casual 13 |
| `and you` | 15 | 32.4 | 4.3 | 3% | 10x | casual 15 |
| `so the` | 16 | 34.5 | 30.2 | 3% | 10x | casual 16 |
| `a real` | 83 | 179.2 | 90.7 | 5% | 3x | casual 82, lazy 1 |
| `yeah the` | 17 | 36.7 | 4.3 | 3% | 9x | casual 16, lazy 1 |
| `how's the` | 17 | 36.7 | 129.6 | 3% | 9x | casual 17 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 10 | 18.0 | casual 7, lazy 3 |
| `are you going to` | 4 | 8 | 16.2 | casual 8 |
| `an early night` | 3 | 10 | 15.3 | casual 10 |
| `best kind of` | 3 | 12 | 14.3 | casual 8, lazy 4 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.2 | casual 15 |
| `for an hour` | 3 | 9 | 12.8 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 11.8 | casual 9, lazy 2 |
| `the best kind` | 3 | 15 | 11.7 | casual 12, lazy 3 |
| `a couple of` | 3 | 11 | 11.4 | casual 11 |
| `how long did` | 3 | 9 | 11.3 | casual 9 |
| `have you got` | 3 | 16 | 11.2 | casual 16 |
| `did you find` | 3 | 9 | 11.2 | casual 9 |
| `did you get` | 3 | 42 | 11.1 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 10.7 | casual 8 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |
| `and i am` | 3 | 8 | 10.1 | casual 7, lazy 1 |
| `do you go` | 3 | 8 | 10.0 | casual 8 |
| `what did you` | 3 | 27 | 9.9 | casual 26, lazy 1 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `these days` | 2 | 8 | 9.8 | casual 8 |
| `did you go` | 3 | 13 | 9.7 | casual 13 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `no plans` | 2 | casual 7, lazy 1 |
| `is the` | 2 | casual 252, lazy 47 |
| `a bit of` | 1 | casual 15 |
| `have you got` | 1 | casual 16 |
| `was it` | 1 | casual 65 |
| `got a` | 1 | casual 21 |
| `the whole` | 2 | casual 55, lazy 16 |
| `just a` | 2 | casual 22, lazy 2 |
| `in the` | 2 | casual 171, lazy 23 |
| `the end` | 2 | casual 26, lazy 2 |
| `of the` | 2 | casual 84, lazy 10 |
| `a new` | 2 | casual 37, lazy 3 |
| `you on` | 1 | casual 8 |
| `have to` | 2 | casual 7, lazy 1 |
| `the first` | 2 | casual 40, lazy 14 |
| `you know` | 1 | casual 10 |
| `is good` | 2 | casual 11, lazy 1 |
| `is a` | 2 | casual 147, lazy 52 |
| `you will` | 2 | casual 9, lazy 4 |
| `i got` | 1 | casual 13 |
| `and you` | 1 | casual 15 |
| `so the` | 1 | casual 16 |
| `a real` | 2 | casual 82, lazy 1 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `how's the` | 1 | casual 17 |

## 4. Opener maps

- assistant pos 0 (n=4631): a 7.8%, that 3.2%, haha 2.9%, the 2.7%, i 2.0%, is 1.3%
- assistant pos 1 (n=4631): the 11.2%, a 2.7%, is 2.7%, you 1.7%, it 1.5%, and 1.3%
- assistant pos 2 (n=4630): the 6.9%, is 4.5%, a 2.5%, are 2.0%, of 1.9%, for 1.5%
- assistant pos last (n=4631): it 5.5%, now 1.7%, time 1.6%, one 1.3%, then 1.2%, again 1.1%
- user pos 0 (n=4631): the 8.1%, i 5.4%, my 5.3%, did 4.7%, a 3.4%, our 2.8%
- user pos 1 (n=4568): the 6.4%, you 4.4%, a 3.9%, was 2.0%, did 1.9%, to 1.9%
- user pos 2 (n=4480): the 6.6%, a 3.7%, you 2.5%, and 2.3%, is 1.9%, one 1.3%
- user pos last (n=4631): again 2.5%, it 2.3%, week 1.7%, today 1.6%, now 1.6%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **9.5%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 750 |

