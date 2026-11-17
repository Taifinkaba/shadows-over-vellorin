from case_support import isolated_case
"""Regression coverage for the explicit Day156 ruling and cash/noncash boundaries."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from scripts.validate import ValidationError, validate, validate_finance_ledger

ROOT=Path(__file__).resolve().parents[1]

class Day156Tests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-day156-')
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
            shutil.copytree(ROOT/name,self.root/name)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')
        from snapshot_helpers import restore_day156
        restore_day156(self.root)
        self.state=json.loads((self.root/'state/checkpoint.json').read_text())
        self.ledger=json.loads((self.root/'state/finance-ledger.json').read_text())

    def reject(self,edit,message):
        ledger=copy.deepcopy(self.ledger);edit(ledger)
        (self.root/'state/finance-ledger.json').write_text(json.dumps(ledger))
        with self.assertRaisesRegex(ValidationError,message):
            validate_finance_ledger(self.root,self.state)


    def test_continuity_and_contracts_and_schema_and_identity_1(self):
        with self.subTest(case='test_final_checkpoint'), isolated_case(self):
            self.assertIn(f"{len(json.loads((self.root/'index.json').read_text())['entries'])} entity records", validate(self.root))
            s=self.state
            self.assertEqual((s['date'],s['calendar']['day_of_season'],s['time'],s['location'],s['status']),('Year 848 Day 156',36,'20:15','Ashvale Estate family sitting room','ENDED'))
            self.assertEqual((s['theron']['hp'],s['theron']['mp'],s['resources']['equipped_defense'],s['resources']['staff_mp'],s['resources']['wagon_mp']),(100,378,49,156,60))
            self.assertEqual({a['id']:a['balance_cp'] for a in self.ledger['controlled_cash']['accounts']},dict(personal_purse=4400,legacy_secured=13590,general_treasury=13000,emergency_reserve=7800,operating_reserve=14700,savings=0,expedition_reserve=500,development=5200,research=0,blackscale_private=2600,ashvale_restitution=15400))
        with self.subTest(case='test_stale_checkpoint_rejected'), isolated_case(self):
            self.state['date']='Year 848 Day 137'
            with self.assertRaisesRegex(ValidationError,'date/status mismatch'):
                validate_finance_ledger(self.root,self.state)
        with self.subTest(case='test_prior_surplus_not_awarded_again'), isolated_case(self):
            self.reject(lambda l:l['historical_reconstruction'].update(application_count=2),'apply once')
            self.reject(lambda l:l['arc_reconciliation'].update(automatic_future_income=True),'automatic future')
        with self.subTest(case='test_ruling_not_fabricated_receipt'), isolated_case(self):
            self.reject(lambda l:l['historical_discrepancies'][0].update(discovered_receipts=True),'player ruling')
            self.reject(lambda l:l['historical_discrepancies'][0].update(current_cash_adjustment_cp=12800),'player ruling')
        with self.subTest(case='test_duplicate_postings'), isolated_case(self):
            for index in range(5):
                with self.subTest(index=index):
                    self.reject(lambda l:l['arc_reconciliation']['events'][index].update(application_count=2),'apply once')
            self.reject(lambda l:l['arc_reconciliation']['events'].append(copy.deepcopy(l['arc_reconciliation']['events'][2])),'duplicate')

    def test_identity_and_resources_2(self):
        with self.subTest(case='test_balanced_duplicate_event_cannot_replace_real_cost'), isolated_case(self):
            self.reject(lambda l:l['arc_reconciliation']['events'].__setitem__(0,copy.deepcopy(l['arc_reconciliation']['events'][1])),'amount differs|duplicate')
        with self.subTest(case='test_cash_cannot_include_cottage'), isolated_case(self):
            self.reject(lambda l:l['controlled_cash']['accounts'][-1].update(balance_cp=20900),'account total')
        with self.subTest(case='test_integer_copper_only'), isolated_case(self):
            for amount in (4400.0,True,-1):
                with self.subTest(amount=amount):
                    self.reject(lambda l:l['controlled_cash']['accounts'][0].update(balance_cp=amount),'integer')
        with self.subTest(case='test_restitution_components_and_noncash'), isolated_case(self):
            self.reject(lambda l:l['restitution']['cash_components_cp'].update(strongbox=6350),'components')
            self.reject(lambda l:l['restitution'].update(noncash_appraisal_cp=0),'noncash')
            self.reject(lambda l:l['excluded_property'][-1].update(included_in_controlled_cash=True),'excluded property')
        with self.subTest(case='test_commitment_does_not_spend_cash'), isolated_case(self):
            self.reject(lambda l:l['commitments'].update(expansion_paid_cp=31700),'unpaid')
            self.reject(lambda l:l['commitments'].update(uncommitted_cp=77190),'uncommitted')
            self.reject(lambda l:l['commitments'].update(construction_started=True),'unpaid')

    def test_resources_3(self):
        with self.subTest(case='test_settlement_does_not_invent_more_assets_or_final_judgment'), isolated_case(self):
            self.reject(lambda l:l['restitution'].update(personal_transferable_holdings_exhausted=False),'settlement limits')
            self.reject(lambda l:l['restitution'].update(future_legal_review_possible=False),'settlement limits')
