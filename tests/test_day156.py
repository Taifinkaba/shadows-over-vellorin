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
        for name in ('entities','archive','state','changes'):
            shutil.copytree(ROOT/name,self.root/name)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')
        self.state=json.loads((self.root/'state/checkpoint.json').read_text())
        self.ledger=json.loads((self.root/'state/finance-ledger.json').read_text())

    def reject(self,edit,message):
        ledger=copy.deepcopy(self.ledger);edit(ledger)
        (self.root/'state/finance-ledger.json').write_text(json.dumps(ledger))
        with self.assertRaisesRegex(ValidationError,message):
            validate_finance_ledger(self.root,self.state)

    def test_final_checkpoint(self):
        self.assertIn(f"{len(json.loads((self.root/'index.json').read_text())['entries'])} entity records", validate(self.root))
        s=self.state
        self.assertEqual((s['date'],s['calendar']['day_of_season'],s['time'],s['location'],s['status']),('Year 848 Day 156',36,'20:15','Ashvale Estate family sitting room','ENDED'))
        self.assertEqual((s['theron']['hp'],s['theron']['mp'],s['resources']['equipped_defense'],s['resources']['staff_mp'],s['resources']['wagon_mp']),(100,378,49,156,60))
        self.assertEqual({a['id']:a['balance_cp'] for a in self.ledger['controlled_cash']['accounts']},dict(personal_purse=4400,legacy_secured=13590,general_treasury=13000,emergency_reserve=7800,operating_reserve=14700,savings=0,expedition_reserve=500,development=5200,research=0,blackscale_private=2600,ashvale_restitution=15400))

    def test_cash_cannot_include_cottage(self):
        self.reject(lambda l:l['controlled_cash']['accounts'][-1].update(balance_cp=20900),'account total')

    def test_duplicate_postings(self):
        for index in range(5):
            with self.subTest(index=index):
                self.reject(lambda l:l['arc_reconciliation']['events'][index].update(application_count=2),'apply once')
        self.reject(lambda l:l['arc_reconciliation']['events'].append(copy.deepcopy(l['arc_reconciliation']['events'][2])),'duplicate')

    def test_balanced_duplicate_event_cannot_replace_real_cost(self):
        self.reject(lambda l:l['arc_reconciliation']['events'].__setitem__(0,copy.deepcopy(l['arc_reconciliation']['events'][1])),'amount differs|duplicate')

    def test_integer_copper_only(self):
        for amount in (4400.0,True,-1):
            with self.subTest(amount=amount):
                self.reject(lambda l:l['controlled_cash']['accounts'][0].update(balance_cp=amount),'integer')

    def test_restitution_components_and_noncash(self):
        self.reject(lambda l:l['restitution']['cash_components_cp'].update(strongbox=6350),'components')
        self.reject(lambda l:l['restitution'].update(noncash_appraisal_cp=0),'noncash')
        self.reject(lambda l:l['excluded_property'][-1].update(included_in_controlled_cash=True),'excluded property')

    def test_commitment_does_not_spend_cash(self):
        self.reject(lambda l:l['commitments'].update(expansion_paid_cp=31700),'unpaid')
        self.reject(lambda l:l['commitments'].update(uncommitted_cp=77190),'uncommitted')
        self.reject(lambda l:l['commitments'].update(construction_started=True),'unpaid')

    def test_prior_surplus_not_awarded_again(self):
        self.reject(lambda l:l['historical_reconstruction'].update(application_count=2),'apply once')
        self.reject(lambda l:l['arc_reconciliation'].update(automatic_future_income=True),'automatic future')

    def test_ruling_not_fabricated_receipt(self):
        self.reject(lambda l:l['historical_discrepancies'][0].update(discovered_receipts=True),'player ruling')
        self.reject(lambda l:l['historical_discrepancies'][0].update(current_cash_adjustment_cp=12800),'player ruling')

    def test_settlement_does_not_invent_more_assets_or_final_judgment(self):
        self.reject(lambda l:l['restitution'].update(personal_transferable_holdings_exhausted=False),'settlement limits')
        self.reject(lambda l:l['restitution'].update(future_legal_review_possible=False),'settlement limits')

    def test_stale_checkpoint_rejected(self):
        self.state['date']='Year 848 Day 137'
        with self.assertRaisesRegex(ValidationError,'date/status mismatch'):
            validate_finance_ledger(self.root,self.state)
