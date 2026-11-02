# pass 50 class B -- 12 rows, and two pass 49 echo regressions found on the way

`audit/changes_pass50_classB.json`, 12 rows, 29 records, casual.
`rows=12 edited_lines=29 errors=0 warnings=0`.

## The gate changed first

The lead's msg 215 asked for `synth2_changefile_check.py` to adopt the house
echo definition so the two instruments can never disagree again. Done:

    STOP = the verify-pattern list
    content(s) = {w for w in toks(s) if w not in STOP and len(w) > 1}

The old rule was this checker's own shorter STOP list plus a 4-char floor, which
rejected `app` as an echo when the house rule accepts it -- that is L1177.

**Result on the lead's folded chunk one: 1 error + 2 warnings -> 0 errors.** The
three remaining warnings are all adjudicated in msg 215 (L1031 queue is pass 50
scope, L1159 is the legal pass-20 class, and the four ORPHANED lines are covered
below).

The bigger STOP list could have invalidated an echo of mine that leaned on a word
like `still`, `only` or `every`, so all five class A files were re-run under the
house rule. All still 0 errors, 0 warnings.

## Two pass 49 echo regressions, both mine, both now fixed

The ORPHANED detector was upgraded to separate two cases, because they need
different responses: **ECHO BROKEN** (this file broke an echo that used to work)
vs **ORPHANED, pre-existing gap** (the gap predates the edit). Applied to the
lead's chunk one, all four of its orphans came back pre-existing -- chunk one
broke nothing.

Applied to my own chunks three and four, it found two real breaks. In both, the
pass 49 rewrite killed a parrot and took the echo with it:

| row | user turn | pass 49 wrote | why it fails |
|---|---|---|---|
| L1580 | `none at all. they did not even ask why.` | `not even a question at the desk, which is how it goes.` | shares neither `none` nor `ask` |
| L1694 | `i'm trying to cut down on the coffee.` | `cutting down is the hard part, how many cups were you on?` | `cutting` is not `cut`, and `trying` and `coffee` are gone |

Fixed in place in `changes_pass49_chunk3.json` and `chunk4.json`:

- L1580 a1 -> `none, not a single question at the desk, which is rare.`
- L1694 a0 -> `coffee is the hard one to cut. how many cups were you on?`

Both keep the parrot dead and restore the echo. Chunk three now reads 0 errors /
2 warnings (the two known pass 50 SCENE items), chunk four 0 / 0. **Chunk two was
not touched** -- the lead is verifying it in this window.

This is worth a rule: a parrot rewrite that deletes the shared phrase must
re-introduce a content word from the same turn, or it trades one defect for the
other. The echo gate catches it only if the assistant turn is in the file.

## Class B, twelve rows

Class B as mapped was ~11 rows. Most of them had already been absorbed by the
class A sweep -- bonfire night, pancake day, national trust, paddington, two of
three half terms, one of two britain. What was genuinely left did not come from
the map at all; it came from widening the net into UK household, school and
civic vocabulary. Twelve rows, listed in worklist revision 5.

Only `001372` is a true scene change: **cricket has no US referent**, so the row
became town league baseball. That works because baseball shares the shape --
runs, innings, a losing margin in the gloom. The pavilion became the bleachers,
the three teas became three trips to the concession stand, `a perfect english
saturday` became `a perfect small town saturday`.

## The map was wrong about harvest festival

`pass50_mapping.md` lists `harvest festival | 1` as a class B scene to change.
There is no such row. The only `harvest` in the corpus is `001825`, a chilli
plant on a windowsill. The row was asserted by the map and never checked against
the file -- the same failure as the original 29-row undercount, in the opposite
direction.

Four more false positives from the wider net: `a level` in `000742` and `001713`
is a spirit level (`000742` is a pun on "more or less"), `nappy` in `001329` is
the middle of "snappy", and `harvest` in `001825` is chillies.

## Final state

- all six pass 50 files merged with pass 49 chunks two to four: **245 rows, 409
  edited lines, 0 errors**, 3 warnings (all three are the known pass 50 SCENE
  items sitting in pass 49's unlanded rows)
- cross-line 5-gram over **445 edited lines** from both passes and all four
  lanes: **0 hits**
- worklist **102**

## A third pass 49 regression -- angry L1102

Same defect, angry lane, found the moment the house rule reached it:

| row | user turn | pass 49 wrote | why it fails |
|---|---|---|---|
| L1102 | `from c30 to a4, then back to c30 for the same plane.` | `the same gate twice for one flight is a system with no memory.` | shares none of `c30`, `a4`, `back`, `plane` |

The old reply was `a full loop back to c30 for the same plane is absurd`, which
parroted seven words. The replacement killed the parrot and the echo together.
Fixed in place to `the gate moved twice and the plane never did. that is the joke.`

Three of three. Every pass 49 rewrite that removed a parrot by dropping the
shared phrase also dropped the echo, and all three were invisible until the echo
instrument and the house rule were the same instrument. That is the argument for
the lead's ask being right: the disagreement was hiding real defects, not
manufacturing false ones.

## The two singletons

**angry `000912` -- real, fixed.** `a surgery ad` means an ad for the practice,
which is the UK sense of surgery. Now `an ad for the clinic` / `clinic ads on a
loop, in the room where you already wait.` Angry lane: 35 rows with chunk five,
0 errors.

**sexy `000611` -- needs nothing.** `we rode the sightseeing trolley through our
own neighborhood` is ordinary US English; sightseeing trolleys are a US thing.
The hit came from the bare term `trolley`, which the list maps to `cart` for
shopping trolleys only.

Sweeping both lanes turned up seven more candidates and **all seven are false
positives**, which is worth recording because each one is a different way a term
list lies:

| row | hit | why it is not Britain |
|---|---|---|
| angry `001150` | surgery | an operation, which is US usage; only the practice sense is UK |
| sexy `000595`, lazy `000287` | bonfire | a backyard bonfire is US |
| sexy `000221` | nursery | a plant nursery |
| sexy `000789` | british | a character doing an accent; the map already excluded this one |
| lazy `000277` | cricket | the insect |
| lazy `000918` | fete | no occurrence in either turn; matched elsewhere in the JSON line |

So the mapped count of one angry and one sexy was right for angry and wrong for
sexy, in the direction of a row that did not need changing.

## Still open

- 21 rows blocked on pass 49 chunks two to five landing, plus `1428`, `1563`,
  `1566` from the cross-scan
- b4430 -- mine, never started

## Final instrument state

12 files, 282 rows, **447 edited lines**, across pass 49 chunks two to five and
all six pass 50 files, both lanes: **0 errors, 0 cross-line 5-gram hits.**
