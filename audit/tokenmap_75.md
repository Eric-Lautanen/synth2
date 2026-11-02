# synth2 token-attractor map

Generated 2026-10-22 02:56  |  corpus 8048 rows, **10408 assistant turns**, 10408 user turns
Probe: `probe_out75_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T23:40:53

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.5% | 4.5% | +0.1 |
| `the`-opener (user) | 13.9% | 14.0% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | 5% | 5% | 14x | 14x |
| `it is` | 7% | 7% | 5x | 5x |
| `did you get` | - | 5% | - | 13x |
| `did it` | 3% | 5% | 8x | 13x |
| `the day` | - | 5% | - | 11x |
| `how long` | - | 5% | - | 9x |
| `was fine` | - | 3% | - | 43x |
| `up there` | - | 3% | - | 43x |
| `luck with` | - | 3% | - | 43x |
| `good luck` | - | 3% | - | 29x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.5% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 32 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a bit` | 36 | 34.6 | 30.7 | 5% | 14x | casual 34, angry 1, lazy 1 |
| `it is` | 132 | 126.8 | 50.9 | 7% | 5x | casual 82, lazy 36, angry 10 |
| `did you get` | 41 | 39.4 | 39.4 | 5% | 13x | casual 37, angry 2, lazy 2 |
| `did it` | 41 | 39.4 | 12.5 | 5% | 13x | casual 32, lazy 4, sexy 3 |
| `the day` | 47 | 45.2 | 21.1 | 5% | 11x | lazy 22, casual 18, angry 4 |
| `how long` | 56 | 53.8 | 14.4 | 5% | 9x | casual 31, sexy 15, angry 9 |
| `was fine` | 8 | 7.7 | 3.8 | 3% | 43x | casual 6, lazy 2 |
| `up there` | 8 | 7.7 | 1.9 | 3% | 43x | sexy 4, casual 2, lazy 2 |
| `luck with` | 8 | 7.7 | 2.9 | 3% | 43x | casual 8 |
| `good luck` | 12 | 11.5 | 0.0 | 3% | 29x | casual 9, lazy 2, angry 1 |
| `long did` | 13 | 12.5 | 4.8 | 3% | 27x | casual 9, angry 3, sexy 1 |
| `what is the` | 15 | 14.4 | 0.0 | 3% | 23x | casual 10, angry 2, sexy 2 |
| `bit of` | 16 | 15.4 | 8.6 | 3% | 22x | casual 15, angry 1 |
| `a free` | 16 | 15.4 | 8.6 | 3% | 22x | lazy 6, angry 5, sexy 3 |
| `yeah the` | 17 | 16.3 | 1.9 | 3% | 20x | casual 16, lazy 1 |
| `with the` | 102 | 98.0 | 77.8 | 5% | 5x | casual 50, sexy 22, angry 18 |
| `i was` | 19 | 18.3 | 46.1 | 3% | 18x | casual 14, sexy 3, lazy 2 |
| `and no` | 22 | 21.1 | 18.3 | 3% | 16x | casual 10, sexy 7, angry 5 |
| `got a` | 23 | 22.1 | 79.7 | 3% | 15x | casual 17, sexy 3, angry 2 |
| `you have` | 27 | 25.9 | 14.4 | 3% | 13x | casual 18, lazy 5, angry 2 |
| `to be` | 27 | 25.9 | 19.2 | 3% | 13x | casual 13, lazy 8, sexy 4 |
| `is there` | 29 | 27.9 | 0.0 | 3% | 12x | casual 15, angry 10, sexy 3 |
| `about it` | 29 | 27.9 | 27.9 | 3% | 12x | casual 20, lazy 4, sexy 3 |
| `better than` | 35 | 33.6 | 22.1 | 3% | 10x | casual 22, lazy 8, sexy 5 |
| `a good` | 65 | 62.5 | 13.5 | 3% | 5x | casual 50, lazy 12, sexy 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.7 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `the front desk` | 3 | 13 | 13.0 | angry 8, lazy 4, casual 1 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `an hour of` | 3 | 14 | 12.0 | angry 6, casual 3, sexy 3 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.0 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 11.0 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.5 | casual 15, angry 2 |
| `did you get` | 3 | 41 | 10.5 | casual 37, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `it is` | 4 | casual 82, lazy 36, angry 10, sexy 4 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `did it` | 4 | casual 32, lazy 4, sexy 3, angry 2 |
| `the day` | 4 | lazy 22, casual 18, angry 4, sexy 3 |
| `how long` | 4 | casual 31, sexy 15, angry 9, lazy 1 |
| `was fine` | 2 | casual 6, lazy 2 |
| `up there` | 3 | sexy 4, casual 2, lazy 2 |
| `luck with` | 1 | casual 8 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `long did` | 3 | casual 9, angry 3, sexy 1 |
| `what is the` | 4 | casual 10, angry 2, sexy 2, lazy 1 |
| `bit of` | 2 | casual 15, angry 1 |
| `a free` | 4 | lazy 6, angry 5, sexy 3, casual 2 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `with the` | 4 | casual 50, sexy 22, angry 18, lazy 12 |
| `i was` | 3 | casual 14, sexy 3, lazy 2 |
| `and no` | 3 | casual 10, sexy 7, angry 5 |
| `got a` | 4 | casual 17, sexy 3, angry 2, lazy 1 |
| `you have` | 4 | casual 18, lazy 5, angry 2, sexy 2 |
| `to be` | 4 | casual 13, lazy 8, sexy 4, angry 2 |
| `is there` | 4 | casual 15, angry 10, sexy 3, lazy 1 |
| `about it` | 4 | casual 20, lazy 4, sexy 3, angry 2 |
| `better than` | 3 | casual 22, lazy 8, sexy 5 |
| `a good` | 3 | casual 50, lazy 12, sexy 3 |

## 4. Opener maps

- assistant pos 0 (n=10408): a 10.3%, the 4.5%, did 2.2%, how 2.0%, that 1.7%, was 1.6%
- assistant pos 1 (n=10408): the 10.4%, a 1.9%, is 1.8%, you 1.7%, does 1.1%, on 1.0%
- assistant pos 2 (n=10407): the 6.9%, a 2.9%, is 2.6%, on 2.0%, of 2.0%, for 1.9%
- assistant pos last (n=10408): it 3.8%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10408): the 14.0%, my 9.9%, our 8.1%, we 6.1%, i 6.0%, you 5.7%
- user pos 1 (n=10345): the 3.1%, you 2.2%, a 1.8%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=10255): the 7.8%, a 3.3%, is 1.6%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10408): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.1%, today 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.0%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

