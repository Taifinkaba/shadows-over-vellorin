"""Dashboard projections are read-only, source-bound, conservative and disposable."""
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

from scripts.gm_dashboard import build_dashboard,verify_view,render_markdown
from scripts.validate import validate,ValidationError

ROOT=Path(__file__).resolve().parents[1]


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-dashboard-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')
        from snapshot_helpers import restore_day156
        restore_day156(self.root)

    def edit_json(self,path,change):
        p=self.root/path;d=json.loads(p.read_text());change(d);p.write_text(json.dumps(d))

    def edit_payload(self,path,change):
        p=self.root/path;s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self,path,fn):
        self.edit_payload(path,fn)
        with self.assertRaises(ValidationError):validate(self.root)

    def test_current_repository_valid_dynamic_entity_total(self):
        count=len(json.loads((self.root/'index.json').read_text())['entries'])
        self.assertIn(f'{count} entity records',validate(self.root))

    def test_every_protected_campaign_record_byte_preserved(self):
        f=json.loads((ROOT/'tests/fixtures/chunk10-preservation.json').read_text())
        for path,digest in f['sha256'].items():
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)

    def test_generation_and_validation_write_nothing(self):
        def hashes():return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}
        before=hashes();v=build_dashboard(self.root);render_markdown(v);verify_view(self.root,v)
        self.assertEqual(before,hashes());self.assertFalse((self.root/'state/world-state.json').exists())

    def test_current_scene_and_finite_resource_snapshot(self):
        d=build_dashboard(self.root)['sections'];scene=d['current_scene'];h=d['theron']
        self.assertEqual(scene['date']['value'],'Year 848 Day 156');self.assertEqual(scene['calendar']['value'],{'season':'Suncrest','day_of_season':36})
        self.assertEqual(scene['time']['value'],'20:15');self.assertEqual(scene['location']['value'],'Ashvale Estate family sitting room');self.assertEqual(scene['status']['value'],'ENDED')
        expected={'hp':100,'hp_max':100,'mp':378,'mp_max':400,'defense':46,'equipped_defense':49,'staff_mp':156,'staff_mp_max':180,'wagon_mp':60,'wagon_mp_max':60,'defense_if_night_sovereign_worn':51,'night_sovereign_worn_bonus':2}
        for key,value in expected.items():self.assertEqual(h[key]['value'],value)
        self.assertTrue(h['night_sovereign_carried_not_equipped']['value']);self.assertTrue(h['chronos_eye_locked']['value']);self.assertTrue(h['dragon_slayer_locked']['value'])

    def test_money_commitments_and_exclusions_are_not_added_twice(self):
        f=build_dashboard(self.root)['sections']['finances']
        self.assertEqual([f[x]['value'] for x in ('controlled_cp','committed_unpaid_cp','uncommitted_cp')],[77190,31700,45490])
        self.assertEqual(sum(x['balance_cp']['value'] for x in f['accounts']),77190)
        self.assertEqual(f['controlled_display']['value'],'771 gp 9 sp 0 cp');self.assertEqual(f['committed_unpaid_display']['value'],'317 gp 0 sp 0 cp')
        self.assertEqual(f['currency']['value'],{'unit':'cp','cp_per_gp':100,'cp_per_sp':10})
        self.assertFalse(f['construction_started']['value']);self.assertIsNone(f['accounting_gaps']['value'])
        cottage=next(x for x in f['excluded_holdings'] if x['holding_id']['value']=='briarstone_cottage')
        self.assertEqual(cottage['amount_cp']['value'],5500);self.assertIsNone(cottage['amount_cp']['as_of'])

    def test_only_explicit_checkpoint_presence_is_current(self):
        d=build_dashboard(self.root)['sections'];rows=d['companions']+d['personnel']
        known={x['person']['value'] for x in rows if x['last_verified_location']['value'] is not None}
        self.assertEqual(known,{'aric-ashvale','therons-mother'})
        for ident in ('alpha','garrick-vale','nyx-thorne','master-beren','tomas'):
            row=next(x for x in rows if x['person']['value']==ident)
            self.assertIsNone(row['last_verified_location']['value']);self.assertIsNone(row['source_date']['value'])
        self.assertNotIn('tomas',{x['person']['value'] for x in d['companions']})

    def test_academy_management_does_not_pool_independent_money(self):
        rows=build_dashboard(self.root)['sections']['estate_and_academy'];a=next(x for x in rows if x['property']['value']=='dragon-slayer-academy')
        self.assertEqual(a['manager_id']['value'],'master-beren');self.assertIsNone(a['legal_owner_id']['value'])
        self.assertIn('independent',a['financial_ownership']['value']);self.assertIsNone(a['operations_and_projects']['value'])

    def test_quest_and_world_values_do_not_claim_completion_or_clearance(self):
        d=build_dashboard(self.root)['sections'];q=d['quests'];self.assertEqual(q['approval_gaps']['value'],{'core_design_approval_ids':10,'optional_design_approval_ids':8});self.assertEqual(q['unfilled_clue_routes']['value'],14)
        first=next(x for x in q['metadata'] if x['quest_id']['value']=='first-hour-restoration');self.assertEqual(first['status']['value'],'active')
        rows=d['world']['dungeon_sections'];west=next(x for x in rows if 'western-gallery' in x['section_id']['value'])
        self.assertEqual(west['exploration']['value'],'unexplored')
        keeper=next(x for x in rows if 'keeper' in x['section_id']['value'])
        self.assertEqual(keeper['exploration']['value'],'unknown');self.assertEqual(keeper['access']['value'],'protected')
        self.assertTrue(all('pending' in x['current_result']['value'] for x in d['world']['legal_reviews']))

    def test_every_display_leaf_has_valid_source_asof_and_qualification(self):
        def inspect(x):
            if isinstance(x,dict) and 'value' in x:
                self.assertEqual(set(x),{'value','source_ref','as_of','qualification'})
                path=x['source_ref'].split('#',1)[0];self.assertTrue((self.root/path).is_file());self.assertTrue(x['qualification'])
            elif isinstance(x,dict):
                for v in x.values():inspect(v)
            elif isinstance(x,list):
                for v in x:inspect(v)
            else:self.fail('unsourced displayed leaf')
        inspect(build_dashboard(self.root)['sections'])

    def test_mixed_narrative_and_private_text_are_not_projected(self):
        sentinel='UNREVEALED_PRIVATE_SENTINEL'
        for path in ('entities/characters/lyanna-ashvale.md','entities/characters/theron-ashvale.md','state/open-verifications.md','state/next-chat-handoff.md'):
            p=self.root/path;p.write_text(p.read_text()+'\n'+sentinel+'\n')
        view=build_dashboard(self.root)
        self.assertNotIn(sentinel,json.dumps(view));self.assertNotIn(sentinel,render_markdown(view))
        self.assertNotIn('ashvale-lifeline',json.dumps(view));self.assertNotIn('twin-sword-origin',json.dumps(view))

    def test_unknown_source_phrase_produces_unknown_not_an_invented_bonus(self):
        p=self.root/'entities/items/night-sovereign.md';p.write_text(p.read_text().replace('+2 equipped DEF while worn','Worn bonus unverified'))
        h=build_dashboard(self.root)['sections']['theron'];self.assertIsNone(h['night_sovereign_worn_bonus']['value']);self.assertIsNone(h['defense_if_night_sovereign_worn']['value'])

    def test_new_gm_secret_entity_is_excluded_from_output(self):
        p=self.root/'entities/characters/secret-test.md'
        p.write_text('---\nid: secret-test\ntype: characters\nstatus: gm-secret-locked\nvisibility: gm-secret\nsource_refs:\n- changes/chronicles/gm-continuity-maintenance.md\n---\n\nHidden mastermind SECRET-SENTINEL\n')
        self.edit_json('index.json',lambda d:d['entries'].append({'id':'secret-test','type':'characters','title':'SECRET-SENTINEL','path':'entities/characters/secret-test.md','status':'gm-secret-locked','visibility':'gm-secret','tags':[]}))
        view=build_dashboard(self.root);self.assertNotIn('secret-test',json.dumps(view));self.assertNotIn('SECRET-SENTINEL',json.dumps(view))

    def test_source_visibility_changes_fail_closed(self):
        p=self.root/'entities/items/night-sovereign.md';p.write_text(p.read_text().replace('visibility: gm-reference','visibility: gm-secret'))
        self.edit_json('index.json',lambda d:[row.update(visibility='gm-secret') for row in d['entries'] if row['id']=='night-sovereign'])
        with self.assertRaises(ValueError):build_dashboard(self.root)

    def test_stale_or_edited_view_rejected_and_regeneration_current(self):
        old=build_dashboard(self.root);verify_view(self.root,old)
        p=self.root/'entities/creatures/alpha.md';p.write_text(p.read_text()+'\nSource freshness test; no changed outcome.\n')
        with self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,old)
        fresh=build_dashboard(self.root);verify_view(self.root,fresh)
        changed=copy.deepcopy(fresh);changed['sections']['finances']['controlled_cp']['value']=74590
        with self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,changed)

    def test_saved_view_cannot_substitute_float_or_boolean_for_integer(self):
        view=build_dashboard(self.root)
        for section,key,bad in [('finances','controlled_cp',77190.0),('theron','chronos_eye_locked',1)]:
            candidate=copy.deepcopy(view);candidate['sections'][section][key]['value']=bad
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,candidate)

    def test_source_owned_section_change_is_read_fresh_without_reset(self):
        before=build_dashboard(self.root);p=self.root/'entities/mechanics/shady-salvage.md'
        text=p.read_text();self.assertIn('| Hollow western gallery | Unexplored',text)
        p.write_text(text.replace('| Hollow western gallery | Unexplored','| Hollow western gallery | Visited'))
        after=build_dashboard(self.root)
        row=next(x for x in after['sections']['world']['dungeon_sections'] if 'western-gallery' in x['section_id']['value'])
        self.assertEqual(row['exploration']['value'],'visited')
        with self.assertRaisesRegex(ValueError,'stale'):verify_view(self.root,before)

    def test_unadopted_snapshot_cannot_override_repository_authority(self):
        d=build_dashboard(self.root)['sections'];self.assertIn('UNADOPTED',d['verification_warnings']['later_supplied_snapshot']['value'])
        self.assertEqual(d['theron']['mp']['value'],378);self.assertEqual(d['finances']['controlled_cp']['value'],77190)

    def test_markdown_has_independent_closed_controls_and_personnel_columns(self):
        text=render_markdown(build_dashboard(self.root))
        self.assertGreaterEqual(text.count('<details>'),9);self.assertEqual(text.count('<details>'),text.count('</details>'))
        self.assertNotRegex(text,r'<details\s+open');self.assertIn('| Person | Assignment | Status |',text)
        self.assertIn('<summary>Personnel</summary>',text);self.assertIn('<summary>Dungeon Sections</summary>',text)

    def test_cli_json_markdown_and_check_view(self):
        command=[sys.executable,str(ROOT/'scripts/gm_dashboard.py'),'--root',str(self.root)]
        result=subprocess.run(command,capture_output=True,text=True);self.assertEqual(result.returncode,0,result.stderr)
        viewfile=Path(self.temp.name)/'saved-view.json';viewfile.write_text(result.stdout)
        checkresult=subprocess.run(command+['--check-view',str(viewfile)],capture_output=True,text=True);self.assertEqual(checkresult.returncode,0,checkresult.stderr)
        result=subprocess.run(command+['--format','markdown'],capture_output=True,text=True);self.assertEqual(result.returncode,0,result.stderr);self.assertIn('<details>',result.stdout)
        view=json.loads(viewfile.read_text());view['sections']['current_scene']['status']['value']='ACTIVE';viewfile.write_text(json.dumps(view))
        result=subprocess.run(command+['--check-view',str(viewfile)],capture_output=True,text=True);self.assertNotEqual(result.returncode,0)

    def test_unsupported_snapshot_schema_fails_visibly(self):
        self.edit_json('state/checkpoint.json',lambda d:d.update(schema_version=999))
        with self.assertRaises(ValueError):build_dashboard(self.root)

    def test_missing_document_or_invalid_template_links_fail(self):
        p=self.root/'docs/end-session-codex-template.md';p.unlink()
        with self.assertRaises(ValueError):validate(self.root)

    def test_broken_workflow_link_fails(self):
        p=self.root/'docs/game-master-operating-manual.md';p.write_text(p.read_text()+'\n[Broken](missing-owner.md)\n')
        with self.assertRaisesRegex(ValueError,'broken'):validate(self.root)

    def test_escape_link_fails(self):
        p=self.root/'docs/game-master-operating-manual.md';p.write_text(p.read_text()+'\n[Escape](../../outside.md)\n')
        with self.assertRaisesRegex(ValueError,'escaping'):validate(self.root)

    def test_competing_world_state_file_rejected(self):
        for path in ('state/world-state.json','state/dashboard.json'):
            p=self.root/path;p.write_text('{"current_cash":1}')
            with self.assertRaisesRegex(ValueError,'competing'):validate(self.root)
            p.unlink()

    def test_partial_workflow_extension_rejected(self):
        (self.root/'entities/mechanics/gm-workflow.md').unlink()
        self.edit_json('index.json',lambda d:d.update(entries=[x for x in d['entries'] if x['id']!='gm-workflow']))
        with self.assertRaisesRegex(ValueError,'incomplete GM'):validate(self.root)


