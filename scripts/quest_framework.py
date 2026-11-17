"""Read-only quest routing, finite proposal graph and blank-answer validation."""
import argparse
import json
from pathlib import Path
import re

HELPERS={'main-quest-map','quest-history-and-identities','quest-evidence-and-mysteries','quest-resolution-proposals','quest-answer-blueprint','quest-continuation-and-completion'}
CORE={'command-chain','v9-harm','fifth-bell','counterfeit-authority','surviving-opposition','witness-choice','immediate-consequences'}
MYSTERIES={'fb5':'fifth-bell-threat','northern-index':'seven-bells-investigation','er7-safety':'seven-bells-investigation','witness-authority':'artificial-witness','surviving-crown':'first-oath-conspiracy','v9-transferred':'v9-memories','v9-other-cases':'v9-memories','dene':'first-oath-conspiracy','thane-review':'first-oath-conspiracy','sorn-review':'first-oath-conspiracy','remaining-notices':'first-oath-conspiracy','a07-consent':'a07-signature','correspondent':'seven-bells-investigation','watcher':'seven-bells-investigation','freight-director':'freight-ward-conspiracy','acting-receiver':'seven-bells-investigation','damaged-channels':'first-hour-restoration','v9-controller':'v9-memories'}
MYSTERY_OBJECTIVES={'fb5':['fifth-bell'],'northern-index':['counterfeit-authority'],'er7-safety':['counterfeit-authority'],'witness-authority':['counterfeit-authority','witness-choice'],'surviving-crown':['command-chain','surviving-opposition'],'v9-transferred':['v9-harm'],'v9-other-cases':['v9-harm'],'dene':['surviving-opposition'],'thane-review':[],'sorn-review':[],'remaining-notices':[],'a07-consent':[],'correspondent':[],'watcher':[],'freight-director':[],'acting-receiver':['surviving-opposition'],'damaged-channels':[],'v9-controller':['command-chain']}

PEOPLE={'severin-valcrest','maelor-thane','edrick-sorn','halric-dene','varian-morthal','corvin-dareth','selvar-renn','damaris-keld','oren-veyl','aldric-voss','elian-voss','malrec','corven','corven-north-return-house','corvin-hale','corvin-halbrecht','rellan-sorn'}
RESOLUTIONS={'lyanna-vessels','lyanna-restoration','first-hour','original-protections','crown07-identity','fifth-activation','no-fifth-toll','av07-authority','thane-surrender','sorn-field-command','sorn-command-relinquished','ss41-specific','empty-seat-channel'}
CLUES={'third-leaf','leaf-transcription','er7','viir','counterfeit-plate','blue-case','wa17','witness-registers','v9-registers','ss41-chain','limited-probe','freight-records','a07','resonance','damaged-signature','anonymous-letter','watcher-map'}
CLUE_TYPES={'third-leaf':'physical-evidence','leaf-transcription':'historical-record','er7':'physical-evidence','viir':'physical-evidence','counterfeit-plate':'physical-evidence','blue-case':'physical-evidence','wa17':'physical-evidence','witness-registers':'authenticated-document','v9-registers':'historical-record','ss41-chain':'historical-record','limited-probe':'limited-mental-probe','freight-records':'authenticated-document','a07':'unverified-allegation','resonance':'theory','damaged-signature':'historical-record','anonymous-letter':'historical-record','watcher-map':'historical-record'}
CLUE_OWNERS={**{x:'seven-bells-inventory' for x in ('third-leaf','leaf-transcription','er7','viir','counterfeit-plate','blue-case','wa17')},'witness-registers':'first-hour-restoration','v9-registers':'first-oath-conspiracy','ss41-chain':'first-oath-conspiracy','limited-probe':'seven-bells-investigation','freight-records':'freight-ward-conspiracy','a07':'a07-signature','resonance':'first-oath-conspiracy','damaged-signature':'seven-bells-investigation','anonymous-letter':'seven-bells-investigation','watcher-map':'seven-bells-investigation'}
RESOLUTION_OWNERS={'lyanna-vessels':'v9-memories','lyanna-restoration':'v9-memories','first-hour':'first-hour-restoration','original-protections':'first-hour-restoration','crown07-identity':'severin-valcrest','fifth-activation':'fifth-bell-threat','no-fifth-toll':'fifth-bell','av07-authority':'maelor-thane','thane-surrender':'maelor-thane','sorn-field-command':'edrick-sorn','sorn-command-relinquished':'edrick-sorn','ss41-specific':'first-oath-conspiracy','empty-seat-channel':'artificial-witness'}

