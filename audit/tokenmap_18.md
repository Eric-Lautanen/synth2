# synth2 token-attractor map

Generated 2026-10-11 15:58  |  corpus 2573 rows, **4497 assistant turns**, 4497 user turns
Probe: `probe_out18_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-11T14:29:17

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | +0.0 |
| `the`-opener (user) | 8.0% | 8.0% | +0.0 |
| copula-only | 0.4% | 0.5% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the coffee` | - | 8% | - | 29x |
| `a good` | - | 8% | - | 5x |
| `your own` | - | 5% | - | 19x |
| `it for` | - | 5% | - | 12x |
| `have you` | - | 7% | - | 4x |
| `it the` | - | 5% | - | 6x |
| `at the` | - | 7% | - | 3x |
| `this time` | - | 5% | - | 5x |
| `does it` | - | 5% | - | 5x |
| `good one` | - | 3% | - | 19x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 0.5% | < 4% |
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
| `the coffee` | 13 | 28.9 | 13.3 | 8% | 29x | casual 7, lazy 6 |
| `a good` | 71 | 157.9 | 22.2 | 8% | 5x | casual 69, lazy 2 |
| `your own` | 12 | 26.7 | 2.2 | 5% | 19x | casual 11, lazy 1 |
| `it for` | 19 | 42.3 | 28.9 | 5% | 12x | casual 18, lazy 1 |
| `have you` | 80 | 177.9 | 48.9 | 7% | 4x | casual 80 |
| `it the` | 38 | 84.5 | 20.0 | 5% | 6x | casual 34, lazy 4 |
| `at the` | 116 | 257.9 | 249.1 | 7% | 3x | casual 104, lazy 12 |
| `this time` | 43 | 95.6 | 20.0 | 5% | 5x | casual 42, lazy 1 |
| `does it` | 45 | 100.1 | 4.4 | 5% | 5x | casual 44, lazy 1 |
| `good one` | 8 | 17.8 | 6.7 | 3% | 19x | casual 8 |
| `nothing on` | 9 | 20.0 | 2.2 | 3% | 17x | casual 8, lazy 1 |
| `and i` | 53 | 117.9 | 171.2 | 5% | 4x | casual 29, lazy 24 |
| `they get` | 10 | 22.2 | 2.2 | 3% | 15x | casual 9, lazy 1 |
| `good luck` | 10 | 22.2 | 0.0 | 3% | 15x | casual 9, lazy 1 |
| `on my` | 12 | 26.7 | 31.1 | 3% | 12x | casual 7, lazy 5 |
| `no idea` | 12 | 26.7 | 17.8 | 3% | 12x | casual 10, lazy 2 |
| `are just` | 12 | 26.7 | 4.4 | 3% | 12x | lazy 11, casual 1 |
| `in the` | 191 | 424.7 | 442.5 | 7% | 2x | casual 171, lazy 20 |
| `is usually` | 13 | 28.9 | 0.0 | 3% | 12x | casual 12, lazy 1 |
| `this weekend` | 15 | 33.4 | 53.4 | 3% | 10x | casual 14, lazy 1 |
| `on sunday` | 16 | 35.6 | 51.1 | 3% | 9x | casual 16 |
| `is just` | 16 | 35.6 | 2.2 | 3% | 9x | lazy 10, casual 6 |
| `the good` | 17 | 37.8 | 22.2 | 3% | 9x | casual 14, lazy 3 |
| `up to` | 18 | 40.0 | 35.6 | 3% | 8x | casual 18 |
| `a walk` | 18 | 40.0 | 24.5 | 3% | 8x | casual 16, lazy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 9 | 17.9 | casual 7, lazy 2 |
| `are you going to` | 4 | 8 | 16.3 | casual 8 |
| `an early night` | 3 | 10 | 15.4 | casual 10 |
| `best kind of` | 3 | 11 | 14.2 | casual 8, lazy 3 |
| `have you tried` | 3 | 15 | 13.2 | casual 15 |
| `for an hour` | 3 | 9 | 12.8 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 11.7 | casual 9, lazy 2 |
| `the best kind` | 3 | 14 | 11.6 | casual 12, lazy 2 |
| `a couple of` | 3 | 11 | 11.4 | casual 11 |
| `how long did` | 3 | 9 | 11.3 | casual 9 |
| `have you got` | 3 | 16 | 11.2 | casual 16 |
| `did you find` | 3 | 9 | 11.2 | casual 9 |
| `did you get` | 3 | 40 | 11.1 | casual 40 |
| `has it been` | 3 | 8 | 10.6 | casual 8 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.3 | casual 15 |
| `and i am` | 3 | 8 | 10.1 | casual 7, lazy 1 |
| `do you go` | 3 | 8 | 10.0 | casual 8 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `these days` | 2 | 8 | 9.9 | casual 8 |
| `what did you` | 3 | 26 | 9.8 | casual 26 |
| `washing machine` | 2 | 11 | 9.7 | casual 11 |
| `did you go` | 3 | 13 | 9.7 | casual 13 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the coffee` | 2 | casual 7, lazy 6 |
| `a good` | 2 | casual 69, lazy 2 |
| `your own` | 2 | casual 11, lazy 1 |
| `it for` | 2 | casual 18, lazy 1 |
| `have you` | 1 | casual 80 |
| `it the` | 2 | casual 34, lazy 4 |
| `at the` | 2 | casual 104, lazy 12 |
| `this time` | 2 | casual 42, lazy 1 |
| `does it` | 2 | casual 44, lazy 1 |
| `good one` | 1 | casual 8 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `and i` | 2 | casual 29, lazy 24 |
| `they get` | 2 | casual 9, lazy 1 |
| `good luck` | 2 | casual 9, lazy 1 |
| `on my` | 2 | casual 7, lazy 5 |
| `no idea` | 2 | casual 10, lazy 2 |
| `are just` | 2 | lazy 11, casual 1 |
| `in the` | 2 | casual 171, lazy 20 |
| `is usually` | 2 | casual 12, lazy 1 |
| `this weekend` | 2 | casual 14, lazy 1 |
| `on sunday` | 1 | casual 16 |
| `is just` | 2 | lazy 10, casual 6 |
| `the good` | 2 | casual 14, lazy 3 |
| `up to` | 1 | casual 18 |
| `a walk` | 2 | casual 16, lazy 2 |

## 4. Opener maps

- assistant pos 0 (n=4497): a 7.8%, that 3.3%, haha 3.0%, the 2.7%, i 2.0%, is 1.3%
- assistant pos 1 (n=4497): the 11.5%, a 2.8%, is 2.8%, you 1.8%, it 1.6%, and 1.3%
- assistant pos 2 (n=4496): the 7.1%, is 4.6%, a 2.5%, of 1.9%, are 1.7%, for 1.5%
- assistant pos last (n=4497): it 5.5%, now 1.8%, time 1.6%, one 1.4%, then 1.3%, again 1.2%
- user pos 0 (n=4497): the 8.0%, i 5.2%, did 4.8%, my 4.8%, a 3.4%, how 2.6%
- user pos 1 (n=4434): the 6.6%, you 4.5%, a 4.0%, was 2.0%, did 2.0%, to 2.0%
- user pos 2 (n=4346): the 6.5%, a 3.8%, you 2.5%, and 2.4%, is 1.9%, one 1.4%
- user pos last (n=4497): again 2.4%, it 2.3%, week 1.7%, today 1.6%, now 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **9.8%**; model outputs: **21.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 616 |

