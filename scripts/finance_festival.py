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
