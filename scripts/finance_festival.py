"""Validate the sourced festival, estate and fair cash window."""
if __package__:
    from .finance_endpoint import validate_endpoint
    from .validate import copper, integer, keys, read_json, repository_file, require
else:
    from finance_endpoint import validate_endpoint
    from validate import copper, integer, keys, read_json, repository_file, require

SOURCE = 'changes/chronicles/year851-day160-end-session.md'
PRIOR = 'archive/checkpoints/year848-suncrest262'
POSTINGS_GP = {
    'festival': {
        'general-tickets': 2400, 'premium-tickets': 1200, 'merchant-commission': 176,
        'lodging': 165, 'stall-and-venue-fees': 120, 'caravan-services': 65,
        'food-concessions': 210, 'champion-prize-kaela': -100, 'other-festival-expenses': -3010,
    },
    'estate-expansion': {'arena-build': -1750, 'land-registration': -280, 'retreat-build': -340},
    'first-fair': {'first-fair-receipts': 184, 'first-fair-expenses': -100},
}
CAPITAL_PROJECTS = {
    'arena-build': 'ashvale-grand-arena',
    'land-registration': 'therons-commercial-estate',
    'retreat-build': 'dragon-friendship-retreat',
}


def validate_festival(root, state, ledger):
    prior_state = read_json(repository_file(root, PRIOR + '.json', 'prior checkpoint'))
    prior_ref = PRIOR + '-finance-ledger.json'
    prior = read_json(repository_file(root, prior_ref, 'prior ledger'))
    validate_endpoint(root, prior_state, prior)
    keys(ledger, set(prior) | {'historical_suncrest262_ref', 'completed_projects'}, 'festival ledger')
    require(type(ledger['schema_version']) is int and ledger['schema_version'] == 7,
            'festival: invalid ledger version')
    require(state['source'] == ledger['source'] == SOURCE, 'festival: source mismatch')
    require(state['calendar'] == dict(annual_day=160, season=None, historical_label='Year 848, Suncrest 1135'),
            'festival: preserve historical label and unknown season')
    require((state['date'], state['time'], state['location'], state['status']) ==
            ('Year 851 Day 160', '19:00', "Theron's Estate, Ashvale Grand Arena", 'ENDED'),
            'festival: approved scene differs')
    for field in ('theron', 'resources', 'world'):
        require(state[field] == prior_state[field], f'festival: unexpected change to {field}')
    provenance = dict(prior_state['provenance'], exact_room='Ashvale Grand Arena')
    require(state['provenance'] == provenance, 'festival: unsupported equipment or presence observation')

    scene = dict(date=state['date'], annual_day=160, season=None, time=state['time'],
                 location=state['location'], session_status=state['status'])
    require(ledger['as_of'] == scene, 'festival: ledger as-of differs from checkpoint')
    require(ledger['historical_suncrest262_ref'] == prior_ref, 'festival: prior ledger reference differs')
    updated = {'schema_version', 'as_of', 'source', 'qualification', 'bridge', 'endpoint',
               'transactions', 'controlled_cash'}
    for field in prior.keys() - updated:
        require(ledger[field] == prior[field], f'festival: preserved {field} differs')

    opening = 213300
    prior_cash = prior['controlled_cash']['total_cp']
    require(ledger['bridge'] == dict(historical_closing_cp=prior_cash, opening_cp=opening,
                                   difference_cp=opening-prior_cash, classification='UNRESOLVED HISTORICAL GAP',
                                   is_transaction=False, assigned_account_id=None, source_ref=SOURCE),
            'festival: missing bridge evidence cannot become a posting')
    expected = {ident: (event, gp * 100) for event, rows in POSTINGS_GP.items() for ident, gp in rows.items()}
    seen = set()
    closing = opening
    for row in ledger['transactions']:
        ident = row.get('id')
        require(ident in expected and ident not in seen, 'festival: unsupported or duplicate posting')
        event, effect = expected[ident]
        inflow = effect > 0
        integer(row.get('amount_cp'), 'festival amount', 1)
        require(type(row.get('cash_effect_cp')) is int and row ==
                dict(id=ident, event=event, amount_cp=abs(effect), cash_effect_cp=effect,
                     direction='inflow' if inflow else 'outflow', kind='revenue' if inflow else 'expense',
                     status='received' if inflow else 'paid', date=None, account_id=None, source_ref=SOURCE),
                'festival: posting differs from played evidence')
        seen.add(ident)
        closing += effect
    require(seen == set(expected) and closing == 107300 == copper(state['money']['total_gp_sp']),
            'festival: missing posting or cash mismatch')
    require(ledger['endpoint'] == dict(as_of=scene, total_cp=closing, source_ref=SOURCE,
                                      classification=prior['endpoint']['classification']),
            'festival: cash endpoint differs')
    require(ledger['controlled_cash'] == dict(prior['controlled_cash'], total_cp=closing),
            'festival: only the existing purse is allocated')
    require(ledger['completed_projects'] ==
            [dict(asset_id=asset, transaction_id=ident, outstanding_cp=0)
             for ident, asset in CAPITAL_PROJECTS.items()], 'festival: paid capital projects differ')


