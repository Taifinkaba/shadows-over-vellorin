"""Explicit historical fixture selection; never rewrite actual campaign authorities."""
import json
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
