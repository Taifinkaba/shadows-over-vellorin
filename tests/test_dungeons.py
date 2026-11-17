"""Source-state, no-reset, ownership and proposal tests mutate only disposable copies."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate import ValidationError, validate, require, repository_file
from scripts.dungeons import read_section_state, validate_population_event

ROOT=Path(__file__).resolve().parents[1]


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-dungeons-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes'):shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):
        kind='rules' if ident=='dungeon-exploration' else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self,ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,change):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S)
        d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,ensure_ascii=False,indent=2)+s[m.end(1):])

    def reject(self,ident,change,pattern):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,pattern):validate(self.root)

    def section(self,slug):
        return next(s for s in self.data('exploration-sections')['sections'] if s['section_id']==slug)

    def state(self,slug):
        return read_section_state(self.root,self.section(slug)['state_ref'],require,repository_file)

    def test_registry_and_reference_counts(self):
        self.assertIn('checkpoint valid',validate(self.root))
        self.assertEqual(len(self.data('dungeon-registry')['sites']),18)
        self.assertEqual(len(self.data('exploration-sections')['sections']),14)
        self.assertEqual(len(self.data('dungeon-ecology-and-hazards')['hazard_references']),4)
        self.assertEqual(len(self.data('dungeon-design-proposals')['proposals']),5)

    def test_duplicate_dungeon_id(self):
        self.reject('dungeon-registry',lambda d:d['sites'].append(d['sites'][0]),'duplicate/invalid site ID')

    def test_invalid_location_reference(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0].update(location_entity_id='missing-site'),'broken entity reference')

    def test_character_not_location(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0].update(location_entity_id='theron-ashvale'),'wrong reference type')

    def test_no_duplicate_location_alias(self):
        self.reject('dungeon-registry',lambda d:d['sites'][1].update(location_entity_id='ninth-vault'),'duplicate canonical location routing')

    def test_hollows_stay_distinct(self):
        sites={s['site_id']:s for s in self.data('dungeon-registry')['sites']}
        self.assertEqual(sites['site:hollow-first-hour']['location_entity_id'],'hollow-first-hour')
        self.assertEqual(sites['site:hollow-veil']['location_entity_id'],'hollow-veil')
        self.assertNotEqual(sites['site:hollow-first-hour']['location_entity_id'],sites['site:hollow-veil']['location_entity_id'])

    def test_unsourced_alias_rejected(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0]['aliases'].append('Mirror Foundation'),'unsourced alias/merger')

    def test_no_unsupported_entrance_connection(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0].update(entrance_location_id='seven-bells-witness-entry'),'no verified entrance assignment')

    def test_no_nearby_road_assumed_entrance_route(self):
        self.reject('dungeon-registry',lambda d:d['sites'][3]['access_route_ids'].append('route-caelthorne-mount-vaelspire'),'no verified road-to-entrance')

    def test_no_retroactive_threat_rank(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0].update(danger_classification='S+'),'no unsupported geography, category, threat')

    def test_no_blanket_dungeon_classification(self):
        self.reject('dungeon-registry',lambda d:d['sites'][15].update(record_kind='monster-lair'),'unsupported blanket dungeon classification')

    def test_unknown_does_not_mean_cleared(self):
        for s in self.data('dungeon-registry')['sites']:
            self.assertIsNone(s['exploration_state_ref'])
            self.assertIsNone(s['danger_classification'])

    def test_no_cleared_flag_from_visited_site(self):
        self.reject('dungeon-registry',lambda d:d['sites'][8].update(exploration_state_ref='cleared'),'whole-site status')

    def test_duplicate_section_id(self):
        self.reject('exploration-sections',lambda d:d['sections'].append(d['sections'][0]),'duplicate/invalid section ID')

    def test_section_parent_must_match(self):
        self.reject('exploration-sections',lambda d:d['sections'][0].update(site_id='site:hollow-veil'),'section site mismatch')

    def test_bad_status_vocabulary(self):
        self.reject('exploration-sections',lambda d:d['allowed_exploration_statuses'].append('auto-cleared'),'invalid exploration status vocabulary')

    def test_no_duplicate_source_row_or_inventory_alias(self):
        self.reject('exploration-sections',lambda d:d['sections'][1].update(state_ref=d['sections'][0]['state_ref']),'duplicate section/source inventory alias')

    def test_no_new_exploration_or_trap_event(self):
        self.reject('exploration-sections',lambda d:d['new_exploration_events'].append({'status':'cleared'}),'no new historical exploration')

    def test_western_gallery_stays_unexplored(self):
        self.assertEqual(self.state('section:hollow-first-hour:western-gallery')['exploration_status'],'unexplored')

    def test_annex_searched_not_cleared(self):
        state=self.state('section:hollow-first-hour:supply-annex')
        self.assertEqual(state['exploration_status'],'explored')
        self.assertEqual(state['source_label'],'Searched')

    def test_protected_quarters_not_unexplored_or_sealed(self):
        state=self.state('section:hollow-first-hour:keeper-quarters')
        self.assertEqual(state['exploration_status'],'unknown')
        self.assertEqual(state['access_status'],'protected')

    def test_visits_do_not_become_explored_or_unexplored(self):
        for site in ('old-copperworks','ravencrest-waystation'):
            self.assertEqual(self.state(f'section:{site}:recorded-area')['exploration_status'],'visited')

    def test_partial_sources_remain_partial(self):
        for site in ('whisperstone-hollow','frostglass-western-ridge','seven-bells-lower-foundations'):
            self.assertEqual(self.state(f'section:{site}:recorded-area')['exploration_status'],'partially-explored')

    def test_cellar_inspection_is_not_whole_site_clearance(self):
        self.assertEqual(self.state('section:north-return-house:cellar')['exploration_status'],'visited')

    def test_source_state_is_derived_not_duplicate_snapshot(self):
        p=self.root/'entities/mechanics/shady-salvage.md'
        p.write_text(p.read_text().replace('| Old Copperworks | Visited |','| Old Copperworks | Partially explored |'))
        self.assertEqual(self.state('section:old-copperworks:recorded-area')['exploration_status'],'partially-explored')

    def test_section_source_must_resolve(self):
        self.reject('exploration-sections',lambda d:d['sections'][0]['state_ref'].update(locator='Invented treasury'),'state row missing')

    def test_lost_section_link_rejected(self):
        self.reject('dungeon-registry',lambda d:d['sites'][2]['section_ids'].pop(),'routing coverage mismatch')

    def test_no_duplicate_or_new_salvage_inventory(self):
        self.reject('dungeon-registry',lambda d:d['new_inventory_records'].append({'coins':680}),'no new loot or objective completion')

    def test_protected_evidence_cannot_route_to_loot(self):
        self.reject('dungeon-registry',lambda d:d['sites'][5].update(protected_evidence_owner_refs=['shady-salvage']),'protected evidence cannot be rerouted')

    def test_protected_originals_must_keep_owner(self):
        self.reject('dungeon-registry',lambda d:d['sites'][5].update(protected_evidence_owner_refs=[]),'protected originals remain')

    def test_no_duplicate_contract_rewards_or_site_offers(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0]['guild_contract_ids'].append('B-83'),'no new offered/site-bound contract')

    def test_no_automatic_loot(self):
        self.reject('dungeon-registry',lambda d:d.update(automatic_loot=True),'automatic respawn/loot forbidden')

    def test_no_objective_completion(self):
        self.reject('dungeon-registry',lambda d:d['new_objective_outcomes'].append({'objective':'cleared'}),'no new loot or objective completion')

    def test_no_monster_respawning(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d.update(automatic_respawn=True),'automatic respawn/stat scaling forbidden')

    def test_no_automatic_rank_scaling(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d.update(automatic_scaling=True),'automatic respawn/stat scaling forbidden')

    def test_no_new_creature_population(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['ecology_references'][0].update(population_count=100),'no new creature location, population')

    def test_no_forced_guardian_location(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['ecology_references'][0].update(current_location_id='hollow-veil'),'no new creature location')

    def test_containment_is_not_a_new_defeat_or_revival(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['new_encounter_events'].append({'name':'Pale Devourer','outcome':'defeated'}),'no new encounter, defeat, revival')

    def test_no_trap_trigger(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['hazard_references'][0]['new_trigger_events'].append({'triggered':True}),'no retroactive trap')

    def test_no_retroactive_trap_placement_or_solution(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['hazard_references'][0].update(section_id='section:old-copperworks:recorded-area'),'no retroactive trap location')

    def test_missing_hazard_source_row(self):
        self.reject('dungeon-ecology-and-hazards',lambda d:d['hazard_references'][0]['state_ref'].update(locator='Invented trap'),'state row missing')

    def test_ss_rank_conflict_not_silently_resolved(self):
        self.reject('dungeon-design-proposals',lambda d:d['proposals'][4].update(scale_compatibility='PROPOSED SCALE LABEL ONLY'),'SS scale conflict')

    def test_ss_label_not_normalized_to_splus(self):
        self.reject('dungeon-design-proposals',lambda d:d['proposals'][4].update(proposed_threat_label='S+'),'proposal rank/name changed')

    def test_proposed_dungeon_not_active(self):
        self.reject('dungeon-design-proposals',lambda d:d['proposals'][0].update(classification='CONFIRMED CANON'),'cannot become approved canon')

    def test_no_proposed_dungeon_location_or_loot(self):
        self.reject('dungeon-design-proposals',lambda d:d['proposals'][0].update(candidate_location_id='mount-vaelspire'),'no proposed site placement')

    def test_no_world_dungeon_census(self):
        self.reject('dungeon-design-proposals',lambda d:d.update(world_census_count=10000),'not a census or active site')

    def test_proposal_does_not_merge_with_old_hollow(self):
        self.reject('dungeon-design-proposals',lambda d:d['proposals'][0].update(existing_site_id='site:hollow-first-hour'),'no proposed site placement, merger')

    def test_no_chest_refill(self):
        self.reject('dungeon-exploration',lambda d:d.update(automatic_chest_refill=True),'no new loot, battle, chest refill')

    def test_loot_ownership_domains_stay_distinct(self):
        self.reject('dungeon-exploration',lambda d:d['loot_ownership_categories'].remove('protected-evidence'),'ownership categories cannot be merged')

    def test_secret_source_not_public_lookup(self):
        self.reject('dungeon-registry',lambda d:d['sites'][0]['source_refs'].append('entities/items/black-runeblade.md'),'secret reference excluded')

    def test_partial_framework_rejected(self):
        p=self.root/'index.json';d=json.loads(p.read_text());d['entries']=[e for e in d['entries'] if e['id']!='exploration-sections'];p.write_text(json.dumps(d))
        self.path('exploration-sections').unlink()
        with self.assertRaisesRegex(ValidationError,'incomplete framework'):validate(self.root)

    def test_optimized_validator_rejects_respawn(self):
        self.edit('dungeon-registry',lambda d:d.update(automatic_respawn=True))
        p=subprocess.run([sys.executable,'-O',str(ROOT/'scripts/validate.py'),'--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(p.returncode,1);self.assertIn('automatic respawn/loot forbidden',p.stderr)

    def test_protected_existing_campaign_and_exploration_records_preserved(self):
        f=json.loads((ROOT/'tests/fixtures/chunk6-preservation.json').read_text())
        for path,digest in f['protected_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)

    def test_validator_does_not_mutate_sources(self):
        files=[p for folder in ('state','entities','archive') for p in (self.root/folder).rglob('*') if p.is_file()]
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in files};validate(self.root)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in files})

    def test_inventory_pointer_not_relocated_to_visited_site(self):
        self.reject('dungeon-registry',lambda d:d['sites'][8].update(recovered_inventory_owner_refs=['seven-bells-inventory']),'inventory lookup cannot be relocated')

    def test_unexplored_section_gets_no_recovered_inventory(self):
        self.reject('exploration-sections',lambda d:d['sections'][1].update(recovered_inventory_owner_refs=['shady-salvage']),'no unsourced section recovery')


class PopulationEventTests(unittest.TestCase):
    """Synthetic schema-only examples, never actual creature changes."""
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='dungeon-population-fixture-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);(self.root/'event.md').write_text('Test-only causal migration after elapsed time. Not campaign canon.')
        self.event=dict(site_id='fixture-site',creature_reference_id='fixture-creature',status='proposed',cause=None,elapsed_time_ref=None,event_ref=None,source_refs=[],automatic=False)

    def check(self):
        validate_population_event(self.event,self.root,{'fixture-site'},{'fixture-creature'},require,repository_file)

    def test_proposal_can_keep_unknowns(self):self.check()

    def test_no_automatic_respawn(self):
        self.event['automatic']=True
        with self.assertRaisesRegex(ValidationError,'automatic respawn forbidden'):self.check()

    def test_recorded_change_needs_cause(self):
        self.event['status']='recorded'
        with self.assertRaisesRegex(ValidationError,'plausible cause required'):self.check()

    def test_recorded_change_needs_elapsed_time_and_event(self):
        self.event.update(status='recorded',cause='Test-only migration')
        with self.assertRaisesRegex(ValidationError,'elapsed time and actual event'):self.check()

    def test_recorded_source_completeness_does_not_execute_spawn(self):
        self.event.update(status='recorded',cause='Test-only migration',elapsed_time_ref='event.md',event_ref='event.md',source_refs=['event.md'])
        before=(self.root/'event.md').read_bytes();self.check();self.assertEqual((self.root/'event.md').read_bytes(),before)