YEAR_END_SOURCE = 'changes/chronicles/year852-day1-end-session.md'
DAY160 = 'archive/checkpoints/year851-day160'
PROVISIONAL = 'PROVISIONAL PLAYED ENDPOINT'
YEAR_END_POSTINGS_GP = {
    'general-tickets': 3900, 'reserved-tickets': 2900, 'premium-tickets': 1500,
    'registration': 128, 'merchant-pitches': 150, 'camping-rentals': 270,
    'merchant-profit-share': (2400 - 1200) // 4, 'lodge-stays': 240, 'food-concessions': 500,
    'security': -620, 'medical': -270, 'food-supplies': -720, 'staff-referees': -380,
    'emberpears': -360, 'emberpear-nursery-stock': -120, 'entertainment': -210,
    'advertising': -130, 'camping-cleanup': -240, 'dsi-logistics': -150,
    'maeryn-prize': -100, 'utilities-staging': -250, 'repairs': -150,
}


def validate_year_end(root, state, ledger):
    prior_state = read_json(repository_file(root, DAY160 + '.json', 'Day 160 checkpoint'))
    prior = read_json(repository_file(root, DAY160 + '-finance-ledger.json', 'Day 160 ledger'))
    validate_festival(root, prior_state, prior)
    keys(ledger, set(prior), 'year-end ledger')
    require(type(ledger['schema_version']) is int and ledger['schema_version'] == 7,
            'year end: invalid ledger version')
    require(state['source'] == ledger['source'] == YEAR_END_SOURCE,
            'year end: source mismatch')
    require((state['date'], state['time'], state['location'], state['status']) ==
            ('Year 852 Day 1', '00:00', "Theron's Commercial Estate, Ashvale Grand Arena", 'ENDED')
            and state['calendar'] == dict(annual_day=1, season=None, historical_label='Year 852 Day 1'),
            'year end: midnight rollover or season differs')
    require(state['theron'] == dict(prior_state['theron'], mp=385),
            'year end: last-tracked MP or other stats differ')
    for field in ('resources', 'world', 'custody'):
        require(state[field] == prior_state[field], f'year end: unsupported change to {field}')
    require(state['provenance']['current_equipment']['status'] ==
            state['provenance']['current_presence']['status'] == 'UNKNOWN'
            and state['provenance']['exact_room'] == 'Ashvale Grand Arena',
            'year end: unsupported observation')
    updated = {'as_of', 'source', 'qualification', 'bridge', 'endpoint',
               'transactions', 'controlled_cash'}
    for field in prior.keys() - updated:
        require(ledger[field] == prior[field], f'year end: preserved {field} differs')

    scene = dict(date=state['date'], annual_day=1, season=None, time=state['time'],
                 location=state['location'], session_status=state['status'])
    require(ledger['as_of'] == scene, 'year end: ledger as-of differs from checkpoint')
    opening = 105300
    verified = prior['controlled_cash']['total_cp']
    require(ledger['bridge'] == dict(historical_closing_cp=verified, opening_cp=opening,
                                   difference_cp=opening-verified, classification='UNRESOLVED HISTORICAL GAP',
                                   is_transaction=False, assigned_account_id=None, source_ref=YEAR_END_SOURCE),
            'year end: opening difference must stay unposted')
    historical = prior['transactions']
    require(ledger['transactions'][:len(historical)] == historical,
            'year end: prior postings changed')
    expected = {
        'observatory-feast-initial-payment': ('private-celebration', -70, 'Year 851 Day 326'),
        'observatory-feast-final-settlement': ('private-celebration', -26, None),
    }
    expected.update({'year-end-' + ident: ('year-end-festival', gp, 'Year 851 Day 365')
                     for ident, gp in YEAR_END_POSTINGS_GP.items()})
    closing = opening
    for row in ledger['transactions'][len(historical):]:
        ident = row.get('id')
        require(ident in expected, 'year end: unsupported or duplicate posting')
        event, gp, date = expected.pop(ident)
        effect = gp * 100
        inflow = effect > 0
        integer(row.get('amount_cp'), 'year-end amount', 1)
        require(type(row.get('cash_effect_cp')) is int and row ==
                dict(id=ident, event=event, amount_cp=abs(effect), cash_effect_cp=effect,
                     direction='inflow' if inflow else 'outflow', kind='revenue' if inflow else 'expense',
                     status='received' if inflow else 'paid', date=date, account_id=None,
                     source_ref=YEAR_END_SOURCE), 'year end: posting differs from played evidence')
        closing += effect
    require(not expected and closing == 714500 == copper(state['money']['total_gp_sp']),
            'year end: missing posting or cash mismatch')
    require(ledger['endpoint'] == dict(as_of=scene, total_cp=closing, source_ref=YEAR_END_SOURCE,
                                      classification=PROVISIONAL), 'year end: closing cash must stay provisional')
    require(ledger['controlled_cash'] ==
            dict(total_cp=closing, accounts=[], allocation_status=state['money']['allocation_status'])
            and state['money']['allocation_status'].startswith('Provisional'),
            'year end: current purse and allocations unverified')
