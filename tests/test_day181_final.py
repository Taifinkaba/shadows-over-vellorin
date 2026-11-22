from case_support import isolated_case
"""Player-confirmed reconciliation; all mutations use disposable fixtures."""
import copy
import hashlib
import json
import unittest
import test_day181
ROOT=test_day181.ROOT
from snapshot_helpers import YEAR852_REVISED_AUTHORITIES, YEAR851_REVISED_AUTHORITIES, CHARACTER_SHEET_REVISIONS, DAY196_REVISED_AUTHORITIES, SUNCREST262_REVISED_AUTHORITIES, restore_reconciled_day181
from scripts.validate import validate,validate_finance_ledger
from scripts.gm_dashboard import build_dashboard,verify_view
from scripts.economy import financial_report

class FinalReconciliationTests(test_day181.Day181Tests):
    # Inherit future transaction and historical protection coverage, selecting schema4.
    def setUp(self):
        super().setUp()
        restore_reconciled_day181(self.root, ROOT/'tests/fixtures/day181-final-state-delta.json')
        for path in ('entities/mechanics/theron-abilities.md','entities/locations/briarstone-cottage.md'):
            (self.root/path).write_bytes((ROOT/path).read_bytes())
        self.state=json.loads((self.root/'state/checkpoint.json').read_text());self.ledger=json.loads((self.root/'state/finance-ledger.json').read_text())

    def test_no_new_mana_event_or_other_pool_change(self):
        event=self.state['provenance']['mp_bridge']['recovery_events'][0]
        self.assertEqual((event['potential_mp'],event['actual_mp'],event['excess_mp']),(24,22,2))
        self.assertIsNone(event['date']);self.assertIsNone(event['location'])
        self.assertEqual((self.state['resources']['staff_mp'],self.state['resources']['wagon_mp']),(156,60))

    def test_dashboard_and_financial_report_support_new_schema(self):
        d=build_dashboard(self.root);verify_view(self.root,d)
        f=d['sections']['finances'];h=d['sections']['theron']
        self.assertEqual(f['reconciled_repair_expense_cp']['value'],2600)
        self.assertTrue(f['cottage_repairs_completed']['value'])
        self.assertEqual(h['reconciled_mp_recovery']['value']['actual_mp'],22)
        self.assertNotIn('unexplained_mp_endpoint_change',h)
        report=financial_report(self.root)
        self.assertEqual(report['cash_position']['controlled']['amount_cp'],74590)
        self.assertEqual(len(report['post_arc_transactions']),2)


    def test_causality_and_continuity_and_contracts_and_schema_1(self):
        with self.subTest(case='test_repair_event_cannot_repost_as_future'), isolated_case(self):
            t=self.synthetic();t['source_event_id']=self.ledger['post_arc_transactions'][0]['id'];self.apply_fixture(t)
            with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)
        with self.subTest(case='test_unrelated_authorities_and_historical_adoption_preserved'), isolated_case(self):
            manifest=json.loads((ROOT/'tests/fixtures/day181-final-reconciliation.json').read_text())
            self.assertEqual(hashlib.sha256((ROOT/'archive/checkpoints/year848-day181-unresolved-adoption.json').read_bytes()).hexdigest(),manifest['prior_unresolved_snapshot_sha256'])
            for key,value in manifest.items():
                if isinstance(value,dict):
                    for path,digest in value.items():
                        if path not in (DAY196_REVISED_AUTHORITIES | SUNCREST262_REVISED_AUTHORITIES | CHARACTER_SHEET_REVISIONS | YEAR851_REVISED_AUTHORITIES | YEAR852_REVISED_AUTHORITIES) and isinstance(digest,str) and len(digest)==64:self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        with self.subTest(case='test_repair_mutations_rejected'), isolated_case(self):
            original=copy.deepcopy(self.ledger)
            for field,value in [('amount_cp',801),('account_id','blackscale'),('time','12:00'),('application_count',2),('commitment_effect_cp',-800),('source_quote','invented'),('date','Year 848 Day 159')]:
                with self.subTest(field=field):
                    self.ledger=copy.deepcopy(original);self.ledger['post_arc_transactions'][0][field]=value
                    self.save()
                    with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)
        with self.subTest(case='test_future_maintenance_supported'), isolated_case(self):
            t=self.synthetic();t['category']='maintenance';t['property_id']='briarstone-cottage';self.apply_fixture(t)
            validate_finance_ledger(self.root,self.state)
        with self.subTest(case='test_recovery_mutations_rejected'), isolated_case(self):
            original=copy.deepcopy(self.state)
            for field,value in [('intervals',2),('actual_mp',24),('date','Year 848 Day 165'),('location','Ashvale Estate'),('usable_ambient_mana',False),('concentration_conditions_met',False)]:
                self.state=copy.deepcopy(original);self.state['provenance']['mp_bridge']['recovery_events'][0][field]=value;self.save()
                with self.subTest(field=field),self.assertRaises(ValueError):validate(self.root)

    def test_contracts_and_schema_and_identity_and_resources_2(self):
        with self.subTest(case='test_pre_reconciliation_view_is_stale'), isolated_case(self):
            from snapshot_helpers import restore_unresolved_day181
            current=[(p,(self.root/p).read_bytes()) for p in ('state/checkpoint.json','state/finance-ledger.json','entities/characters/theron-ashvale.md','entities/mechanics/party-finances.md','entities/mechanics/theron-abilities.md','entities/locations/briarstone-cottage.md')]
            restore_unresolved_day181(self.root);old=build_dashboard(self.root)
            for p,data in current:(self.root/p).write_bytes(data)
            with self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,old)
        with self.subTest(case='test_duplicate_historical_payment_rejected'), isolated_case(self):
            self.ledger['post_arc_transactions'].append(copy.deepcopy(self.ledger['post_arc_transactions'][0]));self.save()
            with self.assertRaises(ValueError):validate_finance_ledger(self.root,self.state)
        with self.subTest(case='test_repair_payments_exactly_once_and_unknown_accounts'), isolated_case(self):
            payments=self.ledger['post_arc_transactions']
            self.assertEqual([(t['date'],t['cash_effect_cp']) for t in payments],[('Year 848 Day 158',-800),('Year 848 Day 165',-1800)])
            self.assertEqual(77190+sum(t['cash_effect_cp'] for t in payments),74590)
            for t in payments:
                self.assertIsNone(t['account_id']);self.assertIsNone(t['time']);self.assertIsNone(t['recipient'])
            self.assertEqual(self.ledger['commitments']['expansion_paid_cp'],0)
            self.assertEqual(self.ledger['commitments']['uncommitted_cp'],42890)
