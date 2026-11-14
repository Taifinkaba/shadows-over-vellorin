"""Schema4 regression cases for the supplied Seven Bells checkpoint."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate import ValidationError, copper, validate, validate_state

ROOT = Path(__file__).resolve().parents[1]


class NorthReturnHouseTests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads((ROOT / 'state/checkpoint.json').read_text())

    def invalid(self, edit, message):
        state = copy.deepcopy(self.state)
        edit(state)
        with self.assertRaisesRegex(ValidationError, message):
            validate_state(state)

    def test_exact_supplied_snapshot(self):
        s = self.state
        self.assertIn('checkpoint valid', validate(ROOT))
        self.assertEqual((s['schema_version'], s['date'], s['calendar'], s['time'], s['location'], s['status']),
                         (4, 'Year 848 Day 124', {'season': 'Suncrest', 'day_of_season': 4}, '01:45', 'North Return House', 'PAUSED'))
        self.assertEqual((s['theron']['hp'], s['theron']['hp_max'], s['theron']['mp'], s['theron']['mp_max']), (100,100,386,400))
        self.assertEqual((s['theron']['defense'], s['resources']['equipped_defense']), (46,49))
        self.assertEqual((s['resources']['staff_mp'], s['resources']['staff_mp_max'], s['resources']['wagon_mp'], s['resources']['wagon_mp_max']), (156,180,60,60))
        self.assertEqual(copper(s['money']['total_gp_sp']), 54590)
        self.assertEqual(s['money']['provisional_historic_gp_sp'], '9gp 1sp 14cp')
        self.assertEqual(copper(s['money']['office_petty_gp_sp']), 640)
        self.assertEqual(s['custody'], dict(detainees=['perrin','dask','corven-north-return-house'], guard='garrick-vale', free_people=['sella','orenic'], fatalities=0, party_injuries=0))
        self.assertEqual(s['context']['mp_before_recent_casts'],375)
        self.assertEqual(s['context']['recent_mp_costs'],{'Mental Probe':13})
        self.assertEqual(s['context']['recent_mp_recovery']['amount'],24)

    def test_no_free_recovery(self):
        self.invalid(lambda s:s['context']['recent_mp_recovery'].update(ambient_source_usable=False), 'usable ambient source')

    def test_recovery_personal_only(self):
        self.invalid(lambda s:s['context']['recent_mp_recovery'].update(personal_only=False), 'personal-only')

    def test_no_partial_interval(self):
        for minutes in (0,9,11,True):
            with self.subTest(minutes=minutes):
                self.invalid(lambda s:s['context']['recent_mp_recovery'].update(uninterrupted_minutes=minutes), 'integer|incomplete')

    def test_old_or_exaggerated_rate_rejected(self):
        for amount in (12,48,True):
            with self.subTest(amount=amount):
                self.invalid(lambda s:s['context']['recent_mp_recovery'].update(amount=amount), 'integer|incorrect Assimilation')

    def test_cost_cannot_be_omitted(self):
        self.invalid(lambda s:s['context'].update(recent_mp_costs={}), 'expected entries')

    def test_wrong_mp_or_double_deduction_rejected(self):
        self.invalid(lambda s:s['theron'].update(mp=361), 'expenditure/recovery')
        self.invalid(lambda s:s['context']['recent_mp_costs'].update({'Shadow Mantle':16,'Umbral Murmur':9}), 'expenditure/recovery')

    def test_costs_cannot_exceed_available_mana(self):
        self.invalid(lambda s:s['context']['recent_mp_costs'].update({'Mental Probe':376}), 'exceeds starting pool')

    def test_personal_recovery_caps_at_maximum(self):
        s = copy.deepcopy(self.state)
        s['context']['mp_before_recent_casts'] = 400
        s['theron']['mp'] = 400
        validate_state(s)
        self.invalid(lambda s:s['theron'].update(mp=401), 'MP exceeds')

    def test_no_invented_old_account(self):
        self.invalid(lambda s:s['money'].update(blackscale_private_gp_sp='112gp'), 'expected keys')

    def test_no_duplicate_or_detained_free_person(self):
        self.invalid(lambda s:s['custody']['detainees'].append('perrin'), 'duplicate person')
        self.invalid(lambda s:s['custody']['detainees'].append('sella'), 'free people cannot')

    def test_nonnegative_integer_casualties(self):
        self.invalid(lambda s:s['custody'].update(fatalities=True), 'integer')

    def test_segregated_cash_and_entity_agreement(self):
        for field, amount in [('total_gp_sp','552gp 3sp'), ('total_gp_sp','555gp 1sp 4cp'), ('office_petty_gp_sp','0gp'), ('provisional_historic_gp_sp','0gp')]:
            with self.subTest(field=field, amount=amount), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                for name in ('entities','archive','state'):
                    shutil.copytree(ROOT/name,root/name)
                shutil.copy2(ROOT/'index.json',root/'index.json')
                state = copy.deepcopy(self.state);state['money'][field]=amount
                (root/'state/checkpoint.json').write_text(json.dumps(state))
                with self.assertRaisesRegex(ValidationError,'checkpoint/entity mismatch: party-finances'):
                    validate(root)

    def test_unknown_custody_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ('entities','archive','state'):
                shutil.copytree(ROOT/name,root/name)
            shutil.copy2(ROOT/'index.json',root/'index.json')
            state = copy.deepcopy(self.state);state['custody']['detainees'].append('invented-prisoner')
            (root/'state/checkpoint.json').write_text(json.dumps(state))
            with self.assertRaisesRegex(ValidationError,'custody: unknown character'):
                validate(root)