RESOLUTION_LIMITS={'lyanna-vessels': 'Recovery objective complete; three vessels are not three people.', 'lyanna-restoration': 'Restoration complete; other V-9 cases remain distinct.', 'first-hour': 'Specific objective complete; damaged other channels remain open.', 'original-protections': 'Protective systems preserved, not universally corrupted or destroyed.', 'crown07-identity': 'Known identification/capture; exact current custody not supplied.', 'fifth-activation': 'Encounter prevention succeeded; broader permanent threat resolution remains open.', 'no-fifth-toll': 'Checkpoint observation, not a promise about future play.', 'av07-authority': 'Established authority, not a newly inferred universal controller.', 'thane-surrender': 'Surrender is established; no conviction or prison destination inferred.', 'sorn-field-command': 'Established field responsibility; separate from other similarly named figures.', 'sorn-command-relinquished': 'Command relinquishment established; military disposition remains pending.', 'ss41-specific': 'Only the specified registry/instruction changed; no blanket notice cancellation.', 'empty-seat-channel': 'Resolved old channel; later counterfeit branches do not negate it.'}

CHAPTERS=[('gray-ledger','The Gray Ledger',3),('last-v9-cases','The Last V-9 Cases',3),('surviving-conspiracy','The Surviving Conspiracy',3),('fifth-bell','The Fifth Bell',3),('judgment','Judgment of the Witness',2)]
ANSWER_FIELDS=['definitive_answer','causal_explanation','responsible_actor_or_institution','motive','method','timeline','physical_location','supporting_evidence','discovery_opportunities','possible_contradictions','consequences']
OUTCOMES=['active','objective-completed','main-quest-completed','failed','abandoned','deferred','partially-resolved','consequences-pending','outcome-unknown']
OPTIONAL=['estate-expansion','academy','companion-training','magic-research','dungeon-exploration','optional-bounties','independent-legal-proceedings','guild-progression','family-relationships','property-management','unrelated-faction-disputes']
CLUE_FIELDS=['clue_id','source_record','found_location','discovery_event','evidence_type','custody','proves','does_not_prove','question_id','theron_discovery','companion_discovery','gm_boundary','reliability','next_supported_lead']
EVIDENCE_TYPES=['authenticated-document','physical-evidence','witness-testimony','confession','limited-mental-probe','historical-record','theory','deliberate-misinformation','unverified-allegation']
SYSTEMS=['travel-routes','settlement-services','justice-and-jurisdiction','prisoner-custody','guild-network','contract-registry','dungeon-registry','theron-abilities','party-finances','independent-assignments','npc-autonomy-and-time','world-event-references']


def check(condition,message):
    if not condition:raise ValueError('quest framework: '+message)


def strings(values,label):
    check(isinstance(values,list) and all(isinstance(x,str) and bool(x.strip()) for x in values),f'invalid {label}')
    check(len(values)==len(set(values)),f'duplicate {label}')


def text(value,label):check(isinstance(value,str) and bool(value.strip()),f'invalid {label}')


def payload(path,unique_json=None):
    blocks=re.findall(r'^```json\n(.*?)\n```$',path.read_text(),re.M|re.S)
    check(len(blocks)==1,'one JSON block required')
    return json.loads(blocks[0],object_pairs_hook=unique_json)


