from case_support import isolated_case, validate_scope
"""Approved settlement design must not create current conditions or gameplay."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from snapshot_helpers import YEAR852_REVISED_AUTHORITIES, YEAR851_REVISED_AUTHORITIES, SUNCREST262_REVISED_AUTHORITIES
from scripts.validate import ValidationError, validate
from scripts.settlement_expansion import POPULATIONS, validate_dispatch

ROOT = Path(__file__).resolve().parents[1]


class Phase2SettlementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-phase2-settlements-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ('entities', 'state', 'archive', 'changes', 'docs', 'governance'):
            shutil.copytree(ROOT/folder, self.root/folder)
        shutil.copy2(ROOT/'index.json', self.root/'index.json')

    def path(self, ident):
        kind = 'locations' if ident in POPULATIONS else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```', self.path(ident).read_text(), re.S)[1])

    def edit(self, ident, change):
        p = self.path(ident); s = p.read_text(); m = re.search(r'```json\n(.*?)\n```', s, re.S)
        d = json.loads(m[1]); change(d)
        p.write_text(s[:m.start(1)] + json.dumps(d, indent=2) + s[m.end(1):])

    def reject(self, ident, change, pattern):
        self.edit(ident, change)
        with self.assertRaisesRegex(ValidationError, pattern): validate_scope(self.root, 'settlements', 'settlement_expansion')


    def test_causality_and_contracts_and_schema_1(self):
        with self.subTest(case='test_trade_does_not_invent_missing_river_route'), isolated_case(self):
            d = next(d for d in self.data('settlement-trade')['relationships'] if d['origin']=='southbank-landing')
            self.assertEqual(d['route_dependencies'], [])
            self.assertIn('No compatible surveyed', d['unresolved_operational_details'])
            self.assertEqual(d['verification_status'], 'UNVERIFIED PROPOSAL')
        with self.subTest(case='test_all_ten_populations_and_households'), isolated_case(self):
            self.assertIn('checkpoint valid', validate(self.root))
            for ident, amount in POPULATIONS.items():
                d = self.data(ident)['approved_design']
                self.assertEqual(d['population']['amount'], amount)
                self.assertEqual(d['population']['classification'], 'CONFIRMED CANON' if ident=='brackenford' else 'APPROVED DESIGN')
                self.assertIsNone(d['current_conditions'])
                self.assertEqual(d['events'], [])
                if ident != 'brackenford': self.assertIsNone(d['households'])
            self.assertEqual(self.data('brackenford')['approved_design']['households']['amount'], 42)
        with self.subTest(case='test_population_is_not_census'), isolated_case(self):
            self.reject('caelthorne', lambda d:d['approved_design']['population'].update(classification='CONFIRMED CANON'), 'classification/qualification')
        with self.subTest(case='test_population_cannot_change'), isolated_case(self):
            self.reject('silverbrook', lambda d:d['approved_design']['population'].update(amount=420), 'population contradicts')
        with self.subTest(case='test_no_unsupported_household_counts'), isolated_case(self):
            self.reject('stoneford', lambda d:d['approved_design'].update(households=100), 'unsupported household')

    def test_contracts_and_schema_2(self):
        cases = [
            ('test_registry_cannot_omit_settlement', 'settlement-services', lambda d: d['approved_design_location_ids'].pop(), 'ten-settlement coverage'),
            ('test_new_settlement_cannot_gain_unapproved_realm', 'world-geography', lambda d: next((n for n in d['nodes'] if n['id'] == 'windmere'))['parents'][0].update(id='valedorn'), 'unsupported realm/parent'),
            ('test_design_cannot_certify_license', 'rivermere', lambda d: d['approved_design']['businesses'][0].update(current_license='royal'), 'invented ownership'),
            ('test_adult_venue_requires_adult_workers', 'caelthorne', lambda d: next((b for b in d['approved_design']['businesses'] if 'brothel' in b['categories'])).update(adult_workers_only=False), 'adult consent/regulation'),
            ('test_adult_venue_requires_agency', 'rivermere', lambda d: next((b for b in d['approved_design']['businesses'] if 'brothel' in b['categories'])).update(worker_agency='Bound workers'), 'agency safeguards'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_3(self):
        cases = [
            ('test_business_legal_design_is_not_enacted_license', 'caelthorne', lambda d: d['approved_design']['businesses'][0].update(legal_design='licensed'), 'legal classification'),
            ('test_no_faction_or_mystery_connections', 'briarfall-crossing', lambda d: d['approved_design']['criminal_faction_refs'].append('Crown-07'), 'PR4 faction records'),
            ('test_illegal_context_cannot_be_active_crime', 'caelthorne', lambda d: d['approved_design']['unlawful_activity_designs'][0]['events'].append('theft'), 'active crimes'),
            ('test_trade_cannot_post_shipments', 'settlement-trade', lambda d: d['relationships'][0]['actual_shipments'].append('shipment1'), 'completed commerce'),
            ('test_trade_requires_origin_supplier', 'settlement-trade', lambda d: d['relationships'][0].update(supplier_industry_id='windmere:industry-pastoral'), 'supplier does not belong'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_and_identity_4(self):
        with self.subTest(case='test_partial_extension_is_rejected'), isolated_case(self):
            p = self.root/'index.json'; d=json.loads(p.read_text())
            d['entries']=[e for e in d['entries'] if e['id']!='settlement-trade'];p.write_text(json.dumps(d))
            (self.root/'entities/mechanics/settlement-trade.md').unlink()
            with self.assertRaisesRegex(ValidationError, 'incomplete trade/postal'):validate(self.root)
        with self.subTest(case='test_population_requires_approval_source'), isolated_case(self):
            self.reject('windmere', lambda d:d['approved_design']['population'].update(source_ref='README.md'), 'wrong approval provenance')
        with self.subTest(case='test_no_duplicate_business_design_ids'), isolated_case(self):
            self.reject('eastrun', lambda d:d['approved_design']['businesses'].append(copy.deepcopy(d['approved_design']['businesses'][0])), 'duplicate or wrong business')
        with self.subTest(case='test_known_brackenford_business_is_reference_not_duplicate'), isolated_case(self):
            b = self.data('brackenford'); a = b['approved_design']
            self.assertEqual({x['existing_business_ref'] for x in a['businesses']}, {x['id'] for x in b['businesses']})
            self.assertEqual(b['principal_official_id'], 'elsbeth-marrin')
            self.assertEqual(b['watch_official_id'], 'ressa-vale')
            self.assertEqual(b['businesses'][0]['operator_id'], 'mara-fenwick')
        with self.subTest(case='test_design_does_not_appoint_owner'), isolated_case(self):
            self.reject('eastrun', lambda d:d['approved_design']['businesses'][0].update(owner_id='theron-ashvale'), 'invented ownership')

    def test_identity_and_resources_5(self):
        with self.subTest(case='test_prices_are_baselines_not_quotes'), isolated_case(self):
            self.reject('service-price-references', lambda d:d['approved_references'][0].update(kind='current-verified-quote'), 'not a quote/charge')
        with self.subTest(case='test_legacy_payloads_and_unrelated_history_preserved'), isolated_case(self):
            f = json.loads((ROOT/'tests/fixtures/phase2-02-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path, revision in f['authorized_owner_revisions'].items():
                current = (SUNCREST262_REVISED_AUTHORITIES | YEAR851_REVISED_AUTHORITIES | YEAR852_REVISED_AUTHORITIES).get(path, revision)
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), current['after_sha256'], path)
            for path, legacy in f['legacy_settlement_payloads'].items():
                current = json.loads(re.search(r'```json\n(.*?)\n```', (ROOT/path).read_text(), re.S)[1])
                current.pop('approved_design', None)
                self.assertEqual(current, legacy, path)
        with self.subTest(case='test_design_cannot_create_stock_or_cash'), isolated_case(self):
            self.reject('windmere', lambda d:d['approved_design']['businesses'][0].update(cash_balance_cp=100), 'stock or cash')
        with self.subTest(case='test_trade_requires_compatible_endpoint_dependency'), isolated_case(self):
            self.reject('settlement-trade', lambda d:d['relationships'][0].update(route_dependencies=['route-brackenford-cottage']), 'does not connect trade')
        with self.subTest(case='test_price_or_wage_cannot_disagree_with_approval'), isolated_case(self):
            self.reject('service-price-references', lambda d:d['approved_references'][-1].update(minimum_cp=200), 'contradicts approval')

    def test_resources_6(self):
        cases = [
            ('test_boolean_is_not_price', 'service-price-references', lambda d: d['approved_references'][0].update(minimum_cp=True), 'contradicts approval'),
            ('test_postal_methods_cannot_imply_instant_network', 'settlement-communications', lambda d: d['methods'][0].update(id='instant-network'), 'unsupported method'),
            ('test_postal_template_cannot_claim_delivery', 'settlement-communications', lambda d: d['message_template'].update(actual_delivery_status='delivered'), 'empty template'),
            ('test_no_completed_message_records', 'settlement-communications', lambda d: d['messages'].append({'status': 'delivered'}), 'cannot dispatch/deliver'),
            ('test_template_cannot_imply_fee_or_carrier', 'settlement-communications', lambda d: d['message_template'].update(delivery_fee_cp=0), 'populated message template'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)


class FutureDispatchShapeTests(unittest.TestCase):
    """Synthetic inputs only; no repository records or messages are written."""
    def setUp(self):
        self.message=dict(id='fixture-message', sender='fixture-sender', recipient='fixture-recipient',
                          carrier='fixture-carrier', method='mounted-courier', departure_date='Year 848 Day 182',
                          departure_time='08:00', origin='fixture-a', destination='fixture-b',
                          intended_route_ids=['fixture-route'], delivery_fee_cp=10,
                          estimated_delivery_window=dict(earliest=None, latest=None, basis='Timing unverified; await carrier estimate'),
                          actual_delivery_status='sent', receipt_evidence=[],
                          dispatch_evidence=[dict(source_ref='fixture.md', quote='Carrier departed', date='Year 848 Day 182')],
                          spell_rule_ref=None, resource_evidence=[], source_ref='fixture.md')
        self.routes={'fixture-route':dict(start='fixture-a', destination='fixture-b', classification='CONFIRMED CANON',
                                          bidirectional=True, reverse_status='PROPOSED', accessibility=dict(riding=True))}

    def require(self, condition, message):
        if not condition:raise ValueError(message)

    def check(self): validate_dispatch(self.message, self.routes, self.require)


    def test_causality_and_contracts_and_schema_and_identity_1(self):
        with self.subTest(case='test_no_automatic_receipt_from_send'), isolated_case(self):
            self.message['actual_delivery_status']='delivered'
            self.message['receipt_evidence']=self.message['dispatch_evidence']
            with self.assertRaisesRegex(ValueError, 'sending is not delivery'):self.check()
        with self.subTest(case='test_physical_dispatch_cannot_use_proposed_route'), isolated_case(self):
            self.routes['fixture-route']['classification']='PROPOSED'
            with self.assertRaisesRegex(ValueError, 'not operational'):self.check()
        with self.subTest(case='test_dispatch_cannot_infer_reverse_verification'), isolated_case(self):
            self.message.update(origin='fixture-b',destination='fixture-a')
            with self.assertRaisesRegex(ValueError, 'unverified reverse'):self.check()
        with self.subTest(case='test_sourced_send_is_separate_from_receipt'), isolated_case(self):
            self.check()
            self.message['actual_delivery_status']='delivered'
            with self.assertRaisesRegex(ValueError, 'independent receipt'):self.check()
        with self.subTest(case='test_dispatch_needs_named_carrier'), isolated_case(self):
            self.message['carrier']=None
            with self.assertRaisesRegex(ValueError, 'requires sender'):self.check()

    def test_identity_and_resources_2(self):
        with self.subTest(case='test_magic_needs_existing_rule_and_resource_evidence'), isolated_case(self):
            self.message['method']='limited-magic';self.message['intended_route_ids']=[]
            with self.assertRaisesRegex(ValueError, 'finite-resource'):self.check()
        with self.subTest(case='test_method_needs_route_compatibility'), isolated_case(self):
            self.routes['fixture-route']['accessibility']['riding']=None
            with self.assertRaisesRegex(ValueError, 'method compatibility'):self.check()
