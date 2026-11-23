"""Read-only magic/combat integration guards and public Phase2 audit; no game engine."""
import argparse
import hashlib
import json
from pathlib import Path
import re

APPROVAL='changes/chronicles/phase2-08-magic-combat-approval.md'
OWNER='magic-and-combat-integration'
SCHOOL_SPELLS={
 'elemental':['Frost Lance','Frost Veil','Glacial Step','Rime Snare'],
 'restoration':['Minor Restoration','Deep Restoration','Regenerative Weave','Master Restoration Weave'],
 'runecraft':['Rune Barrier','Greater Rune Barrier','Runic Edge','Ward Sense'],
 'mental':['Mental Probe','Dreamfall Mastered','Mirror Mind','Mental Link'],
 'spatial':['Spatial Step','Extended Spatial Transfer'],'temporal':[],'spirit':[],
 'shadow':['Umbral Bolt','Umbral Murmur','Shadow Mantle','Phantom Procession']}
PRESERVED_COSTS={'Frost Lance':6,'Umbral Bolt':7,'Rune Barrier':9,'Minor Restoration':11,'Spatial Step':9,
 'Runic Edge':6,'Ward Sense':5,'Mental Probe':13,'Extended Spatial Transfer':21,'Greater Rune Barrier':28,
 'Dreamfall Mastered':21,'Shadow Mantle':16,'Phantom Procession':18,'Umbral Murmur':9,
 'Deep Restoration':36,'Regenerative Weave':32,'Master Restoration Weave':48}
AUTHORITIES=dict(spells='theron-spells',abilities='theron-abilities',skills='theron-skills',story_mode='story-mode',
 travel='travel-procedure',settlements='settlement-services',communications='settlement-communications',
 law='justice-and-jurisdiction',guilds='guild-membership-and-contracts',dungeons='dungeon-design-proposals',
 monsters='dungeon-ecology-and-hazards',exploration='dungeon-exploration',economy='economy-accounting',
 property='property-financial-references',autonomy='npc-autonomy-and-time',events='world-event-references',
 quests='quest-continuation-and-completion',ledger='state/finance-ledger.json',checkpoint='state/checkpoint.json')
PHASE_OWNERS={1:['world-geography','travel-routes','travel-procedure'],2:['settlement-services','settlement-trade','settlement-communications'],
 3:['justice-authorities','justice-and-jurisdiction'],4:['guild-network','guild-membership-and-contracts','illicit-commerce-design'],
 5:['dungeon-design-proposals','dungeon-ecology-and-hazards','dungeon-exploration'],6:['economy-accounting','property-financial-references','payroll-construction-and-trade'],
 7:['npc-autonomy-and-time','independent-assignments','world-event-references']}
EQUIPMENT=['sovereign-nexus','sovereign-expedition-wagon','dawnbreakers-promise','night-sovereign','guardian-links']
COMBAT=set('initiative-action-order movement attacks defense damage healing spellcasting concentration status-effects environmental-hazards retreat nonlethal defeat-permanent-death rest-recovery resource-expenditure encounter-consequences'.split())
ENVIRONMENTS=set('fire-combustibles ice-water electricity darkness-visibility sound-stealth water-breathing heat-endurance poison-biology spatial-barriers mental-defenses magical-wards structural-damage'.split())
SCHOOL_TEXT=set('principles applications resource_requirements training casting_constraints failure_conditions defensive_interactions ethical_legal_limits unresolved'.split())
PROFILE_TEXT=set('physical_characteristics movement_capabilities attack_types attack_limits defensive_characteristics environmental_adaptations resource_costs behavior retreat_conditions noncombat_interactions defeat_consequences loot_limits'.split())
EVENT_ARRAYS='actual_casts actual_combat_events actual_recovery_events actual_monster_instances actual_loot_events new_spells new_equipment new_progression'.split()


def need(condition,message):
    if not condition:raise ValueError('magic/combat: '+message)


def integer(value):
    need(type(value) is int and value>=0,'finite nonnegative integer required')
    return value


def spend_preview(current,cost):
    """Pure arithmetic after independent verification of pool ownership and cost."""
    integer(current);integer(cost);need(cost<=current,'insufficient finite resource')
    return current-cost


