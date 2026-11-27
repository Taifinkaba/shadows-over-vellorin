"""Validate the Year 853 cash bridge and independent academy operations."""

from collections import Counter
import json
import re

if __package__:
    from .finance_expedition import validate_expedition
    from .validate import YEAR853_SOURCE, copper, integer, keys, read_json, require, unique_json
else:
    from finance_expedition import validate_expedition
    from validate import YEAR853_SOURCE, copper, integer, keys, read_json, require, unique_json

PRIOR = 'archive/checkpoints/year852-day365'
FESTIVAL_TOTALS = {
    'tickets': 27575000, 'commercial': 1639000, 'original': -1015000,
    'wages': -403600, 'infrastructure': -281000, 'utilities': -220000,
    'repairs': -110000, 'provisions': -380000, 'retreat': -12000,
}
INITIATED = {'elias-renn', 'kaela', 'gorren', 'nessa'}
DS_RANKS = ('F', 'E', 'D', 'C', 'B', 'A', 'S', 'S+')
ADVANCES = {'Adventurer opening', 'Dragon quarterfinals', 'Adventurer registration',
            'Dragon registration', 'Commercial plot rentals'}


def validate_year853(root, state, ledger, *, academy_ledger=None, disciple_level=1, registries=None):
    previous = read_json(root / (PRIOR + '-finance-ledger.json'))
    previous_state = read_json(root / (PRIOR + '.json'))
    validate_expedition(root, previous_state, previous)
    keys(ledger, set(previous) | {'previous_ledger_ref'}, 'Year 853 ledger')
    updated = {'schema_version', 'as_of', 'source', 'qualification', 'bridge',
               'endpoint', 'transactions', 'controlled_cash'}
    for key in set(previous) - updated:
        require(ledger[key] == previous[key], f'Year 853: historical {key} changed')
    require(ledger['previous_ledger_ref'] == PRIOR + '-finance-ledger.json'
            and ledger['source'] == state['source'] == YEAR853_SOURCE,
            'Year 853: ledger source mismatch')
    require(state['theron'] == dict(previous_state['theron'], hp=None, mp=None)
            and state['world'] == previous_state['world']
            and state['custody'] == previous_state['custody'],
            'Year 853: unsupported advancement or world change')
    require(state['location'] == 'Hollow Veil sanctuary, Mount Vaelspire'
            and state['status'] == 'ENDED' and state['time'] is None,
            'Year 853: closing scene differs from played evidence')
    for field in ('provisional_historic_gp_sp', 'office_petty_gp_sp'):
        require(copper(state['money'][field], field) == copper(previous_state['money'][field], field),
                'Year 853: historical cash exclusions changed')
    scene = dict(previous['as_of'], date=state['date'], annual_day=None, time=None,
                 location=state['location'], session_status=state['status'])
    require(ledger['as_of'] == scene, 'Year 853: ledger scene mismatch')

    old_rows = previous['transactions']
    all_rows = ledger['transactions']
    require(all_rows[:len(old_rows)] == old_rows, 'Year 853: historical postings changed')
    ids = {row['id'] for row in old_rows}
    totals = Counter()
    names = set()
    advances = {}
    admissions = 0
    transfer = None
    for row in all_rows[len(old_rows):]:
        category = row.get('category')
        require(category in FESTIVAL_TOTALS or category == 'founder-contribution',
                'Year 853: unsupported payment or companion distribution')
        integer(row['amount_cp'], 'Year 853 posting amount', 1)
        amount = row['amount_cp']
        received = category in {'tickets', 'commercial'}
        effect = amount if received else -amount
        foundation = category == 'founder-contribution'
        kind = 'transfer' if foundation else 'revenue' if received else 'expense'
        name_key = (category, row['name'])
        require(row['id'] not in ids and name_key not in names, 'Year 853: duplicate posting')
        ids.add(row['id'])
        names.add(name_key)
        require(type(row.get('cash_effect_cp')) is int and row['cash_effect_cp'] == effect
                and row['source_ref'] == YEAR853_SOURCE and row['account_id'] is None
                and row['date'] is None and row['kind'] == kind
                and row['direction'] == ('inflow' if received else 'outflow')
                and row['status'] == ('received' if received else 'paid'),
                'Year 853: posting metadata differs')
        is_advance = row['name'] in ADVANCES
        require(row['advance'] is is_advance, 'Year 853: advance receipts must be counted once')
        if is_advance:
            advances[row['name']] = amount
        if category == 'tickets':
            counts, prices = row['admissions'], row['prices_cp']
            require(len(counts) == len(prices) == 3, 'Year 853: ticket tiers')
            for entry in counts + prices:
                integer(entry, 'Year 853: ticket count or price', 1)
            require(sum(n * price for n, price in zip(counts, prices)) == amount,
                    'Year 853: ticket receipt does not match tiers')
            admissions += sum(counts)
        if category == 'wages':
            require(row['workers'] * row['days'] * row['daily_cp'] == amount,
                    'Year 853: ordinary labor amount differs')
        if category in {'wages', 'infrastructure', 'utilities', 'repairs', 'provisions'}:
            require(row.get('reconstruction') is True, 'Year 853: reconstructed expense provenance')
        if foundation:
            require(transfer is None and row.get('counterparty') == 'dragon-slayer-academy',
                    'Year 853: duplicate or misdirected founder transfer')
            transfer = row
        totals[category] += effect

    require(admissions == 25550 and set(advances) == ADVANCES and sum(advances.values()) == 2227000,
            'Year 853: ticket admissions or advance receipts differ')
    require(dict(totals) == dict(FESTIVAL_TOTALS, **{'founder-contribution': -120000}),
            'Year 853: festival totals or contribution differ')
    opening = previous['controlled_cash']['total_cp']
    gross = totals['tickets'] + totals['commercial']
    expenses = -sum(v for k, v in totals.items() if k in FESTIVAL_TOTALS and v < 0)
    closing = opening + sum(totals.values())
    require(ledger['bridge'] == dict(opening_cp=opening, gross_cp=gross,
                                    festival_expenses_cp=expenses, founder_contribution_cp=120000,
                                    closing_cp=closing), 'Year 853: financial bridge differs')
    require(closing == copper(state['money']['total_gp_sp'], 'Year 853 controlled cash')
            and ledger['controlled_cash'] == dict(total_cp=closing, accounts=[],
                                                   allocation_status=state['money']['allocation_status'])
            and ledger['endpoint'] == dict(as_of=scene, total_cp=closing, source_ref=YEAR853_SOURCE,
                                             classification='RECONCILED CONTROLLED TREASURY'),
            'Year 853: controlled cash or allocation differs')
    validate_academy(root, state, transfer, ledger=academy_ledger, disciple_level=disciple_level, registries=registries)


