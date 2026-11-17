"""Read-only approved government/legal design checks; never exercise authority."""
import json
import re

APPROVAL = 'changes/chronicles/phase2-03-government-approval.md'
REALMS = {'valedorn': 'Hereditary monarchy', 'elyndor': 'Circle of Rootwardens',
          'ironhollow-holds': 'Clan confederation', 'rivermere-league': 'Federation of river merchant towns',
          'frostmarch': 'Clan chiefs and seasonal assemblies'}
FIGURES = {'elowen-marcrest': 47, 'cassian-thornmere': 39, 'durnek-stonevein': 132,
           'selene-harrow': 34, 'aveline-hartwell': 54}
FACILITIES = {'proposal:building-'+slug for slug in ('crown-hall', 'central-watchhouse', 'eastrun-gaol',
              'briarfall-gaol', 'blackthorn-gaol', 'stonegate', 'warded-annex')}
OFFENSES = {'theft', 'burglary', 'assault', 'murder', 'fraud', 'forgery', 'bribery-corruption', 'smuggling',
            'extortion', 'illegal-detention', 'kidnapping', 'trafficking', 'property-destruction',
            'illegal-magical-experimentation', 'unlicensed-dangerous-magic', 'unlawful-mining',
            'unlawful-timber', 'contract-fraud', 'cargo-theft', 'organized-crime', 'obstruction'}
BUSINESS_LAWS = {'hospitality', 'gambling', 'adult-entertainment', 'pawnshops', 'markets', 'couriers',
                 'warehouses', 'mercenaries', 'magical-shops', 'healing', 'extraction', 'exploitation'}
CRIME_CONTEXT = {'Gilded Hand', 'Thornless Circle', 'Black Pick Syndicate', 'Sable Current',
                 'Red Antler Brotherhood', 'Veiled Coin Exchange', 'Broken Seal Society', 'Nightglass Circle'}
ACTION_FIELDS = set('action_id action_type status arresting_authority_id sending_authority_id legal_basis subject_ref '
                    'date time location_id custody_officer_id evidence_inventory_ref property_inventory_ref '
                    'receiving_authority_id destination_facility_id receiving_officer_id transport_requirements '
                    'departure_ref arrival_ref transfer_receipt_ref medical_condition review_order_ref '
                    'release_or_disposition_status source_refs'.split())


