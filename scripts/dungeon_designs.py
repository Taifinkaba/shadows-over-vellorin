"""Read-only approved dungeon design/graph checks, with no encounter or loot engine."""
import json
import re

APPROVAL='changes/chronicles/phase2-05-dungeon-approval.md'
DUNGEONS={
 'hollowstone-mine':('Hollowstone Mine','stoneford','D'),
 'ashen-anvil':('Ashen Anvil','ironhollow-holds','B'),
 'drowned-archive':('Drowned Archive','rivermere','A'),
 'pale-reliquary':('Pale Reliquary',None,'S'),
 'shattered-meridian':('Shattered Meridian',None,'SS')}
MONSTERS={
 'giant-cave-spider':('Giant Cave Spider',24,0,12,'D'),
 'fungal-burrower':('Fungal Burrower',36,0,14,'D'),
 'ash-sentinel':('Ash Sentinel',85,40,20,'B'),
 'waterbound-guardian':('Waterbound Guardian',110,80,23,'A'),
 'ancient-reliquary-warden':('Ancient Reliquary Warden',190,160,30,'S')}
SITE_MONSTERS={'hollowstone-mine':{'giant-cave-spider','fungal-burrower'},'ashen-anvil':{'ash-sentinel'},
               'drowned-archive':{'waterbound-guardian'},'pale-reliquary':{'ancient-reliquary-warden'},'shattered-meridian':set()}
HAZARDS={'cave-in','flooding','toxic-spores','extreme-heat','smoke','unstable-bridge','collapsing-floor',
         'low-oxygen','darkness','magical-residue','spatial-instability','unstable-machinery'}
ENCOUNTER_KINDS={'exploration','environmental-hazard','creature-encounter','magical-defense','mechanical-trap',
                 'resource-management','negotiation','stealth','rescue','moral-decision','retreat'}
REWARD_CATEGORIES={'coins','tools','craft-materials','mineral-samples','historical-records','salvage-equipment',
                   'decorative-objects','rare-materials','research-fragments','relics-for-review'}
RECOVERY_FIELDS=set('event_id status dungeon_design_id area_id item_description source_ref quantity unit '
                    'verified_available_quantity discovery_evidence_ref recovery_evidence_ref ownership_provenance_ref '
                    'transport_capacity_ref legal_authority_ref inventory_owner_ref approved_update_evidence_ref finance_transaction_ref'.split())


def validate_recovery_requirements(record,require):
    """Pure completeness/finite-quantity check for a supplied future recovery, never award.

    The caller must independently review source truth, title, transport, legal scope
    and the approved original inventory/finance update. Text is not proof of a fact.
    """
    require(isinstance(record,dict) and set(record)==RECOVERY_FIELDS,'dungeon recovery: incomplete fields')
    require(record['status'] in ('proposed','recorded'),'dungeon recovery: invalid status')
    if record['status']=='proposed':return
    for field in RECOVERY_FIELDS-{'status','quantity','verified_available_quantity','finance_transaction_ref'}:
        require(isinstance(record[field],str) and bool(record[field].strip()),'dungeon recovery: source, discovery, title, transport, law and approved update evidence required')
    q,available=record['quantity'],record['verified_available_quantity']
    require(type(q) is int and type(available) is int and 0<q<=available,
            'dungeon recovery: finite positive quantity within verified availability required')
    require(record['dungeon_design_id'] in DUNGEONS and record['area_id'].startswith('design-area:'+record['dungeon_design_id']+':'),
            'dungeon recovery: wrong design/location scope')
    require(record['finance_transaction_ref'] is None or isinstance(record['finance_transaction_ref'],str) and bool(record['finance_transaction_ref'].strip()),
            'dungeon recovery: invalid original finance reference')


