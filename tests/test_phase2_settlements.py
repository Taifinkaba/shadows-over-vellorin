"""Approved settlement design must not create current conditions or gameplay."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

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
        with self.assertRaisesRegex(ValidationError, pattern): validate(self.root)

    def test_all_ten_populations_and_households(self):
        self.assertIn('checkpoint valid', validate(self.root))
        for ident, amount in POPULATIONS.items():
            d = self.data(ident)['approved_design']
            self.assertEqual(d['population']['amount'], amount)
            self.assertEqual(d['population']['classification'], 'CONFIRMED CANON' if ident=='brackenford' else 'APPROVED DESIGN')
            self.assertIsNone(d['current_conditions'])
            self.assertEqual(d['events'], [])
            if ident != 'brackenford': self.assertIsNone(d['households'])
        self.assertEqual(self.data('brackenford')['approved_design']['households']['amount'], 42)

    def test_legacy_payloads_and_unrelated_history_preserved(self):
        f = json.loads((ROOT/'tests/fixtures/phase2-02-preservation.json').read_text())
        for path, digest in f['unchanged_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), digest, path)
        for path, revision in f['authorized_owner_revisions'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), revision['after_sha256'], path)
        for path, legacy in f['legacy_settlement_payloads'].items():
            current = json.loads(re.search(r'```json\n(.*?)\n```', (ROOT/path).read_text(), re.S)[1])
            current.pop('approved_design', None)
            self.assertEqual(current, legacy, path)

    def test_population_is_not_census(self):
        self.reject('caelthorne', lambda d:d['approved_design']['population'].update(classification='CONFIRMED CANON'), 'classification/qualification')

    def test_population_cannot_change(self):
        self.reject('silverbrook', lambda d:d['approved_design']['population'].update(amount=420), 'population contradicts')

    def test_population_requires_approval_source(self):
        self.reject('windmere', lambda d:d['approved_design']['population'].update(source_ref='README.md'), 'wrong approval provenance')

    def test_no_unsupported_household_counts(self):
        self.reject('stoneford', lambda d:d['approved_design'].update(households=100), 'unsupported household')

    def test_registry_cannot_omit_settlement(self):
        self.reject('settlement-services', lambda d:d['approved_design_location_ids'].pop(), 'ten-settlement coverage')

    def test_new_settlement_cannot_gain_unapproved_realm(self):
        self.reject('world-geography', lambda d:next(n for n in d['nodes'] if n['id']=='windmere')['parents'][0].update(id='valedorn'), 'unsupported realm/parent')

    def test_no_duplicate_business_design_ids(self):
        self.reject('eastrun', lambda d:d['approved_design']['businesses'].append(copy.deepcopy(d['approved_design']['businesses'][0])), 'duplicate or wrong business')

    def test_known_brackenford_business_is_reference_not_duplicate(self):
        b = self.data('brackenford'); a = b['approved_design']
        self.assertEqual({x['existing_business_ref'] for x in a['businesses']}, {x['id'] for x in b['businesses']})
        self.assertEqual(b['principal_official_id'], 'elsbeth-marrin')
        self.assertEqual(b['watch_official_id'], 'ressa-vale')
        self.assertEqual(b['businesses'][0]['operator_id'], 'mara-fenwick')

    def test_design_does_not_appoint_owner(self):
        self.reject('eastrun', lambda d:d['approved_design']['businesses'][0].update(owner_id='theron-ashvale'), 'invented ownership')

    def test_design_cannot_certify_license(self):
        self.reject('rivermere', lambda d:d['approved_design']['businesses'][0].update(current_license='royal'), 'invented ownership')

    def test_design_cannot_create_stock_or_cash(self):
        self.reject('windmere', lambda d:d['approved_design']['businesses'][0].update(cash_balance_cp=100), 'stock or cash')

    def test_adult_venue_requires_adult_workers(self):
        self.reject('caelthorne', lambda d:next(b for b in d['approved_design']['businesses'] if 'brothel' in b['categories']).update(adult_workers_only=False), 'adult consent/regulation')

    def test_adult_venue_requires_agency(self):
        self.reject('rivermere', lambda d:next(b for b in d['approved_design']['businesses'] if 'brothel' in b['categories']).update(worker_agency='Bound workers'), 'agency safeguards')

    def test_business_legal_design_is_not_enacted_license(self):
        self.reject('caelthorne', lambda d:d['approved_design']['businesses'][0].update(legal_design='licensed'), 'legal classification')

    def test_no_faction_or_mystery_connections(self):
        self.reject('briarfall-crossing', lambda d:d['approved_design']['criminal_faction_refs'].append('Crown-07'), 'PR4 faction records')

    def test_illegal_context_cannot_be_active_crime(self):
        self.reject('caelthorne', lambda d:d['approved_design']['unlawful_activity_designs'][0]['events'].append('theft'), 'active crimes')

    def test_trade_cannot_post_shipments(self):
        self.reject('settlement-trade', lambda d:d['relationships'][0]['actual_shipments'].append('shipment1'), 'completed commerce')

    def test_trade_requires_compatible_endpoint_dependency(self):
        self.reject('settlement-trade', lambda d:d['relationships'][0].update(route_dependencies=['route-brackenford-cottage']), 'does not connect trade')

    def test_trade_requires_origin_supplier(self):
        self.reject('settlement-trade', lambda d:d['relationships'][0].update(supplier_industry_id='windmere:industry-pastoral'), 'supplier does not belong')

    def test_trade_does_not_invent_missing_river_route(self):
        d = next(d for d in self.data('settlement-trade')['relationships'] if d['origin']=='southbank-landing')
        self.assertEqual(d['route_dependencies'], [])
        self.assertIn('No compatible surveyed', d['unresolved_operational_details'])
        self.assertEqual(d['verification_status'], 'UNVERIFIED PROPOSAL')

    def test_prices_are_baselines_not_quotes(self):
        self.reject('service-price-references', lambda d:d['approved_references'][0].update(kind='current-verified-quote'), 'not a quote/charge')

    def test_price_or_wage_cannot_disagree_with_approval(self):
        self.reject('service-price-references', lambda d:d['approved_references'][-1].update(minimum_cp=200), 'contradicts approval')

    def test_boolean_is_not_price(self):
        self.reject('service-price-references', lambda d:d['approved_references'][0].update(minimum_cp=True), 'contradicts approval')

    def test_postal_methods_cannot_imply_instant_network(self):
        self.reject('settlement-communications', lambda d:d['methods'][0].update(id='instant-network'), 'unsupported method')

    def test_postal_template_cannot_claim_delivery(self):
        self.reject('settlement-communications', lambda d:d['message_template'].update(actual_delivery_status='delivered'), 'empty template')

    def test_no_completed_message_records(self):
        self.reject('settlement-communications', lambda d:d['messages'].append({'status':'delivered'}), 'cannot dispatch/deliver')

    def test_template_cannot_imply_fee_or_carrier(self):
        self.reject('settlement-communications', lambda d:d['message_template'].update(delivery_fee_cp=0), 'populated message template')

    def test_partial_extension_is_rejected(self):
        p = self.root/'index.json'; d=json.loads(p.read_text())
        d['entries']=[e for e in d['entries'] if e['id']!='settlement-trade'];p.write_text(json.dumps(d))
        (self.root/'entities/mechanics/settlement-trade.md').unlink()
        with self.assertRaisesRegex(ValidationError, 'incomplete trade/postal'):validate(self.root)


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

    def test_sourced_send_is_separate_from_receipt(self):
        self.check()
        self.message['actual_delivery_status']='delivered'
        with self.assertRaisesRegex(ValueError, 'independent receipt'):self.check()

    def test_no_automatic_receipt_from_send(self):
        self.message['actual_delivery_status']='delivered'
        self.message['receipt_evidence']=self.message['dispatch_evidence']
        with self.assertRaisesRegex(ValueError, 'sending is not delivery'):self.check()

    def test_physical_dispatch_cannot_use_proposed_route(self):
        self.routes['fixture-route']['classification']='PROPOSED'
        with self.assertRaisesRegex(ValueError, 'not operational'):self.check()

    def test_method_needs_route_compatibility(self):
        self.routes['fixture-route']['accessibility']['riding']=None
        with self.assertRaisesRegex(ValueError, 'method compatibility'):self.check()

    def test_dispatch_cannot_infer_reverse_verification(self):
        self.message.update(origin='fixture-b',destination='fixture-a')
        with self.assertRaisesRegex(ValueError, 'unverified reverse'):self.check()

    def test_dispatch_needs_named_carrier(self):
        self.message['carrier']=None
        with self.assertRaisesRegex(ValueError, 'requires sender'):self.check()

    def test_magic_needs_existing_rule_and_resource_evidence(self):
        self.message['method']='limited-magic';self.message['intended_route_ids']=[]
        with self.assertRaisesRegex(ValueError, 'finite-resource'):self.check()