def validate_graph(nodes,edges,entry=None,ending=None):
    """Finite DAG; optional entry/ending additionally require all nodes reachable."""
    strings(nodes,'graph nodes');check(isinstance(edges,dict) and set(edges)==set(nodes),'graph coverage differs')
    for node,targets in edges.items():
        strings(targets,'graph edges');check(set(targets)<=set(nodes),'unreachable/unknown graph target')
    visiting,done=set(),set()
    def visit(node):
        check(node not in visiting,'mandatory investigation/dependency cycle')
        if node in done:return
        visiting.add(node)
        for target in edges[node]:visit(target)
        visiting.remove(node);done.add(node)
    for node in nodes:visit(node)
    if entry is None and ending is None:return
    check(entry in nodes and ending in nodes,'invalid chapter entry/ending')
    def reach(start):
        seen=set();todo=[start]
        while todo:
            node=todo.pop()
            if node not in seen:seen.add(node);todo.extend(edges[node])
        return seen
    check(reach(entry)==set(nodes),'unreachable required chapter transition')
    check(not edges[ending] and all(ending in reach(x) for x in nodes),'chapter cannot reach finite ending')


def readiness_report(root):
    """Only non-spoiler pending IDs/counts; caller validates before presentation."""
    p=payload(root/'entities/mechanics/quest-answer-blueprint.md')
    plan=payload(root/'entities/mechanics/quest-resolution-proposals.md')
    pending=[x['mystery_id'] for x in p['pending_answers'] if x['approval_status']=='REQUIRES APPROVAL']
    return {'classification':'PROPOSED','play_activation':'BLOCKED PENDING ANSWER APPROVAL',
            'missing_answer_approvals':pending,'core_design_approval_ids':[x for x in pending if MYSTERY_OBJECTIVES[x.removeprefix('mystery:')]],
            'optional_design_approval_ids':[x for x in pending if not MYSTERY_OBJECTIVES[x.removeprefix('mystery:')]],'unfilled_clue_route_ids':[x['route_id'] for x in plan['clue_route_slots']],
            'secret_storage':'PRIVATE STORAGE NOT ESTABLISHED','baseline_valid':True,
            'note':'Missing prospective approvals are nonfatal planning blockers; optional questions are not ending prerequisites. No answer or route is invented.'}


