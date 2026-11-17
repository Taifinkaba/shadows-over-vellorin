from case_support import isolated_case, validate_scope
"""Government design approval must not become exercised power or historical custody."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.validate import ValidationError, validate, require, repository_file
from scripts.governments import REALMS, FIGURES, FACILITIES
from scripts.justice import TRANSFER_FIELDS, validate_transfer

ROOT=Path(__file__).resolve().parents[1]


class GovernmentDesignTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-governments-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self, ident):
        kind='locations' if ident in REALMS else 'characters' if ident in FIGURES else 'rules' if ident=='justice-and-jurisdiction' else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self, ident, change):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def reject(self, ident, change, pattern):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,pattern):validate_scope(self.root, 'justice', 'governments')


    def test_causality_and_continuity_1(self):
        with self.subTest(case='test_business_statuses_are_jurisdiction_sensitive'), isolated_case(self):
            l=self.data('justice-and-jurisdiction')['approved_legal_design']
            rules={r['id']:r for r in l['business_regulations']}
            self.assertEqual({x['design_status'] for x in rules['business-law:gambling']['realm_statuses']},{'REGULATED','TOLERATED'})
            self.assertEqual(len(l['business_links']),41)
            self.assertTrue(all(x['actual_license'] is None for x in l['business_links']))
        with self.subTest(case='test_no_automatic_legal_outcomes'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design'].update(automatic_outcomes=True),'no automatic political/legal')
        with self.subTest(case='test_existing_village_officials_and_all_twenty_roads_unchanged'), isolated_case(self):
            a=self.data('justice-authorities')['authorities']
            self.assertEqual(next(x for x in a if x['id']=='justice:brackenford-government')['leadership_ids'],['elsbeth-marrin'])
            self.assertEqual(next(x for x in a if x['id']=='justice:brackenford-watch')['leadership_ids'],['ressa-vale'])
            fixture=json.loads((ROOT/'tests/fixtures/phase2-03-preservation.json').read_text())
            roads=[p for p in fixture['unchanged_sha256'] if '/route-' in p]
            self.assertEqual(len(roads),20)
        with self.subTest(case='test_no_current_royal_appointment'), isolated_case(self):
            self.reject('valedorn',lambda d:d['government_design']['actual_appointments'].append('queen-installed'),'no actual appointments')
        with self.subTest(case='test_no_current_treasury_or_taxes'), isolated_case(self):
            self.reject('rivermere-league',lambda d:d['government_design'].update(current_treasury_cp=100),'resources must remain unknown')

    def test_continuity_and_contracts_and_schema_2(self):
        with self.subTest(case='test_facility_has_no_current_capacity_or_staffing'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'][1].update(exact_capacity=24),'custody, capacity')
        with self.subTest(case='test_all_five_governments_and_figure_ages'), isolated_case(self):
            self.assertIn('checkpoint valid',validate(self.root))
            for ident,form in REALMS.items():
                g=self.data(ident)['government_design'];self.assertEqual(g['form'],form)
                self.assertEqual(g['classification'],'APPROVED DESIGN')
                self.assertEqual(g['actual_appointments'],[]);self.assertIsNone(g['current_officeholders'])
                self.assertEqual({o['level'] for o in g['offices']},{'local','regional','realm'})
                self.assertIn('government:'+ident+'-local-courts',{o['id'] for o in g['offices']})
            for ident,age in FIGURES.items():self.assertEqual(self.data(ident)['character_design']['age'],age)
        with self.subTest(case='test_design_office_cannot_appoint_existing_captain'), isolated_case(self):
            self.reject('valedorn',lambda d:d['government_design']['offices'][0]['assigned_person_ids'].append('ressa-vale'),'no actual appointments')
        with self.subTest(case='test_no_court_across_all_realms'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design'].update(exclusive_cross_realm_court=True),'no universal court')
        with self.subTest(case='test_office_cannot_expand_to_another_realm'), isolated_case(self):
            self.reject('elyndor',lambda d:d['government_design']['offices'][0].update(scope_realm_id='valedorn'),'no cross-realm')

    def test_contracts_and_schema_3(self):
        cases = [
            ('test_capital_cannot_be_replaced', 'valedorn', lambda d: d['government_design'].update(capital_id='eastrun'), 'unsupported capital'),
            ('test_government_needs_approval_provenance', 'frostmarch', lambda d: d['government_design'].update(approval_source_ref='README.md'), 'wrong approval'),
            ('test_character_has_no_prior_meeting', 'elowen-marcrest', lambda d: d['character_design']['meetings_with_theron'].append('Day100 audience'), 'no actual appointments'),
            ('test_character_title_is_no_appointment', 'selene-harrow', lambda d: d['character_design'].update(current_office_id='justice:caelthorne-watch'), 'location and resources must remain unknown'),
            ('test_character_age_is_approved_design', 'durnek-stonevein', lambda d: d['character_design'].update(age=133), 'age/design mismatch'),
        ]
        for case, arg0, arg1, arg2 in cases:
            with self.subTest(case=case), isolated_case(self):
                self.reject(arg0, arg1, arg2)

    def test_contracts_and_schema_4(self):
        with self.subTest(case='test_aveline_cannot_take_an_office'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['officers'][0].update(candidate_office_id='Chief Justice'),'identity/appointment/relationship')
        with self.subTest(case='test_all_seven_facility_ids_reused_and_unknown'), isolated_case(self):
            fs=self.data('justice-proposals')['approved_facility_designs']
            self.assertEqual({f['proposal_id'] for f in fs},FACILITIES)
            for f in fs:
                self.assertEqual(f['classification'],'APPROVED DESIGN');self.assertIsNone(f['current_prisoners'])
                self.assertIsNone(f['exact_capacity']);self.assertEqual(f['operational_status'],'UNKNOWN')
        with self.subTest(case='test_facility_requires_a_valid_court_model'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'][0].update(court_design_authority_id='government:valedorn-treasury'),'judicial design role')
        with self.subTest(case='test_facility_cannot_become_operational'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'][0].update(operational_status='OPERATIONAL'),'cannot receive prisoners')
        with self.subTest(case='test_unknown_prisoners_is_not_zero'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'][1].update(current_prisoners=[]),'custody, capacity')

    def test_contracts_and_schema_5(self):
        with self.subTest(case='test_unlocated_prison_cannot_be_placed'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'][-1].update(candidate_location_id='caelthorne'),'not surveyed/relocated')
        with self.subTest(case='test_facility_design_is_blocked_by_existing_actual_transfer_guard'), isolated_case(self):
            f=self.data('justice-proposals')['approved_facility_designs'][1];ident=f['proposal_id']
            record={k:None for k in TRANSFER_FIELDS};record.update(case_id='fixture-only',status='completed',source_refs=[],
                 sending_authority_id='fixture-sender',receiving_authority_id='fixture-receiver',destination_facility_id=ident)
            authorities={k:dict(classification='CONFIRMED CANON') for k in ('fixture-sender','fixture-receiver')}
            with self.assertRaisesRegex(ValidationError,'nonoperational facility'):
                validate_transfer(record,self.root,{},authorities,{ident:f},require,repository_file)
        with self.subTest(case='test_offense_cannot_establish_conviction'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['offenses'][0]['actual_cases'].append('convicted'),'no actual appointments')
        with self.subTest(case='test_trial_authority_cannot_cross_realms'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['offenses'][0]['realm_treatment'][0].update(trial_authority_id='government:elyndor-regional-courts'),'scope mismatch')
        with self.subTest(case='test_required_offense_coverage'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['offenses'].pop(),'criminal code coverage')

    def test_contracts_and_schema_6(self):
        with self.subTest(case='test_business_cannot_gain_actual_license'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['business_links'][0].update(actual_license='issued'),'must remain unknown')
        with self.subTest(case='test_adult_workers_need_independent_agency'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:next(r for r in d['approved_legal_design']['business_regulations'] if r['id']=='business-law:adult-entertainment').update(compliance='Adult labor'), 'independence safeguards')
        with self.subTest(case='test_eight_crime_labels_not_faction_profiles'), isolated_case(self):
            r=self.data('justice-and-jurisdiction')['approved_legal_design']['organized_crime_responses']
            self.assertEqual(len(r),8)
            self.assertTrue(all(x['actual_investigations']==[] and x['secret_connections']==[] for x in r))
        with self.subTest(case='test_no_new_criminal_investigations'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['organized_crime_responses'][0]['actual_investigations'].append('opened'),'no actual appointments')
        with self.subTest(case='test_no_hidden_mystery_links'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['organized_crime_responses'][0]['secret_connections'].append('Crown-07'),'secret outcomes')

    def test_contracts_and_schema_and_identity_7(self):
        with self.subTest(case='test_no_fine_or_tax_postings'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['actual_tax_fine_or_fee_events'].append('fine'),'no actual appointments')
        with self.subTest(case='test_partial_government_extension_rejected'), isolated_case(self):
            self.reject('justice-authorities',lambda d:d.pop('approved_design_routing'),'missing design routing')
        with self.subTest(case='test_no_secret_character_answer'), isolated_case(self):
            self.reject('cassian-thornmere',lambda d:d['character_design']['secret_facts'].append('hidden allegiance'),'secret outcomes')
        with self.subTest(case='test_aveline_reuses_existing_proposal_identity'), isolated_case(self):
            p=self.data('justice-proposals');o=next(x for x in p['officers'] if x['id']=='proposal:officer-aveline-hartwell')
            self.assertEqual(o['existing_character_id'],'aveline-hartwell');self.assertIsNone(o['candidate_office_id'])
            self.assertEqual(o['approval_status'],'REQUIRES APPROVAL')
            self.assertEqual(self.data('aveline-hartwell')['character_design']['existing_proposal_id'],o['id'])
        with self.subTest(case='test_no_duplicate_facility_design'), isolated_case(self):
            self.reject('justice-proposals',lambda d:d['approved_facility_designs'].append(copy.deepcopy(d['approved_facility_designs'][0])),'duplicate/wrong facility')

    def test_identity_and_resources_8(self):
        with self.subTest(case='test_no_secret_leader_slots'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['organized_crime_responses'][0].update(secret_leader='hidden'),'unexpected design fields')
        with self.subTest(case='test_unrelated_campaign_history_and_legacy_legal_fields_preserved'), isolated_case(self):
            f=json.loads((ROOT/'tests/fixtures/phase2-03-preservation.json').read_text())
            pass  # Whole-file fingerprints are centralized in test_preservation.
            for path,revision in f['authorized_owner_revisions'].items():
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),revision['after_sha256'],path)
                self.assertNotEqual(revision['before_sha256'],revision['after_sha256'])
            for path,old in f['legacy_legal_payloads'].items():
                now=json.loads(re.search(r'```json\n(.*?)\n```',(ROOT/path).read_text(),re.S)[1])
                for field in ('approved_design_routing','approved_facility_designs','approved_legal_design'):now.pop(field,None)
                if path.endswith('/justice-proposals.md'):
                    expected=copy.deepcopy(old['officers'][0])
                    expected.update(existing_character_id='aveline-hartwell',identity_review='Phase2 approved character design promotes this same proposed identity; Chief Justice office and any actual appointment remain unapproved. Existing magistrates remain authoritative.')
                    expected['source_refs'].append('changes/chronicles/phase2-03-government-approval.md')
                    self.assertEqual(now['officers'][0],expected)
                    now['officers'][0]=old['officers'][0]
                self.assertEqual(now,old,path)
        with self.subTest(case='test_no_completed_political_movement'), isolated_case(self):
            self.reject('ironhollow-holds',lambda d:d['government_design']['political_interests'][0]['active_events'].append('strike'),'no actual appointments')
        with self.subTest(case='test_arrest_transfer_template_includes_medical_inventory_and_receipt'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['action_template'].pop('medical_condition'),'incomplete arrest/transfer')
        with self.subTest(case='test_template_is_no_completed_custody_record'), isolated_case(self):
            self.reject('justice-and-jurisdiction',lambda d:d['approved_legal_design']['action_template'].update(status='received'),'cannot imply actual custody')
