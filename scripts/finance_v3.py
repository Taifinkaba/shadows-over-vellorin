"""Source-backed finance3 arithmetic and endpoint provenance. No posting/write API."""
import hashlib
import json
import re

ADOPTION='changes/chronicles/year848-day181-endpoint-adoption.md'
HISTORY='archive/checkpoints/year848-day156-finance-ledger.json'
STATE_HISTORY='archive/checkpoints/year848-day156-2015.json'
RECORD_HISTORY='archive/checkpoints/year848-day156-entity-records.json'
HISTORICAL_HASHES = {'archive/checkpoints/year848-day156-2015.json': '1083b116bdfbfac0946984420930178ebd31250ebf311362290f0a5cb6fed294', 'archive/checkpoints/year848-day156-finance-ledger.json': '97226723e6511e4c5fe6059d6509b45d9cb05e688e1ef79356f1bfeb089656d9', 'archive/checkpoints/year848-day156-entity-records.json': 'ae9051234f54c925c583681a30b6aa3fda8d236804de9d5159dd4e0379e95367'}
BRIDGE_STATUS='UNEXPLAINED ENDPOINT DIFFERENCE — PROVENANCE UNRESOLVED'
MP_STATUS='UNEXPLAINED ENDPOINT CHANGE — PROVENANCE UNRESOLVED'
LEGACY_EVENT_SOURCES = {'changes/chronicles/character-reference-design-approval.md', 'changes/chronicles/npc-autonomy-framework-maintenance.md', 'changes/chronicles/year848-day156-end-session.md', 'changes/chronicles/year847-day472-first-hour.md', 'changes/chronicles/gm-continuity-maintenance.md', 'changes/chronicles/main-quest-framework-maintenance.md', 'changes/chronicles/year848-day137-end-session.md', 'changes/chronicles/world-geography-travel-design.md', 'changes/chronicles/year847-day153-freight.md', 'changes/chronicles/guild-concord-contracts-design.md', 'changes/chronicles/economy-framework-maintenance.md', 'changes/chronicles/year847-day153-finances.md', 'changes/chronicles/dungeon-exploration-registry-design.md', 'changes/chronicles/year847-day153-development.md', 'changes/chronicles/settlements-businesses-services-design.md', 'changes/chronicles/justice-courts-prisons-design.md'}

RECONCILIATION='changes/chronicles/year848-day181-cottage-mana-reconciliation.md'
REPAIR_STATUS='RECONCILED — PLAYER-CONFIRMED BRIARSTONE COTTAGE REPAIRS'
RECOVERY_STATUS='RECONCILED — PLAYER-CONFIRMED SPIRIT MANA ASSIMILATION II'
DAY196 = 'changes/chronicles/year848-day196-end-session.md'
PLAYED_SESSION = 'PLAYER-APPROVED PLAYED SESSION'
DAY196_WINDOW = dict(first_date='Year 848 Day 182', last_date='Year 848 Day 196', source_ref=DAY196)
# Approved aggregate postings. Dates and accounts were not supplied for these events.
DAY196_EVENTS = {
    'y848-d196-vanguard-refit': ('other-expense', -16000, None, None),
    'y848-d196-supply-refit': ('other-expense', -10500, None, None),
    'y848-d196-eastrun-reward': ('contract-reward', 4200, 'WG-848-196-EASTRUN', None),
    'y848-d196-briarfall-reward': ('contract-reward', 3800, 'WG-848-196-BRIARFALL', None),
    'y848-d196-guild-commission': ('other-expense', -800, None, 'Wayfarers Guild'),
    'y848-d196-field-expenses': ('supplies-purchased', -800, None, None),
    'y848-d196-companion-compensation': ('wages-paid', -2000, None, 'Garrick Vale and Nyx Thorne'),
}

CATEGORIES={'maintenance':'outflow','business-revenue':'inflow','wages-paid':'outflow','supplies-purchased':'outflow','construction-payment':'outflow','property-purchase':'outflow','contract-reward':'inflow','internal-transfer':'internal','owner-distribution':None,'restitution-disbursement':'outflow','other-receipt':'inflow','other-expense':'outflow'}


