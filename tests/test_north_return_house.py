from case_support import isolated_case
"""Schema4 regression cases for the supplied Seven Bells checkpoint."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import yaml

from scripts.validate import ValidationError, copper, validate, validate_state, frontmatter

ROOT = Path(__file__).resolve().parents[1]


class NorthReturnHouseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-day124-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
            shutil.copytree(ROOT/name, self.root/name)
        shutil.copy2(ROOT/'index.json', self.root/'index.json')
        shutil.copy2(ROOT/'archive/checkpoints/year848-day124-0145.json', self.root/'state/checkpoint.json')
        historical = json.loads((ROOT/'archive/checkpoints/year848-day124-entity-values.json').read_text())
        for ident, values in historical.items():
            path = next((self.root/'entities').rglob(ident+'.md'))
            meta = frontmatter(path)
            body = path.read_text().split('---', 2)[2]
            meta['checkpoint_values'] = values
            path.write_text('---\n'+yaml.safe_dump(meta, sort_keys=False)+'---'+body)
        self.state = json.loads((self.root/'state/checkpoint.json').read_text())

    def invalid(self, edit, message):
        state = copy.deepcopy(self.state)
        edit(state)
        with self.assertRaisesRegex(ValidationError, message):
            validate_state(state)


    def test_contracts_and_schema_1(self):
        with self.subTest(case='test_exact_supplied_snapshot'), isolated_case(self):
            s = self.state
            self.assertIn('checkpoint valid', validate(self.root))
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
        with self.subTest(case='test_no_free_recovery'), isolated_case(self):
            self.invalid(lambda s:s['context']['recent_mp_recovery'].update(ambient_source_usable=False), 'usable ambient source')
        with self.subTest(case='test_recovery_personal_only'), isolated_case(self):
            self.invalid(lambda s:s['context']['recent_mp_recovery'].update(personal_only=False), 'personal-only')
        with self.subTest(case='test_no_partial_interval'), isolated_case(self):
            for minutes in (0,9,11,True):
                with self.subTest(minutes=minutes):
                    self.invalid(lambda s:s['context']['recent_mp_recovery'].update(uninterrupted_minutes=minutes), 'integer|incomplete')
        with self.subTest(case='test_old_or_exaggerated_rate_rejected'), isolated_case(self):
            for amount in (12,48,True):
                with self.subTest(amount=amount):
                    self.invalid(lambda s:s['context']['recent_mp_recovery'].update(amount=amount), 'integer|incorrect Assimilation')

    def test_contracts_and_schema_and_identity_2(self):
        with self.subTest(case='test_personal_recovery_caps_at_maximum'), isolated_case(self):
            s = copy.deepcopy(self.state)
            s['context']['mp_before_recent_casts'] = 400
            s['theron']['mp'] = 400
            validate_state(s)
            self.invalid(lambda s:s['theron'].update(mp=401), 'MP exceeds')
        with self.subTest(case='test_no_invented_old_account'), isolated_case(self):
            self.invalid(lambda s:s['money'].update(blackscale_private_gp_sp='112gp'), 'expected keys')
        with self.subTest(case='test_nonnegative_integer_casualties'), isolated_case(self):
            self.invalid(lambda s:s['custody'].update(fatalities=True), 'integer')
        with self.subTest(case='test_no_duplicate_or_detained_free_person'), isolated_case(self):
            self.invalid(lambda s:s['custody']['detainees'].append('perrin'), 'duplicate person')
            self.invalid(lambda s:s['custody']['detainees'].append('sella'), 'free people cannot')
        with self.subTest(case='test_unknown_custody_reference'), isolated_case(self):
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
                    shutil.copytree(self.root/name,root/name)
                shutil.copy2(self.root/'index.json',root/'index.json')
                state = copy.deepcopy(self.state);state['custody']['detainees'].append('invented-prisoner')
                (root/'state/checkpoint.json').write_text(json.dumps(state))
                with self.assertRaisesRegex(ValidationError,'custody: unknown character'):
                    validate(root)

    def test_resources_3(self):
        with self.subTest(case='test_cost_cannot_be_omitted'), isolated_case(self):
            self.invalid(lambda s:s['context'].update(recent_mp_costs={}), 'expected entries')
        with self.subTest(case='test_wrong_mp_or_double_deduction_rejected'), isolated_case(self):
            self.invalid(lambda s:s['theron'].update(mp=361), 'expenditure/recovery')
            self.invalid(lambda s:s['context']['recent_mp_costs'].update({'Shadow Mantle':16,'Umbral Murmur':9}), 'expenditure/recovery')
        with self.subTest(case='test_costs_cannot_exceed_available_mana'), isolated_case(self):
            self.invalid(lambda s:s['context']['recent_mp_costs'].update({'Mental Probe':376}), 'exceeds starting pool')
        with self.subTest(case='test_segregated_cash_and_entity_agreement'), isolated_case(self):
            for field, amount in [('total_gp_sp','552gp 3sp'), ('total_gp_sp','555gp 1sp 4cp'), ('office_petty_gp_sp','0gp'), ('provisional_historic_gp_sp','0gp')]:
                with self.subTest(field=field, amount=amount), tempfile.TemporaryDirectory() as temp:
                    root = Path(temp)
                    for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
                        shutil.copytree(self.root/name,root/name)
                    shutil.copy2(self.root/'index.json',root/'index.json')
                    state = copy.deepcopy(self.state);state['money'][field]=amount
                    (root/'state/checkpoint.json').write_text(json.dumps(state))
                    with self.assertRaisesRegex(ValidationError,'checkpoint/entity mismatch: party-finances'):
                        validate(root)
