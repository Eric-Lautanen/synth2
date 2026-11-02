# synth2 token-attractor map

Generated 2026-10-23 09:45  |  corpus 8544 rows, **10944 assistant turns**, 10944 user turns
Probe: `probe_out83_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T06:13:18

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.4% | 5.5% | +0.0 |
| `the`-opener (user) | 14.4% | 14.4% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a real` | - | 7% | - | 7x |
| `get a` | - | 5% | - | 20x |
| `get the` | - | 5% | - | 18x |
| `a bit` | - | 5% | - | 15x |
| `the morning` | 3% | 5% | 10x | 14x |
| `the whole` | 7% | 7% | 4x | 4x |
| `is the` | - | 8% | - | 2x |
| `i am` | 5% | 5% | 8x | 8x |
| `to get` | - | 3% | - | 33x |
| `get to` | - | 3% | - | 33x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.5% | < 12% |
| `the`-opener (user) | 14.4% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 38 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a real` | 98 | 89.5 | 36.5 | 7% | 7x | casual 75, angry 13, lazy 10 |
| `get a` | 27 | 24.7 | 10.1 | 5% | 20x | casual 17, sexy 6, lazy 3 |
| `get the` | 30 | 27.4 | 17.4 | 5% | 18x | casual 16, lazy 8, angry 2 |
| `a bit` | 36 | 32.9 | 29.2 | 5% | 15x | casual 34, angry 1, lazy 1 |
| `the morning` | 38 | 34.7 | 24.7 | 5% | 14x | casual 18, lazy 11, angry 5 |
| `the whole` | 187 | 170.9 | 117.0 | 7% | 4x | lazy 83, casual 57, angry 32 |
| `is the` | 490 | 447.7 | 76.8 | 8% | 2x | casual 292, lazy 116, angry 50 |
| `i am` | 68 | 62.1 | 35.6 | 5% | 8x | casual 46, lazy 11, sexy 10 |
| `to get` | 11 | 10.1 | 10.1 | 3% | 33x | casual 6, lazy 2, angry 1 |
| `get to` | 11 | 10.1 | 1.8 | 3% | 33x | casual 5, angry 4, sexy 2 |
| `no idea` | 13 | 11.9 | 7.3 | 3% | 28x | casual 11, lazy 2 |
| `is going` | 15 | 13.7 | 3.7 | 3% | 24x | casual 10, lazy 2, angry 1 |
| `the post` | 16 | 14.6 | 9.1 | 3% | 23x | casual 10, lazy 4, formal 2 |
| `bit of` | 16 | 14.6 | 8.2 | 3% | 23x | casual 15, angry 1 |
| `you going` | 17 | 15.5 | 4.6 | 3% | 21x | casual 15, angry 2 |
| `is my` | 17 | 15.5 | 14.6 | 3% | 21x | sexy 10, casual 5, lazy 2 |
| `do you` | 107 | 97.8 | 48.4 | 5% | 5x | casual 73, angry 25, sexy 8 |
| `the weekend` | 19 | 17.4 | 35.6 | 3% | 19x | casual 14, lazy 4, sexy 1 |
| `got a` | 23 | 21.0 | 79.5 | 3% | 16x | casual 17, sexy 3, angry 2 |
| `how is` | 28 | 25.6 | 10.1 | 3% | 13x | angry 16, casual 9, sexy 3 |
| `the usual` | 29 | 26.5 | 9.1 | 3% | 13x | casual 21, lazy 7, formal 1 |
| `a long` | 32 | 29.2 | 7.3 | 3% | 11x | casual 21, lazy 8, angry 3 |
| `is a` | 513 | 468.8 | 63.0 | 7% | 1x | angry 222, casual 147, lazy 116 |
| `way to` | 36 | 32.9 | 2.7 | 3% | 10x | casual 17, angry 11, lazy 6 |
| `just a` | 37 | 33.8 | 21.0 | 3% | 10x | casual 24, angry 7, lazy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `the front desk` | 3 | 14 | 12.5 | angry 8, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `counts as a` | 3 | 12 | 12.4 | formal 5, casual 2, lazy 2 |
| `an hour of` | 3 | 17 | 12.3 | angry 6, casual 3, formal 3 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `get a` | 4 | casual 17, sexy 6, lazy 3, formal 1 |
| `get the` | 5 | casual 16, lazy 8, angry 2, formal 2 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 2 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 16 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `to get` | 5 | casual 6, lazy 2, angry 1, formal 1 |
| `get to` | 3 | casual 5, angry 4, sexy 2 |
| `no idea` | 2 | casual 11, lazy 2 |
| `is going` | 5 | casual 10, lazy 2, angry 1, formal 1 |
| `the post` | 3 | casual 10, lazy 4, formal 2 |
| `bit of` | 2 | casual 15, angry 1 |
| `you going` | 2 | casual 15, angry 2 |
| `is my` | 3 | sexy 10, casual 5, lazy 2 |
| `do you` | 4 | casual 73, angry 25, sexy 8, lazy 1 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `got a` | 4 | casual 17, sexy 3, angry 2, lazy 1 |
| `how is` | 3 | angry 16, casual 9, sexy 3 |
| `the usual` | 3 | casual 21, lazy 7, formal 1 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `is a` | 5 | angry 222, casual 147, lazy 116, sexy 15 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 2 |
| `just a` | 4 | casual 24, angry 7, lazy 4, formal 2 |

## 4. Opener maps

- assistant pos 0 (n=10944): a 10.1%, the 5.5%, did 2.3%, how 2.2%, does 1.7%, that 1.7%
- assistant pos 1 (n=10944): the 11.0%, a 2.0%, is 1.8%, you 1.7%, does 1.2%, on 0.9%
- assistant pos 2 (n=10943): the 7.1%, a 2.9%, is 2.7%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10944): it 3.9%, now 1.5%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10944): the 14.4%, my 9.7%, our 8.4%, i 6.3%, we 6.1%, you 5.4%
- user pos 1 (n=10881): the 3.2%, you 2.1%, a 1.7%, was 1.0%, got 1.0%, is 1.0%
- user pos 2 (n=10791): the 7.8%, a 3.5%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=10944): again 2.1%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.8%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

