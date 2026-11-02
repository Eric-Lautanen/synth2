# pass 49 re-cut of chunks three, four and five under the four new gate rules

Prompted by msg 218. The gate now encodes four rules it did not have, and
re-running chunks three to five against them found **eight hits**, none of which
any earlier pass could see. Chunk two needed nothing.

## The four rules, and the fourth is the interesting one

1. **Full banned list.** This checker had `rough classic at all british flu jab`.
   The verify pattern also carries `robbery theft scam bait nightmare stings
   brutal timing bold dirty sneaky underhanded`. Adopted whole, word-boundary
   matched, with `at all` kept as a phrase.
2. **Sentence-initial is-frame.** Any edited reply opening `is|are|was|were`.
3. **Watchlist.** `were you able to`, `have you tried`, `did you get`, `is just`,
   `a real`.
4. **The DUP gap.** `corpus_index()` kept a single `(lane, line)` per 5-gram via
   `setdefault`, so a row that was the FIRST place a phrase appeared could never
   collide with the second occurrence. That is exactly how 1239 read clean while
   the verify pattern caught `two hundred pages in` against a landed 5-gram. The
   index now stores a **set of every location** and the check compares against
   all of them, excluding only this lane and this line.

The fourth one is the one worth keeping: it was not a missing rule, it was a
wrong instrument reporting success. A gate that cannot fail is not a gate.

## The eight hits

| row | rule | old | new |
|---|---|---|---|
| 1521 a0 | watchlist | `an hour of hold music, did you get through to a person?` | `an hour of hold music, so did anyone pick up?` |
| 1556 a0 | banned `bold` | `a darts league is a bold move, are you any good at it?` | `a darts league, that is a commitment. are you any good at it?` |
| 1582 a0 | watchlist | `a real bargain at the thrift store, did you come away loaded?` | `the thrift store came through then, did you come away loaded?` |
| 1683 a0 | watchlist | `walking in instead of driving is a real change, how long is it?` | `walking in instead of driving, how long does that take you?` |
| 1695 a0 | banned `timing` | `a boiler acting up in the cold is bad timing, no heat?` | `a boiler acting up in the cold is miserable. no heat then?` |
| 1950 a2 | banned `bold` | `taking the ladder away is a bold protest, did it work?` | `he hid the ladder, so did that protest work out?` |
| 1883 a0 | banned `bait` | `a cleaning fee that shows up at the end is bait and switch.` | `a cleaning fee appearing at the end, plainly a con.` |
| 905 a0 | banned `theft` | `a half day gone for ten minutes is theft of your time.` | `a half day gone for ten minutes, and you still paid.` |

`1883` then failed on `at the end is a` against angry:778 -- the same 5-gram that
took two attempts in pass 49 -- so it was restructured to `at the end, plainly a
con` rather than reworded around.

## State after the re-cut

- chunk three: 0 errors, 2 warnings (the `snooker` and `rounders` SCENE items,
  both now fixed by pass 50)
- chunk four: **0 errors, 0 warnings -- unheld**
- chunk five angry: 0 errors, 0 warnings
- chunk five lazy: 0 errors, 0 warnings

## And the four new rules broke nineteen of my own pass 50 lines

Which is the point of adopting them. All nineteen fixed: five is-frames, five
`a real`, three `did you get`, two `bold`, one `brutal`, one `nightmare`, one
`timing`, one 5-gram. Details in the change files themselves.
