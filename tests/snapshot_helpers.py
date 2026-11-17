"""Explicit historical fixture selection; never rewrite actual campaign authorities."""
import json


def restore_day156(root):
    (root/'state/checkpoint.json').write_bytes((root/'archive/checkpoints/year848-day156-2015.json').read_bytes())
    (root/'state/finance-ledger.json').write_bytes((root/'archive/checkpoints/year848-day156-finance-ledger.json').read_bytes())
    for path,content in json.loads((root/'archive/checkpoints/year848-day156-entity-records.json').read_text()).items():
        (root/path).write_text(content)
