"""Public prospective character/event design guards; no scheduler or event writer."""
import json
import re

APPROVAL='changes/chronicles/phase2-07-autonomy-approval.md'
FIGURES={'elowen-marcrest':(47,'valedorn'),'cassian-thornmere':(39,'valedorn'),
'aveline-hartwell':(54,'valedorn'),'durnek-stonevein':(132,'ironhollow-holds'),
'liora-thistlebloom':(86,'elyndor'),'selene-harrow':(34,'rivermere'),
'orrin-valecrest':(28,'frostmarch'),'mira-hearthwick':(42,'brackenford')}
NEW_FIGURES={'liora-thistlebloom','orrin-valecrest','mira-hearthwick'}
AUTHORITIES=dict(assignments='independent-assignments',factions='faction-activity',chronology='world-event-references',
 communications='settlement-communications',travel='travel-routes',law='justice-and-jurisdiction',
 guilds='guild-membership-and-contracts',economy='economy-accounting',ledger='state/finance-ledger.json')
STATES=['proposed-schedule','planned-action','attempted-action','completed-action','verified-outcome']
ACTIVITIES=['working','traveling','training','resting','shopping','socializing','business-management','meetings','investigation','family-care','personal-interests']
EVENTS=['political-developments','merchant-negotiations','trade-disputes','seasonal-harvests','weather-disruptions','guild-elections','professional-disputes','construction','local-celebrations','criminal-investigations','frontier-conflicts','personal-milestones','natural-disasters','community-projects']
RELATIONSHIPS=['trust','friendship','rivalry','professional-respect','family-bonds','political-alliances','business-partnerships','personal-disagreements','reputation','betrayal','reconciliation']
INTERESTS=['recruitment','trade','political-influence','professional-training','territorial-interests','diplomacy','competition','internal-reform','economic-survival']
PACING=['local-relevance','consequence-severity','information-availability','existing-obligations','time-elapsed','player-proximity','narrative-importance']
EVENT_FIELDS=set('trigger initiating_actor_or_environment participants actor_knowledge time location resources relationships applicable_law action immediate_outcome resource_changes knowledge_changes longer_term_consequences source_refs owner_updates time_advance_evidence discovery_evidence'.split())
SCHEDULE_FIELDS=set('actor proposed_interval activity origin destination verified_route transport weather physical_limits obligations resources consent evidence status'.split())
TEXT_FIELDS=set('role_design personality_traits values public_motivations long_term_goals short_term_interests relationships_design preferences_fears_and_ambitions professional_obligations decision_priorities cooperation_conditions refusal_conditions potential_consequences knowledge_limits routine_design'.split())
NULLS={'current_location','current_job','current_office_id'}
EMPTY={'actual_appointments','actual_relationship_changes','actual_schedules','actual_actions','secret_facts','known_resources'}


def need(condition,message):
    if not condition:raise ValueError('autonomy design: '+message)


def supported(value):
    """Completeness only. Even a complete record still requires independent review."""
    if isinstance(value,bool):return value
    if isinstance(value,str):return bool(value.strip()) and value.strip().upper()!='UNKNOWN'
    if type(value) is int:return value>=0
    if isinstance(value,(dict,list)):
        return bool(value) and all(supported(v) for v in (value.values() if isinstance(value,dict) else value))
    return False


def check_resolution_evidence(record):
    need(isinstance(record,dict) and set(record)==EVENT_FIELDS,'complete causal event fields required')
    need(all(supported(v) for v in record.values()),'actual resolution needs supported evidence; UNKNOWN is not completion')
    # Explicit reviewed no-change/not-applicable evidence is permitted, never invented resources.
    return True


def check_schedule_evidence(record):
    need(isinstance(record,dict) and set(record)==SCHEDULE_FIELDS,'complete scheduling fields required')
    need(record['status'] in STATES,'unsupported action stage')
    if record['status'] in STATES[2:]:
        need(all(supported(v) for v in record.values()),'attempt/completion needs time, travel, consent and resources')
    return True


def check_knowledge_claim(source_kind,receipt_evidence,discovery_evidence):
    need(source_kind in ('direct-observation','received-report','rumor'),'unsupported knowledge source')
    need(supported(receipt_evidence) and supported(discovery_evidence),'information needs receipt/observation and discovery evidence')
    return 'UNVERIFIED RUMOR' if source_kind=='rumor' else 'SOURCE-QUALIFIED; authenticity requires review'


