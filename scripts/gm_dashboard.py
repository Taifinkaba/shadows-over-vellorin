"""Read-only, reviewed-field world projection and GM continuity validation.

No raw source renderer, event writer, cache, scheduler or automatic gameplay API.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import sys

DIRECTORIES=['docs/geography-and-travel.md','docs/settlement-directory.md','docs/justice-and-custody-directory.md','docs/guild-and-contract-directory.md','docs/dungeon-and-exploration-directory.md','docs/property-and-economy-directory.md','docs/npc-autonomy-and-world-events.md','docs/faction-activity-directory.md','docs/main-quest-directory.md']
DOCUMENTS=['docs/game-master-operating-manual.md','docs/world-status.md','docs/end-session-codex-template.md','docs/next-session-chat-template.md']
AUTHORITIES=['story-mode','knowledge-boundaries','theron-abilities','theron-skills','theron-spells','travel-routes','settlement-services','justice-and-jurisdiction','prisoner-custody','guild-network','contract-registry','dungeon-registry','exploration-sections','party-finances','property-financial-references','independent-assignments','faction-activity','world-event-references','main-quest-map','quest-history-and-identities','quest-resolution-proposals','quest-answer-blueprint']
SCENARIOS={'opening-scene':['checkpoint','location-owner','present-actors'],'combat':['participants','theron-abilities','theron-spells','equipment-owner'],'travel':['travel-routes','route-owners','destination-owner'],'shopping':['settlement-services','business-parent','party-finances'],'bounty':['contract-registry','justice-and-jurisdiction','prisoner-custody'],'dungeon':['dungeon-registry','section-owner','creature-owner','inventory-owner'],'estate':['tomas','ashvale-estate','finance-ledger'],'academy':['master-beren','dragon-slayer-academy','independent-assignments'],'main-quest':['active-quest-owner','evidence-owner','discovery-source'],'end-session':['changed-owners','checkpoint','finance-ledger','chronicle']}
HANDOFF={'session_identification':['date','time','location','session_status','last_scene','last_player_decision'],'character_resources':['hp','mp','defense_base','defense_equipped','conditional_defense','equipped_items','staff_resources','wagon_resources','conditions','skill_progress'],'companions':['present','elsewhere','assignments','safety','last_verified_updates'],'finances':['opening_balance','verified_income','verified_spending','internal_transfers','closing_balance','committed_funds','excluded_holdings','unresolved_discrepancies'],'inventory':['new_acquisitions','consumed_items','transfers','protected_evidence','provisional_salvage'],'world_changes':['quests','factions','relationships','custody','dungeon_states','property','construction','research','legal_outcomes'],'open_issues':['mysteries','pending_responses','deferred_work','historical_discrepancies','approval_requirements'],'codex_instructions':['affected_entity_ids','affected_files','source_evidence','checkpoint_changes','required_validation','explicitly_unchanged_systems','discovery_boundaries']}
RETRIEVAL_ORDER=['precedence-and-narration','latest-approved-checkpoint','requested-activity','relevant-owner-lookup','targeted-provenance','presence-and-autonomy','finite-resources','quest-and-discovery-boundaries','player-decision','end-session-handoff']
COMPETING=['state/world-state.json','state/dashboard.json','state/dashboard-state.json','state/world-status.json']


def check(condition,message):
    if not condition:raise ValueError('GM continuity: '+message)


def payload(path,unique_json=None):
    blocks=re.findall(r'^```json\n(.*?)\n```$',path.read_text(),re.M|re.S)
    check(len(blocks)==1,'one JSON template block required')
    return json.loads(blocks[0],object_pairs_hook=unique_json)


def validate_document_links(root,relative):
    """Check local links in new workflow docs only, without recursive ingestion."""
    path=root/relative
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',path.read_text()):
        target=target.strip('<>').split('#',1)[0]
        if not target:continue
        check('://' not in target and not target.startswith('/'),'workflow link must be repository-relative')
        resolved=(path.parent/target).resolve()
        check(resolved.is_relative_to(root.resolve()) and resolved.is_file(),'broken or escaping workflow document link')


def validate_gm_continuity(root,records,require,repository_file,unique_json):
    if 'gm-workflow' not in records:
        check(not any((root/path).exists() for path in DOCUMENTS),'incomplete GM workflow extension')
        return
    def ref(ident):
        check(ident in records and records[ident]['visibility']=='gm-reference','missing/secret workflow authority')
        return repository_file(root,f"entities/{records[ident]['type']}/{ident}.md",'workflow owner')
    d=payload(ref('gm-workflow'),unique_json)
    check(set(d)=={'schema_version','directory_refs','document_refs','authority_refs','retrieval_scenarios','dashboard_policy','checkpoint_ref','finance_ref','new_session_events','new_resource_postings','new_knowledge_disclosures','automatic_writes'},'unexpected workflow fields; no cached world state')
    check(type(d['schema_version']) is int and d['schema_version']==1,'unsupported workflow schema')
    check(d['directory_refs']==DIRECTORIES and d['document_refs']==DOCUMENTS and d['authority_refs']==AUTHORITIES,'workflow source coverage differs')
    check(d['retrieval_scenarios']==SCENARIOS,'retrieval-first scenario ownership differs')
    check(d['checkpoint_ref']=='state/checkpoint.json' and d['finance_ref']=='state/finance-ledger.json','competing checkpoint/ledger')
    check(d['dashboard_policy']=='REVIEWED FIELDS ONLY','no broad source or GM-secret rendering')
    check(d['automatic_writes'] is False and all(d[x]==[] for x in ('new_session_events','new_resource_postings','new_knowledge_disclosures')),'maintenance cannot play/post/disclose')
    for ident in AUTHORITIES:ref(ident)
    for path in DIRECTORIES+DOCUMENTS:repository_file(root,path,'workflow document')
    for path in DOCUMENTS:validate_document_links(root,path)
    for path in COMPETING:check(not (root/path).exists(),'competing editable world-state/cache forbidden')
    h=payload(root/'docs/end-session-codex-template.md',unique_json)
    check(set(h)=={'schema_version','template_only','stop_story','merge_requires_approval','apply_only_supported_outcomes','handoff','source_refs','verified_as_of'},'END SESSION template fields differ')
    check(type(h['schema_version']) is int and h['schema_version']==1 and all(h[x] is True for x in ('template_only','stop_story','merge_requires_approval','apply_only_supported_outcomes')),'END SESSION must stop play and require supported outcomes/merge approval')
    check(isinstance(h['handoff'],dict) and set(h['handoff'])==set(HANDOFF),'incomplete END SESSION groups')
    for group,fields in HANDOFF.items():
        check(isinstance(h['handoff'][group],dict) and set(h['handoff'][group])==set(fields),'incomplete END SESSION requirements')
        check(all(v is None for v in h['handoff'][group].values()),'template cannot contain an actual checkpoint or hidden answer')
    check(h['source_refs']==[] and h['verified_as_of'] is None,'unfilled handoff is not an observed session')
    n=payload(root/'docs/next-session-chat-template.md',unique_json)
    check(set(n)=={'schema_version','template_only','repository','checkpoint_ref','handoff_ref','retrieval_order','hardcoded_checkpoint','automatic_actions','stop_on_end_session','merge_requires_approval'},'next-chat template fields differ')
    check(type(n['schema_version']) is int and n['schema_version']==1 and n['template_only'] is True,'invalid next-chat schema')
    check(n['repository']=='Taifinkaba/shadows-over-vellorin' and n['checkpoint_ref']=='state/checkpoint.json' and n['handoff_ref']=='state/next-chat-handoff.md','next-chat must retrieve current authority')
    check(n['retrieval_order']==RETRIEVAL_ORDER and n['hardcoded_checkpoint'] is None and n['automatic_actions'] is False and n['stop_on_end_session'] is True and n['merge_requires_approval'] is True,'next-chat cannot cache/act/continue past END SESSION')
    page=(root/'docs/world-status.md').read_text()
    check('usage guide' in page and '--check-view' in page,'dashboard guide must describe regeneration/freshness')
    # The guide is deliberately instructions, never a persisted numeric projection.
    check(not re.search(r'^```json\n',page,re.M),'no cached dashboard JSON in static guide')


def build_dashboard(root):
    """Validate then derive a restricted source-qualified projection, without writes."""
    if __package__:
        from .validate import validate,repository_file,require,frontmatter
        from .dungeons import read_section_state
        from .quest_framework import readiness_report
    else:
        from validate import validate,repository_file,require,frontmatter
        from dungeons import read_section_state
        from quest_framework import readiness_report
    validate(root)
    index=json.loads((root/'index.json').read_text());records={x['id']:x for x in index['entries']}
    used={'index.json'}
    def file(path):
        p=repository_file(root,path,'dashboard source');used.add(path)
        if path.startswith('entities/'):
            ident=Path(path).stem
            check(ident in records and records[ident]['visibility']=='gm-reference','secret source excluded')
            meta=frontmatter(p)
            check(meta['id']==ident and meta['visibility']=='gm-reference','source visibility/identity mismatch')
        return p
    def owner(ident):
        check(ident in records,'missing dashboard owner')
        file(records[ident]['path']);return records[ident]['path']
    def data(ident):return payload(file(owner(ident)))
    def value(item,source_ref,as_of=None,qualification='Reviewed field; source/discovery review still applies'):
        file(source_ref.split('#',1)[0])
        return {'value':item,'source_ref':source_ref,'as_of':as_of,'qualification':qualification}
    checkpoint='state/checkpoint.json';ledgerref='state/finance-ledger.json'
    c=json.loads(file(checkpoint).read_text());ledger=json.loads(file(ledgerref).read_text())
    check((c['schema_version'],ledger['schema_version']) in ((5,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9)),'dashboard requires checkpoint5/ledger2 or checkpoint6/ledger3–9')
    date=' '.join(filter(None, (c['date'], c['time'])));scene={}
    for field in ('date','calendar','time','location','status'):
        item = {k: c['calendar'][k] for k in ('year', 'season', 'day_of_season', 'annual_day', 'latest_numbered_day', 'part_of_day', 'historical_label')
                if k in c['calendar']} if field == 'calendar' else c[field]
        scene[field]=value(item,checkpoint+'#/'+field,date)
    present=c['context']['companions_present']
    for ident in present:owner(ident)
    scene['explicitly_present_ids']=value(present,checkpoint+'#/context/companions_present',date,'Only checkpoint-listed presence; no inferred recall')
    scene['last_verified_source']=value(c['source'],checkpoint+'#/source',date)
    year_end = ledger.get('endpoint', {}).get('classification') == 'PROVISIONAL PLAYED ENDPOINT'
    working_treasury = ledger.get('endpoint', {}).get('classification') == 'PLAYER-CORRECTED WORKING TREASURY'
    hero={}
    for field in ('hp','hp_max','mp','mp_max','defense'):
        hero[field]=value(c['theron'][field],checkpoint+'#/theron/'+field,date)
    if year_end or working_treasury:
        hero['mp']['as_of'] = None
        hero['mp']['qualification'] = 'Last tracked; current reading unverified'
    for field in ('equipped_defense','staff_mp','staff_mp_max','wagon_mp','wagon_mp_max','chronos_eye_locked','dragon_slayer_locked'):
        hero[field]=value(c['resources'][field],checkpoint+'#/resources/'+field,date)
    if 'refitted_wagon_mana' in c['resources']:
        hero['refitted_wagon_mana'] = value(c['resources']['refitted_wagon_mana'], checkpoint+'#/resources/refitted_wagon_mana', date, 'Independent reservoirs by vehicle ID')
    maskpath=owner('night-sovereign');mask=file(maskpath).read_text().split('## Historical record',1)[0]
    match=re.search(r'\+(\d+) equipped DEF while worn',mask)
    bonus=int(match[1]) if match else None
    hero['night_sovereign_worn_bonus']=value(bonus,maskpath,None,'Conditional worn bonus only; UNKNOWN if reviewed phrase unavailable')
    hero['defense_if_night_sovereign_worn']=value(c['resources']['equipped_defense']+bonus if bonus is not None else None,maskpath,None,'Derived from checkpoint equipped defense plus item worn bonus; not current equipped status')
    hero['night_sovereign_carried_not_equipped']=value(c['provenance']['current_equipment']['night_sovereign_carried_not_equipped'] if c['schema_version']==6 else True if 'carried, not equipped at final checkpoint' in mask else None,checkpoint+'#/provenance/current_equipment' if c['schema_version']==6 else maskpath,None,'Current observation UNKNOWN for adopted endpoint; Day156 carried/not-equipped remains historical only')
    hero['equipment_owner_refs']=value([owner(x) for x in ('frostguard-bracers','night-sovereign','sovereign-nexus','sovereign-expedition-wagon')],checkpoint,None,'Limited equipment retrieval, not exhaustive current inventory')
    hero['conditions_and_other_skills']=value(None,owner('theron-abilities'),None,'UNKNOWN / targeted retrieval required; mixed narrative is not rendered')
    cash=ledger['controlled_cash'];commit=ledger['commitments']
    later_endpoint = ledger['schema_version'] in (6,7,8,9)
    unpaid = commit['expansion_outstanding_cp'] if later_endpoint else (
        commit['expansion_committed_cp'] - commit['expansion_paid_cp'])
    finances={k:value(v,ledgerref+'#'+pointer,date,qualification) for k,v,pointer,qualification in [
        ('controlled_cp',cash['total_cp'],'/controlled_cash/total_cp','Player-corrected controlled working funds' if working_treasury else 'Provisional played close; reconciliation pending' if year_end else 'Controlled cash; source owner labels do not establish sole personal title'),
        ('committed_unpaid_cp',unpaid,'/commitments','Included in controlled cash until paid'),
        ('uncommitted_cp',commit['uncommitted_cp'],'/commitments/uncommitted_cp','Available under existing ownership/authority restrictions'),
        ('construction_started',commit['construction_started'],'/commitments/construction_started','Commitment is not construction') ]}
    finances['currency']=value({k:ledger['currency'][k] for k in ('unit','cp_per_gp','cp_per_sp')},ledgerref+'#/currency',date)
    for key in ('controlled_cp','committed_unpaid_cp','uncommitted_cp'):
        copper=finances[key]['value']
        finances[key.removesuffix('_cp')+'_display']=value(None if copper is None else f'{copper//100} gp {(copper%100)//10} sp {copper%10} cp',finances[key]['source_ref'],date,finances[key]['qualification'] if year_end and key == 'controlled_cp' else 'Integer-copper display:1gp=100cp,1sp=10cp')
    finances['accounts']=[{'account_id':value(x['id'],ledgerref+f'#/controlled_cash/accounts/{i}/id',date),'balance_cp':value(x['balance_cp'],ledgerref+f'#/controlled_cash/accounts/{i}/balance_cp',date),'ownership_review':value(None,ledgerref+f'#/controlled_cash/accounts/{i}/owner',None,'Read source legal/control qualification; no new personal-title claim')} for i,x in enumerate(cash['accounts'])]
    finances['excluded_holdings']=[{'holding_id':value(x['id'],ledgerref+f'#/excluded_property/{i}/id'),'amount_cp':value(x['amount_cp'],ledgerref+f'#/excluded_property/{i}/amount_cp',None,'Excluded; source may be historical, approximate or noncash; not a certified current third-party cash total')} for i,x in enumerate(ledger['excluded_property'])]
    if ledger['schema_version'] in (3,4,5,6,7,8,9):
        historyref=ledger['historical_day156_ref'];history=json.loads(file(historyref).read_text())
        finances['account_allocation_status']=value(cash['allocation_status'],ledgerref+'#/controlled_cash/allocation_status',date)
        finances['historical_day156_accounts']=value([{'id':a['id'],'balance_cp':a['balance_cp']} for a in history['controlled_cash']['accounts']],historyref+'#/controlled_cash/accounts',history['as_of']['date'],'Historical allocations only, not current account balances or funding authorization')
        if ledger['schema_version']==3:
            finances['unexplained_endpoint_difference_cp']=value(ledger['bridge']['difference_cp'],ledgerref+'#/bridge',None,'UNEXPLAINED ENDPOINT DIFFERENCE — PROVENANCE UNRESOLVED; not a transaction or account assignment')
            hero['unexplained_mp_endpoint_change']=value(c['provenance']['mp_bridge']['difference_mp'],checkpoint+'#/provenance/mp_bridge',None,'UNEXPLAINED ENDPOINT CHANGE — PROVENANCE UNRESOLVED; no recovery event')
        elif working_treasury:
            finances['working_funds_comparison_cp'] = value(
                ledger['bridge']['difference_cp'], ledgerref+'#/bridge', None,
                'Unitemized comparison of earlier provisional ordinary cash and later working funds')
        elif ledger['schema_version'] in (8,9):
            finances['year853_cash_bridge'] = value(ledger['bridge'], ledgerref+'#/bridge', date)
            hero['day28_recovery_readings'] = value(c['provenance']['year853_readings'],
                                                    checkpoint+'#/provenance/year853_readings',
                                                    'Year 853 Day 28')
        elif later_endpoint:
            finances['unexplained_endpoint_difference_cp'] = value(
                ledger['bridge']['difference_cp'], ledgerref+'#/bridge', None,
                'Unresolved difference before the recorded cash window without a transaction or account assignment')
        else:
            finances['reconciled_repair_expense_cp']=value(2600,ledgerref+'#/post_arc_transactions','Year 848 Day 165','Player-confirmed maintenance; already included in endpoint; no account allocation')
            finances['repair_payments']=value([{'id':t['id'],'date':t['date'],'amount_cp':t['amount_cp']} for t in ledger['post_arc_transactions']],ledgerref+'#/post_arc_transactions',None,'Two historical payments; times, recipients and accounts unknown')
            finances['cottage_repairs_completed']=value(True,'changes/chronicles/year848-day181-cottage-mana-reconciliation.md','Year 848 Day 165','House Ashvale ownership retained; unrelated expansion remains unpaid')
            hero['reconciled_mp_recovery']=value({'intervals':1,'minutes':10,'potential_mp':24,'actual_mp':22,'excess_mp':2,'cap':400,'date':None,'location':None},checkpoint+'#/provenance/mp_bridge',None,'Player-confirmed qualifying assimilation; exact date/location unknown')
        hero['endpoint_qualification']=value(c['provenance']['classification'],checkpoint+'#/provenance',date)
    finances['accounting_gaps']=value(None,'state/open-verifications.md',None,'Targeted source review required; no balancing entries or raw private gap text')
    assignments=data('independent-assignments');companions=[]
    for actor in assignments['actors']:
        ident=actor['actor_id'];p=owner(ident)
        handles=[x['assignment_id'] for x in assignments['assignments'] if x['actor_id']==ident]
        companions.append({'person':value(ident,p),'assignment':value(handles,owner('independent-assignments')),
            'status':value('checkpoint-listed-present' if ident in present else 'current whereabouts/progress UNKNOWN; retrieve dated owner',checkpoint if ident in present else p,date if ident in present else None),
            'last_verified_location':value(c['location'] if ident in present else None,checkpoint if ident in present else p,date if ident in present else None,'No current position inferred from role or historical assignment'),
            'source_date':value(date if ident in present else None,checkpoint if ident in present else p,None,'Unknown/not projected dates require targeted owner review')})
    estate=[]
    for row in data('property-financial-references')['properties']:
        p=owner(row['property_id'])
        estate.append({'property':value(row['property_id'],p),'manager_id':value(row['manager_id'],owner('property-financial-references'),None,'Management role is not current physical presence or legal title'),
            'legal_owner_id':value(row['legal_owner_id'],owner('property-financial-references')),
            'legal_owner_label':value(row['legal_owner_label'],owner('property-financial-references')),
            'operations_and_projects':value(None,p,None,'Read original facilities and outstanding-projects; no inferred completion'),
            'financial_ownership':value('independent; excluded from controlled cash' if row['property_id']=='dragon-slayer-academy' else 'premises/title distinct from merchant stock and managed accounts',ledgerref,None,'No cash, valuation or ownership transfer is generated')})
    quests={'metadata':[{'quest_id':value(x['quest_id'],owner(x['quest_id'])),'status':value(records[x['quest_id']]['status'],'index.json',None,'Metadata only; completed subobjectives may coexist with wider active work')} for x in data('main-quest-map')['quest_owners']],
        'completed_milestone_handles':value([x['resolution_id'] for x in data('quest-history-and-identities')['historical_objectives']],owner('quest-history-and-identities'),None,'Scoped source references; not new achievements'),
        'deferred_details':value(None,owner('open-quests'),None,'Targeted source/discovery review required')}
    ready=readiness_report(root)
    quests['approval_gaps']=value({k:len(ready[k]) for k in ('core_design_approval_ids','optional_design_approval_ids')},owner('quest-answer-blueprint'),None,'Proposed design blockers; optional questions are not ending prerequisites')
    quests['unfilled_clue_routes']=value(len(ready['unfilled_clue_route_ids']),owner('quest-resolution-proposals'),None,'Blank planning slots, not established roads or discovered clues')
    sections=[]
    for row in data('exploration-sections')['sections']:
        state=read_section_state(root,row['state_ref'],require,repository_file);p=row['state_ref']['source_ref']
        sections.append({'section_id':value(row['section_id'],owner('exploration-sections')),
            'exploration':value(state['exploration_status'],p,None,'Scoped historical observation; not whole-site clearance/current safety'),
            'access':value(state['access_status'],p,None,'Protected access is distinct from exploration; no raw source label/notes rendered')})
    world={'factions':[{'faction_id':value(x['faction_id'],owner(x['faction_id'])),'classification':value(x['classification'],owner('faction-activity'),None,'Identity/design classification, not current operations or faction intelligence')} for x in data('faction-activity')['factions']],
        'dungeon_sections':sections,'legal_reviews':[{'person':value(x,owner(x)),'current_result':value(('independent-legal-review-pending' if x=='maelor-thane' else 'military-review-pending') if ('independent legal review pending.' if x=='maelor-thane' else 'pending military review.') in file(owner(x)).read_text().split('## Historical record',1)[0] else None,owner(x),None,'Reviewed pending-status phrase only; no automatic verdict, destination or case conflation')} for x in ('maelor-thane','edrick-sorn')],
        'world_event_details':value(None,owner('world-event-references'),None,'Historical references only; current developments require targeted source review; no scheduler')}
    warnings={'provenance_and_identity':value('UNKNOWN details remain in their owners','state/open-verifications.md',None,'No raw verification/handoff text or private knowledge distinctions rendered'),
        'later_supplied_snapshot':value('PLAYED SESSION; closing cash provisional and current personal MP unverified' if year_end else 'APPROVED PLAYED SESSION' if ledger['schema_version'] in (5,6,7,8,9) else 'ADOPTED FROM PLAYER-SUPPLIED CONTINUITY; cash/MP provenance gaps remain' if c['schema_version']==6 else 'UNADOPTED; separate reconciliation required' if c['date']=='Year 848 Day 156' else 'SOURCE REVIEW REQUIRED; compare approved checkpoint with the historical supplied endpoint',checkpoint if c['schema_version']==6 else 'docs/world-bible-integration-audit.md',None,'Authoritative scene comes from checkpoint; no invented cash/MP bridge'),
        'privacy':value('Public repository / private-governance conflict unresolved','governance/precedence.md',None,'This projection does not certify the repository spoiler-safe; private GM-answer storage remains separate'),
        'proposals':value('Unapproved institutions/routes/clocks/answers remain proposed',owner('gm-workflow'))}
    personnel_ids={'tomas','master-beren','bren','mira-lodge-helper','joren','elsi','elias-renn','maera','mira-thorne'}
    personnel=[x for x in companions if x['person']['value'] in personnel_ids]
    companions=[x for x in companions if x['person']['value'] not in personnel_ids]
    result={'schema_version':1,'view_kind':'read-only reviewed-field projection','sections':{'current_scene':scene,'theron':hero,'finances':finances,'companions':companions,'personnel':personnel,'estate_and_academy':estate,'quests':quests,'world':world,'verification_warnings':warnings}}
    # Fingerprints make stale copies visibly invalid without storing a new authority.
    result['source_fingerprints']={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in sorted(used)}
    return result


def verify_view(root,candidate):
    expected=build_dashboard(root)
    check(json.dumps(candidate,sort_keys=True,allow_nan=False)==json.dumps(expected,sort_keys=True,allow_nan=False),'stale, edited or unsupported dashboard; regenerate from current owners')


def render_markdown(view):
    """Render only already-filtered fields; independent initially closed sections."""
    def clean(x):return html.escape(str(x)).replace('|','\\|').replace('\n',' ')
    def rows(obj,prefix=''):
        if isinstance(obj,dict) and set(obj)=={'value','source_ref','as_of','qualification'}:
            v='UNKNOWN' if obj['value'] is None else json.dumps(obj['value'],ensure_ascii=False)
            return [f"| {clean(prefix)} | {clean(v)} | {clean(obj['source_ref'])} | {clean(obj['as_of'] or 'UNKNOWN')} | {clean(obj['qualification'])} |"]
        result=[]
        iterator=obj.items() if isinstance(obj,dict) else enumerate(obj)
        for key,item in iterator:result.extend(rows(item,f'{prefix}.{key}' if prefix else str(key)))
        return result
    out=['# World status — read-only projection','Regenerate before use; owners and discovery review remain authoritative.','']
    def table(content):
        return ['| Field | Value | Source | Source as-of | Qualification |','|---|---|---|---|---|',*rows(content)]
    for section,content in view['sections'].items():
        out+=['<details>',f'<summary>{clean(section.replace("_"," ").title())}</summary>','']
        if section in ('companions','personnel'):
            out+=['| Person | Assignment | Status | Last verified location | Source date | Sources |','|---|---|---|---|---|---|']
            for row in content:
                values=[row['person']['value'],', '.join(row['assignment']['value']) or 'UNKNOWN / no assignment inferred',row['status']['value'],row['last_verified_location']['value'] or 'UNKNOWN',row['source_date']['value'] or 'UNKNOWN',', '.join(sorted({x['source_ref'] for x in row.values()}))]
                out.append('| '+' | '.join(clean(x) for x in values)+' |')
        elif section=='world':
            for name,group in content.items():
                out+=['<details>',f'<summary>{clean(name.replace("_"," ").title())}</summary>','',*table(group),'','</details>','']
        else:out+=table(content)
        out+=['','</details>','']
    return '\n'.join(out)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--format',choices=('json','markdown'),default='json');parser.add_argument('--check-view',type=Path);args=parser.parse_args()
    try:
        if args.check_view:
            if __package__:from .validate import unique_json
            else:from validate import unique_json
            verify_view(args.root,json.loads(args.check_view.read_text(),object_pairs_hook=unique_json));print('OK: dashboard matches current reviewed sources')
        else:
            view=build_dashboard(args.root);print(json.dumps(view,indent=2) if args.format=='json' else render_markdown(view))
    except (ValueError,OSError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr);return 1
    return 0


if __name__=='__main__':sys.exit(main())
