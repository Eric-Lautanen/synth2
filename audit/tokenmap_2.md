# synth2 token-attractor map

Generated 2026-10-07 13:48  |  corpus 950 rows, **1533 assistant turns**, 1533 user turns
Probe: `probe_out2.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T13:21:40

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.3% | 5.9% | +2.6 |
| `the`-opener (user) | 4.9% | 7.1% | +2.2 |
| copula-only | 0.2% | 1.3% | +1.1 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.9% | < 12% |
| `the`-opener (user) | 7.1% | n/a |
| copula-only turns | 1.3% | < 4% |
| registers carrying a top attractor | 0 / 1 | n/a |
| probe outputs carrying a top attractor | 0 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `did you get` | 3 | 13 | 11.6 | casual 13 |
| `what did you` | 3 | 8 | 10.6 | casual 8 |
| `in the morning` | 3 | 8 | 8.9 | casual 8 |
| `twenty minutes` | 2 | 17 | 8.6 | casual 17 |
| `an hour` | 2 | 19 | 8.5 | casual 19 |
| `how many` | 2 | 8 | 7.9 | casual 8 |
| `is a good` | 3 | 12 | 7.8 | casual 12 |
| `tell me` | 2 | 8 | 7.8 | casual 8 |
| `ten minutes` | 2 | 10 | 7.8 | casual 10 |
| `oh no` | 2 | 13 | 7.4 | casual 13 |
| `at least` | 2 | 14 | 7.4 | casual 14 |
| `that is a` | 3 | 11 | 7.4 | casual 11 |
| `my mum` | 2 | 9 | 7.3 | casual 9 |
| `better than` | 2 | 13 | 7.0 | casual 13 |
| `too much` | 2 | 8 | 6.7 | casual 8 |
| `next time` | 2 | 11 | 6.6 | casual 11 |
| `much better` | 2 | 9 | 6.6 | casual 9 |
| `couple of` | 2 | 8 | 6.5 | casual 8 |
| `not bad` | 2 | 8 | 6.5 | casual 7 |
| `i've been` | 2 | 26 | 6.4 | casual 26 |
| `any good` | 2 | 8 | 6.2 | casual 8 |
| `that is the` | 3 | 8 | 6.2 | casual 8 |
| `how long` | 2 | 8 | 6.0 | casual 8 |
| `kind of` | 2 | 10 | 6.0 | casual 10 |
| `i've got` | 2 | 17 | 5.8 | casual 17 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|

## 4. Opener maps

- assistant pos 0 (n=1533): the 5.9%, yeah 4.2%, a 3.2%, i 3.1%, not 2.4%, how 2.3%
- assistant pos 1 (n=1511): the 5.8%, it 5.6%, a 3.8%, is 2.7%, i 2.3%, you 1.9%
- assistant pos 2 (n=1462): the 5.4%, i 3.5%, is 3.2%, a 3.0%, it 2.9%, in 2.0%
- assistant pos last (n=1533): it 6.3%, again 1.6%, now 1.5%, you 1.4%, time 1.4%, out 1.2%
- user pos 0 (n=1533): did 7.5%, the 7.1%, how's 4.6%, you 4.5%, i 3.9%, what 3.5%
- user pos 1 (n=1493): the 9.6%, you 7.0%, a 3.5%, was 2.9%, did 2.1%, are 2.0%
- user pos 2 (n=1424): the 5.8%, a 4.1%, you 3.5%, is 2.0%, get 1.7%, for 1.6%
- user pos last (n=1533): today 2.3%, again 2.0%, weekend 2.0%, week 1.8%, up 1.6%, it 1.6%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **25.6%**; model outputs: **23.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 392 / 1533 |

