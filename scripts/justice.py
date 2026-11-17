"""Read-only justice reference checks and prospective transfer completeness validation."""
import json
import re

CUSTODY_MARKER = '\n## Justice workflow and source routing — Chunk 4\n'
STAGES = ['apprehended','awaiting-transport','in-transit','received-at-station','booked',
          'awaiting-judicial-review','released','remanded','transferred','convicted','sentenced',
          'final-disposition-recorded']
TRANSFER_FIELDS = {'case_id','prisoner_id','status','sending_authority_id','receiving_authority_id',
                   'destination_facility_id','legal_basis','departure_ref','arrival_ref','receiving_officer_id',
                   'custody_receipt_ref','evidence_inventory_ref','property_inventory_ref','source_refs'}
EVIDENCE_FIELDS = {'evidence_id','original_owner_id','seizing_person_id','seizure_date','custodian_id',
                   'storage_location_id','transfer_history','legal_restrictions','current_disposition','source_refs'}


def validate_transfer(record, root, records, authorities, facilities, require, repository_file):
    """Validate a prospective event, never perform transport or mutate custody.

    Called directly by tests; Chunk4 creates no actual transfer records. Existence of
    a cited file is not independent proof of a handover or legal competence.
    """
    require(isinstance(record, dict) and set(record) == TRANSFER_FIELDS, 'justice transfer: invalid fields')
    require(isinstance(record['case_id'], str) and bool(record['case_id'].strip()), 'justice transfer: stable case ID required')
    status = record['status']
    require(status in ('planned','in-transit','completed'), 'justice transfer: invalid status')
    for field in ('prisoner_id','receiving_officer_id'):
        ident = record[field]
        if ident is not None:
            require(isinstance(ident, str) and ident in records and records[ident]['type']=='characters',
                    'justice transfer: invalid person/officer reference')
    for field in ('sending_authority_id','receiving_authority_id'):
        ident = record[field]
        require(ident is None or isinstance(ident, str) and ident in authorities, 'justice transfer: invalid authority reference')
    facility_id = record['destination_facility_id']
    require(facility_id is None or isinstance(facility_id, str) and facility_id in facilities,
            'justice transfer: invalid destination reference')
    refs = record['source_refs']
    require(isinstance(refs, list) and all(isinstance(x, str) for x in refs) and len(refs)==len(set(refs)),
            'justice transfer: invalid source references')
    for ref in refs:
        repository_file(root, ref, 'transfer source')
    source_fields = ('departure_ref','arrival_ref','custody_receipt_ref','evidence_inventory_ref','property_inventory_ref')
    for field in source_fields:
        if record[field] is not None:
            require(record[field] in refs, 'justice transfer: undeclared event/inventory source')
            repository_file(root, record[field], field)
    if status == 'planned':
        require(all(record[f] is None for f in ('departure_ref','arrival_ref','custody_receipt_ref')),
                'justice transfer: a plan cannot claim departure, arrival or receipt')
        return
    require(all(record[f] is not None for f in ('sending_authority_id','receiving_authority_id','destination_facility_id')),
            'justice transfer: verified authorities and destination required')
    require(all(authorities[record[f]]['classification']=='CONFIRMED CANON' for f in ('sending_authority_id','receiving_authority_id')),
            'justice transfer: proposed authority cannot conduct actual transfer')
    facility = facilities[facility_id]
    require(facility['classification']=='CONFIRMED CANON' and facility['operational_status']=='OPERATIONAL',
            'justice transfer: proposed/nonoperational facility cannot receive prisoner')
    require(facility['operating_authority_id']==record['receiving_authority_id'], 'justice transfer: receiving authority mismatch')
    require(isinstance(record['legal_basis'], str) and bool(record['legal_basis'].strip()), 'justice transfer: legal basis required')
    require(record['departure_ref'] is not None, 'justice transfer: actual departure source required')
    if status == 'in-transit':
        require(record['arrival_ref'] is None and record['custody_receipt_ref'] is None,
                'justice transfer: transit cannot claim arrival or receipt')
        return
    require(record['receiving_officer_id'] is not None, 'justice transfer: receiving officer required')
    require(all(record[f] is not None for f in source_fields),
            'justice transfer: completed transfer needs departure, arrival, receipt and both inventories')
    require(bool(refs), 'justice transfer: completed handover source required')