def validate_designs(root,records,require,repository_file,unique_json):
    def get(ident):
        r=records[ident];p=root/f"entities/{r['type']}/{ident}.md"
        return json.loads(re.search(r'^```json\n(.*?)\n```$',p.read_text(),re.M|re.S)[1],object_pairs_hook=unique_json)
    if 'npc-autonomy-and-time' not in records:return
    rule=get('npc-autonomy-and-time');design=rule.get('approved_autonomy_design')
    present={ident for ident in FIGURES if ident in records and 'autonomy_design' in get(ident)}
    if design is None and not present:return
    require(design is not None and present==set(FIGURES),'autonomy design: incomplete eight-character framework')
    def check(c,m):require(c,'autonomy design: '+m)
    def shape(d,fields):check(isinstance(d,dict) and set(d)==set(fields),'unexpected fields')
    def ref(ident):check(ident in records and records[ident]['visibility']=='gm-reference','private/broken public reference')
    def approval(ident,d):
        ref(ident);check(d['classification']=='APPROVED DESIGN' and d['approval_source_ref']==APPROVAL and APPROVAL in records[ident]['source_refs'],'approval provenance differs')
    repository_file(root,APPROVAL,'autonomy approval')
    shape(design,'classification approval_source_ref character_design_ids authority_refs action_states activity_categories event_categories relationship_domains faction_interests pacing_factors schedule_template event_template actual_schedules actual_events actual_knowledge_changes actual_relationship_changes automatic_resolution'.split())
    approval('npc-autonomy-and-time',design)
    check(isinstance(design['character_design_ids'],list) and len(design['character_design_ids'])==8 and set(design['character_design_ids'])==set(FIGURES),'duplicate/missing character identity')
    check(design['authority_refs']==AUTHORITIES,'competing chronology/resource/communication authority')
    for ident in AUTHORITIES.values():
        if ident!='state/finance-ledger.json':ref(ident)
    for field,expected in [('action_states',STATES),('activity_categories',ACTIVITIES),('event_categories',EVENTS),('relationship_domains',RELATIONSHIPS),('faction_interests',INTERESTS),('pacing_factors',PACING)]:
        check(design[field]==expected,'bounded procedure vocabulary differs')
    for field,fields in [('schedule_template',SCHEDULE_FIELDS),('event_template',EVENT_FIELDS)]:
        shape(design[field],fields);check(all(v is None for v in design[field].values()),'empty template cannot assert an event')
    check(design['automatic_resolution'] is False and all(design[f]==[] for f in ('actual_schedules','actual_events','actual_knowledge_changes','actual_relationship_changes')),'no autonomous events or changes during maintenance')
    for ident,(age,region) in FIGURES.items():
        ref(ident);check(records[ident]['type']=='characters','wrong character type');p=get(ident);d=p['autonomy_design']
        shape(d,TEXT_FIELDS|NULLS|EMPTY|set('classification approval_source_ref identity_owner_ref age regional_association unknown_resources historical_source_refs'.split()))
        approval(ident,d);ref(region)
        check(d['identity_owner_ref']==ident and type(d['age']) is int and d['age']==age and d['regional_association']==region,'identity/age/region mismatch')
        for f in TEXT_FIELDS:check(isinstance(d[f],str) and bool(d[f].strip()),'bounded personality/decision text required')
        check(all(d[f] is None for f in NULLS) and all(d[f]==[] for f in EMPTY),'no possessions, appointments, schedules, relationships, secrets or outcomes')
        check(d['unknown_resources']==['funds','possessions','inventory','staff','available-time','physical-condition','current-location'],'resources remain UNKNOWN')
        history=[] if ident in NEW_FIGURES else ['changes/chronicles/phase2-03-government-approval.md']
        check(d['historical_source_refs']==history,'no invented historical character source')
        for path in history:repository_file(root,path,'character history')
        if ident in NEW_FIGURES:shape(p,{'schema_version','autonomy_design'})
        else:check(p['character_design']['age']==age,'existing age authority differs')
        check(type(p['schema_version']) is int and p['schema_version']==1,'invalid character schema')