def validate_governments(root, records, require, repository_file, unique_json):
    def check(condition, message): require(condition, 'governments: '+message)
    def shape(value, fields): check(isinstance(value, dict) and set(value)==set(fields.split()), 'unexpected design fields')
    def text(value): check(isinstance(value, str) and bool(value.strip()), 'text required')
    def strings(value):
        check(isinstance(value, list) and all(isinstance(v, str) and v.strip() for v in value) and
              len(value)==len(set(value)), 'invalid/duplicate string list')
    def payload(ident):
        check(ident in records, 'missing design owner')
        path = root/f"entities/{records[ident]['type']}/{ident}.md"
        blocks = re.findall(r'^```json\n(.*?)\n```$', path.read_text(), re.M|re.S)
        check(len(blocks)==1, 'exactly one owner JSON block required')
        try: return json.loads(blocks[0], object_pairs_hook=unique_json)
        except ValueError as exc: check(False, 'invalid JSON: '+str(exc))
    def approval(value):
        check(value==APPROVAL, 'wrong approval provenance')
        repository_file(root, value, 'government approval')
    def design_owner(ident):
        check(ident in records and records[ident]['status']=='canon' and records[ident]['visibility']=='gm-reference'
              and APPROVAL in records[ident]['source_refs'], 'owner classification/provenance mismatch')
    def empty(value, fields):
        for field in fields.split(): check(value[field]==[], 'no actual appointments, cases, money, politics or secret outcomes')
    def null(value, fields):
        for field in fields.split(): check(value[field] is None, 'current staffing, custody, capacity, location and resources must remain unknown')

    routing = payload('justice-authorities') if 'justice-authorities' in records else {}
    present = 'approved_design_routing' in routing or bool(set(FIGURES)&records.keys())
    if not present:
        for realm in set(REALMS)&records.keys():
            if '"government_design"' in (root/f'entities/locations/{realm}.md').read_text(): present=True
    if not present: return  # Historical trees before this entire extension.
    check(set(REALMS)|set(FIGURES)|{'justice-authorities','justice-proposals','justice-and-jurisdiction'} <= records.keys(),
          'incomplete government extension')
    check('approved_design_routing' in routing, 'missing design routing')
    r = routing['approved_design_routing']
    shape(r, 'classification approval_source_ref realm_ids character_design_ids facility_owner_ref legal_owner_ref '
          'verified_new_authorities actual_appointments')
    check(r['classification']=='APPROVED DESIGN', 'routing cannot establish current authority')
    approval(r['approval_source_ref']); strings(r['realm_ids']); strings(r['character_design_ids'])
    check(set(r['realm_ids'])==set(REALMS) and set(r['character_design_ids'])==set(FIGURES), 'realm/figure routing mismatch')
    check(r['facility_owner_ref']=='justice-proposals' and r['legal_owner_ref']=='justice-and-jurisdiction', 'competing legal/facility owner')
    empty(r, 'verified_new_authorities actual_appointments')
    offices = {}
    for realm, form in REALMS.items():
        design_owner(realm); p=payload(realm)
        shape(p, 'schema_version government_design'); check(type(p['schema_version']) is int and p['schema_version']==1, 'unsupported schema')
        g=p['government_design']
        shape(g, 'classification approval_source_ref realm_id form capital_id selection_and_succession nobility_and_political_rights '
              'taxation_design property_and_inheritance industry_and_labor justice_hierarchy defense_and_emergency_limits '
              'diplomacy corruption_and_oversight legal_owner_ref design_figure_ids offices political_interests '
              'actual_appointments actual_orders actual_political_events current_officeholders current_treaties current_treasury_cp')
        check(g['classification']=='APPROVED DESIGN' and g['realm_id']==realm and g['form']==form, 'wrong realm government/classification')
        approval(g['approval_source_ref'])
        check(g['capital_id']==('caelthorne' if realm=='valedorn' else None), 'unsupported capital assignment')
        check(g['legal_owner_ref']=='justice-and-jurisdiction', 'legal owner mismatch')
        strings(g['design_figure_ids'])
        expected={'valedorn': {'elowen-marcrest','cassian-thornmere'}, 'ironhollow-holds': {'durnek-stonevein'},
                  'rivermere-league': {'selene-harrow'}}.get(realm,set())
        check(set(g['design_figure_ids'])==expected, 'design figure is not a new officeholder')
        for field in ('selection_and_succession','nobility_and_political_rights','taxation_design','property_and_inheritance',
                      'industry_and_labor','justice_hierarchy','defense_and_emergency_limits','diplomacy','corruption_and_oversight'): text(g[field])
        empty(g, 'actual_appointments actual_orders actual_political_events current_treaties')
        null(g, 'current_officeholders current_treasury_cp')
        check(isinstance(g['offices'], list) and g['offices'], 'offices required')
        for o in g['offices']:
            shape(o, 'id name level classification scope_realm_id selection_or_mandate powers_and_limits '
                  'assigned_person_ids current_staffing operational_status')
            ident=o['id']
            check(isinstance(ident,str) and re.fullmatch('government:'+re.escape(realm)+r'-[a-z]+(?:-[a-z]+)*',ident)
                  and ident not in offices, 'duplicate/wrong office scope')
            offices[ident]=o
            check(o['classification']=='APPROVED DESIGN' and o['scope_realm_id']==realm and
                  o['level'] in ('local','regional','realm'), 'office has no cross-realm authority')
            for field in ('name','selection_or_mandate','powers_and_limits'): text(o[field])
            empty(o, 'assigned_person_ids'); null(o, 'current_staffing')
            check(o['operational_status']=='UNKNOWN', 'office design does not certify operations')
        check({o['level'] for o in g['offices']}=={'local','regional','realm'}, 'three-level justice/government design required')
        check(isinstance(g['political_interests'],list) and g['political_interests'], 'finite political interests required')
        for interest in g['political_interests']:
            shape(interest, 'label goals finite_resources classification active_events')
            check(interest['classification']=='APPROVED DESIGN', 'political interest is design only')
            for field in ('label','goals','finite_resources'): text(interest[field])
            empty(interest, 'active_events')
    for ident, age in FIGURES.items():
        design_owner(ident);p=payload(ident);shape(p, 'schema_version character_design')
        check(type(p['schema_version']) is int and p['schema_version']==1, 'unsupported character schema')
        c=p['character_design']
        shape(c, 'classification approval_source_ref age role_design background_design appearance_design personality goals '
              'loyalties relationships_design responsibilities_and_limits public_reputation_design potential_conflicts '
              'existing_proposal_id current_location current_office_id actual_appointments historical_decisions meetings_with_theron secret_facts')
        check(c['classification']=='APPROVED DESIGN' and type(c['age']) is int and c['age']==age, 'character age/design mismatch')
        approval(c['approval_source_ref'])
        check(c['existing_proposal_id']==('proposal:officer-aveline-hartwell' if ident=='aveline-hartwell' else None), 'duplicate/proposed identity mismatch')
        for field in ('role_design','background_design','appearance_design','personality','goals','loyalties',
                      'relationships_design','responsibilities_and_limits','public_reputation_design','potential_conflicts'): text(c[field])
        null(c, 'current_location current_office_id'); empty(c, 'actual_appointments historical_decisions meetings_with_theron secret_facts')
    proposals=payload('justice-proposals')
    alias=next((o for o in proposals['officers'] if o['id']=='proposal:officer-aveline-hartwell'),None)
    check(alias is not None and alias['existing_character_id']=='aveline-hartwell' and alias['candidate_office_id'] is None,
          'Aveline identity must reuse proposal without appointment')
    check(isinstance(proposals.get('approved_facility_designs'),list), 'missing seven facility designs')
    seen=set(); old={b['id']:b for b in proposals['buildings']}
    for f in proposals['approved_facility_designs']:
        shape(f, 'proposal_id classification approval_source_ref candidate_location_id governing_design_authority_id '
              'court_design_authority_id jurisdiction_condition purpose prisoner_classification staffing_roles security_design '
              'intake_release custody_documentation medical_and_conditions transport_requirements inspection_and_oversight '
              'emergency_procedures capacity_limits actual_governing_authority_id responsible_officer_id current_staffing '
              'exact_capacity current_prisoners operational_status actual_transfers actual_intakes')
        ident=f['proposal_id']
        check(isinstance(ident,str) and ident in FACILITIES and ident not in seen, 'duplicate/wrong facility proposal identity')
        seen.add(ident);check(f['classification']=='APPROVED DESIGN', 'facility approval is design, not operating status')
        approval(f['approval_source_ref'])
        check(f['candidate_location_id']==old[ident]['candidate_location_id'], 'facility location was not surveyed/relocated')
        for field in ('governing_design_authority_id','court_design_authority_id'):
            target=f[field]
            check(isinstance(target,str) and target in offices and target.startswith('government:valedorn-'), 'broken facility authority/court model')
        check(f['court_design_authority_id'] in {'government:valedorn-regional-courts', 'government:valedorn-high-court'},
              'facility court must be a judicial design role')
        expected_governor = 'government:valedorn-high-court' if ident == 'proposal:building-crown-hall' else \
                            'government:valedorn-watch' if ident == 'proposal:building-central-watchhouse' else \
                            'government:valedorn-custody-service'
        check(f['governing_design_authority_id'] == expected_governor, 'wrong facility governing role')
        for field in ('jurisdiction_condition','purpose','prisoner_classification','security_design','intake_release',
                      'custody_documentation','medical_and_conditions','transport_requirements','inspection_and_oversight',
                      'emergency_procedures','capacity_limits'): text(f[field])
        strings(f['staffing_roles']); check(bool(f['staffing_roles']), 'staffing design required')
        null(f, 'actual_governing_authority_id responsible_officer_id current_staffing exact_capacity current_prisoners')
        empty(f, 'actual_transfers actual_intakes');check(f['operational_status']=='UNKNOWN', 'proposed facility cannot receive prisoners')
    check(seen==FACILITIES, 'seven-facility coverage mismatch')
    legal=payload('justice-and-jurisdiction').get('approved_legal_design')
    shape(legal, 'classification approval_source_ref realm_ids exclusive_cross_realm_court historical_authority_owner_ref '
          'custody_owner_ref finance_owner_ref court_levels jurisdiction_policy proof_standards process_steps offenses '
          'business_regulations business_links organized_crime_responses oversight rank_and_capture_limits action_template '
          'actual_arrests actual_transfers actual_judgments actual_tax_fine_or_fee_events actual_political_events automatic_outcomes')
    approval(legal['approval_source_ref']);strings(legal['realm_ids'])
    check(legal['classification']=='APPROVED DESIGN' and set(legal['realm_ids'])==set(REALMS) and
          legal['exclusive_cross_realm_court'] is False, 'no universal court/current legal power')
    check(legal['historical_authority_owner_ref']=='justice-authorities' and legal['custody_owner_ref']=='prisoner-custody'
          and legal['finance_owner_ref']=='party-finances', 'competing authority, custody or finance owner')
    check(legal['court_levels']==['local','regional','realm'], 'justice hierarchy mismatch')
    text(legal['jurisdiction_policy']);text(legal['rank_and_capture_limits'])
    shape(legal['proof_standards'], 'investigation search_arrest civil criminal serious_penalty')
    for value in legal['proof_standards'].values():text(value)
    strings(legal['process_steps']); check(len(legal['process_steps'])>=8, 'court/appeal process incomplete')
    check(isinstance(legal['offenses'],list), 'offense code required')
    seen_offenses=set()
    for o in legal['offenses']:
        shape(o, 'id classification conduct offense_class evidence_requirements realm_treatment sanctions appeal_and_limits actual_cases')
        ident=o['id'];check(isinstance(ident,str) and ident.startswith('offense:') and ident[8:] in OFFENSES and ident not in seen_offenses, 'offense coverage/duplicate mismatch')
        seen_offenses.add(ident);check(o['classification']=='APPROVED DESIGN', 'offense is not a historical conviction')
        for field in ('conduct','offense_class','evidence_requirements','sanctions','appeal_and_limits'):text(o[field])
        check(isinstance(o['realm_treatment'],list), 'realm-specific offense treatment required')
        scoped=set()
        for treatment in o['realm_treatment']:
            shape(treatment, 'realm_id investigation_authority_id trial_authority_id local_trial_authority_id appeal_authority_id local_variation')
            realm=treatment['realm_id'];check(isinstance(realm,str) and realm in REALMS and realm not in scoped, 'duplicate/wrong offense realm')
            scoped.add(realm)
            for field,slug in [('investigation_authority_id','watch'),('trial_authority_id','regional-courts'),('local_trial_authority_id','local-courts'),('appeal_authority_id','high-court')]:
                target=treatment[field];check(isinstance(target,str) and target in offices and target=='government:'+realm+'-'+slug, 'court/investigator scope mismatch')
            text(treatment['local_variation'])
        check(scoped==set(REALMS), 'offense must distinguish all five realms');empty(o, 'actual_cases')
    check(seen_offenses=={'offense:'+x for x in OFFENSES}, 'criminal code coverage mismatch')
    rules={}
    check(isinstance(legal['business_regulations'],list), 'business law required')
    for rule in legal['business_regulations']:
        shape(rule, 'id name classification categories realm_statuses compliance current_licenses actual_enforcement_events')
        ident=rule['id'];check(isinstance(ident,str) and ident in {'business-law:'+x for x in BUSINESS_LAWS} and ident not in rules, 'duplicate/missing business law')
        rules[ident]=rule;check(rule['classification']=='APPROVED DESIGN', 'business rule is not a license')
        text(rule['name']);text(rule['compliance']);strings(rule['categories'])
        check(isinstance(rule['realm_statuses'],list), 'realm business status required');scoped=set()
        for status in rule['realm_statuses']:
            shape(status, 'realm_id design_status qualification')
            realm=status['realm_id'];check(isinstance(realm,str) and realm in REALMS and realm not in scoped, 'duplicate/wrong business realm')
            scoped.add(realm);check(status['design_status'] in ('LAWFUL','REGULATED','TOLERATED','PROHIBITED'), 'invalid business legal classification');text(status['qualification'])
        check(scoped==set(REALMS), 'business law must distinguish five realms');empty(rule, 'current_licenses actual_enforcement_events')
    check(set(rules)=={'business-law:'+x for x in BUSINESS_LAWS}, 'business law coverage mismatch')
    worker=rules['business-law:adult-entertainment']['compliance']
    check(all(term in worker for term in ('consenting adults','independent agency','earnings','documents','boundaries','refuse','leave','Coercion','confinement','trafficking','debt bondage','violence')), 'adult-worker independence safeguards missing')
    expected_businesses={}
    for ident in payload('settlement-services')['approved_design_location_ids']:
        for b in payload(ident)['approved_design']['businesses']:expected_businesses[b['id']]=ident
    check(isinstance(legal['business_links'],list), 'business law routing required');seen=set()
    for link in legal['business_links']:
        shape(link, 'business_id parent_location_id regulation_ids actual_legal_status actual_license jurisdiction_verified')
        ident=link['business_id'];check(isinstance(ident,str) and ident in expected_businesses and ident not in seen and
                                     link['parent_location_id']==expected_businesses[ident], 'business owner/duplicate mismatch')
        seen.add(ident);strings(link['regulation_ids']);check(bool(link['regulation_ids']) and set(link['regulation_ids'])<=rules.keys(), 'broken regulation reference')
        null(link, 'actual_legal_status actual_license');check(link['jurisdiction_verified'] is False, 'business design does not verify jurisdiction/license')
    check(seen==set(expected_businesses), 'PR2 business coverage mismatch')
    check(isinstance(legal['organized_crime_responses'],list), 'legal response context required');seen=set()
    for response in legal['organized_crime_responses']:
        shape(response, 'design_label scope investigative_focus required_safeguards actual_investigations secret_connections')
        label=response['design_label'];check(isinstance(label,str) and label in CRIME_CONTEXT and label not in seen, 'crime context coverage mismatch')
        seen.add(label)
        for field in ('scope','investigative_focus','required_safeguards'):text(response[field])
        empty(response, 'actual_investigations secret_connections')
    check(seen==CRIME_CONTEXT, 'eight criminal labels required without faction profiles')
    shape(legal['oversight'], 'investigation financial_fraud cross_jurisdiction witnesses_informants official_misconduct wrongful_conviction')
    for value in legal['oversight'].values():text(value)
    a=legal['action_template'];check(isinstance(a,dict) and set(a)==ACTION_FIELDS, 'incomplete arrest/transfer intake template')
    for field in ACTION_FIELDS:
        expected='proposed' if field=='status' else [] if field=='source_refs' else None
        check(a[field]==expected and type(a[field]) is type(expected), 'action template cannot imply actual custody/outcomes')
    empty(legal, 'actual_arrests actual_transfers actual_judgments actual_tax_fine_or_fee_events actual_political_events')
    check(legal['automatic_outcomes'] is False, 'no automatic political/legal outcomes')
