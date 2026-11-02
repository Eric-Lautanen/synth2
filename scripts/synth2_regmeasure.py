#!/usr/bin/env python3
"""Measure the register of a synth2 file or a pipe-format draft batch.

Accepts EITHER:
  * a live raw .jsonl (one JSON object per line, turns = [{"role","text"},...])
  * a pipe-format draft .txt (turns joined by ' | ', 2 or 4 segments per line)

Prints: rows, turns/row, tone, itype, buckets, multi share, per-position
first-word histograms, terminal punctuation by (pos, role), duplicate turn
texts, and non-ascii / hyphen / capital-start counts.

Use it BEFORE composing (on the live file, to get the target) and AFTER every
edit pass (on the draft, to see what moved). This is the instrument the
campaign's "read the register first" rule depends on.

Usage:
  python synth2_regmeasure.py <live.jsonl>
  python synth2_regmeasure.py <draft.txt> --pipe
"""
import io
import re
import sys
import json
import collections


def load(path, pipe):
    if pipe:
        lines = [l.rstrip('\n').rstrip('\r') for l in io.open(path, encoding='utf-8') if l.strip()]
        return [[s.strip() for s in l.split(' | ')] for l in lines]
    rows = []
    for ln in io.open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        o = json.loads(ln)
        rows.append([t['text'] for t in o['turns']])
    return rows


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    pipe = '--pipe' in sys.argv or path.endswith('.txt')
    rows = load(path, pipe)
    n = len(rows)
    print('source %s  (%s)' % (path, 'pipe draft' if pipe else 'live jsonl'))
    print('rows %d' % n)
    print('turns/row %s' % dict(sorted(collections.Counter(len(r) for r in rows).items())))

    def wc(t):
        return len(re.findall(r"[A-Za-z0-9']+", t))

    b = collections.Counter()
    multi = 0
    for r in rows:
        mx = max(wc(t) for t in r) if r else 0
        b['short' if mx < 15 else ('medium' if mx < 60 else 'long')] += 1
        if len(r) >= 4:
            multi += 1
    print('buckets %s  (%.1f/%.1f/%.1f)' % (
        dict(b), 100.0 * b['short'] / n, 100.0 * b['medium'] / n, 100.0 * b['long'] / n))
    print('multi %d/%d = %.1f%%' % (multi, n, 100.0 * multi / n))

    for pos in range(4):
        c = collections.Counter()
        tot = 0
        for r in rows:
            if len(r) > pos and r[pos]:
                c[r[pos].split()[0].lower()] += 1
                tot += 1
        if tot:
            print('pos%d n=%d  %s' % (pos, tot, ', '.join(
                '%s %d %.1f%%' % (k, v, 100.0 * v / tot) for k, v in c.most_common(9))))

    print('--- terminal punctuation by (pos, role) ---')
    for pos in range(4):
        role = 'user' if pos % 2 == 0 else 'assistant'
        c = collections.Counter()
        for r in rows:
            if len(r) > pos:
                t = r[pos].strip()
                c['?' if t.endswith('?') else ('end' if t[-1] in '.!' else 'bare')] += 1
        if sum(c.values()):
            print('  pos%d %-9s %s' % (pos, role, dict(c)))

    flat = [t for r in rows for t in r]
    d = {k: v for k, v in collections.Counter(flat).items() if v > 1}
    print('dup turn texts: %d  %s' % (len(d), list(d.items())[:6]))
    print('non-ascii %d, hyphen %d, capital-start %d' % (
        sum(1 for t in flat if any(ord(ch) > 126 for ch in t)),
        sum(1 for t in flat if '-' in t),
        sum(1 for t in flat if t[:1].isupper())))


if __name__ == '__main__':
    main()
