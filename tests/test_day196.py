"""Guard the approved aggregate ledger exception and independent vehicle pools."""
import copy
import json
from pathlib import Path
import unittest

from scripts.economy import financial_report
from scripts.finance_v3 import validate_finance_v3
from scripts.gm_dashboard import build_dashboard
from scripts.validate import validate_state

ROOT = Path(__file__).resolve().parents[1]


class Day196Tests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads((ROOT / 'state/checkpoint.json').read_text())
        self.ledger = json.loads((ROOT / 'state/finance-ledger.json').read_text())

    def test_closing_cash_and_separate_pools(self):
        result = validate_finance_v3(ROOT, self.state, self.ledger)
        self.assertEqual((result['total_cp'], result['paid_cp']), (52490, 0))
        self.assertEqual(self.ledger['commitments']['uncommitted_cp'], 20790)
        report = financial_report(ROOT)['approved_session_cash']
        self.assertEqual((report['gross_bounty_cp'], report['outflows_cp'], report['net_cash_effect_cp']),
                         (8000, 30100, -22100))
        resources = build_dashboard(ROOT)['sections']['theron']
        self.assertEqual((resources['staff_mp']['value'], resources['wagon_mp']['value']), (156, 60))
        self.assertEqual(resources['refitted_wagon_mana']['value'],
                         {'vanguard-wagon': {'current': 120, 'max': 120},
                          'ashvale-wagon': {'current': 80, 'max': 80}})

    def test_no_duplicate_payment_or_invented_account(self):
        for case in ('duplicate', 'handover', 'account', 'historical-contract'):
            with self.subTest(case=case):
                ledger = copy.deepcopy(self.ledger)
                transactions = ledger['transactions']
                if case == 'duplicate':
                    transactions.append(copy.deepcopy(transactions[0]))
                elif case == 'handover':
                    receipt = copy.deepcopy(transactions[2])
                    receipt.update(id='handover', source_event_id='handover', amount_cp=4400,
                                   cash_effect_cp=4400, revenue_recognized_cp=4400)
                    transactions.append(receipt)
                elif case == 'account':
                    transactions[0]['account_id'] = 'blackscale'
                else:
                    transactions[2]['contract_id'] = 'B-83'
                with self.assertRaises(ValueError):
                    validate_finance_v3(ROOT, self.state, ledger)

    def test_refitted_wagon_charge_cannot_use_another_pool(self):
        self.state['resources']['refitted_wagon_mana']['ashvale-wagon']['current'] = 120
        with self.assertRaisesRegex(ValueError, 'independent reservoir'):
            validate_state(self.state)
