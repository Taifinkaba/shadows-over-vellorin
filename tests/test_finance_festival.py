"""Protect the adopted festival receipts and paid estate projects."""
import copy
from pathlib import Path
import unittest

from scripts.economy import financial_report
from scripts.validate import read_json, ValidationError
from scripts.finance_festival import validate_festival, validate_year_end

ROOT = Path(__file__).resolve().parents[1]


class FestivalFinanceTests(unittest.TestCase):
    def test_report_projects_actual_cash_and_receipts(self):
        report = financial_report(ROOT)
        self.assertEqual(report['cash_position']['controlled']['amount_cp'], 714500)
        self.assertIn('provisional', report['cash_position']['controlled']['status'])
        self.assertEqual(report['income_statement']['actual_received_revenue']['amount_cp'], 1440800)
        self.assertEqual(report['income_statement']['actual_paid_expenses']['amount_cp'], 937600)
        self.assertEqual([row['outstanding_cp'] for row in report['five_part_completed_projects']], [0, 0, 0])

    def test_duplicate_and_missing_postings_fail(self):
        state = read_json(ROOT / 'archive/checkpoints/year851-day160.json')
        ledger = read_json(ROOT / 'archive/checkpoints/year851-day160-finance-ledger.json')
        for update in (lambda rows: rows.append(rows[0]), lambda rows: rows.pop()):
            changed = copy.deepcopy(ledger)
            update(changed['transactions'])
            with self.assertRaisesRegex(ValidationError, 'duplicate posting|missing posting'):
                validate_festival(ROOT, state, changed)


    def test_year_end_provisional_close_and_paid_rows(self):
        state = read_json(ROOT / 'state/checkpoint.json')
        ledger = read_json(ROOT / 'state/finance-ledger.json')
        validate_year_end(ROOT, state, ledger)
        self.assertEqual(ledger['bridge']['difference_cp'], -2000)
        self.assertEqual(ledger['controlled_cash']['accounts'], [])
        for key, update, reason in (
            ('transactions', lambda rows: rows.append(rows[-1]), 'duplicate posting'),
            ('bridge', lambda row: row.update(is_transaction=True), 'unposted'),
            ('endpoint', lambda row: row.update(classification='AUDITED'), 'provisional'),
        ):
            changed = copy.deepcopy(ledger)
            update(changed[key])
            with self.subTest(key=key), self.assertRaisesRegex(ValidationError, reason):
                validate_year_end(ROOT, state, changed)
