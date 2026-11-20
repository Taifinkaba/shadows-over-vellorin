"""High-value autonomy boundaries: public design is never an executed world action."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from case_support import isolated_case, validate_scope, validate_scope
from snapshot_helpers import SUNCREST262_REVISED_AUTHORITIES
from scripts.autonomy_designs import (FIGURES, EVENT_FIELDS, SCHEDULE_FIELDS, check_resolution_evidence,
    check_schedule_evidence, check_knowledge_claim)
from scripts.validate import validate, ValidationError

ROOT=Path(__file__).resolve().parents[1]


class ApprovedAutonomyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def payload(self,ident):
        p=self.root/f'entities/{"rules" if ident=="npc-autonomy-and-time" else "characters"}/{ident}.md'
        return p,json.loads(re.search(r'```json\n(.*?)\n```',p.read_text(),re.S)[1])

    def reject(self,ident,change,pattern):
        p,d=self.payload(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S)
        change(d['approved_autonomy_design' if ident=='npc-autonomy-and-time' else 'autonomy_design'])
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])
        with self.assertRaisesRegex(ValidationError,pattern):validate_scope(self.root, 'autonomy')

    def test_eight_unique_designs_and_prior_identities(self):
        entries=json.loads((self.root/'index.json').read_text())['entries'];ids=[e['id'] for e in entries]
        self.assertEqual(len(ids),len(set(ids)));self.assertIn(f'{len(entries)} entity records',validate(self.root))
        for ident,(age,region) in FIGURES.items():
            with self.subTest(ident=ident):
                _,d=self.payload(ident);a=d['autonomy_design'];self.assertEqual((a['age'],a['regional_association']),(age,region))
                self.assertEqual(a['identity_owner_ref'],ident);self.assertEqual(a['actual_actions'],[])
        _,a=self.payload('aveline-hartwell');self.assertEqual(a['character_design']['existing_proposal_id'],'proposal:officer-aveline-hartwell')
        for ident in ('mira-lodge-helper','mira-thorne','orenic','orven-pell'):self.assertIn(ident,ids)

    def test_no_appointments_possessions_or_secret_design_payloads(self):
        for ident in FIGURES:
            for field,value in [('current_office_id','speaker'),('current_location','ashvale-estate'),('current_job','owner'),
                                ('known_resources',['100gp']),('actual_appointments',['queen']),('actual_relationship_changes',['friend']),('secret_facts',['hidden plan'])]:
                with self.subTest(ident=ident,field=field),isolated_case(self):
                    self.reject(ident,lambda d,f=field,v=value:d.update({f:v}),'no possessions')

    def test_no_schedules_events_finance_or_knowledge_changes(self):
        for field,value in [('actual_schedules',['work']),('actual_events',['harvest']),('actual_knowledge_changes',['secret']),
                            ('actual_relationship_changes',['betrayal']),('automatic_resolution',True)]:
            with self.subTest(field=field),isolated_case(self):
                self.reject('npc-autonomy-and-time',lambda d,f=field,v=value:d.update({f:v}),'no autonomous')
        for field in ('resources','action','time_advance_evidence','actor_knowledge','owner_updates'):
            with self.subTest(field=field),isolated_case(self):
                self.reject('npc-autonomy-and-time',lambda d,f=field:d['event_template'].update({f:'completed'}),'empty template')

    def test_existing_authorities_and_communication_cannot_be_replaced(self):
        for field in ('ledger','economy','communications','chronology','law'):
            with self.subTest(field=field),isolated_case(self):
                self.reject('npc-autonomy-and-time',lambda d,f=field:d['authority_refs'].update({f:'unsupported-authority'}),'competing chronology')
        with isolated_case(self):self.reject('npc-autonomy-and-time',lambda d:d['character_design_ids'].__setitem__(0,'mira-hearthwick'),'duplicate/missing')

    def test_causal_resolution_evidence_is_finite_and_complete(self):
        good=dict.fromkeys(EVENT_FIELDS,'documented reviewed evidence');self.assertTrue(check_resolution_evidence(good))
        for field in EVENT_FIELDS:
            with self.subTest(field=field),self.assertRaises(ValueError):check_resolution_evidence(good|{field:None})
        for value in ({'available':float('inf')},{'spent':None},False):
            with self.subTest(value=value),self.assertRaises(ValueError):check_resolution_evidence(good|{'resources':value})
        good['resource_changes']={'cp':0};self.assertTrue(check_resolution_evidence(good))

    def test_schedule_stages_do_not_imply_completion(self):
        proposed=dict.fromkeys(SCHEDULE_FIELDS,None);proposed['status']='proposed-schedule'
        self.assertTrue(check_schedule_evidence(proposed))
        for stage in ('attempted-action','completed-action','verified-outcome'):
            with self.subTest(stage=stage),self.assertRaises(ValueError):check_schedule_evidence(proposed|{'status':stage})
        complete=dict.fromkeys(SCHEDULE_FIELDS,'reviewed evidence');complete['status']='verified-outcome'
        self.assertTrue(check_schedule_evidence(complete))
        for field in ('verified_route','resources','consent','weather','physical_limits'):
            with self.subTest(field=field),self.assertRaises(ValueError):check_schedule_evidence(complete|{field:None})

    def test_knowledge_requires_receipt_and_rumor_stays_unverified(self):
        for kind in ('direct-observation','received-report','rumor'):
            with self.subTest(kind=kind):
                with self.assertRaises(ValueError):check_knowledge_claim(kind,None,'discovery')
                with self.assertRaises(ValueError):check_knowledge_claim(kind,'received',None)
        self.assertEqual(check_knowledge_claim('rumor','heard','source'),'UNVERIFIED RUMOR')
        with self.assertRaises(ValueError):check_knowledge_claim('unsent-message','sent','claimed')

    def test_unaffected_companion_and_location_sources_are_unchanged(self):
        fixture=json.loads((ROOT/'tests/fixtures/phase2-07-preservation.json').read_text())
        for path in ('entities/creatures/alpha.md','entities/creatures/shade.md','entities/mechanics/independent-assignments.md',
                     'entities/locations/brackenford.md'):
            with self.subTest(path=path):self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),SUNCREST262_REVISED_AUTHORITIES.get(path, {}).get('after_sha256', fixture['unchanged_sha256'][path]))
        self.assertIn('Independent larger white Frostfang', (ROOT/'entities/creatures/alpha.md').read_text())
        self.assertIn('bond3/5 (supersedes earlier5/5)', (ROOT/'entities/creatures/shade.md').read_text())
