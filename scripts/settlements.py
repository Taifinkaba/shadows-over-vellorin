"""Validate parent-owned settlement/service references without posting events or money."""
import json
import re

MARKER = '\n## Settlement and business references — Chunk 3\n'
CLASSIFICATIONS = {'CONFIRMED CANON', 'PROPOSED'}
PRICE_KINDS = {'historically-paid', 'current-verified-quote', 'approved-reference', 'proposed-regional-estimate'}


def validate_settlements(root, records, require, repository_file, unique_json):
    helpers = {'settlement-services', 'service-price-references', 'local-settlement-activity'}
    profiles = {}
    for ident, record in records.items():
        if record['type'] == 'locations' and not ident.startswith('route-'):
            path = root / f'entities/locations/{ident}.md'
            if MARKER in path.read_text():
                profiles[ident] = path
    if not (helpers & records.keys() or profiles):
        return  # Older repositories/fixtures without this extension remain supported.
    require(helpers <= records.keys(), 'settlements: missing routing, price or activity framework')

    def shape(value, fields, label):
        expected = set(fields.split())
        extensions = {'profile': 'approved_design', 'routing': 'approved_design_location_ids',
                      'price framework': 'approved_references'}
        if isinstance(value, dict) and extensions.get(label) in value:
            expected.add(extensions[label])
        if label == 'price framework' and isinstance(value, dict) and 'approved_service_adjustment' in value:
            expected.add('approved_service_adjustment')
        require(isinstance(value, dict) and set(value) == expected, f'settlements: invalid {label} fields')

    def text(value, label):
        require(isinstance(value, str) and value.strip(), f'settlements: invalid {label}')

    def strings(value, label):
        require(isinstance(value, list) and all(isinstance(v, str) and v.strip() for v in value), f'settlements: invalid {label}')
        require(len(value) == len(set(value)), f'settlements: duplicate {label}')

    def reference(ident, types=None):
        require(isinstance(ident, str) and ident in records, 'settlements: broken entity reference')
        require(records[ident]['visibility'] != 'gm-secret', 'settlements: GM-secret reference excluded from public service view')
        require(types is None or records[ident]['type'] in types, 'settlements: invalid reference type')

    def physical(ident):
        reference(ident, {'locations'})
        require(not ident.startswith('route-'), 'settlements: route cannot be parent location')

    def classification(value):
        require(isinstance(value, str) and value in CLASSIFICATIONS, 'settlements: invalid classification')

    def sources(values):
        strings(values, 'source_refs')
        require(bool(values), 'settlements: source_refs required')
        for value in values:
            repository_file(root, value, 'settlement source')

    def quote(ref, value):
        text(value, 'evidence quote')
        # Self references can cite only preexisting prose, never certify their own appended claim.
        source = repository_file(root, ref, 'settlement evidence').read_text().split(MARKER)[0]
        require(value in source, 'settlements: evidence quote not found in original source')

    def evidence(values, refs):
        require(isinstance(values, list) and values, 'settlements: evidence required')
        for item in values:
            shape(item, 'source_ref quote', 'evidence')
            require(item['source_ref'] in refs, 'settlements: undeclared evidence source')
            quote(item['source_ref'], item['quote'])

    def payload(path, section=False):
        content = path.read_text()
        if section:
            require(content.count(MARKER) == 1, 'settlements: duplicate profile section')
            content = content.split(MARKER)[1]
        blocks = re.findall(r'^```json\n(.*?)\n```$', content, re.M | re.S)
        require(len(blocks) == 1, 'settlements: expected one JSON block')
        try:
            data = json.loads(blocks[0], object_pairs_hook=unique_json)
        except ValueError as exc:
            require(False, f'settlements: invalid JSON: {exc}')
        require(isinstance(data, dict) and type(data.get('schema_version')) is int and data['schema_version'] == 1,
                'settlements: unsupported schema')
        return data

    registry = payload(root/'entities/mechanics/settlement-services.md')
    shape(registry, 'schema_version location_ids business_categories automatic_financial_postings', 'routing')
    strings(registry['location_ids'], 'settlement IDs')
    require(set(registry['location_ids']) == set(profiles), 'settlements: profile/routing coverage mismatch')
    strings(registry['business_categories'], 'business categories')
    require(registry['automatic_financial_postings'] is False, 'settlements: automatic financial postings forbidden')

    prices = payload(root/'entities/mechanics/service-price-references.md')
    shape(prices, 'schema_version currency price_kinds reference_bands automatic_financial_postings', 'price framework')
    shape(prices['currency'], 'cp_per_gp cp_per_sp', 'currency')
    require(all(type(n) is int for n in prices['currency'].values()) and prices['currency'] == {'cp_per_gp':100,'cp_per_sp':10},
            'settlements: currency must be100cp/gp and10cp/sp')
    strings(prices['price_kinds'], 'price kinds')
    require(set(prices['price_kinds']) == PRICE_KINDS, 'settlements: missing price distinctions')
    require(prices['automatic_financial_postings'] is False, 'settlements: automatic financial postings forbidden')
    bands = set()
    require(isinstance(prices['reference_bands'], list), 'settlements: invalid reference bands')
    for band in prices['reference_bands']:
        shape(band, 'id item kind classification minimum_cp maximum_cp unit source_ref source_quote note', 'reference band')
        text(band['id'], 'price ID')
        require(band['id'] not in bands, 'settlements: duplicate reference price ID')
        bands.add(band['id'])
        require(band['kind'] == 'proposed-regional-estimate' and band['classification'] == 'PROPOSED',
                'settlements: archived design price not approved or quoted')
        validate_amount(band, require)
        quote(band['source_ref'], band['source_quote'])
        # Verify exact original copper conversion, rather than trusting a copied proposed band.
        match = re.fullmatch(r'\| .* \| (\d+)–(\d+) (cp|sp|gp)(?: per horse)? \|', band['source_quote'])
        require(match is not None, 'settlements: unrecognized price evidence')
        low, high, unit = match.groups()
        factor = {'cp':1,'sp':10,'gp':100}[unit]
        require((band['minimum_cp'],band['maximum_cp']) == (int(low)*factor,int(high)*factor),
                'settlements: reference price contradicts source conversion')

    activity = payload(root/'entities/mechanics/local-settlement-activity.md')
    shape(activity, 'schema_version categories events automatic_progression', 'activity framework')
    strings(activity['categories'], 'activity categories')
    require(activity['events'] == [] and activity['automatic_progression'] is False,
            'settlements: maintenance cannot trigger events or progression')

    businesses = {}
    pending_links = []
    for ident, path in profiles.items():
        p = payload(path, section=True)
        shape(p, 'schema_version location_id classification nation_id territory_id region_id settlement_type population government '
              'principal_official_id watch watch_official_id court route_ids neighborhoods nearby_location_ids '
              'institutions service_links local_problem_refs notes source_refs evidence businesses', 'profile')
        require(p['location_id'] == ident, 'settlements: profile ID does not match owner')
        physical(ident)
        classification(p['classification'])
        require((p['classification'] == 'PROPOSED') == (records[ident]['status'] == 'research'),
                'settlements: proposed/canon location mismatch')
        for field in ('nation_id','territory_id','region_id'):
            if p[field] is not None:
                physical(p[field])
        for field in ('principal_official_id','watch_official_id'):
            if p[field] is not None:
                reference(p[field], {'characters'})
        for field in ('settlement_type','government','watch','court'):
            if p[field] is not None:
                text(p[field], field)
        if p['population'] is not None:
            shape(p['population'], 'amount qualifier', 'population')
            require(type(p['population']['amount']) is int and p['population']['amount'] > 0, 'settlements: invalid population')
            text(p['population']['qualifier'], 'population qualifier')
        if p['population'] is not None:
            original = path.read_text().split(MARKER)[0]
            supplied = re.search(r'approx(\d+) residents', original)
            require(supplied is not None and p['population']['amount'] == int(supplied[1]),
                    'settlements: population not supported by original source')
        if ident == 'brackenford':
            require(p['principal_official_id'] == 'elsbeth-marrin' and p['watch_official_id'] == 'ressa-vale',
                    'settlements: established village authority changed')
        if p['neighborhoods'] is not None:
            strings(p['neighborhoods'], 'neighborhoods')
        strings(p['route_ids'], 'route IDs')
        for route in p['route_ids']:
            reference(route, {'locations'})
            require(route.startswith('route-'), 'settlements: expected route reference')
            d = payload(root/f'entities/locations/{route}.md')
            require(ident in (d['start'],d['destination']), 'settlements: route does not connect parent')
            # Classification is read from route owner, never copied/promoted into the profile.
        strings(p['nearby_location_ids'], 'nearby location IDs')
        for target in p['nearby_location_ids']:
            physical(target)
            require(target != ident, 'settlements: self-nearby reference')
        require(isinstance(p['institutions'], list), 'settlements: invalid institutions')
        for inst in p['institutions']:
            shape(inst, 'kind label entity_id classification', 'institution')
            text(inst['kind'], 'institution kind')
            text(inst['label'], 'institution label')
            classification(inst['classification'])
            if inst['entity_id'] is not None:
                reference(inst['entity_id'])
                require(inst['classification'] != 'CONFIRMED CANON' or records[inst['entity_id']]['status'] != 'research',
                        'settlements: proposed institution promoted')
        strings(p['service_links'], 'service links')
        pending_links += p['service_links']
        strings(p['local_problem_refs'], 'problem refs')
        for target in p['local_problem_refs']:
            reference(target, {'quests','mechanics'})
        sources(p['source_refs'])
        evidence(p['evidence'], p['source_refs'])
        text(p['notes'], 'profile notes')
        require(isinstance(p['businesses'], list), 'settlements: invalid businesses')
        for b in p['businesses']:
            shape(b, 'id name display_label parent_location_id classification address categories owner_id manager_id '
                  'operator_id staff_ids staff_notes services goods_categories stock_counts capacity schedule accepted_currency '
                  'payment_practices prices price_reference_ids supplier_relationships existing_contracts licenses '
                  'operational_status last_verified_date last_verified_note source_refs evidence automatic_financial_postings', 'business')
            bid = b['id']
            require(isinstance(bid, str) and re.fullmatch(re.escape(ident)+r':[a-z0-9]+(?:-[a-z0-9]+)*',bid),
                    'settlements: invalid parent-scoped business ID')
            require(bid not in businesses, 'settlements: duplicate business ID')
            businesses[bid] = b
            require(b['parent_location_id'] == ident, 'settlements: business parent mismatch')
            classification(b['classification'])
            require(p['classification'] == 'CONFIRMED CANON' or b['classification'] == 'PROPOSED',
                    'settlements: canon business in proposed location')
            for field in ('name','address','staff_notes','schedule','accepted_currency','payment_practices','last_verified_date'):
                if b[field] is not None:
                    text(b[field], field)
            for field in ('display_label','operational_status','last_verified_note'):
                text(b[field], field)
            strings(b['categories'], 'business categories')
            require(b['categories'] and set(b['categories']) <= set(registry['business_categories']), 'settlements: unsupported category')
            for field in ('owner_id','manager_id','operator_id'):
                if b[field] is not None:
                    reference(b[field], {'characters','factions'})
            strings(b['staff_ids'], 'staff IDs')
            for target in b['staff_ids']:
                reference(target, {'characters'})
            strings(b['services'], 'services')
            if b['goods_categories'] is not None:
                strings(b['goods_categories'], 'goods categories')
            require(b['stock_counts'] is None, 'settlements: no counted stock verified in this maintenance baseline')
            if b['capacity'] is not None:
                shape(b['capacity'], 'unit amount', 'capacity')
                text(b['capacity']['unit'], 'capacity unit')
                require(type(b['capacity']['amount']) is int and b['capacity']['amount'] > 0, 'settlements: invalid capacity')
            if b['capacity'] is not None:
                original = path.read_text().split(MARKER)[0]
                if bid == 'brackenford:willow-lantern':
                    require('six-room inn' in original and b['capacity'] == {'unit':'rooms','amount':6},
                            'settlements: inn capacity contradicts source')
                elif bid == 'ashvale-estate:merchant-storage':
                    count = re.search(r'(\d+) merchant storage bays',original)
                    require(count is not None and b['capacity'] == {'unit':'storage-bays','amount':int(count[1])},
                            'settlements: storage capacity contradicts source')
                else:
                    require(False, 'settlements: new capacity requires sourced support')
            require(b['automatic_financial_postings'] is False, 'settlements: automatic financial postings forbidden')
            strings(b['price_reference_ids'], 'price references')
            require(set(b['price_reference_ids']) <= bands, 'settlements: unknown reference price')
            sources(b['source_refs'])
            evidence(b['evidence'], b['source_refs'])
            require(isinstance(b['prices'], list), 'settlements: invalid prices')
            for price in b['prices']:
                shape(price, 'kind item minimum_cp maximum_cp unit source_ref source_quote note', 'business price')
                require(isinstance(price['kind'], str) and price['kind'] in PRICE_KINDS, 'settlements: invalid price kind')
                validate_amount(price, require)
                require(price['source_ref'] in b['source_refs'], 'settlements: undeclared price source')
                quote(price['source_ref'], price['source_quote'])
                if price['kind'] == 'historically-paid':
                    m = re.fullmatch(r'Forge/workshop(\d+)gp',price['source_quote'])
                    require(m is not None and price['minimum_cp'] == price['maximum_cp'] == int(m[1])*100,
                            'settlements: historical paid price contradicts source')
                else:
                    # No current/approved shop quote was supplied in Chunk3; extend with evidence when one is adopted.
                    require(False, 'settlements: new quote or approved price requires separate sourced support')
            require(b['supplier_relationships'] == [], 'settlements: no verified supply contract; proposals are not deliveries')
            require(b['existing_contracts'] is None and b['licenses'] is None,
                    'settlements: no verified business contracts/licenses supplied')
            # Preserve evidenced management/property distinction without treating every operator as owner.
            if ident in ('ashvale-estate','ashvale-lodge'):
                require(b['owner_id'] == 'theron-ashvale' and b['manager_id'] == 'tomas',
                        'settlements: established ownership/management changed')
            if ident == 'brackenford':
                require(b['owner_id'] is None, 'settlements: operator is not a verified property owner')
                expected_operators = {'brackenford:willow-lantern':'mara-fenwick',
                                      'brackenford:forge':'borin-emberhand',
                                      'brackenford:herbalist':'seren-willowmere'}
                require(b['operator_id'] == expected_operators.get(bid),
                        'settlements: established operator changed or new assignment inferred')
    require(all(link in businesses for link in pending_links), 'settlements: broken scoped business link')


def validate_amount(value, require):
    lo, hi = value['minimum_cp'], value['maximum_cp']
    require(type(lo) is int and type(hi) is int and 0 <= lo <= hi,
            'settlements: invalid integer-copper price range')
    require(isinstance(value['item'], str) and value['item'].strip(), 'settlements: invalid price item')
    require(isinstance(value['unit'], str) and value['unit'].strip(), 'settlements: invalid price unit')
    require(isinstance(value['note'], str) and value['note'].strip(), 'settlements: invalid price note')
