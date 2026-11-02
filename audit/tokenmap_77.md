# synth2 token-attractor map

Generated 2026-10-22 10:04  |  corpus 8172 rows, **10542 assistant turns**, 10542 user turns
Probe: `probe_out77_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T06:54:57

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.6% | 4.6% | +0.0 |
| `the`-opener (user) | 14.1% | 14.1% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `is going` | - | 5% | - | 38x |
| `the weekend` | 3% | 5% | 18x | 28x |
| `in the` | - | 10% | - | 3x |
| `worse than` | - | 3% | - | 44x |
| `one or` | - | 3% | - | 44x |
| `now the` | - | 3% | - | 39x |
| `for a` | - | 7% | - | 3x |
| `it will` | - | 3% | - | 32x |
| `and that` | - | 3% | - | 32x |
| `a bad` | - | 3% | - | 29x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.6% | < 12% |
| `the`-opener (user) | 14.1% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `is going` | 14 | 13.3 | 3.8 | 5% | 38x | casual 10, lazy 2, angry 1 |
| `the weekend` | 19 | 18.0 | 37.0 | 5% | 28x | casual 14, lazy 4, sexy 1 |
| `in the` | 380 | 360.5 | 340.5 | 10% | 3x | casual 164, sexy 73, angry 67 |
| `worse than` | 8 | 7.6 | 2.8 | 3% | 44x | casual 5, angry 2, sexy 1 |
| `one or` | 8 | 7.6 | 0.0 | 3% | 44x | casual 6, angry 1, sexy 1 |
| `now the` | 9 | 8.5 | 2.8 | 3% | 39x | casual 6, lazy 3 |
| `for a` | 209 | 198.3 | 161.3 | 7% | 3x | angry 93, casual 66, lazy 23 |
| `it will` | 11 | 10.4 | 2.8 | 3% | 32x | casual 11 |
| `and that` | 11 | 10.4 | 0.9 | 3% | 32x | angry 4, casual 4, lazy 2 |
| `a bad` | 12 | 11.4 | 1.9 | 3% | 29x | angry 5, lazy 4, casual 3 |
| `at the` | 257 | 243.8 | 233.4 | 7% | 3x | casual 98, sexy 67, lazy 52 |
| `i've been` | 14 | 13.3 | 16.1 | 3% | 25x | casual 14 |
| `is on` | 15 | 14.2 | 19.9 | 3% | 23x | casual 12, lazy 2, sexy 1 |
| `the work` | 16 | 15.2 | 2.8 | 3% | 22x | lazy 8, casual 6, angry 2 |
| `in a` | 98 | 93.0 | 77.8 | 5% | 5x | casual 29, angry 27, lazy 22 |
| `have been` | 19 | 18.0 | 40.8 | 3% | 18x | casual 12, lazy 4, sexy 2 |
| `years of` | 20 | 19.0 | 17.1 | 3% | 18x | casual 13, angry 5, lazy 1 |
| `we are` | 21 | 19.9 | 31.3 | 3% | 17x | sexy 13, casual 4, lazy 2 |
| `you never` | 22 | 20.9 | 2.8 | 3% | 16x | angry 16, casual 4, lazy 2 |
| `will be` | 22 | 20.9 | 7.6 | 3% | 16x | casual 18, sexy 3, lazy 1 |
| `too much` | 22 | 20.9 | 7.6 | 3% | 16x | casual 9, lazy 9, sexy 2 |
| `to do` | 24 | 22.8 | 21.8 | 3% | 15x | casual 20, angry 2, lazy 1 |
| `is still` | 24 | 22.8 | 13.3 | 3% | 15x | casual 12, lazy 8, angry 2 |
| `that is` | 165 | 156.5 | 12.3 | 5% | 3x | casual 96, lazy 26, sexy 25 |
| `is the` | 481 | 456.3 | 69.2 | 7% | 1x | casual 292, lazy 116, angry 50 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.7 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `the front desk` | 3 | 13 | 12.9 | angry 8, lazy 4, casual 1 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 15 | 12.1 | angry 6, casual 3, sexy 3 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `feel like a` | 3 | 11 | 11.2 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.6 | casual 15, angry 2 |
| `did you get` | 3 | 41 | 10.5 | casual 37, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `is going` | 4 | casual 10, lazy 2, angry 1, sexy 1 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `in the` | 5 | casual 164, sexy 73, angry 67, lazy 67 |
| `worse than` | 3 | casual 5, angry 2, sexy 1 |
| `one or` | 3 | casual 6, angry 1, sexy 1 |
| `now the` | 2 | casual 6, lazy 3 |
| `for a` | 5 | angry 93, casual 66, lazy 23, sexy 23 |
| `it will` | 1 | casual 11 |
| `and that` | 4 | angry 4, casual 4, lazy 2, formal 1 |
| `a bad` | 3 | angry 5, lazy 4, casual 3 |
| `at the` | 5 | casual 98, sexy 67, lazy 52, angry 38 |
| `i've been` | 1 | casual 14 |
| `is on` | 3 | casual 12, lazy 2, sexy 1 |
| `the work` | 3 | lazy 8, casual 6, angry 2 |
| `in a` | 5 | casual 29, angry 27, lazy 22, sexy 18 |
| `have been` | 4 | casual 12, lazy 4, sexy 2, angry 1 |
| `years of` | 4 | casual 13, angry 5, lazy 1, sexy 1 |
| `we are` | 5 | sexy 13, casual 4, lazy 2, angry 1 |
| `you never` | 3 | angry 16, casual 4, lazy 2 |
| `will be` | 3 | casual 18, sexy 3, lazy 1 |
| `too much` | 5 | casual 9, lazy 9, sexy 2, angry 1 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `is still` | 4 | casual 12, lazy 8, angry 2, sexy 2 |
| `that is` | 5 | casual 96, lazy 26, sexy 25, angry 17 |
| `is the` | 5 | casual 292, lazy 116, angry 50, sexy 16 |

## 4. Opener maps

- assistant pos 0 (n=10542): a 10.2%, the 4.6%, did 2.3%, how 2.1%, that 1.7%, was 1.6%
- assistant pos 1 (n=10542): the 10.5%, a 2.0%, is 1.8%, you 1.7%, does 1.1%, on 1.0%
- assistant pos 2 (n=10541): the 6.9%, a 2.8%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10542): it 3.8%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10542): the 14.1%, my 9.8%, our 8.1%, we 6.2%, i 6.0%, you 5.7%
- user pos 1 (n=10479): the 3.2%, you 2.2%, a 1.8%, was 1.0%, got 1.0%, did 1.0%
- user pos 2 (n=10389): the 7.8%, a 3.3%, is 1.7%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10542): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.1%, morning 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.0%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

