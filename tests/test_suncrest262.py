"""Protect the adopted cash endpoint and its separate DSI receipts."""
import copy
import json
from pathlib import Path
import unittest

from scripts.economy import financial_report
from scripts.finance_endpoint import validate_endpoint
from scripts.gm_dashboard import build_dashboard

ROOT = Path(__file__).resolve().parents[1]


class Suncrest262Tests(unittest.TestCase):
    def test_read_only_views_keep_commitments_unknown(self):
        report = financial_report(ROOT)
        cash = report['cash_position']
        self.assertEqual(cash['controlled']['amount_cp'], 299040)
        self.assertEqual([account['balance']['amount_cp'] for account in cash['accounts']], [10000])
        self.assertIsNone(cash['committed_unpaid']['amount_cp'])
        self.assertIsNone(cash['uncommitted']['amount_cp'])
        finances = build_dashboard(ROOT)['sections']['finances']
        self.assertEqual(finances['unexplained_endpoint_difference_cp']['value'], 246550)
        self.assertIsNone(finances['uncommitted_display']['value'])

    def test_gap_and_included_lodge_profit_cannot_be_posted(self):
        state = json.loads((ROOT/'state/checkpoint.json').read_text())
        ledger = json.loads((ROOT/'state/finance-ledger.json').read_text())
        validate_endpoint(ROOT, state, ledger)
        for amount in (246550, 4900, 2400):
            with self.subTest(amount=amount):
                changed = copy.deepcopy(ledger)
                changed['transactions'].append({'cash_effect_cp': amount})
                with self.assertRaisesRegex(ValueError, 'do not post'):
                    validate_endpoint(ROOT, state, changed)
