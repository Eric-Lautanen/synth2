# pass 49, chunk four -- handover notes

The last 31 casual parrot rows. This chunk closes the class: with all four
chunks applied, `synth2_parrotscan.py --corpus --lane casual` returns **0**.

**File:** `audit/changes_pass49_chunk4.json` (compact `apply_rewrites` form)
**Apply:** `python scripts/apply_rewrites.py audit/changes_pass49_chunk4.json --dry`
then drop `--dry`. Default target is `raw/small_talk_casual.jsonl`, which is correct.

## Coverage

| | |
|---|---|
| rows edited | 31 |
| edit records | 38 |
| casual parrots before | 238 |
| casual parrots after, this chunk alone (simulated) | 207 |
| cleared by this chunk | 31 |
| rows in the chunk that still parrot | 0 |

## The whole class, simulated end to end

Applied in order -- chunk one (your folded file), two, three, four -- to a copy of
the lane, then rescanned:

    PARROT: 0 rows at 6+ grams

238 -> 0. And the 310 edited lines across the four chunks, scanned against each
other: 0 shared 5-grams, 0 near-dups at Jaccard 0.60.

That last number is the one to keep, because it is the only check that can see a
collision between two chunks. It already found one: chunk two's `001347` shared
`yet or are you still` with chunk one's `000956`, and neither chunk could see the
other. Fixed in chunk two.

## Validation

`python scripts/synth2_changefile_check.py audit/changes_pass49_chunk4.json`

    lane=casual rows=31 edited_lines=38 errors=0 warnings=0
    questions in these rows: 30 -> 26 of 75 assistant turns

The 5-gram gate caught one line during drafting, `a week to settle into` against
`casual:811` at `st2_casual_001749`, and it was rewritten.

## Rows here that belong to pass 50

Left alone, as agreed -- the parrot class is fixed and the scene is not:

| row | markers |
|---|---|
| `st2_casual_001941` | `milk float` |
| `st2_casual_001961` | `mot` |
| `st2_casual_001965` | `bypass`, `forty meters` |
| `st2_casual_001957` | `duvet`, `a day on the line` |
| `st2_casual_001868` | `airing cupboard`, `pipework` |
| `st2_casual_001874` | `washing line` |

`milk float` and `washing line` are new to the list and both are strong tells; I
have added them to revision 2 of the pass 50 worklist.

## State of pass 49

| lane | parrots | state |
|---|---|---|
| casual | 238 -> 0 | done in four chunks, all staged |
| lazy | 2 | not started |
| angry | 34 | not started |
| sexy | 0 | clean |

So 36 rows remain in the class, all in the two small lanes, and they are one
chunk of work. Then pass 50 relocates 85 scenes.
