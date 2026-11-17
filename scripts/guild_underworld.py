"""Read-only guild/underworld design checks; no enrollment, crime or money writer."""
import json
import re

APPROVAL='changes/chronicles/phase2-04-guild-underworld-approval.md'
GUILDS={
    'ironhand-smiths-compact':('archived:ironhand','ironhollow-holds'),
    'circle-of-seven-lamps':('archived:seven-lamps','caelthorne'),
    'scribes-collegium':('archived:scribes','caelthorne'),
    'river-charter-league':('archived:river-charter','rivermere'),
    'greenward-covenant':('archived:greenward','silverbrook'),
    'stonewatch-wardens':('archived:stonewatch','northern-marches')}
CRIMINAL={
    'gilded-hand':('Gilded Hand','valedorn'), 'thornless-circle':('Thornless Circle','elyndor'),
    'black-pick-syndicate':('Black Pick Syndicate','ironhollow-holds'), 'sable-current':('Sable Current','rivermere'),
    'red-antler-brotherhood':('Red Antler Brotherhood','frostmarch'),
    'veiled-coin-exchange':('Veiled Coin Exchange',None), 'broken-seal-society':('Broken Seal Society',None),
    'nightglass-circle':('Nightglass Circle',None)}
INDEPENDENT={'wayfarers-guild','dragon-slayer-academy','northern-provisioning-consortium'}
DUES={'apprentice':100,'journeyman':300,'master':800,'traveling-member':200}
STATUS_CLASSES={'lawful-guild','unrecognized-association','suspended-guild','outlawed-organization','criminal-faction'}
CONTRACT_KINDS={'apprenticeship-agreement','skilled-labor','caravan-protection','research-commission',
                'material-procurement','craft-certification','merchant-arbitration','guild-notice',
                'contract-dispute','professional-discipline'}
CONTRACT_TEMPLATE=set('id kind status issuer worker_or_counterparty scope professional_competence consent_ref '
                      'legal_authority_ref route_or_site_refs materials_and_safety term_or_deadline compensation_quote_cp '
                      'verified_funding_ref acceptance_evidence completion_evidence payment_evidence source_refs'.split())
DECISION_TEMPLATE=set('organization_id jurisdiction_id decision_kind competent_authority_id legal_basis_ref '
                      'decision_evidence_ref notice_and_defense_ref appeal_or_review_ref effective_scope'.split())
TRANSACTION_TEMPLATE=set('event_id status seller_ref buyer_ref goods_or_service ownership_provenance_ref quantity '
                        'quoted_price_cp available_funds_evidence_ref transport_route_refs storage_or_delivery_terms '
                        'jurisdiction_and_legal_risk consent_or_coercion_evidence_ref event_evidence_ref source_refs finance_transaction_ref'.split())
ILLICIT_CONTEXTS={'stolen-goods','counterfeit-documents','smuggled-cargo','restricted-ingredients','illegal-mining-materials',
                  'forged-certifications','unlawful-gambling','extortion','illicit-information','criminal-debt','bribery','fraudulent-transactions'}
AUTONOMY=['npc-autonomy-and-time','faction-activity','world-event-references']


