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
        for name in ('entities', 'archive', 'state', 'changes'):
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
            validate(self.root)

    def test_current_profiles_and_counts(self):
        self.assertIn('checkpoint valid',validate(self.root))
        ids = self.data('settlement-services')['location_ids']
        self.assertEqual(len(ids),11)
        businesses = [b for i in ids for b in self.data(i)['businesses']]
        self.assertEqual(len(businesses),14)
        self.assertTrue(all(b['classification']=='CONFIRMED CANON' for b in businesses))
        self.assertEqual(len(self.data('service-price-references')['reference_bands']),6)

    def test_duplicate_settlement_id(self):
        self.reject('settlement-services',lambda d:d['location_ids'].append(d['location_ids'][0]),'duplicate settlement IDs')

    def test_missing_profile_routing(self):
        self.reject('settlement-services',lambda d:d['location_ids'].pop(),'coverage mismatch')

    def test_duplicate_business_id(self):
        self.reject('brackenford',lambda d:d['businesses'].append(d['businesses'][0]),'duplicate business ID')

    def test_business_parent_must_match(self):
        self.reject('brackenford',lambda d:d['businesses'][0].update(parent_location_id='eastrun'),'parent mismatch')

    def test_business_scoped_to_real_parent(self):
        self.reject('brackenford',lambda d:d['businesses'][0].update(id='missing-town:inn'),'parent-scoped business ID')

    def test_profile_identity_matches_entity(self):
        self.reject('eastrun',lambda d:d.update(location_id='brackenford'),'ID does not match owner')

    def test_broken_region_reference(self):
        self.reject('eastrun',lambda d:d.update(region_id='invented-region'),'broken entity reference')

    def test_route_cannot_be_nation(self):
        self.reject('eastrun',lambda d:d.update(nation_id='route-ashvale-eastrun'),'route cannot be parent')

    def test_invalid_route_reference(self):
        self.reject('eastrun',lambda d:d['route_ids'].append('missing-road'),'broken entity reference')

    def test_unrelated_road_not_local(self):
        self.reject('eastrun',lambda d:d['route_ids'].append('route-brackenford-cottage'),'does not connect parent')

    def test_no_route_promotion_or_state_change_by_validation(self):
        paths = [p for folder in ('state','entities/characters','entities/creatures','entities/items','entities/quests','entities/factions') for p in (self.root/folder).rglob('*') if p.is_file()]
        paths += list((self.root/'entities/locations').glob('route-*.md'))
        before = {p:p.read_bytes() for p in paths}
        validate(self.root)
        self.assertEqual(before,{p:p.read_bytes() for p in paths})

    def test_proposed_profile_not_silently_canon(self):
        self.reject('eastrun',lambda d:d.update(classification='PROPOSED'),'proposed/canon location mismatch')

    def test_bad_business_classification(self):
        self.reject('brackenford',lambda d:d['businesses'][0].update(classification='APPROVED'),'invalid classification')

    def test_unknown_owner_price_and_stock_are_valid(self):
        b = self.data('brackenford')['businesses'][0]
        self.assertIsNone(b['owner_id'])
        self.assertEqual(b['operator_id'],'mara-fenwick')
        self.assertEqual(b['prices'],[])
        self.assertIsNone(b['stock_counts'])
        self.assertIsNone(b['accepted_currency'])
        self.assertIn('checkpoint valid',validate(self.root))

    def test_unknown_operator_does_not_imply_property_owner(self):
        self.reject('brackenford',lambda d:d['businesses'][0].update(owner_id='mara-fenwick'),'operator is not a verified property owner')

    def test_tomas_cannot_be_replaced(self):
        self.reject('ashvale-estate',lambda d:d['businesses'][0].update(manager_id='bren'),'ownership/management changed')

    def test_property_owner_cannot_change(self):
        self.reject('ashvale-lodge',lambda d:d['businesses'][0].update(owner_id='edrick-sorn'),'ownership/management changed')

    def test_municipal_authority_cannot_be_claimed(self):
        self.reject('brackenford',lambda d:d.update(principal_official_id='theron-ashvale'),'village authority changed')

    def test_population_not_invented(self):
        self.reject('eastrun',lambda d:d.update(population=dict(amount=10000,qualifier='approximately')),'population not supported')

    def test_existing_population_cannot_change(self):
        self.reject('brackenford',lambda d:d['population'].update(amount=10000),'population not supported')

    def test_bad_source_path(self):
        self.reject('brackenford',lambda d:d['businesses'][0]['source_refs'].append('../elsewhere.md'),'repository-relative')

    def test_missing_source(self):
        self.reject('brackenford',lambda d:d['businesses'][0]['source_refs'].append('not-real.md'),'missing file')

    def test_cannot_self_certify_new_claim_with_appended_evidence(self):
        def change(d):
            d['businesses'][0]['evidence'][0]['quote']='This merchant has now gifted Theron a thousand gold.'
        self.reject('brackenford',change,'quote not found in original source')

    def test_no_automatic_financial_postings(self):
        self.reject('ashvale-estate',lambda d:d['businesses'][0].update(automatic_financial_postings=True),'automatic financial postings forbidden')

    def test_no_automatic_registry_income(self):
        self.reject('settlement-services',lambda d:d.update(automatic_financial_postings=True),'automatic financial postings forbidden')

    def test_archived_prices_stay_proposed(self):
        self.reject('service-price-references',lambda d:d['reference_bands'][0].update(classification='CONFIRMED CANON'),'design price not approved')

    def test_archived_band_cannot_be_current_quote(self):
        self.reject('service-price-references',lambda d:d['reference_bands'][0].update(kind='current-verified-quote'),'design price not approved')

    def test_integer_copper_range(self):
        for amount in (-1,True,2.5):
            with self.subTest(amount=amount):
                self.edit('service-price-references',lambda d:d['reference_bands'][0].update(minimum_cp=amount))
                with self.assertRaisesRegex(ValidationError,'integer-copper'):
                    validate(self.root)

    def test_reversed_price_range(self):
        self.reject('service-price-references',lambda d:d['reference_bands'][0].update(minimum_cp=100),'integer-copper')

    def test_price_conversion_from_archived_source(self):
        self.reject('service-price-references',lambda d:d['reference_bands'][1].update(minimum_cp=100,maximum_cp=300),'source conversion')

    def test_wrong_gold_conversion(self):
        self.reject('service-price-references',lambda d:d['currency'].update(cp_per_gp=1000),'currency must be100cp')

    def test_historical_cost_not_repriced(self):
        self.reject('ashvale-lodge',lambda d:d['businesses'][1]['prices'][0].update(minimum_cp=7300,maximum_cp=7300),'paid price contradicts')

    def test_historical_construction_not_new_shop_quote(self):
        self.reject('ashvale-lodge',lambda d:d['businesses'][1]['prices'][0].update(kind='current-verified-quote'),'new quote or approved price')

    def test_invented_counted_stock(self):
        self.reject('brackenford',lambda d:d['businesses'][1].update(stock_counts={'legendary_swords':50}),'no counted stock verified')

    def test_no_invented_deliveries(self):
        self.reject('ashvale-estate',lambda d:d['businesses'][0]['supplier_relationships'].append({'arrived':True}),'no verified supply contract')

    def test_category_not_event(self):
        self.reject('local-settlement-activity',lambda d:d['events'].append({'kind':'medical-emergency','completed':True}),'cannot trigger events')

    def test_no_automatic_progression(self):
        self.reject('local-settlement-activity',lambda d:d.update(automatic_progression=True),'cannot trigger events')

    def test_broken_scoped_service_link(self):
        self.reject('ashvale-estate',lambda d:d['service_links'].append('eastrun:invented-shop'),'broken scoped business link')

    def test_partial_framework_fails(self):
        path = self.root/'index.json'
        idx = json.loads(path.read_text())
        idx['entries'] = [e for e in idx['entries'] if e['id']!='local-settlement-activity']
        path.write_text(json.dumps(idx))
        (self.root/'entities/mechanics/local-settlement-activity.md').unlink()
        with self.assertRaisesRegex(ValidationError,'missing routing, price or activity'):
            validate(self.root)

    def test_optimized_validator_rejects_bad_business_parent(self):
        self.edit('brackenford',lambda d:d['businesses'][0].update(parent_location_id='eastrun'))
        result = subprocess.run([sys.executable,'-O',str(ROOT/'scripts/validate.py'),'--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(result.returncode,1)
        self.assertIn('business parent mismatch',result.stderr)

    def test_preexisting_source_state_staff_and_property_prose_preserved(self):
        fixture = json.loads((ROOT/'tests/fixtures/chunk3-preservation.json').read_text())
        for path, digest in fixture['protected_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        for path, digest in fixture['source_prefix_sha256'].items():
            prefix = (ROOT/path).read_text().split(MARKER)[0].encode()
            self.assertEqual(hashlib.sha256(prefix).hexdigest(),digest,path)

    def test_inn_capacity_not_current_vacancy_or_arbitrary_count(self):
        self.reject('brackenford',lambda d:d['businesses'][0]['capacity'].update(amount=50),'inn capacity contradicts')

    def test_storage_capacity_preserved(self):
        self.reject('ashvale-estate',lambda d:d['businesses'][1]['capacity'].update(amount=50),'storage capacity contradicts')

    def test_existing_operator_cannot_be_replaced(self):
        self.reject('brackenford',lambda d:d['businesses'][0].update(operator_id='borin-emberhand'),'established operator changed')

    def test_miller_not_assigned_to_unverified_specific_premises(self):
        self.reject('brackenford',lambda d:d['businesses'][3].update(operator_id='harlan-wicks'),'new assignment inferred')
