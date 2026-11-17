"""Read-only assignment/faction/event routing; no simulation, clock or write API."""
import json
from pathlib import Path
import re

HELPERS={'independent-assignments','faction-activity','world-event-references','world-development-proposals','npc-autonomy-and-time'}
WORKFLOW=['proposed','offered','accepted','active-last-verified','paused','blocked','awaiting-response','completed','failed','canceled','outcome-unknown']
EVENT_CATEGORIES=['merchant-negotiations','guild-recruitment','military-patrols','criminal-movements','political-negotiations','supply-shortages','construction','research','investigations','diplomatic-responses','rival-expeditions']
CLOCK_CATEGORIES=['political-tensions','criminal-investigations','merchant-activity','construction','training','guild-activity','dungeon-threats','regional-conflicts','seasonal-conditions','npc-personal-goals']
RELATIONSHIP_DOMAINS=['personal-trust','professional-standing','guild-reputation','government-reputation','public-notoriety','criminal-fear','faction-alliances','friendships','family']
ASSIGNMENT_FIELDS=['assignment_id','actor_id','responsibility','request_source','acceptance','willingness_conditions','last_verified_location','last_verified_date','quest_project','resources','permissions','constraints','progress_evidence','verification_status','report_destination','next_dependency','source_refs','knowledge']
FACTION_FIELDS=['name','territory_presence','leadership','members','objectives','allies','rivals','resources','legal_status','last_verified_activity','relationships','active_quests','pending_investigations','source_refs','knowledge']
EVENT_FIELDS=['event_id','date','time','location_id','initiator_id','participant_ids','category','trigger_ref','action_ref','outcome_ref','affected_actor_ids','affected_faction_ids','quest_ids','resource_effect_refs','knowledge','source_refs','time_advance_ref']
CLOCK_FIELDS=['clock_id','owner_ref','starting_condition_ref','source_refs','current_verified_progress','trigger_refs','possible_consequences','visibility','last_verified_date','approval_ref']
RELATIONSHIP_FIELDS=['subject_id','counterparty_id','domain','evidence_ref','date','visibility','discovery_ref','change_source_ref']
ACTORS={'theron-ashvale','tomas','master-beren','vaeltharion','garrick-vale','nyx-thorne','lyra-moonvale','lyanna-ashvale','aric-ashvale','therons-mother','halden-marr','bren','alpha','shade','ember','aurelion','frost','frostmoon','hounds-tomas','bracken','morrow','caelrix','aeloryn','caelan-ashvale','mira-lodge-helper','joren','elsi','elias-renn','maera','mira-thorne'}
ASSIGNMENTS={'tomas-estate':'tomas','tomas-lodge':'tomas','beren-academy':'master-beren','vaeltharion-academy':'vaeltharion','vaeltharion-request':'vaeltharion','garrick-inquiry':'garrick-vale','garrick-expedition':'garrick-vale','nyx-scout':'nyx-thorne','lyra-care':'lyra-moonvale','lyra-springs':'lyra-moonvale','aric-research':'aric-ashvale','bren-maintenance':'bren','mira-lodge-work':'mira-lodge-helper','joren-lodge-work':'joren','elsi-lodge-work':'elsi','elias-academy':'elias-renn','maera-academy':'maera','mira-academy':'mira-thorne','shade-expedition':'shade','ember-expedition':'ember'}
FACTIONS={'wayfarers-guild','dragon-slayer-academy','northern-provisioning-consortium','wardens','crown-black-ledger','continental-guild-concord'}
CHRONICLES={'year847-day153-development','year847-day153-finances','year847-day153-freight','year847-day472-first-hour','year848-day137-end-session','year848-day156-end-session'}


def check(condition,message):
    if not condition:raise ValueError('autonomy: '+message)


def text(value):
    check(isinstance(value,str) and bool(value.strip()),'nonempty text required')


def source(root,path):
    if __package__:from .validate import repository_file
    else:from validate import repository_file
    return repository_file(root,path,'autonomy source')


def evidence(root,reference):
    check(isinstance(reference,dict) and set(reference)=={'source_ref','quote'},'evidence fields differ')
    text(reference['quote']);p=source(root,reference['source_ref'])
    check(reference['quote'] in p.read_text(),'source quote missing')
    # This is an evidence locator, not a player-visible excerpt or new status.
    return reference.copy()