def validate_guild_underworld(root,records,require,repository_file,unique_json):
    def check(condition,message):require(condition,'guild underworld: '+message)
    def shape(value,fields):check(isinstance(value,dict) and set(value)==set(fields.split()),'unexpected design fields')
    def text(value):check(isinstance(value,str) and bool(value.strip()),'text required')
    def strings(value):
        check(isinstance(value,list) and all(isinstance(v,str) and v.strip() for v in value)
              and len(value)==len(set(value)),'invalid/duplicate string list')
    def empty(value,fields):
        for field in fields.split():check(value[field]==[],'no actual memberships, operations, bans, money or secret outcomes')
    def unknown(value,fields):
        for field in fields.split():check(value[field] is None,'leaders, rosters, premises, funds and current conditions stay unknown')
    def payload(ident):
        check(ident in records,'missing owner')
        p=root/f"entities/{records[ident]['type']}/{ident}.md"
        blocks=re.findall(r'^```json\n(.*?)\n```$',p.read_text(),re.M|re.S)
        check(len(blocks)==1,'one owner JSON block required')
        try:d=json.loads(blocks[0],object_pairs_hook=unique_json)
        except ValueError as exc:check(False,'invalid JSON: '+str(exc))
        check(isinstance(d,dict) and type(d.get('schema_version')) is int and d['schema_version']==1,'invalid design schema')
        return d
    def approval(value):
        check(value==APPROVAL,'wrong approval provenance');repository_file(root,value,'guild/underworld approval')
    def ref(ident,kind=None):
        check(isinstance(ident,str) and ident in records and records[ident]['visibility']=='gm-reference', 'invalid/public owner reference')
        check(kind is None or records[ident]['type']==kind,'wrong reference type')
    def place(ident):
        ref(ident,'locations');check(not ident.startswith('route-'),'route is not an organization region or branch context')
    def template(value,fields,list_fields=(),status=False):
        check(isinstance(value,dict) and set(value)==fields,'incomplete agreement/decision/transaction template')
        for key in fields:
            expected='proposed' if status and key=='status' else [] if key in list_fields else None
            check(value[key]==expected and type(value[key]) is type(expected),'populated template implies an unsupported event')
    n=payload('guild-network') if 'guild-network' in records else {}
    active='approved_design_index' in n or bool((set(GUILDS)|set(CRIMINAL)|{'illicit-commerce-design'})&records.keys())
    if not active:return  # Historical trees without the entire approved extension remain valid.
    required=set(GUILDS)|set(CRIMINAL)|INDEPENDENT|{'illicit-commerce-design','continental-guild-concord',
             'guild-membership-and-contracts','guild-network','justice-and-jurisdiction','settlement-trade','settlement-services'}
    check(required<=records.keys(),'incomplete guild/underworld extension')
    check('approved_design_index' in n,'missing approved design routing')
    routing=n['approved_design_index']
    shape(routing,'classification approval_source_ref professional_guild_ids criminal_faction_ids archive_promotions '
          'concord_owner_ref rules_owner_ref illicit_economy_owner_ref activity_owner_ref settlement_links actual_memberships actual_events')
    check(routing['classification']=='APPROVED DESIGN','routing is design only');approval(routing['approval_source_ref'])
    strings(routing['professional_guild_ids']);strings(routing['criminal_faction_ids'])
    check(set(routing['professional_guild_ids'])==set(GUILDS) and set(routing['criminal_faction_ids'])==set(CRIMINAL), 'six-guild/eight-faction routing mismatch')
    check(routing['concord_owner_ref']=='continental-guild-concord' and routing['rules_owner_ref']=='guild-membership-and-contracts'
          and routing['illicit_economy_owner_ref']=='illicit-commerce-design' and routing['activity_owner_ref']=='faction-activity','competing design owner')
    empty(routing,'actual_memberships actual_events')
    archived={o['id']:o for o in n['organizations'] if o['id'].startswith('archived:')}
    check(isinstance(routing['archive_promotions'],list),'archive promotion routing required');seen=set()
    for promotion in routing['archive_promotions']:
        shape(promotion,'archived_id entity_id classification')
        ident=promotion['entity_id'];check(isinstance(ident,str) and ident in GUILDS and ident not in seen,'duplicate/wrong guild promotion')
        seen.add(ident);check(promotion['archived_id']==GUILDS[ident][0] and promotion['archived_id'] in archived
                             and promotion['classification']=='APPROVED DESIGN','archive identity cannot be merged or duplicated')
    check(seen==set(GUILDS),'six archived concepts must be promoted once')
    profiles={}
    for ident in set(GUILDS)|set(CRIMINAL):
        ref(ident,'factions');check(records[ident]['status']=='canon' and APPROVAL in records[ident]['source_refs'], 'design owner provenance mismatch')
        p=payload(ident);shape(p,'schema_version organization_design');d=p['organization_design'];profiles[ident]=d
        check(isinstance(d,dict) and d.get('classification')=='APPROVED DESIGN','organization is design, not current operation')
        approval(d['approval_source_ref']);text(d['name'])
        check(d['autonomy_owner_refs']==AUTONOMY,'use existing autonomy/event owners')
        for owner in d['autonomy_owner_refs']:ref(owner)
        check(d['legal_rules_ref']=='justice-and-jurisdiction','legal owner mismatch')
        if ident in GUILDS:
            shape(d,'classification approval_source_ref kind name archived_design_id association_location_id professions '
                  'governance_design training_and_assessment standards_and_services finite_resources ethics_and_safety '
                  'internal_tensions identity_limits membership_rules_ref legal_rules_ref concord_owner_ref cooperation_candidate_ids '
                  'branch_designs independent compulsory_concord_membership actual_leaders current_member_roster current_premises '
                  'current_funds_cp current_recognition actual_memberships actual_contracts actual_dues_events actual_operations secret_facts autonomy_owner_refs')
            archive,scope=GUILDS[ident]
            check(d['kind']=='professional-guild' and d['archived_design_id']==archive and d['association_location_id']==scope,'guild identity/region mismatch');place(scope)
            normalize=lambda value:re.sub(r'[^a-z0-9]','',value.casefold())
            check(normalize(d['name'])==normalize(archived[archive]['archived_name']),'archived name identity mismatch')
            check(d['membership_rules_ref']=='guild-membership-and-contracts' and d['concord_owner_ref']=='continental-guild-concord','wrong professional rules/Concord owner')
            check(d['independent'] is True and d['compulsory_concord_membership'] is False,'guild independence must be preserved')
            strings(d['professions']);check(bool(d['professions']),'professional scope required')
            for field in ('governance_design','training_and_assessment','standards_and_services','finite_resources','ethics_and_safety','internal_tensions','identity_limits'):text(d[field])
            strings(d['cooperation_candidate_ids']);check(set(d['cooperation_candidate_ids'])<=set(GUILDS)-{ident},'cooperation is prospective professional scope only')
            check(isinstance(d['branch_designs'],list) and d['branch_designs'],'branch proposal required');branches=set()
            for branch in d['branch_designs']:
                shape(branch,'id candidate_context_id classification purpose building_location_id responsible_officer_id route_ids operational_status')
                context=branch['candidate_context_id'];place(context)
                check(branch['id']==ident+':branch-proposal-'+context and branch['id'] not in branches,'duplicate/wrong branch owner');branches.add(branch['id'])
                check(branch['classification']=='PROPOSED' and branch['operational_status']=='UNKNOWN' and branch['route_ids']==[],'branch is not operating or routed');text(branch['purpose'])
                unknown(branch,'building_location_id responsible_officer_id')
            unknown(d,'actual_leaders current_member_roster current_premises current_funds_cp current_recognition')
            empty(d,'actual_memberships actual_contracts actual_dues_events actual_operations secret_facts')
        else:
            shape(d,'classification approval_source_ref kind name scope_kind association_location_id public_identity_design '
                  'criminal_interests recruitment_model hierarchy_model finite_resources operational_limits legitimate_commerce_context '
                  'rival_design_ids rivalry_design lawful_opposition_ids legal_rules_ref legal_response_label internal_tensions '
                  'reputation_design potential_hooks growth_decline_conditions independent_goals current_leaders current_member_roster '
                  'current_safehouses current_informants current_funds_cp current_inventory current_presence current_legal_ban '
                  'actual_crimes actual_operations actual_recruitments actual_transactions actual_bans unsupported_mystery_connections '
                  'secret_facts autonomy_owner_refs magic_owner_refs')
            name,scope=CRIMINAL[ident]
            check(d['kind']=='criminal-faction' and d['name']==name and d['legal_response_label']==name and d['association_location_id']==scope
                  and d['scope_kind']==('regional' if scope else 'transregional'),'criminal faction identity/scope mismatch')
            if scope:place(scope)
            for field in ('public_identity_design','recruitment_model','hierarchy_model','finite_resources','operational_limits',
                          'legitimate_commerce_context','rivalry_design','internal_tensions','reputation_design','potential_hooks',
                          'growth_decline_conditions','independent_goals'):text(d[field])
            strings(d['criminal_interests']);check(bool(d['criminal_interests']),'criminal interest design required')
            strings(d['rival_design_ids']);check(bool(d['rival_design_ids']) and set(d['rival_design_ids'])<=set(CRIMINAL)-{ident},'invalid rivalry scope')
            strings(d['lawful_opposition_ids']);check(bool(d['lawful_opposition_ids']) and set(d['lawful_opposition_ids'])<=set(GUILDS),'opposition does not confer police powers')
            unknown(d,'current_leaders current_member_roster current_safehouses current_informants current_funds_cp current_inventory current_presence current_legal_ban')
            empty(d,'actual_crimes actual_operations actual_recruitments actual_transactions actual_bans unsupported_mystery_connections secret_facts')
            check(d['magic_owner_refs']==(['theron-spells','theron-abilities'] if ident=='nightglass-circle' else []),'no new magic, artifacts or resource authority')
            for owner in d['magic_owner_refs']:ref(owner)
    for ident in CRIMINAL:
        for rival in profiles[ident]['rival_design_ids']:check(ident in profiles[rival]['rival_design_ids'],'rivalry models must be symmetric, not current events')
    law=payload('justice-and-jurisdiction')['approved_legal_design']
    check({r['design_label'] for r in law['organized_crime_responses']}=={v[0] for v in CRIMINAL.values()},'PR3 legal-response identity mismatch')
    settlements=payload('settlement-services')['approved_design_location_ids']
    businesses={};industries={}
    for ident in settlements:
        d=payload(ident)['approved_design'];businesses[ident]={b['id'] for b in d['businesses']};industries[ident]={i['id'] for i in d['industries']}
    trade={t['id']:t for t in payload('settlement-trade')['relationships']}
    check(isinstance(routing['settlement_links'],list),'settlement connections required');seen=set()
    for link in routing['settlement_links']:
        shape(link,'settlement_id classification industry_ids business_ids guild_candidate_ids criminal_pressure_candidate_ids '
              'trade_dependency_ids scope_condition potential_relationships actual_affiliations actual_events')
        ident=link['settlement_id'];check(isinstance(ident,str) and ident in settlements and ident not in seen,'duplicate/wrong settlement connection');seen.add(ident)
        check(link['classification']=='PROPOSED','settlement relationship is not actual pressure or membership')
        for field in ('industry_ids','business_ids','guild_candidate_ids','criminal_pressure_candidate_ids','trade_dependency_ids'):strings(link[field])
        check(set(link['industry_ids'])==industries[ident] and set(link['business_ids'])==businesses[ident],'business/industry owner mismatch')
        check(bool(link['guild_candidate_ids']) and set(link['guild_candidate_ids'])<=set(GUILDS)
              and bool(link['criminal_pressure_candidate_ids']) and set(link['criminal_pressure_candidate_ids'])<=set(CRIMINAL),'invalid guild/pressure candidate')
        for t in link['trade_dependency_ids']:check(t in trade and ident in (trade[t]['origin'],trade[t]['destination']),'unrelated trade dependency')
        for field in ('scope_condition','potential_relationships'):text(link[field])
        empty(link,'actual_affiliations actual_events')
    check(seen==set(settlements),'all ten settlements must retain original owners')
    concord=payload('continental-guild-concord').get('approved_charter')
    shape(concord,'classification approval_source_ref purpose independent_organizations voluntary_membership independent_exit '
          'compulsory_dues treasury_consolidation academy_takeover property_transfer_authority automatic_affiliation governance_model '
          'recognition_and_standards mediation_and_advocacy funding_and_assets academy_safeguard current_members current_delegates '
          'current_treasury_cp actual_enrollments actual_dues_events actual_asset_transfers actual_contracts')
    check(concord['classification']=='APPROVED DESIGN','Concord charter is design only');approval(concord['approval_source_ref'])
    strings(concord['purpose']);strings(concord['independent_organizations']);check(set(concord['independent_organizations'])==INDEPENDENT|set(GUILDS),'independent organization protection mismatch')
    check(concord['voluntary_membership'] is True and concord['independent_exit'] is True,'Concord membership and exit must be voluntary')
    for field in ('compulsory_dues','treasury_consolidation','academy_takeover','property_transfer_authority','automatic_affiliation'):check(concord[field] is False,'no Concord takeover, compulsory fee or automatic affiliation')
    for field in ('governance_model','recognition_and_standards','mediation_and_advocacy','funding_and_assets','academy_safeguard'):text(concord[field])
    check(all(term in concord['academy_safeguard'] for term in ('Theron','Vaeltharion','Beren','cofounder','Dragon Master','No dues','Dragon Slayer')),'academy independence safeguards missing')
    unknown(concord,'current_members current_delegates current_treasury_cp');empty(concord,'actual_enrollments actual_dues_events actual_asset_transfers actual_contracts')
    rules=payload('guild-membership-and-contracts').get('approved_professional_rules')
    shape(rules,'classification approval_source_ref applies_to_guild_ids annual_dues_references dues_scope professional_certification_levels '
          'traveling_member_is_rank automatic_combat_rank_equivalence combat_scale_policy membership_and_elections contract_design_categories '
          'contract_template association_statuses legal_consequences legal_decision_template justice_owner_ref finance_owner_ref autonomy_owner_ref '
          'actual_memberships actual_examinations actual_certifications actual_dues_events actual_legal_bans actual_suspensions actual_contracts actual_hires')
    check(rules['classification']=='APPROVED DESIGN','rules are not actual membership history');approval(rules['approval_source_ref'])
    strings(rules['applies_to_guild_ids']);check(set(rules['applies_to_guild_ids'])==set(GUILDS),'dues cannot apply to independent existing organizations')
    check(isinstance(rules['annual_dues_references'],list),'dues references required');seen=set()
    for due in rules['annual_dues_references']:
        shape(due,'membership amount_cp period kind source_ref');key=due['membership']
        check(isinstance(key,str) and key in DUES and key not in seen,'duplicate/wrong dues category');seen.add(key)
        check(type(due['amount_cp']) is int and due['amount_cp']==DUES[key] and due['period']=='year'
              and due['kind']=='approved-reference','dues are approved annual references, not charges');approval(due['source_ref'])
    check(seen==set(DUES),'four dues categories required')
    check(rules['professional_certification_levels']==['apprentice','journeyman','master'] and rules['traveling_member_is_rank'] is False
          and rules['automatic_combat_rank_equivalence'] is False,'professional rank is distinct from combat power')
    for field in ('dues_scope','combat_scale_policy','legal_consequences'):text(rules[field])
    strings(rules['membership_and_elections']);check(len(rules['membership_and_elections'])>=7,'membership/appeal procedures incomplete')
    strings(rules['contract_design_categories']);check(set(rules['contract_design_categories'])==CONTRACT_KINDS,'prospective contract coverage mismatch')
    template(rules['contract_template'],CONTRACT_TEMPLATE,{'route_or_site_refs','source_refs'},True)
    check(isinstance(rules['association_statuses'],list),'association status policy required');seen=set()
    for status in rules['association_statuses']:
        shape(status,'id classification meaning');ident=status['id']
        check(isinstance(ident,str) and ident in STATUS_CLASSES and ident not in seen and status['classification']=='APPROVED DESIGN','association classification is design, not a ban');seen.add(ident);text(status['meaning'])
    check(seen==STATUS_CLASSES,'five association classes required')
    template(rules['legal_decision_template'],DECISION_TEMPLATE)
    check(rules['justice_owner_ref']=='justice-and-jurisdiction' and rules['finance_owner_ref']=='party-finances'
          and rules['autonomy_owner_ref']=='npc-autonomy-and-time','use existing law, money and autonomy owners')
    empty(rules,'actual_memberships actual_examinations actual_certifications actual_dues_events actual_legal_bans actual_suspensions actual_contracts actual_hires')
    economy=payload('illicit-commerce-design')
    shape(economy,'schema_version classification approval_source_ref finance_ledger_ref finance_owner_ref legal_owner_ref trade_owner_ref '
          'communication_owner_ref contexts transaction_template procedure actual_transactions current_market_locations current_suppliers current_cash_cp automatic_postings')
    check(economy['classification']=='APPROVED DESIGN','illicit commerce design is not actual activity');approval(economy['approval_source_ref'])
    check(economy['finance_ledger_ref']=='state/finance-ledger.json' and economy['finance_owner_ref']=='party-finances'
          and economy['legal_owner_ref']=='justice-and-jurisdiction' and economy['trade_owner_ref']=='settlement-trade'
          and economy['communication_owner_ref']=='settlement-communications','no second ledger or competing route/legal authority')
    check(isinstance(economy['contexts'],list),'illicit contexts required');seen=set()
    for context in economy['contexts']:
        shape(context,'id classification description finite_dependencies current_seller current_buyer current_inventory current_price_cp actual_events')
        ident=context['id'];check(isinstance(ident,str) and ident in {'illicit-context:'+x for x in ILLICIT_CONTEXTS} and ident not in seen,'duplicate/missing illicit context');seen.add(ident)
        check(context['classification']=='PROPOSED','illicit context is not an operating market');text(context['description']);text(context['finite_dependencies'])
        unknown(context,'current_seller current_buyer current_inventory current_price_cp');empty(context,'actual_events')
    check(seen=={'illicit-context:'+x for x in ILLICIT_CONTEXTS},'twelve finite illicit contexts required')
    template(economy['transaction_template'],TRANSACTION_TEMPLATE,{'transport_route_refs','source_refs'},True);text(economy['procedure'])
    empty(economy,'actual_transactions');unknown(economy,'current_market_locations current_suppliers current_cash_cp')
    check(economy['automatic_postings'] is False,'no automatic criminal proceeds or resource postings')
