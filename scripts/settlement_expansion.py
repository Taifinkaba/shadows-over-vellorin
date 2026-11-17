"""Read-only Phase 2 settlement, trade and message-design validation.

Settlement facts live in their location owner; this module creates no events or state.
"""
import json
import re

APPROVAL = 'changes/chronicles/phase2-02-settlement-approval.md'
POPULATIONS = {'caelthorne': 38000, 'eastrun': 4800, 'briarfall-crossing': 1650,
               'rivermere': 12000, 'ironhollow-hold': 9200, 'brackenford': 180,
               'silverbrook': 620, 'stoneford': 940, 'southbank-landing': 2300,
               'windmere': 310}
NEW_LOCATIONS = {'silverbrook', 'stoneford', 'southbank-landing', 'windmere'}
HELPERS = {'settlement-trade', 'settlement-communications'}
LEGAL = {'lawful-design', 'regulated-design', 'tolerated-design', 'prohibited-design'}
METHODS = {'mounted-courier', 'guild-messenger', 'caravan-post', 'river-dispatch',
           'beacon-signal', 'limited-magic'}
PRICES = {'simple-bed': (50, 50, 'night'), 'private-room': (100, 100, 'night'),
          'hot-meal': (20, 20, 'meal'), 'horse-feed': (30, 30, 'day'),
          'rations': (50, 50, 'day'), 'healing-herbs': (80, 80, 'bundle'),
          'rope': (100, 100, '50 feet'), 'iron-sword': (800, 800, 'sword'),
          'wagon-hire': (80, 80, 'day'), 'farm-labor': (20, 20, 'day'),
          'caravan-guard': (50, 50, 'day'), 'skilled-blacksmith': (60, 60, 'day'),
          'experienced-healer': (80, 80, 'day'), 'master-artisan': (100, 200, 'day')}
MESSAGE_FIELDS = set('id sender recipient carrier method departure_date departure_time origin destination '
                     'intended_route_ids delivery_fee_cp estimated_delivery_window actual_delivery_status '
                     'receipt_evidence dispatch_evidence spell_rule_ref resource_evidence source_ref'.split())


