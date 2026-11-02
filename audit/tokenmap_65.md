# synth2 token-attractor map

Generated 2026-10-20 13:46  |  corpus 7428 rows, **9738 assistant turns**, 9738 user turns
Probe: `probe_out65_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T10:36:09

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.2% | 4.2% | +0.0 |
| `the`-opener (user) | 14.0% | 14.0% | +0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `no idea` | 5% | 7% | 40x | 54x |
| `i will` | - | 5% | - | 9x |
| `it's the` | - | 3% | - | 30x |
| `want to` | - | 3% | - | 27x |
| `around the` | - | 3% | - | 23x |
| `the neighbors` | - | 3% | - | 17x |
| `have been` | 3% | 3% | 17x | 17x |
| `the same` | - | 5% | - | 4x |
| `in the` | - | 7% | - | 2x |
| `that is` | - | 5% | - | 3x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.2% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 40 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `no idea` | 12 | 12.3 | 8.2 | 7% | 54x | casual 10, lazy 2 |
| `i will` | 55 | 56.5 | 8.2 | 5% | 9x | casual 31, lazy 14, sexy 10 |
| `it's the` | 11 | 11.3 | 16.4 | 3% | 30x | casual 11 |
| `want to` | 12 | 12.3 | 58.5 | 3% | 27x | casual 7, sexy 4, angry 1 |
| `around the` | 14 | 14.4 | 11.3 | 3% | 23x | casual 5, lazy 4, angry 3 |
| `the neighbors` | 19 | 19.5 | 17.5 | 3% | 17x | sexy 8, casual 7, lazy 4 |
| `have been` | 19 | 19.5 | 41.1 | 3% | 17x | casual 13, lazy 4, angry 1 |
| `the same` | 113 | 116.0 | 105.8 | 5% | 4x | angry 36, casual 36, lazy 29 |
| `in the` | 359 | 368.7 | 336.8 | 7% | 2x | casual 169, angry 69, lazy 68 |
| `that is` | 142 | 145.8 | 13.3 | 5% | 3x | casual 76, lazy 26, sexy 25 |
| `is that` | 27 | 27.7 | 2.1 | 3% | 12x | sexy 15, casual 9, angry 3 |
| `you have` | 29 | 29.8 | 15.4 | 3% | 11x | casual 20, lazy 5, angry 2 |
| `got the` | 30 | 30.8 | 48.3 | 3% | 11x | casual 27, lazy 2, sexy 1 |
| `a long` | 32 | 32.9 | 7.2 | 3% | 10x | casual 21, lazy 8, angry 3 |
| `the next` | 35 | 35.9 | 15.4 | 3% | 9x | casual 17, lazy 8, sexy 6 |
| `the whole` | 182 | 186.9 | 124.3 | 5% | 3x | lazy 83, casual 55, angry 32 |
| `i have` | 51 | 52.4 | 80.1 | 3% | 6x | casual 35, lazy 12, sexy 4 |
| `you get` | 59 | 60.6 | 52.4 | 3% | 6x | casual 49, angry 5, lazy 5 |
| `did you` | 278 | 285.5 | 253.6 | 5% | 2x | casual 192, sexy 53, angry 28 |
| `what did` | 72 | 73.9 | 42.1 | 3% | 5x | casual 41, angry 19, sexy 11 |
| `by the` | 78 | 80.1 | 62.6 | 3% | 4x | casual 31, lazy 21, sexy 19 |
| `a real` | 105 | 107.8 | 45.2 | 3% | 3x | casual 82, angry 13, lazy 10 |
| `you forget` | 8 | 8.2 | 1.0 | 2% | 20x | casual 4, lazy 4 |
| `used to` | 8 | 8.2 | 6.2 | 2% | 20x | casual 6, lazy 2 |
| `to go` | 8 | 8.2 | 22.6 | 2% | 20x | casual 6, angry 1, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.5 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.9 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `ten minutes of` | 3 | 9 | 12.5 | sexy 6, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.1 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `fell asleep` | 2 | 9 | 11.5 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `no idea` | 2 | casual 10, lazy 2 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `it's the` | 1 | casual 11 |
| `want to` | 3 | casual 7, sexy 4, angry 1 |
| `around the` | 4 | casual 5, lazy 4, angry 3, sexy 2 |
| `the neighbors` | 3 | sexy 8, casual 7, lazy 4 |
| `have been` | 4 | casual 13, lazy 4, angry 1, sexy 1 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 12 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 53 |
| `that is` | 4 | casual 76, lazy 26, sexy 25, angry 15 |
| `is that` | 3 | sexy 15, casual 9, angry 3 |
| `you have` | 4 | casual 20, lazy 5, angry 2, sexy 2 |
| `got the` | 3 | casual 27, lazy 2, sexy 1 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `the next` | 4 | casual 17, lazy 8, sexy 6, angry 4 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 12 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `did you` | 4 | casual 192, sexy 53, angry 28, lazy 5 |
| `what did` | 4 | casual 41, angry 19, sexy 11, lazy 1 |
| `by the` | 4 | casual 31, lazy 21, sexy 19, angry 7 |
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `you forget` | 2 | casual 4, lazy 4 |
| `used to` | 2 | casual 6, lazy 2 |
| `to go` | 3 | casual 6, angry 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=9738): a 9.0%, the 4.2%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9738): the 11.0%, a 2.2%, you 1.8%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9737): the 6.7%, a 3.0%, is 2.7%, of 1.8%, for 1.8%, are 1.7%
- assistant pos last (n=9738): it 4.0%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9738): the 14.0%, my 10.1%, our 8.1%, i 6.2%, we 5.4%, you 4.6%
- user pos 1 (n=9675): the 3.3%, you 2.4%, a 1.9%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9586): the 7.4%, a 3.2%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9738): again 2.3%, it 2.0%, now 1.3%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.5%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1541 |
| lazy | 1 / 2155 |

