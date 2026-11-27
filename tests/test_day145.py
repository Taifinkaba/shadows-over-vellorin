"""Regression coverage for the player-approved Sovereign Legacy endpoint."""
from copy import deepcopy
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from scripts import session_day145
from scripts.validate import ValidationError, read_json, validate, validate_state, UniqueLoader
import yaml

ROOT = Path(__file__).resolve().parents[1]


class Day145Tests(unittest.TestCase):
    def setUp(self):
        self.state = read_json(ROOT / 'state/checkpoint.json')
        self.ledger = read_json(ROOT / 'state/finance-ledger.json')

    def test_endpoint_and_structured_owners_agree(self):
        self.assertIn('checkpoint valid', validate(ROOT))
        self.assertEqual((self.state['date'], self.state['time'], self.state['status']),
                         ('Year 853 Day 145', '20:05', 'PAUSED'))
        self.assertEqual(self.state['money']['total_gp_sp'], '288928gp')

    def test_checkpoint_rejects_invented_advancement_or_resources(self):
        for mutation in (
            lambda s: s.update(time='20:06'),
            lambda s: s.update(status='ENDED'),
            lambda s: s['theron'].update(unspent_attributes=0, str=16),
            lambda s: s['resources'].update(wagon_mp=60),
            lambda s: s['resources'].update(staff_mp=170),
            lambda s: s['resources'].update(dragon_slayer_locked=False),
            lambda s: s['provenance'].update(conditional_defense=49),
        ):
            state = deepcopy(self.state)
            mutation(state)
            with self.assertRaises(ValidationError):
                validate_state(state)
                session_day145.validate_checkpoint(ROOT, state)

    def test_duplicate_postings_and_salary_payment_are_rejected(self):
        for mutation in (
            lambda ledger: ledger['transactions'].append(ledger['transactions'][-1]),
            lambda ledger: ledger['commitments']['research_salary_review'].update(paid=True),
        ):
            ledger = deepcopy(self.ledger)
            mutation(ledger)
            with self.assertRaises(ValidationError):
                session_day145.validate_finances(ROOT, self.state, ledger)

    def test_academy_balances_and_eligibility(self):
        path = ROOT / 'state/dsi-finance-ledger.json'
        ledger = read_json(path)
        reconciliation = ledger['sovereign_legacy_reconciliation']
        self.assertEqual(sum(reconciliation['individual_balances_cp'].values()), 223050)
        self.assertEqual(reconciliation['settlements'][-1]['closing_cp'], 154750)
        reconciliation['individual_balances_cp']['mira-thorne'] = 100
        previous = read_json(ROOT / (session_day145.PRIOR + '-dsi-finance-ledger.json'))
        with patch.object(session_day145, 'read_json', side_effect=lambda p: ledger if p == path else read_json(p)):
            with self.assertRaisesRegex(ValidationError, 'individual totals or recipients'):
                session_day145.validate_academy(ROOT, self.state, previous)

    def test_identity_and_distinct_witness_evidence(self):
        index = read_json(ROOT / 'index.json')['entries']
        self.assertEqual([row['id'] for row in index if 'blackscale' in row['title'].lower()
                          and row['type'] in {'characters', 'factions'}], ['theron-ashvale'])
        note = (ROOT / 'entities/mechanics/seven-bells-inventory.md').read_text().split('## Year 853 Day 145')[1]
        for phrase in ('E-R-7 command fitting remains installed', 'recognition inscription is a separate record',
                       'VII/R is the distinct removed fitting', 'Return Custodian Seven remains independent'):
            self.assertIn(phrase, note)
        self.assertIn('return-custodian-seven', {row['id'] for row in index})
        self.assertEqual(set(self.state['resources']['refitted_wagon_mana']), {'vanguard-wagon','ashvale-wagon'})
        self.assertEqual(self.state['resources']['wagon_mp_max'], 60)

    def test_mira_and_six_dragon_slayer_placements(self):
        text = (ROOT / 'entities/characters/mira-thorne.md').read_text()
        match = re.search(r'## Character sheet\n\n```yaml\n(.*?)\n```', text, re.S)
        mira = yaml.load(match[1], Loader=UniqueLoader)['character_sheet']
        for key in ('rank','level','hp','hp_max','mp','mp_max','defense'):
            self.assertIsNone(mira[key])
        self.assertNotIn('dragon_slayer', mira)
        self.assertNotIn('unassessed_stat_proposal', mira['character_design_profile'])
        text = (ROOT / 'entities/mechanics/way-of-the-dragon.md').read_text()
        registry = json.loads(re.search(r'```dragon-slayer-registry\n(.*?)\n```', text, re.S)[1])
        self.assertEqual(len(registry), 6)
        self.assertTrue(all(row['rank'] == 'F' and 1 <= row['level'] <= 5 for row in registry.values()))
        session_day145.validate_registries(ROOT)