def validate_dungeon_designs(root,records,require,repository_file,unique_json):
    def check(condition,message):require(condition,'dungeon designs: '+message)
    def shape(value,fields):check(isinstance(value,dict) and set(value)==set(fields.split()),'unexpected design fields')
    def text(value):check(isinstance(value,str) and bool(value.strip()),'text required')
    def strings(value):
        check(isinstance(value,list) and all(isinstance(v,str) and v.strip() for v in value) and len(value)==len(set(value)),'invalid/duplicate string list')
    def empty(value,fields):
        for field in fields.split():check(value[field]==[],'no discoveries, populations, loot, damage, quests, abilities or secret outcomes')
    def unknown(value,fields):
        for field in fields.split():check(value[field] is None,'current placement, state, inhabitants, treasure and effects remain unknown')
    def approval(value):check(value==APPROVAL,'wrong approval provenance');repository_file(root,value,'dungeon approval')
    def payload(ident):
        check(ident in records,'missing design owner')
        p=root/f"entities/{records[ident]['type']}/{ident}.md"
        blocks=re.findall(r'^```json\n(.*?)\n```$',p.read_text(),re.M|re.S);check(len(blocks)==1,'one owner JSON block required')
        try:d=json.loads(blocks[0],object_pairs_hook=unique_json)
        except ValueError as exc:check(False,'invalid JSON: '+str(exc))
        check(isinstance(d,dict) and type(d.get('schema_version')) is int and d['schema_version']==1,'unsupported schema')
        return d
    def ref(ident,kind=None):
        check(isinstance(ident,str) and ident in records and records[ident]['visibility']=='gm-reference','invalid public owner reference')
        check(kind is None or records[ident]['type']==kind,'wrong owner type')
    proposal=payload('dungeon-design-proposals') if 'dungeon-design-proposals' in records else {}
    active='approved_design_index' in proposal or bool(set(DUNGEONS)&records.keys())
    if not active:return  # Historical trees without this complete extension remain valid.
    required=set(DUNGEONS)|{'dungeon-design-proposals','dungeon-ecology-and-hazards','dungeon-exploration','guild-network'}
    check(required<=records.keys(),'incomplete dungeon design extension')
    p=proposal.get('approved_design_index')
    shape(p,'classification approval_source_ref profiles ecology_hazards_owner_ref exploration_owner_ref actual_site_instantiations automatic_discovery')
    check(p['classification']=='APPROVED DESIGN','approval is not an active discovered site');approval(p['approval_source_ref'])
    check(p['ecology_hazards_owner_ref']=='dungeon-ecology-and-hazards' and p['exploration_owner_ref']=='dungeon-exploration','competing design owners')
    empty(p,'actual_site_instantiations');check(p['automatic_discovery'] is False,'no automatic discovery')
    check(isinstance(p['profiles'],list),'profile routing required');seen=set()
    legacy={x['proposal_id']:x for x in proposal['proposals']}
    for link in p['profiles']:
        shape(link,'proposal_id entity_id');ident=link['entity_id']
        check(isinstance(ident,str) and ident in DUNGEONS and ident not in seen and link['proposal_id']=='dungeon-proposal:'+ident
              and link['proposal_id'] in legacy,'duplicate/wrong dungeon proposal identity');seen.add(ident)
    check(seen==set(DUNGEONS),'all five proposal identities required')
    reference=payload('dungeon-ecology-and-hazards').get('approved_reference_design')
    shape(reference,'classification approval_source_ref final_combat_integration_phase monster_references hazard_references '
          'actual_population_events actual_encounters actual_damage_events automatic_respawn automatic_scaling')
    check(reference['classification']=='APPROVED DESIGN' and reference['final_combat_integration_phase']=='PR8','combat integration remains PR8');approval(reference['approval_source_ref'])
    empty(reference,'actual_population_events actual_encounters actual_damage_events')
    check(reference['automatic_respawn'] is False and reference['automatic_scaling'] is False,'no automatic respawn or scaling')
    monster_ids=set();check(isinstance(reference['monster_references'],list),'monster references required')
    for m in reference['monster_references']:
        shape(m,'id name classification approval_source_ref hp mp defense reference_rank compatibility combat_usable '
              'attack_bonus damage_formula movement resistances current_instance_count ecological_constraints')
        ident=m['id'];check(isinstance(ident,str) and ident.startswith('monster-reference:') and ident[18:] in MONSTERS and ident not in monster_ids,'duplicate/wrong monster reference')
        monster_ids.add(ident);name,hp,mp,defense,rank=MONSTERS[ident[18:]]
        check(m['name']==name and all(type(m[f]) is int for f in ('hp','mp','defense')) and
              (m['hp'],m['mp'],m['defense'],m['reference_rank'])==(hp,mp,defense,rank),'reference stats contradict approval')
        check(m['classification']=='PROPOSED' and m['combat_usable'] is False,'reference-only monster stats; no usable opponent')
        approval(m['approval_source_ref']);text(m['compatibility']);text(m['ecological_constraints'])
        unknown(m,'attack_bonus damage_formula movement resistances current_instance_count')
    check(monster_ids=={'monster-reference:'+x for x in MONSTERS},'five approved monster references required')
    hazards=set();check(isinstance(reference['hazard_references'],list),'hazard references required')
    for h in reference['hazard_references']:
        shape(h,'id classification trigger observable_warnings exposure possible_consequences avoidance_or_mitigation '
              'required_resources failure_conditions recovery_limitations numerical_effects automatic_damage current_placement_ids')
        ident=h['id'];check(isinstance(ident,str) and ident in {'hazard-design:'+x for x in HAZARDS} and ident not in hazards,'duplicate/missing hazard design');hazards.add(ident)
        check(h['classification']=='APPROVED DESIGN' and h['automatic_damage'] is False,'no automatic hazard damage')
        for field in ('trigger','observable_warnings','exposure','possible_consequences','avoidance_or_mitigation',
                      'required_resources','failure_conditions','recovery_limitations'):text(h[field])
        unknown(h,'numerical_effects current_placement_ids')
    check(hazards=={'hazard-design:'+x for x in HAZARDS},'twelve hazard categories required')
    guilds=payload('guild-network')['approved_design_index'];factions=set(guilds['professional_guild_ids'])|set(guilds['criminal_faction_ids'])
    all_encounter_kinds=set()
    for ident,(name,region,rank) in DUNGEONS.items():
        ref(ident,'mechanics');check(records[ident]['status']=='canon' and APPROVAL in records[ident]['source_refs'],'design owner provenance mismatch')
        data=payload(ident);shape(data,'schema_version dungeon_design');d=data['dungeon_design']
        shape(d,'classification approval_source_ref proposal_id name purpose_and_history_design regional_association difficulty '
              'areas connections entry_interface_area_ids retreat_path_designs access_and_rest_limits resource_requirements '
              'ecology_design ecological_boundary encounter_designs treasure_categories recovery_rule_ref treasure_policy '
              'legal_owner_ref legal_access_design prospective_faction_interests discovery_requirements lead_categories '
              'persistence_rule current_conditions current_population current_reward_inventory current_recoverable_quantity '
              'actual_discoveries actual_exploration_events actual_population_events actual_reward_events actual_quest_outcomes '
              'hidden_solutions hidden_treasure_locations unsupported_mystery_connections new_abilities existing_site_id')
        check(d['classification']=='APPROVED DESIGN' and d['proposal_id']=='dungeon-proposal:'+ident and d['name']==name,'dungeon identity/classification mismatch');approval(d['approval_source_ref'])
        a=d['regional_association'];shape(a,'classification candidate_region_id description verified_entrance_id exact_coordinates access_route_ids')
        check(a['classification']=='PROPOSED' and a['candidate_region_id']==region,'candidate region cannot become verified placement')
        if region:ref(region,'locations')
        text(a['description']);unknown(a,'verified_entrance_id exact_coordinates');empty(a,'access_route_ids')
        r=d['difficulty'];shape(r,'domain design_label legacy_proposed_label compatible_rank mapping_status combat_integration_phase')
        check(r['domain']=='dungeon-threat' and r['design_label']==r['legacy_proposed_label']==rank and r['combat_integration_phase']=='PR8','rank is not global combat integration')
        check(r['compatible_rank']==(None if rank=='SS' else rank) and r['mapping_status']==('UNRESOLVED LEGACY SS' if rank=='SS' else 'DESIGN REFERENCE ONLY'),'legacy SS mapping cannot be silently resolved')
        check(isinstance(d['areas'],list) and len(d['areas'])==5,'finite five-area design required');areas=set()
        for area in d['areas']:
            shape(area,'id name description classification hazard_reference_ids current_state current_inhabitants current_contents')
            area_id=area['id'];check(isinstance(area_id,str) and re.fullmatch('design-area:'+re.escape(ident)+r':[a-z]+(?:-[a-z]+)*',area_id) and area_id not in areas,'duplicate/wrong area identity');areas.add(area_id)
            check(area['classification']=='APPROVED DESIGN','area is not a surveyed discovery');text(area['name']);text(area['description'])
            strings(area['hazard_reference_ids']);check(set(area['hazard_reference_ids'])<=hazards,'unknown area hazard')
            unknown(area,'current_state current_inhabitants current_contents')
        strings(d['entry_interface_area_ids']);check(bool(d['entry_interface_area_ids']) and set(d['entry_interface_area_ids'])<=areas,'entry interfaces are internal design areas only')
        check(isinstance(d['connections'],list) and 4<=len(d['connections'])<=10,'bounded physical connection graph required');adj={a:set() for a in areas};edges=set()
        for edge in d['connections']:
            shape(edge,'from_area_id to_area_id classification physical_model traversal_condition reverse_possible current_passability')
            start,end=edge['from_area_id'],edge['to_area_id'];check(isinstance(start,str) and isinstance(end,str) and start in areas and end in areas and start!=end,'invalid physical graph endpoint')
            key=tuple(sorted((start,end)));check(key not in edges,'duplicate physical connection');edges.add(key)
            check(edge['classification']=='APPROVED DESIGN' and edge['reverse_possible'] is True,'physical reverse retreat design required')
            text(edge['physical_model']);text(edge['traversal_condition']);unknown(edge,'current_passability');adj[start].add(end);adj[end].add(start)
        reached=set(d['entry_interface_area_ids']);pending=list(reached)
        while pending:
            current=pending.pop()
            for target in adj[current]-reached:reached.add(target);pending.append(target)
        check(reached==areas,'all design areas must connect to an entry/retreat interface')
        paths=d['retreat_path_designs'];check(isinstance(paths,list) and len(paths)>=2,'multiple retreat design options required');seen_paths=set()
        for path in paths:
            strings(path);check(len(path)>=2 and set(path)<=areas and path[-1] in d['entry_interface_area_ids'],'retreat must reach a design interface')
            check(tuple(path) not in seen_paths,'duplicate retreat option');seen_paths.add(tuple(path))
            check(all(b in adj[a] for a,b in zip(path,path[1:])),'retreat path has no physical connection')
        for field in ('purpose_and_history_design','access_and_rest_limits','ecology_design','ecological_boundary','treasure_policy',
                      'legal_access_design','persistence_rule'):text(d[field])
        for field in ('resource_requirements','treasure_categories','discovery_requirements','lead_categories'):strings(d[field]);check(bool(d[field]),'resources, finite treasure/discovery categories required')
        check(1<=len(d['treasure_categories'])<=6,'bounded potential reward categories required')
        check(d['recovery_rule_ref']=='dungeon-exploration' and d['legal_owner_ref']=='justice-and-jurisdiction','existing recovery/legal ownership required')
        check(isinstance(d['encounter_designs'],list) and 3<=len(d['encounter_designs'])<=8,'finite encounter design required');encounters=set();site_monsters=set()
        for e in d['encounter_designs']:
            shape(e,'id classification types area_id premise monster_reference_ids options required_resources guaranteed_success current_population_count actual_outcomes')
            eid=e['id'];check(isinstance(eid,str) and eid.startswith('encounter-design:'+ident+':') and eid not in encounters,'duplicate/wrong encounter owner');encounters.add(eid)
            check(e['classification']=='PROPOSED' and e['area_id'] in areas and e['guaranteed_success'] is False,'encounter is not a current guaranteed event')
            strings(e['types']);check(bool(e['types']) and set(e['types'])<=ENCOUNTER_KINDS,'unknown encounter kind');all_encounter_kinds.update(e['types'])
            strings(e['monster_reference_ids']);check(set(e['monster_reference_ids'])<=monster_ids,'unknown reference monster');site_monsters.update(e['monster_reference_ids'])
            for field in ('premise','options','required_resources'):text(e[field])
            unknown(e,'current_population_count');empty(e,'actual_outcomes')
        check(site_monsters=={'monster-reference:'+x for x in SITE_MONSTERS[ident]},'dungeon-specific monster reference mismatch')
        check(isinstance(d['prospective_faction_interests'],list),'faction interests required');seen_factions=set()
        for f in d['prospective_faction_interests']:
            shape(f,'faction_id classification interest actual_operations');fid=f['faction_id']
            check(isinstance(fid,str) and fid in factions and fid not in seen_factions and f['classification']=='PROPOSED','faction interest is not an operation or hidden link');seen_factions.add(fid)
            text(f['interest']);empty(f,'actual_operations')
        unknown(d,'current_conditions current_population current_reward_inventory current_recoverable_quantity existing_site_id')
        empty(d,'actual_discoveries actual_exploration_events actual_population_events actual_reward_events actual_quest_outcomes hidden_solutions hidden_treasure_locations unsupported_mystery_connections new_abilities')
    check(all_encounter_kinds==ENCOUNTER_KINDS,'all exploration/noncombat/retreat encounter types required')
    rule=payload('dungeon-exploration').get('approved_exploration_design')
    shape(rule,'classification approval_source_ref design_owner_ref reference_owner_ref historical_sections_owner_ref finance_owner_ref '
          'legal_owner_ref magic_owner_refs salvage_owner_refs recovery_template procedure actual_recoveries actual_damage_events '
          'actual_discoveries actual_resource_postings automatic_population automatic_damage automatic_loot automatic_recovery potential_reward_categories')
    check(rule['classification']=='APPROVED DESIGN','exploration rules are not actual events');approval(rule['approval_source_ref'])
    check(rule['design_owner_ref']=='dungeon-design-proposals' and rule['reference_owner_ref']=='dungeon-ecology-and-hazards'
          and rule['historical_sections_owner_ref']=='exploration-sections' and rule['finance_owner_ref']=='party-finances'
          and rule['legal_owner_ref']=='justice-and-jurisdiction','no competing history, treasure, finance or law authority')
    check(rule['magic_owner_refs']==['theron-spells','theron-abilities'] and rule['salvage_owner_refs']==['shady-salvage','launder','seven-bells-inventory'],'preserve original spell/inventory/evidence owners')
    for ident in rule['magic_owner_refs']+rule['salvage_owner_refs']:ref(ident)
    strings(rule['potential_reward_categories']);check(set(rule['potential_reward_categories'])==REWARD_CATEGORIES,'finite reward category framework required')
    template=rule['recovery_template'];check(isinstance(template,dict) and set(template)==RECOVERY_FIELDS,'complete recovery template required')
    for field in RECOVERY_FIELDS:
        expected='proposed' if field=='status' else None
        check(template[field]==expected and type(template[field]) is type(expected),'empty recovery template cannot grant treasure')
    text(rule['procedure']);empty(rule,'actual_recoveries actual_damage_events actual_discoveries actual_resource_postings')
    for field in ('automatic_population','automatic_damage','automatic_loot','automatic_recovery'):check(rule[field] is False,'no automatic population, damage, loot or recovery')