def validate_finance_v3(root,state,l):
    if __package__:from .validate import require,keys,integer,string,repository_file,read_json,validate_finance_ledger_v2,frontmatter,copper
    else:from validate import require,keys,integer,string,repository_file,read_json,validate_finance_ledger_v2,frontmatter,copper
    def evidence(e):
        keys(e,{'source_ref','quote'},'finance3 evidence')
        string(e['quote'],'finance3 quote');path=repository_file(root,e['source_ref'],'finance3 evidence')
        require(e['quote'] in path.read_text(),'finance3: source quote missing')
        require(e['source_ref'].startswith('changes/chronicles/') and e['source_ref'] not in (ADOPTION,RECONCILIATION) and e['source_ref'] not in LEGACY_EVENT_SOURCES,'finance3: historical/adoption/reference evidence is not a new payment/funding event')
    def actor(ident):
        require(isinstance(ident,str) and re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',ident),'finance3: invalid actor id')
        entries={x['id']:x for x in read_json(root/'index.json')['entries']}
        require(ident in entries and entries[ident]['type'] in {'characters','factions'},'finance3: unknown actor')
        require(entries[ident]['visibility']=='gm-reference','finance3: secret actor excluded')
    def stamp(date,time):
        require(isinstance(date,str) and re.fullmatch(r'Year \d+ Day \d+',date),'finance3: invalid date')
        require(isinstance(time,str) and re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',time),'finance3: invalid time')
        year,day=map(int,re.findall(r'\d+',date));return year,day,time
    def status(value):require(value in ('verified','player-approved'),'finance3: actual verification/approval required')
    def signed(value,label):require(type(value) is int,label+': integer copper required')
    has_session = l.get('schema_version') == 5
    if has_session:
        require(l.get('approved_session_window') == DAY196_WINDOW, 'finance5: approved session window differs')
    keys(l,{'schema_version','as_of','source','qualification','currency','historical_day156_ref','endpoint','bridge','account_verifications','transactions','controlled_cash','commitments','excluded_property','automatic_future_income'} | ({'post_arc_transactions'} if l.get('schema_version') in (4,5) else set()) | ({'approved_session_window'} if has_session else set()),'finance3')
    require(type(l['schema_version']) is int and l['schema_version'] in (3,4,5),'finance3: version')
    def integer_money(obj):
        if isinstance(obj,dict):
            for key,value in obj.items():
                if key.endswith('_cp') and value is not None:require(type(value) is int,'finance3: integer copper required')
                integer_money(value)
        elif isinstance(obj,list):
            for item in obj:integer_money(item)
    integer_money(l)

    for path,digest in HISTORICAL_HASHES.items():
        p=repository_file(root,path,'immutable Day156 snapshot')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'finance3: immutable Day156 history changed')
    require(l['historical_day156_ref']==HISTORY,'finance3: historical owner mismatch')
    old=read_json(root/HISTORY);oldstate=read_json(root/STATE_HISTORY)
    validate_finance_ledger_v2(root,oldstate,old)  # Keep every historical arithmetic/ownership check.
    require(l['currency']==old['currency'] and all(type(l['currency'][k]) is int for k in ('cp_per_gp','cp_per_sp')),'finance3: currency conversion differs')
    require(l['automatic_future_income'] is False,'finance3: automatic income forbidden')
    repository_file(root,l['source'],'finance3 source');string(l['qualification'],'finance3 qualification')
    require(l['source']==state['source'] and l['as_of']==dict(date=state['date'],season=state['calendar']['season'],day_of_season=state['calendar']['day_of_season'],time=state['time'],location=state['location'],session_status=state['status']),'finance3: checkpoint/source/as-of mismatch')
    require(state['provenance']['mp_bridge']['classification']==(RECOVERY_STATUS if l['schema_version'] in (4,5) else MP_STATUS),'finance3/4: checkpoint reconciliation version mismatch')
    endpoint=l['endpoint'];keys(endpoint,{'as_of','total_cp','source_ref','classification'},'finance3 endpoint')
    require(endpoint=={'as_of':{'date':'Year 848 Day 181','time':'19:30'},'total_cp':74590,'source_ref':ADOPTION,'classification':'PLAYER-APPROVED SUPPLIED ENDPOINT'},'finance3: approved endpoint changed')
    require(type(endpoint['total_cp']) is int,'finance3: integer endpoint')
    b=l['bridge']
    expected=dict(historical_closing_cp=77190,endpoint_total_cp=74590,difference_cp=2600,classification=BRIDGE_STATUS,is_transaction=False,assigned_account_id=None,source_ref=ADOPTION)
    repair_ids=[]
    if l['schema_version'] in (4,5):
        payments=l['post_arc_transactions']
        require(isinstance(payments,list) and len(payments)==2,'finance4: exactly two approved historical payments')
        for t,(ident,day,season_day,amount,quote) in zip(payments,[('briarstone-repair-deposit-day158',158,38,800,'repair deposit paid800cp'),('briarstone-repair-final-day165',165,45,1800,'final cottage repair payment paid1800cp')]):
            approved=dict(id=ident,source_event_id=ident,date=f'Year 848 Day {day}',season='Suncrest',season_day=season_day,time=None,category='maintenance',property_id='briarstone-cottage',amount_cp=amount,cash_effect_cp=-amount,commitment_effect_cp=0,funding_scope='uncommitted-controlled-funds',account_id=None,recipient=None,source_ref=RECONCILIATION,source_quote=quote,status='player-confirmed-continuity',application_count=1)
            require(t==approved and type(t['application_count']) is int and type(t['season_day']) is int,'finance4: approved repair payment/provenance differs')
            require(quote in repository_file(root,RECONCILIATION,'repair evidence').read_text(),'finance4: repair source quote missing')
            repair_ids.append(ident)
        expected.update(classification=REPAIR_STATUS,source_ref=RECONCILIATION,transaction_ids=repair_ids)
        require(old['arc_reconciliation']['closing_cp']+sum(t['cash_effect_cp'] for t in payments)==endpoint['total_cp'],'finance4: repairs must explain endpoint once')
    require(b==expected,'finance3/4: historical bridge differs from approved provenance')
    require(all(type(b[k]) is int for k in ('historical_closing_cp','endpoint_total_cp','difference_cp')) and b['is_transaction'] is False,'finance3: bridge types')
    require(b['historical_closing_cp']==old['arc_reconciliation']['closing_cp'] and b['historical_closing_cp']-endpoint['total_cp']==b['difference_cp'],'finance3: bridge arithmetic')
    accounts={};balances={};ids=set();historical_ids={x['id'] for x in old['arc_reconciliation']['events']}|{'eight-period-model','historical_distribution','endpoint_difference','day181_bridge'}
    startstamp = stamp(endpoint['as_of']['date'], endpoint['as_of']['time'])
    if has_session:
        # No intra-day order is established at the close of the approved window.
        startstamp = stamp('Year 848 Day 197', '00:00')
    if state['time'] is None:
        require(has_session and state['source'] == DAY196, 'finance5: unknown closing time needs approved source')
        endstamp = stamp(state['date'], '00:00')
    else:
        endstamp = stamp(state['date'], state['time'])
    require(not has_session or endstamp[:2] >= (848, 196), 'finance5: checkpoint precedes approved window')
    require(has_session or endstamp>=startstamp,'finance3: current date precedes endpoint')
    require(isinstance(l['account_verifications'],list) and isinstance(l['transactions'],list),'finance3: lists required')
    for a in l['account_verifications']:
        keys(a,{'account_id','opening_cp','owner','scope','authorized_actor_ids','status','date','time','evidence'},'finance3 account verification')
        string(a['account_id'],'account id');require(a['account_id'] not in accounts,'finance3: duplicate account')
        integer(a['opening_cp'],'finance3 account opening');string(a['owner'],'finance3 owner')
        require(a['scope']=='controlled','finance3: third-party/noncash cannot fund controlled cash')
        status(a['status']);evidence(a['evidence']);when=stamp(a['date'],a['time'])
        require(a['evidence']['source_ref'] != DAY196, 'finance5: session evidence does not verify an account')
        require(startstamp<=when<=endstamp,'finance3: account verification outside current period')
        require(isinstance(a['authorized_actor_ids'],list) and a['authorized_actor_ids'] and len(a['authorized_actor_ids'])==len(set(a['authorized_actor_ids'])),'finance3: authority required')
        for ident in a['authorized_actor_ids']:actor(ident)
        accounts[a['account_id']]=a;balances[a['account_id']]=a['opening_cp']
    total=endpoint['total_cp'];paid=0;events=set(historical_ids)|set(repair_ids);last=startstamp
    session_ids = set()
    approved_contracts = {event[2] for event in DAY196_EVENTS.values() if event[2] is not None}
    if has_session:
        require(sum(balances.values()) <= total + sum(event[1] for event in DAY196_EVENTS.values()),
                'finance5: account verification cannot create cash')
    else:
        require(sum(balances.values())<=total,'finance3: account verification cannot create cash')
    for t in l['transactions']:
        keys(t,{'id','source_event_id','date','time','evidence','status','category','direction','amount_cp','payer','recipient','account_id','to_account_id','authority_id','cash_effect_cp','revenue_recognized_cp','commitment_id','commitment_effect_cp','property_id','business_id','contract_id','application_count','ownership_scope'},'finance3 transaction')
        string(t['id'],'transaction id');string(t['source_event_id'],'source event id')
        require(t['id'] not in ids and t['id'] not in historical_ids and t['id'] not in repair_ids and t['source_event_id'] not in events,'finance3: duplicate/historical transaction event')
        ids.add(t['id']);events.add(t['source_event_id'])
        require(t['ownership_scope']=='controlled','finance3: third-party/noncash transaction excluded')
        status(t['status']);evidence(t['evidence'])
        require(t['category'] in CATEGORIES,'finance3: unsupported category/noncash appraisal')
        direction=t['direction'];require(direction in ('inflow','outflow','internal'),'finance3: direction')
        require((t['category']=='owner-distribution' and direction in ('internal','outflow')) or direction==CATEGORIES[t['category']],'finance3: category/direction mismatch')
        integer(t['amount_cp'],'finance3 amount',1);signed(t['cash_effect_cp'],'finance3 cash effect');signed(t['commitment_effect_cp'],'finance3 commitment effect');integer(t['revenue_recognized_cp'],'finance3 revenue')
        require(type(t['application_count']) is int and t['application_count']==1,'finance3: transaction must apply once')
        expected_effect = t['amount_cp'] * (1 if direction == 'inflow' else -1 if direction == 'outflow' else 0)
        require(t['cash_effect_cp'] == expected_effect, 'finance3: cash effect mismatch')
        require(t['revenue_recognized_cp'] == (t['amount_cp'] if direction == 'inflow' else 0),
                'finance3: internal transfer/distribution is not new income')
        if t['evidence']['source_ref'] == DAY196:
            require(has_session and len(ids) == len(session_ids) + 1 and t['id'] in DAY196_EVENTS
                    and t['source_event_id'] == t['id'], 'finance5: unexpected or repeated session posting')
            require((t['category'], t['cash_effect_cp'], t['contract_id'], t['recipient']) == DAY196_EVENTS[t['id']],
                    'finance5: approved session posting differs')
            require(t['status'] == 'player-approved' and t['commitment_effect_cp'] == 0
                    and all(t[k] is None for k in ('date','time','payer','account_id','to_account_id',
                                                   'authority_id','commitment_id','property_id','business_id')),
                    'finance5: session scope, commitment or unknown fields differ')
            session_ids.add(t['id'])
            total += t['cash_effect_cp']
            continue
        require(t['id'] not in DAY196_EVENTS and t['source_event_id'] not in DAY196_EVENTS,
                'finance5: reserved session event reference')
        require(t['contract_id'] not in approved_contracts, 'finance5: completed bounty cannot be posted again')
        require(not has_session or session_ids == set(DAY196_EVENTS), 'finance5: session postings must precede later events')
        when = stamp(t['date'], t['time'])
        require(last <= when <= endstamp, 'finance3: transactions must be ordered after endpoint')
        last = when
        ident=t['account_id'];require(ident in accounts,'finance3: verified funding/receiving account required')
        actor(t['authority_id']);require(t['authority_id'] in accounts[ident]['authorized_actor_ids'],'finance3: unauthorized account actor')
        require(when>=stamp(accounts[ident]['date'],accounts[ident]['time']),'finance3: funding authority not yet verified')
        for role in ('payer','recipient'):string(t[role],'finance3 '+role)
        if direction in ('outflow','internal'):
            require(balances[ident]>=t['amount_cp'],'finance3: insufficient verified account funds');balances[ident]-=t['amount_cp']
        else:balances[ident]+=t['amount_cp']
        if direction=='internal':
            dest=t['to_account_id'];require(dest in accounts and dest!=ident,'finance3: distinct verified transfer destination required')
            require(when>=stamp(accounts[dest]['date'],accounts[dest]['time']),'finance3: destination not yet verified')
            balances[dest]+=t['amount_cp']
        else:require(t['to_account_id'] is None,'finance3: unexpected destination account')
        if t['category']=='construction-payment':
            require(t['commitment_id']=='estate-expansion' and t['commitment_effect_cp']==-t['amount_cp'],'finance3: construction payment must reduce commitment once')
            paid+=t['amount_cp'];require(paid<=31700,'finance3: payment exceeds commitment')
        else:require(t['commitment_id'] is None and t['commitment_effect_cp']==0,'finance3: unsupported commitment effect')
        for field in ('property_id','business_id','contract_id'):
            if t[field] is not None:string(t[field],'finance3 associated reference')
        if t['property_id'] is not None:
            p=repository_file(root,'entities/locations/'+t['property_id']+'.md','finance3 property');require(frontmatter(p)['visibility']=='gm-reference','finance3: secret property')
        if t['business_id'] is not None:
            require(':' in t['business_id'],'finance3: parent-scoped business required')
            parent=t['business_id'].split(':')[0];p=repository_file(root,'entities/locations/'+parent+'.md','finance3 business')
            blocks=re.findall(r'^```json\n(.*?)\n```$',p.read_text(),re.M|re.S)
            require(len(blocks)==1 and t['business_id'] in {x['id'] for x in json.loads(blocks[0])['businesses']},'finance3: unknown business')
            require(t['property_id'] in (None,parent),'finance3: business/property mismatch')
        if t['category']=='contract-reward':require(t['contract_id'] is not None and t['contract_id'] not in ('G-215','G-216','B-83','SS-41'),'finance3: historical reward cannot be paid again')
        total+=t['cash_effect_cp'];require(total>=0 and sum(balances.values())<=total,'finance3: controlled/account arithmetic')
    require(not has_session or session_ids == set(DAY196_EVENTS), 'finance5: missing session posting')
    cash=l['controlled_cash'];keys(cash,{'total_cp','accounts','allocation_status'},'finance3 cash');integer(cash['total_cp'],'finance3 total')
    require(cash['total_cp']==total==copper(state['money']['total_gp_sp']),'finance3: current total differs from endpoint plus actual transactions/checkpoint')
    expected_accounts=[dict(id=ident,owner=accounts[ident]['owner'],balance_cp=balance) for ident,balance in balances.items()]
    require(cash['accounts']==expected_accounts,'finance3: fabricated current account allocation')
    expected_status='UNRECONCILED / UNKNOWN' if not accounts else 'VERIFIED' if sum(balances.values())==total else 'PARTIALLY VERIFIED / REMAINDER UNKNOWN'
    require(cash['allocation_status']==expected_status,'finance3: allocation qualification')
    commit=l['commitments'];keys(commit,{'expansion_committed_cp','expansion_paid_cp','expansion_outstanding_cp','uncommitted_cp','construction_started','progress_ref'},'finance3 commitment')
    for k in ('expansion_committed_cp','expansion_paid_cp','expansion_outstanding_cp','uncommitted_cp'):integer(commit[k],'finance3 '+k)
    require(commit['expansion_committed_cp']==31700 and commit['expansion_paid_cp']==paid and commit['expansion_outstanding_cp']==31700-paid and commit['uncommitted_cp']==total-(31700-paid),'finance3: commitment/current availability arithmetic')
    require(commit['uncommitted_cp']>=0,'finance3: committed funds not available for unrelated spending')
    require(type(commit['construction_started']) is bool,'finance3: construction flag')
    if commit['progress_ref'] is None:require(commit['construction_started'] is False,'finance3: construction needs actual progress evidence')
    else:
        evidence(commit['progress_ref'])
        require(commit['progress_ref']['source_ref'] != DAY196, 'finance5: session evidence does not verify expansion progress')
    require(all(x.get('included_in_controlled_cash') is False for x in l['excluded_property']),'finance3: excluded property cannot enter cash')
    require(l['excluded_property']==old['excluded_property'],'finance3: excluded ownership/noncash boundaries changed without separate migration')
    return {'balances':balances,'total_cp':total,'paid_cp':paid}


def validate_checkpoint6(root,s):
    if __package__:from .validate import require,keys,repository_file,read_json,YEAR853_SOURCE,WESTBRIDGE_SOURCE
    else:from validate import require,keys,repository_file,read_json,YEAR853_SOURCE,WESTBRIDGE_SOURCE
    if s['source'] == WESTBRIDGE_SOURCE:
        if __package__:
            from .session_westbridge import validate_checkpoint
        else:
            from session_westbridge import validate_checkpoint
        return validate_checkpoint(root, s)
    year853 = s['source'] == YEAR853_SOURCE
    p=s['provenance'];keys(p,{'classification','adoption_source_ref','historical_checkpoint_ref','historical_entity_records_ref','current_presence','current_equipment','exact_room','conditional_defense','carried_forward_world_context_ref','mp_bridge'} | ({'year853_readings'} if year853 else set()),'checkpoint6 provenance')
    require(p['classification'] in ('PLAYER-SUPPLIED ENDPOINT ADOPTION', PLAYED_SESSION)
            and p['adoption_source_ref']==ADOPTION and p['historical_checkpoint_ref']==STATE_HISTORY and p['historical_entity_records_ref']==RECORD_HISTORY and p['carried_forward_world_context_ref']==STATE_HISTORY,'checkpoint6: provenance source mismatch')
    for name in ('adoption_source_ref','historical_checkpoint_ref','historical_entity_records_ref','carried_forward_world_context_ref'):repository_file(root,p[name],'checkpoint6 history')
    old_bridge=dict(from_mp=378,to_mp=400,difference_mp=22,classification=MP_STATUS,recovery_events=[])
    recovered=dict(from_mp=378,to_mp=400,difference_mp=22,classification=RECOVERY_STATUS,recovery_events=[dict(ability='Spirit Mana Assimilation II',intervals=1,uninterrupted_minutes=10,usable_ambient_mana=True,concentration_conditions_met=True,potential_mp=24,actual_mp=22,excess_mp=2,personal_max_mp=400,date=None,location=None,source_ref=RECONCILIATION)])
    year_end = s['source'] == 'changes/chronicles/year852-day1-end-session.md'
    last_tracked = dict(from_mp=400, to_mp=385, difference_mp=-15,
                        classification='LAST TRACKED — CURRENT PERSONAL MP UNVERIFIED',
                        recovery_events=[])
    allowed_bridges = (last_tracked,) if year_end else (old_bridge, recovered)
    if s['source'] == 'changes/chronicles/year852-day365-end-session.md':
        allowed_bridges = (dict(last_tracked, from_mp=385, to_mp=351, difference_mp=-34),)
    if year853:
        allowed_bridges = (dict(last_tracked, from_mp=351, to_mp=410, difference_mp=59,
                                classification='DAY 28 READING — INTERVENING MOVEMENTS AND CLOSING POOLS UNVERIFIED'),)
        previous = 'archive/checkpoints/year852-day365.json'
        require(p['year853_readings'] == dict(day=28, hp=104, mp=410, nexus_mp=180,
                                             nexus_recharge_source=None, previous_checkpoint=previous),
                'checkpoint6: observed Day 28 readings and unknown recharge')
        repository_file(root, previous, 'checkpoint6: prior session')
    require(p['mp_bridge'] in allowed_bridges,'checkpoint6: recovery must match approved capped interval or historical unresolved snapshot')
    if p['mp_bridge']==recovered:
        repository_file(root,RECONCILIATION,'mana continuity')
        event=p['mp_bridge']['recovery_events'][0]
        require(all(type(event[k]) is int for k in ('intervals','uninterrupted_minutes','potential_mp','actual_mp','excess_mp','personal_max_mp')) and event['usable_ambient_mana'] is True and event['concentration_conditions_met'] is True,'checkpoint6: recovery types/conditions')
    require(all(type(p['mp_bridge'][k]) is int for k in ('from_mp','to_mp','difference_mp')),'checkpoint6: MP types')
    require(type(p['conditional_defense']) is int and p['conditional_defense']==s['resources']['equipped_defense']+2,'checkpoint6: conditional DEF')
    for name in ('current_presence','current_equipment'):
        d=p[name];keys(d,{'status','evidence_ref'}|({'night_sovereign_carried_not_equipped'} if name=='current_equipment' else set()),'checkpoint6 observation')
        require(d['status'] in ('UNKNOWN','VERIFIED'),'checkpoint6: verification status')
        if d['status']=='UNKNOWN':
            require(d['evidence_ref'] is None,'checkpoint6: unknown observation cannot imply verification')
            if name=='current_presence':require(s['context']['companions_present']==[] and s['context']['party_roles']=={},'checkpoint6: no inferred companion positions')
            else:require(d['night_sovereign_carried_not_equipped'] is None,'checkpoint6: historical wearing state is not current')
        else:
            require(isinstance(d['evidence_ref'],str) and d['evidence_ref']!=ADOPTION,'checkpoint6: actual new observation source required');repository_file(root,d['evidence_ref'],'checkpoint6 observation')
            if name=='current_equipment':require(type(d['night_sovereign_carried_not_equipped']) is bool,'checkpoint6: wearing observation type')
    if s['source'] == DAY196:
        require(p['classification'] == PLAYED_SESSION, 'checkpoint6: Day196 requires played-session provenance')
        require((s['date'], s['time'], s['location'], s['status']) ==
                ('Year 848 Day 196', None, 'Ashvale Lodge', 'ENDED')
                and s['calendar'] == dict(season='Suncrest', day_of_season=76)
                and p['exact_room'] is None, 'checkpoint6: Day196 endpoint differs')
        require(p['current_presence']['status'] == p['current_equipment']['status'] == 'UNKNOWN',
                'checkpoint6: Day196 unverified observations')
        require(s['theron'] == {**read_json(root/STATE_HISTORY)['theron'], 'mp': 400}
                and (s['resources']['staff_mp'], s['resources']['staff_mp_max'],
                     s['resources']['wagon_mp'], s['resources']['wagon_mp_max']) == (156, 180, 60, 60)
                and s['resources'].get('refitted_wagon_mana') == {
                    'vanguard-wagon': {'current': 120, 'max': 120}, 'ashvale-wagon': {'current': 80, 'max': 80}},
                'checkpoint6: Day196 resource snapshot differs')
    if s['source'] in (ADOPTION,RECONCILIATION):
        require(p['classification'] == 'PLAYER-SUPPLIED ENDPOINT ADOPTION', 'checkpoint6: adoption provenance')
        old=read_json(root/STATE_HISTORY)
        require(s['date']=='Year 848 Day 181' and s['calendar']==dict(season='Suncrest',day_of_season=61) and s['time']=='19:30' and s['location']=='Ashvale Estate' and s['status']=='UNKNOWN' and p['exact_room'] is None,'checkpoint6: approved endpoint/missing fields differ')
        require(s['theron']=={**old['theron'],'mp':400} and s['resources']==old['resources'] and s['world']==old['world'] and s['custody']==old['custody'],'checkpoint6: unrelated canon/resource change during adoption')
        require(p['current_presence']['status']==p['current_equipment']['status']=='UNKNOWN','checkpoint6: no invented endpoint observations')