WORKFLOW='entities/mechanics/gm-workflow.md'
END='docs/end-session-codex-template.md';NEXT='docs/next-session-chat-template.md'
CASES={
 'duplicate_directory':(WORKFLOW,lambda d:d['directory_refs'].__setitem__(0,d['directory_refs'][1])),
 'missing_directory':(WORKFLOW,lambda d:d['directory_refs'].pop()),
 'invalid_document':(WORKFLOW,lambda d:d['document_refs'].__setitem__(0,'docs/missing.md')),
 'wrong_authority':(WORKFLOW,lambda d:d['authority_refs'].__setitem__(0,'twin-sword-origin')),
 'second_checkpoint':(WORKFLOW,lambda d:d.update(checkpoint_ref='archive/checkpoints/year847-day153-2205.json')),
 'second_ledger':(WORKFLOW,lambda d:d.update(finance_ref='state/checkpoint.json')),
 'raw_gm_rendering':(WORKFLOW,lambda d:d.update(dashboard_policy='RENDER ALL SOURCES')),
 'cached_world_balance':(WORKFLOW,lambda d:d.update(current_cash_cp=77190)),
 'invented_session':(WORKFLOW,lambda d:d['new_session_events'].append({'date':'Day181'})),
 'automatic_resource_posting':(WORKFLOW,lambda d:d['new_resource_postings'].append({'cp':6500})),
 'secret_disclosure':(WORKFLOW,lambda d:d['new_knowledge_disclosures'].append('hidden answer')),
 'automatic_writer':(WORKFLOW,lambda d:d.update(automatic_writes=True)),
 'unbounded_retrieval':(WORKFLOW,lambda d:d['retrieval_scenarios'].update(combat=['all-entities'])),
 'missing_handoff_section':(END,lambda d:d['handoff'].pop('companions')),
 'missing_last_player_decision':(END,lambda d:d['handoff']['session_identification'].pop('last_player_decision')),
 'missing_equipment_requirement':(END,lambda d:d['handoff']['character_resources'].pop('equipped_items')),
 'missing_excluded_holdings':(END,lambda d:d['handoff']['finances'].pop('excluded_holdings')),
 'missing_custody_requirement':(END,lambda d:d['handoff']['world_changes'].pop('custody')),
 'missing_codex_sources':(END,lambda d:d['handoff']['codex_instructions'].pop('source_evidence')),
 'missing_unchanged_systems':(END,lambda d:d['handoff']['codex_instructions'].pop('explicitly_unchanged_systems')),
 'populated_checkpoint':(END,lambda d:d['handoff']['session_identification'].update(date='Day156')),
 'hidden_template_answer':(END,lambda d:d['handoff']['open_issues'].update(mysteries='hidden mastermind')),
 'no_stop_after_end':(END,lambda d:d.update(stop_story=False)),
 'merge_without_approval':(END,lambda d:d.update(merge_requires_approval=False)),
 'unsupported_outcomes':(END,lambda d:d.update(apply_only_supported_outcomes=False)),
 'actual_session_template_flag':(END,lambda d:d.update(template_only=False)),
 'invented_template_verification':(END,lambda d:d.update(verified_as_of='Day181')),
 'cached_next_chat_state':(NEXT,lambda d:d.update(hardcoded_checkpoint={'mp':400})),
 'old_checkpoint_retrieval':(NEXT,lambda d:d.update(checkpoint_ref='archive/checkpoints/year847-day153-2205.json')),
 'next_chat_automatic_actions':(NEXT,lambda d:d.update(automatic_actions=True)),
 'next_chat_continues_after_end':(NEXT,lambda d:d.update(stop_on_end_session=False)),
 'next_chat_merge_without_approval':(NEXT,lambda d:d.update(merge_requires_approval=False)),
 'next_chat_missing_discovery_boundary':(NEXT,lambda d:d['retrieval_order'].remove('quest-and-discovery-boundaries')),
 'unknown_workflow_status':(WORKFLOW,lambda d:d.update(status='ACTIVE')),
}
for name,(path,fn) in CASES.items():
    def case(self,path=path,fn=fn):self.reject(path,fn)
    setattr(DashboardTests,'test_reject_'+name,case)

if __name__=='__main__':unittest.main()
