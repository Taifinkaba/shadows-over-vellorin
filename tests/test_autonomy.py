"""Autonomy maintenance has no state engine; mutations stay in disposable copies."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.autonomy import (evidence, validate_event_candidate, validate_public_clock_proposal,
                              EVENT_FIELDS, CLOCK_FIELDS)
from scripts.validate import validate, ValidationError

ROOT=Path(__file__).resolve().parents[1]


class AutonomyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-autonomy-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for directory in ('entities','state','archive','changes'):shutil.copytree(ROOT/directory,self.root/directory)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):
        return self.root/f"entities/{'rules' if ident=='npc-autonomy-and-time' else 'mechanics'}/{ident}.md"

    def data(self,ident):return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,fn):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);fn(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,ident,fn):
        self.edit(ident,fn)
        with self.assertRaises(ValidationError):validate(self.root)

    def test_current_repository_valid(self):self.assertIn(f"{len(json.loads((self.root/'index.json').read_text())['entries'])} entity records",validate(self.root))

    def test_all_preexisting_campaign_owners_and_history_preserved(self):
        fixture=json.loads((ROOT/'tests/fixtures/chunk8-preservation.json').read_text())
        for path,digest in fixture['sha256'].items():
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)

    def test_validation_is_readonly(self):
        before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('entities','state','archive','changes') for p in (self.root/folder).rglob('*') if p.is_file()}
        validate(self.root)
        self.assertEqual(before,{path:hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in before})

    def test_routing_does_not_claim_current_positions_or_completion(self):
        for row in self.data('independent-assignments')['assignments']:
            self.assertNotIn('status',row);self.assertNotIn('location',row);self.assertNotIn('last_verified_date',row)
            self.assertIn('state/checkpoint.json',row['freshness_refs'])
        self.assertEqual(self.data('independent-assignments')['new_assignment_events'],[])

    def test_alpha_has_no_imposed_assignment(self):
        a=self.data('independent-assignments');self.assertIn('alpha',{x['actor_id'] for x in a['actors']})
        self.assertNotIn('alpha',{x['actor_id'] for x in a['assignments']})
        self.assertIn('Current whereabouts unverified',(self.root/'entities/creatures/alpha.md').read_text())

    def test_scale_request_is_not_a_gift_or_reply(self):
        row=next(x for x in self.data('independent-assignments')['assignments'] if x['assignment_id']=='assignment:vaeltharion-request')
        self.assertEqual(row['responsibility_ref']['quote'],'Voluntary shed-scale request pending, no reply received.')
        self.assertNotIn('accepted',row);self.assertNotIn('completed',row)

    def test_lyra_care_and_research_are_distinct_scopes(self):
        rows=[x for x in self.data('independent-assignments')['assignments'] if x['actor_id']=='lyra-moonvale']
        self.assertEqual(len(rows),2);self.assertNotEqual(rows[0]['responsibility_ref'],rows[1]['responsibility_ref'])
        self.assertTrue(all('progress' not in x for x in rows))

    def test_constructs_are_ability_contexts_not_new_actor_ids(self):
        a=self.data('independent-assignments')
        self.assertEqual({x['context_id'] for x in a['construct_contexts']},{'construct:raze','construct:aegis'})
        self.assertNotIn('raze',{x['actor_id'] for x in a['actors']})
        self.assertNotIn('aegis',{x['actor_id'] for x in a['actors']})

    def test_bonds_and_independent_identities_remain_with_owners(self):
        self.assertIn('bond3/5 (supersedes earlier5/5)',(self.root/'entities/creatures/shade.md').read_text())
        self.assertIn('bond4/5',(self.root/'entities/creatures/aurelion.md').read_text())
        self.assertIn('not a raven',(self.root/'entities/creatures/aurelion.md').read_text().lower())
        self.assertIn('Do not equate or duplicate',(self.root/'entities/creatures/frostmoon.md').read_text())

    def test_faction_directory_owns_no_leaders_members_or_intelligence(self):
        data=self.data('faction-activity')
        for row in data['factions']:
            self.assertEqual(set(row),{'faction_id','source_ref','classification','knowledge'})
            self.assertEqual(row['knowledge'],'requires-discovery-review')
        concord=next(x for x in data['factions'] if x['faction_id']=='continental-guild-concord')
        self.assertEqual(concord['classification'],'PROPOSED')

    def test_chronicles_are_document_pointers_not_new_timeline_events(self):
        d=self.data('world-event-references');self.assertEqual(len(d['chronicles']),6)
        self.assertEqual(d['new_events'],[])
        for row in d['chronicles']:
            self.assertNotIn('outcome',row);self.assertNotIn('date',row);self.assertNotIn('participating_actors',row)

    def test_missing_dated_assignment_observation_stays_a_contract_gap(self):
        d=self.data('independent-assignments')
        self.assertIn('last_verified_date',d['owner_field_contract'])
        self.assertTrue(all('last_verified_date' not in x for x in d['assignments']))

    def test_partial_framework_rejected(self):
        p=self.path('world-event-references');p.unlink()
        index=self.root/'index.json';d=json.loads(index.read_text());d['entries']=[x for x in d['entries'] if x['id']!='world-event-references'];index.write_text(json.dumps(d))
        with self.assertRaises(ValidationError):validate(self.root)

    def test_secret_entity_cannot_enter_public_actor_routing(self):
        # Even a valid canonical ID must not be promoted from GM-only metadata.
        p=self.root/'entities/creatures/alpha.md';p.write_text(p.read_text().replace('visibility: gm-reference','visibility: gm-secret'))
        index=self.root/'index.json';d=json.loads(index.read_text())
        for row in d['entries']:
            if row['id']=='alpha':row['visibility']='gm-secret'
        index.write_text(json.dumps(d))
        with self.assertRaises(ValidationError):validate(self.root)


CASES={
 'duplicate_assignment_id':('independent-assignments',lambda d:d['assignments'].__setitem__(0,copy.deepcopy(d['assignments'][1]))),
 'duplicate_actor':('independent-assignments',lambda d:d['actors'].__setitem__(0,copy.deepcopy(d['actors'][1]))),
 'missing_actor':('independent-assignments',lambda d:d['actors'].pop()),
 'wrong_actor_type':('independent-assignments',lambda d:d['actors'][0].update(actor_id='ashvale-estate')),
 'unknown_actor':('independent-assignments',lambda d:d['assignments'][0].update(actor_id='new-person')),
 'different_actor_assignment':('independent-assignments',lambda d:d['assignments'][0].update(actor_id='master-beren')),
 'source_owner_mismatch':('independent-assignments',lambda d:d['assignments'][0]['responsibility_ref'].update(source_ref='entities/characters/master-beren.md')),
 'invented_progress_quote':('independent-assignments',lambda d:d['assignments'][0]['responsibility_ref'].update(quote='Expansion completed and paid.')),
 'unsupported_current_location':('independent-assignments',lambda d:d['assignments'][0].update(location_id='ashvale-estate')),
 'invented_acceptance':('independent-assignments',lambda d:d['assignments'][4].update(acceptance='accepted')),
 'automatically_completed_assignment':('independent-assignments',lambda d:d['assignments'][0].update(status='completed')),
 'invented_last_verified_date':('independent-assignments',lambda d:d['assignments'][0].update(last_verified_date='Day181')),
 'forced_remote_outcome':('independent-assignments',lambda d:d['new_assignment_events'].append({'outcome':'success'})),
 'automatic_outcomes':('independent-assignments',lambda d:d.update(automatic_outcomes=True)),
 'invented_communication':('independent-assignments',lambda d:d['new_communications'].append({'status':'received'})),
 'discovery_assumed':('independent-assignments',lambda d:d['actors'][0].update(knowledge='player-known')),
 'new_construct_ability':('independent-assignments',lambda d:d['construct_contexts'][0].update(ability='independent spellcasting')),
 'wrong_construct_source':('independent-assignments',lambda d:d['construct_contexts'][0].update(source_ref='entities/characters/theron-ashvale.md')),
 'missing_precedence_source':('independent-assignments',lambda d:d['assignments'][0]['freshness_refs'].pop()),
 'duplicate_faction':('faction-activity',lambda d:d['factions'].__setitem__(0,copy.deepcopy(d['factions'][1]))),
 'unsupported_membership':('faction-activity',lambda d:d['new_memberships'].append({'member':'tomas'})),
 'unauthorized_legal_power':('faction-activity',lambda d:d['new_legal_powers'].append('estate police authority')),
 'invented_faction_operation':('faction-activity',lambda d:d['new_activity'].append({'operation':'new patrol'})),
 'concealed_leadership_field':('faction-activity',lambda d:d['factions'][0].update(leadership='hidden chief')),
 'secret_intention_field':('faction-activity',lambda d:d['factions'][0].update(secret_intentions='hidden motive')),
 'concord_promoted':('faction-activity',lambda d:d['factions'][-1].update(classification='CONFIRMED CANON')),
 'faction_knowledge_assumed':('faction-activity',lambda d:d['factions'][0].update(knowledge='player-known')),
 'duplicate_historical_document':('world-event-references',lambda d:d['chronicles'].__setitem__(0,copy.deepcopy(d['chronicles'][1]))),
 'missing_event_source':('world-event-references',lambda d:d['chronicles'][0].update(source_ref='changes/chronicles/missing.md')),
 'maintenance_as_history':('world-event-references',lambda d:d['chronicles'][0].update(source_ref='changes/chronicles/npc-autonomy-framework-maintenance.md')),
 'new_historical_event':('world-event-references',lambda d:d['new_events'].append({'event_id':'new-event'})),
 'hidden_event_outcome':('world-event-references',lambda d:d['chronicles'][0].update(outcome='hidden future outcome')),
 'automatic_world_event':('world-event-references',lambda d:d.update(automatic_events=True)),
 'active_clock':('world-development-proposals',lambda d:d['clocks'].append({'value':3})),
 'automatic_clock_advance':('world-development-proposals',lambda d:d.update(automatic_advancement=True)),
 'bond_change':('world-development-proposals',lambda d:d['relationship_changes'].append({'bond':5})),
 'numeric_reputation':('world-development-proposals',lambda d:d.update(criminal_fear=1)),
 'workflow_frontmatter_status':('world-development-proposals',lambda d:d.update(classification='CONFIRMED CANON')),
 'approval_assumed':('world-development-proposals',lambda d:d.update(approval_status='approved')),
 'instant_communication':('npc-autonomy-and-time',lambda d:d['new_communications'].append({'status':'delivered'})),
 'time_advance':('npc-autonomy-and-time',lambda d:d['new_time_advances'].append('Day181')),
 'ability_award':('npc-autonomy-and-time',lambda d:d['new_abilities'].append('free mana')),
 'forced_relationship':('npc-autonomy-and-time',lambda d:d['new_relationships'].append('betrayal')),
 'resource_posting':('npc-autonomy-and-time',lambda d:d['new_resource_postings'].append({'income_cp':6500})),
 'automatic_writer':('npc-autonomy-and-time',lambda d:d.update(automatic_writes=True)),
 'unlimited_magical_channel':('npc-autonomy-and-time',lambda d:d['communication_owner_refs'].append('world-event-references')),
 'competing_finance_authority':('npc-autonomy-and-time',lambda d:d['resource_owner_refs'].__setitem__(0,'world-event-references')),
}
for name,(ident,fn) in CASES.items():
    def case(self,ident=ident,fn=fn):self.reject(ident,fn)
    setattr(AutonomyTests,'test_reject_'+name,case)


class CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records={x['id']:x for x in json.loads((ROOT/'index.json').read_text())['entries']}

    def event(self):
        return dict(event_id='synthetic-candidate',date=None,time=None,location_id=None,initiator_id=None,
            participant_ids=[],category='research',trigger_ref=None,action_ref=None,outcome_ref=None,
            affected_actor_ids=[],affected_faction_ids=[],quest_ids=[],resource_effect_refs=[],knowledge='requires-discovery-review',
            source_refs=[],time_advance_ref=None,status='proposed',automatic=False,discovery_ref=None)

    def observed(self):
        # Evidence locator validation does not independently prove a new occurrence.
        p='changes/chronicles/year848-day156-end-session.md'
        e={'source_ref':p,'quote':'party returned home'}
        return {**self.event(),'status':'recorded','source_refs':[p],'trigger_ref':e,'action_ref':e,'outcome_ref':e,'time_advance_ref':e}

    def clock(self):
        return dict(clock_id='synthetic-proposal',owner_ref='dragon-slayer-academy',starting_condition_ref=None,
            source_refs=['changes/chronicles/npc-autonomy-framework-maintenance.md'],current_verified_progress=None,
            trigger_refs=[],possible_consequences=[],visibility='public-reference',last_verified_date=None,
            approval_ref=None,classification='PROPOSED',automatic=False)

    def test_proposed_event_can_have_unknown_dates_actors_and_sources(self):
        validate_event_candidate(self.event(),ROOT,self.records)

    def test_recorded_event_keeps_unknown_exact_date_without_fabrication(self):
        validate_event_candidate(self.observed(),ROOT,self.records)
        self.assertIsNone(self.observed()['date']);self.assertIsNone(self.observed()['time'])

    def test_recorded_event_needs_actual_scene_and_outcome_evidence(self):
        for key in ('trigger_ref','action_ref','outcome_ref','time_advance_ref'):
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'actual time-advance'):
                validate_event_candidate({**self.observed(),key:None},ROOT,self.records)

    def test_duplicate_historical_event_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'duplicate historical'):
            validate_event_candidate(self.observed(),ROOT,self.records,['synthetic-candidate'])

    def test_proposal_cannot_force_outcome(self):
        with self.assertRaisesRegex(ValueError,'proposed event'):
            validate_event_candidate({**self.event(),'outcome_ref':self.observed()['outcome_ref'],'source_refs':self.observed()['source_refs']},ROOT,self.records)

    def test_unknown_location_actor_faction_and_quest_rejected(self):
        for key,value in [('location_id','new-location'),('initiator_id','new-person'),('affected_faction_ids',['tomas']),('participant_ids',['guardian-links']),('quest_ids',['ashvale-estate'])]:
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'entity reference'):
                validate_event_candidate({**self.event(),key:value},ROOT,self.records)

    def test_duplicate_participants_rejected(self):
        with self.assertRaisesRegex(ValueError,'duplicate'):
            validate_event_candidate({**self.event(),'participant_ids':['tomas','tomas']},ROOT,self.records)

    def test_secret_actor_cannot_be_used_in_public_event(self):
        records=copy.deepcopy(self.records);records['tomas']['visibility']='gm-secret'
        with self.assertRaisesRegex(ValueError,'secret entity'):
            validate_event_candidate({**self.event(),'participant_ids':['tomas']},ROOT,records)

    def test_public_knowledge_requires_discovery(self):
        with self.assertRaisesRegex(ValueError,'discovery evidence'):
            validate_event_candidate({**self.event(),'knowledge':'player-known'},ROOT,self.records)

    def test_gm_only_event_needs_safe_storage(self):
        with self.assertRaisesRegex(ValueError,'safe storage'):
            validate_event_candidate({**self.event(),'knowledge':'gm-only'},ROOT,self.records)

    def test_resource_effects_link_authorities_not_balances(self):
        row={**self.observed(),'resource_effect_refs':['state/finance-ledger.json']}
        validate_event_candidate(row,ROOT,self.records)
        with self.assertRaisesRegex(ValueError,'never a new balance'):
            validate_event_candidate({**row,'resource_effect_refs':['state/checkpoint.json']},ROOT,self.records)
        with self.assertRaisesRegex(ValueError,'resource references'):
            validate_event_candidate({**row,'resource_effect_refs':[{'amount_cp':100}]},ROOT,self.records)

    def test_source_quote_and_normalized_path_required(self):
        for e in [{'source_ref':'../outside.md','quote':'x'},{'source_ref':'entities/characters/tomas.md','quote':'unrecorded work completed'},{'source_ref':'missing.md','quote':'x'}]:
            with self.subTest(e=e),self.assertRaises(ValueError):evidence(ROOT,e)

    def test_valid_unstarted_clock_has_no_effect(self):
        before=(ROOT/'state/checkpoint.json').read_bytes()
        validate_public_clock_proposal(self.clock(),ROOT,self.records)
        self.assertEqual((ROOT/'state/checkpoint.json').read_bytes(),before)

    def test_clock_cannot_import_archived_progress_or_start_countdown(self):
        for key,value in [('current_verified_progress',3),('last_verified_date','Day181'),('approval_ref','approved'),('starting_condition_ref','archived clock'),('trigger_refs',['tomorrow']),('possible_consequences',['guaranteed discovery']),('automatic',True)]:
            with self.subTest(key=key),self.assertRaises(ValueError):validate_public_clock_proposal({**self.clock(),key:value},ROOT,self.records)

    def test_clock_cannot_be_active_or_secret(self):
        for key,value in [('classification','CONFIRMED CANON'),('visibility','gm-secret'),('owner_ref','tomas'),('source_refs',[])]:
            with self.subTest(key=key),self.assertRaises(ValueError):validate_public_clock_proposal({**self.clock(),key:value},ROOT,self.records)

    def test_candidate_validators_have_no_write_or_apply_interface(self):
        import scripts.autonomy as module
        self.assertFalse(any(hasattr(module,x) for x in ('advance_time','apply_event','tick_clock','write_state','send_message')))

if __name__=='__main__':unittest.main()
