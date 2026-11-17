"""Read-only validation of entity-owned geography and travel JSON blocks.

Helpers supplied by validate.py retain its error type in CLI and import modes.
"""
import json
import re

CLASSIFICATIONS = {'CONFIRMED CANON', 'PROPOSED'}
MODES = {'walking', 'riding', 'wagon', 'caravan', 'unknown'}
KINDS = {'continent', 'territory', 'region', 'province', 'city', 'town', 'settlement',
         'village', 'hamlet', 'property', 'watch-station', 'landmark', 'wilderness',
         'dungeon-site', 'dungeon-entrance', 'sanctuary', 'unknown'}


def validate_geography(root, records, require, repository_file, unique_json):
    """Optional on historical fixture trees; mandatory if any travel record exists."""
    required = {'world-geography', 'travel-routes', 'travel-procedure'}
    route_ids = {i for i in records if i.startswith('route-')}
    if not (required & records.keys() or route_ids):
        return  # Historical snapshots predating this maintenance extension.
    require(required <= records.keys(), 'travel: missing directory, registry or procedure')

    def shape(value, fields, label):
        require(isinstance(value, dict) and set(value) == set(fields.split()),
                f'travel: {label}: invalid fields')

    def text(value, label):
        require(isinstance(value, str) and bool(value.strip()), f'travel: {label}: expected text')

    def refs(values, owner):
        require(isinstance(values, list) and bool(values), 'travel: source_refs required')
        require(all(isinstance(v, str) for v in values), 'travel: invalid source_refs')
        require(len(values) == len(set(values)), 'travel: duplicate source_refs')
        for v in values:
            require(v in records[owner]['source_refs'], 'travel: undeclared source reference')
            repository_file(root, v, 'travel source')

    def payload(ident):
        p = root / f"entities/{records[ident]['type']}/{ident}.md"
        blocks = re.findall(r'^```json\n(.*?)\n```$', p.read_text(), re.M | re.S)
        require(len(blocks) == 1, f'travel: {ident}: expected one JSON block')
        try:
            data = json.loads(blocks[0], object_pairs_hook=unique_json)
        except ValueError as exc:
            require(False, f'travel: {ident}: invalid JSON: {exc}')
        require(isinstance(data, dict) and type(data.get('schema_version')) is int
                and data['schema_version'] == 1, f'travel: {ident}: unsupported schema')
        return data

    def classify(value, geographic=False):
        allowed = CLASSIFICATIONS | ({'APPROVED DESIGN'} if geographic else set())
        require(isinstance(value, str) and value in allowed, 'travel: invalid classification')

    geo = payload('world-geography')
    design_ids = {e['id'] for e in json.loads((root / 'index.json').read_text())['entries']
                  if 'approved-design' in e.get('tags', []) and e['type'] == 'locations'
                  and not e['id'].startswith('route-')}
    shape(geo, 'schema_version nodes', 'directory')
    require(isinstance(geo['nodes'], list), 'travel: nodes must be list')
    nodes = {}
    for node in geo['nodes']:
        shape(node, 'id kind classification parents', 'node')
        ident = node['id']
        require(isinstance(ident, str) and ident in records
                and records[ident]['type'] == 'locations' and not ident.startswith('route-'),
                'travel: invalid location node')
        require(ident not in nodes, 'travel: duplicate canonical location/node')
        require(isinstance(node['kind'], str) and node['kind'] in KINDS, 'travel: invalid geographic kind')
        classify(node['classification'], geographic=True)
        require((node['classification'] == 'PROPOSED') == (records[ident]['status'] == 'research'),
                'travel: location proposed/canon metadata mismatch')
        if node['classification'] == 'APPROVED DESIGN':
            require(records[ident]['status'] == 'canon' and
                    'changes/chronicles/phase2-01-geography-approval.md' in records[ident]['source_refs'],
                    'travel: approved design requires approval provenance')
        require(isinstance(node['parents'], list), 'travel: parents must be list')
        require((node['classification'] == 'APPROVED DESIGN') == (ident in design_ids),
                'travel: approved design classification/metadata mismatch')
        nodes[ident] = node
    physical = {i for i, m in records.items() if m['type'] == 'locations' and not i.startswith('route-')}
    require(set(nodes) == physical, 'travel: location directory coverage mismatch')
    # Exact identity duplicates are errors; similar names require human review, not guessed merging.
    titles = {}
    location_titles = {}
    index = json.loads((root / 'index.json').read_text())
    for e in index['entries']:
        if e['id'] in nodes:
            location_titles[e['id']] = e['title']
        if e['id'] in nodes and nodes[e['id']]['classification'] == 'CONFIRMED CANON':
            title = re.sub(r'[^a-z0-9]', '', e['title'].casefold())
            require(title not in titles, 'travel: duplicate canonical location title')
            titles[title] = e['id']
    for ident, node in nodes.items():
        parent_ids = set()
        for edge in node['parents']:
            shape(edge, 'id classification source_refs', 'parent edge')
            parent = edge['id']
            require(isinstance(parent, str) and parent in nodes and parent != ident,
                    'travel: invalid containment parent')
            require(parent not in parent_ids, 'travel: duplicate containment parent')
            parent_ids.add(parent)
            classify(edge['classification'], geographic=True)
            refs(edge['source_refs'], 'world-geography')
            if edge['classification'] == 'APPROVED DESIGN':
                require(node['classification'] != 'PROPOSED' and nodes[parent]['classification'] != 'PROPOSED'
                        and 'changes/chronicles/phase2-01-geography-approval.md' in edge['source_refs'],
                        'travel: invalid approved containment/provenance')
            if edge['classification'] == 'CONFIRMED CANON':
                require(node['classification'] == nodes[parent]['classification'] == 'CONFIRMED CANON',
                        'travel: canonical containment through proposed location')
    visiting, visited = set(), set()
    def visit(ident):
        require(ident not in visiting, 'travel: geographic containment cycle')
        if ident in visited:
            return
        visiting.add(ident)
        for edge in nodes[ident]['parents']:
            visit(edge['id'])
        visiting.remove(ident)
        visited.add(ident)
    for ident in nodes:
        visit(ident)

    registry = payload('travel-routes')
    shape(registry, 'schema_version route_ids', 'registry')
    listed = registry['route_ids']
    require(isinstance(listed, list) and all(isinstance(i, str) for i in listed), 'travel: invalid route IDs')
    require(len(listed) == len(set(listed)), 'travel: duplicate route ID')
    require(set(listed) == route_ids, 'travel: route registry coverage mismatch')
    canonical_pairs = set()
    for ident in listed:
        require(records[ident]['type'] == 'locations', 'travel: route must be location entity')
        data = payload(ident)
        shape(data, 'schema_version classification start destination bidirectional reverse_status '
              'intermediate_settlements road_name road_type distance durations accessibility terrain '
              'road_condition known_hazards patrol_jurisdiction toll_requirements seasonal_restrictions '
              'last_verified_status source_refs integration_points notes', 'route')
        classify(data['classification'])
        classify(data['reverse_status'])
        canon = data['classification'] == 'CONFIRMED CANON'
        require(records[ident]['status'] == ('canon' if canon else 'research'),
                'travel: route proposed/canon metadata mismatch')
        start, end = data['start'], data['destination']
        for endpoint in (start, end):
            require(isinstance(endpoint, str) and endpoint in nodes, 'travel: invalid route endpoint')
            require(nodes[endpoint]['kind'] != 'continent', 'travel: impossible continent road endpoint')
            if canon:
                require(nodes[endpoint]['classification'] == 'CONFIRMED CANON',
                        'travel: canonical route through proposed location')
        require(start != end, 'travel: identical route endpoints')
        require(type(data['bidirectional']) is bool, 'travel: bidirectional must be boolean')
        require(data['bidirectional'] or data['reverse_status'] == 'PROPOSED', 'travel: invalid reverse status')
        require(canon or data['reverse_status'] == 'PROPOSED', 'travel: proposed reverse cannot be canon')
        mids = data['intermediate_settlements']
        require(mids is None or isinstance(mids, list), 'travel: invalid intermediate settlements')
        if mids is not None:
            require(all(isinstance(i, str) and i in nodes for i in mids), 'travel: invalid intermediate location')
            chain = [start] + mids + [end]
            require(len(chain) == len(set(chain)), 'travel: repeated route waypoint')
            for mid in mids:
                require(nodes[mid]['kind'] in {'city','town','settlement','village','hamlet'},
                        'travel: intermediate is not a settlement')
                require(not canon or nodes[mid]['classification'] == 'CONFIRMED CANON',
                        'travel: canonical route through proposed settlement')
        if canon:
            chain = tuple([start] + (mids or []) + [end])
            path_key = min(chain, tuple(reversed(chain)))
            signature = (path_key, data['road_name'], data['road_type'])
            # Distinct named roads can legitimately connect the same endpoints.
            require(all(v is None or isinstance(v, str) for v in signature[1:]),
                    'travel: invalid road name/type')
            require(signature not in canonical_pairs, 'travel: duplicate canonical route; review alternatives')
            canonical_pairs.add(signature)
        for field in ('road_name','road_type','terrain','road_condition','patrol_jurisdiction',
                      'toll_requirements','seasonal_restrictions'):
            if data[field] is not None:
                text(data[field], field)
        for field in ('last_verified_status','notes'):
            text(data[field], field)
        hazards = data['known_hazards']
        require(hazards is None or isinstance(hazards, list) and all(isinstance(h, str) and h.strip() for h in hazards),
                'travel: invalid hazards')
        refs(data['source_refs'], ident)
        access = data['accessibility']
        shape(access, 'walking riding wagon caravan', 'accessibility')
        require(all(v is None or type(v) is bool for v in access.values()), 'travel: invalid accessibility')
        distance = data['distance']
        if distance is not None:
            shape(distance, 'value unit basis', 'distance')
            require(type(distance['value']) is int and distance['value'] > 0, 'travel: invalid distance')
            require(distance['unit'] in ('m','km','miles'), 'travel: invalid distance unit')
            require(distance['basis'] in ('verified','proposed-estimate'), 'travel: invalid distance basis')
            # No verified survey exists yet; approving one requires extending this guard with its evidence.
            require(not canon and distance['basis'] == 'proposed-estimate',
                    'travel: unsupported historical distance')
        require(isinstance(data['durations'], list), 'travel: durations must be list')
        seen_modes = set()
        for d in data['durations']:
            fields = 'mode minimum maximum unit qualifier basis'
            if canon:
                fields += ' source_ref source_quote'
            shape(d, fields, 'duration')
            mode = d['mode']
            require(isinstance(mode, str) and mode in MODES and mode not in seen_modes, 'travel: invalid/duplicate mode')
            seen_modes.add(mode)
            require(access.get(mode) is not False, 'travel: duration for inaccessible mode')
            mn, mx = d['minimum'], d['maximum']
            require(type(mn) is int and mn > 0 and (mx is None or type(mx) is int and mx >= mn),
                    'travel: invalid duration range')
            require(d['unit'] in ('minutes','hours','days'), 'travel: invalid duration unit')
            text(d['qualifier'], 'duration qualifier')
            require(d['basis'] == ('historical-report' if canon else 'proposed-estimate'),
                    'travel: duration proposed/canon basis mismatch')
            if canon:
                require(d['source_ref'] in data['source_refs'], 'travel: duration source not declared')
                source = repository_file(root, d['source_ref'], 'travel duration source').read_text()
                require(all(location_titles[e].casefold() in source.casefold() for e in (start, end)),
                        'travel: historical endpoints not supported by duration source')
                quote = d['source_quote']
                text(quote, 'duration evidence quote')
                require(quote in source, 'travel: historical quote not found in source')
                # A deliberately narrow source parser preserves the four existing reports, not a speed model.
                parsed = re.fullmatch(r'(?:(walking) route to [^~]+ )?(a little over |~)(two|three|\d+) (hours|minutes)(.*)', quote)
                require(parsed is not None, 'travel: unsupported historical duration evidence')
                explicit_mode, prefix, number, unit, suffix = parsed.groups()
                amount = {'two':2,'three':3}.get(number)
                if amount is None:
                    amount = int(number)
                amount *= 60 if unit == 'hours' else 1
                expected_mode = 'wagon' if 'by wagon' in suffix else 'walking' if 'walk' in suffix or explicit_mode == 'walking' else 'unknown'
                require((mn, mx, d['unit'], mode) == (amount, None if prefix == 'a little over ' else amount,
                                                       'minutes', expected_mode),
                        'travel: duration contradicts historical source')
        require(isinstance(data['integration_points'], list), 'travel: integration points must be list')
        for point in data['integration_points']:
            shape(point, 'role target_id classification placement at_location', 'integration point')
            target = point['target_id']
            require(isinstance(target, str) and target in records, 'travel: broken integration reference')
            require(records[target]['visibility'] == 'gm-reference', 'travel: secret integration requires separate GM view')
            classify(point['classification'])
            text(point['role'], 'integration role')
            require(point['placement'] in ('endpoint','endpoint-service','along-route','unlocated'),
                    'travel: invalid integration placement')
            require(point['at_location'] is None or isinstance(point['at_location'], str)
                    and point['at_location'] in nodes, 'travel: broken integration location')
            if point['placement'] in ('endpoint', 'endpoint-service'):
                require(point['at_location'] in (start, end), 'travel: integration outside endpoints')
            if point['placement'] == 'endpoint':
                require(target in (start,end), 'travel: endpoint service at unrelated location')
            if point['classification'] == 'CONFIRMED CANON':
                require(records[target]['status'] != 'research', 'travel: proposed integration promoted to canon')
