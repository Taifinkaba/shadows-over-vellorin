"""Validate the corrected Year 852 working treasury and sourced close."""

if __package__:
    from .finance_festival import validate_year_end
    from .validate import copper, integer, keys, read_json, repository_file, require
else:
    from finance_festival import validate_year_end
    from validate import copper, integer, keys, read_json, repository_file, require

SOURCE = 'changes/chronicles/year852-day365-end-session.md'
PRIOR = 'archive/checkpoints/year852-day1'
REWARDS_CP = {
    'WG-852-260': (12000, 1200),
    'WG-852-261': (8500, 850),
    'WG-852-347': (11000, 1100),
    'WG-852-354': (9000, 900),
}
EXPENSES = {
    'year852-expedition-provisions': ('funded-expedition', -950),
    'watchpost-outer-maintenance': ('forgotten-watchpost', -5400),
    'arena-phase-vi': ('arena-phase-vi', -50000),
}


def validate_expedition(root, state, ledger):
    prior_state = read_json(repository_file(root, PRIOR + '.json', 'Day 1 checkpoint'))
    prior = read_json(repository_file(root, PRIOR + '-finance-ledger.json', 'Day 1 ledger'))
    validate_year_end(root, prior_state, prior)
    keys(ledger, set(prior), 'expedition ledger')
    require(ledger['schema_version'] == prior['schema_version']
            and state['source'] == ledger['source'] == SOURCE, 'expedition: source or schema differs')
    require((state['date'], state['time'], state['location'], state['status']) ==
            ('Year 852 Day 365', None, 'Ashvale Estate', 'ENDED')
            and state['calendar'] == dict(annual_day=365, season=None, historical_label='Year 852 Day 365'),
            'expedition: closing scene differs')
    require(state['theron'] == dict(prior_state['theron'], level=6, str=14, con=19,
                                   hp_max=104, mp=351, mp_max=410), 'expedition: last recorded stats differ')
    for field in ('resources', 'world', 'custody'):
        require(state[field] == prior_state[field], f'expedition: unsupported change to {field}')
    require(state['context']['academy'] == prior_state['context']['academy'],
            'expedition: independent academy balances changed')

    updated = {'as_of', 'source', 'qualification', 'bridge', 'endpoint', 'transactions', 'controlled_cash'}
    for field in prior.keys() - updated:
        require(ledger[field] == prior[field], f'expedition: preserved {field} differs')
    scene = dict(date=state['date'], annual_day=365, season=None, time=None,
                 location=state['location'], session_status=state['status'])
    require(ledger['as_of'] == scene, 'expedition: ledger scene differs')
    opening = 534500
    historical = prior['controlled_cash']['total_cp']
    require(ledger['bridge'] == dict(
        historical_closing_cp=historical, opening_cp=opening, difference_cp=opening-historical,
        classification='UNITEMIZED PROVISIONAL ORDINARY CASH TO SUPPLIED WORKING FUNDS COMPARISON',
        is_transaction=False, assigned_account_id=None, source_ref=SOURCE),
        'expedition: working-funds bridge must remain unposted')

    earlier_rows = prior['transactions']
    require(ledger['transactions'][:len(earlier_rows)] == earlier_rows, 'expedition: historical postings changed')
    expected = {ident: ('funded-expedition', gross - fee)
                for ident, (gross, fee) in REWARDS_CP.items()} | EXPENSES
    closing = opening
    for row in ledger['transactions'][len(earlier_rows):]:
        ident = row.get('id')
        require(ident in expected, 'expedition: unsupported or duplicate posting')
        event, effect = expected.pop(ident)
        income = effect > 0
        integer(row.get('amount_cp'), 'expedition amount', 1)
        require(type(row.get('cash_effect_cp')) is int and row == dict(
            id=ident, event=event, amount_cp=abs(effect), cash_effect_cp=effect,
            direction='inflow' if income else 'outflow', kind='revenue' if income else 'expense',
            status='received' if income else 'paid', date=None, account_id=None, source_ref=SOURCE),
            'expedition: posting differs from corrected evidence')
        closing += effect
    require(not expected and closing == 514600 == copper(state['money']['total_gp_sp']),
            'expedition: missing posting or cash mismatch')
    require(ledger['endpoint'] == dict(as_of=scene, total_cp=closing, source_ref=SOURCE,
                                      classification='PLAYER-CORRECTED WORKING TREASURY'),
            'expedition: incorrect endpoint')
    require(ledger['controlled_cash'] == dict(
        total_cp=closing, accounts=[], allocation_status=state['money']['allocation_status']),
        'expedition: account allocations unverified')
