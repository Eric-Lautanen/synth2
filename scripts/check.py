#!/usr/bin/env python3
"""synth2 batch self-check -- the fast loop before you call preflight.

preflight.py is the authority on whether a batch may be appended. This is the
cheaper loop that runs first, and it exists because of three things preflight
either reports late or does not report at all:

1. CORPUS COLLISIONS BEFORE PREFLIGHT. A row that reuses a turn already in
   raw/ costs a full preflight round trip to find. Checking the corpus is one
   dictionary lookup per turn.
2. NO TRUNCATION IN THE OPENER REPORT. preflight prints the top 5 openers per
   position; a word sitting at 6th can still be over the floor and fail the
   gate. This prints every word used 2+ times and, more importantly, lists the
   FAILING ones in a single summary line per position, so a clean verdict is a
   claim about the whole position rather than about the top 14.
3. STRUCTURE FIRST. Odd turn counts are an instant hard fail in add_rows, and
   writing five-segment rows by accident is the single most common drafting
   error in this campaign. Run this before anything else.

It also hand-feeds the one check no gate performs: repeated 5-grams within the
batch, which is how two rows sharing a premise show up before they ship.

NOT A GATE. preflight is the gate. Nothing here writes to raw/.

Usage:
  python runs/synth2/scripts/check.py /tmp/batch.txt \
      --ref runs/synth2/raw/small_talk_greetings.jsonl
  python runs/synth2/scripts/check.py /tmp/batch.txt <ref.jsonl>

Exit code 0 when clean, 1 otherwise, so it can gate a pipeline.
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))

FUNC = set('the a an and or but if of to in on at for with is are was were be been '
           'it its this that these those i you he she they we my your his her their '
           'not no so as by from have has had do does did will would can could '
           'should may might must there here me him them us'.split())

# Mirrors preflight.AUX_OPEN / WH_OPEN exactly. qmark.py's own AUX set is
# deliberately WIDER (it includes any/anyone/anything); matching preflight here
# is the point, because preflight is what decides whether the batch is legal.
AUX = set('did does do is are was were am can could shall should will would may '
          'might must have has had'.split())
WH = set('what when where who whom whose why how which'.split())
WH_DIRECT_MAX_WORDS = 5

OPENER_FACTOR = 3.0
OPENER_FLOOR = 8.0
MULTI_TARGET = 50.0
MULTI_TOL = 5.0
CHAR_CAP = 4000


def words(t):
    return re.findall(r"[a-z0-9']+", str(t).lower())


def read_rows(path):
    rows = []
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get('id'):
            rows.append(r)
    return rows


def reference_openers(ref_path):
    """Byte-for-byte behaviour of preflight.reference_openers: ASSISTANT turns
    only, batches of the generator shape skipped. Measure the reference the way
    the gate measures it, or a batch you believe is clean will be rejected."""
    rows = read_rows(ref_path)
    by = collections.OrderedDict()
    for r in rows:
        by.setdefault(r.get('batch_no'), []).append(
            [t.get('text', '') for t in r.get('turns', [])])
    kept, skipped = {}, []
    for b, rws in by.items():
        flat = [t for row in [x[1::2] for x in rws] for t in row]
        toks = [w for w in (words(t) for t in flat) if w]
        m = sum(len(t) for t in toks) / max(1, len(toks))
        nf = 100.0 * sum(1 for t in toks if not (set(t) & FUNC)) / max(1, len(toks))
        if m < 6.2 and nf > 40.0:
            skipped.append((b, len(rws), round(m, 2), round(nf, 1)))
            continue
        kept[b] = rws
    pos = {0: collections.Counter(), 1: collections.Counter(),
           2: collections.Counter(), 'last': collections.Counter()}
    denom = collections.Counter()
    for rws in kept.values():
        for r in rws:
            idxs = [(0, r[0]), (1, r[1] if len(r) > 1 else None)]
            if len(r) > 2:
                idxs.append((2, r[2]))
            if r:
                idxs.append(('last', r[-1]))
            for k, t in idxs:
                if t is None:
                    continue
                denom[k] += 1
                w = words(t)
                if w:
                    pos[k][w[0]] += 1
    return pos, denom, skipped, len(kept)


def parse_row(raw):
    p = [x.strip() for x in raw.split('|')]
    return [('user' if i % 2 == 0 else 'assistant', t) for i, t in enumerate(p)]


def load_corpus():
    ref = {}
    for fn in sorted(os.listdir(RAW)):
        if not fn.endswith('.jsonl'):
            continue
        cat = fn[len('small_talk_'):-len('.jsonl')]
        for r in read_rows(os.path.join(RAW, fn)):
            for t in r.get('turns', []):
                ref.setdefault(t.get('text', '').strip().lower(), (cat, r.get('batch_no')))
    return ref


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 1
    batch_path = argv[0]
    if not os.path.exists(batch_path):
        print('batch file not found: %s' % batch_path, file=sys.stderr)
        print('note: on this host /tmp resolves differently depending on whether '
              'the path was written by git bash or by python. Pass an explicit '
              'C:/... path if the file exists and this still fires.',
              file=sys.stderr)
        return 1
    # Accept --ref PATH, -r PATH, or a bare trailing path. Guessing here is not
    # an option: a mistyped flag that silently skips the opener gate turns this
    # tool into a rubber stamp that prints CLEAN.
    refpath = None
    rest = argv[1:]
    i = 0
    while i < len(rest):
        a = rest[i]
        if a in ('--ref', '-r'):
            if i + 1 >= len(rest):
                print('%s needs a path after it' % a, file=sys.stderr)
                return 1
            refpath = rest[i + 1]
            i += 2
        elif a.startswith('--ref='):
            refpath = a.split('=', 1)[1]
            i += 1
        elif a.startswith('-'):
            print('unknown flag %r; see --help' % a, file=sys.stderr)
            return 1
        else:
            refpath = a
            i += 1

    rows = [l.strip() for l in open(batch_path, encoding='utf-8') if l.strip()]
    segs = [parse_row(r) for r in rows]
    raw = open(batch_path, encoding='utf-8').read()
    fails = []
    print('=== %s : %d row(s) ===' % (os.path.basename(batch_path), len(segs)))

    # --- 1. structure, before anything else -------------------------------
    odd = [i + 1 for i, s in enumerate(segs) if len(s) % 2]
    if odd:
        fails.append('odd turn counts on rows %s (add_rows rejects these outright)' % odd)
    print('\n[1] odd turn count rows: %s' % (odd or 'none'))
    print('    turns/row: %s' % dict(collections.Counter(len(s) for s in segs)))
    multi = sum(1 for s in segs if len(s) > 2)
    share = 100.0 * multi / max(1, len(segs))
    if abs(share - MULTI_TARGET) > MULTI_TOL:
        fails.append('multi %.1f%% outside %.0f-%.0f%%' % (share, MULTI_TARGET - MULTI_TOL, MULTI_TARGET + MULTI_TOL))
    print('    multi: %d/%d = %.1f%% (need %.0f-%.0f%%)'
          % (multi, len(segs), share, MULTI_TARGET - MULTI_TOL, MULTI_TARGET + MULTI_TOL))
    bk = collections.Counter()
    for s in segs:
        lg = max(len(t.split()) for _, t in s)
        bk['short' if lg < 15 else ('medium' if lg < 60 else 'long')] += 1
    if bk['long'] == 0:
        fails.append('no long rows -- every file must have them')
    print('    buckets short/medium/long: %d/%d/%d' % (bk['short'], bk['medium'], bk['long']))

    # --- 2. characters ------------------------------------------------------
    hy = sum(1 for s in segs if any('-' in t for _, t in s))
    dash = raw.count('\u2013') + raw.count('\u2014')
    na = sum(1 for c in raw if ord(c) > 127)
    over = [(i + 1, k) for i, s in enumerate(segs) for k, t in enumerate(s) if len(t) > CHAR_CAP]
    for label, n in (('hyphen', hy), ('en/em dash', dash), ('non-ASCII', na)):
        if n:
            fails.append('%d %s' % (n, label))
    if over:
        fails.append('turn(s) over the %d char cap: %s' % (CHAR_CAP, over[:4]))
    print('\n[2] hyphen %d  endash/emdash %d  nonascii %d  over%d %d'
          % (hy, dash, na, CHAR_CAP, len(over)))

    # --- 3. the '?' rule ----------------------------------------------------
    missing, maybe, spurious = [], [], []
    for i, s in enumerate(segs, 1):
        for k, (_, t) in enumerate(s):
            tk = words(t)
            if not tk:
                continue
            ends = t.strip().endswith('?')
            if not ends and (tk[0] in AUX or (tk[0] in WH and len(tk) <= WH_DIRECT_MAX_WORDS)):
                missing.append((i, k, t[:48]))
            elif not ends and tk[0] in WH:
                maybe.append((i, k, t[:48]))
            elif ends and tk[0] not in AUX and tk[0] not in WH:
                spurious.append((i, k, t[:48]))
    if missing:
        fails.append('%d question(s) with no ?: %s' % (len(missing), missing[:6]))
    if maybe:
        print('    READ THESE wh-initial turns with no "?": %s' % maybe[:8])
    print('\n[3] MISSING (fail): %d %s' % (len(missing), missing[:6]))
    print('    ?-but-statement (warn; expected and permanent in greetings): %d' % len(spurious))

    # --- 4. openers, every position, every word used 2+ ---------------------
    if refpath and os.path.exists(refpath):
        pos, denom, skipped, nk = reference_openers(refpath)
        print('\n[4] reference %s: %d clean batches kept%s'
              % (os.path.basename(refpath), nk,
                 '' if not skipped else ', skipped %d generator-shaped' % len(skipped)))
        mine = {0: collections.Counter(), 1: collections.Counter(),
                2: collections.Counter(), 'last': collections.Counter()}
        for s in segs:
            for k, t in ((0, s[0][1]), (1, s[1][1] if len(s) > 1 else None),
                         (2, s[2][1] if len(s) > 2 else None), ('last', s[-1][1])):
                if t:
                    w = words(t)
                    if w:
                        mine[k][w[0]] += 1
        for k in (0, 1, 2, 'last'):
            d = max(1, denom.get(k, 0))
            red = max(1, len(segs) if k != 2 else multi)
            bad = []
            for w, c in mine[k].items():
                sb = 100.0 * c / red
                rf = 100.0 * pos[k][w] / d
                if sb >= OPENER_FLOOR and sb > OPENER_FACTOR * rf:
                    bad.append((sb, w, c, rf))
            print('  pos %-4s (n=%d)  FAILING: %s'
                  % (k, red, ['%s %.1f%% (x%d) vs ref %.1f%%' % (w, sb, c, rf)
                              for sb, w, c, rf in sorted(bad, reverse=True)] or 'none'))
            for sb, w, c, rf in bad:
                fails.append('position %s opener %r at %.1f%% vs ref %.1f%%' % (k, w, sb, rf))
            # EVERY opener this position uses, not just the ones used 2+ times.
            # Patching only the words the FAIL line names is what causes
            # whack-a-mole: fixing one duplicate can promote a word that was
            # previously harmless to just over the floor. To plan a whole
            # position you have to see all of it at once.
            for w, c in sorted(mine[k].items(), key=lambda x: (-x[1], x[0])):
                sb = 100.0 * c / red
                rf = 100.0 * pos[k][w] / d
                print('      %-12s %5.1f%%  ref %5.1f%%  3x=%5.1f%%%s'
                      % (w, sb, rf, OPENER_FACTOR * rf,
                         '   <<< FAIL' if (sb >= OPENER_FLOOR and sb > OPENER_FACTOR * rf) else ''))
    else:
        fails.append('no --ref given, so openers were NOT compared; a clean '
                     'verdict without it is meaningless')
        print('\n[4] no --ref given: openers NOT compared (pass one to check them)')

    # --- 5. repeats ---------------------------------------------------------
    txts = [t.strip().lower() for s in segs for _, t in s]
    dup = [k for k, v in collections.Counter(txts).items() if v > 1]
    if dup:
        fails.append('turn text repeated inside the batch: %s' % dup[:6])
    hits = []
    if os.path.isdir(RAW):
        corpus = load_corpus()
        hits = [(t, corpus[t]) for t in txts if t in corpus]
        if hits:
            fails.append('%d turn(s) already in the corpus: %s' % (len(hits), [h[0] for h in hits[:4]]))
    g5 = collections.Counter()
    for s in segs:
        for _, t in s:
            w = words(t)
            for i in range(len(w) - 4):
                g5[' '.join(w[i:i + 5])] += 1
    rep = [k for k, v in g5.items() if v > 1]
    print('\n[5] in-batch dup: %s' % (dup or 'none'))
    print('    corpus collisions: %d' % len(hits))
    for t, (cat, b) in hits:
        print('      %s b%s: %r' % (cat, b, t))
    print('    repeated 5-grams (two rows sharing a premise): %s' % (rep or 'none'))

    print('\n' + '=' * 66)
    if fails:
        print('NOT CLEAN (%d)' % len(fails))
        for f in fails:
            print('  FAIL %s' % f)
        return 1
    print('CLEAN (0 fail). Warnings above still need a human read.')
    print('Next: preflight.py, then add_rows.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())