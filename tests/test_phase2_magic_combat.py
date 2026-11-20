"""Consolidated finite-magic/combat references; no spell, encounter or state engine."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from case_support import isolated_case,validate_scope
from snapshot_helpers import SUNCREST262_REVISED_AUTHORITIES
from scripts.magic_combat import (OWNER,PRESERVED_COSTS,EVENT_ARRAYS,spell_costs,recovery_preview,
    spend_preview,defense_reference,audit)
from scripts.dungeon_designs import MONSTERS
from scripts.validate import ValidationError

ROOT=Path(__file__).resolve().parents[1]


class MagicCombatTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        for folder in ('entities','state','archive','changes','docs','governance'):shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copy2(ROOT/'index.json',self.root/'index.json')

    def data(self,ident=OWNER):
        p=self.root/f'entities/mechanics/{ident}.md';return json.loads(re.search(r'```json\n(.*?)\n```',p.read_text(),re.S)[1])

    def change(self,fn,ident=OWNER):
        p=self.root/f'entities/mechanics/{ident}.md';s=p.read_text();m=re.search(r'```json\n(.*?)\n```',s,re.S);d=json.loads(m[1]);fn(d)
        p.write_text(s[:m.start(1)]+json.dumps(d,indent=2)+s[m.end(1):])

    def rejected(self,fn,pattern,ident=OWNER,scopes=('magic_combat',)):
        self.change(fn,ident)
        with self.assertRaisesRegex(ValidationError,pattern):validate_scope(self.root,*scopes)

    def test_eight_schools_no_new_spells_or_abilities(self):
        d=self.data();self.assertEqual(len(d['schools']),8);self.assertEqual(len(d['combat_procedures']),16);self.assertEqual(len(d['environment_interactions']),12)
        for change in (lambda d:d['schools'].__setitem__(1,copy.deepcopy(d['schools'][0])),
                       lambda d:d['schools'][0]['existing_spell_names'].append('Firestorm'),
                       lambda d:d['schools'][0].update(classification='GRANTED')):
            with self.subTest(change=change),isolated_case(self):self.rejected(change,'school|grant')
        self.assertEqual(d['new_spells'],[])

    def test_established_costs_preserved_and_missing_references_ungranted(self):
        costs=spell_costs(self.root)
        self.assertTrue(all(costs[n]==v for n,v in PRESERVED_COSTS.items()))
        self.assertNotIn('Deep Mend',costs);self.assertNotIn('Greater Healing',costs)
        p=self.root/'entities/mechanics/theron-spells.md';original=p.read_text()
        for name in PRESERVED_COSTS:
            with self.subTest(name=name),isolated_case(self):
                updated=re.sub(r'(\|\s*'+re.escape(name)+r'\s*\|\s*)\d+',lambda m:m[1]+'999',original)
                if updated==original:updated=re.sub(re.escape(name)+r'\d+MP',name+'999MP',original)
                self.assertNotEqual(original,updated);p.write_text(updated)
                with self.assertRaisesRegex(ValidationError,'spell costs'):validate_scope(self.root,'magic_combat')
        for field,value in [('granted',True),('verified_owner_cost',17)]:
            with self.subTest(field=field),isolated_case(self):
                self.rejected(lambda d,f=field,v=value:d['cost_policy']['unverified_player_references'][0].update({f:v}),'unverified references')

    def test_dreamfall_keeps_range_area_duration_save_and_waking(self):
        p=self.root/'entities/mechanics/theron-spells.md';source=p.read_text()
        for old,new in [('60-ft range','600-ft range'),('20-ft radius','200-ft radius'),('1–30 min maximum','1–300 min maximum'),
                        ('concentration','no focus'),('wake on damage/shaking/end concentration','never wake'),('DC18 mental save','DC99 mental save')]:
            with self.subTest(rule=old),isolated_case(self):
                self.assertIn(old,source);p.write_text(source.replace(old,new))
                with self.assertRaisesRegex(ValidationError,'Dreamfall'):validate_scope(self.root,'magic_combat')

    def test_efficiency_never_double_discounts_or_invents_rounding(self):
        for field,value in [('current_ordinary_discount_percent',60),('automatic_repricing',True),('additional_discount_application',True),('new_rounding_formula','ceil(base*0.6)')]:
            with self.subTest(field=field),isolated_case(self):
                self.rejected(lambda d,f=field,v=value:d['cost_policy'].update({f:v}),'efficiency|discount|rounding')
        self.assertEqual(spend_preview(13,13),0)
        for args in ((10,11),(True,1),(1,-1),(10,1.0)):
            with self.subTest(args=args),self.assertRaises(ValueError):spend_preview(*args)

    def test_assimilation_is_finite_personal_conditional_and_capped(self):
        self.assertEqual(recovery_preview(378,400,10,True,True),dict(potential_mp=24,actual_mp=22,excess_mp=2,ending_mp=400))
        self.assertEqual(recovery_preview(400,400,20,True,True)['actual_mp'],0)
        for args in ((378,400,9,True,True),(378,400,10,False,True),(378,400,10,True,False),
                     (401,400,10,True,True),(True,400,10,True,True),(378,float('inf'),10,True,True)):
            with self.subTest(args=args),self.assertRaises(ValueError):recovery_preview(*args)
        for pool in ('staff','wagon','ally','construct'):
            with self.subTest(pool=pool),self.assertRaises(ValueError):recovery_preview(156,180,10,True,True,pool=pool)
        with isolated_case(self):self.rejected(lambda d:d['recovery_policy'].update(personal_only=False),'cross-pool')

    def test_equipment_defense_and_locked_progression_remain_qualified(self):
        self.assertEqual(defense_reference(None),dict(normal_equipped=49,conditional_if_worn=51,current_equipped=None))
        self.assertEqual(defense_reference(False)['current_equipped'],49);self.assertEqual(defense_reference(True)['current_equipped'],51)
        with self.assertRaises(ValueError):defense_reference(1)
        state=json.loads((ROOT/'state/checkpoint.json').read_text());self.assertTrue(state['resources']['chronos_eye_locked']);self.assertTrue(state['resources']['dragon_slayer_locked'])
        self.assertIsNone(state['provenance']['current_equipment']['night_sovereign_carried_not_equipped'])
        with isolated_case(self):self.rejected(lambda d:d['equipment_owner_refs'].append('new-staff'),'equipment identity')
        for field in EVENT_ARRAYS:
            with self.subTest(field=field),isolated_case(self):self.rejected(lambda d,f=field:d[f].append('event'),'no casting')

    def test_five_monster_stats_unchanged_no_numerical_completion_or_spawns(self):
        ident='dungeon-ecology-and-hazards';d=self.data(ident);profiles=d['approved_combat_reference_profiles']['profiles']
        self.assertEqual(len(profiles),5)
        for m in d['approved_reference_design']['monster_references']:
            expected=MONSTERS[m['id'].removeprefix('monster-reference:')]
            self.assertEqual((m['name'],m['hp'],m['mp'],m['defense'],m['reference_rank']),expected)
        cases=[(lambda d:d['approved_reference_design']['monster_references'][0].update(hp=999),'stats'),
               (lambda d:d['approved_reference_design']['monster_references'][0].update(damage_formula='2d6'),'unknown'),
               (lambda d:d['approved_combat_reference_profiles']['profiles'][0].update(combat_ready=True),'combat-ready'),
               (lambda d:d['approved_combat_reference_profiles']['profiles'][0]['new_spell_names'].append('Venom Cloud'),'combat-ready'),
               (lambda d:d['approved_combat_reference_profiles']['profiles'][0].update(current_instances=1),'current instance'),
               (lambda d:d['approved_combat_reference_profiles']['actual_spawns'].append('spider'),'spawns'),
               (lambda d:d['approved_combat_reference_profiles'].update(automatic_respawn=True),'respawn')]
        for change,pattern in cases:
            with self.subTest(pattern=pattern),isolated_case(self):self.rejected(change,pattern,ident,('dungeon_designs','magic_combat'))

    def test_dungeon_counts_ss_domain_and_no_loot_preserved(self):
        paths=('hollowstone-mine','ashen-anvil','drowned-archive','pale-reliquary','shattered-meridian');totals=[0,0,0]
        for ident in paths:
            d=self.data(ident)['dungeon_design']
            for i,f in enumerate(('areas','connections','encounter_designs')):totals[i]+=len(d[f])
            self.assertEqual(d['actual_discoveries'],[]);self.assertEqual(d['actual_population_events'],[])
        self.assertEqual(totals,[25,30,25]);self.assertEqual(len(self.data('dungeon-ecology-and-hazards')['approved_reference_design']['hazard_references']),12)
        with isolated_case(self):self.rejected(lambda d:d['rank_policy'].update(compatible_adventurer_rank='S+'),'SS')
        with isolated_case(self):self.rejected(lambda d:d.update(automatic_resolution=True),'no casting')
        with isolated_case(self):self.rejected(lambda d:d['approved_combat_reference_profiles']['actual_loot'].append('coins'),'loot','dungeon-ecology-and-hazards')

    def test_cross_system_public_references_and_no_shadow_authorities(self):
        for key in ('spells','ledger','checkpoint','autonomy','travel','law'):
            with self.subTest(key=key),isolated_case(self):self.rejected(lambda d,k=key:d['authority_refs'].update({k:'new-authority'}),'competing')
        with isolated_case(self):self.rejected(lambda d:d['phase2_links'][0].update(owner_ids=['theron-spells']),'phase authority')
        with isolated_case(self):self.rejected(lambda d:d.update(approval_source_ref='README.md'),'provenance')
        with isolated_case(self):self.rejected(lambda d:d.update(secret_outcome='hidden solution'),'unexpected')
        with isolated_case(self):
            p=self.root/f'entities/mechanics/{OWNER}.md';p.write_text(p.read_text().replace('visibility: gm-reference','visibility: gm-secret'))
            with self.assertRaisesRegex(ValidationError,'private'):validate_scope(self.root,'magic_combat')

    def test_readonly_audit_and_original_payload_preservation(self):
        fixture=json.loads((ROOT/'tests/fixtures/phase2-08-preservation.json').read_text())
        p='entities/mechanics/dungeon-ecology-and-hazards.md';d=json.loads(re.search(r'```json\n(.*?)\n```',(ROOT/p).read_text(),re.S)[1]);d.pop('approved_combat_reference_profiles')
        self.assertEqual(d,fixture['legacy_monster_payloads'][p])
        paths=[ROOT/'state/checkpoint.json',ROOT/'state/finance-ledger.json',ROOT/'entities/mechanics/theron-spells.md']
        before=[p.read_bytes() for p in paths];report=audit(ROOT)
        self.assertEqual([p.read_bytes() for p in paths],before);self.assertFalse(report['numerical_combat_ready']);self.assertFalse(report['gameplay_performed'])
        self.assertEqual(report['dungeon_design_counts'],dict(areas=25,connections=30,encounters=25,hazards=12))
        self.assertEqual(len(report['audit_findings']),18);self.assertEqual(report['finances']['controlled_cp'],299040)
        for p in ('entities/items/sovereign-nexus.md','entities/items/dawnbreakers-promise.md',
                  'entities/items/night-sovereign.md','entities/creatures/alpha.md','entities/creatures/shade.md'):
            with self.subTest(path=p):self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),SUNCREST262_REVISED_AUTHORITIES.get(p, {}).get('after_sha256', fixture['unchanged_sha256'][p]))
