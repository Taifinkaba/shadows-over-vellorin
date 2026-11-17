"""Justice proposal/custody preservation and prospective transfer regression tests."""
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

from scripts.validate import ValidationError, validate, require, repository_file
from scripts.justice import CUSTODY_MARKER, TRANSFER_FIELDS, validate_transfer

ROOT = Path(__file__).resolve().parents[1]


class JusticeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vellorin-justice-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ('entities','state','archive','changes'):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self, ident):
        kind = 'rules' if ident=='justice-and-jurisdiction' else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self, ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self, ident, change):
        p = self.path(ident);s = p.read_text()
        m = re.search(r'```json\n(.*?)\n```',s,re.S)
        d = json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2,ensure_ascii=False)+s[m.end(1):])

    def reject(self, ident, change, message):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,message):
            validate(self.root)

    def test_framework_passes_and_keeps_all_proposals_unapproved(self):
        self.assertIn('checkpoint valid',validate(self.root))
        p = self.data('justice-proposals')
        self.assertEqual((len(p['roles']),len(p['buildings']),len(p['officers'])),(7,12,16))
        self.assertTrue(all(b['operational_status']=='PROPOSED — NOT OPERATIONAL' for b in p['buildings']))
        self.assertEqual(len(self.data('justice-road-links')['roads']),18)

    def test_duplicate_institution(self):
        self.reject('justice-authorities',lambda d:d['authorities'].append(d['authorities'][0]),'duplicate/invalid authority ID')

    def test_bad_jurisdiction_reference(self):
        self.reject('justice-authorities',lambda d:d['authorities'][0]['jurisdiction_location_ids'].append('not-a-place'),'broken entity reference')

    def test_canonical_jurisdiction_cannot_use_proposed_continent(self):
        self.reject('justice-authorities',lambda d:d['authorities'][0]['jurisdiction_location_ids'].append('aethoria'),'canonical jurisdiction through proposed')

    def test_bad_officer_reference(self):
        self.reject('justice-authorities',lambda d:d['authorities'][2].update(leadership_ids=['not-an-officer']),'broken entity reference')

    def test_village_officials_cannot_be_replaced(self):
        self.reject('justice-authorities',lambda d:d['authorities'][2].update(leadership_ids=['theron-ashvale']),'village authority changed')

    def test_watch_command_is_not_civilian_court(self):
        self.reject('justice-authorities',lambda d:d['authorities'][4].update(authority_kind='judicial'),'cannot become civilian judicial power')

    def test_private_security_is_not_police(self):
        self.reject('justice-authorities',lambda d:d['authorities'][6].update(authority_kind='civilian-law-enforcement'),'cannot become civilian judicial power')

    def test_no_new_operational_prison(self):
        self.reject('justice-authorities',lambda d:d['verified_receiving_facilities'].append('proposal:building-stonegate'),'no new operational receiving facility')

    def test_duplicate_proposal_id(self):
        self.reject('justice-proposals',lambda d:d['roles'][1].update(id=d['roles'][0]['id']),'duplicate proposal ID')

    def test_building_reference_must_exist(self):
        self.reject('justice-proposals',lambda d:d['buildings'][0].update(candidate_location_id='invented-capital'),'broken entity reference')

    def test_unlocated_stonegate_cannot_be_placed(self):
        self.reject('justice-proposals',lambda d:d['buildings'][10].update(candidate_location_id='eastrun'),'no geography supplied')

    def test_role_is_not_nationwide_authority(self):
        self.reject('justice-proposals',lambda d:d['roles'][0]['jurisdiction_location_ids'].append('vellorin'),'no approved reach')

    def test_proposed_building_cannot_be_operational(self):
        self.reject('justice-proposals',lambda d:d['buildings'][1].update(operational_status='OPERATIONAL'),'cannot be staffed or operational')

    def test_no_fabricated_approval(self):
        self.reject('justice-proposals',lambda d:d['buildings'][0].update(approval_status='APPROVED'),'approval/canon cannot be fabricated')

    def test_proposals_cannot_be_canonical(self):
        self.reject('justice-proposals',lambda d:d.update(classification='CONFIRMED CANON'),'proposals cannot become canon')

    def test_no_proposed_official_alias_to_established_person(self):
        self.reject('justice-proposals',lambda d:d['officers'][2].update(existing_character_id='mara-vey'),'identity/appointment/relationship not established')

    def test_no_duplicate_established_official_name(self):
        self.reject('justice-proposals',lambda d:d['officers'][2].update(name='Captain Mara Vey'),'duplicates an established name')

    def test_no_invented_meeting_or_kinship(self):
        self.reject('justice-proposals',lambda d:d['officers'][0].update(relationships_to_theron='Trusted family friend'),'relationship not established')

    def test_no_new_warden_assignment(self):
        self.reject('justice-proposals',lambda d:d['buildings'][6].update(responsible_officer_id='harlan-wicks'),'cannot be staffed or operational')

    def test_unknown_capacity_is_valid_not_zero_inmates(self):
        self.assertIsNone(self.data('justice-proposals')['buildings'][6]['capacity'])
        self.assertIn('checkpoint valid',validate(self.root))

    def test_no_invented_capacity(self):
        self.reject('justice-proposals',lambda d:d['buildings'][6].update(capacity=100),'cannot be staffed or operational')

    def test_boolean_detention_type_rejected(self):
        self.reject('justice-proposals',lambda d:d['buildings'][1].update(detention_type=True),'invalid detention type')

    def test_missing_road_link(self):
        self.reject('justice-road-links',lambda d:d['roads'].pop(),'coverage mismatch')

    def test_duplicate_road_link(self):
        self.reject('justice-road-links',lambda d:d['roads'].append(d['roads'][0]),'duplicate/invalid road ID')

    def test_no_proximity_based_patrol_or_receiving_destination(self):
        self.reject('justice-road-links',lambda d:d['roads'][0].update(responsible_authority_id='justice:caelthorne-watch'),'proximity does not establish')

    def test_endpoint_authority_requires_correct_endpoint(self):
        self.reject('justice-road-links',lambda d:d['roads'][0]['endpoint_contacts'][0].update(location_id='brackenford'),'not a sourced endpoint contact')

    def test_automatic_transport_forbidden(self):
        self.reject('justice-road-links',lambda d:d.update(automatic_transport=True),'automatic transport forbidden')

    def test_automatic_custody_forbidden(self):
        self.reject('prisoner-custody',lambda d:d.update(automatic_custody_actions=True),'automatic custody actions forbidden')

    def test_no_new_case_status_or_conviction(self):
        self.reject('prisoner-custody',lambda d:d['new_case_records'].append({'case_id':'test-only','stage':'convicted'}),'cannot add case outcomes')

    def test_no_historical_prison_assignment(self):
        self.reject('prisoner-custody',lambda d:d['new_transfer_records'].append({'destination':'proposal:building-stonegate'}),'cannot add case outcomes')

    def test_no_evidence_ownership_change(self):
        self.reject('prisoner-custody',lambda d:d['new_evidence_records'].append({'owner':'theron-ashvale'}),'cannot add case outcomes')

    def test_no_new_hidden_status_in_source_pointer(self):
        self.reject('prisoner-custody',lambda d:d['history_routing'][0].update(current_prisoner_location='stonegate'),'invalid history pointer fields')

    def test_secret_entity_not_public_source(self):
        self.reject('prisoner-custody',lambda d:d['history_routing'][0]['source_refs'].append('entities/items/black-runeblade.md'),'secret reference forbidden')

    def test_missing_source_file(self):
        self.reject('prisoner-custody',lambda d:d['history_routing'][0]['source_refs'].append('no-source.md'),'missing file')

    def test_no_replacement_evidence_register(self):
        self.reject('prisoner-custody',lambda d:d.update(evidence_owner_refs=['justice-proposals']),'existing evidence/finance owners required')

    def test_proposed_process_cannot_be_enacted_silently(self):
        self.reject('justice-and-jurisdiction',lambda d:d.update(legal_process_classification='CONFIRMED CANON'),'not enacted law')

    def test_transfer_inventory_fields_required(self):
        self.reject('justice-and-jurisdiction',lambda d:d['transfer_fields'].remove('property_inventory_ref'),'incomplete transfer/evidence schema')

    def test_duplicate_history_group_rejected(self):
        self.reject('prisoner-custody',lambda d:d['history_routing'].append(d['history_routing'][0]),'duplicate custody source pointer')

    def test_optimized_mode_rejects_operational_proposal(self):
        self.edit('justice-proposals',lambda d:d['buildings'][0].update(operational_status='OPERATIONAL'))
        p = subprocess.run([sys.executable,'-O',str(ROOT/'scripts/validate.py'),'--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(p.returncode,1)
        self.assertIn('cannot be staffed or operational',p.stderr)

    def test_preexisting_state_legal_outcomes_roads_and_custody_prefix_preserved(self):
        fixture=json.loads((ROOT/'tests/fixtures/chunk4-preservation.json').read_text())
        for path,digest in fixture['protected_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        prefix=(ROOT/'entities/mechanics/prisoner-custody.md').read_text().split(CUSTODY_MARKER)[0]
        self.assertEqual(hashlib.sha256(prefix.encode()).hexdigest(),fixture['custody_prefix_sha256'])

    def test_validator_does_not_mutate_existing_campaign_files(self):
        paths=[p for folder in ('state','entities','archive') for p in (self.root/folder).rglob('*') if p.is_file()]
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in paths}
        validate(self.root)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in paths})