def validate_dispatch(message, route_lookup, require):
    """Validate a supplied future dispatch shape; never send, deliver, price or write it.

    Source/evidence truth, current route conditions, permissions and spell limits still
    require the existing owner/chronicle procedure. Presence of text proves none of them.
    """
    def text(value):
        return isinstance(value, str) and bool(value.strip())

    require(isinstance(message, dict) and set(message) == MESSAGE_FIELDS,
            'postal: invalid message fields')
    require(message['method'] in METHODS, 'postal: unsupported method')
    status = message['actual_delivery_status']
    require(status in {'proposed', 'sent', 'delivered', 'acknowledged', 'delayed', 'lost', 'refused'},
            'postal: invalid delivery status')
    window = message['estimated_delivery_window']
    require(isinstance(window, dict) and set(window) == {'earliest', 'latest', 'basis'},
            'postal: invalid delivery window')
    require(all(v is None or text(v) for v in window.values()), 'postal: invalid window value')
    fee = message['delivery_fee_cp']
    require(fee is None or type(fee) is int and fee >= 0, 'postal: invalid fee')
    routes = message['intended_route_ids']
    require(isinstance(routes, list) and all(text(r) and r in route_lookup for r in routes)
            and len(routes) == len(set(routes)), 'postal: unknown/duplicate route')
    for field in ('receipt_evidence', 'dispatch_evidence', 'resource_evidence'):
        require(isinstance(message[field], list), 'postal: invalid evidence list')
        for evidence in message[field]:
            require(isinstance(evidence, dict) and set(evidence) == {'source_ref', 'quote', 'date'}
                    and all(text(x) for x in evidence.values()), 'postal: dated source evidence required')
    if status != 'proposed':
        require(all(text(message[k]) for k in ('id', 'sender', 'recipient', 'carrier', 'departure_date',
                                              'departure_time', 'origin', 'destination', 'source_ref')),
                'postal: actual dispatch requires sender/recipient/carrier/departure/source')
        require(bool(re.fullmatch(r'Year \d+ Day \d+', message['departure_date'])) and
                bool(re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', message['departure_time'])),
                'postal: invalid departure date/time')
        require(message['dispatch_evidence'] and text(window['basis']),
                'postal: dispatch and estimate evidence required')
        if message['method'] in {'mounted-courier', 'guild-messenger', 'caravan-post', 'river-dispatch'}:
            require(bool(routes), 'postal: actual physical dispatch needs a route')
            current = message['origin']
            for ident in routes:
                route = route_lookup[ident]
                require(route['classification'] == 'CONFIRMED CANON',
                        'postal: proposed route is not operational dispatch evidence')
                mode = {'mounted-courier': 'riding', 'guild-messenger': 'walking',
                        'caravan-post': 'wagon', 'river-dispatch': 'river'}[message['method']]
                require(route.get('accessibility', {}).get(mode) is True,
                        'postal: method compatibility is unverified')
                if route['start'] == current:
                    current = route['destination']
                else:
                    require(route['destination'] == current and route['bidirectional'] and
                            route['reverse_status'] == 'CONFIRMED CANON',
                            'postal: disconnected/unverified reverse dispatch route')
                    current = route['start']
            require(current == message['destination'], 'postal: dispatch route endpoint mismatch')
        if message['method'] == 'limited-magic':
            require(message['spell_rule_ref'] in {'guardian-links', 'first-hours-accord', 'theron-spells'}
                    and bool(message['resource_evidence']), 'postal: magic requires existing rule and finite-resource evidence')
    if status in {'delivered', 'acknowledged'}:
        require(bool(message['receipt_evidence']), 'postal: delivery requires independent receipt evidence')
        require(message['receipt_evidence'] != message['dispatch_evidence'],
                'postal: sending is not delivery evidence')
    else:
        require(message['receipt_evidence'] == [], 'postal: non-delivered message cannot claim receipt')


def validate_settlement_expansion(root, records, require, repository_file, unique_json):
    def payload(ident):
        require(ident in records, 'phase2 settlements: missing owner')
        path = root/f"entities/{records[ident]['type']}/{ident}.md"
        blocks = re.findall(r'^```json\n(.*?)\n```$', path.read_text(), re.M | re.S)
        require(len(blocks) == 1, 'phase2 settlements: exactly one owner JSON block required')
        try:
            value = json.loads(blocks[0], object_pairs_hook=unique_json)
        except ValueError as exc:
            require(False, f'phase2 settlements: malformed JSON: {exc}')
        return value

    def shape(value, fields):
        require(isinstance(value, dict) and set(value) == set(fields.split()),
                'phase2 settlements: unexpected fields')

    def text(value):
        require(isinstance(value, str) and bool(value.strip()), 'phase2 settlements: expected text')

    def strings(value):
        require(isinstance(value, list) and all(isinstance(v, str) and v.strip() for v in value)
                and len(value) == len(set(value)), 'phase2 settlements: invalid/duplicate string list')

    def approval(value):
        require(value == APPROVAL, 'phase2 settlements: wrong approval provenance')
        repository_file(root, value, 'Phase 2 approval')

    registry = payload('settlement-services') if 'settlement-services' in records else {}
    located = set()
    for ident, record in records.items():
        if record['type'] == 'locations' and not ident.startswith('route-'):
            if '"approved_design"' in (root/f'entities/locations/{ident}.md').read_text():
                located.add(ident)
    present = HELPERS.intersection(records) or 'approved_design_location_ids' in registry or located
    if not present:
        return  # Historical disposable fixtures remain valid without the entire extension.
    require(HELPERS <= records.keys(), 'phase2 settlements: incomplete trade/postal extension')
    routed = registry.get('approved_design_location_ids')
    strings(routed)
    require(set(routed) == located == set(POPULATIONS), 'phase2 settlements: ten-settlement coverage mismatch')
    nodes = {n['id']: n for n in payload('world-geography')['nodes']}
    prices = payload('service-price-references').get('approved_references')
    require(isinstance(prices, list), 'phase2 settlements: approved references missing')
    seen_prices = set()
    for p in prices:
        shape(p, 'id item kind classification minimum_cp maximum_cp unit reference_type source_ref')
        ident = p['id']
        require(isinstance(ident, str) and ident in PRICES and ident not in seen_prices,
                'phase2 settlements: unknown/duplicate approved reference')
        seen_prices.add(ident)
        require(p['kind'] == 'approved-reference' and p['classification'] == 'APPROVED DESIGN',
                'phase2 settlements: reference is not a quote/charge')
        require(type(p['minimum_cp']) is int and type(p['maximum_cp']) is int and
                (p['minimum_cp'], p['maximum_cp'], p['unit']) == PRICES[ident],
                'phase2 settlements: price/wage contradicts approval')
        require(p['reference_type'] == ('wage' if ident in {'farm-labor', 'caravan-guard', 'skilled-blacksmith',
                                                          'experienced-healer', 'master-artisan'} else 'price'),
                'phase2 settlements: reference type mismatch')
        text(p['item']); approval(p['source_ref'])
    require(seen_prices == set(PRICES), 'phase2 settlements: approved price/wage coverage mismatch')
    industry_ids = set()
    business_ids = set()
    categories = set()
    for ident in routed:
        record = records[ident]
        require(record['type'] == 'locations' and record['status'] != 'research' and
                record['visibility'] == 'gm-reference', 'phase2 settlements: invalid settlement owner')
        require(APPROVAL in record['source_refs'], 'phase2 settlements: owner missing approval source')
        owner = payload(ident)
        d = owner['approved_design']
        shape(d, 'classification approval_source_ref settlement_label population households geographic_identity '
              'geographic_owner_ref districts government housing_and_classes customs_and_daily_life community_services '
              'market_and_employment household_expenses maintenance_and_emergencies communication_ref trade_ref '
              'communications_local local_challenges commercial_context current_conditions events industries businesses '
              'criminal_faction_refs unlawful_activity_designs')
        require(d['classification'] == 'APPROVED DESIGN', 'phase2 settlements: design is not historical observation')
        approval(d['approval_source_ref'])
        shape(d['population'], 'amount qualifier classification source_ref')
        pop = d['population']
        require(type(pop['amount']) is int and pop['amount'] == POPULATIONS[ident],
                'phase2 settlements: population contradicts approval')
        require(pop['classification'] == ('CONFIRMED CANON' if ident == 'brackenford' else 'APPROVED DESIGN') and
                pop['qualifier'] == ('approximately' if ident == 'brackenford' else 'approved estimate'),
                'phase2 settlements: population classification/qualification mismatch')
        if ident == 'brackenford':
            require(pop['source_ref'] == 'changes/chronicles/year848-day156-end-session.md' and
                    d['households'] == dict(amount=42, classification='CONFIRMED CANON', source_ref=pop['source_ref']),
                    'phase2 settlements: Brackenford household/identity changed')
        else:
            approval(pop['source_ref'])
            require(d['households'] is None, 'phase2 settlements: unsupported household count')
        if ident == 'southbank-landing':
            require(d['settlement_label'] == 'Southbank' and 'southbank' not in records,
                    'phase2 settlements: duplicate Southbank identity')
        require(d['geographic_owner_ref'] == 'world-geography' and ident in nodes,
                'phase2 settlements: geographic owner mismatch')
        if ident in NEW_LOCATIONS:
            require(nodes[ident]['classification'] == 'APPROVED DESIGN' and
                    nodes[ident]['parents'] == [dict(id='vellorin', classification='APPROVED DESIGN', source_refs=[APPROVAL])],
                    'phase2 settlements: unsupported realm/parent assignment')
        require(d['communication_ref'] == 'settlement-communications' and d['trade_ref'] == 'settlement-trade',
                'phase2 settlements: broken framework reference')
        require(d['current_conditions'] is None and d['events'] == [] and d['criminal_faction_refs'] == [],
                'phase2 settlements: no current events, secret connections or PR4 faction records')
        for f in ('settlement_label', 'geographic_identity', 'government', 'housing_and_classes', 'customs_and_daily_life',
                  'community_services', 'market_and_employment', 'household_expenses', 'maintenance_and_emergencies',
                  'communications_local', 'local_challenges', 'commercial_context'):
            text(d[f])
        strings(d['districts']); require(bool(d['districts']), 'phase2 settlements: districts required')
        require(isinstance(d['industries'], list) and bool(d['industries']), 'phase2 settlements: industry chains required')
        local_industries = set()
        for industry in d['industries']:
            shape(industry, 'id goods_services producers buyers raw_materials workers_skills storage transport '
                  'seasonality potential_shortages legal_obligations criminal_risks')
            require(isinstance(industry['id'], str) and industry['id'].startswith(ident+':industry-') and
                    industry['id'] not in industry_ids, 'phase2 settlements: industry owner/duplicate mismatch')
            for v in industry.values(): text(v)
            local_industries.add(industry['id']); industry_ids.add(industry['id'])
        require(isinstance(d['businesses'], list) and bool(d['businesses']), 'phase2 settlements: businesses required')
        legacy = {b['id']: b for b in owner.get('businesses', [])}
        for b in d['businesses']:
            shape(b, 'id name classification existing_business_ref district categories services ownership_status owner_id '
                  'staff_ids staffing_model supplier_industry_ids customers price_reference_ids pricing_basis legal_design '
                  'current_license adult_workers_only worker_agency operating_costs limitations stock_counts cash_balance_cp '
                  'operational_status source_ref suppliers')
            bid = b['id']
            require(isinstance(bid, str) and re.fullmatch(re.escape(ident)+r':[a-z0-9]+(?:-[a-z0-9]+)*', bid) and
                    bid not in business_ids, 'phase2 settlements: duplicate or wrong business owner')
            business_ids.add(bid)
            require(b['classification'] == 'APPROVED DESIGN' and b['legal_design'] in LEGAL,
                    'phase2 settlements: invalid business/legal classification')
            require(b['owner_id'] is None and b['staff_ids'] == [] and b['current_license'] is None and
                    b['stock_counts'] is None and b['cash_balance_cp'] is None and b['operational_status'] == 'UNKNOWN',
                    'phase2 settlements: no invented ownership, license, hires, stock or cash')
            if b['existing_business_ref'] is not None:
                require(b['existing_business_ref'] == bid and bid in legacy,
                        'phase2 settlements: invalid inherited business reference')
                if bid == 'brackenford:willow-lantern':
                    require(b['name'] == legacy[bid]['name'], 'phase2 settlements: existing business renamed')
            else:
                require(bid not in legacy, 'phase2 settlements: duplicate historical business')
            strings(b['categories']); categories.update(b['categories'])
            for field in ('supplier_industry_ids', 'price_reference_ids', 'services', 'operating_costs', 'suppliers'):
                strings(b[field])
            require(b['supplier_industry_ids'] and set(b['supplier_industry_ids']) <= local_industries,
                    'phase2 settlements: missing/wrong supplier dependency')
            require(set(b['price_reference_ids']) <= set(PRICES), 'phase2 settlements: unknown price reference')
            for field in ('name', 'district', 'ownership_status', 'staffing_model', 'customers', 'pricing_basis',
                          'worker_agency', 'limitations'):
                text(b[field])
            if set(b['categories']) & {'brothel', 'pleasure-house'}:
                require(b['adult_workers_only'] is True and b['legal_design'] == 'regulated-design',
                        'phase2 settlements: adult consent/regulation required')
                require(all(term in b['worker_agency'] for term in ('adults', 'refuse', 'leave', 'coercion', 'trafficking')),
                        'phase2 settlements: adult worker agency safeguards missing')
            else:
                require(b['adult_workers_only'] is None, 'phase2 settlements: invalid adult venue flag')
            approval(b['source_ref'])
        if ident == 'brackenford':
            require({b['id'] for b in d['businesses']} == set(legacy),
                    'phase2 settlements: Brackenford business identity mismatch')
        require(isinstance(d['unlawful_activity_designs'], list) and d['unlawful_activity_designs'],
                'phase2 settlements: commercial risk context required')
        for risk in d['unlawful_activity_designs']:
            shape(risk, 'category legal_design description finite_constraints events')
            require(risk['legal_design'] in {'tolerated-design', 'prohibited-design'} and risk['events'] == [],
                    'phase2 settlements: risk design cannot create active crimes')
            for field in ('category', 'description', 'finite_constraints'): text(risk[field])
    require({'general-store', 'blacksmith', 'tailor', 'baker', 'butcher', 'apothecary', 'healer', 'inn', 'tavern',
             'stable', 'warehouse', 'market', 'bathhouse', 'gambling', 'brothel', 'pleasure-house', 'pawnshop',
             'courier', 'caravan', 'ferry', 'barge'} <= categories, 'phase2 settlements: missing service categories')
    trade = payload('settlement-trade')
    shape(trade, 'schema_version classification road_owner_ref finance_owner_ref relationships actual_transactions automatic_shipments')
    require(trade['schema_version'] == 1 and type(trade['schema_version']) is int and trade['classification'] == 'PROPOSED' and
            trade['road_owner_ref'] == 'travel-routes' and trade['finance_owner_ref'] == 'party-finances' and
            trade['actual_transactions'] == [] and trade['automatic_shipments'] is False,
            'phase2 settlements: trade proposal cannot post transactions/shipments')
    require(isinstance(trade['relationships'], list), 'phase2 settlements: invalid trade relationships')
    seen_trade, participants = set(), set()
    routes = {ident: payload(ident) for ident in records if ident.startswith('route-')}
    for relation in trade['relationships']:
        shape(relation, 'id classification origin destination goods_services supplier_industry_id supplier_type buyer_type '
              'transport_method storage_handling seasonality route_dependencies unresolved_operational_details legal_risks '
              'criminal_risks verification_status actual_shipments source_ref')
        a, b = relation['origin'], relation['destination']
        require(isinstance(a, str) and isinstance(b, str) and a in POPULATIONS and b in POPULATIONS and a != b,
                'phase2 settlements: invalid trade endpoints')
        require(relation['id'] == 'trade:'+a+'--'+b and relation['id'] not in seen_trade,
                'phase2 settlements: duplicate trade relationship')
        seen_trade.add(relation['id']); participants.update((a, b))
        require(relation['supplier_industry_id'] in industry_ids and relation['supplier_industry_id'].startswith(a+':'),
                'phase2 settlements: trade supplier does not belong to origin')
        require(relation['classification'] == 'PROPOSED' and relation['verification_status'] == 'UNVERIFIED PROPOSAL' and
                relation['actual_shipments'] == [], 'phase2 settlements: proposed trade is not completed commerce')
        strings(relation['route_dependencies'])
        for route_id in relation['route_dependencies']:
            require(route_id in routes and {routes[route_id]['start'], routes[route_id]['destination']} == {a, b},
                    'phase2 settlements: route dependency does not connect trade endpoints')
        for field in ('goods_services', 'supplier_type', 'buyer_type', 'transport_method', 'storage_handling',
                      'seasonality', 'unresolved_operational_details', 'legal_risks', 'criminal_risks'):
            text(relation[field])
        approval(relation['source_ref'])
    require(participants == set(POPULATIONS), 'phase2 settlements: incomplete ten-settlement trade coverage')
    postal = payload('settlement-communications')
    shape(postal, 'schema_version classification autonomy_owner_ref road_owner_ref finance_owner_ref methods '
          'message_template messages automatic_delivery automatic_resource_postings')
    require(postal['schema_version'] == 1 and type(postal['schema_version']) is int and
            postal['classification'] == 'APPROVED DESIGN' and postal['autonomy_owner_ref'] == 'npc-autonomy-and-time' and
            postal['road_owner_ref'] == 'travel-routes' and postal['finance_owner_ref'] == 'party-finances',
            'phase2 settlements: wrong postal authority')
    require(postal['messages'] == [] and postal['automatic_delivery'] is False and postal['automatic_resource_postings'] is False,
            'phase2 settlements: maintenance cannot dispatch/deliver/post resources')
    require(isinstance(postal['methods'], list) and len(postal['methods']) == len(METHODS),
            'phase2 settlements: incomplete communication methods')
    seen_methods = set()
    for method in postal['methods']:
        shape(method, 'id carrier requirements')
        require(method['id'] in METHODS and method['id'] not in seen_methods, 'phase2 settlements: duplicate/unsupported method')
        seen_methods.add(method['id']); text(method['carrier']); text(method['requirements'])
    template = postal['message_template']
    require(isinstance(template, dict) and set(template) == MESSAGE_FIELDS, 'phase2 settlements: incomplete message template')
    require(template['actual_delivery_status'] == 'proposed' and template['estimated_delivery_window'] ==
            dict(earliest=None, latest=None, basis=None), 'phase2 settlements: empty template cannot imply delivery')
    for field in MESSAGE_FIELDS - {'actual_delivery_status', 'estimated_delivery_window'}:
        expected = [] if field in {'intended_route_ids', 'receipt_evidence', 'dispatch_evidence', 'resource_evidence'} else None
        require(template[field] == expected and type(template[field]) is type(expected),
                'phase2 settlements: populated message template implies event')
