"""Mutation tests for independent guilds, proposal boundaries and reward funding."""
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
from scripts.guilds import GUILD_MARKER, CONTRACT_FIELDS, validate_contract

ROOT=Path(__file__).resolve().parents[1]


class GuildTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='vellorin-guilds-')
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes'):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def path(self,ident):
        kind='factions' if ident in ('wayfarers-guild','dragon-slayer-academy','continental-guild-concord') else 'rules' if ident=='guild-membership-and-contracts' else 'mechanics'
        return self.root/f'entities/{kind}/{ident}.md'

    def data(self,ident):
        return json.loads(re.search(r'```json\n(.*?)\n```',self.path(ident).read_text(),re.S)[1])

    def edit(self,ident,change):
        p=self.path(ident);s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S)
        d=json.loads(m[1]);change(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,ensure_ascii=False,indent=2)+s[m.end(1):])

    def reject(self,ident,change,message):
        self.edit(ident,change)
        with self.assertRaisesRegex(ValidationError,message):validate(self.root)

    def test_current_framework_and_reference_counts(self):
        self.assertIn('checkpoint valid',validate(self.root))
        self.assertEqual(len(self.data('guild-network')['organizations']),9)
        self.assertEqual(len(self.data('continental-guild-concord')['divisions']),8)
        self.assertEqual(len(self.data('wayfarers-guild')['contracts']),4)

    def test_duplicate_guild_id(self):
        self.reject('guild-network',lambda d:d['organizations'].append(d['organizations'][0]),'duplicate guild ID')

    def test_archived_design_not_promoted(self):
        self.reject('guild-network',lambda d:d['organizations'][3].update(classification='CONFIRMED CANON'),'archived guild design cannot be promoted')

    def test_archived_guild_cannot_merge_with_existing(self):
        self.reject('guild-network',lambda d:d['organizations'][3].update(entity_id='wayfarers-guild'),'archived guild design cannot be promoted or merged')

    def test_bad_branch_settlement(self):
        self.reject('guild-network',lambda d:d['branch_candidates'][0].update(candidate_settlement_id='missing-town'),'broken entity reference')

    def test_road_is_not_branch_settlement(self):
        self.reject('guild-network',lambda d:d['branch_candidates'][0].update(candidate_settlement_id='route-ashvale-eastrun'),'physical location required')

    def test_branch_guild_reference(self):
        self.reject('guild-network',lambda d:d['branch_candidates'][0].update(guild_id='not-a-guild'),'invalid branch guild reference')

    def test_no_operational_archived_branch(self):
        self.reject('guild-network',lambda d:d['branch_candidates'][0].update(operational_status='OPEN'),'no approved hall')

    def test_no_branch_staff(self):
        self.reject('guild-network',lambda d:d['branch_candidates'][0].update(responsible_officer_id='master-beren'),'no approved hall, officer')

    def test_concord_requires_approval(self):
        self.reject('continental-guild-concord',lambda d:d.update(operational=True),'Concord remains unapproved')

    def test_cannot_fake_concord_approval(self):
        self.reject('continental-guild-concord',lambda d:d.update(approval_status='APPROVED'),'Concord remains unapproved')

    def test_concord_does_not_own_existing_guilds(self):
        self.reject('continental-guild-concord',lambda d:d['member_organization_ids'].append('wayfarers-guild'),'no Concord staff, membership')

    def test_concord_no_collected_dues_or_treasury(self):
        self.reject('continental-guild-concord',lambda d:d.update(treasury_cp=10000),'no Concord staff, membership, branches, fees or treasury')

    def test_divisions_stay_proposed(self):
        self.reject('continental-guild-concord',lambda d:d['divisions'][0].update(classification='CONFIRMED CANON'),'division cannot become canon')

    def test_broken_compatibility_link(self):
        self.reject('continental-guild-concord',lambda d:d['divisions'][0]['existing_guild_relationship_ids'].append('missing-guild'),'broken compatibility')

    def test_duplicate_division_id(self):
        self.reject('continental-guild-concord',lambda d:d['divisions'][1].update(id=d['divisions'][0]['id']),'duplicate division ID')

    def test_no_new_wayfarers_guildmaster(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['leadership'].append({'entity_id':'tomas'}),'no Wayfarers guildmaster established')

    def test_academy_leadership_preserved(self):
        self.reject('dragon-slayer-academy',lambda d:d['profile']['leadership'][0].update(entity_id='tomas'),'independent academy leadership changed')

    def test_hq_not_relocated(self):
        self.reject('wayfarers-guild',lambda d:d['profile'].update(headquarters_location_id='eastrun'),'headquarters/site changed')

    def test_confirmed_site_not_archived_branch(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['branches'][0].update(settlement_id='eastrun'),'cannot be relocated')

    def test_unrelated_branch_road(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['branches'][0]['route_ids'].append('route-brackenford-cottage'),'road does not serve branch context')

    def test_duplicate_established_branch(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['branches'].append(d['profile']['branches'][0]),'duplicate/invalid branch ID')

    def test_no_new_guild_hall(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['branches'][0].update(building_location_id='ashvale-estate'),'no hall, guildmaster')

    def test_unknown_guildmaster_license_and_funding_valid(self):
        p=self.data('wayfarers-guild')['profile']
        self.assertEqual(p['leadership'],[])
        self.assertIsNone(p['funding']);self.assertIsNone(p['licensing'])
        self.assertIn('checkpoint valid',validate(self.root))

    def test_no_membership_enrollment(self):
        self.reject('wayfarers-guild',lambda d:d['new_memberships'].append({'person':'theron-ashvale'}),'cannot enroll')

    def test_no_retroactive_license_change(self):
        self.reject('wayfarers-guild',lambda d:d['license_changes'].append({'rank':'S+'}),'alter licenses')

    def test_no_paid_new_contract_generation(self):
        self.reject('wayfarers-guild',lambda d:d['new_contracts'].append({'reward_cp':1000}),'create contracts')

    def test_duplicate_contract_reward(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'].append(d['contracts'][0]),'duplicate contract ID/reward')

    def test_historical_payment_must_match(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][0].update(historical_payment_cp=2700),'historical payment/status changed')

    def test_historical_payout_not_repaid(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][0].update(historical_application_count=2),'referenced once')

    def test_paid_history_not_new_reward(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][0].update(reward_cp=2600),'historical payout is not a new reward')

    def test_no_financial_postings(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][0]['financial_postings'].append({'delta_cp':2600}),'cannot post money')

    def test_no_new_commission(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['commission_policy'].update(reference_percent=20),'commission cannot be changed/reapplied')

    def test_no_retroactive_commission(self):
        self.reject('wayfarers-guild',lambda d:d['profile']['commission_policy'].update(retroactive_deductions=True),'commission cannot be changed/reapplied')

    def test_ss41_revocation_not_restored(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][3].update(current_availability='available'),'SS-41 withdrawal')

    def test_independent_notices_not_canceled(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][3].update(independent_notices_cancelled=True),'cannot cancel unrelated notices')

    def test_no_new_historical_completion(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][1].update(completion_status='historical-completed'),'unsupported historical completion')

    def test_missing_contract_route(self):
        self.reject('contract-registry',lambda d:d['contracts'].pop(),'coverage mismatch')

    def test_contract_owner_reference_valid(self):
        self.reject('contract-registry',lambda d:d['contracts'][0].update(owner_entity_id='missing-guild'),'broken entity reference')

    def test_no_license_award_from_combat_rank(self):
        self.reject('guild-membership-and-contracts',lambda d:d['new_license_records'].append({'domain':'guild-license','value':'S+'}),'no new licenses')

    def test_rank_domains_stay_distinct(self):
        self.reject('guild-membership-and-contracts',lambda d:d['rank_domains'].remove('professional-certification'),'rank domains must remain separate')

    def test_no_automatic_guild_events(self):
        self.reject('guild-membership-and-contracts',lambda d:d.update(automatic_world_events=True),'no new licenses/staff/events')

    def test_secret_contract_source_not_public(self):
        self.reject('wayfarers-guild',lambda d:d['contracts'][0]['source_refs'].append('entities/items/black-runeblade.md'),'secret source excluded')

    def test_partial_framework_rejected(self):
        p=self.root/'index.json';d=json.loads(p.read_text())
        d['entries']=[e for e in d['entries'] if e['id']!='contract-registry'];p.write_text(json.dumps(d))
        self.path('contract-registry').unlink()
        # New dungeon provenance may detect the same removed contract owner earlier.
        with self.assertRaisesRegex(ValidationError,'incomplete guild framework|source_refs: missing file entities/mechanics/contract-registry.md'):validate(self.root)

    def test_optimized_validator_preserves_proposals(self):
        self.edit('continental-guild-concord',lambda d:d.update(operational=True))
        p=subprocess.run([sys.executable,'-O',str(ROOT/'scripts/validate.py'),'--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(p.returncode,1);self.assertIn('Concord remains unapproved',p.stderr)

    def test_preexisting_guild_prefixes_resources_licenses_and_custody_preserved(self):
        f=json.loads((ROOT/'tests/fixtures/chunk5-preservation.json').read_text())
        for path,digest in f['protected_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        for path,digest in f['guild_prefix_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_text().split(GUILD_MARKER)[0].encode()).hexdigest(),digest,path)

    def test_validator_does_not_mutate_campaign(self):
        files=[p for folder in ('state','entities','archive') for p in (self.root/folder).rglob('*') if p.is_file()]
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in files};validate(self.root)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in files})


