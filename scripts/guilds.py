"""Read-only guild/contract reference validation; no financial or membership actions."""
import json
import re

GUILD_MARKER = '\n## Guild and contract references — Chunk 5\n'
CONTRACT_FIELDS = {'contract_id','classification','issuing_organization_id','registry_organization_id','funding_party_id',
                  'funding_party_name','funding_source_ref','funding_source_quote','funding_committed_cp','objective','location_id',
                  'difficulty','eligibility_requirements','legal_authorization_ref','apprehension_authorized','acceptance_status',
                  'assigned_party_ids','deadline','reward_cp','reward_guaranteed','expenses_fees','evidence_requirements',
                  'completion_conditions','completion_status','payment_status','historical_payment_cp','historical_application_count',
                  'current_availability','existing_quest_ref','independent_notices_cancelled','financial_postings','source_refs',
                  'source_quote','last_verified_date','last_verified_note'}


def validate_contract(record, root, records, require, repository_file):
    """Validate terms/funding without accepting, completing or paying a contract.

    Missing historical funding is legitimate for already-paid reference records.
    Actual funding/title/legal truth still requires human source review.
    """
    require(isinstance(record, dict) and set(record)==CONTRACT_FIELDS, 'guild contract: invalid fields')
    for f in ('contract_id','current_availability','last_verified_note'):
        require(isinstance(record[f], str) and record[f].strip(), f'guild contract: invalid {f}')
    require(record['classification'] in ('CONFIRMED CANON','PROPOSED'), 'guild contract: invalid classification')
    def ref(ident, kinds):
        require(isinstance(ident, str) and ident in records and records[ident]['type'] in kinds,
                'guild contract: invalid entity reference')
        require(records[ident]['visibility']=='gm-reference', 'guild contract: secret reference excluded')
    for f in ('issuing_organization_id','registry_organization_id'):
        if record[f] is not None:
            ref(record[f], {'factions'})
            require(record['classification']=='PROPOSED' or records[record[f]]['status']!='research',
                    'guild contract: unapproved organization cannot issue canon contract')
    if record['funding_party_id'] is not None:
        ref(record['funding_party_id'], {'characters','factions'})
    if record['location_id'] is not None:
        ref(record['location_id'], {'locations'})
        require(not record['location_id'].startswith('route-'), 'guild contract: site must be physical location')
    if record['existing_quest_ref'] is not None:
        ref(record['existing_quest_ref'], {'quests'})
    if record['assigned_party_ids'] is not None:
        require(isinstance(record['assigned_party_ids'], list) and all(isinstance(i,str) for i in record['assigned_party_ids']),
                'guild contract: invalid assigned party')
        require(len(record['assigned_party_ids'])==len(set(record['assigned_party_ids'])), 'guild contract: duplicate assigned person')
        for ident in record['assigned_party_ids']:
            ref(ident, {'characters','creatures'})
    for f in ('funding_committed_cp','reward_cp','historical_payment_cp'):
        require(record[f] is None or type(record[f]) is int and record[f]>=0, 'guild contract: integer copper required')
    for f in ('reward_guaranteed','apprehension_authorized','independent_notices_cancelled'):
        require(type(record[f]) is bool, f'guild contract: invalid boolean {f}')
    require(record['financial_postings']==[], 'guild contract: maintenance cannot post money')
    require(record['independent_notices_cancelled'] is False, 'guild contract: cannot cancel unrelated notices')
    refs = record['source_refs']
    require(isinstance(refs, list) and refs and all(isinstance(s,str) for s in refs) and len(refs)==len(set(refs)),
            'guild contract: invalid sources')
    for source in refs:
        if source.startswith('entities/'):
            target=source.rsplit('/',1)[-1].removesuffix('.md')
            require(target in records and records[target]['visibility']=='gm-reference', 'guild contract: secret source excluded')
        repository_file(root,source,'contract source')
    require(isinstance(record['source_quote'],str) and record['source_quote'].strip(), 'guild contract: source quote required')
    require(any(record['source_quote'] in repository_file(root,s,'contract quote').read_text().split(GUILD_MARKER)[0] for s in refs),
            'guild contract: quote not found in original source')
    for f in ('funding_source_ref','legal_authorization_ref'):
        if record[f] is not None:
            require(record[f] in refs, 'guild contract: undeclared funding/legal source')
            repository_file(root,record[f],f)
    if record['reward_guaranteed']:
        require(record['classification']=='CONFIRMED CANON' and record['historical_payment_cp'] is None,
                'guild contract: proposals/paid history cannot create new guaranteed rewards')
        require(record['funding_party_id'] is not None or isinstance(record['funding_party_name'],str) and record['funding_party_name'].strip(),
                'guild contract: identifiable funding party required')
        require(record['funding_source_ref'] is not None and isinstance(record['funding_source_quote'],str)
                and record['funding_source_quote'].strip(), 'guild contract: funding commitment evidence required')
        require(record['funding_source_quote'] in repository_file(root,record['funding_source_ref'],'funding commitment').read_text().split(GUILD_MARKER)[0],
                'guild contract: funding quote not found')
        require(record['reward_cp'] is not None and record['funding_committed_cp'] is not None
                and record['funding_committed_cp']>=record['reward_cp'], 'guild contract: reward exceeds verified committed budget')
        if record['funding_party_id'] is not None:
            require(records[record['funding_party_id']]['status']!='research', 'guild contract: unapproved funder cannot guarantee reward')
    if record['apprehension_authorized']:
        require(record['legal_authorization_ref'] is not None, 'guild contract: bounty alone is not arrest authorization')
    require(type(record['historical_application_count']) is int and record['historical_application_count'] in (0,1),
            'guild contract: historical reward must be referenced once')
    if record['payment_status']=='historically-paid':
        require(record['historical_payment_cp'] is not None and record['historical_application_count']==1
                and record['reward_cp'] is None and record['reward_guaranteed'] is False,
                'guild contract: historical payout is not a new reward')
    else:
        require(record['payment_status'] in ('unknown','unpaid','not-payable','session-paid'), 'guild contract: invalid payment status')
        require(record['historical_payment_cp'] is None and record['historical_application_count']==0,
                'guild contract: unsupported payment history')