def payload(path,unique_json=None):
    blocks=re.findall(r'^```json\n(.*?)\n```$',path.read_text(),re.M|re.S)
    check(len(blocks)==1,'one JSON block required')
    return json.loads(blocks[0],object_pairs_hook=unique_json)


def validate_event_candidate(event,root,records,existing_ids=()):
    """Prospective evidence completeness, never create/apply an event.

    This neutral public-storage contract rejects GM-only content. Existence of a
    document/quote cannot prove event truth, legal powers or player discovery.
    """
    check(isinstance(event,dict) and set(event)==set(EVENT_FIELDS)|{'status','automatic','discovery_ref'},'event fields differ')
    text(event['event_id']);check(event['event_id'] not in existing_ids,'duplicate historical event')
    check(event['status'] in ('proposed','recorded'),'invalid event status')
    check(event['automatic'] is False,'automatic world events forbidden')
    check(event['knowledge'] in ('requires-discovery-review','player-known'),'secret content requires safe storage outside public framework')
    def ref(ident,kinds):
        check(isinstance(ident,str) and ident in records and records[ident]['type'] in kinds,'invalid entity reference')
        check(records[ident]['visibility']=='gm-reference','secret entity forbidden in public event')
    def refs(values,kinds):
        check(isinstance(values,list) and all(isinstance(x,str) for x in values) and len(values)==len(set(values)),'duplicate/invalid event actors')
        for ident in values:ref(ident,kinds)
    if event['location_id'] is not None:ref(event['location_id'],{'locations'})
    if event['initiator_id'] is not None:ref(event['initiator_id'],{'characters','creatures','factions'})
    for field,kinds in [('participant_ids',{'characters','creatures','factions'}),('affected_actor_ids',{'characters','creatures'}),('affected_faction_ids',{'factions'}),('quest_ids',{'quests'})]:refs(event[field],kinds)
    check(event['category'] in EVENT_CATEGORIES,'unsupported event category')
    check(isinstance(event['source_refs'],list) and all(isinstance(x,str) for x in event['source_refs']) and len(event['source_refs'])==len(set(event['source_refs'])),'duplicate/invalid sources')
    for path in event['source_refs']:source(root,path)
    for field in ('date','time'):
        check(event[field] is None or isinstance(event[field],str) and bool(event[field].strip()),'invalid event date/time; unknown is null')
    for field in ('trigger_ref','action_ref','outcome_ref','time_advance_ref','discovery_ref'):
        if event[field] is not None:
            evidence(root,event[field]);check(event[field]['source_ref'] in event['source_refs'],'event evidence not in sources')
    check(isinstance(event['resource_effect_refs'],list) and all(isinstance(x,str) for x in event['resource_effect_refs']) and len(event['resource_effect_refs'])==len(set(event['resource_effect_refs'])),'invalid resource references')
    for path in event['resource_effect_refs']:
        check(path=='state/finance-ledger.json' or path.startswith('entities/'),'resource effects must link original authority, never a new balance')
        source(root,path)
    if event['status']=='recorded':
        for field in ('trigger_ref','action_ref','outcome_ref','time_advance_ref'):check(event[field] is not None,'recorded event needs actual time-advance/scene, trigger, action and outcome evidence')
        # Missing exact time/date can be retained honestly; never invent one or start a countdown.
        check(bool(event['source_refs']),'recorded event source required')
    else:
        check(event['action_ref'] is None and event['outcome_ref'] is None and not event['resource_effect_refs'],'proposed event cannot assert action/outcome/resource postings')
    if event['knowledge']=='player-known':check(event['discovery_ref'] is not None,'player knowledge needs discovery evidence')


def validate_public_clock_proposal(clock,root,records):
    """Only unstarted proposals; active or secret simulation is outside this API."""
    check(isinstance(clock,dict) and set(clock)==set(CLOCK_FIELDS)|{'classification','automatic'},'clock fields differ')
    text(clock['clock_id'])
    check(clock['owner_ref'] in records and records[clock['owner_ref']]['type'] in ('factions','quests','mechanics'),'invalid clock owner')
    check(records[clock['owner_ref']]['visibility']=='gm-reference','secret owner forbidden')
    check(clock['classification']=='PROPOSED' and clock['automatic'] is False,'clock must remain proposed and manual')
    check(clock['visibility']=='public-reference','secret clock needs safe storage decision')
    check(clock['current_verified_progress'] is None and clock['last_verified_date'] is None and clock['approval_ref'] is None,'no fabricated clock progress/date/approval')
    check(clock['starting_condition_ref'] is None and clock['trigger_refs']==[] and clock['possible_consequences']==[],'no active clock conditions or guaranteed consequences in template')
    check(isinstance(clock['source_refs'],list) and bool(clock['source_refs']) and all(isinstance(x,str) for x in clock['source_refs']) and len(clock['source_refs'])==len(set(clock['source_refs'])),'clock source required')
    for path in clock['source_refs']:source(root,path)


