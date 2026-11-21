"""Assign dev/test splits to data/media/manifest.jsonl by group_id.

Rules (data/README.md, "Dev/test split"):
- split by source group (group_id), never by item: every item in a group gets the same split
- random assignment with a fixed seed; about 30% of groups go to `test`
- each core problem type has at least 3 `test` items, and no-problem and look-alike items appear in both splits
- public items and fallback items are split independently (fallback items are scored separately)

Method: shuffle the groups with random.Random(SEED); put the first ceil(30%) of groups in test; if the
constraints fail, reshuffle with the same RNG and try again (up to MAX_TRIES). Nothing is chosen by hand.
The attempt that was accepted is printed so the run can be reproduced.

Usage: python3 -I split.py            (rewrites manifest.jsonl in place, prints a summary)
       python3 -I split.py --dry-run
"""
import collections
import json
import math
import os
import random
import sys

SEED = 20261121
TEST_SHARE = 0.30
MAX_TRIES = 5000
CORE = ['leak', 'mold', 'peeling-paint', 'wall-ceiling-damage', 'pests', 'smoke-co-detector', 'window', 'heat-hot-water']
HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, 'manifest.jsonl')


def check(rows, test_groups, require_core):
    test = [r for r in rows if r['group_id'] in test_groups]
    dev = [r for r in rows if r['group_id'] not in test_groups]
    problems = []
    for t in require_core:
        n = sum(1 for r in test if r['category'] == 'problem' and t in r['draft_label'])
        if n < 3:
            problems.append('%s has %d test items' % (t, n))
        if not any(r['category'] == 'problem' and t in r['draft_label'] for r in dev):
            problems.append('%s has no dev items' % t)
    for cat in ('no-problem', 'look-alike'):
        if any(r['category'] == cat for r in rows):
            if not any(r['category'] == cat for r in test):
                problems.append('no %s in test' % cat)
            if not any(r['category'] == cat for r in dev):
                problems.append('no %s in dev' % cat)
    return problems


def assign(rows, rng, label):
    groups = sorted({r['group_id'] for r in rows})
    n_test = math.ceil(len(groups) * TEST_SHARE)
    # only require a core type where the pool can satisfy it (>= 3 groups... checked by trying)
    avail = {t: sum(1 for r in rows if r['category'] == 'problem' and t in r['draft_label']) for t in CORE}
    require_core = [t for t in CORE if avail[t] >= 4]
    last = None
    for attempt in range(1, MAX_TRIES + 1):
        order = groups[:]
        rng.shuffle(order)
        test_groups = set(order[:n_test])
        problems = check(rows, test_groups, require_core)
        if not problems:
            print('%s: accepted shuffle attempt %d (seed %d); %d of %d groups in test' % (
                label, attempt, SEED, n_test, len(groups)))
            return test_groups, require_core
        last = problems
    print('%s: NO shuffle met all constraints after %d attempts; last problems: %s' % (label, MAX_TRIES, last))
    return test_groups, require_core


def main():
    dry = '--dry-run' in sys.argv
    rows = [json.loads(l) for l in open(MANIFEST) if l.strip()]
    rng = random.Random(SEED)
    pools = collections.OrderedDict()
    pools['public'] = [r for r in rows if not r.get('fallback') and not r['id'].startswith('med-f')]
    pools['fallback'] = [r for r in rows if r.get('fallback') or r['id'].startswith('med-f')]
    for label, pool in pools.items():
        if not pool:
            continue
        test_groups, req = assign(pool, rng, label)
        for r in pool:
            r['split'] = 'test' if r['group_id'] in test_groups else 'dev'
        # summary
        c = collections.Counter()
        for r in pool:
            c[(r['split'], 'items')] += 1
            c[(r['split'], r['category'])] += 1
            for t in r['draft_label']:
                if r['category'] == 'problem':
                    c[(r['split'], t)] += 1
        print('  items dev %d test %d' % (c[('dev', 'items')], c[('test', 'items')]))
        for k in ['no-problem', 'look-alike'] + CORE:
            print('  %-20s dev %3d test %3d' % (k, c[('dev', k)], c[('test', k)]))
        both = {r['group_id'] for r in pool if r['split'] == 'dev'} & {r['group_id'] for r in pool if r['split'] == 'test'}
        assert not both, both
    if not dry:
        with open(MANIFEST, 'w') as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        print('wrote', MANIFEST)


if __name__ == '__main__':
    main()