def recovery_preview(current,maximum,uninterrupted_minutes,ambient_usable,concentration_met,pool='personal'):
    """Source-conditional personal assimilation example; records no action or time."""
    for value in (current,maximum,uninterrupted_minutes):integer(value)
    need(maximum>0 and current<=maximum,'invalid current/maximum resource')
    need(pool=='personal','assimilation cannot refill staff, wagon or others')
    need(ambient_usable is True and concentration_met is True,'usable ambient source and uninterrupted concentration required')
    need(uninterrupted_minutes%10==0,'complete uninterrupted10minute intervals required')
    potential=24*(uninterrupted_minutes//10);actual=min(potential,maximum-current)
    return dict(potential_mp=potential,actual_mp=actual,excess_mp=potential-actual,ending_mp=current+actual)


def defense_reference(worn):
    need(worn is None or type(worn) is bool,'wearing must be verified or UNKNOWN')
    return dict(normal_equipped=49,conditional_if_worn=51,current_equipped=None if worn is None else 51 if worn else 49)


def spell_costs(root):
    text=(root/'entities/mechanics/theron-spells.md').read_text();costs={}
    for name,mp in re.findall(r'\|\s*([^|\n]+?)\s*\|\s*(\d+)\s*(?=\|)',text):costs[name.strip()]=int(mp)
    for name,mp in re.findall(r'\b(Deep Restoration|Regenerative Weave|Master Restoration Weave)(\d+)MP',text):costs[name]=int(mp)
    return costs


def payload(root,path,unique_json=None):
    blocks=re.findall(r'^```json\n(.*?)\n```$',(root/path).read_text(),re.M|re.S)
    need(len(blocks)==1,'one owner JSON block required')
    return json.loads(blocks[0],object_pairs_hook=unique_json)


def validate_magic_combat(root,records,require,repository_file,unique_json):
    ecology=payload(root,'entities/mechanics/dungeon-ecology-and-hazards.md',unique_json) if 'dungeon-ecology-and-hazards' in records else {}
    extension=ecology.get('approved_combat_reference_profiles')
    if OWNER not in records and extension is None:return
    def check(c,m):require(c,'magic/combat: '+m)
    check(OWNER in records and extension is not None,'incomplete integration owners')
    def shape(d,fields):check(isinstance(d,dict) and set(d)==set(fields),'unexpected integration fields')
    def ref(ident):check(isinstance(ident,str) and ident in records and records[ident]['visibility']=='gm-reference','private/broken public reference')
    def text(v):check(isinstance(v,str) and bool(v.strip()),'bounded reference text required')
    def approval(ident,d):
        ref(ident);check(d['classification']=='APPROVED INTEGRATION DESIGN' and d['approval_source_ref']==APPROVAL and APPROVAL in records[ident]['source_refs'],'approval provenance mismatch')
    repository_file(root,APPROVAL,'magic/combat approval')
    d=payload(root,'entities/mechanics/'+OWNER+'.md',unique_json)
    shape(d,set('schema_version classification approval_source_ref authority_refs schools combat_procedures environment_interactions cost_policy recovery_policy equipment_owner_refs phase2_links rank_policy automatic_resolution'.split())|set(EVENT_ARRAYS))
    check(type(d['schema_version']) is int and d['schema_version']==1,'invalid integration schema');approval(OWNER,d)
    check(records[OWNER]['type']=='mechanics' and records[OWNER]['status']=='canon','wrong integration owner kind')
    check(d['authority_refs']==AUTHORITIES,'competing spell, resource, finance or chronology authority')
    for ident in AUTHORITIES.values():
        if ident.startswith('state/'):repository_file(root,ident,'original resource authority')
        else:ref(ident)
    check(d['automatic_resolution'] is False and all(d[k]==[] for k in EVENT_ARRAYS),'no casting, combat, recovery, spawn, loot, equipment or progression events')
    check(isinstance(d['schools'],list) and len(d['schools'])==8,'eight schools required');seen=set()
    costs=spell_costs(root)
    for row in d['schools']:
        shape(row,SCHOOL_TEXT|set('id name classification spell_owner_ref ability_owner_ref existing_spell_names'.split()))
        ident=row['id'];check(isinstance(ident,str) and ident.startswith('school:') and ident[7:] in SCHOOL_SPELLS and ident not in seen,'duplicate/unknown school');seen.add(ident)
        check(row['classification']=='REFERENCE CLASSIFICATION' and row['spell_owner_ref']=='theron-spells' and row['ability_owner_ref']=='theron-abilities','classification cannot grant powers or duplicate spell authority')
        check(row['existing_spell_names']==SCHOOL_SPELLS[ident[7:]] and all(s in costs for s in row['existing_spell_names']),'unsupported spell grant/classification')
        for f in SCHOOL_TEXT|{'name'}:text(row[f])
    for field,prefix,expected in [('combat_procedures','combat:',COMBAT),('environment_interactions','environment:',ENVIRONMENTS)]:
        rows=d[field];check(isinstance(rows,list) and len(rows)==len(expected),'bounded combat/environment coverage required');ids=set()
        for row in rows:
            shape(row,{'id','procedure'});check(isinstance(row['id'],str) and row['id'].startswith(prefix) and row['id'][len(prefix):] in expected and row['id'] not in ids,'duplicate/unknown procedure');ids.add(row['id']);text(row['procedure'])
    check(all(costs.get(name)==mp for name,mp in PRESERVED_COSTS.items()),'established spell costs changed or missing')
    spells=(root/'entities/mechanics/theron-spells.md').read_text()
    check(all(s in spells for s in ('60-ft range','20-ft radius','1–30 min maximum','concentration','wake on damage/shaking/end concentration','DC18 mental save')),'Dreamfall range, duration, concentration, save or waking changed')
    c=d['cost_policy'];shape(c,'owner_ref current_ordinary_discount_percent automatic_repricing new_rounding_formula additional_discount_application unverified_player_references'.split())
    check(c['owner_ref']=='theron-spells' and type(c['current_ordinary_discount_percent']) is int and c['current_ordinary_discount_percent']==40,'ordinary efficiency authority differs')
    check(c['automatic_repricing'] is False and c['additional_discount_application'] is False and c['new_rounding_formula'] is None,'no double discount or new rounding/repricing')
    check(c['unverified_player_references']==[dict(name='Deep Mend',supplied_mp=17,verified_owner_cost=None,granted=False),dict(name='Greater Healing',supplied_mp=21,verified_owner_cost=None,granted=False)],'unverified references cannot be granted or silently repriced')
    for name in ('Deep Mend','Greater Healing'):check(name not in costs,'new governing spell evidence needs explicit conflict review')
    check('Ordinary discount is now40%' in spells,'governing discount revision missing')
    ability=(root/'entities/mechanics/theron-abilities.md').read_text();skills=(root/'entities/mechanics/theron-skills.md').read_text()
    check('24 personal MP per uninterrupted10 minutes' in ability and 'capped400' in ability and 'usable ambient mana' in ability,'assimilation source/rate/cap changed')
    check('Chronos Eye' in skills and 'LOCKED' in skills and 'Dragon Slayer' in skills,'locked progression source missing')
    check(d['recovery_policy']==dict(owner_ref='theron-abilities',personal_only=True,automatic_recovery=False),'no cross-pool/automatic recovery')
    check(d['equipment_owner_refs']==EQUIPMENT,'equipment identity/resource ownership differs')
    for ident in EQUIPMENT:ref(ident)
    links=d['phase2_links'];check(isinstance(links,list) and len(links)==7,'all seven prior phases required');phases=set()
    for row in links:
        shape(row,{'phase','owner_ids'});n=row['phase'];check(type(n) is int and n in PHASE_OWNERS and n not in phases and row['owner_ids']==PHASE_OWNERS[n],'phase authority routing differs');phases.add(n)
        for ident in row['owner_ids']:ref(ident)
    check(d['rank_policy']==dict(adventurer_scale_owner_ref='guild-network',dungeon_rating_domain='dungeon-threat',shattered_meridian_raw_label='SS',compatible_adventurer_rank=None,status='UNRESOLVED LEGACY SS',changes_theron_rank=False),'SS cannot become a global adventurer rank')
    e=extension;shape(e,'classification approval_source_ref integration_owner_ref profiles actual_spawns actual_encounters actual_loot automatic_respawn'.split());approval('dungeon-ecology-and-hazards',e)
    check(e['integration_owner_ref']==OWNER,'competing monster integration owner')
    check(all(e[k]==[] for k in ('actual_spawns','actual_encounters','actual_loot')) and e['automatic_respawn'] is False,'no encounters, spawns, loot or respawn')
    old={m['id']:m for m in ecology['approved_reference_design']['monster_references']}
    rows=e['profiles'];check(isinstance(rows,list) and len(rows)==5,'five reference profiles required');ids=set()
    for m in rows:
        shape(m,PROFILE_TEXT|set('reference_id classification ecology_owner_field combat_ready numerical_completion_status new_spell_names current_instances'.split()))
        ident=m['reference_id'];check(isinstance(ident,str) and ident in old and ident not in ids,'duplicate/unsupported monster identity');ids.add(ident)
        check(m['classification']=='DESCRIPTIVE COMBAT REFERENCE' and m['ecology_owner_field']=='approved_reference_design.monster_references','original monster stats/ecology authority required')
        check(m['combat_ready'] is False and m['new_spell_names']==[] and m['current_instances'] is None,'no combat-ready opponent, new power or current instance')
        for f in PROFILE_TEXT|{'numerical_completion_status'}:text(m[f])
        check(old[ident]['combat_usable'] is False and all(old[ident][f] is None for f in ('attack_bonus','damage_formula','movement','resistances','current_instance_count')),'missing numerical mechanics cannot be silently completed')


def audit(root):
    if __package__:from .validate import validate
    else:from validate import validate
    validation=validate(root);state=json.loads((root/'state/checkpoint.json').read_text());ledger=json.loads((root/'state/finance-ledger.json').read_text())
    ecology=payload(root,'entities/mechanics/dungeon-ecology-and-hazards.md');refs=ecology['approved_reference_design'];counts=dict(areas=0,connections=0,encounters=0,hazards=len(refs['hazard_references']))
    if __package__:from .dungeon_designs import DUNGEONS
    else:from dungeon_designs import DUNGEONS
    for ident in DUNGEONS:
        d=payload(root,'entities/mechanics/'+ident+'.md')['dungeon_design']
        for field,key in [('areas','areas'),('connections','connections'),('encounter_designs','encounters')]:counts[key]+=len(d[field])
    manifest=root/'tests/fixtures/phase2-08-preservation.json';preservation=None
    if manifest.is_file():
        expected = json.loads(manifest.read_text())['unchanged_sha256']
        revised = set()
        for filename in ('day196-authority-revisions.json', 'suncrest262-authority-revisions.json',
                         'character-sheet-authority-revisions.json', 'year851-day160-authority-revisions.json',
                         'year852-day1-authority-revisions.json', 'dragon-humanoid-reference-revisions.json',
                         'twin-sword-authority-revisions.json'):
            session_manifest = manifest.with_name(filename)
            revisions = json.loads(session_manifest.read_text())['revisions'] if session_manifest.is_file() else {}
            for path in set(expected) & set(revisions):
                need(expected[path] == revisions[path]['before_sha256'], 'session revision baseline differs: '+path)
                expected[path] = revisions[path]['after_sha256']
                revised.add(path)
        mismatches = [path for path, digest in expected.items() if hashlib.sha256((root/path).read_bytes()).hexdigest() != digest]
        need(not mismatches, 'untouched or approved source mismatch: '+str(mismatches))
        preservation = dict(unchanged_files=len(expected)-len(revised), approved_revisions=sorted(revised), mismatches=mismatches)
    topics=['entity-identity','references','spell-costs','HP-MP-DEF','rank-domains','travel-access','finite-magic','property-ownership','sole-finance-authority','appointments','world-events','quest-progress','chronology','companion-identity','monster-statistics','dungeon-discovery','public-reference-safety','canon-preservation']
    open_items={'spell-costs':'Two supplied costs lack a current spell owner;40% repricing/base costs unresolved. Existing costs preserved.',
                'rank-domains':'SS remains unresolved dungeon-threat design, not a new adventurer rank.',
                'public-reference-safety':'New references are declared public; existing mixed-knowledge source material is not certified spoiler-clean.'}
    return dict(classification='READ-ONLY DESIGN INTEGRATION AUDIT',validation=validation,
        audit_findings=[dict(topic=t,status='QUALIFIED / OPEN' if t in open_items else 'CHECKED WITH VALIDATORS AND PRESERVATION',note=open_items.get(t,'No new actual event or state change; existing owner and regression protections apply.')) for t in topics],
        schools=8,preserved_cost_checks={n:dict(listed_mp=mp,status='PRESERVED; no automatic40% repricing') for n,mp in PRESERVED_COSTS.items()},
        unverified_cost_references=['Deep Mend17MP','Greater Healing21MP'],dungeon_design_counts=counts,
        monster_references=[{k:m[k] for k in ('id','name','hp','mp','defense','reference_rank','combat_usable')} for m in refs['monster_references']],
        numerical_combat_ready=False,design_completion='Public classification/procedures and descriptive profiles complete; unresolved mechanics remain explicit.',
        current_resources=state['resources'],equipment_configuration_status=state['provenance']['current_equipment']['status'],conditional_night_sovereign_defense=state['provenance']['conditional_defense'],current_hp_mp={k:state['theron'][k] for k in ('hp','hp_max','mp','mp_max')},
        finances=dict(schema_version=ledger['schema_version'],controlled_cp=ledger['controlled_cash']['total_cp'],classification=ledger.get('endpoint', {}).get('classification'),allocation_status=ledger['controlled_cash']['allocation_status']),
        preservation=preservation,ending_readiness='UNCHANGED:18 pending answer approvals /14 unfilled clue routes; not complete',gameplay_performed=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--audit',action='store_true',required=True);args=parser.parse_args()
    try:print(json.dumps(audit(args.root),indent=2))
    except (ValueError,OSError) as exc:parser.exit(1,str(exc)+'\n')


if __name__=='__main__':main()
