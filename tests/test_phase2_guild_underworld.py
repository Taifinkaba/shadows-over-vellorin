from case_support import isolated_case, validate_scope
"""Guild and underworld designs must not create membership, covert truth or money."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.validate import ValidationError,validate
from scripts.guild_underworld import GUILDS,CRIMINAL,DUES

ROOT=Path(__file__).resolve().parents[1]


class GuildUnderworldTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-guild-underworld-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):
        kind='factions' if ident in set(GUILDS)|set(CRIMINAL)|{'continental-guild-concord'} else 'rules' if ident=='guild-membership-and-contracts' else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self,ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,change):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,ident,change,pattern):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,pattern):validate_scope(self.root, 'guild_underworld')


    def test_causality_and_continuity_and_contracts_and_schema_1(self):
        with self.subTest(case='test_master_is_not_automatic_combat_rank'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules'].update(automatic_combat_rank_equivalence=True),'distinct from combat')
        with self.subTest(case='test_no_current_guildmaster'), isolated_case(self):
            self.reject('scribes-collegium',lambda d:d['organization_design'].update(actual_leaders=['mara-vey']),'stay unknown')
        with self.subTest(case='test_no_current_supplier'), isolated_case(self):
            self.reject('illicit-commerce-design',lambda d:d['contexts'][0].update(current_seller='secret supplier'),'stay unknown')
        with self.subTest(case='test_no_historical_dues_posting'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['actual_dues_events'].append('paid'),'no actual memberships')
        with self.subTest(case='test_six_guilds_eight_criminal_designs_and_scopes'), isolated_case(self):
            self.assertIn('checkpoint valid',validate(self.root))
            for ident,(archive,scope) in GUILDS.items():
                d=self.data(ident)['organization_design'];self.assertEqual(d['archived_design_id'],archive)
                self.assertEqual(d['association_location_id'],scope);self.assertTrue(d['independent'])
                self.assertEqual(d['kind'],'professional-guild')
            for ident,(name,scope) in CRIMINAL.items():
                d=self.data(ident)['organization_design'];self.assertEqual((d['name'],d['association_location_id']),(name,scope))
                self.assertIsNone(d['current_leaders']);self.assertIsNone(d['current_funds_cp'])
                self.assertEqual(d['actual_crimes'],[])

    def test_contracts_and_schema_2(self):
        cases = [
            ('test_profile_needs_approval_provenance', 'ironhand-smiths-compact', lambda d: d['organization_design'].update(approval_source_ref='README.md'), 'wrong approval'),
            ('test_guild_cannot_merge_with_government', 'river-charter-league', lambda d: d['organization_design'].update(association_location_id='rivermere-league'), 'identity/region'),
            ('test_professional_guild_is_independent', 'greenward-covenant', lambda d: d['organization_design'].update(compulsory_concord_membership=True), 'independence'),
            ('test_branch_context_cannot_be_road', 'stonewatch-wardens', lambda d: d['organization_design']['branch_designs'][0].update(candidate_context_id='route-waystation-brackenford'), 'route is not'),
            ('test_branch_design_cannot_open', 'circle-of-seven-lamps', lambda d: d['organization_design']['branch_designs'][0].update(operational_status='OPEN'), 'not operating'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_3(self):
        with self.subTest(case='test_no_new_guild_members'), isolated_case(self):
            self.reject('ironhand-smiths-compact',lambda d:d['organization_design']['actual_memberships'].append('Theron'),'no actual memberships')
        with self.subTest(case='test_prospective_annual_dues_and_professional_ranks'), isolated_case(self):
            r=self.data('guild-membership-and-contracts')['approved_professional_rules']
            self.assertEqual({d['membership']:d['amount_cp'] for d in r['annual_dues_references']},DUES)
            self.assertEqual(r['professional_certification_levels'],['apprentice','journeyman','master'])
            self.assertFalse(r['traveling_member_is_rank']);self.assertFalse(r['automatic_combat_rank_equivalence'])
            self.assertNotIn('dragon-slayer-academy',r['applies_to_guild_ids'])
        with self.subTest(case='test_dues_cannot_disagree_with_approval'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['annual_dues_references'][0].update(amount_cp=200),'annual references')
        with self.subTest(case='test_dues_are_annual_not_monthly'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['annual_dues_references'][0].update(period='month'),'annual references')
        with self.subTest(case='test_no_academy_dues'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['applies_to_guild_ids'].append('dragon-slayer-academy'),'dues cannot apply')

    def test_contracts_and_schema_4(self):
        cases = [
            ('test_concord_requires_voluntary_membership_and_exit', 'continental-guild-concord', lambda d: d['approved_charter'].update(independent_exit=False), 'must be voluntary'),
            ('test_no_concord_treasury_consolidation', 'continental-guild-concord', lambda d: d['approved_charter'].update(treasury_consolidation=True), 'no Concord takeover'),
            ('test_no_academy_takeover', 'continental-guild-concord', lambda d: d['approved_charter'].update(academy_takeover=True), 'no Concord takeover'),
            ('test_no_actual_concord_enrollment', 'continental-guild-concord', lambda d: d['approved_charter']['actual_enrollments'].append('wayfarers-guild'), 'no actual memberships'),
            ('test_transregional_is_not_verified_reach', 'veiled-coin-exchange', lambda d: d['organization_design'].update(current_presence=['caelthorne']), 'stay unknown'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_5(self):
        cases = [
            ('test_no_confidential_informant', 'thornless-circle', lambda d: d['organization_design'].update(current_informants=['named witness']), 'stay unknown'),
            ('test_no_active_crime_or_plot', 'sable-current', lambda d: d['organization_design']['actual_operations'].append('smuggling'), 'no actual memberships'),
            ('test_no_unsupported_mystery_connection', 'broken-seal-society', lambda d: d['organization_design']['unsupported_mystery_connections'].append('Crown-07'), 'secret outcomes'),
            ('test_no_new_magic_authority', 'nightglass-circle', lambda d: d['organization_design'].update(magic_owner_refs=['new-spell']), 'no new magic'),
            ('test_rivalry_models_are_reciprocal', 'gilded-hand', lambda d: d['organization_design']['rival_design_ids'].remove('broken-seal-society'), 'must be symmetric'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_6(self):
        with self.subTest(case='test_all_settlements_businesses_and_industries_remain_owned'), isolated_case(self):
            links=self.data('guild-network')['approved_design_index']['settlement_links']
            self.assertEqual(len(links),10);self.assertEqual(sum(len(x['business_ids']) for x in links),41)
            self.assertEqual(sum(len(x['industry_ids']) for x in links),17)
            self.assertTrue(all(x['classification']=='PROPOSED' and not x['actual_affiliations'] for x in links))
        with self.subTest(case='test_business_link_cannot_assign_guilty_proprietor'), isolated_case(self):
            self.reject('guild-network',lambda d:d['approved_design_index']['settlement_links'][0]['actual_affiliations'].append('secret member'),'no actual memberships')
        with self.subTest(case='test_unrelated_trade_dependency_rejected'), isolated_case(self):
            self.reject('guild-network',lambda d:d['approved_design_index']['settlement_links'][0].update(trade_dependency_ids=['trade:windmere--eastrun']),'unrelated trade')
        with self.subTest(case='test_criminal_design_is_not_a_global_ban'), isolated_case(self):
            self.reject('gilded-hand',lambda d:d['organization_design'].update(current_legal_ban='all realms'),'stay unknown')
        with self.subTest(case='test_no_suspension_without_decision'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['actual_suspensions'].append('issued'),'no actual memberships')

    def test_contracts_and_schema_and_identity_7(self):
        with self.subTest(case='test_all_five_association_classes'), isolated_case(self):
            d=self.data('guild-membership-and-contracts')['approved_professional_rules']
            self.assertEqual({x['id'] for x in d['association_statuses']},{'lawful-guild','unrecognized-association','suspended-guild','outlawed-organization','criminal-faction'})
            self.assertTrue(all(v is None for v in d['legal_decision_template'].values()))
        with self.subTest(case='test_no_actual_illicit_transaction'), isolated_case(self):
            self.reject('illicit-commerce-design',lambda d:d['actual_transactions'].append('sale'),'no actual memberships')
        with self.subTest(case='test_partial_extension_rejected'), isolated_case(self):
            self.reject('guild-network',lambda d:d.pop('approved_design_index'),'missing approved design routing')
        with self.subTest(case='test_archive_promotion_is_not_a_second_identity'), isolated_case(self):
            self.reject('guild-network',lambda d:d['approved_design_index']['archive_promotions'][0].update(entity_id='river-charter-league'),'archive identity')
        with self.subTest(case='test_criminal_regional_identity_cannot_expand'), isolated_case(self):
            self.reject('sable-current',lambda d:d['organization_design'].update(association_location_id='valedorn'),'identity/scope mismatch')

    def test_identity_8(self):
        cases = [
            ('test_no_actual_secret_leader', 'gilded-hand', lambda d: d['organization_design'].update(current_leaders=['hidden']), 'stay unknown'),
            ('test_no_secret_safehouse', 'black-pick-syndicate', lambda d: d['organization_design'].update(current_safehouses=['secret tunnel']), 'stay unknown'),
            ('test_no_private_secret_fact', 'nightglass-circle', lambda d: d['organization_design']['secret_facts'].append('unknown artifact'), 'secret outcomes'),
            ('test_rivalries_reference_designs_not_existing_mysteries', 'gilded-hand', lambda d: d['organization_design'].update(rival_design_ids=['crown-black-ledger']), 'rivalry scope'),
            ('test_business_link_cannot_reference_another_parent', 'guild-network', lambda d: d['approved_design_index']['settlement_links'][0]['business_ids'].append('brackenford:forge'), 'owner mismatch'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_identity_and_resources_9(self):
        with self.subTest(case='test_transaction_needs_ownership_funds_transport_and_evidence_fields'), isolated_case(self):
            self.reject('illicit-commerce-design',lambda d:d['transaction_template'].pop('ownership_provenance_ref'),'incomplete agreement/decision/transaction')
        with self.subTest(case='test_history_independence_and_legacy_payloads_preserved'), isolated_case(self):
            f=json.loads((ROOT/'tests/fixtures/phase2-04-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path,d in f['authorized_owner_revisions'].items():
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),d['after_sha256'],path)
            for path,legacy in f['legacy_guild_payloads'].items():
                now=json.loads(re.search(r'```json\n(.*?)\n```',(ROOT/path).read_text(),re.S)[1])
                for field in ('approved_design_index','approved_charter','approved_professional_rules'):now.pop(field,None)
                self.assertEqual(now,legacy,path)
            for ident in ('wayfarers-guild','dragon-slayer-academy','northern-provisioning-consortium'):
                self.assertIn('entities/factions/'+ident+'.md',f['unchanged_sha256'])
            for name in ('state/checkpoint.json','state/finance-ledger.json','entities/mechanics/prisoner-custody.md'):
                self.assertIn(name,f['unchanged_sha256'])
        with self.subTest(case='test_boolean_is_not_dues_amount'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['annual_dues_references'][0].update(amount_cp=True),'annual references')
        with self.subTest(case='test_no_compulsory_concord_fee'), isolated_case(self):
            self.reject('continental-guild-concord',lambda d:d['approved_charter'].update(compulsory_dues=True),'no Concord takeover')
        with self.subTest(case='test_no_operational_funds'), isolated_case(self):
            self.reject('red-antler-brotherhood',lambda d:d['organization_design'].update(current_funds_cp=100),'stay unknown')

    def test_resources_10(self):
        with self.subTest(case='test_twelve_finite_contexts_without_sellers_or_stock'), isolated_case(self):
            e=self.data('illicit-commerce-design');self.assertEqual(len(e['contexts']),12)
            self.assertTrue(all(x['finite_dependencies'] and x['current_inventory'] is None for x in e['contexts']))
            self.assertEqual(e['finance_ledger_ref'],'state/finance-ledger.json');self.assertIsNone(e['current_market_locations'])
        with self.subTest(case='test_no_competing_ledger'), isolated_case(self):
            self.reject('illicit-commerce-design',lambda d:d.update(finance_ledger_ref='state/black-market-ledger.json'),'no second ledger')
        with self.subTest(case='test_transaction_template_is_not_a_deal'), isolated_case(self):
            self.reject('illicit-commerce-design',lambda d:d['transaction_template'].update(seller_ref='named dealer'),'populated template')
        with self.subTest(case='test_contract_templates_create_no_job_or_acceptance'), isolated_case(self):
            self.reject('guild-membership-and-contracts',lambda d:d['approved_professional_rules']['contract_template'].update(status='accepted'),'populated template')
