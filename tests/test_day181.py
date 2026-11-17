"""Explicit adoption and future finance fixtures; no real posting or recovered history."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import yaml
from scripts.validate import validate,ValidationError,validate_finance_ledger
from scripts.gm_dashboard import build_dashboard,verify_view,render_markdown
from scripts.economy import financial_report
from snapshot_helpers import restore_day156,restore_unresolved_day181

ROOT=Path(__file__).resolve().parents[1]

class Day181Tests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-day181-');self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')
        restore_unresolved_day181(self.root)
        self.state=json.loads((self.root/'state/checkpoint.json').read_text());self.ledger=json.loads((self.root/'state/finance-ledger.json').read_text())

    def save(self):
        (self.root/'state/checkpoint.json').write_text(json.dumps(self.state));(self.root/'state/finance-ledger.json').write_text(json.dumps(self.ledger))

    def reject_ledger(self,fn):
        fn(self.ledger);self.save()
        with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)

    def reject_state(self,fn):
        fn(self.state);self.save()
        with self.assertRaises(ValueError):validate(self.root)

    def synthetic(self):
        path='changes/chronicles/synthetic-finance-fixture.md'
        (self.root/path).write_text('Synthetic fixture only: verified controlled funding, authority and received/paid transaction evidence. Not real campaign activity.\n')
        evidence={'source_ref':path,'quote':'verified controlled funding, authority and received/paid transaction evidence'}
        self.state['source']=path;self.ledger['source']=path
        self.ledger['account_verifications']=[dict(account_id='test-funds',opening_cp=10000,owner='synthetic controlled owner',scope='controlled',authorized_actor_ids=['theron-ashvale'],status='player-approved',date='Year 848 Day 181',time='19:30',evidence=evidence)]
        self.ledger['controlled_cash']['accounts']=[dict(id='test-funds',owner='synthetic controlled owner',balance_cp=10000)]
        self.ledger['controlled_cash']['allocation_status']='PARTIALLY VERIFIED / REMAINDER UNKNOWN'
        return dict(id='synthetic-event',source_event_id='synthetic-source-event',date='Year 848 Day 181',time='19:30',evidence=evidence,status='verified',category='supplies-purchased',direction='outflow',amount_cp=100,payer='synthetic payer',recipient='synthetic recipient',account_id='test-funds',to_account_id=None,authority_id='theron-ashvale',cash_effect_cp=-100,revenue_recognized_cp=0,commitment_id=None,commitment_effect_cp=0,property_id=None,business_id=None,contract_id=None,application_count=1,ownership_scope='controlled')

    def apply_fixture(self,t):
        # Disposable test arithmetic, not a production posting API.
        self.ledger['transactions']=[t];cash=self.ledger['controlled_cash'];cash['total_cp']+=t['cash_effect_cp']
        balances={x['id']:x for x in cash['accounts']}
        balances[t['account_id']]['balance_cp']+=t['cash_effect_cp'] if t['direction']!='internal' else -t['amount_cp']
        if t['direction']=='internal':balances[t['to_account_id']]['balance_cp']+=t['amount_cp']
        c=self.ledger['commitments'];c['expansion_paid_cp']-=t['commitment_effect_cp'];c['expansion_outstanding_cp']+=t['commitment_effect_cp'];c['uncommitted_cp']=cash['total_cp']-c['expansion_outstanding_cp']
        self.state['money']['total_gp_sp']=f"{cash['total_cp']}cp";self.save()

    def test_valid_endpoint_and_unknown_fields(self):
        self.assertIn('checkpoint valid',validate(self.root));s=self.state
        self.assertEqual((s['schema_version'],s['date'],s['time'],s['location'],s['status']),(6,'Year 848 Day 181','19:30','Ashvale Estate','UNKNOWN'))
        self.assertEqual(s['calendar'],dict(season='Suncrest',day_of_season=61));self.assertEqual((s['theron']['hp'],s['theron']['mp']),(100,400))
        self.assertEqual(s['context']['companions_present'],[]);self.assertEqual(s['context']['party_roles'],{});self.assertIsNone(s['provenance']['current_equipment']['night_sovereign_carried_not_equipped'])

    def test_historical_snapshot_exact_and_arithmetic_preserved(self):
        fixture=json.loads((ROOT/'tests/fixtures/day181-migration.json').read_text())
        for path,digest in fixture['historical_sha256'].items():self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)
        old=json.loads((self.root/self.ledger['historical_day156_ref']).read_text());a=old['arc_reconciliation']
        self.assertEqual(a['opening_cp'],115990);self.assertEqual(len(a['events']),5);self.assertEqual(a['opening_cp']+sum(x['delta_cp'] for x in a['events']),77190)
        self.assertEqual(old['controlled_cash']['total_cp']-old['commitments']['expansion_committed_cp'],45490)
        self.assertEqual(sum(x['balance_cp'] for x in old['controlled_cash']['accounts']),77190)

    def test_unexplained_bridge_is_not_a_transaction_or_account(self):
        self.assertEqual(self.ledger['bridge']['difference_cp'],2600);self.assertFalse(self.ledger['bridge']['is_transaction']);self.assertIsNone(self.ledger['bridge']['assigned_account_id'])
        self.assertEqual(self.ledger['transactions'],[]);self.assertEqual(self.ledger['account_verifications'],[]);self.assertEqual(self.ledger['controlled_cash']['accounts'],[])
        self.assertEqual(self.ledger['controlled_cash']['allocation_status'],'UNRECONCILED / UNKNOWN')
        self.assertEqual(self.ledger['controlled_cash']['total_cp']-self.ledger['commitments']['expansion_outstanding_cp'],42890)

    def test_no_new_mana_event_or_other_pool_change(self):
        p=self.state['provenance']['mp_bridge'];self.assertEqual(p['difference_mp'],22);self.assertEqual(p['recovery_events'],[])
        self.assertEqual((self.state['resources']['staff_mp'],self.state['resources']['wagon_mp']),(156,60))
        self.assertEqual(self.state['context']['recent_mp_costs'],{});self.assertIsNone(self.state['context']['mp_before_recent_casts'])

    def test_dashboard_and_financial_report_support_new_schema(self):
        d=build_dashboard(self.root);h=d['sections']['theron'];f=d['sections']['finances'];scene=d['sections']['current_scene']
        self.assertEqual(scene['date']['value'],'Year 848 Day 181');self.assertEqual(scene['time']['value'],'19:30');self.assertEqual(scene['location']['value'],'Ashvale Estate')
        self.assertEqual([h[x]['value'] for x in ('mp','equipped_defense','defense_if_night_sovereign_worn','staff_mp','wagon_mp')],[400,49,51,156,60]);self.assertIsNone(h['night_sovereign_carried_not_equipped']['value'])
        self.assertEqual([f[x]['value'] for x in ('controlled_cp','committed_unpaid_cp','uncommitted_cp')],[74590,31700,42890]);self.assertEqual(f['accounts'],[])
        self.assertEqual(f['unexplained_endpoint_difference_cp']['value'],2600);self.assertEqual(h['unexplained_mp_endpoint_change']['value'],22)
        self.assertIn('ADOPTED',d['sections']['verification_warnings']['later_supplied_snapshot']['value']);self.assertIn('<details>',render_markdown(d))
        for row in d['sections']['companions']+d['sections']['personnel']:self.assertIsNone(row['last_verified_location']['value'])
        r=financial_report(self.root);self.assertEqual(r['cash_position']['controlled']['amount_cp'],74590);self.assertEqual(r['cash_position']['accounts'],[]);self.assertEqual(len(r['cash_position']['historical_day156_accounts']),11)

    def test_saved_day156_view_is_stale_after_adoption(self):
        restore_day156(self.root);old=build_dashboard(self.root)
        for path in ('state/checkpoint.json','state/finance-ledger.json','entities/characters/theron-ashvale.md','entities/mechanics/party-finances.md','entities/mechanics/theron-abilities.md'):(self.root/path).write_bytes((ROOT/path).read_bytes())
        with self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,old)
        verify_view(self.root,build_dashboard(self.root))

    def test_future_verified_expense_supported(self):
        t=self.synthetic();self.apply_fixture(t);validate_finance_ledger(self.root,self.state)
        self.assertEqual(self.ledger['controlled_cash']['total_cp'],74490)
        self.assertEqual(self.ledger['commitments']['uncommitted_cp'],42790)

    def test_future_received_income_supported_without_automatic_income(self):
        t=self.synthetic();t.update(category='business-revenue',direction='inflow',cash_effect_cp=100,revenue_recognized_cp=100,business_id='ashvale-lodge:forge',property_id='ashvale-lodge')
        self.apply_fixture(t);validate_finance_ledger(self.root,self.state);self.assertEqual(self.ledger['controlled_cash']['total_cp'],74690)

    def test_future_construction_payment_reduces_cash_and_remaining_commitment_once(self):
        t=self.synthetic();t.update(category='construction-payment',commitment_id='estate-expansion',commitment_effect_cp=-100)
        self.apply_fixture(t);validate_finance_ledger(self.root,self.state)
        c=self.ledger['commitments'];self.assertEqual((c['expansion_paid_cp'],c['expansion_outstanding_cp'],c['uncommitted_cp']),(100,31600,42890));self.assertFalse(c['construction_started'])

    def test_future_transfer_is_not_income(self):
        t=self.synthetic();a=copy.deepcopy(self.ledger['account_verifications'][0]);a.update(account_id='destination',opening_cp=0);self.ledger['account_verifications'].append(a)
        self.ledger['controlled_cash']['accounts'].append(dict(id='destination',owner=a['owner'],balance_cp=0))
        t.update(category='internal-transfer',direction='internal',cash_effect_cp=0,to_account_id='destination');self.apply_fixture(t)
        validate_finance_ledger(self.root,self.state);self.assertEqual(self.ledger['controlled_cash']['total_cp'],74590)
        self.assertEqual(sum(x['balance_cp'] for x in self.ledger['controlled_cash']['accounts']),10000)

    def test_duplicate_transaction_and_source_ids_rejected(self):
        for duplicate_source in (False,True):
            self.state=json.loads((ROOT/'state/checkpoint.json').read_text());self.ledger=json.loads((ROOT/'state/finance-ledger.json').read_text())
            t=self.synthetic();self.apply_fixture(t);second=copy.deepcopy(t)
            if duplicate_source:second['id']='different-id'
            self.ledger['transactions'].append(second);self.save()
            with self.subTest(source=duplicate_source),self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)

    def test_account_approval_cannot_create_cash_or_use_historical_source(self):
        t=self.synthetic();self.ledger['account_verifications'][0]['opening_cp']=74591;self.save()
        with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)
        self.ledger['account_verifications'][0]['opening_cp']=10000
        self.ledger['account_verifications'][0]['evidence']={'source_ref':'changes/chronicles/year848-day181-endpoint-adoption.md','quote':'74590cp'};self.save()
        with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)

    def test_actual_future_session_can_sync_same_authorities(self):
        t=self.synthetic();self.apply_fixture(t)
        path=self.root/'entities/mechanics/party-finances.md';parts=path.read_text().split('---',2);m=yaml.safe_load(parts[1]);m['checkpoint_values']['money.total_gp_sp']=self.state['money']['total_gp_sp'];path.write_text('---\n'+yaml.safe_dump(m,sort_keys=False)+'---'+parts[2])
        self.assertIn('checkpoint valid',validate(self.root))

    def test_finance_and_dashboard_are_readonly(self):
        def hashes():return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}
        before=hashes();financial_report(self.root);build_dashboard(self.root);validate(self.root);self.assertEqual(hashes(),before)

    def test_day137_surplus_source_cannot_be_reposted_with_new_ids(self):
        t=self.synthetic();t.update(category='other-receipt',direction='inflow',amount_cp=52000,cash_effect_cp=52000,revenue_recognized_cp=52000,evidence={'source_ref':'changes/chronicles/year848-day137-end-session.md','quote':'520gp'})
        self.apply_fixture(t)
        with self.assertRaisesRegex(ValueError,'historical/adoption/reference'):validate_finance_ledger(self.root,self.state)

    def test_checkpoint6_rejects_rewritten_ledger2(self):
        old=json.loads((self.root/'archive/checkpoints/year848-day156-finance-ledger.json').read_text())
        old['as_of']=self.ledger['as_of'];old['source']=self.state['source'];old['controlled_cash']['total_cp']=74590
        old['controlled_cash']['accounts'][1]['balance_cp']-=2600
        old['arc_reconciliation'].update(opening_cp=113390,closing_cp=74590)
        old['commitments']['uncommitted_cp']=42890
        (self.root/'state/finance-ledger.json').write_text(json.dumps(old))
        with self.assertRaisesRegex(ValueError,'requires finance schema3'):validate_finance_ledger(self.root,self.state)

    def test_modified_historical_snapshot_rejected_even_if_balanced(self):
        p=self.root/self.ledger['historical_day156_ref'];old=json.loads(p.read_text());old['controlled_cash']['accounts'][0]['balance_cp']+=100;old['controlled_cash']['accounts'][1]['balance_cp']-=100;p.write_text(json.dumps(old))
        with self.assertRaisesRegex(ValueError,'immutable Day156'):validate(self.root)

    def test_historical_entity_bodies_preserved(self):
        for path,old in json.loads((ROOT/'archive/checkpoints/year848-day156-entity-records.json').read_text()).items():
            self.assertIn(old.split('---',2)[2],(ROOT/path).read_text())

    def test_all_unrelated_authorities_and_old_history_unchanged(self):
        f=json.loads((ROOT/'tests/fixtures/day181-migration.json').read_text())
        for path,digest in f['unrelated_sha256'].items():
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)


LEDGER_CASES={
 'wrong_total':lambda l:l['controlled_cash'].update(total_cp=77190),
 'wrong_available':lambda l:l['commitments'].update(uncommitted_cp=45490),
 'double_commitment_deduction':lambda l:l['controlled_cash'].update(total_cp=42890),
 'incorrect_bridge':lambda l:l['bridge'].update(difference_cp=2700),
 'bridge_as_transaction':lambda l:l['bridge'].update(is_transaction=True),
 'bridge_blackscale_assignment':lambda l:l['bridge'].update(assigned_account_id='blackscale_private'),
 'bridge_operating_assignment':lambda l:l['bridge'].update(assigned_account_id='operating_reserve'),
 'bridge_resolved':lambda l:l['bridge'].update(classification='expense'),
 'fictitious_gap_account':lambda l:l['controlled_cash']['accounts'].append({'id':'missing','owner':'unknown','balance_cp':2600}),
 'historical_accounts_as_current':lambda l:l['controlled_cash'].update(allocation_status='VERIFIED'),
 'unpaid_expansion_deducted':lambda l:l['commitments'].update(expansion_paid_cp=31700,expansion_outstanding_cp=0),
 'construction_started':lambda l:l['commitments'].update(construction_started=True),
 'automatic_income':lambda l:l.update(automatic_future_income=True),
 'property_as_cash':lambda l:l['excluded_property'][-1].update(included_in_controlled_cash=True),
 'third_party_as_cash':lambda l:l['excluded_property'][1].update(included_in_controlled_cash=True),
 'floating_cash':lambda l:l['controlled_cash'].update(total_cp=74590.0),
 'boolean_bridge':lambda l:l['bridge'].update(difference_cp=True),
 'historical_distribution_repost':lambda l:l.update(automatic_future_income=True),
 'restitution_recredited':lambda l:l['controlled_cash'].update(total_cp=89990),
}
for name,fn in LEDGER_CASES.items():
 def test(self,fn=fn):self.reject_ledger(fn)
 setattr(Day181Tests,'test_reject_'+name,test)
STATE_CASES={
 'fabricated_room':lambda s:s.update(location='Ashvale Estate family sitting room'),
 'invented_session_status':lambda s:s.update(status='ENDED'),
 'inferred_companion':lambda s:s['context']['companions_present'].append('aric-ashvale'),
 'historical_mask_status_as_current':lambda s:s['provenance']['current_equipment'].update(night_sovereign_carried_not_equipped=True),
 'invented_mp_recovery':lambda s:s['provenance']['mp_bridge']['recovery_events'].append('rest'),
 'staff_recharge':lambda s:s['resources'].update(staff_mp=180),
 'wagon_recharge':lambda s:s['resources'].update(wagon_mp=59),
 'arbitrary_attribute':lambda s:s['theron'].update(str=13),
 'conditional_defense':lambda s:s['provenance'].update(conditional_defense=53),
}
for name,fn in STATE_CASES.items():
 def test(self,fn=fn):self.reject_state(fn)
 setattr(Day181Tests,'test_reject_'+name,test)
TX_CASES={
 'unverified_funding':lambda l,t:t.update(account_id='blackscale_private'),
 'unauthorized_actor':lambda l,t:t.update(authority_id='master-beren'),
 'unapproved_status':lambda l,t:t.update(status='proposed'),
 'wrong_cash_effect':lambda l,t:t.update(cash_effect_cp=0),
 'float_amount':lambda l,t:t.update(amount_cp=100.0),
 'bool_amount':lambda l,t:t.update(amount_cp=True),
 'repeated_application':lambda l,t:t.update(application_count=2),
 'historical_event':lambda l,t:t.update(source_event_id='new_operating_surplus'),
 'historical_transaction_id':lambda l,t:t.update(id='night_sovereign'),
 'fake_bridge_source':lambda l,t:t.update(evidence={'source_ref':'changes/chronicles/year848-day181-endpoint-adoption.md','quote':'2600cp'}),
 'missing_source':lambda l,t:t['evidence'].update(source_ref='missing.md'),
 'invented_quote':lambda l,t:t['evidence'].update(quote='invented unrecorded amount'),
 'prior_date':lambda l,t:t.update(date='Year 848 Day 156'),
 'invalid_date':lambda l,t:t.update(time='25:00'),
 'insufficient_funds':lambda l,t:t.update(amount_cp=10001,cash_effect_cp=-10001),
 'third_party_transaction':lambda l,t:t.update(ownership_scope='academy'),
 'noncash_appraisal':lambda l,t:t.update(category='property-appraisal'),
 'expense_as_income':lambda l,t:t.update(revenue_recognized_cp=100),
 'unrelated_commitment_effect':lambda l,t:t.update(commitment_effect_cp=-100),
 'unknown_business':lambda l,t:t.update(business_id='ashvale-lodge:invented'),
 'wrong_business_parent':lambda l,t:t.update(business_id='ashvale-lodge:forge',property_id='ashvale-estate'),
 'old_contract_reward':lambda l,t:t.update(category='contract-reward',direction='inflow',cash_effect_cp=100,revenue_recognized_cp=100,contract_id='G-215'),
}
for name,fn in TX_CASES.items():
 def test(self,fn=fn):
  t=self.synthetic();self.apply_fixture(t);fn(self.ledger,t);self.save()
  with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)
 setattr(Day181Tests,'test_reject_transaction_'+name,test)

if __name__=='__main__':unittest.main()