def validate_justice(root, records, require, repository_file, unique_json):
    expected = {'justice-authorities','justice-proposals','justice-road-links','justice-and-jurisdiction'}
    custody_path = root/'entities/mechanics/prisoner-custody.md'
    marked = custody_path.is_file() and CUSTODY_MARKER in custody_path.read_text()
    if not (expected & records.keys() or marked):
        return
    require(expected <= records.keys() and marked, 'justice: incomplete justice/custody framework')

    def shape(value, fields, label):
        expected_fields = set(fields.split())
        optional = {'authority registry': 'approved_design_routing', 'proposals': 'approved_facility_designs',
                    'workflow rules': 'approved_legal_design'}
        if isinstance(value, dict) and optional.get(label) in value:
            expected_fields.add(optional[label])
        require(isinstance(value, dict) and set(value)==expected_fields, f'justice: invalid {label} fields')

    def text(value, label):
        require(isinstance(value, str) and value.strip(), f'justice: invalid {label}')

    def strings(values, label):
        require(isinstance(values, list) and all(isinstance(x, str) and x.strip() for x in values), f'justice: invalid {label}')
        require(len(values)==len(set(values)), f'justice: duplicate {label}')

    def reference(ident, types=None):
        require(isinstance(ident, str) and ident in records, 'justice: broken entity reference')
        require(records[ident]['visibility']=='gm-reference', 'justice: secret reference forbidden in public view')
        require(types is None or records[ident]['type'] in types, 'justice: wrong reference type')

    def location(ident):
        reference(ident, {'locations'})
        require(not ident.startswith('route-'), 'justice: road is not a building/territory')

    def refs(values):
        strings(values, 'source refs')
        require(values, 'justice: source references required')
        for value in values:
            # Source pointers do not disclose source contents, but must not point to locked-secret entities.
            if value.startswith('entities/'):
                target = value.rsplit('/',1)[-1].removesuffix('.md')
                reference(target)
            repository_file(root, value, 'justice source')

    def payload(ident, section=False):
        record = records[ident]
        path = root/f"entities/{record['type']}/{ident}.md"
        content = path.read_text()
        if section:
            require(content.count(CUSTODY_MARKER)==1, 'justice: duplicate custody workflow')
            content = content.split(CUSTODY_MARKER)[1]
        blocks = re.findall(r'^```json\n(.*?)\n```$',content,re.M|re.S)
        require(len(blocks)==1, 'justice: expected one JSON block')
        try:
            data = json.loads(blocks[0],object_pairs_hook=unique_json)
        except ValueError as exc:
            require(False, f'justice: invalid JSON: {exc}')
        require(isinstance(data, dict) and type(data.get('schema_version')) is int and data['schema_version']==1,
                'justice: unsupported schema')
        return data

    data = payload('justice-authorities')
    shape(data, 'schema_version authorities protected_official_ids verified_receiving_facilities automatic_custody_actions', 'authority registry')
    require(data['automatic_custody_actions'] is False, 'justice: automatic custody actions forbidden')
    require(data['verified_receiving_facilities']==[], 'justice: no new operational receiving facility verified')
    strings(data['protected_official_ids'], 'protected officials')
    require(set(data['protected_official_ids'])=={'mara-vey','aldric-voss','ressa-vale','elsbeth-marrin'},
            'justice: existing officials must remain distinct')
    for ident in data['protected_official_ids']:
        reference(ident, {'characters'})
    require(isinstance(data['authorities'], list), 'justice: invalid authorities')
    authorities = {}
    kinds = {'judicial','civilian-law-enforcement','civil-government','military-watch','guild-contractual','private-security'}
    for a in data['authorities']:
        shape(a, 'id name classification authority_kind government_affiliation jurisdiction_location_ids jurisdiction_boundary '
              'legal_powers limitations leadership_ids headquarters_location_id subordinate_station_ids court_relationship_ids '
              'prison_relationship_ids cross_border_agreements source_refs evidence', 'authority')
        ident = a['id']
        text(ident, 'authority ID')
        require(ident.startswith('justice:') and ident not in authorities, 'justice: duplicate/invalid authority ID')
        authorities[ident] = a
        require(a['classification']=='CONFIRMED CANON' and a['authority_kind'] in kinds, 'justice: invalid existing authority classification/kind')
        for f in ('name','government_affiliation'):
            text(a[f], f)
        for f in ('legal_powers','limitations','jurisdiction_location_ids','leadership_ids'):
            strings(a[f], f)
        for place in a['jurisdiction_location_ids']:
            location(place)
            require(records[place]['status']!='research', 'justice: canonical jurisdiction through proposed location')
        for person in a['leadership_ids']:
            reference(person, {'characters'})
        require(a['jurisdiction_boundary'] is None, 'justice: no precise jurisdiction boundary established')
        require(a['headquarters_location_id'] is None and a['subordinate_station_ids']==[] and a['prison_relationship_ids']==[]
                and a['court_relationship_ids']==[] and a['cross_border_agreements']==[],
                'justice: unsupplied station/court/prison/agreement assertion')
        refs(a['source_refs'])
        require(isinstance(a['evidence'], list) and a['evidence'], 'justice: authority evidence required')
        for e in a['evidence']:
            shape(e, 'source_ref quote', 'authority evidence')
            require(e['source_ref'] in a['source_refs'], 'justice: undeclared authority source')
            text(e['quote'], 'evidence quote')
            require(e['quote'] in repository_file(root,e['source_ref'],'authority evidence').read_text(),
                    'justice: authority quote not found')
    require(set(authorities)=={'justice:caelthorne-magistrates','justice:caelthorne-watch','justice:brackenford-government',
                              'justice:brackenford-watch','justice:blackthorn-command','justice:wayfarers-contracts','justice:ashvale-private-security'},
            'justice: new authority requires sourced review')
    require(authorities['justice:brackenford-government']['leadership_ids']==['elsbeth-marrin']
            and authorities['justice:brackenford-watch']['leadership_ids']==['ressa-vale'], 'justice: village authority changed')

    require(authorities['justice:blackthorn-command']['authority_kind']=='military-watch'
            and authorities['justice:wayfarers-contracts']['authority_kind']=='guild-contractual'
            and authorities['justice:ashvale-private-security']['authority_kind']=='private-security',
            'justice: military/guild/private roles cannot become civilian judicial power')
    proposals = payload('justice-proposals')
    shape(proposals, 'schema_version classification roles buildings officers other_approval_items automatic_custody_actions', 'proposals')
    require(records['justice-proposals']['status']=='research' and proposals['classification']=='PROPOSED', 'justice: proposals cannot become canon')
    require(proposals['automatic_custody_actions'] is False, 'justice: automatic custody actions forbidden')
    proposal_ids = set()
    def proposal(p):
        text(p['id'], 'proposal ID')
        require(p['id'].startswith('proposal:') and p['id'] not in proposal_ids, 'justice: duplicate proposal ID')
        proposal_ids.add(p['id'])
        require(p['classification']=='PROPOSED' and p['approval_status']=='REQUIRES APPROVAL' and p['approval_source_ref'] is None,
                'justice: proposal approval/canon cannot be fabricated')
        refs(p['source_refs'])
    for field, count in (('roles',7),('buildings',12),('officers',16),('other_approval_items',5)):
        require(isinstance(proposals[field], list) and len(proposals[field])==count, 'justice: incomplete proposal crosswalk')
    for p in proposals['roles']:
        shape(p, 'id name classification proposed_purpose government_affiliation jurisdiction_location_ids legal_powers limitations '
              'leadership_ids headquarters_location_id subordinate_station_ids court_relationship_ids prison_relationship_ids '
              'cross_border_agreements existing_equivalent_ids approval_status approval_source_ref source_refs', 'proposed role')
        proposal(p)
        for f in ('name','proposed_purpose','government_affiliation','limitations'):
            text(p[f], f)
        require(all(p[f]==[] for f in ('jurisdiction_location_ids','leadership_ids','subordinate_station_ids','court_relationship_ids',
                                      'prison_relationship_ids','cross_border_agreements')) and p['legal_powers'] is None
                and p['headquarters_location_id'] is None, 'justice: proposed role has no approved reach/appointments')
        strings(p['existing_equivalent_ids'], 'equivalent authority IDs')
        require(set(p['existing_equivalent_ids'])<=authorities.keys(), 'justice: broken equivalent authority')
    facilities = {}
    for p in proposals['buildings']:
        shape(p, 'id name classification candidate_location_id location_entity_id building_kind detention_type operating_authority_id '
              'responsible_officer_id capacity security_arrangements medical_access court_authority_id transfer_rules operational_status '
              'reconciliation_authority_ids reconciliation_note approval_status approval_source_ref source_refs', 'building proposal')
        proposal(p)
        facilities[p['id']] = p
        for f in ('name','building_kind','reconciliation_note'):
            text(p[f], f)
        if p['candidate_location_id'] is not None:
            location(p['candidate_location_id'])
            require(records[p['candidate_location_id']]['status']!='research', 'justice: unsupported candidate geography')
        if p['id'] in ('proposal:building-stonegate','proposal:building-warded-annex'):
            require(p['candidate_location_id'] is None, 'justice: no geography supplied for unlocated prison')
        require(p['detention_type'] is None or type(p['detention_type']) is int and 1<=p['detention_type']<=4,
                'justice: invalid detention type')
        require(all(p[f] is None for f in ('location_entity_id','operating_authority_id','responsible_officer_id','capacity',
                                          'security_arrangements','medical_access','court_authority_id','transfer_rules'))
                and p['operational_status']=='PROPOSED — NOT OPERATIONAL', 'justice: proposed prison cannot be staffed or operational')
        strings(p['reconciliation_authority_ids'], 'reconciliation authority IDs')
        require(set(p['reconciliation_authority_ids'])<=authorities.keys(), 'justice: invalid building authority reference')
    names = set()
    for p in proposals['officers']:
        shape(p, 'id name classification existing_character_id candidate_office_id identity_review_ids identity_review relationships_to_theron '
              'approval_status approval_source_ref source_refs', 'officer proposal')
        proposal(p)
        text(p['name'], 'officer name')
        require(p['name'].casefold() not in names, 'justice: duplicate proposed official name')
        names.add(p['name'].casefold())
        parts = re.findall(r'[a-z]+',p['name'].casefold())
        rank_words = {'chief','justice','captain','commander','warden','marshal','magister','magistrate','judge'}
        full_name_id = '-'.join(part for part in parts if part not in rank_words)
        approved_identity = (p['id'] == 'proposal:officer-aveline-hartwell' and
                             full_name_id == p['existing_character_id'] == 'aveline-hartwell' and
                             'changes/chronicles/phase2-03-government-approval.md' in p['source_refs'] and
                             full_name_id in records and records[full_name_id]['type'] == 'characters')
        require(full_name_id not in records or records[full_name_id]['type']!='characters' or approved_identity,
                'justice: proposed official duplicates an established name; review identity first')
        require((p['existing_character_id'] is None or approved_identity) and p['candidate_office_id'] is None and p['relationships_to_theron'] is None,
                'justice: proposed official identity/appointment/relationship not established')
        strings(p['identity_review_ids'], 'identity review IDs')
        for ident in p['identity_review_ids']:
            reference(ident, {'characters'})
        text(p['identity_review'], 'identity review')
    for p in proposals['other_approval_items']:
        shape(p, 'id subject classification approval_status approval_source_ref source_refs', 'approval item')
        proposal(p)
        text(p['subject'], 'approval subject')

    road_data = payload('justice-road-links')
    shape(road_data, 'schema_version roads automatic_transport', 'road map')
    require(road_data['automatic_transport'] is False, 'justice: automatic transport forbidden')
    require(isinstance(road_data['roads'], list), 'justice: invalid roads')
    seen = set()
    for road in road_data['roads']:
        shape(road, 'route_id region_id responsible_authority_id nearest_station_location_id court_authority_id remand_facility_id '
              'endpoint_contacts source_refs note', 'road authority link')
        ident = road['route_id']
        reference(ident, {'locations'})
        require(ident.startswith('route-') and ident not in seen, 'justice: duplicate/invalid road ID')
        seen.add(ident)
        owner = payload(ident)
        require(owner['patrol_jurisdiction'] is None, 'justice: source changed; reconcile road jurisdiction explicitly')
        require(all(road[f] is None for f in ('region_id','responsible_authority_id','nearest_station_location_id','court_authority_id','remand_facility_id')),
                'justice: endpoint proximity does not establish patrol/court/prison jurisdiction')
        refs(road['source_refs'])
        text(road['note'], 'road note')
        require(isinstance(road['endpoint_contacts'], list), 'justice: invalid endpoint contacts')
        contacts = set()
        for c in road['endpoint_contacts']:
            shape(c, 'location_id authority_id', 'endpoint contact')
            require(isinstance(c['authority_id'], str) and c['authority_id'] in authorities, 'justice: invalid endpoint authority')
            location(c['location_id'])
            require(c['location_id'] in (owner['start'],owner['destination'])
                    and c['location_id'] in authorities[c['authority_id']]['jurisdiction_location_ids'],
                    'justice: authority is not a sourced endpoint contact')
            key = (c['location_id'],c['authority_id'])
            require(key not in contacts, 'justice: duplicate endpoint contact')
            contacts.add(key)
    require(seen=={i for i in records if i.startswith('route-')}, 'justice: road lookup coverage mismatch')

    rules = payload('justice-and-jurisdiction')
    shape(rules, 'schema_version workflow_stages legal_process_classification detention_types transfer_fields evidence_fields automatic_custody_actions', 'workflow rules')
    require(rules['workflow_stages']==STAGES, 'justice: workflow stages changed')
    require(rules['legal_process_classification']=='PROPOSED', 'justice: proposed process is not enacted law')
    require(rules['automatic_custody_actions'] is False, 'justice: automatic custody actions forbidden')
    strings(rules['transfer_fields'], 'transfer fields')
    strings(rules['evidence_fields'], 'evidence fields')
    require(set(rules['transfer_fields'])==TRANSFER_FIELDS and set(rules['evidence_fields'])==EVIDENCE_FIELDS,
            'justice: incomplete transfer/evidence schema')
    require(isinstance(rules['detention_types'], list) and len(rules['detention_types'])==4, 'justice: four detention types required')
    for n,t in enumerate(rules['detention_types'],1):
        shape(t, 'type classification label', 'detention type')
        require(type(t['type']) is int and t['type']==n and t['classification']=='PROPOSED', 'justice: invalid detention taxonomy')
        text(t['label'], 'detention type label')
    custody = payload('prisoner-custody',section=True)
    shape(custody, 'schema_version workflow_ref history_routing evidence_owner_refs new_case_records new_transfer_records '
          'new_evidence_records automatic_custody_actions', 'custody extension')
    require(custody['workflow_ref']=='justice-and-jurisdiction', 'justice: custody must use shared workflow owner')
    require(custody['automatic_custody_actions'] is False, 'justice: automatic custody actions forbidden')
    require(all(custody[f]==[] for f in ('new_case_records','new_transfer_records','new_evidence_records')),
            'justice: maintenance cannot add case outcomes, transfers or evidence ownership')
    strings(custody['evidence_owner_refs'], 'evidence owners')
    require(set(custody['evidence_owner_refs'])=={'seven-bells-inventory','shady-salvage','launder','party-finances'},
            'justice: existing evidence/finance owners required')
    for ident in custody['evidence_owner_refs']:
        reference(ident, {'mechanics'})
    seen_history = set()
    require(isinstance(custody['history_routing'], list), 'justice: invalid source routing')
    for h in custody['history_routing']:
        shape(h, 'id scope source_refs note', 'history pointer')
        text(h['id'], 'history pointer ID')
        require(h['id'] not in seen_history, 'justice: duplicate custody source pointer')
        seen_history.add(h['id'])
        require(h['scope'] in ('historical','later-source','identity-gap','non-detention-reference'), 'justice: invalid historical scope')
        refs(h['source_refs'])
        text(h['note'], 'history note')
