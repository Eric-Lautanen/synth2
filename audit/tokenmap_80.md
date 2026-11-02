# synth2 token-attractor map

Generated 2026-10-22 22:22  |  corpus 8358 rows, **10743 assistant turns**, 10743 user turns
Probe: `probe_out80_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T18:48:23

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.0% | 5.2% | +0.2 |
| `the`-opener (user) | 14.3% | 14.3% | +0.1 |
| copula-only | 0.7% | 0.7% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `on the` | - | 10% | - | 3x |
| `did you` | 7% | 8% | 3x | 3x |
| `on a` | - | 7% | - | 6x |
| `just a` | - | 5% | - | 15x |
| `i have` | - | 5% | - | 11x |
| `you get` | 3% | 5% | 6x | 10x |
| `so much` | - | 3% | - | 45x |
| `it still` | - | 3% | - | 40x |
| `do the` | - | 5% | - | 8x |
| `no idea` | - | 3% | - | 28x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.2% | < 12% |
| `the`-opener (user) | 14.3% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `on the` | 358 | 333.2 | 295.1 | 10% | 3x | casual 138, sexy 111, lazy 51 |
| `did you` | 280 | 260.6 | 229.0 | 8% | 3x | casual 187, sexy 57, angry 28 |
| `on a` | 125 | 116.4 | 66.1 | 7% | 6x | angry 46, casual 40, lazy 17 |
| `just a` | 37 | 34.4 | 21.4 | 5% | 15x | casual 24, angry 7, lazy 4 |
| `i have` | 50 | 46.5 | 79.1 | 5% | 11x | casual 34, lazy 12, sexy 4 |
| `you get` | 55 | 51.2 | 46.5 | 5% | 10x | casual 45, angry 5, lazy 5 |
| `so much` | 8 | 7.4 | 4.7 | 3% | 45x | casual 3, lazy 3, angry 2 |
| `it still` | 9 | 8.4 | 3.7 | 3% | 40x | casual 3, formal 3, lazy 2 |
| `do the` | 64 | 59.6 | 7.4 | 5% | 8x | casual 28, sexy 13, formal 12 |
| `no idea` | 13 | 12.1 | 7.4 | 3% | 28x | casual 11, lazy 2 |
| `it is the` | 13 | 12.1 | 1.9 | 3% | 28x | casual 10, lazy 3 |
| `weeks of` | 14 | 13.0 | 1.9 | 3% | 26x | casual 7, angry 3, lazy 2 |
| `a time` | 14 | 13.0 | 2.8 | 3% | 26x | lazy 5, casual 4, formal 2 |
| `is on` | 15 | 14.0 | 20.5 | 3% | 24x | casual 12, lazy 2, sexy 1 |
| `with it` | 16 | 14.9 | 7.4 | 3% | 22x | casual 10, sexy 4, formal 1 |
| `the first` | 109 | 101.5 | 84.7 | 5% | 5x | lazy 38, casual 36, sexy 22 |
| `have been` | 19 | 17.7 | 40.0 | 3% | 19x | casual 12, lazy 4, sexy 2 |
| `like the` | 20 | 18.6 | 15.8 | 3% | 18x | casual 9, lazy 4, sexy 4 |
| `one is` | 21 | 19.5 | 11.2 | 3% | 17x | casual 14, lazy 4, sexy 2 |
| `for me` | 23 | 21.4 | 12.1 | 3% | 16x | casual 9, lazy 9, sexy 4 |
| `i did` | 25 | 23.3 | 30.7 | 3% | 14x | casual 20, lazy 4, sexy 1 |
| `did not` | 25 | 23.3 | 30.7 | 3% | 14x | casual 10, lazy 6, angry 4 |
| `this week` | 32 | 29.8 | 44.7 | 3% | 11x | casual 22, angry 4, lazy 4 |
| `the way` | 32 | 29.8 | 23.3 | 3% | 11x | casual 20, sexy 7, lazy 4 |
| `better than` | 35 | 32.6 | 21.4 | 3% | 10x | casual 22, lazy 8, sexy 5 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `the front desk` | 3 | 13 | 12.8 | angry 8, lazy 4, casual 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `counts as a` | 3 | 12 | 12.4 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 15 | 12.2 | angry 6, casual 3, sexy 3 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 14 | 11.1 | casual 9, angry 3, formal 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.6 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `on the` | 5 | casual 138, sexy 111, lazy 51, angry 50 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `on a` | 5 | angry 46, casual 40, lazy 17, sexy 16 |
| `just a` | 4 | casual 24, angry 7, lazy 4, formal 2 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `so much` | 3 | casual 3, lazy 3, angry 2 |
| `it still` | 4 | casual 3, formal 3, lazy 2, angry 1 |
| `do the` | 5 | casual 28, sexy 13, formal 12, angry 6 |
| `no idea` | 2 | casual 11, lazy 2 |
| `it is the` | 2 | casual 10, lazy 3 |
| `weeks of` | 5 | casual 7, angry 3, lazy 2, formal 1 |
| `a time` | 5 | lazy 5, casual 4, formal 2, sexy 2 |
| `is on` | 3 | casual 12, lazy 2, sexy 1 |
| `with it` | 4 | casual 10, sexy 4, formal 1, lazy 1 |
| `the first` | 5 | lazy 38, casual 36, sexy 22, angry 7 |
| `have been` | 4 | casual 12, lazy 4, sexy 2, angry 1 |
| `like the` | 5 | casual 9, lazy 4, sexy 4, angry 2 |
| `one is` | 4 | casual 14, lazy 4, sexy 2, formal 1 |
| `for me` | 4 | casual 9, lazy 9, sexy 4, formal 1 |
| `i did` | 3 | casual 20, lazy 4, sexy 1 |
| `did not` | 5 | casual 10, lazy 6, angry 4, sexy 4 |
| `this week` | 4 | casual 22, angry 4, lazy 4, sexy 2 |
| `the way` | 4 | casual 20, sexy 7, lazy 4, angry 1 |
| `better than` | 3 | casual 22, lazy 8, sexy 5 |

## 4. Opener maps

- assistant pos 0 (n=10743): a 10.1%, the 5.2%, did 2.3%, how 2.1%, that 1.7%, was 1.6%
- assistant pos 1 (n=10743): the 11.0%, a 2.0%, is 1.8%, you 1.7%, does 1.1%, on 1.0%
- assistant pos 2 (n=10742): the 6.9%, a 2.8%, is 2.5%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10743): it 3.9%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10743): the 14.3%, my 9.8%, our 8.4%, i 6.1%, we 6.1%, you 5.5%
- user pos 1 (n=10680): the 3.1%, you 2.1%, a 1.7%, was 1.0%, got 1.0%, did 1.0%
- user pos 2 (n=10590): the 7.8%, a 3.4%, is 1.7%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10743): again 2.2%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.9%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

