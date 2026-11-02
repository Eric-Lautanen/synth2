# synth2 token-attractor map

Generated 2026-10-07 13:57  |  corpus 1043 rows, **1738 assistant turns**, 1738 user turns
Probe: `probe_out3.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T13:48:23

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.9% | 7.0% | +1.1 |
| `the`-opener (user) | 7.1% | 7.4% | +0.3 |
| copula-only | 1.3% | 1.5% | +0.2 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.0% | < 12% |
| `the`-opener (user) | 7.4% | n/a |
| copula-only turns | 1.5% | < 4% |
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
| `that is a good` | 4 | 8 | 13.9 | casual 8 |
| `did you get` | 3 | 14 | 11.4 | casual 14 |
| `what did you` | 3 | 8 | 10.3 | casual 8 |
| `twenty minutes` | 2 | 17 | 8.7 | casual 17 |
| `in the morning` | 3 | 8 | 8.6 | casual 8 |
| `an hour` | 2 | 20 | 8.5 | casual 20 |
| `is the best` | 3 | 9 | 8.5 | casual 9 |
| `give it a` | 3 | 10 | 8.5 | casual 10 |
| `same here` | 2 | 8 | 8.0 | casual 8 |
| `ten minutes` | 2 | 12 | 8.0 | casual 12 |
| `is a good` | 3 | 15 | 7.8 | casual 15 |
| `tell me` | 2 | 8 | 7.7 | casual 8 |
| `how many` | 2 | 12 | 7.7 | casual 12 |
| `oh no` | 2 | 13 | 7.5 | casual 13 |
| `my mum` | 2 | 9 | 7.5 | casual 9 |
| `at least` | 2 | 14 | 7.4 | casual 14 |
| `that is a` | 3 | 14 | 7.4 | casual 14 |
| `better than` | 2 | 13 | 6.9 | casual 13 |
| `too much` | 2 | 8 | 6.7 | casual 8 |
| `next time` | 2 | 13 | 6.7 | casual 13 |
| `more than` | 2 | 8 | 6.7 | casual 8 |
| `i've been` | 2 | 26 | 6.6 | casual 26 |
| `how far` | 2 | 8 | 6.6 | casual 8 |
| `couple of` | 2 | 8 | 6.5 | casual 8 |
| `much better` | 2 | 9 | 6.5 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|

## 4. Opener maps

- assistant pos 0 (n=1738): the 7.0%, yeah 3.7%, a 3.1%, i 2.8%, that 2.4%, how 2.4%
- assistant pos 1 (n=1709): the 6.1%, it 6.0%, a 3.9%, is 3.3%, i 2.0%, you 2.0%
- assistant pos 2 (n=1640): the 5.5%, is 3.4%, i 3.1%, a 3.1%, it 2.9%, in 2.0%
- assistant pos last (n=1738): it 6.5%, again 1.7%, now 1.4%, you 1.3%, time 1.3%, out 1.1%
- user pos 0 (n=1738): the 7.4%, did 6.6%, how's 4.0%, you 4.0%, i 3.9%, my 3.3%
- user pos 1 (n=1675): the 9.1%, you 6.3%, a 3.7%, was 2.7%, is 2.1%, are 2.0%
- user pos 2 (n=1593): the 5.7%, a 4.1%, you 3.1%, is 2.0%, for 1.5%, get 1.5%
- user pos last (n=1738): today 2.1%, weekend 2.0%, again 2.0%, week 1.8%, it 1.7%, up 1.6%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **23.3%**; model outputs: **35.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 405 / 1738 |

