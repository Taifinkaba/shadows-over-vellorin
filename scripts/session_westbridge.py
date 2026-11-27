"""Validate the adopted Westbridge close against the preserved Hollow Veil window."""

from collections import Counter, defaultdict

if __package__:
    from .finance_year853 import INITIATED, validate_year853
    from .validate import WESTBRIDGE_SOURCE, copper, integer, read_json, require
else:
    from finance_year853 import INITIATED, validate_year853
    from validate import WESTBRIDGE_SOURCE, copper, integer, read_json, require

PRIOR = 'archive/checkpoints/year853-hollow-veil'
EXPEDITION_PARTY = {
    'aric-ashvale', 'maeryn-sol', 'lyra-moonvale', 'garrick-vale', 'nyx-thorne',
    'ilyr-varess', 'seren-veylor',
}


def validate_checkpoint(root, state):
    prior = read_json(root / (PRIOR + '.json'))
    require((state['date'], state['time'], state['location'], state['status']) ==
            ('Year 853 Day 52', '20:00', 'Westbridge', 'PAUSED'),
            'Westbridge: approved paused scene differs')
    require(state['theron'] == dict(prior['theron'], hp=104, mp=410)
            and state['resources'] == dict(prior['resources'], staff_mp=180)
            and state['world'] == prior['world'] and state['custody'] == prior['custody'],
            'Westbridge: resources, locks or character/world progression differ')
    for field in ('provisional_historic_gp_sp', 'office_petty_gp_sp'):
        require(state['money'][field] == prior['money'][field], 'Westbridge: historical cash exclusion changed')
    presence = state['context']['companions_present']
    require(len(presence) == len(EXPEDITION_PARTY) and set(presence) == EXPEDITION_PARTY,
            'Westbridge: closing expedition presence differs')
    expected = dict(prior['provenance'], adoption_source_ref=WESTBRIDGE_SOURCE,
                    historical_checkpoint_ref=PRIOR + '.json',
                    exact_room='Grand Council, private meeting room',
                    current_presence=dict(status='VERIFIED', evidence_ref=WESTBRIDGE_SOURCE),
                    current_equipment=dict(status='UNKNOWN', evidence_ref=WESTBRIDGE_SOURCE,
                                           night_sovereign_carried_not_equipped=None))
    recovery = dict(minutes=10, restored_mp=24, usable_ambient_mana=True,
                    uninterrupted=True, scope='personal')
    bridge = state['provenance']['mp_bridge']
    require(bridge['trial_costs_mp'] == [12, 12] and bridge['recovery_events'] == [recovery, recovery],
            'Westbridge: trial costs or qualifying personal recovery intervals differ')
    closing_mp = 386 - sum(bridge['trial_costs_mp'])
    for event in bridge['recovery_events']:
        closing_mp = min(state['theron']['mp_max'], closing_mp + event['restored_mp'])
    require(closing_mp == state['theron']['mp'], 'Westbridge: personal MP fails reconciliation')
    expected['mp_bridge'] = dict(from_mp=386, to_mp=closing_mp, difference_mp=closing_mp - 386,
                                 classification='DAY 52 CONTROLLED TRIALS AND PERSONAL RECOVERY',
                                 recovery_events=[recovery, recovery], trial_costs_mp=[12, 12])
    require(state['provenance'] == expected, 'Westbridge: recovery or observation provenance differs')


