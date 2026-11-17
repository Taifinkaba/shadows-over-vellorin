"""Read-only source-state routing and dungeon proposal validation."""
import json
import re

EXPLORATION_STATUSES={'unknown','unexplored','partially-explored','visited','explored','cleared','sealed','inaccessible','destroyed'}


def read_section_state(root, reference, require, repository_file):
    """Derive observation from the original owner, never save a second status.

    Protection is access information, not an exploration degree. A visit/inspection
    is not clearance. Unrecognized historical wording stays unknown with raw label.
    """
    require(isinstance(reference,dict) and set(reference)=={'source_ref','locator_kind','locator'}, 'dungeons: invalid state reference')
    require(isinstance(reference['locator'],str) and reference['locator'].strip(), 'dungeons: invalid state locator')
    source=repository_file(root,reference['source_ref'],'exploration source').read_text()
    kind=reference['locator_kind'];label=reference['locator']
    if kind=='table-row':
        rows=[]
        for line in source.splitlines():
            cells=[c.strip() for c in line.strip().split('|')[1:-1]] if line.strip().startswith('|') else []
            if len(cells)==2 and cells[0]==label:rows.append(cells[1])
        require(len(rows)==1,'dungeons: state row missing or ambiguous')
        raw=rows[0].split(';',1)[0].strip()
        value=raw.casefold()
        mapped={'unknown':'unknown','unexplored':'unexplored','partially explored':'partially-explored',
                'visited':'visited','searched':'explored','explored':'explored','cleared':'cleared','sealed':'sealed',
                'inaccessible':'inaccessible','destroyed':'destroyed'}
        return {'exploration_status':mapped.get(value,'unknown'),'access_status':'protected' if value=='protected' else None,
                'source_label':raw}
    require(kind=='inspection-phrase','dungeons: unsupported section locator kind')
    require(label in source,'dungeons: inspection source phrase missing')
    # A recorded inspection is an observation/visit, not proof every space was searched.
    return {'exploration_status':'visited','access_status':None,'source_label':'Recorded inspection; full exploration/clearance unverified'}


def validate_population_event(event, root, site_ids, creature_ids, require, repository_file):
    """Prospective source completeness only; never spawn or change any creature."""
    fields={'site_id','creature_reference_id','status','cause','elapsed_time_ref','event_ref','source_refs','automatic'}
    require(isinstance(event,dict) and set(event)==fields,'dungeons population: invalid fields')
    require(isinstance(event['site_id'],str) and event['site_id'] in site_ids,'dungeons population: unknown site')
    require(isinstance(event['creature_reference_id'],str) and event['creature_reference_id'] in creature_ids,'dungeons population: unknown creature')
    require(event['automatic'] is False,'dungeons population: automatic respawn forbidden')
    require(event['status'] in ('proposed','recorded'),'dungeons population: invalid status')
    refs=event['source_refs']
    require(isinstance(refs,list) and all(isinstance(x,str) for x in refs) and len(refs)==len(set(refs)),
            'dungeons population: invalid sources')
    for ref in refs:repository_file(root,ref,'population source')
    if event['status']=='recorded':
        require(isinstance(event['cause'],str) and event['cause'].strip(),'dungeons population: plausible cause required')
        for field in ('elapsed_time_ref','event_ref'):
            require(event[field] is not None and event[field] in refs,'dungeons population: elapsed time and actual event sources required')
            repository_file(root,event[field],field)


