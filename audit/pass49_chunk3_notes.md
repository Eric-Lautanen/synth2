# pass 49, chunk three -- handover notes

Hand-written rewrites for the next 70 casual parrot rows. Same rule as chunk
two: the echo comes from the turn immediately being replied to, one word
altered, so the shared run never reaches six.

**File:** `audit/changes_pass49_chunk3.json` (compact `apply_rewrites` form)
**Apply:** `python scripts/apply_rewrites.py audit/changes_pass49_chunk3.json --dry`
then drop `--dry`. Default target is `raw/small_talk_casual.jsonl`, which is correct.

## Coverage

| | |
|---|---|
| rows edited | 70 |
| edit records | 72 (1 row also carries a user-side currency fix) |
| casual parrots before | 238 |
| casual parrots after (simulated, this chunk alone) | 168 |
| cleared by this chunk | 70 |
| rows in the chunk that still parrot | 0 |

Dry run on the live corpus: `round-trip check: 0 non-identical line(s) of 2001`,
`would rewrite 72 row(s) of 2001`. Simulated apply on a copy of the lane, then
`synth2_parrotscan.py`: one row cleared per rewrite, no collateral, nothing left
needing a second pass.

Chunks one to three together clear 67 + 70 + 70 = 207 of the 238 casual parrots.
**31 rows left in casual.**

## Currency folded in

`pounds` -> `bucks` on two rows, both sides where both sides had it:
`st2_casual_001582` (`eight pounds`), `st2_casual_001588` (`fifteen pounds`).
As with chunk two, drop those records if you would rather sweep `pounds` once.

## Deliberately NOT fixed here -- the Britain set, your second pass

| row | markers |
|---|---|
| `st2_casual_001495` | `single yellow` |
| `st2_casual_001527` | `bin collection` |
| `st2_casual_001541` | `mate`, `joiner`, `mates rates` |
| `st2_casual_001556` | `pub` (darts league) |
| `st2_casual_001558` | `cricket`, `july` |
| `st2_casual_001563` | `snooker club` |
| `st2_casual_001566` | `rounders` |
| `st2_casual_001584` | `trolley` |
| `st2_casual_001617` | `wellington boot` |

Nine rows, and only one of them (`single yellow`) is a term in my 145-term
marker list. The rest are the same story as `premium bonds` in chunk two: the
list catches the obvious nouns and misses the scene. `rounders`, `snooker` and
`wellington` are the three I would add first.

## Validation run on every row

1. no assistant turn shares a 6-gram with any user turn in its row
2. every rewritten assistant turn shares a 4+ char content token with the turn
   immediately before it
3. all lowercase, pure ASCII, no hyphens, no em dash
4. no British vocabulary term, no British spelling stem in any edited turn
5. rewritten replies land in 10-13 words
6. no 5-gram collision with the corpus outside the row itself -- this caught one
   line, `is the machine walking across the floor`, against `casual:1452`
7. the 85 edited lines against each other: 0 shared 5-grams, 0 near-dups at
   Jaccard 0.60

Result across the chunk: **0 errors, 0 warnings.**

## One thing to check before you fold

`st2_casual_001567` and `st2_casual_001692` are near-identical rows in the
corpus: both open with a new series and both answer with a detective in a small
town. They are not a parrot problem and not a duplicate in the 3-shingle sense,
but the opener pair is the same joke twice. I gave them different rewrites, so
this chunk does not make it worse. Whether the corpus keeps both is your call.

## Next

Chunk four: the last 31 casual parrots, then angry 34 plus lazy 2. `b4430`
still queued behind them.
