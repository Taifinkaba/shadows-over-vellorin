"""Explicit historical fixture selection; never rewrite actual campaign authorities."""
import json
import re

import yaml
from pathlib import Path


def restore_day156(root):
    (root/'state/checkpoint.json').write_bytes((root/'archive/checkpoints/year848-day156-2015.json').read_bytes())
    (root/'state/finance-ledger.json').write_bytes((root/'archive/checkpoints/year848-day156-finance-ledger.json').read_bytes())
    for path,content in json.loads((root/'archive/checkpoints/year848-day156-entity-records.json').read_text()).items():
        (root/path).write_text(content)


def restore_unresolved_day181(root):
    snapshot=json.loads((root/'archive/checkpoints/year848-day181-unresolved-adoption.json').read_text())
    for path,key in [('state/checkpoint.json','checkpoint'),('state/finance-ledger.json','ledger')]:
        (root/path).write_text(json.dumps(snapshot[key]))
    for path,content in snapshot['entity_records'].items():(root/path).write_text(content)
    (root/'entities/locations/briarstone-cottage.md').write_text(snapshot['cottage_record'])


DAY196_MANIFEST = Path(__file__).with_name('fixtures') / 'day196-authority-revisions.json'
DAY196_REVISED_AUTHORITIES = json.loads(DAY196_MANIFEST.read_text())['revisions']


SUNCREST262_MANIFEST = DAY196_MANIFEST.with_name('suncrest262-authority-revisions.json')
SUNCREST262_REVISED_AUTHORITIES = json.loads(SUNCREST262_MANIFEST.read_text())['revisions']


def restore_day196(root):
    for name in ('checkpoint', 'finance-ledger'):
        suffix = '' if name == 'checkpoint' else '-finance-ledger'
        (root/f'state/{name}.json').write_bytes(
            (root/f'archive/checkpoints/year848-day196{suffix}.json').read_bytes())

    restore_checkpoint_owner_values(root)


def restore_checkpoint_owner_values(root):
    checkpoint = json.loads((root/'state/checkpoint.json').read_text())
    for relative in ('characters/theron-ashvale.md', 'mechanics/party-finances.md'):
        path = root/'entities'/relative
        text = path.read_text()
        block = re.search(r'(?m)^checkpoint_values:\n(?:  .*\n)+', text)[0]
        values = yaml.safe_load(block)['checkpoint_values']
        for key in values:
            section, _, field = key.partition('.')
            values[key] = checkpoint[section][field] if field else checkpoint[section]
        path.write_text(text.replace(block, yaml.safe_dump({'checkpoint_values': values}, sort_keys=False)))


def restore_reconciled_day181(root, fixture):
    """Restore the historical endpoint and its approved reconciliation delta."""
    restore_unresolved_day181(root)
    delta = json.loads(fixture.read_text())
    path = root / 'state/checkpoint.json'
    checkpoint = json.loads(path.read_text())
    fields = delta['checkpoint']
    checkpoint['context']['projects']['briarstone_repairs'] = fields.pop('briarstone_repairs')
    checkpoint['provenance']['mp_bridge'] = fields.pop('mp_bridge')
    checkpoint.update(fields)
    path.write_text(json.dumps(checkpoint))
    path = root / 'state/finance-ledger.json'
    ledger = json.loads(path.read_text())
    ledger.update(delta['ledger'])
    path.write_text(json.dumps(ledger))

CHARACTER_SHEET_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('character-sheet-authority-revisions.json').read_text()
)['revisions']


YEAR851_MANIFEST = DAY196_MANIFEST.with_name('year851-day160-authority-revisions.json')
YEAR851_REVISED_AUTHORITIES = json.loads(YEAR851_MANIFEST.read_text())['revisions']


YEAR852_MANIFEST = DAY196_MANIFEST.with_name('year852-day1-authority-revisions.json')
YEAR852_REVISED_AUTHORITIES = json.loads(YEAR852_MANIFEST.read_text())['revisions']


DRAGON_REFERENCE_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('dragon-humanoid-reference-revisions.json').read_text()
)['revisions']


TWIN_SWORD_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('twin-sword-authority-revisions.json').read_text()
)['revisions']


YEAR852_CLOSE_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('year852-day365-authority-revisions.json').read_text()
)['revisions']

YEAR853_HOLLOW_VEIL_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('year853-authority-revisions.json').read_text()
)['revisions']

WESTBRIDGE_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('year853-day52-authority-revisions.json').read_text()
)['revisions']

DAY52_CLEANUP_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('year853-day52-cleanup-revisions.json').read_text()
)['revisions']

HISTORICAL_LINK_REVISIONS = json.loads(
    DAY196_MANIFEST.with_name('historical-reference-links-revisions.json').read_text()
)['revisions']

# Current-owner lookups use the latest digest; preservation checks walk both windows.
YEAR853_REVISIONS = YEAR853_HOLLOW_VEIL_REVISIONS | WESTBRIDGE_REVISIONS | DAY52_CLEANUP_REVISIONS | HISTORICAL_LINK_REVISIONS