def validate_autonomy(root,records,require,repository_file,unique_json):
    if not HELPERS.intersection(records):return
    require(HELPERS<=records.keys(),'autonomy: incomplete framework')
    def get(ident):return payload(root/f"entities/{records[ident]['type']}/{ident}.md",unique_json)
    def shape(d,fields):
        check(isinstance(d,dict) and set(d)==set(fields.split()),'unexpected fields')
        check(type(d['schema_version']) is int and d['schema_version']==1,'invalid schema')
    def ref(ident,kinds):
        check(isinstance(ident,str) and ident in records and records[ident]['type'] in kinds,'invalid entity reference')
        check(records[ident]['visibility']=='gm-reference','secret entity forbidden in public routing')
    def owner(ident,path):
        ref(ident,{'characters','creatures','factions','mechanics','quests','items'})
        check(path==f"entities/{records[ident]['type']}/{ident}.md",'owner/source mismatch');source(root,path)
    def rows(values,key,expected):
        check(isinstance(values,list) and all(isinstance(x,dict) and isinstance(x.get(key),str) for x in values),'invalid routing rows')
        ids=[x[key] for x in values]
        check(len(ids)==len(set(ids)),'duplicate routing IDs')
        check(set(ids)==set(expected),'routing coverage differs')
    a=get('independent-assignments')
    shape(a,'schema_version classification actors assignments owner_field_contract construct_contexts support_refs new_assignment_events new_communications automatic_outcomes')
    check(a['classification']=='CONFIRMED CANON' and a['owner_field_contract']==ASSIGNMENT_FIELDS,'assignment classification/field contract differs')
    check(a['new_assignment_events']==[] and a['new_communications']==[] and a['automatic_outcomes'] is False,'maintenance cannot complete/communicate assignments')
    rows(a['actors'],'actor_id',ACTORS)
    for row in a['actors']:
        check(set(row)=={'actor_id','source_ref','knowledge'},'actor fields differ')
        ref(row['actor_id'],{'characters','creatures'});owner(row['actor_id'],row['source_ref'])
        check(row['knowledge']=='requires-discovery-review','actor facts are not automatically player-known')
    rows(a['assignments'],'assignment_id',{'assignment:'+x for x in ASSIGNMENTS})
    for row in a['assignments']:
        check(set(row)=={'assignment_id','actor_id','owner_ref','responsibility_ref','freshness_refs','classification','knowledge'},'assignment fields differ; no duplicate editable current state')
        actor=ASSIGNMENTS[row['assignment_id'].removeprefix('assignment:')]
        check(row['actor_id']==row['owner_ref']==actor,'assignment actor/owner mismatch')
        ref(actor,{'characters','creatures'});evidence(root,row['responsibility_ref']);owner(actor,row['responsibility_ref']['source_ref'])
        check(row['freshness_refs']==[row['responsibility_ref']['source_ref'],'state/checkpoint.json','entities/mechanics/outstanding-projects.md'],'freshness/precedence links differ')
        for path in row['freshness_refs']:source(root,path)
        check(row['classification']=='CONFIRMED CANON' and row['knowledge']=='requires-discovery-review','assignment knowledge/classification differs')
    rows(a['construct_contexts'],'context_id',{'construct:raze','construct:aegis'})
    for row in a['construct_contexts']:
        check(set(row)=={'context_id','source_ref','quote'},'construct reference fields differ')
        check(row['source_ref']=='entities/mechanics/theron-abilities.md','construct ability authority differs')
        evidence(root,{k:row[k] for k in ('source_ref','quote')})
    check(a['support_refs']==['entities/locations/ashvale-lodge.md','entities/factions/dragon-slayer-academy.md','entities/items/guardian-links.md','entities/mechanics/guild-animal-registry.md'],'assignment support authorities differ')
    for path in a['support_refs']:source(root,path)
    f=get('faction-activity');shape(f,'schema_version factions owner_field_contract activity_kinds new_activity new_memberships new_legal_powers automatic_activity')
    rows(f['factions'],'faction_id',FACTIONS)
    check(f['owner_field_contract']==FACTION_FIELDS and f['activity_kinds']==['confirmed','historical','alleged','proposed','unknown-current'],'faction field/claim vocabulary differs')
    check(f['new_activity']==[] and f['new_memberships']==[] and f['new_legal_powers']==[] and f['automatic_activity'] is False,'no faction operations/membership/powers created')
    for row in f['factions']:
        check(set(row)=={'faction_id','source_ref','classification','knowledge'},'faction fields differ; no hidden activity in directory')
        ref(row['faction_id'],{'factions'});owner(row['faction_id'],row['source_ref'])
        check(row['knowledge']=='requires-discovery-review','faction knowledge requires discovery review')
        check(row['classification']==('PROPOSED' if row['faction_id']=='continental-guild-concord' else 'CONFIRMED CANON'),'faction classification differs')
    w=get('world-event-references');shape(w,'schema_version chronicles event_fields new_events automatic_events')
    check(w['event_fields']==EVENT_FIELDS and w['new_events']==[] and w['automatic_events'] is False,'maintenance cannot create historical events')
    rows(w['chronicles'],'reference_id',{'chronicle:'+x for x in CHRONICLES})
    paths=[]
    for row in w['chronicles']:
        check(set(row)=={'reference_id','source_ref','classification','knowledge'},'chronicle fields differ')
        expected='changes/chronicles/'+row['reference_id'].removeprefix('chronicle:')+'.md'
        check(row['source_ref']==expected and row['classification']=='CONFIRMED CANON' and row['knowledge']=='requires-discovery-review','chronicle owner/knowledge differs')
        source(root,row['source_ref']);paths.append(row['source_ref'])
    check(len(paths)==len(set(paths)),'duplicate historical event source')
    p=get('world-development-proposals');shape(p,'schema_version classification approval_status workflow_states event_categories clock_categories clock_fields relationship_domains relationship_fields clocks relationship_changes automatic_advancement')
    check(records['world-development-proposals']['status']=='research' and p['classification']=='PROPOSED' and p['approval_status']=='REQUIRES APPROVAL','world proposals require approval')
    check(p['workflow_states']==WORKFLOW and p['event_categories']==EVENT_CATEGORIES and p['clock_categories']==CLOCK_CATEGORIES and p['clock_fields']==CLOCK_FIELDS and p['relationship_domains']==RELATIONSHIP_DOMAINS and p['relationship_fields']==RELATIONSHIP_FIELDS,'proposal vocabulary/contract differs')
    check(p['clocks']==[] and p['relationship_changes']==[] and p['automatic_advancement'] is False,'no clock, reputation or bond advancement')
    rule=get('npc-autonomy-and-time');shape(rule,'schema_version assignment_owner_ref faction_owner_ref event_owner_ref proposal_owner_ref communication_owner_refs resource_owner_refs road_owner_ref communication_states new_communications new_time_advances new_abilities new_relationships new_resource_postings automatic_writes')
    for key,ident in [('assignment_owner_ref','independent-assignments'),('faction_owner_ref','faction-activity'),('event_owner_ref','world-event-references'),('proposal_owner_ref','world-development-proposals'),('road_owner_ref','travel-routes')]:
        check(rule[key]==ident,'workflow authority mismatch');ref(ident,{'mechanics'})
    check(rule['communication_owner_refs']==['guardian-links','first-hours-accord'] and rule['resource_owner_refs']==['party-finances','theron-abilities','payroll-construction-and-trade'],'communication/resource owners differ')
    for ident in rule['communication_owner_refs']:ref(ident,{'items'})
    for ident in rule['resource_owner_refs']:ref(ident,{'mechanics','rules'})
    check(rule['communication_states']==['proposed','sent','delivered','acknowledged','accepted','reported','closed'],'communication states differ')
    check(rule['automatic_writes'] is False and all(rule[x]==[] for x in ('new_communications','new_time_advances','new_abilities','new_relationships','new_resource_postings')),'no communication/time/ability/relationship/resource events in maintenance')
