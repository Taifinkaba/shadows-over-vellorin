"""Year 853 replay guards for the checkpoint, treasury and academy."""
from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch

from scripts import finance_year853
from scripts.validate import ValidationError, read_json, validate, validate_state

ROOT = Path(__file__).resolve().parents[1]


class Year853Tests(unittest.TestCase):
    def setUp(self):
        self.state = read_json(ROOT / 'state/checkpoint.json')
        self.ledger = read_json(ROOT / 'state/finance-ledger.json')
        self.academy = read_json(ROOT / 'state/dsi-finance-ledger.json')

    def test_full_validation(self):
        self.assertIn('checkpoint valid', validate(ROOT))

    def test_calendar_and_closing_observations(self):
        for change in (
            lambda s: s['calendar'].update(latest_numbered_day=366),
            lambda s: s['calendar'].update(annual_day=28),
            lambda s: s['theron'].update(mp=410),
            lambda s: s['resources'].update(staff_mp=180),
            lambda s: s['resources'].update(dragon_slayer_locked=False),
        ):
            state = deepcopy(self.state)
            change(state)
            with self.assertRaises(ValidationError):
                validate_state(state)

    def test_bridge_rejects_duplicate_receipt_or_companion_share(self):
        receipt = next(row for row in self.ledger['transactions'] if row.get('advance'))
        for row, message in (
            (receipt, 'duplicate posting'),
            ({**receipt, 'id': 'companion-share', 'category': 'distribution'}, 'companion distribution'),
        ):
            ledger = deepcopy(self.ledger)
            ledger['transactions'].append(row)
            with self.assertRaisesRegex(ValidationError, message):
                finance_year853.validate_year853(ROOT, self.state, ledger)
        self.state['theron']['level'] += 1
        with self.assertRaisesRegex(ValidationError, 'unsupported advancement'):
            finance_year853.validate_year853(ROOT, self.state, self.ledger)

    def test_academy_tithe_shares_and_allocations(self):
        transfer = self.ledger['transactions'][-1]
        for change, message in (
            (lambda d: d.update(prospective_tithe_percent=10), 'prospective tithe'),
            (lambda d: d['year853'].update(historical_tithe_percent=25), 'historical tithe'),
            (lambda d: d['year853']['student_distributions']['gorren'].update(earned_cp=12250),
             'incorrect individual distribution'),
            (lambda d: d['year853'].update(development_disbursements_cp=120000), 'unspent allocations'),
            (lambda d: d.update(treasury_total_cp=122000), 'historical ledger'),
        ):
            ledger = deepcopy(self.academy)
            change(ledger)
            with self.subTest(message=message), patch.object(
                finance_year853, 'read_json',
                side_effect=lambda p: ledger if p.name == 'dsi-finance-ledger.json' else read_json(p),
            ), self.assertRaisesRegex(ValidationError, message):
                finance_year853.validate_academy(ROOT, self.state, transfer)

    def test_standing_boundaries_have_canonical_routes(self):
        for path, required in (
            ('entities/factions/dragon-slayer-academy.md', ('Greyhaven Valley', 'separate from the commercial estate')),
            ('entities/mechanics/way-of-the-dragon.md', ('voluntarily offered', 'independently and voluntarily',
                                                         'Theron\'s own Dragon Slayer ability remains locked')),
            ('entities/locations/route-eastrun-greyhaven-valley.md', ('"classification": "PROPOSED"',)),
            ('entities/locations/hollow-veil.md', ('exact historical temple identity was not verified',)),
            ('entities/quests/twin-sword-origin.md', ('full statement is not obtained', 'Seek lawful access')),
        ):
            text = (ROOT / path).read_text()
            for evidence in required:
                with self.subTest(path=path, evidence=evidence):
                    self.assertIn(evidence, text)