def validate_finances(root, state, ledger):
    prior_state = read_json(root / (PRIOR + '.json'))
    prior = read_json(root / (PRIOR + '-finance-ledger.json'))
    prior_academy = read_json(root / (PRIOR + '-dsi-finance-ledger.json'))
    validate_year853(root, prior_state, prior, academy_ledger=prior_academy, disciple_level=3)

    unchanged = set(prior) - {'schema_version', 'as_of', 'source', 'qualification',
                              'previous_ledger_ref', 'controlled_cash', 'transactions',
                              'endpoint', 'bridge'}
    require(set(prior) == set(ledger) and all(ledger[key] == prior[key] for key in unchanged),
            'Westbridge: historical ledger metadata changed')
    scene = dict(prior['as_of'], date=state['date'], annual_day=52, time=state['time'],
                 location=state['location'], session_status=state['status'])
    require(ledger['schema_version'] == 9 and ledger['as_of'] == scene
            and ledger['source'] == WESTBRIDGE_SOURCE
            and ledger['previous_ledger_ref'] == PRIOR + '-finance-ledger.json',
            'Westbridge: ledger source or scene mismatch')
    transactions = ledger['transactions']
    before = prior['transactions']
    require(transactions[:len(before)] == before, 'Westbridge: historical postings changed')
    ids = {row['id'] for row in before}
    contract_ids = {f'WG-853-W{n:02}' for n in range(1, 12)}
    contracts = defaultdict(dict)
    totals = Counter()
    for row in transactions[len(before):]:
        ident, category, amount = row['id'], row['category'], row['amount_cp']
        integer(amount, 'Westbridge posting amount', 1)
        require(ident not in ids and category in {'guild-reward', 'guild-commission', 'expedition-expense'},
                'Westbridge: duplicate or unsupported posting')
        ids.add(ident)
        reward = category == 'guild-reward'
        require(row['cash_effect_cp'] == (amount if reward else -amount)
                and row['direction'] == ('inflow' if reward else 'outflow')
                and row['kind'] == ('revenue' if reward else 'expense')
                and row['status'] == ('received' if reward else 'paid')
                and row['source_ref'] == WESTBRIDGE_SOURCE and row['account_id'] is None
                and row['advance'] is False, 'Westbridge: posting metadata differs')
        totals[category] += amount
        if category != 'expedition-expense':
            contract = row['contract_id']
            suffix = 'reward' if reward else 'commission'
            require(contract in contract_ids and ident == f'{contract}-{suffix}' and row['date'] is None,
                    'Westbridge: contract identity or unverified timestamp differs')
            contracts[contract][category] = amount
    require(set(contracts) == contract_ids and all(
        set(rows) == {'guild-reward', 'guild-commission'}
        and rows['guild-commission'] * 10 == rows['guild-reward'] for rows in contracts.values()
    ), 'Westbridge: each contract requires one gross reward and one 10% commission')
    gross, fees, expenses = (totals[key] for key in ('guild-reward', 'guild-commission', 'expedition-expense'))
    require((gross, fees, expenses) == (450000, 45000, 20200), 'Westbridge: approved posting totals differ')
    opening = prior['controlled_cash']['total_cp']
    gain = gross - fees - expenses
    closing = opening + gain
    require(ledger['bridge'] == dict(opening_cp=opening, gross_cp=gross, guild_commissions_cp=fees,
                                    other_expenses_cp=expenses, net_gain_cp=gain, closing_cp=closing)
            and ledger['endpoint'] == dict(prior['endpoint'], as_of=scene, total_cp=closing,
                                           source_ref=WESTBRIDGE_SOURCE)
            and ledger['controlled_cash'] == dict(total_cp=closing, accounts=[],
                                                 allocation_status=state['money']['allocation_status'])
            and copper(state['money']['total_gp_sp'], 'Westbridge treasury') == closing,
            'Westbridge: controlled cash fails reconciliation')
    validate_academy(root, state, prior_academy)


def validate_academy(root, state, prior):
    academy = read_json(root / 'state/dsi-finance-ledger.json')
    window = academy['westbridge_reconciliation']
    require(set(academy) == set(prior) | {'westbridge_reconciliation'}
            and academy['previous_ledger_ref'] == PRIOR + '-dsi-finance-ledger.json'
            and all(academy[key] == prior[key] for key in prior if key != 'previous_ledger_ref'),
            'Westbridge DSI: historical balances or tithe changed')
    require(window['source_ref'] == WESTBRIDGE_SOURCE and window['tithe_percent'] == 25
            and window['contract_window'] == dict(days=[45, 48], classification='RECONSTRUCTED'),
            'Westbridge DSI: current tithe or provenance differs')
    historical = prior['year853']
    eligible = set(historical['student_distributions']) - INITIATED
    earned = Counter()
    total_tithe = 0
    require(len(window['contracts']) == 4, 'Westbridge DSI: four independent contracts required')
    for number, row in enumerate(window['contracts'], 10):
        participants = row['participants']
        require(row['id'] == f'DSI-853-{number:03}' and len(set(participants)) == len(participants) == 3
                and set(participants) <= eligible, 'Westbridge DSI: contract identity or participants differ')
        paid = row['paid_after_guild_fees_cp']
        integer(paid, 'Westbridge DSI: contract reward', 1)
        tithe, fraction = divmod(paid * window['tithe_percent'], 100)
        share, remainder = divmod(paid - tithe, len(participants))
        require(fraction == remainder == 0 and row['tithe_cp'] == tithe
                and row['student_proceeds_cp'] == paid - tithe, 'Westbridge DSI: incorrect tithe or proceeds')
        total_tithe += tithe
        for student in participants:
            earned[student] += share
    require(total_tithe == window['academy_tithe_cp'] == 9000 and sum(earned.values()) == 27000,
            'Westbridge DSI: approved academy and student receipts differ')
    opening = historical['newly_accounted_cp']
    allocations = dict(historical['allocations_cp'])
    operating = {'food_and_maintenance': 2500}
    development = {'Additional dormitories': 6000}
    allocations['Additional dormitories'] -= development['Additional dormitories']
    closing = opening + total_tithe - sum(operating.values()) - sum(development.values())
    require(window['opening_accounted_cp'] == opening and window['accounted_cp'] == closing
            and window['operating_expenses_cp'] == operating
            and window['development_disbursements_cp'] == development
            and window['remaining_allocations_cp'] == allocations
            and window['unallocated_cp'] == closing - sum(allocations.values())
            and copper(state['context']['academy']['latest_reported_cash_gp_sp'], 'DSI accounted cash') == closing,
            'Westbridge DSI: accounted cash or allocation bridge differs')
    expected = {}
    for student, row in historical['student_distributions'].items():
        opening = row['remaining_cp']
        expected[student] = dict(opening_cp=opening, new_cp=earned[student],
                                 remaining_cp=opening + earned[student])
    require(window['student_distributions'] == expected, 'Westbridge DSI: individual student proceeds differ')