def validate_dungeons(root, records, require, repository_file, unique_json):
    required={'dungeon-registry','exploration-sections','dungeon-ecology-and-hazards','dungeon-design-proposals','dungeon-exploration'}
    if not(required & records.keys()):return
    require(required<=records.keys(),'dungeons: incomplete framework')
    def shape(d,fields,label):
        require(isinstance(d,dict) and set(d)==set(fields.split()),f'dungeons: invalid {label} fields')
    def text(s,label):
        require(isinstance(s,str) and s.strip(),f'dungeons: invalid {label}')
    def strings(values,label):
        require(isinstance(values,list) and all(isinstance(x,str) and x.strip() for x in values),f'dungeons: invalid {label}')
        require(len(values)==len(set(values)),f'dungeons: duplicate {label}')
    def ref(ident,kinds=None):
        require(isinstance(ident,str) and ident in records,'dungeons: broken entity reference')
        require(kinds is None or records[ident]['type'] in kinds,'dungeons: wrong reference type')
        require(records[ident]['visibility']=='gm-reference','dungeons: secret reference excluded from public lookup')
    def place(ident):
        ref(ident,{'locations'});require(not ident.startswith('route-'),'dungeons: physical location required')
    def source(path):
        if isinstance(path,str) and path.startswith('entities/'):
            ref(path.rsplit('/',1)[-1].removesuffix('.md'))
        return repository_file(root,path,'dungeon source')
    def refs(values):
        strings(values,'source refs');require(values,'dungeons: source refs required')
        for path in values:source(path)
    def payload(ident):
        p=root/f"entities/{records[ident]['type']}/{ident}.md"
        blocks=re.findall(r'^```json\n(.*?)\n```$',p.read_text(),re.M|re.S)
        require(len(blocks)==1,'dungeons: expected one JSON block')
        try:d=json.loads(blocks[0],object_pairs_hook=unique_json)
        except ValueError as exc:require(False,f'dungeons: invalid JSON: {exc}')
        require(isinstance(d,dict) and type(d.get('schema_version')) is int and d['schema_version']==1,'dungeons: unsupported schema')
        return d
    def state_ref(d,allowed_kinds):
        shape(d,'source_ref locator_kind locator','state pointer')
        text(d['locator'],'state locator');source(d['source_ref'])
        require(d['locator_kind'] in allowed_kinds,'dungeons: invalid locator kind')
        if d['locator_kind'] in ('table-row','inspection-phrase'):
            return read_section_state(root,d,require,repository_file)
        require(d['locator'] in source(d['source_ref']).read_text(),'dungeons: source phrase missing')
        return None

    registry=payload('dungeon-registry')
    shape(registry,'schema_version sites sections_owner_ref ecology_hazards_owner_ref contract_registry_ref new_inventory_records '
          'new_objective_outcomes automatic_respawn automatic_loot','registry')
    require(registry['sections_owner_ref']=='exploration-sections' and registry['ecology_hazards_owner_ref']=='dungeon-ecology-and-hazards'
            and registry['contract_registry_ref']=='contract-registry','dungeons: existing section/ecology/contract owners required')
    for f in ('sections_owner_ref','ecology_hazards_owner_ref','contract_registry_ref'):ref(registry[f],{'mechanics'})
    require(registry['new_inventory_records']==[] and registry['new_objective_outcomes']==[],'dungeons: no new loot or objective completion in maintenance')
    require(registry['automatic_respawn'] is False and registry['automatic_loot'] is False,'dungeons: automatic respawn/loot forbidden')
    require(isinstance(registry['sites'],list),'dungeons: invalid sites')
    sites={};names=set();locations=set();site_sections={}
    for s in registry['sites']:
        shape(s,'site_id name classification record_kind location_entity_id entrance_location_id region_id access_route_ids category danger_classification '
              'exploration_state_ref section_ids creature_context_ids hazard_reference_ids recovered_inventory_owner_refs protected_evidence_owner_refs '
              'associated_quest_ids guild_contract_ids last_verified_visit_ref access_source_refs source_refs aliases note','site')
        ident=s['site_id'];text(ident,'site ID')
        require(ident.startswith('site:') and ident not in sites,'dungeons: duplicate/invalid site ID')
        sites[ident]=s;text(s['name'],'site name')
        name=re.sub(r'[^a-z0-9]','',s['name'].casefold())
        require(name not in names,'dungeons: duplicate canonical site name');names.add(name)
        require(s['classification']=='CONFIRMED CANON','dungeons: design cannot replace source-backed site identity')
        text(s['record_kind'],'record kind');text(s['note'],'site note')
        require(s['record_kind'] in {'investigation-site','historical-site','sanctuary','ordinary-structure-investigation-site',
                                   'named-site-unclassified','shrine-site','observatory-context','infrastructure-site',
                                   'fortress-site','wilderness-area','ordinary-structure','exploration-area-label','entrance-reference'},
                'dungeons: unsupported blanket dungeon classification')
        require(s['aliases']==[],'dungeons: no unsourced alias/merger established')
        if s['location_entity_id'] is not None:
            place(s['location_entity_id'])
            require(s['location_entity_id'] not in locations,'dungeons: duplicate canonical location routing')
            locations.add(s['location_entity_id'])
        if s['entrance_location_id'] is not None:
            place(s['entrance_location_id'])
            require(s['record_kind']=='entrance-reference' and s['entrance_location_id']==s['location_entity_id'],
                    'dungeons: no verified entrance assignment between distinct sites')
        require(s['region_id'] is None and s['category'] is None and s['danger_classification'] is None
                and s['exploration_state_ref'] is None,'dungeons: no unsupported geography, category, threat or whole-site status')
        strings(s['access_route_ids'],'access route IDs')
        require(s['access_route_ids']==[],'dungeons: no verified road-to-entrance connection supplied')
        for field in ('section_ids','creature_context_ids','hazard_reference_ids','recovered_inventory_owner_refs',
                      'protected_evidence_owner_refs','associated_quest_ids','guild_contract_ids','access_source_refs'):
            strings(s[field],field)
        site_sections[ident]=s['section_ids']
        for field in ('recovered_inventory_owner_refs','protected_evidence_owner_refs'):
            for owner in s[field]:ref(owner,{'mechanics'})
        require(set(s['recovered_inventory_owner_refs'])<={'shady-salvage','launder','seven-bells-inventory'},'dungeons: existing inventory owners only')
        require(set(s['protected_evidence_owner_refs'])<={'seven-bells-inventory'},'dungeons: protected evidence cannot be rerouted to loot')
        expected_inventory=(['shady-salvage','launder'] if ident=='site:hollow-first-hour' else
                            ['seven-bells-inventory'] if ident in ('site:north-return-house','site:seven-bells-receiving-chambers') else [])
        require(s['recovered_inventory_owner_refs']==expected_inventory,
                'dungeons: inventory lookup cannot be relocated to another site')
        for q in s['associated_quest_ids']:ref(q,{'quests'})
        require(s['guild_contract_ids']==[],'dungeons: no new offered/site-bound contract supplied')
        if s['last_verified_visit_ref'] is not None:source(s['last_verified_visit_ref'])
        for src in s['access_source_refs']:source(src)
        refs(s['source_refs'])
        # Source names prove retrieval identity only, never geographic equivalence or a connection.
        require(any(s['name'].casefold() in source(x).read_text().casefold() for x in s['source_refs']),
                'dungeons: site name not found in existing source')
    require(len(sites)==18,'dungeons: incomplete source-backed site crosswalk')
    require(sites['site:hollow-first-hour']['location_entity_id']=='hollow-first-hour'
            and sites['site:hollow-veil']['location_entity_id']=='hollow-veil','dungeons: distinct Hollow identities must be preserved')
    require(sites['site:ravencrest-waystation']['record_kind']=='ordinary-structure'
            and sites['site:abbey-bellkeeper-residence']['record_kind']=='ordinary-structure'
            and sites['site:north-return-house']['record_kind']=='ordinary-structure-investigation-site',
            'dungeons: ordinary structures cannot become active dungeons')
    require(sites['site:northern-depository']['protected_evidence_owner_refs']==['seven-bells-inventory'],
            'dungeons: protected originals remain with existing evidence owner')

    section_data=payload('exploration-sections')
    shape(section_data,'schema_version allowed_exploration_statuses sections new_exploration_events','section framework')
    strings(section_data['allowed_exploration_statuses'],'exploration statuses')
    require(set(section_data['allowed_exploration_statuses'])==EXPLORATION_STATUSES,'dungeons: invalid exploration status vocabulary')
    require(section_data['new_exploration_events']==[],'dungeons: no new historical exploration or clearing event')
    require(isinstance(section_data['sections'],list),'dungeons: invalid sections')
    sections={};locators=set()
    for s in section_data['sections']:
        shape(s,'section_id site_id name classification state_ref contents_owner_refs access_ref hazard_reference_ids encounter_history_refs '
              'recovered_inventory_owner_refs remaining_objective_owner_refs last_verified_state_ref source_refs note','section')
        sid=s['section_id'];text(sid,'section ID')
        require(sid not in sections and sid.startswith('section:'),'dungeons: duplicate/invalid section ID')
        sections[sid]=s
        require(s['site_id'] in sites and sid.startswith('section:'+s['site_id'].removeprefix('site:')+':'),
                'dungeons: section site mismatch')
        require(s['classification']=='CONFIRMED CANON','dungeons: no proposed rooms in existing exploration')
        text(s['name'],'section name');text(s['note'],'section note')
        for field in ('contents_owner_refs','hazard_reference_ids','encounter_history_refs','recovered_inventory_owner_refs','remaining_objective_owner_refs'):
            strings(s[field],field)
        require(s['access_ref'] is None and s['hazard_reference_ids']==[] and s['encounter_history_refs']==[],
                'dungeons: no unsupplied section access, trap placement or encounter')
        for field in ('contents_owner_refs','recovered_inventory_owner_refs'):
            require(set(s[field])<={'shady-salvage','launder','seven-bells-inventory'},'dungeons: section cannot duplicate material inventory')
            for owner in s[field]:ref(owner,{'mechanics'})
        expected_inventory=(['shady-salvage','launder'] if sid=='section:hollow-first-hour:supply-annex' else
                            ['seven-bells-inventory'] if sid=='section:north-return-house:cellar' else [])
        require(s['contents_owner_refs']==expected_inventory and s['recovered_inventory_owner_refs']==expected_inventory,
                'dungeons: no unsourced section recovery/contents assignment')
        for owner in s['remaining_objective_owner_refs']:ref(owner,{'quests'})
        refs(s['source_refs']);source(s['last_verified_state_ref'])
        require(s['state_ref']['source_ref'] in s['source_refs'],'dungeons: undeclared section state source')
        observed=state_ref(s['state_ref'],('table-row','inspection-phrase'))
        require(observed['exploration_status'] in EXPLORATION_STATUSES,'dungeons: invalid derived exploration state')
        key=(s['state_ref']['source_ref'],s['state_ref']['locator_kind'],s['state_ref']['locator'])
        require(key not in locators,'dungeons: duplicate section/source inventory alias');locators.add(key)
    for ident,links in site_sections.items():
        require(set(links)=={sid for sid,s in sections.items() if s['site_id']==ident},'dungeons: section routing coverage mismatch')

    ecology_data=payload('dungeon-ecology-and-hazards')
    shape(ecology_data,'schema_version ecology_references hazard_references new_encounter_events new_population_events automatic_respawn automatic_scaling','ecology/hazards')
    require(ecology_data['new_encounter_events']==[] and ecology_data['new_population_events']==[],
            'dungeons: no new encounter, defeat, revival or population event')
    require(ecology_data['automatic_respawn'] is False and ecology_data['automatic_scaling'] is False,
            'dungeons: automatic respawn/stat scaling forbidden')
    creatures={};hazards={}
    require(isinstance(ecology_data['ecology_references'],list),'dungeons: invalid ecology references')
    for c in ecology_data['ecology_references']:
        shape(c,'reference_id name creature_entity_id reference_kind historical_site_ids current_location_id population_count threat_rank behavior_ref species_ref '
              'territory diet group_structure intelligence_ref hostility special_abilities_owner_ref weaknesses last_verified_status_ref encounter_history_refs source_refs note','creature pointer')
        ident=c['reference_id'];text(ident,'creature reference ID')
        require(ident not in creatures,'dungeons: duplicate creature pointer');creatures[ident]=c
        text(c['name'],'creature label');text(c['reference_kind'],'reference kind');text(c['note'],'ecology note')
        require(all(c[f] is None for f in ('current_location_id','population_count','threat_rank','territory','diet','group_structure',
                                         'intelligence_ref','hostility','weaknesses')) and c['encounter_history_refs']==[],
                'dungeons: no new creature location, population, stats or encounters')
        if c['creature_entity_id'] is not None:
            ref(c['creature_entity_id'],{'creatures'})
            require(c['special_abilities_owner_ref']==c['creature_entity_id'],'dungeons: existing creature abilities owner required')
        else:require(c['special_abilities_owner_ref'] is None,'dungeons: no invented creature abilities')
        strings(c['historical_site_ids'],'historical site IDs')
        require(set(c['historical_site_ids'])<=sites.keys(),'dungeons: unknown historical creature context')
        for field in ('behavior_ref','species_ref','last_verified_status_ref'):
            if c[field] is not None:source(c[field])
        refs(c['source_refs'])
    require(isinstance(ecology_data['hazard_references'],list),'dungeons: invalid hazards')
    for h in ecology_data['hazard_references']:
        shape(h,'hazard_id name location_site_id section_id trigger detectability effect disarm_or_avoidance state_ref source_refs new_trigger_events note','hazard pointer')
        ident=h['hazard_id'];text(ident,'hazard ID')
        require(ident not in hazards,'dungeons: duplicate hazard pointer');hazards[ident]=h
        text(h['name'],'hazard label');text(h['note'],'hazard note')
        require(all(h[f] is None for f in ('location_site_id','section_id','trigger','detectability','effect','disarm_or_avoidance'))
                and h['new_trigger_events']==[],'dungeons: no retroactive trap location, solution, effect or trigger event')
        refs(h['source_refs'])
        require(h['state_ref']['source_ref'] in h['source_refs'],'dungeons: undeclared hazard source')
        state_ref(h['state_ref'],('table-row','source-phrase'))
    for s in sites.values():
        require(set(s['creature_context_ids'])<=creatures.keys() and set(s['hazard_reference_ids'])<=hazards.keys(),
                'dungeons: broken creature/hazard reference')

    proposal_data=payload('dungeon-design-proposals')
    shape(proposal_data,'schema_version classification world_census_count proposed_threat_scale proposals automatic_instantiation','proposal crosswalk')
    require(records['dungeon-design-proposals']['status']=='research' and proposal_data['classification']=='PROPOSED'
            and proposal_data['world_census_count'] is None and proposal_data['automatic_instantiation'] is False,
            'dungeons: proposal is not a census or active site')
    require(proposal_data['proposed_threat_scale']==['F','E','D','C','B','A','S','S+'],'dungeons: unapproved threat scale change')
    require(isinstance(proposal_data['proposals'],list) and len(proposal_data['proposals'])==5,'dungeons: five supplied proposals required')
    expected={'Hollowstone Mine':'D','Ashen Anvil':'B','Drowned Archive':'A','Pale Reliquary':'S','Shattered Meridian':'SS'}
    seen=set();proposal_names=set()
    for p in proposal_data['proposals']:
        shape(p,'proposal_id name classification proposed_threat_label scale_compatibility candidate_location_id existing_site_id current_inhabitants treasure '
              'exploration_history collision_review_site_ids collision_note approval_status approval_source_ref source_refs','proposal')
        text(p['proposal_id'],'proposal ID')
        require(p['proposal_id'] not in seen,'dungeons: duplicate dungeon proposal ID');seen.add(p['proposal_id'])
        require(p['name'] in expected and p['name'] not in proposal_names and p['proposed_threat_label']==expected[p['name']],
                'dungeons: supplied proposal rank/name changed or duplicated')
        proposal_names.add(p['name'])
        require(p['classification']=='PROPOSED' and p['approval_status']=='REQUIRES APPROVAL' and p['approval_source_ref'] is None,
                'dungeons: proposed dungeon cannot become approved canon')
        require(all(p[f] is None for f in ('candidate_location_id','existing_site_id','current_inhabitants','treasure')) and p['exploration_history']==[],
                'dungeons: no proposed site placement, merger, monsters, loot or history')
        require(p['scale_compatibility']==('CONFLICT / REQUIRES APPROVAL' if p['proposed_threat_label']=='SS' else 'PROPOSED SCALE LABEL ONLY'),
                'dungeons: SS scale conflict cannot be silently resolved')
        strings(p['collision_review_site_ids'],'collision review IDs')
        require(set(p['collision_review_site_ids'])<=sites.keys(),'dungeons: unknown collision-review site')
        text(p['collision_note'],'collision note');refs(p['source_refs'])

    rules=payload('dungeon-exploration')
    shape(rules,'schema_version classification_framework physical_categories hazard_categories loot_ownership_categories completion_kinds creature_fields '
          'section_fields rank_domains new_loot_records new_combat_events automatic_chest_refill automatic_quest_completion','exploration rules')
    require(rules['classification_framework']=='PROPOSED','dungeons: physical/threat framework not enacted')
    for field in ('physical_categories','hazard_categories','loot_ownership_categories','completion_kinds','creature_fields','section_fields','rank_domains'):
        strings(rules[field],field)
    require(set(rules['rank_domains'])=={'dungeon-threat','combat-power','guild-license','professional-certification','contract-difficulty'},
            'dungeons: rank domains must remain distinct')
    require(set(rules['loot_ownership_categories'])=={'unclaimed','provisional-salvage','party-owned','merchant-owned','protected-evidence','dangerous-isolated',
                                                   'third-party-prisoner-property','consumed','sold','unknown-title'},'dungeons: ownership categories cannot be merged')
    require(rules['new_loot_records']==[] and rules['new_combat_events']==[] and rules['automatic_chest_refill'] is False
            and rules['automatic_quest_completion'] is False,'dungeons: no new loot, battle, chest refill or completion')
