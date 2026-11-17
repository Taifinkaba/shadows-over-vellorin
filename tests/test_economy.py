from case_support import isolated_case, validate_scope
"""Economy reports and candidate validation never post or mutate campaign records."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from scripts.economy import (amount, commission, copper, display, financial_report, validate_amount,
                             validate_transactions, validate_payroll)
from scripts.validate import validate, ValidationError

ROOT=Path(__file__).resolve().parents[1]


class MoneyTests(unittest.TestCase):


    def transaction(self):
        return dict(id='synthetic-payment',event_id='synthetic-event',kind='expense',account_id='a',to_account_id=None,
            amount=amount(100,'entities/locations/ashvale-lodge.md','owner','paid','synthetic-date'),source_quote='Forge performs actual paid repair jobs.',
            ownership_scope='controlled-cash',revenue_recognized_cp=0,status='paid',period='synthetic-period')

    def accounts(self):return {'a':{'owner':'owner'},'b':{'owner':'owner'}}


    def payroll(self):
        return dict(employee_id='tomas',employee_label='Tomas',employer='synthetic employer',job='synthetic job',pay_rate=None,
                    pay_period='synthetic-period',hours_or_work=None,gross_pay=amount(100,'entities/locations/ashvale-lodge.md','owner','paid','synthetic-date'),
                    deductions=0,payment_status='paid',payment_date='synthetic-date',ledger_transaction_ref='synthetic-payment',
                    source_ref='entities/locations/ashvale-lodge.md',source_quote='wages included in operating ledger',expense_coverage_id='synthetic-coverage')


    def test_contracts_and_schema_and_identity_1(self):
        with self.subTest(case='test_conversion_and_normalization'), isolated_case(self):
            self.assertEqual(copper(1),100);self.assertEqual(copper(sp=1),10)
            self.assertEqual(copper(9,1,14),924);self.assertEqual(display(77190),'771 gp 9 sp 0 cp')
        with self.subTest(case='test_noninteger_denominations_rejected'), isolated_case(self):
            for bad in (True,False,1.0,-1,'100'):
                with self.subTest(bad=bad),self.assertRaises(ValueError):copper(gp=bad)
        with self.subTest(case='test_all_existing_arc_ids_cannot_be_reposted'), isolated_case(self):
            ledger=json.loads((ROOT/'archive/checkpoints/year848-day156-finance-ledger.json').read_text())
            ids=[x['id'] for x in ledger['arc_reconciliation']['events']]
            for ident in ids:
                with self.subTest(ident=ident),self.assertRaisesRegex(ValueError,'historical event'):
                    validate_transactions([{**self.transaction(),'event_id':ident}],self.accounts(),ROOT,ids)
        with self.subTest(case='test_internal_transfer_cannot_be_income'), isolated_case(self):
            t={**self.transaction(),'kind':'transfer','to_account_id':'b'}
            validate_transactions([t],self.accounts(),ROOT)
            with self.assertRaisesRegex(ValueError,'not income'):validate_transactions([{**t,'revenue_recognized_cp':100}],self.accounts(),ROOT)
            with self.assertRaisesRegex(ValueError,'distinct'):validate_transactions([{**t,'to_account_id':'a'}],self.accounts(),ROOT)
        with self.subTest(case='test_duplicate_transaction_and_event_rejected'), isolated_case(self):
            t=self.transaction()
            with self.assertRaisesRegex(ValueError,'transaction id'):validate_transactions([t,copy.deepcopy(t)],self.accounts(),ROOT)
            second={**t,'id':'different'}
            with self.assertRaisesRegex(ValueError,'historical event'):validate_transactions([t,second],self.accounts(),ROOT)
            with self.assertRaisesRegex(ValueError,'historical event'):validate_transactions([t],self.accounts(),ROOT,[t['event_id']])

    def test_identity_and_resources_2(self):
        with self.subTest(case='test_unknown_account_or_owner_rejected'), isolated_case(self):
            for key,val in [('account_id','not-an-account'),('ownership_scope','academy'),('ownership_scope','noncash-property')]:
                with self.subTest(key=key,val=val),self.assertRaises(ValueError):validate_transactions([{**self.transaction(),key:val}],self.accounts(),ROOT)
            t=self.transaction();t['amount']['ownership']='third party'
            with self.assertRaisesRegex(ValueError,'ownership mismatch'):validate_transactions([t],self.accounts(),ROOT)
        with self.subTest(case='test_payment_needs_date_and_quote'), isolated_case(self):
            t=self.transaction();t['amount']['verified_date']=None
            with self.assertRaisesRegex(ValueError,'date required'):validate_transactions([t],self.accounts(),ROOT)
            with self.assertRaisesRegex(ValueError,'quote missing'):validate_transactions([{**self.transaction(),'source_quote':'invented receipt'}],self.accounts(),ROOT)
        with self.subTest(case='test_duplicate_payroll_or_aggregate_period_rejected'), isolated_case(self):
            row=self.payroll()
            with self.assertRaisesRegex(ValueError,'duplicate payroll'):validate_payroll([row,row],[self.transaction()],{'tomas'},ROOT)
            with self.assertRaisesRegex(ValueError,'coverage'):validate_payroll([row],[self.transaction()],{'tomas'},ROOT,['synthetic-coverage'])
        with self.subTest(case='test_unpaid_payroll_no_cash_reference'), isolated_case(self):
            row={**self.payroll(),'payment_status':'incurred-unpaid','payment_date':None,'ledger_transaction_ref':None,'deductions':None}
            validate_payroll([row],[],{'tomas'},ROOT)
            with self.assertRaisesRegex(ValueError,'cash payment'):validate_payroll([{**row,'ledger_transaction_ref':'synthetic-payment'}],[],{'tomas'},ROOT)
        with self.subTest(case='test_commission_does_not_claim_merchant_gross'), isolated_case(self):
            self.assertEqual(commission(10000),{'merchant_gross_cp':10000,'estate_revenue_cp':2200,'merchant_share_cp':7800})

    def test_resources_3(self):
        with self.subTest(case='test_fractional_commission_requires_ruling'), isolated_case(self):
            with self.assertRaisesRegex(ValueError,'rounding'):commission(1)
        with self.subTest(case='test_unknown_amount_is_not_zero'), isolated_case(self):
            a=amount(None,'source','unknown','UNKNOWN');validate_amount(a)
            self.assertIsNone(a['amount_cp']);self.assertEqual(a['display_amount'],'UNKNOWN')
        with self.subTest(case='test_amount_metadata_and_display_consistency'), isolated_case(self):
            valid=amount(123,'source','owner','paid','date');validate_amount(valid)
            for key,value in [('amount_cp',True),('amount_cp',1.23),('amount_cp',-1),('display_amount','12 gp'),('currency','gp'),('source_ref',''),('ownership',''),('status',''),('verified_date',False)]:
                bad={**valid,key:value}
                with self.subTest(key=key,value=value),self.assertRaises(ValueError):validate_amount(bad)
        with self.subTest(case='test_candidate_payment_does_not_write'), isolated_case(self):
            before=(ROOT/'state/finance-ledger.json').read_bytes()
            validate_transactions([self.transaction()],self.accounts(),ROOT)
            self.assertEqual(before,(ROOT/'state/finance-ledger.json').read_bytes())
        with self.subTest(case='test_revenue_requires_actual_amount'), isolated_case(self):
            t={**self.transaction(),'kind':'revenue','revenue_recognized_cp':100};validate_transactions([t],self.accounts(),ROOT)
            with self.assertRaises(ValueError):validate_transactions([{**t,'revenue_recognized_cp':0}],self.accounts(),ROOT)

    def test_resources_4(self):
        with self.subTest(case='test_commitment_is_not_payment'), isolated_case(self):
            with self.assertRaisesRegex(ValueError,'not payment'):validate_transactions([{**self.transaction(),'status':'committed'}],self.accounts(),ROOT)
        with self.subTest(case='test_synthetic_payroll_valid_not_posted'), isolated_case(self):
            validate_payroll([self.payroll()],[self.transaction()],{'tomas'},ROOT)
        with self.subTest(case='test_same_payment_cannot_cover_two_payroll_entries'), isolated_case(self):
            second={**self.payroll(),'employee_id':None,'employee_label':'other sourced staff'}
            with self.assertRaisesRegex(ValueError,'duplicate payroll payment'):validate_payroll([self.payroll(),second],[self.transaction()],{'tomas'},ROOT)
        with self.subTest(case='test_paid_payroll_must_match_amount_date_and_expense'), isolated_case(self):
            for key,val in [('payment_date',None),('deductions',None),('deductions',1),('ledger_transaction_ref','missing')]:
                with self.subTest(key=key),self.assertRaises(ValueError):validate_payroll([{**self.payroll(),key:val}],[self.transaction()],{'tomas'},ROOT)
            with self.assertRaisesRegex(ValueError,'paid expense'):validate_payroll([self.payroll()],[{**self.transaction(),'kind':'revenue'}],{'tomas'},ROOT)
        with self.subTest(case='test_wage_rates_require_amount_and_unit'), isolated_case(self):
            row={**self.payroll(),'pay_rate':1.5}
            with self.assertRaisesRegex(ValueError,'pay rate'):validate_payroll([row],[self.transaction()],{'tomas'},ROOT)


class EconomyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-economy-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for directory in ('entities', 'state', 'archive', 'changes', 'docs', 'governance'):shutil.copytree(ROOT/directory,self.root/directory)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')
        from snapshot_helpers import restore_day156
        restore_day156(self.root)

    def path(self,ident):
        return self.root/f"entities/{'rules' if ident=='payroll-construction-and-trade' else 'mechanics'}/{ident}.md"

    def edit(self,ident,fn):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);fn(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,ident,fn):
        self.edit(ident,fn)
        with self.assertRaises(ValidationError):validate_scope(self.root, 'economy')


    def test_continuity_1(self):
        with self.subTest(case='test_current_repository_valid'), isolated_case(self):
            self.assertIn(f"{len(json.loads((self.root / 'index.json').read_text())['entries'])} entity records", validate(self.root))
        with self.subTest(case='test_report_model_not_actual_receipts'), isolated_case(self):
            report=financial_report(self.root);income=report['income_statement']
            for key in ('actual_received_revenue','actual_incurred_expenses','actual_net_profit'):self.assertIsNone(income[key])
            model=income['historical_model'];self.assertEqual(model['periods'],8)
            self.assertEqual([model[x]['amount_cp'] for x in ('receipts','expenses','surplus')],[216000,164000,52000])
            self.assertIn('not independently',model['qualification'])
        with self.subTest(case='test_report_transfers_are_not_income'), isolated_case(self):
            distribution=financial_report(self.root)['internal_transfers']['known_historical_distribution']
            self.assertEqual(distribution['income_effect_cp'],0);self.assertEqual(distribution['application_count'],1)
            self.assertEqual(sum(x['amount']['amount_cp'] for x in distribution['allocations']),52000)
        with self.subTest(case='test_report_arithmetic_does_not_close_evidence_gaps'), isolated_case(self):
            rec=financial_report(self.root)['reconciliation'];self.assertEqual(rec['arithmetic_difference_cp'],0)
            self.assertEqual(rec['recorded_net_inflows']['amount_cp'],22300)
            self.assertEqual(rec['recorded_outflows']['amount_cp'],61100)
            self.assertIn('unitemized',' '.join(rec['evidence_gaps']));self.assertIn('26gp',' '.join(rec['evidence_gaps']))
            self.assertIsNone(rec['opening']['verified_date'])
        with self.subTest(case='test_report_rejects_other_ledger_schema'), isolated_case(self):
            p=self.root/'state/finance-ledger.json';d=json.loads(p.read_text());d['schema_version']=1;p.write_text(json.dumps(d))
            with self.assertRaisesRegex(ValueError,'schema2 or3'):financial_report(self.root)

    def test_continuity_and_identity_and_resources_2(self):
        with self.subTest(case='test_cli_readonly_report'), isolated_case(self):
            result=subprocess.run([sys.executable,str(ROOT/'scripts/economy.py'),'--report','--root',str(self.root)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(json.loads(result.stdout)['as_of']['date'],'Year 848 Day 156')
        with self.subTest(case='test_report_leaves_every_source_unchanged'), isolated_case(self):
            before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('entities', 'state', 'archive', 'changes', 'docs', 'governance') for p in (self.root/folder).rglob('*') if p.is_file()}
            financial_report(self.root)
            self.assertEqual(before,{path:hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in before})
        with self.subTest(case='test_report_cash_commitments_and_exclusions'), isolated_case(self):
            report=financial_report(self.root);cash=report['cash_position']
            self.assertEqual(cash['controlled']['amount_cp'],77190);self.assertEqual(cash['committed_unpaid']['amount_cp'],31700)
            self.assertEqual(cash['uncommitted']['amount_cp'],45490)
            self.assertEqual(sum(x['balance']['amount_cp'] for x in cash['accounts']),77190)
            excluded={x['id']:x for x in cash['excluded']}
            self.assertEqual(excluded['briarstone_cottage']['amount']['amount_cp'],5500)
            self.assertIn('Approximately',excluded['provisional_historic_coinage']['qualification'])
            self.assertIsNone(excluded['academy_cash']['amount']['verified_date'])
            self.assertEqual(cash['accounts'][0]['balance']['ownership'],'Theron-managed controlled funds')
        with self.subTest(case='test_report_no_unsupported_asset_totals'), isolated_case(self):
            assets=financial_report(self.root)['assets_and_liabilities']
            for key in ('inventory_value','receivables','wages_owed','other_payables'):self.assertIsNone(assets[key])

    def test_cases_rejection_table(self):
        for (name, (ident, fn)) in CASES.items():
            with self.subTest(case=name), isolated_case(self):
                self.reject(ident, fn)


# Independent negative cases exercise prohibited promotions and authority drift.
CASES={
 'wrong_conversion':('economy-accounting',lambda d:d['currency'].update(cp_per_gp=1000)),
 'boolean_currency':('economy-accounting',lambda d:d['currency'].update(cp_per_sp=True)),
 'second_ledger':('economy-accounting',lambda d:d.update(ledger_ref='state/checkpoint.json')),
 'wrong_finance_owner':('economy-accounting',lambda d:d.update(mechanics_owner_ref='property-financial-references')),
 'automatic_posting':('economy-accounting',lambda d:d.update(automatic_postings=True)),
 'new_transaction':('economy-accounting',lambda d:d['new_transactions'].append({'amount_cp':2600})),
 'new_payroll':('economy-accounting',lambda d:d['new_payroll'].append({'amount_cp':100})),
 'construction_started':('economy-accounting',lambda d:d['new_construction_events'].append({'status':'in-progress'})),
 'shipment_created':('economy-accounting',lambda d:d['new_shipments'].append({'status':'completed'})),
 'false_classification':('economy-accounting',lambda d:d.update(classification='PROPOSED')),
 'extra_money_field':('economy-accounting',lambda d:d.update(current_balance_cp=74590)),
 'missing_business':('business-financial-references',lambda d:d['businesses'].pop()),
 'duplicate_business':('business-financial-references',lambda d:d['businesses'].__setitem__(0,copy.deepcopy(d['businesses'][1]))),
 'business_income':('business-financial-references',lambda d:d['businesses'][0].update(current_receipts_cp=0)),
 'business_expense':('business-financial-references',lambda d:d['businesses'][0].update(current_expenses_cp=100)),
 'business_autorevenue':('business-financial-references',lambda d:d['businesses'][0].update(automatic_revenue=True)),
 'business_owner_copy':('business-financial-references',lambda d:d['businesses'][0].update(owner_id='theron-ashvale')),
 'unfounded_business_parent':('business-financial-references',lambda d:d['businesses'][0].update(parent_location_id='ashvale-estate')),
 'commission_on_excluded_business':('business-financial-references',lambda d:d['businesses'][0].update(commission_policy_ref='entities/locations/ashvale-estate.md')),
 'model_as_receipts':('business-financial-references',lambda d:d['businesses'][-1].update(historical_qualification='verified receipt')),
 'new_title':('property-financial-references',lambda d:d['new_ownership_events'].append({'owner':'Theron'})),
 'new_valuation':('property-financial-references',lambda d:d['new_valuations'].append({'amount_cp':5500})),
 'property_as_cash':('property-financial-references',lambda d:d['properties'][0].update(cash_inclusion=True)),
 'unsupported_market_value':('property-financial-references',lambda d:d['properties'][0].update(current_market_value_cp=25200)),
 'academy_personal_title':('property-financial-references',lambda d:d['properties'][3].update(legal_owner_id='theron-ashvale')),
 'cottage_personal_title':('property-financial-references',lambda d:d['properties'][2].update(legal_owner_id='theron-ashvale')),
 'academy_new_manager':('property-financial-references',lambda d:d['properties'][3].update(manager_id='tomas')),
 'inventory_appraisal':('property-financial-references',lambda d:d['asset_owner_refs'][0].update(valuation_cp=100)),
 'evidence_as_cash':('property-financial-references',lambda d:d['asset_owner_refs'][-1].update(cash_inclusion=True)),
 'missing_property':('property-financial-references',lambda d:d['properties'].pop()),
 'wrong_asset_source':('property-financial-references',lambda d:d['asset_owner_refs'][0].update(source_ref='entities/items/vanguard-wagon.md')),
 'payroll_payment':('payroll-construction-and-trade',lambda d:d['new_payroll'].append({'status':'paid'})),
 'new_supplier':('payroll-construction-and-trade',lambda d:d['suppliers'].append('new supplier')),
 'completed_shipment':('payroll-construction-and-trade',lambda d:d['shipments'].append({'status':'completed'})),
 'applied_price_modifier':('payroll-construction-and-trade',lambda d:d['active_price_modifiers'].append('shortage')),
 'wrong_road_owner':('payroll-construction-and-trade',lambda d:d.update(road_owner_ref='justice-road-links')),
 'wrong_contract_owner':('payroll-construction-and-trade',lambda d:d.update(contract_owner_ref='party-finances')),
}

if __name__=='__main__':unittest.main()
