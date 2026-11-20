from case_support import isolated_case, validate_scope
"""Settlement mutations exercise unknowns, evidence, routing and maintenance boundaries."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate import ValidationError, validate
from scripts.settlements import MARKER

ROOT = Path(__file__).resolve().parents[1]


class SettlementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-settlements-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('entities', 'archive', 'state', 'changes', 'docs', 'governance'):
            shutil.copytree(ROOT/name, self.root/name)
        shutil.copy2(ROOT/'index.json', self.root/'index.json')

    def path(self, ident):
        kind = 'mechanics' if ident in {'settlement-services','service-price-references','local-settlement-activity'} else 'locations'
        return self.root/f'entities/{kind}/{ident}.md'

    def edit(self, ident, change):
        p = self.path(ident)
        source = p.read_text()
        m = re.search(r'```json\n(.*?)\n```',source,re.S)
        data = json.loads(m[1])
        change(data)
        p.write_text(source[:m.start(1)]+json.dumps(data,indent=2,ensure_ascii=False)+source[m.end(1):])

    def data(self, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def reject(self, ident, change, pattern):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,pattern):
            validate_scope(self.root, 'settlements', 'settlement_expansion')


    def test_causality_1(self):
        with self.subTest(case='test_route_cannot_be_nation'), isolated_case(self):
            self.reject('eastrun',lambda d:d.update(nation_id='route-ashvale-eastrun'),'route cannot be parent')
        with self.subTest(case='test_no_route_promotion_or_state_change_by_validation'), isolated_case(self):
            paths = [p for folder in ('state','entities/characters','entities/creatures','entities/items','entities/quests','entities/factions') for p in (self.root/folder).rglob('*') if p.is_file()]
            paths += list((self.root/'entities/locations').glob('route-*.md'))
            before = {p:p.read_bytes() for p in paths}
            validate(self.root)
            self.assertEqual(before,{p:p.read_bytes() for p in paths})
        with self.subTest(case='test_no_automatic_financial_postings'), isolated_case(self):
            self.reject('ashvale-estate',lambda d:d['businesses'][0].update(automatic_financial_postings=True),'automatic financial postings forbidden')
        with self.subTest(case='test_no_automatic_registry_income'), isolated_case(self):
            self.reject('settlement-services',lambda d:d.update(automatic_financial_postings=True),'automatic financial postings forbidden')
        with self.subTest(case='test_category_not_event'), isolated_case(self):
            self.reject('local-settlement-activity',lambda d:d['events'].append({'kind':'medical-emergency','completed':True}),'cannot trigger events')

    def test_causality_and_continuity_and_contracts_and_schema_2(self):
        with self.subTest(case='test_no_automatic_progression'), isolated_case(self):
            self.reject('local-settlement-activity',lambda d:d.update(automatic_progression=True),'cannot trigger events')
        with self.subTest(case='test_current_profiles_and_counts'), isolated_case(self):
            self.assertIn('checkpoint valid',validate(self.root))
            ids = self.data('settlement-services')['location_ids']
            self.assertEqual(len(ids),11)
            businesses = [b for i in ids for b in self.data(i)['businesses']]
            self.assertEqual(len(businesses),14)
            self.assertTrue(all(b['classification']=='CONFIRMED CANON' for b in businesses))
            self.assertEqual(len(self.data('service-price-references')['reference_bands']),6)
        with self.subTest(case='test_inn_capacity_not_current_vacancy_or_arbitrary_count'), isolated_case(self):
            self.reject('brackenford',lambda d:d['businesses'][0]['capacity'].update(amount=50),'inn capacity contradicts')
        with self.subTest(case='test_storage_capacity_preserved'), isolated_case(self):
            self.reject('ashvale-estate',lambda d:d['businesses'][1]['capacity'].update(amount=50),'storage capacity contradicts')
        with self.subTest(case='test_missing_profile_routing'), isolated_case(self):
            self.reject('settlement-services',lambda d:d['location_ids'].pop(),'coverage mismatch')

    def test_contracts_and_schema_3(self):
        cases = [
            ('test_business_parent_must_match', 'brackenford', lambda d: d['businesses'][0].update(parent_location_id='eastrun'), 'parent mismatch'),
            ('test_business_scoped_to_real_parent', 'brackenford', lambda d: d['businesses'][0].update(id='missing-town:inn'), 'parent-scoped business ID'),
            ('test_unrelated_road_not_local', 'eastrun', lambda d: d['route_ids'].append('route-brackenford-cottage'), 'does not connect parent'),
            ('test_proposed_profile_not_silently_canon', 'eastrun', lambda d: d.update(classification='PROPOSED'), 'proposed/canon location mismatch'),
            ('test_bad_business_classification', 'brackenford', lambda d: d['businesses'][0].update(classification='APPROVED'), 'invalid classification'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_4(self):
        with self.subTest(case='test_tomas_cannot_be_replaced'), isolated_case(self):
            self.reject('ashvale-estate',lambda d:d['businesses'][0].update(manager_id='bren'),'ownership/management changed')
        with self.subTest(case='test_municipal_authority_cannot_be_claimed'), isolated_case(self):
            self.reject('brackenford',lambda d:d.update(principal_official_id='theron-ashvale'),'village authority changed')
        with self.subTest(case='test_population_not_invented'), isolated_case(self):
            self.reject('eastrun',lambda d:d.update(population=dict(amount=10000,qualifier='approximately')),'population not supported')
        with self.subTest(case='test_existing_population_cannot_change'), isolated_case(self):
            self.reject('brackenford',lambda d:d['population'].update(amount=10000),'population not supported')
        with self.subTest(case='test_cannot_self_certify_new_claim_with_appended_evidence'), isolated_case(self):
            def change(d):
                d['businesses'][0]['evidence'][0]['quote']='This merchant has now gifted Theron a thousand gold.'
            self.reject('brackenford',change,'quote not found in original source')

    def test_contracts_and_schema_5(self):
        with self.subTest(case='test_wrong_gold_conversion'), isolated_case(self):
            self.reject('service-price-references',lambda d:d['currency'].update(cp_per_gp=1000),'currency must be100cp')
        with self.subTest(case='test_no_invented_deliveries'), isolated_case(self):
            self.reject('ashvale-estate',lambda d:d['businesses'][0]['supplier_relationships'].append({'arrived':True}),'no verified supply contract')
        with self.subTest(case='test_broken_scoped_service_link'), isolated_case(self):
            self.reject('ashvale-estate',lambda d:d['service_links'].append('eastrun:invented-shop'),'broken scoped business link')
        with self.subTest(case='test_partial_framework_fails'), isolated_case(self):
            path = self.root/'index.json'
            idx = json.loads(path.read_text())
            idx['entries'] = [e for e in idx['entries'] if e['id']!='local-settlement-activity']
            path.write_text(json.dumps(idx))
            (self.root/'entities/mechanics/local-settlement-activity.md').unlink()
            with self.assertRaisesRegex(ValidationError,'missing routing, price or activity'):
                validate(self.root)
        with self.subTest(case='test_optimized_validator_rejects_bad_business_parent'), isolated_case(self):
            self.edit('brackenford',lambda d:d['businesses'][0].update(parent_location_id='eastrun'))
            result = subprocess.run([sys.executable,'-O',str(ROOT/'scripts/validate.py'),'--root',str(self.root)],capture_output=True,text=True)
            self.assertEqual(result.returncode,1)
            self.assertIn('business parent mismatch',result.stderr)

    def test_contracts_and_schema_and_identity_6(self):
        cases = [
            ('test_existing_operator_cannot_be_replaced', 'brackenford', lambda d: d['businesses'][0].update(operator_id='borin-emberhand'), 'established operator changed'),
            ('test_miller_not_assigned_to_unverified_specific_premises', 'brackenford', lambda d: d['businesses'][3].update(operator_id='harlan-wicks'), 'new assignment inferred'),
            ('test_duplicate_settlement_id', 'settlement-services', lambda d: d['location_ids'].append(d['location_ids'][0]), 'duplicate settlement IDs'),
            ('test_duplicate_business_id', 'brackenford', lambda d: d['businesses'].append(d['businesses'][0]), 'duplicate business ID'),
            ('test_profile_identity_matches_entity', 'eastrun', lambda d: d.update(location_id='brackenford'), 'ID does not match owner'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_identity_7(self):
        with self.subTest(case='test_broken_region_reference'), isolated_case(self):
            self.reject('eastrun',lambda d:d.update(region_id='invented-region'),'broken entity reference')
        with self.subTest(case='test_invalid_route_reference'), isolated_case(self):
            self.reject('eastrun',lambda d:d['route_ids'].append('missing-road'),'broken entity reference')
        with self.subTest(case='test_unknown_owner_price_and_stock_are_valid'), isolated_case(self):
            b = self.data('brackenford')['businesses'][0]
            self.assertIsNone(b['owner_id'])
            self.assertEqual(b['operator_id'],'mara-fenwick')
            self.assertEqual(b['prices'],[])
            self.assertIsNone(b['stock_counts'])
            self.assertIsNone(b['accepted_currency'])
            self.assertIn('checkpoint valid',validate(self.root))
        with self.subTest(case='test_unknown_operator_does_not_imply_property_owner'), isolated_case(self):
            self.reject('brackenford',lambda d:d['businesses'][0].update(owner_id='mara-fenwick'),'operator is not a verified property owner')
        with self.subTest(case='test_property_owner_cannot_change'), isolated_case(self):
            self.reject('ashvale-lodge',lambda d:d['businesses'][0].update(owner_id='edrick-sorn'),'ownership/management changed')

    def test_identity_8(self):
        cases = [
            ('test_bad_source_path', 'brackenford', lambda d: d['businesses'][0]['source_refs'].append('../elsewhere.md'), 'repository-relative'),
            ('test_missing_source', 'brackenford', lambda d: d['businesses'][0]['source_refs'].append('not-real.md'), 'missing file'),
            ('test_archived_band_cannot_be_current_quote', 'service-price-references', lambda d: d['reference_bands'][0].update(kind='current-verified-quote'), 'design price not approved'),
            ('test_price_conversion_from_archived_source', 'service-price-references', lambda d: d['reference_bands'][1].update(minimum_cp=100, maximum_cp=300), 'source conversion'),
            ('test_historical_construction_not_new_shop_quote', 'ashvale-lodge', lambda d: d['businesses'][1]['prices'][0].update(kind='current-verified-quote'), 'new quote or approved price'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_identity_and_resources_9(self):
        with self.subTest(case='test_preexisting_source_state_staff_and_property_prose_preserved'), isolated_case(self):
            fixture = json.loads((ROOT/'tests/fixtures/chunk3-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path, digest in fixture['source_prefix_sha256'].items():
                prefix = (ROOT/path).read_text().split(MARKER)[0]
                prefix = prefix.replace('- changes/chronicles/year848-suncrest262-end-session.md\n', '', 1)
                prefix = re.sub(r'\n## Year 848, Suncrest 262 update\n.*?\n## Earlier record\n',
                                '', prefix, count=1, flags=re.S)
                self.assertEqual(hashlib.sha256(prefix.encode()).hexdigest(),digest,path)
        with self.subTest(case='test_archived_prices_stay_proposed'), isolated_case(self):
            self.reject('service-price-references',lambda d:d['reference_bands'][0].update(classification='CONFIRMED CANON'),'design price not approved')
        with self.subTest(case='test_integer_copper_range'), isolated_case(self):
            for amount in (-1,True,2.5):
                with self.subTest(amount=amount):
                    self.edit('service-price-references',lambda d:d['reference_bands'][0].update(minimum_cp=amount))
                    with self.assertRaisesRegex(ValidationError,'integer-copper'):
                        validate(self.root)
        with self.subTest(case='test_reversed_price_range'), isolated_case(self):
            self.reject('service-price-references',lambda d:d['reference_bands'][0].update(minimum_cp=100),'integer-copper')
        with self.subTest(case='test_historical_cost_not_repriced'), isolated_case(self):
            self.reject('ashvale-lodge',lambda d:d['businesses'][1]['prices'][0].update(minimum_cp=7300,maximum_cp=7300),'paid price contradicts')

    def test_resources_10(self):
        cases = [
            ('test_invented_counted_stock', 'brackenford', lambda d: d['businesses'][1].update(stock_counts={'legendary_swords': 50}), 'no counted stock verified'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)
