"""Pick the review set (the items the project owner reviews and freezes) from the test split.

Rules (agreed 2026-11-21, owner plus reviewer session):
- Public items only; the copyrighted fallback is excluded.
- Photos: for each core type, fill to TARGET items from the test split, ranked by
  licence tier (committable yes, then other licensed, then Pexels), then residential first,
  then seeded random. An item counts toward every core type in its label.
- If a type is still short, move whole dev groups (group_id) into test, in seeded random order,
  until the type reaches its target. Moved groups are recorded in review_set.json and in the manifest.
- Negatives: every test photo in category no-problem or look-alike.
- Videos: every test video that has a downloaded file.
- No filtering on label_confidence or residential; the owner drops items with a reason during review.
- Mould photos get a size bin question.

Usage: python3 -I select_review.py   (writes review/review_set.json and updates split in manifest.jsonl)
"""

import collections
import json
import os
import random

SEED = 20261121
HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, 'manifest.jsonl')
OUT = os.path.join(HERE, 'review', 'review_set.json')
CORE = ['leak', 'mold', 'peeling-paint', 'wall-ceiling-damage', 'pests',
        'smoke-co-detector', 'window', 'heat-hot-water']
TARGET = {t: 10 for t in CORE}
TARGET['heat-hot-water'] = 6
TARGET['mold'] = 30  # the owner's main metric (mould size bin)


def is_fallback(r):
    return r['id'].startswith('med-f') or r.get('fallback')


def tier(r):
    if r['committable'] == 'yes':
        return 0
    return 2 if 'pexels' in r['license'].lower() else 1


def residential(r):
    return 0 if str(r.get('residential', '')).lower().startswith('yes') else 1


def core_types(r):
    return [t for t in r.get('draft_label') or [] if t in CORE] if r['category'] == 'problem' else []


def main():
    rows = [json.loads(l) for l in open(MANIFEST) if l.strip()]
    rng = random.Random(SEED)
    pub = [r for r in rows if not is_fallback(r)]
    for r in pub:
        r['_rand'] = rng.random()
    rank = lambda r: (tier(r), residential(r), r['_rand'])

    photos = lambda split: [r for r in pub if r['media_type'] == 'image' and r['split'] == split]
    picked = {}
    count = collections.Counter()

    def take(r, why):
        if r['id'] in picked:
            return
        picked[r['id']] = why
        for t in core_types(r):
            count[t] += 1

    for t in CORE:
        for r in sorted((r for r in photos('test') if t in core_types(r)), key=rank):
            if count[t] >= TARGET[t]:
                break
            take(r, 'core:' + t)

    moved = []
    dev_groups = sorted({r['group_id'] for r in photos('dev')})
    rng.shuffle(dev_groups)
    for t in CORE:
        for g in dev_groups:
            if count[t] >= TARGET[t]:
                break
            members = [r for r in pub if r['group_id'] == g]
            if not any(t in core_types(r) for r in members if r['media_type'] == 'image'):
                continue
            for r in members:
                r['split'] = 'test'
            moved.append(g)
            for r in sorted((r for r in members if r['media_type'] == 'image' and t in core_types(r)), key=rank):
                if count[t] >= TARGET[t]:
                    break
                take(r, 'core:%s (moved group %s)' % (t, g))

    negatives = [r for r in photos('test') if r['category'] in ('no-problem', 'look-alike')]
    videos = [r for r in pub if r['media_type'] == 'video' and r['split'] == 'test'
              and r.get('raw_file') and os.path.exists(os.path.join(HERE, r['raw_file']))]

    by_id = {r['id']: r for r in pub}
    core_items = [by_id[i] for i in picked]
    rng.shuffle(core_items)
    rng.shuffle(negatives)
    rng.shuffle(videos)

    def entry(r, section):
        return {
            'id': r['id'], 'section': section, 'media_type': r['media_type'],
            'file': r.get('raw_file') or r.get('text_file'), 'sha256': r.get('sha256'),
            'category': r['category'], 'draft_label': r.get('draft_label'),
            'draft_facts': r.get('draft_facts'), 'problem_locations': r.get('problem_locations'),
            'source_caption': r.get('source_caption'), 'source_url': r.get('source_url'),
            'license': r['license'], 'committable': r['committable'],
            'residential': r.get('residential'), 'label_confidence': r.get('label_confidence'),
            'duration_s': r.get('duration_s'), 'group_id': r['group_id'],
            'needs_mold_bin': 'mold' in (r.get('draft_label') or []),
            'picked_because': picked.get(r['id'], section),
        }

    items = ([entry(r, 'core-photos') for r in core_items]
             + [entry(r, 'negatives') for r in negatives if r['id'] not in picked]
             + [entry(r, 'videos') for r in videos])

    for r in rows:
        r.pop('_rand', None)
    tmp = MANIFEST + '.tmp'
    with open(tmp, 'w') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    os.replace(tmp, MANIFEST)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump({'seed': SEED, 'targets': TARGET, 'moved_dev_groups': moved,
                   'counts_by_core_type': dict(count), 'items': items}, f, indent=1, ensure_ascii=False)

    sec = collections.Counter(i['section'] for i in items)
    print('review items', len(items), dict(sec))
    print('core type counts', {t: count[t] for t in CORE})
    print('moved dev groups', moved)
    print('mould items needing a bin', sum(i['needs_mold_bin'] for i in items))


if __name__ == '__main__':
    main()