def validate_guilds(root, records, require, repository_file, unique_json):
    required={'guild-network','continental-guild-concord','contract-registry','guild-membership-and-contracts'}
    owners={'wayfarers-guild','dragon-slayer-academy'}
    marked={i for i in owners if (root/f'entities/factions/{i}.md').is_file()
            and GUILD_MARKER in (root/f'entities/factions/{i}.md').read_text()}
    if not (required & records.keys() or marked):
        return
    require(required<=records.keys() and marked==owners, 'guilds: incomplete guild framework')

    def shape(d, fields, label):
        expected_fields=set(fields.split())
        extensions={'network':'approved_design_index','Concord':'approved_charter','guild rules':'approved_professional_rules'}
        if isinstance(d,dict) and extensions.get(label) in d:
            expected_fields.add(extensions[label])
        require(isinstance(d,dict) and set(d)==expected_fields, f'guilds: invalid {label} fields')

    def text(v,label):
        require(isinstance(v,str) and v.strip(), f'guilds: invalid {label}')

    def strings(v,label):
        require(isinstance(v,list) and all(isinstance(i,str) and i.strip() for i in v), f'guilds: invalid {label}')
        require(len(v)==len(set(v)), f'guilds: duplicate {label}')

    def ref(i, kinds=None):
        require(isinstance(i,str) and i in records, 'guilds: broken entity reference')
        require(kinds is None or records[i]['type'] in kinds, 'guilds: invalid reference type')
        require(records[i]['visibility']=='gm-reference', 'guilds: secret reference excluded from public lookup')

    def place(i):
        ref(i,{'locations'})
        require(not i.startswith('route-'), 'guilds: physical location required')

    def refs(v):
        strings(v,'source refs')
        require(v, 'guilds: source refs required')
        for source in v:
            if source.startswith('entities/'):
                ref(source.rsplit('/',1)[-1].removesuffix('.md'))
            repository_file(root,source,'guild source')

    def quote(value,sources):
        text(value,'source quote')
        require(any(value in repository_file(root,s,'guild quote').read_text().split(GUILD_MARKER)[0] for s in sources),
                'guilds: quote not found in original source')

    def payload(ident, section=False):
        rec=records[ident];content=(root/f"entities/{rec['type']}/{ident}.md").read_text()
        if section:
            require(content.count(GUILD_MARKER)==1, 'guilds: duplicate owner section')
            content=content.split(GUILD_MARKER)[1]
        blocks=re.findall(r'^```json\n(.*?)\n```$',content,re.M|re.S)
        require(len(blocks)==1, 'guilds: expected one JSON block')
        try:
            d=json.loads(blocks[0],object_pairs_hook=unique_json)
        except ValueError as exc:
            require(False,f'guilds: invalid JSON: {exc}')
        require(isinstance(d,dict) and type(d.get('schema_version')) is int and d['schema_version']==1,
                'guilds: unsupported schema')
        return d

    network=payload('guild-network')
    shape(network,'schema_version classifications profile_owner_ids organizations branch_candidates concord_proposal_id automatic_financial_postings','network')
    strings(network['classifications'],'classifications')
    require(set(network['classifications'])=={'CONFIRMED CANON','HISTORICAL ORGANIZATION','ARCHIVED DESIGN','PROPOSED','UNKNOWN IDENTITY','REQUIRES APPROVAL'},
            'guilds: incomplete classification vocabulary')
    require(set(network['profile_owner_ids'])==owners and len(network['profile_owner_ids'])==2, 'guilds: profile owners cannot be replaced')
    require(network['concord_proposal_id']=='continental-guild-concord' and network['automatic_financial_postings'] is False,
            'guilds: no replacement guild or automatic finance')
    require(isinstance(network['organizations'],list), 'guilds: invalid organizations')
    organizations={}
    for o in network['organizations']:
        shape(o,'id entity_id classification organization_type archived_name archived_site_labels compatibility approval_status source_refs','organization')
        text(o['id'],'guild ID')
        require(o['id'] not in organizations, 'guilds: duplicate guild ID')
        organizations[o['id']]=o
        refs(o['source_refs']);text(o['organization_type'],'organization type');text(o['compatibility'],'compatibility')
        strings(o['archived_site_labels'],'archived sites')
        if o['id'].startswith('archived:'):
            require(o['classification']=='ARCHIVED DESIGN' and o['entity_id'] is None and o['approval_status']=='REQUIRES APPROVAL',
                    'guilds: archived guild design cannot be promoted or merged')
            text(o['archived_name'],'archived name')
        else:
            ref(o['entity_id'],{'factions'})
            require(o['id']==o['entity_id'] and o['classification']=='CONFIRMED CANON' and o['approval_status'] is None,
                    'guilds: established organization identity changed')
    require(set(organizations)=={'wayfarers-guild','dragon-slayer-academy','northern-provisioning-consortium',
                                'archived:ironhand','archived:seven-lamps','archived:scribes','archived:river-charter',
                                'archived:greenward','archived:stonewatch'}, 'guilds: unsupplied organization or missing crosswalk')
    require(isinstance(network['branch_candidates'],list) and len(network['branch_candidates'])==3, 'guilds: incomplete branch review')
    candidate_ids=set()
    for b in network['branch_candidates']:
        shape(b,'id guild_id candidate_settlement_id classification building_location_id responsible_officer_id operational_status approval_status approval_source_ref source_refs note','branch candidate')
        require(isinstance(b['id'],str) and b['id'] not in candidate_ids, 'guilds: duplicate branch candidate ID')
        candidate_ids.add(b['id'])
        require(b['guild_id']=='wayfarers-guild', 'guilds: invalid branch guild reference')
        place(b['candidate_settlement_id'])
        require(b['candidate_settlement_id'] in ('eastrun','briarfall-crossing','rivermere'), 'guilds: unsupported branch site')
        require(b['classification']=='ARCHIVED DESIGN' and b['building_location_id'] is None and b['responsible_officer_id'] is None
                and b['approval_status']=='REQUIRES APPROVAL' and b['approval_source_ref'] is None
                and b['operational_status']=='UNVERIFIED — NOT AN OPERATIONAL BRANCH ASSERTION',
                'guilds: archived branch has no approved hall, officer or operation')
        refs(b['source_refs']);text(b['note'],'branch note')

    concord=payload('continental-guild-concord')
    shape(concord,'schema_version classification operational approval_status approval_source_ref headquarters_location_id branch_location_ids leadership_ids '
          'member_organization_ids treasury_cp membership_fee_cp exam_fee_cp commission_percent divisions financial_postings','Concord')
    require(records['continental-guild-concord']['status']=='research' and concord['classification']=='PROPOSED'
            and concord['operational'] is False and concord['approval_status']=='REQUIRES APPROVAL'
            and concord['approval_source_ref'] is None, 'guilds: Concord remains unapproved and nonoperational')
    require(all(concord[f] is None for f in ('headquarters_location_id','treasury_cp','membership_fee_cp','exam_fee_cp','commission_percent'))
            and all(concord[f]==[] for f in ('branch_location_ids','leadership_ids','member_organization_ids','financial_postings')),
            'guilds: no Concord staff, membership, branches, fees or treasury established')
    require(isinstance(concord['divisions'],list) and len(concord['divisions'])==8, 'guilds: eight proposed divisions required')
    divisions=set()
    for d in concord['divisions']:
        shape(d,'id name classification responsibilities membership_requirements licensing ranking services contract_types funding_model '
              'regional_representation existing_guild_relationship_ids legal_limitations approval_status approval_source_ref source_refs','division')
        require(isinstance(d['id'],str) and d['id'] not in divisions, 'guilds: duplicate division ID')
        divisions.add(d['id'])
        require(d['classification']=='PROPOSED' and d['approval_status']=='REQUIRES APPROVAL' and d['approval_source_ref'] is None,
                'guilds: division cannot become canon')
        for f in ('name','licensing','ranking','funding_model','regional_representation','legal_limitations'):
            text(d[f],f)
        for f in ('responsibilities','membership_requirements','services','contract_types','existing_guild_relationship_ids'):
            strings(d[f],f)
        require(set(d['existing_guild_relationship_ids'])<=organizations.keys(), 'guilds: broken compatibility relationship')
        refs(d['source_refs'])

    require(divisions=={'concord-division:adventurers','concord-division:monster-hunters','concord-division:bounty-hunters',
                        'concord-division:merchants','concord-division:craftsmen','concord-division:healers',
                        'concord-division:dungeon-registrars','concord-division:transport-navigators'}, 'guilds: unsupported Concord division')
    contracts={};branches=set()
    for owner in owners:
        d=payload(owner,True)
        shape(d,'schema_version profile contracts new_memberships license_changes new_contracts automatic_financial_postings','owner section')
        require(d['automatic_financial_postings'] is False and all(d[f]==[] for f in ('new_memberships','license_changes','new_contracts')),
                'guilds: maintenance cannot enroll, alter licenses, create contracts or post money')
        p=d['profile']
        shape(p,'guild_id name organization_type classification headquarters_location_id branches leadership membership_structure services ranks licensing '
              'contract_types funding commission_policy jurisdiction other_guild_relationships last_verified_date source_refs','profile')
        require(p['guild_id']==owner and p['classification']=='CONFIRMED CANON', 'guilds: profile owner/classification changed')
        for f in ('name','organization_type','jurisdiction'):
            text(p[f],f)
        require(p['membership_structure'] is None and p['ranks'] is None and p['licensing'] is None and p['funding'] is None
                and p['other_guild_relationships'] is None and p['last_verified_date'] is None, 'guilds: unsupported guild membership/license/funding claim')
        require(p['headquarters_location_id']==('caelthorne' if owner=='wayfarers-guild' else None),
                'guilds: established headquarters/site changed')
        if p['headquarters_location_id'] is not None:
            place(p['headquarters_location_id'])
        strings(p['services'],'services');strings(p['contract_types'],'contract types');refs(p['source_refs'])
        require(isinstance(p['branches'],list), 'guilds: invalid branches')
        for b in p['branches']:
            shape(b,'id classification role settlement_id building_location_id responsible_officer_id services contract_board membership_registration '
                  'supplies_facilities route_ids operational_status source_refs source_quote','branch')
            require(isinstance(b['id'],str) and b['id'].startswith(owner+':') and b['id'] not in branches, 'guilds: duplicate/invalid branch ID')
            branches.add(b['id'])
            require(b['classification']=='CONFIRMED CANON', 'guilds: proposed branch cannot replace established reference')
            require(all(b[f] is None for f in ('building_location_id','responsible_officer_id','contract_board','membership_registration','supplies_facilities')),
                    'guilds: no hall, guildmaster, board, stock or fees established')
            strings(b['route_ids'],'branch route IDs');strings(b['services'],'branch services')
            text(b['role'],'branch role');text(b['operational_status'],'branch status');refs(b['source_refs']);quote(b['source_quote'],b['source_refs'])
            expected_sites={'wayfarers-guild:caelthorne-hq':'caelthorne','wayfarers-guild:unlocated-branches':None,
                            'dragon-slayer-academy:greyhaven-site':'greyhaven-valley'}
            require(b['id'] in expected_sites and b['settlement_id']==expected_sites[b['id']],
                    'guilds: confirmed branch/site cannot be relocated or named from design')
            if b['settlement_id'] is not None:
                place(b['settlement_id'])
                for road in b['route_ids']:
                    ref(road,{'locations'})
                    require(road.startswith('route-'), 'guilds: invalid route ID')
                    road_data=payload(road)
                    require(b['settlement_id'] in (road_data['start'],road_data['destination']), 'guilds: road does not serve branch context')
            else:
                require(b['role']=='established-branches-unlocated' and b['route_ids']==[], 'guilds: unlocated branches cannot acquire routes')
        require(isinstance(p['leadership'],list), 'guilds: invalid leadership')
        if owner=='wayfarers-guild':
            require(p['leadership']==[], 'guilds: no Wayfarers guildmaster established')
            policy=p['commission_policy']
            shape(policy,'reference_percent source_ref source_quote applicability retroactive_deductions financial_postings','commission reference')
            require(type(policy['reference_percent']) is int and policy['reference_percent']==10
                    and policy['retroactive_deductions'] is False and policy['financial_postings']==[], 'guilds: existing commission cannot be changed/reapplied')
            quote(policy['source_quote'],[policy['source_ref']]);text(policy['applicability'],'commission applicability')
        else:
            require(p['commission_policy'] is None, 'guilds: no academy commission imposed')
            require({x.get('entity_id') for x in p['leadership']}=={'master-beren','theron-ashvale','vaeltharion'} and len(p['leadership'])==3,
                    'guilds: independent academy leadership changed')
            for lead in p['leadership']:
                shape(lead,'entity_id role source_quote','leadership')
                ref(lead['entity_id'],{'characters','creatures'});text(lead['role'],'leadership role');quote(lead['source_quote'],p['source_refs'])
        require(isinstance(d['contracts'],list), 'guilds: invalid contracts')
        for c in d['contracts']:
            require(owner=='wayfarers-guild', 'guilds: no academy payment contract supplied')
            validate_contract(c,root,records,require,repository_file)
            cid=c['contract_id']
            require(cid not in contracts, 'guilds: duplicate contract ID/reward')
            contracts[cid]=c
    require(branches=={'wayfarers-guild:caelthorne-hq','wayfarers-guild:unlocated-branches','dragon-slayer-academy:greyhaven-site'},
            'guilds: no additional operational branch supplied')
    if __package__: from .finance_v3 import DAY196, DAY196_EVENTS
    else: from finance_v3 import DAY196, DAY196_EVENTS
    history = {'G-215','G-216','B-83','SS-41'}
    completed = {event[2] for event in DAY196_EVENTS.values() if event[2] is not None}
    if __package__:
        from .finance_expedition import SOURCE as EXPEDITION_SOURCE, REWARDS_CP
    else:
        from finance_expedition import SOURCE as EXPEDITION_SOURCE, REWARDS_CP
    expedition = REWARDS_CP.keys() if (root / EXPEDITION_SOURCE).is_file() else set()
    historical_ids = history | completed if (root / DAY196).is_file() else history
    westbridge_source = 'archive/session-handoffs/year853-day52-player-handoff.txt'
    westbridge = {f'WG-853-W{number:02}' for number in range(1, 12)} if (root / westbridge_source).is_file() else set()
    require(set(contracts) == historical_ids | expedition | westbridge, 'guilds: missing or unsupported played contract')
    for cid,c in contracts.items():
        if cid in expedition or cid in westbridge:
            require(c['completion_status'] == 'session-completed' and c['payment_status'] == 'session-paid'
                    and c['current_availability'] == 'completed-not-current-offer'
                    and c['source_refs'] == [westbridge_source if cid in westbridge else EXPEDITION_SOURCE] and c['reward_cp'] is None
                    and c['deadline'] is None and c['reward_guaranteed'] is False,
                    'guilds: expedition completion, payment or provenance differs')
            continue
        if cid in completed:
            require(c['completion_status'] == 'session-completed' and c['payment_status'] == 'session-paid'
                    and c['current_availability'] == 'completed-not-current-offer'
                    and c['assigned_party_ids'] == ['garrick-vale','nyx-thorne']
                    and c['source_refs'] == [DAY196] and c['reward_cp'] is None
                    and c['deadline'] is None and c['reward_guaranteed'] is False,
                    'guilds: Day196 completion, payment or provenance differs')
            continue
        if cid!='SS-41':
            payment={'G-215':2600,'G-216':3200,'B-83':4000}[cid]
            require(c['historical_payment_cp']==payment and c['current_availability']=='historical-not-current-offer'
                    and c['payment_status']=='historically-paid', 'guilds: historical payment/status changed')
            require(c['completion_status']==('historical-completed' if cid=='G-215' else None), 'guilds: unsupported historical completion')
        else:
            require(c['current_availability']=='revoked-specific-notice' and c['payment_status']=='unknown'
                    and c['historical_payment_cp'] is None and c['apprehension_authorized'] is False
                    and c['existing_quest_ref']=='first-oath-conspiracy', 'guilds: SS-41 withdrawal/quest boundary changed')
        require(c['acceptance_status'] is None and c['assigned_party_ids'] is None and c['deadline'] is None and c['reward_cp'] is None,
                'guilds: no new acceptance, assignment, deadline or payable reward')

    registry=payload('contract-registry')
    shape(registry,'schema_version contracts dungeon_contract_kinds automatic_financial_postings','contract routing')
    require(registry['automatic_financial_postings'] is False, 'guilds: automatic financial postings forbidden')
    require(isinstance(registry['contracts'],list), 'guilds: invalid contract routing')
    seen=set()
    for entry in registry['contracts']:
        shape(entry,'contract_id owner_entity_id','contract pointer')
        require(isinstance(entry['contract_id'],str) and entry['contract_id'] not in seen, 'guilds: duplicate contract pointer')
        seen.add(entry['contract_id'])
        ref(entry['owner_entity_id'],{'factions'})
        require(entry['owner_entity_id']=='wayfarers-guild', 'guilds: contract owner cannot be replaced')
    require(seen==set(contracts), 'guilds: contract routing coverage mismatch')
    strings(registry['dungeon_contract_kinds'],'dungeon contract kinds')
    require(set(registry['dungeon_contract_kinds'])=={'exploration','rescue','monster-removal','artifact-recovery','survey','escort','mapping','hazard-containment','salvage','research'},
            'guilds: missing dungeon integration categories')
    rules=payload('guild-membership-and-contracts')
    shape(rules,'schema_version rank_domains rank_owner_ids membership_procedure_classification membership_steps npc_role_categories '
          'justice_workflow_ref custody_owner_ref finance_owner_ref new_license_records new_staff_records automatic_world_events','guild rules')
    strings(rules['rank_domains'],'rank domains')
    require(set(rules['rank_domains'])=={'guild-license','combat-power','dungeon-threat','professional-certification','contract-difficulty'},
            'guilds: rank domains must remain separate')
    strings(rules['rank_owner_ids'],'rank owners')
    require(set(rules['rank_owner_ids'])=={'theron-ashvale','lyanna-ashvale','garrick-vale','nyx-thorne','lyra-moonvale'}, 'guilds: original rank owners required')
    for ident in rules['rank_owner_ids']:
        ref(ident,{'characters'})
    require(rules['membership_procedure_classification']=='PROPOSED' and rules['new_license_records']==[]
            and rules['new_staff_records']==[] and rules['automatic_world_events'] is False, 'guilds: no new licenses/staff/events allowed')
    require(rules['justice_workflow_ref']=='justice-and-jurisdiction' and rules['custody_owner_ref']=='prisoner-custody'
            and rules['finance_owner_ref']=='party-finances', 'guilds: existing justice/custody/finance owners required')
    for k in ('justice_workflow_ref','custody_owner_ref','finance_owner_ref'):
        ref(rules[k])
    strings(rules['membership_steps'],'membership steps');strings(rules['npc_role_categories'],'NPC role categories')
