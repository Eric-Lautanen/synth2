# pass 50 -- class A demonstration, 11 rows

Not a chunk of the pass. A worked sample, so the method in `pass50_mapping.md`
can be judged on eleven real rows before 86 of them get written.

**File:** `audit/changes_pass50_demo_classA.json`
**Apply:** `python scripts/apply_rewrites.py audit/changes_pass50_demo_classA.json --dry`

**All eleven rows are outside pass 49's row set.** That is deliberate: pass 49 has
not landed yet, and any row it touched would have to be authored against text
that does not exist in `raw/` yet. These eleven can be applied today, in any
order, whatever happens to pass 49.

## What the eleven cover

| term | rows | what changed |
|---|---|---|
| mot | 5 | `mot` -> `inspection`, both sides |
| trolley | 3 | `trolley` -> `cart`; `food shop` -> `grocery run`; `big shop` -> `grocery run` |
| optician | 3 | `optician` -> `eye doctor`, both sides |

Result: all eleven rows now read clean on those terms, checked by scanning the
applied copy rather than by eye.

## The rule this sample exists to test

Pass 50 edits user turns, so the assistant echo has to be re-derived, not
assumed. Row 533 is the pattern:

    before  u: the car failed its mot.
            a: oh no, what did the car fail its mot on, big or small?
    after   u: the car failed its inspection.
            a: oh no, what did it fail the inspection on, big or small?

The assistant turn had to be rewritten even though its only defect was the word
it was echoing, because the token it echoed changed underneath it.

Row 811 is the other case: only the user turn changes, because the assistant turn
never named the optician.

    u2: slightly worse, which the eye doctor blamed on screens and i blame on being forty.
    a1: slightly worse, blamed on screens or on being forty, fair enough.   (unchanged)

## What the gate caught in my own work

`st2_casual_001579`, first attempt:

    u0: did the big grocery run this morning.
    a0: big grocery run this morning then, was it busy in there?

That is a parrot, and the 6-gram parrot rule cannot see it, because the shared run
is exactly five words -- `big grocery run this morning`. Only the 5-gram gate
caught it. Rewritten to `the grocery run done, was it busy in there this morning?`

This is the case for keeping the 5-gram check even though the parrot class is
formally defined at 6. A relocation pass walks straight into it, because the
natural way to answer a relocated user turn is to say the relocated phrase back.

## A structural defect found, not fixed

`st2_casual_001291` has a duplicated user turn. Turns 2 and 4 are the same
sentence:

    2 u: eleven bags between twelve of us, plus a shopping trolley and one mysterious boot.
    4 u: eleven bags between twelve of us, plus a shopping cart and one mysterious boot.

Someone already swapped `trolley` -> `cart` in the second copy and left the first
alone, and the assistant reply that follows the duplicate (`haha a cart and a
boot, the classic haul`) then answers a question the user has now asked twice.
`apply_rewrites` only swaps text, so this cannot be repaired by a change file --
the row needs a turn removed. Flagging rather than papering over it. That row is
the only one of the 86 I would not try to fix inside pass 50.

## What is blocked

21 of the 86 rows are in pass 49's set: 000450 000802 000965 001031 001201 001255
001428 001489 001495 001527 001541 001563 001566 001584 001617 001744 001868
001874 001941 001961 001965. They wait for pass 49 to land.

That leaves 65 rows available now, and this sample is 11 of them.