def validate_quest_framework(root,records,require,repository_file,unique_json):
    if not HELPERS.intersection(records):return None
    require(HELPERS<=records.keys(),'quest framework: incomplete extension')
    def get(ident):return payload(root/f"entities/{records[ident]['type']}/{ident}.md",unique_json)
    def shape(d,fields):
        check(isinstance(d,dict) and set(d)==set(fields.split()),'unexpected fields')
        check(type(d['schema_version']) is int and d['schema_version']==1,'invalid schema')
    def ref(ident,kinds):
        check(isinstance(ident,str) and ident in records and records[ident]['type'] in kinds,'invalid owner reference')
        check(records[ident]['visibility']=='gm-reference','secret owner excluded from public directory')
    def source(path):
        p=repository_file(root,path,'quest source')
        if path.startswith('entities/'):ref(Path(path).stem,{'characters','creatures','quests','items','locations','factions','mechanics','rules'})
        return p
    def owner(ident,path):
        ref(ident,{'characters','creatures','quests','items','locations','factions','mechanics','rules'})
        check(path==f"entities/{records[ident]['type']}/{ident}.md",'owner/source mismatch');source(path)
    def locator(value):
        check(isinstance(value,dict) and set(value)=={'source_ref','quote'},'invalid evidence locator')
        text(value['quote'],'evidence quote');check(value['quote'] in source(value['source_ref']).read_text(),'source quote missing')
    def rows(values,key,expected):
        check(isinstance(values,list) and all(isinstance(x,dict) and isinstance(x.get(key),str) for x in values),'invalid routing rows')
        ids=[x[key] for x in values];strings(ids,key);check(set(ids)==set(expected),'routing coverage differs')
    def knowledge(row):check(row['knowledge']=='requires-discovery-review','index/source access is not player knowledge')
    a=get('main-quest-map');shape(a,'schema_version central_quest_id quest_owners mystery_owner_ref history_identity_owner_ref proposal_owner_ref answer_owner_ref procedure_owner_ref new_quest_statuses new_rewards automatic_progress')
    check(a['central_quest_id']=='first-oath-conspiracy','central owner differs')
    expected={x for x in records if records[x]['type']=='quests' and records[x]['visibility']=='gm-reference'}
    rows(a['quest_owners'],'quest_id',expected)
    for row in a['quest_owners']:
        check(set(row)=={'quest_id','source_ref','knowledge'},'quest routing owns no editable status');ref(row['quest_id'],{'quests'});owner(row['quest_id'],row['source_ref']);knowledge(row)
    for key,ident in [('mystery_owner_ref','quest-evidence-and-mysteries'),('history_identity_owner_ref','quest-history-and-identities'),('proposal_owner_ref','quest-resolution-proposals'),('answer_owner_ref','quest-answer-blueprint'),('procedure_owner_ref','quest-continuation-and-completion')]:
        check(a[key]==ident,'competing quest authority');ref(ident,{'mechanics','rules'})
    check(a['new_quest_statuses']==[] and a['new_rewards']==[] and a['automatic_progress'] is False,'no automatic quest progress/rewards')
    h=get('quest-history-and-identities');shape(h,'schema_version historical_objectives distinct_people identity_mergers new_custody_events new_historical_outcomes')
    rows(h['historical_objectives'],'resolution_id',{'resolution:'+x for x in RESOLUTIONS})
    for row in h['historical_objectives']:
        check(set(row)=={'resolution_id','owner_ref','evidence_ref','classification','scope_limit','knowledge'},'historical objective fields differ')
        check(row['owner_ref']==RESOLUTION_OWNERS[row['resolution_id'].removeprefix('resolution:')],'historical objective owner differs')
        check(row['scope_limit']==RESOLUTION_LIMITS[row['resolution_id'].removeprefix('resolution:')],'historical victory scope cannot be expanded/reopened')
        locator(row['evidence_ref']);owner(row['owner_ref'],row['evidence_ref']['source_ref']);text(row['scope_limit'],'objective limit')
        check(row['classification']=='CONFIRMED CANON','historical achievement cannot be reopened/proposed');knowledge(row)
    rows(h['distinct_people'],'character_id',PEOPLE)
    for row in h['distinct_people']:
        check(set(row)=={'character_id','source_ref','knowledge'},'identity fields differ; no aliases/guilt inferred')
        ref(row['character_id'],{'characters'});owner(row['character_id'],row['source_ref']);knowledge(row)
    check(h['identity_mergers']==[] and h['new_custody_events']==[] and h['new_historical_outcomes']==[],'no identity merger, custody transfer or new history')
    e=get('quest-evidence-and-mysteries');shape(e,'schema_version clues mysteries clue_field_contract evidence_types new_evidence_items new_discoveries new_resolutions')
    check(e['clue_field_contract']==CLUE_FIELDS and e['evidence_types']==EVIDENCE_TYPES,'evidence contract differs')
    check(e['new_evidence_items']==[] and e['new_discoveries']==[] and e['new_resolutions']==[],'no duplicate items/discoveries/resolutions')
    rows(e['clues'],'clue_id',{'clue:'+x for x in CLUES});locators=[]
    for row in e['clues']:
        check(set(row)=={'clue_id','owner_ref','source_locator','evidence_type','custody_owner_ref','discovery_owner_ref','knowledge','new_item'},'clue fields differ')
        check(row['owner_ref']==CLUE_OWNERS[row['clue_id'].removeprefix('clue:')],'clue governing owner differs')
        locator(row['source_locator']);owner(row['owner_ref'],row['source_locator']['source_ref']);knowledge(row)
        check(row['custody_owner_ref']==row['owner_ref'] and row['new_item'] is False,'clue is not new possession or transfer')
        ref(row['discovery_owner_ref'],{'quests'});check(row['evidence_type']==CLUE_TYPES[row['clue_id'].removeprefix('clue:')],'unsupported evidence authentication/type')
        locators.append((row['source_locator']['source_ref'],row['source_locator']['quote']))
    check(len(locators)==len(set(locators)),'duplicate evidence scope; not another physical item')
    mids={'mystery:'+x for x in MYSTERIES};rows(e['mysteries'],'mystery_id',mids)
    oids={'objective:'+x for x in CORE}
    for row in e['mysteries']:
        check(set(row)=={'mystery_id','quest_owner_id','question','confirmed_refs','alleged_refs','disproven_refs','unknown_answer','clue_ids','last_status_owner_ref','freshness_refs','knowledge','next_action_key','proposed_objective_ids','main_ending_role','answer_approval','classification'},'mystery fields differ')
        expected_owner=MYSTERIES[row['mystery_id'].removeprefix('mystery:')]
        check(row['quest_owner_id']==row['last_status_owner_ref']==expected_owner,'mystery governing quest differs')
        ref(expected_owner,{'quests'});path=f'entities/quests/{expected_owner}.md'
        check(row['confirmed_refs']==[path] and row['alleged_refs']==[] and row['disproven_refs']==[],'do not promote unindexed allegations/refutations')
        check(row['freshness_refs']==[path,'state/checkpoint.json','state/open-verifications.md'],'missing freshness/precedence sources')
        for p in row['freshness_refs']:source(p)
        text(row['question'],'question');text(row['next_action_key'],'next action');knowledge(row)
        strings(row['clue_ids'],'clue links');check(bool(row['clue_ids']) and set(row['clue_ids'])<={'clue:'+x for x in CLUES},'invalid clue reference')
        strings(row['proposed_objective_ids'],'objective links');check(set(row['proposed_objective_ids'])<=oids,'invalid proposed objective')
        check(row['proposed_objective_ids']==['objective:'+x for x in MYSTERY_OBJECTIVES[row['mystery_id'].removeprefix('mystery:')]],'optional question cannot silently become mandatory')
        check(row['main_ending_role']==('PROPOSED CORE' if row['proposed_objective_ids'] else 'OPTIONAL OR CONSEQUENCE'),'main/optional classification differs')
        check(row['classification']=='CONFIRMED CANON' and row['answer_approval']=='REQUIRES APPROVAL' and row['unknown_answer'] is None,'no invented mystery answer or closed question')
    plan=get('quest-resolution-proposals');shape(plan,'schema_version classification approval_status entry_chapter_id ending_chapter_id chapters objectives clue_route_slots outcome_labels optional_domains new_scene_outcomes new_quest_completions automatic_rewards')
    check(records['quest-resolution-proposals']['status']=='research' and plan['classification']=='PROPOSED' and plan['approval_status']=='REQUIRES APPROVAL','chapter design is not canon')
    chapterids={'chapter:'+x[0] for x in CHAPTERS};rows(plan['chapters'],'chapter_id',chapterids);rows(plan['objectives'],'objective_id',oids)
    chapter_by={x['chapter_id']:x for x in plan['chapters']};assigned=[]
    for slug,title,count in CHAPTERS:
        row=chapter_by['chapter:'+slug]
        check(set(row)=={'chapter_id','title','target_scenes','objective_ids','mystery_ids','next_ids','classification','activation','mandatory_repeat','can_combine_or_reorder'},'chapter fields differ')
        check(row['title']==title and type(row['target_scenes']) is int and row['target_scenes']==count,'five-chapter/14-scene target differs')
        strings(row['objective_ids'],'chapter objectives');check(bool(row['objective_ids']) and set(row['objective_ids'])<=oids,'chapter objective reference differs');assigned+=row['objective_ids']
        strings(row['mystery_ids'],'chapter mysteries');check(set(row['mystery_ids'])<=mids,'chapter mystery reference differs')
        check(row['classification']=='PROPOSED' and row['activation']=='BLOCKED PENDING ANSWER APPROVAL' and row['mandatory_repeat'] is False and row['can_combine_or_reorder'] is True,'no active scenes or repeated mandatory loops')
    check(set(assigned)==oids and len(assigned)==len(oids),'essential objective chapter coverage/duplication differs')
    check(plan['entry_chapter_id']=='chapter:gray-ledger' and plan['ending_chapter_id']=='chapter:judgment','entry/ending differs')
    validate_graph(list(chapterids),{x['chapter_id']:x['next_ids'] for x in plan['chapters']},plan['entry_chapter_id'],plan['ending_chapter_id'])
    for row in plan['objectives']:
        check(set(row)=={'objective_id','target','depends_on','required_for_ending','classification'},'objective fields differ')
        text(row['target'],'objective target');check(row['required_for_ending'] is True and row['classification']=='PROPOSED','required scope is proposed only')
    validate_graph(list(oids),{x['objective_id']:x['depends_on'] for x in plan['objectives']})
    routeids={f'clue-route:{slug}:{n}' for slug in CORE for n in (1,2)};rows(plan['clue_route_slots'],'route_id',routeids)
    for row in plan['clue_route_slots']:
        check(set(row)=={'route_id','objective_id','answer_ref','method','location_id','discovery_ref','activation'},'clue-route fields differ')
        check(row['objective_id']=='objective:'+row['route_id'].split(':')[1],'clue route/objective mismatch')
        check(all(row[k] is None for k in ('answer_ref','method','location_id','discovery_ref')) and row['activation']=='BLOCKED PENDING ANSWER APPROVAL','unapproved answer cannot activate a route/location')
    check(plan['outcome_labels']==OUTCOMES and plan['optional_domains']==OPTIONAL,'outcome/side-quest domain contract differs')
    check(plan['new_scene_outcomes']==[] and plan['new_quest_completions']==[] and plan['automatic_rewards'] is False,'no scene outcome, quest completion or reward')
    b=get('quest-answer-blueprint');shape(b,'schema_version classification storage_status answer_fields resolved_refs pending_answers public_secret_values_allowed new_fixed_answers')
    check(records['quest-answer-blueprint']['status']=='research' and b['classification']=='PROPOSED' and b['storage_status']=='PRIVATE STORAGE NOT ESTABLISHED','secret answers require private storage/approval')
    check(b['answer_fields']==ANSWER_FIELDS,'answer schema differs');strings(b['resolved_refs'],'resolved approval references')
    check(set(b['resolved_refs'])=={'resolution:'+x for x in RESOLUTIONS},'historical resolution approval crosswalk differs')
    rows(b['pending_answers'],'mystery_id',mids)
    for row in b['pending_answers']:
        check(set(row)=={'mystery_id','approval_status','approval_ref','private_storage_ref','values'},'no disguised answer metadata')
        check(row['approval_status']=='REQUIRES APPROVAL' and row['approval_ref'] is None and row['private_storage_ref'] is None,'no unsourced answer approval/private-storage claim')
        check(isinstance(row['values'],dict) and set(row['values'])==set(ANSWER_FIELDS) and all(x is None for x in row['values'].values()),'no unrevealed fixed answers in public storage')
    check(b['public_secret_values_allowed'] is False and b['new_fixed_answers']==[],'secret-answer publication forbidden')
    rule=get('quest-continuation-and-completion');shape(rule,'schema_version map_ref evidence_ref history_ref proposal_ref answer_ref system_owner_refs new_status_changes new_rewards new_world_events new_custody_transfers new_knowledge_disclosures automatic_completion')
    for key,ident in [('map_ref','main-quest-map'),('evidence_ref','quest-evidence-and-mysteries'),('history_ref','quest-history-and-identities'),('proposal_ref','quest-resolution-proposals'),('answer_ref','quest-answer-blueprint')]:check(rule[key]==ident,'procedure authority mismatch')
    check(rule['system_owner_refs']==SYSTEMS,'resource/legal/autonomy integration owners differ')
    for ident in rule['system_owner_refs']:ref(ident,{'mechanics','rules'})
    check(rule['automatic_completion'] is False and all(rule[k]==[] for k in ('new_status_changes','new_rewards','new_world_events','new_custody_transfers','new_knowledge_disclosures')),'no automatic consequences or disclosures')
    return readiness_report(root)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--readiness',action='store_true',required=True);args=parser.parse_args()
    if __package__:from .validate import validate
    else:from validate import validate
    try:
        validate(args.root);print(json.dumps(readiness_report(args.root),indent=2))
    except (ValueError,OSError) as exc:parser.exit(1,f'ERROR: {exc}\n')


if __name__=='__main__':main()
