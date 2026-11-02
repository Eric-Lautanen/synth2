# synth2 token-attractor map

Generated 2026-10-20 21:57  |  corpus 7614 rows, **9939 assistant turns**, 9939 user turns
Probe: `probe_out68_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T18:37:52

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.2% | 4.3% | +0.1 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `you get` | - | 8% | - | 14x |
| `i am` | - | 5% | - | 8x |
| `not the` | - | 3% | - | 30x |
| `has been` | - | 3% | - | 25x |
| `did you` | - | 7% | - | 2x |
| `five minutes` | - | 3% | - | 21x |
| `on sunday` | - | 3% | - | 18x |
| `and you` | - | 3% | - | 17x |
| `to do` | - | 3% | - | 13x |
| `it for` | - | 3% | - | 12x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.3% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 36 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `you get` | 59 | 59.4 | 51.3 | 8% | 14x | casual 49, angry 5, lazy 5 |
| `i am` | 66 | 66.4 | 36.2 | 5% | 8x | casual 44, lazy 11, sexy 10 |
| `not the` | 11 | 11.1 | 6.0 | 3% | 30x | casual 8, lazy 2, sexy 1 |
| `has been` | 13 | 13.1 | 64.4 | 3% | 25x | casual 10, lazy 2, sexy 1 |
| `did you` | 281 | 282.7 | 248.5 | 7% | 2x | casual 192, sexy 56, angry 28 |
| `five minutes` | 16 | 16.1 | 11.1 | 3% | 21x | casual 10, angry 2, lazy 2 |
| `on sunday` | 18 | 18.1 | 25.2 | 3% | 18x | casual 16, sexy 2 |
| `and you` | 19 | 19.1 | 42.3 | 3% | 17x | casual 15, lazy 2, sexy 2 |
| `to do` | 25 | 25.2 | 23.1 | 3% | 13x | casual 21, angry 2, lazy 1 |
| `it for` | 27 | 27.2 | 14.1 | 3% | 12x | casual 18, lazy 7, sexy 2 |
| `is the` | 430 | 432.6 | 69.4 | 7% | 2x | casual 250, lazy 116, angry 49 |
| `so the` | 30 | 30.2 | 15.1 | 3% | 11x | casual 16, angry 11, sexy 3 |
| `the day` | 46 | 46.3 | 20.1 | 3% | 7x | lazy 22, casual 17, angry 4 |
| `i will` | 55 | 55.3 | 8.0 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `a good` | 58 | 58.4 | 14.1 | 3% | 6x | casual 43, lazy 12, sexy 3 |
| `was the` | 291 | 292.8 | 94.6 | 5% | 2x | angry 120, casual 85, sexy 80 |
| `how did` | 66 | 66.4 | 9.1 | 3% | 5x | casual 31, sexy 18, angry 17 |
| `what did` | 73 | 73.4 | 41.3 | 3% | 5x | casual 41, angry 19, sexy 12 |
| `is a` | 458 | 460.8 | 60.4 | 5% | 1x | angry 208, casual 120, lazy 115 |
| `do you` | 108 | 108.7 | 53.3 | 3% | 3x | casual 73, angry 26, sexy 8 |
| `is it` | 111 | 111.7 | 22.1 | 3% | 3x | casual 100, angry 7, sexy 4 |
| `that is` | 142 | 142.9 | 13.1 | 3% | 2x | casual 76, lazy 26, sexy 25 |
| `three in` | 8 | 8.0 | 4.0 | 2% | 21x | casual 4, angry 2, lazy 2 |
| `the shoes` | 8 | 8.0 | 0.0 | 2% | 21x | lazy 4, casual 3, sexy 1 |
| `that you` | 8 | 8.0 | 0.0 | 2% | 21x | casual 7, angry 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.9 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `ten minutes of` | 3 | 11 | 12.7 | sexy 8, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.0 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `fell asleep` | 2 | 9 | 11.4 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `i am` | 4 | casual 44, lazy 11, sexy 10, angry 1 |
| `not the` | 3 | casual 8, lazy 2, sexy 1 |
| `has been` | 3 | casual 10, lazy 2, sexy 1 |
| `did you` | 4 | casual 192, sexy 56, angry 28, lazy 5 |
| `five minutes` | 4 | casual 10, angry 2, lazy 2, sexy 2 |
| `on sunday` | 2 | casual 16, sexy 2 |
| `and you` | 3 | casual 15, lazy 2, sexy 2 |
| `to do` | 4 | casual 21, angry 2, lazy 1, sexy 1 |
| `it for` | 3 | casual 18, lazy 7, sexy 2 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 15 |
| `so the` | 3 | casual 16, angry 11, sexy 3 |
| `the day` | 4 | lazy 22, casual 17, angry 4, sexy 3 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `was the` | 4 | angry 120, casual 85, sexy 80, lazy 6 |
| `how did` | 3 | casual 31, sexy 18, angry 17 |
| `what did` | 4 | casual 41, angry 19, sexy 12, lazy 1 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 15 |
| `do you` | 4 | casual 73, angry 26, sexy 8, lazy 1 |
| `is it` | 3 | casual 100, angry 7, sexy 4 |
| `that is` | 4 | casual 76, lazy 26, sexy 25, angry 15 |
| `three in` | 3 | casual 4, angry 2, lazy 2 |
| `the shoes` | 3 | lazy 4, casual 3, sexy 1 |
| `that you` | 2 | casual 7, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=9939): a 9.3%, the 4.3%, did 2.2%, how 2.1%, was 1.7%, that 1.7%
- assistant pos 1 (n=9939): the 10.8%, a 2.2%, you 1.8%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9938): the 6.8%, a 2.9%, is 2.6%, of 1.9%, for 1.8%, on 1.8%
- assistant pos last (n=9939): it 4.0%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=9939): the 13.9%, my 10.0%, our 8.1%, i 6.2%, we 5.6%, you 4.9%
- user pos 1 (n=9876): the 3.3%, you 2.3%, a 1.9%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9787): the 7.6%, a 3.1%, is 1.7%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9939): again 2.3%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.5%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1742 |
| lazy | 1 / 2155 |

