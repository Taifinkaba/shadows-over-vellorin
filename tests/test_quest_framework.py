"""Finite quest design remains a proposal; source history and blank secrets are protected."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.quest_framework import validate_graph, readiness_report
from scripts.validate import ValidationError, validate

ROOT=Path(__file__).resolve().parents[1]


class QuestFrameworkTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-quest-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for directory in ('entities','state','archive','changes'):shutil.copytree(ROOT/directory,self.root/directory)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):return self.root/f"entities/{'rules' if ident=='quest-continuation-and-completion' else 'mechanics'}/{ident}.md"

    def data(self,ident):return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,fn):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);fn(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,ident,fn):
        self.edit(ident,fn)
        with self.assertRaises(ValidationError):validate(self.root)

    def test_current_repository_and_missing_prospective_approvals_valid(self):
        result=validate(self.root)
        self.assertIn(f"{len(json.loads((self.root/'index.json').read_text())['entries'])} entity records",result);self.assertIn('pending 18 answer approvals / 14 clue routes',result)

    def test_all_preexisting_campaign_state_and_history_unchanged(self):
        fixture=json.loads((ROOT/'tests/fixtures/chunk9-preservation.json').read_text())
        for path,digest in fixture['sha256'].items():
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)

    def test_readiness_reports_blockers_without_secret_values(self):
        r=readiness_report(self.root)
        self.assertEqual(len(r['missing_answer_approvals']),18);self.assertEqual(len(r['unfilled_clue_route_ids']),14)
        self.assertEqual(len(r['core_design_approval_ids']),10);self.assertEqual(len(r['optional_design_approval_ids']),8)
        self.assertTrue(r['baseline_valid']);self.assertIn('BLOCKED',r['play_activation'])
        self.assertNotIn('values',r);self.assertNotIn('definitive_answer',json.dumps(r))
        self.assertIn('optional questions are not ending prerequisites',r['note'])

    def test_cli_readiness_is_readonly_and_validates_first(self):
        before=(self.root/'state/checkpoint.json').read_bytes()
        result=subprocess.run([sys.executable,str(ROOT/'scripts/quest_framework.py'),'--readiness','--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(len(json.loads(result.stdout)['missing_answer_approvals']),18)
        self.assertEqual(before,(self.root/'state/checkpoint.json').read_bytes())
        self.edit('quest-answer-blueprint',lambda d:d['pending_answers'][0]['values'].update(definitive_answer='invented'))
        result=subprocess.run([sys.executable,str(ROOT/'scripts/quest_framework.py'),'--readiness','--root',str(self.root)],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0);self.assertNotIn('invented',result.stdout)

    def test_all_validation_is_readonly(self):
        before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('entities','state','archive','changes') for p in (self.root/folder).rglob('*') if p.is_file()}
        validate(self.root);readiness_report(self.root)
        self.assertEqual(before,{path:hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in before})

    def test_completed_restoration_is_not_entire_case_or_guardian_resolution(self):
        v=(self.root/'entities/quests/v9-memories.md').read_text();f=(self.root/'entities/quests/first-hour-restoration.md').read_text()
        self.assertIn('status: completed',v);self.assertIn('broader Crown/Witness investigations continue',v)
        self.assertIn('status: active',f);self.assertIn('First Hour restoration completed',f)
        self.assertIn('wider Guardian restoration remains active',f)

    def test_prevented_activation_is_not_permanent_threat_resolution(self):
        s=(self.root/'entities/quests/fifth-bell-threat.md').read_text()
        self.assertIn('status: active',s);self.assertIn('activation prevented',s)
        self.assertIn('Surviving conspiracy branches remain open',s)
        self.assertIn('Never sounded through Day156',(self.root/'entities/items/fifth-bell.md').read_text())

    def test_identity_crosswalk_uses_existing_malrec_and_separate_corvens(self):
        people={x['character_id'] for x in self.data('quest-history-and-identities')['distinct_people']}
        self.assertIn('malrec',people);self.assertNotIn('malrec-voss',people)
        self.assertTrue({'corven','corven-north-return-house','corvin-hale','corvin-halbrecht'}<=people)

    def test_source_custody_and_discovery_are_not_new_inventory(self):
        d=self.data('quest-evidence-and-mysteries')
        self.assertEqual(len(d['clues']),17);self.assertEqual(d['new_evidence_items'],[])
        for row in d['clues']:self.assertFalse(row['new_item']);self.assertEqual(row['knowledge'],'requires-discovery-review')
        leaf=next(x for x in d['clues'] if x['clue_id']=='clue:third-leaf')
        copyref=next(x for x in d['clues'] if x['clue_id']=='clue:leaf-transcription')
        self.assertNotEqual(leaf['source_locator'],copyref['source_locator'])

    def test_optional_legal_reviews_are_not_required_to_end_main_quest(self):
        rows={x['mystery_id']:x for x in self.data('quest-evidence-and-mysteries')['mysteries']}
        for ident in ('thane-review','sorn-review','remaining-notices','a07-consent','correspondent','watcher','freight-director','damaged-channels'):
            self.assertEqual(rows['mystery:'+ident]['proposed_objective_ids'],[])
        objectives=self.data('quest-resolution-proposals')['objectives']
        self.assertEqual(len(objectives),7)
        self.assertTrue(all(all(x.startswith('objective:') for x in row['depends_on']) for row in objectives))

    def test_blueprint_is_entirely_unfilled_not_metadata_spoilers(self):
        d=self.data('quest-answer-blueprint')
        for row in d['pending_answers']:
            self.assertTrue(all(v is None for v in row['values'].values()));self.assertIsNone(row['private_storage_ref'])
        self.assertFalse(d['public_secret_values_allowed']);self.assertEqual(d['new_fixed_answers'],[])

    def test_partial_framework_rejected(self):
        self.path('quest-answer-blueprint').unlink()
        p=self.root/'index.json';d=json.loads(p.read_text());d['entries']=[x for x in d['entries'] if x['id']!='quest-answer-blueprint'];p.write_text(json.dumps(d))
        with self.assertRaises(ValidationError):validate(self.root)

    def test_secret_owner_never_added_to_public_routing(self):
        self.reject('main-quest-map',lambda d:d['quest_owners'].append({'quest_id':'twin-sword-origin','source_ref':'entities/quests/twin-sword-origin.md','knowledge':'requires-discovery-review'}))


CASES={
 'duplicate_quest_id':('main-quest-map',lambda d:d['quest_owners'].__setitem__(0,copy.deepcopy(d['quest_owners'][1]))),
 'unknown_quest_owner':('main-quest-map',lambda d:d['quest_owners'][0].update(quest_id='new-quest')),
 'wrong_quest_owner_type':('main-quest-map',lambda d:d['quest_owners'][0].update(quest_id='theron-ashvale')),
 'automatic_quest_status':('main-quest-map',lambda d:d['new_quest_statuses'].append('completed')),
 'automatic_rewards':('main-quest-map',lambda d:d['new_rewards'].append({'gp':100})),
 'copied_mutable_quest_status':('main-quest-map',lambda d:d['quest_owners'][0].update(status='completed')),
 'index_as_knowledge':('main-quest-map',lambda d:d['quest_owners'][0].update(knowledge='player-known')),
 'reopen_completed_objective':('quest-history-and-identities',lambda d:d['historical_objectives'][0].update(classification='PROPOSED')),
 'invented_historical_quote':('quest-history-and-identities',lambda d:d['historical_objectives'][0]['evidence_ref'].update(quote='All V-9 cases resolved.')),
 'victory_scope_expanded':('quest-history-and-identities',lambda d:d['historical_objectives'][0].update(scope_limit='All V-9 cases are solved.')),
 'historical_objective_status_rewrite':('quest-history-and-identities',lambda d:d['historical_objectives'][0].update(status='active')),
 'identity_merge':('quest-history-and-identities',lambda d:d['identity_mergers'].append(['aldric-voss','elian-voss'])),
 'shared_title_as_identity':('quest-history-and-identities',lambda d:d['distinct_people'][0].update(alias_of='maelor-thane')),
 'new_prison_destination':('quest-history-and-identities',lambda d:d['new_custody_events'].append({'destination':'proposed-prison'})),
 'new_historical_conviction':('quest-history-and-identities',lambda d:d['new_historical_outcomes'].append('convicted')),
 'duplicate_evidence_id':('quest-evidence-and-mysteries',lambda d:d['clues'].__setitem__(0,copy.deepcopy(d['clues'][1]))),
 'duplicate_evidence_scope':('quest-evidence-and-mysteries',lambda d:d['clues'][0].update(source_locator=copy.deepcopy(d['clues'][1]['source_locator']))),
 'new_evidence_item':('quest-evidence-and-mysteries',lambda d:d['clues'][0].update(new_item=True)),
 'custody_transfer':('quest-evidence-and-mysteries',lambda d:d['clues'][0].update(custody_owner_ref='theron-ashvale')),
 'invalid_discovery_source':('quest-evidence-and-mysteries',lambda d:d['clues'][0].update(discovery_owner_ref='missing-quest')),
 'deep_probe_invention':('quest-evidence-and-mysteries',lambda d:d['clues'][10]['source_locator'].update(quote='All unrestricted memories extracted.')),
 'theory_as_authenticated_document':('quest-evidence-and-mysteries',lambda d:d['clues'][13].update(evidence_type='authenticated-document')),
 'theory_as_verified_new_type':('quest-evidence-and-mysteries',lambda d:d['clues'][13].update(evidence_type='proven-answer')),
 'duplicate_mystery_id':('quest-evidence-and-mysteries',lambda d:d['mysteries'].__setitem__(0,copy.deepcopy(d['mysteries'][1]))),
 'invented_mystery_answer':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0].update(unknown_answer='invented mechanism')),
 'mystery_closed':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0].update(answer_approval='resolved')),
 'mystery_owner_merger':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0].update(quest_owner_id='v9-memories')),
 'new_discovery':('quest-evidence-and-mysteries',lambda d:d['new_discoveries'].append('mastermind found')),
 'missing_freshness_source':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0]['freshness_refs'].pop()),
 'unverified_discovery_as_player_knowledge':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0].update(knowledge='player-known')),
 'missing_clue_reference':('quest-evidence-and-mysteries',lambda d:d['mysteries'][0]['clue_ids'].append('clue:missing')),
 'optional_review_becomes_mandatory':('quest-evidence-and-mysteries',lambda d:d['mysteries'][8].update(proposed_objective_ids=['objective:command-chain'],main_ending_role='PROPOSED CORE')),
 'chapter_plan_promoted':('quest-resolution-proposals',lambda d:d.update(classification='CONFIRMED CANON')),
 'chapter_target_changed':('quest-resolution-proposals',lambda d:d['chapters'][0].update(target_scenes=30)),
 'boolean_scene_count':('quest-resolution-proposals',lambda d:d['chapters'][0].update(target_scenes=True)),
 'missing_required_chapter':('quest-resolution-proposals',lambda d:d['chapters'].pop()),
 'unreachable_chapter':('quest-resolution-proposals',lambda d:d['chapters'][0].update(next_ids=[])),
 'chapter_cycle':('quest-resolution-proposals',lambda d:d['chapters'][-1].update(next_ids=['chapter:gray-ledger'])),
 'unknown_chapter_transition':('quest-resolution-proposals',lambda d:d['chapters'][0].update(next_ids=['chapter:secret-site'])),
 'repeated_mandatory_search':('quest-resolution-proposals',lambda d:d['chapters'][0].update(mandatory_repeat=True)),
 'forced_chapter_order':('quest-resolution-proposals',lambda d:d['chapters'][0].update(can_combine_or_reorder=False)),
 'duplicate_mandatory_objective':('quest-resolution-proposals',lambda d:d['chapters'][1]['objective_ids'].append('objective:command-chain')),
 'optional_quest_dependency':('quest-resolution-proposals',lambda d:d['objectives'][0].update(depends_on=['estate-expansion'])),
 'objective_cycle':('quest-resolution-proposals',lambda d:d['objectives'][0].update(depends_on=['objective:immediate-consequences'])),
 'reopen_victory_as_dependency':('quest-resolution-proposals',lambda d:d['objectives'][0].update(depends_on=['resolution:lyanna-restoration'])),
 'unapproved_route_location':('quest-resolution-proposals',lambda d:d['clue_route_slots'][0].update(location_id='ashvale-estate')),
 'route_activated_without_answer':('quest-resolution-proposals',lambda d:d['clue_route_slots'][0].update(activation='active')),
 'guaranteed_probe_path':('quest-resolution-proposals',lambda d:d['clue_route_slots'][0].update(method='Mental Probe required')),
 'unapproved_scene_outcome':('quest-resolution-proposals',lambda d:d['new_scene_outcomes'].append('victory')),
 'unplayed_ending':('quest-resolution-proposals',lambda d:d['new_quest_completions'].append('first-oath-conspiracy')),
 'side_quest_erased':('quest-resolution-proposals',lambda d:d['optional_domains'].remove('independent-legal-proceedings')),
 'hidden_mastermind':('quest-answer-blueprint',lambda d:d['pending_answers'][0]['values'].update(responsible_actor_or_institution='new mastermind')),
 'hidden_location':('quest-answer-blueprint',lambda d:d['pending_answers'][0]['values'].update(physical_location='unrevealed location')),
 'hidden_mechanism':('quest-answer-blueprint',lambda d:d['pending_answers'][0]['values'].update(method='unrevealed mechanism')),
 'hidden_betrayal_metadata':('quest-answer-blueprint',lambda d:d['pending_answers'][0].update(secret_betrayal='spoiler')),
 'public_secret_storage_claim':('quest-answer-blueprint',lambda d:d.update(storage_status='gm-secret metadata is private')),
 'answer_approval_without_source':('quest-answer-blueprint',lambda d:d['pending_answers'][0].update(approval_status='approved')),
 'invented_private_storage_ref':('quest-answer-blueprint',lambda d:d['pending_answers'][0].update(private_storage_ref='hidden-answer')),
 'answers_published':('quest-answer-blueprint',lambda d:d.update(public_secret_values_allowed=True)),
 'new_fixed_answer':('quest-answer-blueprint',lambda d:d['new_fixed_answers'].append('answer')),
 'duplicate_answer_crosswalk':('quest-answer-blueprint',lambda d:d['pending_answers'].__setitem__(0,copy.deepcopy(d['pending_answers'][1]))),
 'automatic_completion':('quest-continuation-and-completion',lambda d:d.update(automatic_completion=True)),
 'resource_reward':('quest-continuation-and-completion',lambda d:d['new_rewards'].append({'amount_cp':100})),
 'world_event_advancement':('quest-continuation-and-completion',lambda d:d['new_world_events'].append('retaliation')),
 'custody_transfer_procedure_execution':('quest-continuation-and-completion',lambda d:d['new_custody_transfers'].append('new prison')),
 'knowledge_leak':('quest-continuation-and-completion',lambda d:d['new_knowledge_disclosures'].append('secret answer')),
 'competing_resource_owner':('quest-continuation-and-completion',lambda d:d['system_owner_refs'].__setitem__(0,'main-quest-map')),
}
for name,(ident,fn) in CASES.items():
    def case(self,ident=ident,fn=fn):self.reject(ident,fn)
    setattr(QuestFrameworkTests,'test_reject_'+name,case)


class FiniteGraphTests(unittest.TestCase):
    def test_valid_branching_plan_has_finite_ending(self):
        validate_graph(['a','b','c','z'],{'a':['b','c'],'b':['z'],'c':['z'],'z':[]},'a','z')

    def test_missing_nodes_duplicates_cycles_and_dead_ends_rejected(self):
        cases=[(['a','a'],{'a':[]},None,None),(['a','z'],{'a':['missing'],'z':[]},'a','z'),(['a','z'],{'a':['a','z'],'z':[]},'a','z'),(['a','b','z'],{'a':['z'],'b':[],'z':[]},'a','z'),(['a','b','z'],{'a':['b','z'],'b':[],'z':[]},'a','z')]
        for args in cases:
            with self.subTest(args=args),self.assertRaises(ValueError):validate_graph(*args)

if __name__=='__main__':unittest.main()
