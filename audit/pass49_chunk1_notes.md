# pass 49, chunk one -- handover notes

Hand-written rewrites for the first 82 casual rows. Lead verifies and applies;
this file is the record of what was changed and what was deliberately left.

**File:** `audit/changes_pass49_chunk1.json` (compact `apply_rewrites` form)
**Apply:** `python scripts/apply_rewrites.py audit/changes_pass49_chunk1.json --dry`
then drop `--dry`. Default target is `raw/small_talk_casual.jsonl`, which is correct.

## Coverage

| | |
|---|---|
| rows edited | 82 |
| edit records | 92 (10 rows fix both roles in one rewrite) |
| of which parrot rows | 70 |
| of which vocab-only rows | 12 |
| casual parrots before | 238 |
| casual parrots after | 171 |
| cleared by this chunk | 67 |
| vocab terms left in edited rows | 0 |

Dry run on the live corpus: `round-trip check: 0 non-identical line(s) of 2001`,
`would rewrite 92 row(s) of 2001`.

## The rule applied

The two house rules pull against each other here: every reply must echo an EXACT
content token from its own user turn, and no reply may share a 6-gram with one.
So the echo clause shrinks from a whole restatement to a token or two, and the
beat is carried by the comment or question that follows. Nothing else changes:
same scene, same speaker, same length bucket, 10-13 words on every rewritten
reply, all lowercase, ASCII, no dashes.

Example, `st2_casual_000514` (real pair from this chunk):

    before  u: that gig on friday was brilliant.
            a: wasn't it just, that gig on friday was brilliant from the off.
    after   a: wasn't it just. that friday had everything, and i am still hoarse.

The echo is now `friday` (a token from the user turn), and the shared run drops
from 6+ grams to a single word.

## Vocab residual folded in

`school run` 7 rows, `gran` 4, `satnav` 1 row (4 turns), `traffic warden` 1,
`chap`, `dual carriageway`, `faff`, `hob`, `loo`. One extra found during the
sweep: `st2_casual_001194` also carried `three hundred pounds`, so that row got
the currency fix as well (`pounds` -> `bucks`).

## Deliberately NOT fixed here -- the Britain set, your second pass

Four rows in this chunk still read as Britain. They are correct on the parrot
class now, but the scene still needs relocating, which is your second-pass work:

| row | markers |
|---|---|
| `st2_casual_000802` | `york`, `full english` |
| `st2_casual_000965` | `the dales` |
| `st2_casual_001031` | `bonfire night`, `the rec` |
| `st2_casual_001201` | `clocks going back` |

**This is why the Britain set is bigger than the 29 rows I first reported.**
`the dales`, `clocks going back` and `the rec` were not in my marker list when I
built that count, and they only surfaced because I was reading these rows line by
line. Treat 29 as a floor, not the total.

## Validation run on every row

1. no assistant turn shares a 6-gram with any user turn in its row (both rule
   variants: previous turn only, and any user turn)
2. every rewritten assistant turn shares a content token (4+ chars, not a
   stopword) with a user turn -- the echo is present, not assumed
3. all lowercase, pure ASCII, no dashes
4. no British vocabulary or spelling stem in any edited turn
5. rewritten replies land in 10-13 words

Result across the chunk: **0 errors, 0 warnings.**

## Next

Chunk two: the next 70 of the 171 remaining casual parrots, then chunk three to
clear casual, then angry 34 plus lazy 2. `b4430` follows chunk one's handover.
