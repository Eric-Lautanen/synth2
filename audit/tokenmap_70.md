# synth2 token-attractor map

Generated 2026-10-21 10:54  |  corpus 7738 rows, **10073 assistant turns**, 10073 user turns
Probe: `probe_out70_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T01:19:30

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.3% | 4.4% | +0.0 |
| `the`-opener (user) | 13.8% | 14.0% | +0.1 |
| copula-only | 0.5% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i've been` | - | 5% | - | 36x |
| `not a` | - | 5% | - | 14x |
| `it is` | 5% | 7% | 4x | 5x |
| `i have been` | - | 3% | - | 34x |
| `from home` | - | 3% | - | 34x |
| `an hour` | - | 5% | - | 6x |
| `what does` | - | 3% | - | 22x |
| `does anyone` | - | 3% | - | 22x |
| `for the` | - | 7% | - | 2x |
| `hour of` | - | 3% | - | 16x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.4% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 33 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i've been` | 14 | 13.9 | 16.9 | 5% | 36x | casual 14 |
| `not a` | 35 | 34.7 | 8.9 | 5% | 14x | angry 16, casual 11, lazy 7 |
| `it is` | 133 | 132.0 | 52.6 | 7% | 5x | casual 86, lazy 36, angry 7 |
| `i have been` | 10 | 9.9 | 23.8 | 3% | 34x | casual 8, lazy 2 |
| `from home` | 10 | 9.9 | 4.0 | 3% | 34x | lazy 6, casual 4 |
| `an hour` | 79 | 78.4 | 81.4 | 5% | 6x | casual 33, sexy 18, lazy 16 |
| `what does` | 15 | 14.9 | 0.0 | 3% | 22x | angry 8, sexy 4, casual 3 |
| `does anyone` | 15 | 14.9 | 0.0 | 3% | 22x | casual 6, sexy 6, angry 3 |
| `for the` | 283 | 280.9 | 257.1 | 7% | 2x | casual 132, angry 64, sexy 63 |
| `hour of` | 21 | 20.8 | 4.0 | 3% | 16x | angry 8, sexy 6, lazy 4 |
| `at night` | 23 | 22.8 | 18.9 | 3% | 15x | lazy 9, casual 8, angry 6 |
| `in your` | 26 | 25.8 | 7.9 | 3% | 13x | sexy 9, casual 8, angry 5 |
| `what did you` | 33 | 32.8 | 31.8 | 3% | 10x | casual 26, sexy 6, lazy 1 |
| `this week` | 36 | 35.7 | 46.7 | 3% | 9x | casual 26, angry 4, lazy 4 |
| `is worth` | 37 | 36.7 | 4.0 | 3% | 9x | casual 26, angry 5, lazy 5 |
| `is just` | 37 | 36.7 | 3.0 | 3% | 9x | lazy 20, angry 11, casual 6 |
| `it was` | 42 | 41.7 | 57.6 | 3% | 8x | casual 28, sexy 7, lazy 5 |
| `is not` | 44 | 43.7 | 9.9 | 3% | 8x | angry 27, casual 11, lazy 6 |
| `did you get` | 44 | 43.7 | 41.7 | 3% | 8x | casual 40, angry 2, lazy 2 |
| `how long` | 55 | 54.6 | 14.9 | 3% | 6x | casual 30, sexy 15, angry 9 |
| `twenty minutes` | 59 | 58.6 | 43.7 | 3% | 6x | casual 35, lazy 12, angry 7 |
| `have you` | 108 | 107.2 | 23.8 | 3% | 3x | casual 79, angry 27, sexy 2 |
| `worse than` | 8 | 7.9 | 3.0 | 2% | 21x | casual 5, angry 2, sexy 1 |
| `was fine` | 8 | 7.9 | 4.0 | 2% | 21x | casual 6, lazy 2 |
| `they even` | 8 | 7.9 | 3.0 | 2% | 21x | angry 6, casual 1, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `never stood a chance` | 4 | 8 | 25.9 | sexy 7, casual 1 |
| `stood a chance` | 3 | 8 | 16.9 | sexy 7, casual 1 |
| `are you going to` | 4 | 10 | 16.6 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `never stood a` | 3 | 8 | 13.0 | sexy 7, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.8 | casual 7, sexy 1 |
| `ten minutes of` | 3 | 11 | 12.7 | sexy 8, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i've been` | 1 | casual 14 |
| `not a` | 4 | angry 16, casual 11, lazy 7, sexy 1 |
| `it is` | 4 | casual 86, lazy 36, angry 7, sexy 4 |
| `i have been` | 2 | casual 8, lazy 2 |
| `from home` | 2 | lazy 6, casual 4 |
| `an hour` | 4 | casual 33, sexy 18, lazy 16, angry 12 |
| `what does` | 3 | angry 8, sexy 4, casual 3 |
| `does anyone` | 3 | casual 6, sexy 6, angry 3 |
| `for the` | 4 | casual 132, angry 64, sexy 63, lazy 24 |
| `hour of` | 4 | angry 8, sexy 6, lazy 4, casual 3 |
| `at night` | 3 | lazy 9, casual 8, angry 6 |
| `in your` | 4 | sexy 9, casual 8, angry 5, lazy 4 |
| `what did you` | 3 | casual 26, sexy 6, lazy 1 |
| `this week` | 4 | casual 26, angry 4, lazy 4, sexy 2 |
| `is worth` | 4 | casual 26, angry 5, lazy 5, sexy 1 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `it was` | 4 | casual 28, sexy 7, lazy 5, angry 2 |
| `is not` | 3 | angry 27, casual 11, lazy 6 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `how long` | 4 | casual 30, sexy 15, angry 9, lazy 1 |
| `twenty minutes` | 4 | casual 35, lazy 12, angry 7, sexy 5 |
| `have you` | 3 | casual 79, angry 27, sexy 2 |
| `worse than` | 3 | casual 5, angry 2, sexy 1 |
| `was fine` | 2 | casual 6, lazy 2 |
| `they even` | 3 | angry 6, casual 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=10073): a 9.5%, the 4.4%, did 2.2%, how 2.1%, that 1.8%, was 1.7%
- assistant pos 1 (n=10073): the 10.7%, a 2.1%, is 1.8%, you 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=10072): the 6.9%, a 2.9%, is 2.6%, of 1.9%, on 1.8%, for 1.8%
- assistant pos last (n=10073): it 3.9%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10073): the 14.0%, my 10.0%, our 8.1%, i 6.1%, we 5.7%, you 5.2%
- user pos 1 (n=10010): the 3.2%, you 2.3%, a 1.8%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9921): the 7.6%, a 3.2%, is 1.7%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=10073): again 2.3%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.3%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 431 / 3881 |
| sexy | 5 / 1876 |
| lazy | 1 / 2155 |

