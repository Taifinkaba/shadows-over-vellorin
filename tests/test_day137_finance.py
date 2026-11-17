"""Current checkpoint and mutation tests for one-time estate reconstruction."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate import ValidationError, validate, validate_finance_ledger, validate_state

ROOT = Path(__file__).resolve().parents[1]


class Day137Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-day137-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
            shutil.copytree(ROOT/name, self.root/name)
        shutil.copy2(ROOT/'index.json', self.root/'index.json')
        shutil.copy2(ROOT/'archive/checkpoints/year848-day137-0930.json', self.root/'state/checkpoint.json')
        shutil.copy2(ROOT/'archive/checkpoints/year848-day137-finance-ledger.json', self.root/'state/finance-ledger.json')
        import yaml
        from scripts.validate import frontmatter
        historical = json.loads((ROOT/'archive/checkpoints/year848-day137-entity-values.json').read_text())
        for ident, values in historical.items():
            path = next((self.root/'entities').rglob(ident+'.md'))
            meta = frontmatter(path)
            body = path.read_text().split('---', 2)[2]
            meta['checkpoint_values'] = values
            path.write_text('---\n'+yaml.safe_dump(meta, sort_keys=False)+'---'+body)
        self.state = json.loads((self.root/'state/checkpoint.json').read_text())
        self.ledger = json.loads((self.root/'state/finance-ledger.json').read_text())

    def invalid_ledger(self, edit, message):
        edit(self.ledger)
        (self.root/'state/finance-ledger.json').write_text(json.dumps(self.ledger))
        with self.assertRaisesRegex(ValidationError, message):
            validate_finance_ledger(self.root, self.state)

    def test_current_snapshot_and_exact_approved_model(self):
        self.assertIn('checkpoint valid', validate(self.root))
        s = self.state
        self.assertEqual((s['schema_version'], s['date'], s['time'], s['status'], s['location']), (5,'Year 848 Day 137','09:30','ENDED','Ashvale Estate'))
        self.assertEqual(s['calendar'], dict(season='Suncrest', day_of_season=17))
        self.assertEqual(s['theron'], dict(hp=100,hp_max=100,mp=400,mp_max=400,defense=46,rank='S+',level=5,str=12,dex=20,con=16,int=20,wis=19,cha=19,unspent_attributes=0))
        self.assertEqual(s['resources'],dict(equipped_defense=49,bracers_defense_bonus=3,staff_mp=156,staff_mp_max=180,wagon_mp=60,wagon_mp_max=60,chronos_eye_locked=True,dragon_slayer_locked=True))
        m=self.ledger['operating_reconstruction']
        self.assertEqual(m['periods'],8)
        self.assertEqual(m['revenue_cp_per_period'], dict(merchant_commissions=5500,lodge_rooms_and_meals=4500,rental_cottages=2500,merchant_storage_bays=2500,forge_and_repairs=3500,bakery=4500,caravan_and_stables=2500,healing_springs=1500))
        self.assertEqual(m['expenses_cp_per_period'],dict(staff_wages=9000,supplies_and_materials=3500,maintenance=2000,fodder_and_fuel=1000,guards_and_security=3500,taxes_and_transport=1500))
        self.assertEqual((m['gross_estate_receipts_cp'],m['operating_expenses_cp'],m['net_distributable_surplus_cp']),(216000,164000,52000))
        self.assertEqual({a['id']:a['balance_cp'] for a in self.ledger['controlled_cash']['accounts']},dict(personal_purse=4600,legacy_secured=49490,general_treasury=13000,emergency_reserve=7800,operating_reserve=7800,savings=5200,expedition_reserve=5200,development=5200,research=2600,blackscale_private=2600))
        self.assertEqual([a['percent'] for a in self.ledger['distributions']['allocations']],[25,15,15,10,10,10,5,5,5])
        self.assertEqual((s['custody']['reviewed'],s['custody']['released'],s['custody']['retained'],s['custody']['medically_transferred'],s['custody']['hearing_pending']),(4,2,1,1,True))

    def test_missing_ledger_field_reports_validation_error(self):
        self.invalid_ledger(lambda l:l.pop('controlled_cash'), 'expected keys')

    def test_excluded_money_cannot_inflate_cash(self):
        self.invalid_ledger(lambda l:l['controlled_cash']['accounts'][0].update(balance_cp=5524),'account total')

    def test_duplicate_historical_account_rejected(self):
        self.invalid_ledger(lambda l:l['controlled_cash']['accounts'].append(copy.deepcopy(l['controlled_cash']['accounts'][0])),'duplicate cash account')

    def test_merchant_gross_cannot_be_estate_commission(self):
        self.invalid_ledger(lambda l:l['operating_reconstruction']['revenue_cp_per_period'].update(merchant_commissions=25000),'merchant commission')

    def test_revenue_category_omission_rejected(self):
        self.invalid_ledger(lambda l:l['operating_reconstruction']['revenue_cp_per_period'].pop('bakery'),'revenue categories')

    def test_expense_total_checked(self):
        self.invalid_ledger(lambda l:l['operating_reconstruction']['expenses_cp_per_period'].update(staff_wages=0),'expense sum')

    def test_fractional_or_boolean_copper_rejected(self):
        for amount in (4600.0,True):
            with self.subTest(amount=amount):
                self.invalid_ledger(lambda l:l['controlled_cash']['accounts'][0].update(balance_cp=amount),'integer')

    def test_repeat_distribution_rejected(self):
        self.invalid_ledger(lambda l:l['distributions'].update(application_count=2),'apply once')

    def test_wrong_percentage_rejected(self):
        self.invalid_ledger(lambda l:l['distributions']['allocations'][0].update(percent=24),'allocation amount')

    def test_no_automatic_future_income(self):
        self.invalid_ledger(lambda l:l['operating_reconstruction'].update(automatic_future_awards=True),'automatic future')

    def test_excluded_property_flag_checked(self):
        self.invalid_ledger(lambda l:l['excluded_property'][0].update(included_in_controlled_cash=True),'excluded property')

    def test_no_fabricated_historical_adjustment(self):
        self.invalid_ledger(lambda l:l['historical_discrepancies'][0].update(current_cash_adjustment_cp=12800),'without adjustment')

    def test_expenses_cannot_be_deducted_twice(self):
        self.invalid_ledger(lambda l:l['expense_history']['events'].append(dict(delta_cp=-1900,balance_cp=101590)),'repeated expense')

    def test_land_cannot_be_deducted_again(self):
        self.invalid_ledger(lambda l:l['assets_deposits_liabilities']['land_purchase'].update(current_deduction_cp=25200),'already paid')

    def test_estimate_is_not_invoice(self):
        self.invalid_ledger(lambda l:l['assets_deposits_liabilities']['night_sovereign'].update(current_payable=True),'not payables')

    def test_checkpoint_total_must_match_ledger(self):
        self.state['money']['total_gp_sp']='1162gp 9sp'
        with self.assertRaisesRegex(ValidationError,'account total'):
            validate_finance_ledger(self.root,self.state)

    def test_no_invented_mana_history(self):
        self.state['context'].update(recent_mp_costs={'Imagined cast':10},mp_before_recent_casts=400)
        with self.assertRaisesRegex(ValidationError,'unverified'):
            validate_state(self.state)

    def test_locks_and_finite_resources(self):
        for field, value in [('chronos_eye_locked',False),('dragon_slayer_locked',False),('staff_mp',181),('wagon_mp',61)]:
            with self.subTest(field=field):
                state=copy.deepcopy(self.state);state['resources'][field]=value
                with self.assertRaisesRegex(ValidationError,'locked|exceeds'):
                    validate_state(state)

    def test_custody_counts_checked(self):
        self.state['custody']['released']=3
        with self.assertRaisesRegex(ValidationError,'review counts'):
            validate_state(self.state)

    def test_day137_mp_must_match_authoritative_entity(self):
        self.state['theron']['mp']=399
        (self.root/'state/checkpoint.json').write_text(json.dumps(self.state))
        with self.assertRaisesRegex(ValidationError,'checkpoint/entity mismatch'):
            validate(self.root)
