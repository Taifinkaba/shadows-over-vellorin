"""Protect the adopted festival receipts and paid estate projects."""
import copy
from pathlib import Path
import unittest

from scripts.economy import financial_report
from scripts.validate import read_json, ValidationError
from scripts.finance_festival import validate_festival

ROOT = Path(__file__).resolve().parents[1]


class FestivalFinanceTests(unittest.TestCase):
    def test_report_projects_actual_cash_and_receipts(self):
        report = financial_report(ROOT)
        self.assertEqual(report['cash_position']['controlled']['amount_cp'], 107300)
        self.assertEqual(report['income_statement']['actual_received_revenue']['amount_cp'], 452000)
        self.assertEqual(report['income_statement']['actual_paid_expenses']['amount_cp'], 558000)
        self.assertEqual([row['outstanding_cp'] for row in report['five_part_completed_projects']], [0, 0, 0])

    def test_duplicate_and_missing_postings_fail(self):
        state = read_json(ROOT / 'state/checkpoint.json')
        ledger = read_json(ROOT / 'state/finance-ledger.json')
        for update in (lambda rows: rows.append(rows[0]), lambda rows: rows.pop()):
            changed = copy.deepcopy(ledger)
            update(changed['transactions'])
            with self.assertRaisesRegex(ValidationError, 'duplicate posting|missing posting'):
                validate_festival(ROOT, state, changed)
