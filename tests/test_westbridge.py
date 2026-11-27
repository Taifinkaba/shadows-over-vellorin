"""Regression checks for the approved Westbridge state and separate treasuries."""

from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch

from scripts import session_westbridge
from scripts.validate import ValidationError, read_json, validate_state

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'archive/checkpoints'


class WestbridgeTests(unittest.TestCase):
    def setUp(self):
        self.state = read_json(ARCHIVE / 'year853-day52.json')
        self.ledger = read_json(ARCHIVE / 'year853-day52-finance-ledger.json')
        self.academy = read_json(ARCHIVE / 'year853-day52-dsi-finance-ledger.json')
        self.registries = read_json(ARCHIVE / 'year853-day52-dsi-registries.json')

    def test_checkpoint_rejects_resume_or_uncertified_recovery(self):
        for mutation in (
            lambda state: state.update(status='ENDED'),
            lambda state: state['calendar'].update(annual_day=366),
            lambda state: state['resources'].update(wagon_mp=60),
            lambda state: state['provenance']['mp_bridge']['recovery_events'][0].update(scope='staff'),
        ):
            state = deepcopy(self.state)
            mutation(state)
            with self.subTest(state=state), self.assertRaises(ValidationError):
                validate_state(state)
                session_westbridge.validate_checkpoint(ROOT, state)

    def test_controlled_ledger_rejects_duplicate_posting_or_academy_cash(self):
        for mutation in (
            lambda ledger: ledger['transactions'].append(ledger['transactions'][-1]),
            lambda ledger: ledger['controlled_cash'].update(total_cp=27571800 + 122500),
        ):
            ledger = deepcopy(self.ledger)
            mutation(ledger)
            with self.assertRaises(ValidationError):
                session_westbridge.validate_finances(ROOT, self.state, ledger, academy=self.academy, registries=self.registries)

    def test_academy_ledger_rejects_retroactive_tithe_and_misdirected_shares(self):
        for mutation in (
            lambda ledger: ledger['year853'].update(historical_tithe_percent=25),
            lambda ledger: ledger['westbridge_reconciliation']['student_distributions']['gorren'].update(new_cp=750),
        ):
            academy_path = ROOT / 'state/dsi-finance-ledger.json'
            academy = deepcopy(self.academy)
            mutation(academy)
            with patch.object(session_westbridge, 'read_json',
                              side_effect=lambda path: academy if path == academy_path else read_json(path)):
                with self.assertRaises(ValidationError):
                    session_westbridge.validate_finances(ROOT, self.state, self.ledger, registries=self.registries)