class TransferCompletenessTests(unittest.TestCase):
    """Synthetic test-only context; none of these objects is campaign canon."""
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='justice-transfer-fixture-')
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        (self.root/'test-evidence.md').write_text('Synthetic handover/inventory fixture only.')
        self.records={'fixture-officer':{'type':'characters'}}
        self.authorities={'fixture-sender':{'classification':'CONFIRMED CANON'},'fixture-receiver':{'classification':'CONFIRMED CANON'}}
        self.facilities={'fixture-facility':{'classification':'CONFIRMED CANON','operational_status':'OPERATIONAL','operating_authority_id':'fixture-receiver'}}
        self.record={f:None for f in TRANSFER_FIELDS}
        self.record.update(case_id='fixture-case',status='planned',source_refs=[])

    def check(self):
        validate_transfer(self.record,self.root,self.records,self.authorities,self.facilities,require,repository_file)

    def complete(self):
        self.record.update(status='completed',sending_authority_id='fixture-sender',receiving_authority_id='fixture-receiver',destination_facility_id='fixture-facility',legal_basis='Synthetic court authorization fixture',receiving_officer_id='fixture-officer',source_refs=['test-evidence.md'])
        for f in ('departure_ref','arrival_ref','custody_receipt_ref','evidence_inventory_ref','property_inventory_ref'):
            self.record[f]='test-evidence.md'

    def test_plan_can_preserve_unknowns(self):
        self.check()

    def test_plan_cannot_claim_arrival(self):
        self.record.update(arrival_ref='test-evidence.md',source_refs=['test-evidence.md'])
        with self.assertRaisesRegex(ValidationError,'plan cannot claim'):
            self.check()

    def test_completed_fixture_requires_all_proofs(self):
        self.complete();self.check()
        for f in ('departure_ref','arrival_ref','custody_receipt_ref','evidence_inventory_ref','property_inventory_ref'):
            with self.subTest(field=f):
                self.complete();self.record[f]=None
                with self.assertRaises(ValidationError):self.check()

    def test_completed_transfer_cannot_use_proposed_prison(self):
        self.complete();self.facilities['fixture-facility']['classification']='PROPOSED'
        with self.assertRaisesRegex(ValidationError,'proposed/nonoperational facility'):
            self.check()

    def test_completed_transfer_cannot_use_proposed_authority(self):
        self.complete();self.authorities['fixture-receiver']['classification']='PROPOSED'
        with self.assertRaisesRegex(ValidationError,'proposed authority'):
            self.check()

    def test_completed_transfer_needs_receiving_officer(self):
        self.complete();self.record['receiving_officer_id']=None
        with self.assertRaisesRegex(ValidationError,'receiving officer required'):
            self.check()

    def test_completed_transfer_needs_legal_basis(self):
        self.complete();self.record['legal_basis']=None
        with self.assertRaisesRegex(ValidationError,'legal basis required'):
            self.check()

    def test_stable_case_id_can_preserve_unknown_person(self):
        self.complete();self.assertIsNone(self.record['prisoner_id']);self.check()

    def test_mismatched_receiving_authority(self):
        self.complete();self.facilities['fixture-facility']['operating_authority_id']='fixture-sender'
        with self.assertRaisesRegex(ValidationError,'receiving authority mismatch'):
            self.check()

    def test_in_transit_is_not_completed_handover(self):
        self.complete();self.record.update(status='in-transit',arrival_ref=None,custody_receipt_ref=None)
        self.check()
        self.record['arrival_ref']='test-evidence.md'
        with self.assertRaisesRegex(ValidationError,'transit cannot claim'):
            self.check()