class FundingTests(unittest.TestCase):
    """Synthetic terms only; not actual campaign offers or payments."""
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='guild-funding-fixture-');self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        (self.root/'terms.md').write_text('Fixture Sponsor commits500cp for a test-only offer. Not campaign canon.')
        self.records={'fixture-guild':{'type':'factions','visibility':'gm-reference','status':'canon'}}
        self.c={key:None for key in CONTRACT_FIELDS}
        self.c.update(contract_id='fixture-contract',classification='CONFIRMED CANON',issuing_organization_id='fixture-guild',registry_organization_id='fixture-guild',apprehension_authorized=False,reward_guaranteed=False,payment_status='unpaid',historical_application_count=0,current_availability='test-only',independent_notices_cancelled=False,financial_postings=[],source_refs=['terms.md'],source_quote='Not campaign canon.',last_verified_note='Synthetic test fixture')

    def check(self):
        validate_contract(self.c,self.root,self.records,require,repository_file)

    def funded(self):
        self.c.update(funding_party_name='Fixture Sponsor',funding_source_ref='terms.md',funding_source_quote='Fixture Sponsor commits500cp',funding_committed_cp=500,reward_cp=500,reward_guaranteed=True)

    def test_unknown_unfunded_draft_is_valid_not_guaranteed(self):
        self.check()

    def test_identified_sourced_commitment_sufficient_for_schema(self):
        self.funded();self.check()

    def test_no_unfunded_guaranteed_reward(self):
        self.c.update(reward_cp=500,reward_guaranteed=True)
        with self.assertRaisesRegex(ValidationError,'identifiable funding party'):self.check()

    def test_no_overcommitted_reward(self):
        self.funded();self.c['reward_cp']=600
        with self.assertRaisesRegex(ValidationError,'exceeds verified committed budget'):self.check()

    def test_funding_quote_must_exist(self):
        self.funded();self.c['funding_source_quote']='Unrecorded billion gold guarantee'
        with self.assertRaisesRegex(ValidationError,'funding quote not found'):self.check()

    def test_integer_copper_only(self):
        for amount in (True,1.5,-1):
            with self.subTest(amount=amount):
                self.c['reward_cp']=amount
                with self.assertRaisesRegex(ValidationError,'integer copper'):self.check()

    def test_bounty_contract_not_arrest_warrant(self):
        self.c['apprehension_authorized']=True
        with self.assertRaisesRegex(ValidationError,'not arrest authorization'):self.check()

    def test_proposed_issuer_not_canon(self):
        self.records['fixture-guild']['status']='research'
        with self.assertRaisesRegex(ValidationError,'unapproved organization'):self.check()

    def test_proposal_cannot_guarantee_reward(self):
        self.funded();self.c['classification']='PROPOSED'
        with self.assertRaisesRegex(ValidationError,'cannot create new guaranteed rewards'):self.check()
