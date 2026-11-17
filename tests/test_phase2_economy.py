"""Economic evidence boundaries, finite arithmetic and preservation; never posts events."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.economy import commission, financial_report
from scripts.economy_expansion import (COSTS, DOMAINS, EXTENSIONS, PROPERTY_FIELDS, SHIPMENT_FIELDS,
    cycle_result, remaining_inventory, require_evidence, receipt_classification)
from scripts.validate import validate, ValidationError

ROOT = Path(__file__).resolve().parents[1]


def data(ident, root=ROOT):
    kind = 'rules' if ident == 'payroll-construction-and-trade' else 'mechanics'
    return json.loads(re.search(r'```json\n(.*?)\n```', (root/f'entities/{kind}/{ident}.md').read_text(), re.S)[1])


class Phase2EconomyTests(unittest.TestCase):
    def reject(self, ident, mutation, pattern):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for folder in ('entities','state','archive','changes','docs','governance'):
                shutil.copytree(ROOT/folder, root/folder)
            shutil.copy2(ROOT/'index.json',root/'index.json')
            kind='rules' if ident=='payroll-construction-and-trade' else 'mechanics'
            p=root/f'entities/{kind}/{ident}.md';s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S)
            d=json.loads(m[1]);mutation(d[EXTENSIONS[ident]])
            p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])
            with self.assertRaisesRegex(ValidationError, pattern):validate(root)

    def test_five_part_current_report(self):
        r=financial_report(ROOT);self.assertEqual(list(r['five_part_accounting']),DOMAINS)
        self.assertIsNone(r['income_statement']['actual_received_revenue'])
        self.assertEqual(r['five_part_accounting']['received-revenue']['classified_transactions'],[])

    def test_ownership_remains_unknown(self):
        r=financial_report(ROOT)['five_part_accounting']['cash-ownership']
        self.assertEqual(r['controlled_cp'],74590);self.assertEqual(r['allocation_status'],'UNRECONCILED / UNKNOWN')
        self.assertTrue(all(x['current_amount_cp'] is None for x in r['categories'].values()))

    def test_transfer_not_revenue(self):
        for kind in ('internal-transfer','distribution','deposit','loan'):
            self.assertNotEqual(receipt_classification(dict(direction='inflow',kind=kind,status='received')),'received-revenue')

    def test_forecast_and_unknown_inflow_not_revenue(self):
        for tx in ({'direction':'inflow'},dict(direction='inflow',kind='revenue',status='forecast')):
            self.assertEqual(receipt_classification(tx),'unclassified-cash-movement')
        self.assertEqual(receipt_classification(dict(direction='inflow',kind='revenue',status='received')),'received-revenue')

    def test_unpaid_is_not_paid_expense(self):
        self.assertNotEqual(receipt_classification(dict(direction='outflow',kind='expense',status='committed')),'documented-expenses')
        self.assertEqual(receipt_classification(dict(direction='outflow',kind='expense',status='paid')),'documented-expenses')
        d=financial_report(ROOT)['five_part_accounting']['documented-expenses']
        self.assertEqual(d['unpaid_commitments_cp'],31700);self.assertIs(d['commitment_is_paid_expense'],False)

    def test_appraisal_not_cash(self):
        d=financial_report(ROOT)['five_part_accounting']['assets-and-liabilities']
        self.assertIs(d['noncash_appraisals_are_cash'],False);self.assertIsNone(d['current_asset_total_cp'])
        cottage=next(x for x in data('property-financial-references')['properties'] if x['property_id']=='briarstone-cottage')
        self.assertIs(cottage['cash_inclusion'],False);self.assertIsNone(cottage['current_market_value_cp'])

    def test_positive_negative_zero_business_results(self):
        costs=dict.fromkeys(COSTS,10)
        for received,expected in ((100,30),(30,-40),(70,0)):
            r=cycle_result(100,received,costs);self.assertEqual(r['cash_operating_result_cp'],expected)
            self.assertEqual(r['ending_cash_cp'],100+expected)

    def test_all_cost_classes_required(self):
        with self.assertRaisesRegex(ValueError,'complete paid'):cycle_result(100,100,{'wages':10})

    def test_unknown_not_zero_cost(self):
        costs=dict.fromkeys(COSTS,0);costs['maintenance']=None
        with self.assertRaisesRegex(ValueError,'UNKNOWN'):cycle_result(100,100,costs)

    def test_distribution_changes_cash_once(self):
        r=cycle_result(100,100,dict.fromkeys(COSTS,0),distributions=30,net_transfers=-20)
        self.assertEqual(r,dict(cash_operating_result_cp=100,ending_cash_cp=150))

    def test_no_overspending_or_boolean_money(self):
        for args in ((0,0,dict.fromkeys(COSTS,1)),(True,100,dict.fromkeys(COSTS,0))):
            with self.assertRaises(ValueError):cycle_result(*args)

    def test_finite_inventory_and_losses(self):
        self.assertEqual(remaining_inventory(10,3,8,2,15),3)
        for args in ((10,0,11,0,10),(10,10,0,0,15),(10,None,0,0,15),(True,0,0,0,15)):
            with self.assertRaises(ValueError):remaining_inventory(*args)

    def test_property_requires_title_consent_and_updates(self):
        good=dict.fromkeys(PROPERTY_FIELDS,'documented evidence')
        self.assertTrue(require_evidence(good,PROPERTY_FIELDS))
        for field in ('verified_title','consent','jurisdiction','payment_evidence','original_owner_update','ledger_update'):
            bad=good|{field:None}
            with self.assertRaisesRegex(ValueError,'UNKNOWN'):require_evidence(bad,PROPERTY_FIELDS)

    def test_shipment_requires_route_receipt_settlement(self):
        good=dict.fromkeys(SHIPMENT_FIELDS,'documented evidence');good['quantity']=3
        self.assertTrue(require_evidence(good,SHIPMENT_FIELDS))
        for field in ('verified_route','receipt','departure','ownership','settlement_status'):
            with self.assertRaisesRegex(ValueError,'UNKNOWN'):require_evidence(good|{field:None},SHIPMENT_FIELDS)
        for qty in (0,-1,True,float('inf')):
            with self.assertRaises(ValueError):require_evidence(good|{'quantity':qty},SHIPMENT_FIELDS)

    def test_nested_unknown_evidence_not_accepted(self):
        good=dict.fromkeys(PROPERTY_FIELDS,'evidence');good['verified_title']={'source':None}
        with self.assertRaises(ValueError):require_evidence(good,PROPERTY_FIELDS)

    def test_no_automatic_cycles_or_conditions(self):
        self.reject('economy-accounting',lambda d:d.update(actual_cycles=[{'profit':100}]),'no automatic revenue')
        self.reject('economy-accounting',lambda d:d.update(actual_conditions=['shortage']),'no automatic revenue')

    def test_five_domains_cannot_collapse(self):
        self.reject('economy-accounting',lambda d:d['accounting_domains'].remove('documented-expenses'),'five accounting')

    def test_no_competing_ledger(self):
        self.reject('economy-accounting',lambda d:d['authority_refs'].update(ledger='state/second-ledger.json'),'competing financial')

    def test_industries_reuse_and_coverage(self):
        self.reject('economy-accounting',lambda d:d['sector_integrations'][0].update(industry_refs=['invented-mill']),'industry reference')
        d=data('economy-accounting')['approved_economic_design']
        self.assertEqual(len(d['sector_integrations']),14);self.assertEqual(len(d['settlement_owner_refs']),10)
        self.assertEqual(len(data('settlement-trade')['relationships']),12)

    def test_service_rate_and_rent_exclusion(self):
        self.reject('service-price-references',lambda d:d.update(percent=22),'scope/rate')
        self.reject('service-price-references',lambda d:d.update(excluded_services=[]),'scope/rate')

    def test_no_invented_tariff_or_date(self):
        self.reject('service-price-references',lambda d:d.update(base_tariffs={'bed':55}),'remain UNKNOWN')
        self.reject('service-price-references',lambda d:d.update(effective_date='Day181'),'remain UNKNOWN')

    def test_original_prices_wages_and_commission(self):
        f=json.loads((ROOT/'tests/fixtures/phase2-06-preservation.json').read_text())
        old=f['legacy_economic_payloads']['entities/mechanics/service-price-references.md']
        self.assertEqual(data('service-price-references')['approved_references'],old['approved_references'])
        self.assertEqual(commission(10000),dict(merchant_gross_cp=10000,estate_revenue_cp=2200,merchant_share_cp=7800))
        with self.assertRaisesRegex(ValueError,'rounding'):commission(1)

    def test_no_new_holding_or_transfer(self):
        self.reject('property-financial-references',lambda d:d.update(new_holdings=['house']),'no holdings')

    def test_property_evidence_template_cannot_omit_title(self):
        self.reject('property-financial-references',lambda d:d['transaction_template'].pop('verified_title'),'empty evidence')

    def test_no_automatic_delivery(self):
        self.reject('payroll-construction-and-trade',lambda d:d.update(automatic_delivery=True),'no contracts')

    def test_no_tax_assessment_or_unknown_jurisdiction_override(self):
        self.reject('payroll-construction-and-trade',lambda d:d.update(actual_assessments=[{'tax':100}]),'no contracts')
        self.reject('payroll-construction-and-trade',lambda d:d.update(law_owner_ref='party-finances'),'jurisdiction')

    def test_no_wage_or_shipment_template_event(self):
        self.reject('payroll-construction-and-trade',lambda d:d['wage_template'].update(gross_pay=20),'empty evidence')
        self.reject('payroll-construction-and-trade',lambda d:d['shipment_template'].update(receipt='delivered'),'empty evidence')

    def test_public_approval_and_no_private_authority(self):
        self.reject('economy-accounting',lambda d:d.update(approval_source_ref='README.md'),'approval provenance')
        for ident in EXTENSIONS:
            s=(ROOT/f'entities/{"rules" if ident=="payroll-construction-and-trade" else "mechanics"}/{ident}.md').read_text()
            self.assertIn('visibility: gm-reference',s)
        self.assertNotIn('gm-secret',json.dumps(data('economy-accounting')['approved_economic_design']))

    def test_original_owners_and_history_preserved(self):
        f=json.loads((ROOT/'tests/fixtures/phase2-06-preservation.json').read_text())
        for path,digest in f['unchanged_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        for path,revision in f['authorized_owner_revisions'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),revision['after_sha256'],path)
            ident=Path(path).stem;current=data(ident);current.pop(EXTENSIONS[ident])
            self.assertEqual(current,f['legacy_economic_payloads'][path],path)
        for path in ('state/finance-ledger.json','state/checkpoint.json','entities/locations/briarstone-cottage.md',
                     'entities/locations/ashvale-estate.md','entities/locations/ashvale-lodge.md',
                     'entities/rules/guild-membership-and-contracts.md','entities/mechanics/illicit-commerce-design.md',
                     'entities/rules/dungeon-exploration.md'):
            self.assertIn(path,f['unchanged_sha256'])

    def test_reports_do_not_mutate_sources(self):
        paths=[ROOT/'state/finance-ledger.json',ROOT/'state/checkpoint.json']
        before=[p.read_bytes() for p in paths];financial_report(ROOT)
        self.assertEqual(before,[p.read_bytes() for p in paths])


if __name__=='__main__':unittest.main()
