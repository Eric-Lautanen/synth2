# synth2 token-attractor map

Generated 2026-10-25 08:19  |  corpus 9450 rows, **11923 assistant turns**, 11923 user turns
Probe: `probe_out96_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T04:51:57

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.3% | 6.5% | +0.2 |
| `the`-opener (user) | 14.8% | 14.8% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i will` | - | 8% | - | 12x |
| `is the` | - | 10% | - | 2x |
| `just the` | 3% | 5% | 13x | 20x |
| `a bit` | - | 5% | - | 17x |
| `doing it` | - | 3% | - | 50x |
| `time is` | - | 3% | - | 44x |
| `nothing on` | - | 3% | - | 44x |
| `at least` | - | 5% | - | 8x |
| `the apartment` | - | 3% | - | 33x |
| `in my` | - | 3% | - | 28x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.5% | < 12% |
| `the`-opener (user) | 14.8% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `i will` | 84 | 70.5 | 7.5 | 8% | 12x | casual 31, formal 29, lazy 14 |
| `is the` | 510 | 427.7 | 78.8 | 10% | 2x | casual 292, lazy 116, angry 50 |
| `just the` | 30 | 25.2 | 10.9 | 5% | 20x | casual 19, lazy 6, angry 3 |
| `a bit` | 36 | 30.2 | 26.8 | 5% | 17x | casual 34, angry 1, lazy 1 |
| `doing it` | 8 | 6.7 | 2.5 | 3% | 50x | casual 7, formal 1 |
| `time is` | 9 | 7.5 | 0.0 | 3% | 44x | casual 4, lazy 3, angry 2 |
| `nothing on` | 9 | 7.5 | 0.8 | 3% | 44x | casual 8, lazy 1 |
| `at least` | 72 | 60.4 | 11.7 | 5% | 8x | casual 31, angry 20, sexy 12 |
| `the apartment` | 12 | 10.1 | 11.7 | 3% | 33x | casual 7, sexy 4, lazy 1 |
| `in my` | 14 | 11.7 | 31.9 | 3% | 28x | lazy 6, sexy 4, casual 3 |
| `for the` | 315 | 264.2 | 291.9 | 7% | 3x | casual 120, sexy 70, angry 61 |
| `the weekend` | 19 | 15.9 | 32.7 | 3% | 21x | casual 14, lazy 4, sexy 1 |
| `you got` | 20 | 16.8 | 12.6 | 3% | 20x | casual 19, angry 1 |
| `out the` | 24 | 20.1 | 25.2 | 3% | 17x | lazy 11, casual 8, angry 4 |
| `it is` | 141 | 118.3 | 52.0 | 5% | 4x | casual 82, lazy 36, angry 10 |
| `you have` | 28 | 23.5 | 12.6 | 3% | 14x | casual 18, lazy 5, angry 2 |
| `on it` | 28 | 23.5 | 15.9 | 3% | 14x | casual 14, formal 6, angry 4 |
| `what did you` | 33 | 27.7 | 26.8 | 3% | 12x | casual 26, sexy 6, lazy 1 |
| `a quiet` | 33 | 27.7 | 4.2 | 3% | 12x | casual 13, formal 7, lazy 7 |
| `did you get` | 41 | 34.4 | 34.4 | 3% | 10x | casual 37, angry 2, lazy 2 |
| `it was` | 42 | 35.2 | 54.5 | 3% | 9x | casual 26, sexy 7, lazy 5 |
| `did it` | 42 | 35.2 | 10.9 | 3% | 9x | casual 32, lazy 4, sexy 3 |
| `so the` | 45 | 37.7 | 16.8 | 3% | 9x | casual 21, angry 11, formal 10 |
| `of it` | 45 | 37.7 | 24.3 | 3% | 9x | casual 32, sexy 5, angry 4 |
| `i have` | 50 | 41.9 | 77.2 | 3% | 8x | casual 34, lazy 12, sexy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 15.9 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `the office manager` | 3 | 9 | 12.6 | formal 9 |
| `i have been` | 3 | 10 | 12.5 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `the front desk` | 3 | 14 | 12.1 | angry 8, lazy 4, casual 1 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.3 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i will` | 4 | casual 31, formal 29, lazy 14, sexy 10 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 36 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `doing it` | 2 | casual 7, formal 1 |
| `time is` | 3 | casual 4, lazy 3, angry 2 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `at least` | 4 | casual 31, angry 20, sexy 12, lazy 9 |
| `the apartment` | 3 | casual 7, sexy 4, lazy 1 |
| `in my` | 4 | lazy 6, sexy 4, casual 3, angry 1 |
| `for the` | 5 | casual 120, sexy 70, angry 61, formal 40 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `you got` | 2 | casual 19, angry 1 |
| `out the` | 4 | lazy 11, casual 8, angry 4, sexy 1 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `you have` | 5 | casual 18, lazy 5, angry 2, sexy 2 |
| `on it` | 5 | casual 14, formal 6, angry 4, lazy 3 |
| `what did you` | 3 | casual 26, sexy 6, lazy 1 |
| `a quiet` | 4 | casual 13, formal 7, lazy 7, angry 6 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `it was` | 5 | casual 26, sexy 7, lazy 5, angry 2 |
| `did it` | 5 | casual 32, lazy 4, sexy 3, angry 2 |
| `so the` | 4 | casual 21, angry 11, formal 10, sexy 3 |
| `of it` | 5 | casual 32, sexy 5, angry 4, lazy 3 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |

## 4. Opener maps

- assistant pos 0 (n=11923): a 10.0%, the 6.5%, does 2.7%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=11923): the 11.4%, a 2.1%, is 1.7%, does 1.6%, you 1.6%, on 0.9%
- assistant pos 2 (n=11922): the 7.4%, a 3.0%, is 2.5%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11923): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11923): the 14.8%, my 9.4%, our 9.0%, i 6.6%, we 5.9%, you 5.0%
- user pos 1 (n=11860): the 3.3%, you 2.0%, a 1.6%, is 1.2%, got 1.0%, was 1.0%
- user pos 2 (n=11770): the 8.1%, a 3.9%, is 1.6%, my 1.3%, you 1.2%, in 1.2%
- user pos last (n=11923): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

