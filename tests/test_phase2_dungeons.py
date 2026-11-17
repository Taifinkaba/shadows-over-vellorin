from case_support import isolated_case, validate_scope
"""Approved dungeon architecture/reference data must never instantiate gameplay."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.validate import ValidationError,validate
from scripts.dungeon_designs import DUNGEONS,MONSTERS,RECOVERY_FIELDS,validate_recovery_requirements

ROOT=Path(__file__).resolve().parents[1]


class Phase2DungeonTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-dungeon-designs-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):
        return self.root/f'entities/{"rules" if ident=="dungeon-exploration" else "mechanics"}/{ident}.md'

    def data(self,ident):return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,change):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,ident,change,pattern):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,pattern):validate_scope(self.root, 'dungeon_designs')


    def test_causality_1(self):
        cases = [
            ('test_no_operational_approach_route', 'ashen-anvil', lambda d: d['dungeon_design']['regional_association']['access_route_ids'].append('route-caelthorne-ironhollow-hold'), 'no discoveries'),
            ('test_candidate_region_not_a_new_place', 'pale-reliquary', lambda d: d['dungeon_design']['regional_association'].update(candidate_region_id='frostmarch'), 'cannot become verified'),
            ('test_no_automatic_respawn', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design'].update(automatic_respawn=True), 'no automatic respawn'),
            ('test_no_automatic_hazard_damage', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['hazard_references'][0].update(automatic_damage=True), 'automatic hazard damage'),
            ('test_no_actual_reward_events', 'dungeon-exploration', lambda d: d['approved_exploration_design']['actual_recoveries'].append('loot'), 'no discoveries'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_continuity_and_contracts_and_schema_2(self):
        with self.subTest(case='test_unrelated_history_and_legacy_dungeon_fields_preserved'), isolated_case(self):
            f=json.loads((ROOT/'tests/fixtures/phase2-05-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path,d in f['authorized_owner_revisions'].items():
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),d['after_sha256'],path)
            for path,old in f['legacy_dungeon_payloads'].items():
                now=json.loads(re.search(r'```json\n(.*?)\n```',(ROOT/path).read_text(),re.S)[1])
                for field in ('approved_design_index','approved_reference_design','approved_exploration_design'):now.pop(field,None)
                self.assertEqual(now,old,path)
            for path in ('state/checkpoint.json','state/finance-ledger.json','entities/mechanics/dungeon-registry.md',
                         'entities/mechanics/exploration-sections.md','entities/mechanics/shady-salvage.md','entities/mechanics/theron-spells.md'):
                self.assertIn(path,f['unchanged_sha256'])
            self.assertEqual(len([x for x in f['unchanged_sha256'] if '/route-' in x]),20)
        with self.subTest(case='test_design_edge_is_not_current_passability'), isolated_case(self):
            self.reject('drowned-archive',lambda d:d['dungeon_design']['connections'][0].update(current_passability='safe'),'remain unknown')
        with self.subTest(case='test_no_current_area_state_or_inhabitants'), isolated_case(self):
            self.reject('pale-reliquary',lambda d:d['dungeon_design']['areas'][0].update(current_inhabitants=['warden']),'remain unknown')
        with self.subTest(case='test_hazard_is_not_currently_placed'), isolated_case(self):
            self.reject('dungeon-ecology-and-hazards',lambda d:d['approved_reference_design']['hazard_references'][0].update(current_placement_ids=['known-place']),'remain unknown')
        with self.subTest(case='test_five_unique_proposal_identities_and_finite_designs'), isolated_case(self):
            self.assertIn('checkpoint valid',validate(self.root))
            for ident,(name,region,rank) in DUNGEONS.items():
                d=self.data(ident)['dungeon_design'];self.assertEqual(d['proposal_id'],'dungeon-proposal:'+ident)
                self.assertEqual(d['name'],name);self.assertEqual(d['difficulty']['legacy_proposed_label'],rank)
                self.assertEqual(len(d['areas']),5);self.assertGreaterEqual(len(d['retreat_path_designs']),2)
                self.assertIsNone(d['regional_association']['verified_entrance_id']);self.assertEqual(d['actual_discoveries'],[])

    def test_contracts_and_schema_3(self):
        with self.subTest(case='test_profile_provenance_is_required'), isolated_case(self):
            self.reject('hollowstone-mine',lambda d:d['dungeon_design'].update(approval_source_ref='README.md'),'wrong approval')
        with self.subTest(case='test_ss_stays_unresolved'), isolated_case(self):
            d=self.data('shattered-meridian')['dungeon_design']['difficulty'];self.assertEqual(d['legacy_proposed_label'],'SS')
            self.assertIsNone(d['compatible_rank']);self.assertEqual(d['mapping_status'],'UNRESOLVED LEGACY SS')
            self.assertNotIn('SS',self.data('dungeon-design-proposals')['proposed_threat_scale'])
        with self.subTest(case='test_ss_cannot_be_silently_mapped'), isolated_case(self):
            self.reject('shattered-meridian',lambda d:d['dungeon_design']['difficulty'].update(compatible_rank='S+'),'SS mapping')
        with self.subTest(case='test_dungeon_rank_is_no_global_combat_rank'), isolated_case(self):
            self.reject('pale-reliquary',lambda d:d['dungeon_design']['difficulty'].update(domain='combat-power'),'not global combat')
        with self.subTest(case='test_no_discovered_entrance'), isolated_case(self):
            self.reject('hollowstone-mine',lambda d:d['dungeon_design']['regional_association'].update(verified_entrance_id='known-door'),'remain unknown')

    def test_contracts_and_schema_4(self):
        with self.subTest(case='test_no_coordinates'), isolated_case(self):
            self.reject('shattered-meridian',lambda d:d['dungeon_design']['regional_association'].update(exact_coordinates=[1,2]),'remain unknown')
        with self.subTest(case='test_existing_site_is_not_an_alias'), isolated_case(self):
            self.reject('drowned-archive',lambda d:d['dungeon_design'].update(existing_site_id='site:northern-depository'),'remain unknown')
        with self.subTest(case='test_finite_area_count'), isolated_case(self):
            self.reject('hollowstone-mine',lambda d:d['dungeon_design']['areas'].append(copy.deepcopy(d['dungeon_design']['areas'][0])),'finite five-area')
        with self.subTest(case='test_connections_must_stay_inside_this_design'), isolated_case(self):
            self.reject('hollowstone-mine',lambda d:d['dungeon_design']['connections'][0].update(to_area_id='design-area:ashen-anvil:foundry'),'graph endpoint')
        with self.subTest(case='test_all_areas_have_conceptual_return_path'), isolated_case(self):
            def isolate(d):
                g=d['dungeon_design'];entry=g['entry_interface_area_ids'][0]
                g['connections']=[e for e in g['connections'] if entry not in (e['from_area_id'],e['to_area_id'])]
            self.reject('hollowstone-mine',isolate,'connect to an entry')

    def test_contracts_and_schema_5(self):
        cases = [
            ('test_retreat_uses_physical_connections', 'shattered-meridian', lambda d: d['dungeon_design']['retreat_path_designs'][0].pop(1), 'no physical connection'),
            ('test_no_stat_mutation', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['monster_references'][0].update(hp=25), 'stats contradict'),
            ('test_no_usable_opponent_before_pr8', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['monster_references'][0].update(combat_usable=True), 'reference-only'),
            ('test_no_new_attack_formula', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['monster_references'][0].update(damage_formula='1d6'), 'remain unknown'),
            ('test_no_monster_population', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['monster_references'][0].update(current_instance_count=4), 'remain unknown'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_6(self):
        cases = [
            ('test_no_unapproved_numeric_hazard_effects', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['hazard_references'][0].update(numerical_effects={'damage': 10}), 'remain unknown'),
            ('test_creature_encounter_is_no_guaranteed_success', 'hollowstone-mine', lambda d: d['dungeon_design']['encounter_designs'][0].update(guaranteed_success=True), 'not a current guaranteed event'),
            ('test_no_seeded_treasure_in_vault', 'ashen-anvil', lambda d: d['dungeon_design']['areas'][-1].update(current_contents=['legendary sword']), 'remain unknown'),
            ('test_no_faction_expediton', 'shattered-meridian', lambda d: d['dungeon_design']['prospective_faction_interests'][0]['actual_operations'].append('arrived'), 'no discoveries'),
            ('test_no_unsupported_mystery_link', 'drowned-archive', lambda d: d['dungeon_design']['unsupported_mystery_connections'].append('Crown-07'), 'secret outcomes'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_and_identity_7(self):
        cases = [
            ('test_no_hidden_dungeon_solution', 'pale-reliquary', lambda d: d['dungeon_design']['hidden_solutions'].append('password'), 'secret outcomes'),
            ('test_no_hidden_cache_coordinates', 'shattered-meridian', lambda d: d['dungeon_design']['hidden_treasure_locations'].append([1, 2]), 'secret outcomes'),
            ('test_locked_skills_not_unlocked_by_design', 'shattered-meridian', lambda d: d['dungeon_design']['new_abilities'].append('Chronos Eye'), 'abilities or secret'),
            ('test_partial_extension_rejected', 'dungeon-design-proposals', lambda d: d.pop('approved_design_index'), 'unexpected design fields'),
            ('test_no_duplicate_promoted_identity', 'dungeon-design-proposals', lambda d: d['approved_design_index']['profiles'][0].update(entity_id='ashen-anvil'), 'proposal identity'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_identity_and_resources_8(self):
        with self.subTest(case='test_area_identity_is_unique'), isolated_case(self):
            self.reject('ashen-anvil',lambda d:d['dungeon_design']['areas'][1].update(id=d['dungeon_design']['areas'][0]['id']),'duplicate/wrong area')
        with self.subTest(case='test_monster_stats_exact_and_reference_only'), isolated_case(self):
            rows=self.data('dungeon-ecology-and-hazards')['approved_reference_design']['monster_references']
            for row in rows:
                ident=row['id'].removeprefix('monster-reference:');name,hp,mp,defense,rank=MONSTERS[ident]
                self.assertEqual((row['name'],row['hp'],row['mp'],row['defense'],row['reference_rank']),(name,hp,mp,defense,rank))
                self.assertFalse(row['combat_usable']);self.assertIsNone(row['damage_formula']);self.assertIsNone(row['current_instance_count'])
        with self.subTest(case='test_recovery_template_requires_ownership_and_update'), isolated_case(self):
            self.reject('dungeon-exploration',lambda d:d['approved_exploration_design']['recovery_template'].pop('approved_update_evidence_ref'),'complete recovery template')
        with self.subTest(case='test_no_automatic_resource_recovery'), isolated_case(self):
            self.reject('dungeon-exploration',lambda d:d['approved_exploration_design'].update(automatic_recovery=True),'no automatic population')
        with self.subTest(case='test_boolean_is_not_monster_hp'), isolated_case(self):
            self.reject('dungeon-ecology-and-hazards',lambda d:d['approved_reference_design']['monster_references'][0].update(hp=True),'stats contradict')

    def test_resources_9(self):
        cases = [
            ('test_complete_hazard_warnings_and_exposure_required', 'dungeon-ecology-and-hazards', lambda d: d['approved_reference_design']['hazard_references'][0].pop('observable_warnings'), 'unexpected design fields'),
            ('test_no_completed_rescue_or_encounter', 'ashen-anvil', lambda d: d['dungeon_design']['encounter_designs'][-1]['actual_outcomes'].append('rescued'), 'no discoveries'),
            ('test_no_reward_inventory_or_ore_quantity', 'hollowstone-mine', lambda d: d['dungeon_design'].update(current_recoverable_quantity=100), 'remain unknown'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)


class FiniteRecoveryCompletenessTests(unittest.TestCase):
    def setUp(self):
        self.record={field:'fixture-evidence' for field in RECOVERY_FIELDS}
        self.record.update(status='recorded',quantity=1,verified_available_quantity=2,
            dungeon_design_id='hollowstone-mine',area_id='design-area:hollowstone-mine:collapsed-entrance',finance_transaction_ref=None)

    def require(self,condition,message):
        if not condition:raise ValueError(message)

    def check(self):validate_recovery_requirements(self.record,self.require)


    def test_contracts_and_schema_1(self):
        with self.subTest(case='test_no_infinite_quantity'), isolated_case(self):
            self.record['quantity']=float('inf')
            with self.assertRaisesRegex(ValueError,'finite positive'):self.check()
        with self.subTest(case='test_cannot_recover_more_than_verified_available'), isolated_case(self):
            self.record['quantity']=3
            with self.assertRaisesRegex(ValueError,'verified availability'):self.check()
        with self.subTest(case='test_no_boolean_quantity'), isolated_case(self):
            self.record['quantity']=True
            with self.assertRaisesRegex(ValueError,'finite positive'):self.check()
        with self.subTest(case='test_missing_provenance_blocks_recorded_recovery'), isolated_case(self):
            self.record['ownership_provenance_ref']=None
            with self.assertRaisesRegex(ValueError,'title, transport'):self.check()
        with self.subTest(case='test_missing_transport_blocks_recovery'), isolated_case(self):
            self.record['transport_capacity_ref']=None
            with self.assertRaisesRegex(ValueError,'title, transport'):self.check()

    def test_resources_2(self):
        with self.subTest(case='test_completeness_check_writes_nothing'), isolated_case(self):
            before=copy.deepcopy(self.record);self.check();self.assertEqual(self.record,before)
