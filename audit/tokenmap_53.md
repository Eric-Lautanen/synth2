# synth2 token-attractor map

Generated 2026-10-18 11:35  |  corpus 6684 rows, **8934 assistant turns**, 8934 user turns
Probe: `probe_out53_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T08:38:12

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.6% | 3.7% | +0.0 |
| `the`-opener (user) | 13.7% | 13.8% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `better than` | - | 7% | - | 19x |
| `did you` | - | 10% | - | 4x |
| `a good` | 3% | 7% | 5x | 11x |
| `always the` | - | 5% | - | 22x |
| `the first` | - | 7% | - | 6x |
| `the same` | - | 7% | - | 6x |
| `next time` | - | 5% | - | 13x |
| `i have` | 3% | 5% | 6x | 9x |
| `used to` | - | 3% | - | 37x |
| `good ones` | - | 3% | - | 37x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.7% | < 12% |
| `the`-opener (user) | 13.8% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 39 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `better than` | 31 | 34.7 | 19.0 | 7% | 19x | casual 22, lazy 8, sexy 1 |
| `did you` | 250 | 279.8 | 276.5 | 10% | 4x | casual 192, angry 28, sexy 25 |
| `a good` | 56 | 62.7 | 14.6 | 7% | 11x | casual 43, lazy 12, sexy 1 |
| `always the` | 20 | 22.4 | 1.1 | 5% | 22x | casual 17, lazy 3 |
| `the first` | 92 | 103.0 | 72.8 | 7% | 6x | casual 40, lazy 38, angry 7 |
| `the same` | 108 | 120.9 | 104.1 | 7% | 6x | angry 36, casual 36, lazy 29 |
| `next time` | 34 | 38.1 | 1.1 | 5% | 13x | casual 15, lazy 11, sexy 6 |
| `i have` | 51 | 57.1 | 87.3 | 5% | 9x | casual 35, lazy 12, sexy 4 |
| `used to` | 8 | 9.0 | 6.7 | 3% | 37x | casual 6, lazy 2 |
| `good ones` | 8 | 9.0 | 3.4 | 3% | 37x | casual 5, lazy 3 |
| `you get` | 59 | 66.0 | 57.1 | 5% | 8x | casual 49, angry 5, lazy 5 |
| `too long` | 9 | 10.1 | 7.8 | 3% | 33x | casual 4, lazy 4, angry 1 |
| `to get` | 10 | 11.2 | 11.2 | 3% | 30x | casual 7, lazy 2, angry 1 |
| `a week` | 70 | 78.4 | 59.3 | 5% | 6x | casual 36, lazy 22, angry 10 |
| `an hour` | 72 | 80.6 | 83.9 | 5% | 6x | casual 34, lazy 16, angry 12 |
| `are always` | 13 | 14.6 | 4.5 | 3% | 23x | casual 6, lazy 5, angry 1 |
| `with you` | 14 | 15.7 | 5.6 | 3% | 21x | sexy 7, angry 4, casual 2 |
| `it is a` | 14 | 15.7 | 4.5 | 3% | 21x | lazy 8, casual 6 |
| `i would` | 16 | 17.9 | 4.5 | 3% | 19x | casual 8, angry 4, lazy 2 |
| `oh the` | 17 | 19.0 | 0.0 | 3% | 18x | casual 17 |
| `are just` | 18 | 20.1 | 2.2 | 3% | 17x | lazy 14, angry 3, casual 1 |
| `up at` | 19 | 21.3 | 14.6 | 3% | 16x | casual 11, angry 4, lazy 3 |
| `i was` | 19 | 21.3 | 47.0 | 3% | 16x | casual 14, sexy 3, lazy 2 |
| `or a` | 34 | 38.1 | 1.1 | 3% | 9x | casual 25, lazy 4, sexy 3 |
| `this week` | 36 | 40.3 | 52.6 | 3% | 8x | casual 26, angry 4, lazy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.9 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 8 | 11.6 | casual 4, lazy 4 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `for an hour` | 3 | 11 | 11.5 | casual 8, angry 1, lazy 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `falling asleep` | 2 | 9 | 11.3 | sexy 8, lazy 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 11.1 | casual 11, angry 1 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.6 | casual 40, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `better than` | 3 | casual 22, lazy 8, sexy 1 |
| `did you` | 4 | casual 192, angry 28, sexy 25, lazy 5 |
| `a good` | 3 | casual 43, lazy 12, sexy 1 |
| `always the` | 2 | casual 17, lazy 3 |
| `the first` | 4 | casual 40, lazy 38, angry 7, sexy 7 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 7 |
| `next time` | 4 | casual 15, lazy 11, sexy 6, angry 2 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `used to` | 2 | casual 6, lazy 2 |
| `good ones` | 2 | casual 5, lazy 3 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `too long` | 3 | casual 4, lazy 4, angry 1 |
| `to get` | 3 | casual 7, lazy 2, angry 1 |
| `a week` | 4 | casual 36, lazy 22, angry 10, sexy 2 |
| `an hour` | 4 | casual 34, lazy 16, angry 12, sexy 10 |
| `are always` | 4 | casual 6, lazy 5, angry 1, sexy 1 |
| `with you` | 4 | sexy 7, angry 4, casual 2, lazy 1 |
| `it is a` | 2 | lazy 8, casual 6 |
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `oh the` | 1 | casual 17 |
| `are just` | 3 | lazy 14, angry 3, casual 1 |
| `up at` | 4 | casual 11, angry 4, lazy 3, sexy 1 |
| `i was` | 3 | casual 14, sexy 3, lazy 2 |
| `or a` | 4 | casual 25, lazy 4, sexy 3, angry 2 |
| `this week` | 4 | casual 26, angry 4, lazy 4, sexy 2 |

## 4. Opener maps

- assistant pos 0 (n=8934): a 8.1%, the 3.7%, did 2.5%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=8934): the 11.7%, a 2.4%, you 2.0%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=8933): the 6.2%, a 3.0%, is 2.9%, are 1.9%, of 1.7%, for 1.7%
- assistant pos last (n=8934): it 4.1%, now 1.6%, time 1.3%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8934): the 13.8%, my 10.3%, our 8.1%, i 6.7%, we 4.2%, they 3.1%
- user pos 1 (n=8871): the 3.6%, you 2.6%, a 2.1%, was 1.2%, did 1.1%, is 1.0%
- user pos 2 (n=8782): the 7.0%, a 3.0%, is 1.9%, you 1.6%, my 1.5%, and 1.3%
- user pos last (n=8934): again 2.5%, it 2.0%, now 1.4%, week 1.4%, night 1.3%, morning 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.0%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 737 |
| lazy | 1 / 2155 |