def validate_academy(root, state, transfer, *, ledger=None, disciple_level=1, registries=None):
    previous_file = PRIOR + '-dsi-finance-ledger.json'
    previous = read_json(root / previous_file)
    if ledger is None:
        ledger = read_json(root / 'state/dsi-finance-ledger.json')
    keys(ledger, set(previous) | {'previous_ledger_ref', 'prospective_tithe_percent', 'year853'},
         'Year 853 independent DSI ledger')
    require(ledger['schema_version'] == 2 and ledger['previous_ledger_ref'] == previous_file
            and ledger['prospective_tithe_percent'] == 25, 'DSI: prospective tithe is 25%')
    require(all(ledger[k] == v for k, v in previous.items() if k != 'schema_version')
            and ledger['tithe_percent'] == 10 and ledger['treasury_total_cp'] is None,
            'DSI: historical ledger, tithe and treasury status must be retained')
    window = ledger['year853']
    require(window['source_ref'] == YEAR853_SOURCE and window['historical_tithe_percent'] == 10,
            'DSI: played contracts use historical tithe')
    earned = Counter()
    tithe = 0
    for number, contract in enumerate(window['contracts'], 1):
        require(contract['id'] == f'DSI-853-{number:03}', 'DSI: duplicate or unexpected contract')
        start, end = contract['days']
        integer(start, 'DSI contract start', 1)
        integer(end, 'DSI contract end', 1)
        require(start <= end <= state['calendar']['latest_numbered_day'], 'DSI: invalid contract dates')
        people = contract['participants']
        require(people and len(people) == len(set(people)), 'DSI: duplicate or absent participants')
        gross = contract['gross_paid_cp']
        integer(gross, 'DSI contract reward', 1)
        fee, fraction = divmod(gross * window['historical_tithe_percent'], 100)
        share, remainder = divmod(gross - fee, len(people))
        require(fraction == remainder == 0, 'DSI: equal whole-copper shares after tithe')
        tithe += fee
        for person in people:
            earned[person] += share
    distributions = window['student_distributions']
    require(len(window['contracts']) == 9 and tithe == 8500 and sum(earned.values()) == 76500
            and set(distributions) == set(earned), 'DSI: contract totals or recipients differ')
    for person, row in distributions.items():
        integer(row['purchases_cp'], 'DSI paid purchase')
        integer(row['remaining_cp'], 'DSI remaining recent earnings')
        require(row['earned_cp'] == earned[person] == row['purchases_cp'] + row['remaining_cp'],
                f'DSI: incorrect individual distribution for {person}')
    require(sum(r['purchases_cp'] for r in distributions.values()) == 26700, 'DSI: equipment purchases differ')
    costs = sum(window['operating_expenses_cp'].values())
    contribution = window['founder_contribution_cp']
    allocated = sum(window['allocations_cp'].values())
    require(costs == 6500 and contribution == allocated == transfer['amount_cp']
            and window['founder_transfer_id'] == transfer['id']
            and window['development_disbursements_cp'] == 0,
            'DSI: transfer reconciliation and unspent allocations')
    accounted = tithe - costs + contribution
    require(accounted == window['newly_accounted_cp'] and window['unallocated_cp'] == accounted - allocated
            and accounted == copper(state['context']['academy']['latest_reported_cash_gp_sp'], 'DSI funds')
            and state['context']['academy']['included_in_party_total'] is False,
            'DSI: separate documented-period cash balance')

    academy = (root / 'entities/factions/dragon-slayer-academy.md').read_text()
    match = re.search(r'```dsi-roster\n(.*?)\n```', academy, re.S)
    require(match is not None, 'DSI: roster missing')
    roster = registries["roster"] if registries is not None else json.loads(match[1], object_pairs_hook=unique_json)
    known = {row['id'] for row in read_json(root / 'index.json')['entries'] if row['type'] == 'characters'}
    registered = {person for person, row in roster.items() if row['guild_rank'] is not None}
    require(len(roster) == 19 and set(roster) <= known and len(registered) == 10
            and registered == set(earned) and all(roster[p] == dict(guild_rank='E', general_level=2)
                                                    for p in INITIATED),
            'DSI: independent enrollment and Guild roster differ')
    progression = (root / 'entities/mechanics/way-of-the-dragon.md').read_text()
    registry = re.search(r'```dragon-slayer-registry\n(.*?)\n```', progression, re.S)
    require(registry is not None, 'DSI: Dragon Slayer registry missing')
    disciples = registries["disciples"] if registries is not None else json.loads(registry[1], object_pairs_hook=unique_json)
    require(set(disciples) == INITIATED, 'DSI: four consenting initiates')
    for row in disciples.values():
        level = row['level']
        integer(level, 'Dragon Slayer level', 1)
        require(level <= 40 and row['rank'] in DS_RANKS
                and DS_RANKS.index(row['rank']) <= (level - 1) // 5,
                'DSI: Dragon Slayer eligibility does not grant rank')
        require(row == dict(rank='F', level=disciple_level), 'DSI: rank and level require documented certification')
