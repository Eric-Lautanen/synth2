# pass 49, chunk two -- handover notes

Hand-written rewrites for the next 70 casual parrot rows. Lead verifies and
applies; this file records what changed and what was deliberately left.

**File:** `audit/changes_pass49_chunk2.json` (compact `apply_rewrites` form)
**Apply:** `python scripts/apply_rewrites.py audit/changes_pass49_chunk2.json --dry`
then drop `--dry`. Default target is `raw/small_talk_casual.jsonl`, which is correct.

## Coverage

| | |
|---|---|
| rows edited | 70 |
| edit records | 73 (3 rows also carry a user-side currency fix) |
| casual parrots before | 238 |
| casual parrots after (simulated) | 168 |
| cleared by this chunk | 70 |
| rows in the chunk that still parrot | 0 |

Dry run on the live corpus: `round-trip check: 0 non-identical line(s) of 2001`,
`would rewrite 73 row(s) of 2001`. Simulated apply on a copy of the lane, then
`synth2_parrotscan.py`: 238 -> 168, one row cleared per rewrite, no collateral
and no row that needed a second pass.

## The rule applied -- corrected to yours

Chunk one echoed a content token from *any* user turn in the row. This chunk
echoes **the turn immediately being replied to**, one word altered, so the
shared run stays at four words or fewer and never reaches six. Nothing else
moves: same scene, same speaker, same length bucket, 10-13 words on every
rewritten reply, all lowercase, ASCII, no hyphens, no dashes.

Two shapes in this chunk:

    echo clause kept, tail changed
    before  u: a low hum when it heats up.
            a: a low hum when it heats could be the fan, cooking evenly?
    after   a: a hum at startup could be the fan, so note how it heats.

    echo clause deleted, reply rebuilt around a single echoed token
    before  u: one of the younger crowd just paid the lot and we all transferred her.
            a: one paid the lot and we all transferred her, the modern way.
    after   a: one person paid the lot, and everyone else transfers, which is modern.

The second shape is the one that matters: the original had five 6-grams shared
with its user turn, and the "echo then comma then question" mold is what
produced them. Where the mold and the 6-gram rule collide, the mold goes.

## Currency folded in

`pounds` -> `bucks` on three rows in this chunk, both sides where both sides had
it: `st2_casual_001356` (`twelve pounds`), `st2_casual_001428` (`fifty pounds`),
`st2_casual_001431` (`nine pounds`). Same pattern as `st2_casual_001194` in
chunk one. If you would rather sweep `pounds` in one pass of its own, drop those
three `u` records and the two `a` records that quote them -- the parrot rewrites
stand on their own.

## Deliberately NOT fixed here -- the Britain set, your second pass

| row | markers |
|---|---|
| `st2_casual_001255` | `mot`, `three hundred odd` (currency implied) |
| `st2_casual_001428` | `premium bonds` -- the product itself, not the currency |

`premium bonds` is not in my 145-term marker list; it surfaced because I was
reading the row. Worth adding before the Britain pass runs, because the phrase
survives a currency swap and still reads British.

## Validation run on every row

1. no assistant turn shares a 6-gram with any user turn in its row
2. every rewritten assistant turn shares a 4+ char content token with the turn
   immediately before it -- the echo is measured, not assumed
3. all lowercase, pure ASCII, no hyphens, no em dash
4. no British vocabulary term, no British spelling stem in any edited turn
5. rewritten replies land in 10-13 words
6. no 5-gram collision with the corpus outside the row itself
7. the 84 edited lines against each other: 0 shared 5-grams, 0 near-dups at
   Jaccard 0.60 -- a staged chunk is invisible to the corpus gate, so it has to
   be checked against itself

Result across the chunk: **0 errors, 0 warnings.**

Question share is unchanged: 105 -> 104 of 161 assistant turns in these rows,
lane stays at 43.9 pct.

## Amendment -- one line changed after the cross-chunk scan

`st2_casual_001347` a0 was `have they been in touch yet, or are you still waiting?`
It collided with chunk one's `st2_casual_000956` a0 on `yet or are you still`.
Neither chunk could see the other: the corpus index does not hold staged files,
and the per-chunk self-scan only compares a chunk with itself. Now
`a heating firm that does not call back, chase them again today.`

With all four chunks stacked the cross-chunk scan is clean: 310 edited lines,
0 shared 5-grams, 0 near-dups. Question share in these rows is 105 -> 103 of 161.

## Next

Chunk three: the remaining 101 casual parrots, then angry 34 plus lazy 2.
`b4430` next, now that chunk one is in your hands.
