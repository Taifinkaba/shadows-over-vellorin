"""Explicit historical fixture selection; never rewrite actual campaign authorities."""
import json


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
