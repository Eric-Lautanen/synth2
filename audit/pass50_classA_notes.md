# pass 50 class A -- four batches, 62 rows, done

Authored 2026-10-21 against the live casual lane. Applies with
`apply_rewrites.py <changes> ` -- positional, no `--file` flag on the changes
side, `--file` names the corpus.

| file | rows | edited lines |
|---|---|---|
| `changes_pass50_demo_classA.json` | 11 | 21 |
| `changes_pass50_classA_b1.json` | 9 | 18 |
| `changes_pass50_classA_b2.json` | 10 | 27 |
| `changes_pass50_classA_b3.json` | 15 | 43 |
| `changes_pass50_classA_b4.json` | 17 | 62 |

62 rows, 171 records. All five files together:
`rows=62 edited_lines=171 errors=0 warnings=0`.

## Order of application

Free. No row appears in two files, and no row appears in pass 49's chunks two to
five either (checked: overlap 0). The demo file was built outside pass 49's row
set for exactly this reason. **The 21 rows that do overlap pass 49 are not in any
of these files** -- they are still blocked and still mine.

## What was verified

1. Each file alone: 0 errors, 0 warnings.
2. All five merged: 0 errors, 0 warnings, no duplicate keys.
3. Merged with pass 49 chunks two, three and four (233 rows, 380 lines):
   **0 errors**. This is the check that matters, because pass 49 is unlanded and
   a change file is invisible to the corpus index until it applies.
4. Cross-lane 5-gram scan over all 416 edited lines from pass 50 plus pass 49
   chunks two to five, both lanes: **0 hits**. No per-lane gate can see this.

## Two gate changes this round

`synth2_changefile_check.py` gained:

- **`--show`**: prints old and new text for every edit. Added after I wrote
  `u1` on a six-turn row meaning the *fourth* turn. Role-relative `u1` is the
  second user turn, which in a six-turn row is array index 2, not 4. The write
  landed on the wrong turn and every gate stayed green, because the text I wrote
  was legal text -- it was just in the wrong place. `--show` makes that visible
  in one glance and it is now the first thing I run.
- **ORPHANED warn**: an unedited assistant turn whose own user turn this file
  rewrote and which no longer echoes it. This is the knock-on of the same class:
  move the user turn, forget the reply. It fired correctly on a deliberate
  single-row test before I trusted it.

## Style decisions worth knowing

- **`quiz night` kept on `001908`.** Both `001908` and `001549` are the same
  scene (a thursday quiz, needing a team). Rewriting both to `trivia night`
  converged them further; `pub` was the British word there, not `quiz`, so
  `001908` took `tavern` and kept `quiz night`. `001549` took `trivia night`.
- **`001291` structural defect fixed, not worked around.** Turns 2 and 4 were
  the same user turn twice, with someone already having swapped `trolley` to
  `cart` in the second copy. Rather than flag it again I rewrote turn 4 into the
  turn the assistant already answers -- `a2` says "quarterly is how it becomes a
  habit", so turn 4 now proposes quarterly. The duplicate is gone and no turn
  was deleted.
- **`001842` had a broken sentence** in turn 4: "the kids still believe the
  dame's hilarious are new". Fixed to "the villain's jokes are new" as part of
  the panto relocation. Worth a grep for other truncated clauses -- this one
  survived every gate because it is grammatical enough to parse.
- **`001944` needs nothing.** On the unblocked list but entirely US already.
- **`1706`, `1707`, `1842` turn-2/3 fixes**: `reorganised` -> `reorganized`,
  `uni` -> `college`, `washing` -> `laundry`, `nan` -> `grandma`. UK spellings
  and UK household words that the marker list never had, found by reading.

## New worklist items

The cross-scan against pass 49 found three more: `premium bonds` (`001428`),
`snooker` (`001563`), `rounders` (`001566`). All three are pre-existing, all
three are in pass 49's unlanded chunks. Worklist is now **90**.

`001428` is the fourth mixed row. The pattern: pass 49 swapped pounds for bucks
and left the institution the money was spent on. Every row whose pass 49 fix was
a currency swap needs re-reading for what the money bought.

## Still open

- class B, ~11 rows, no US referent, needs a scene change not a word swap
- the two singletons: angry `000912`, sexy `000611`
- the 21 rows blocked on pass 49 chunks two to five landing
- three new rows from the cross-scan: `1428`, `1563`, `1566` (also blocked)
