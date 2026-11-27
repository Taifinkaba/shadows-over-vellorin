"""Validate the approved Sovereign Legacy reconciliation and preserved Day 52."""
from collections import Counter
import json
import re

if __package__:
    from . import session_westbridge
    from .validate import DAY145_SOURCE, copper, integer, read_json, require, unique_json
else:
    import session_westbridge
    from validate import DAY145_SOURCE, copper, integer, read_json, require, unique_json

PRIOR = 'archive/checkpoints/year853-day52'
SENIORS = {'elias-renn', 'kaela', 'gorren', 'nessa'}
INITIATED = SENIORS | {'talia-fen', 'rowan-hale'}
CONDITIONAL = {'perrin-oak', 'faye-linden'}
F_LEVEL_TWO = {'dalen-reed', 'sera-willow', 'tobin-marsh', 'elowen-briar'}
F_LEVEL_ONE = {'cedric-vale', 'lethara-mossveil', 'brom-ironroot', 'marielle-fenwick', 'aren-duskwell'}


def validate_checkpoint(root, state):
    previous = read_json(root / (PRIOR + '.json'))
    endpoint = ('Year 853 Day 145', '20:05', "Theron's Commercial Estate", 'PAUSED')
    require(tuple(state[field] for field in ('date', 'time', 'location', 'status')) == endpoint,
            'Sovereign Legacy: approved paused endpoint differs')
    require(state['theron'] == dict(previous['theron'], hp=108, hp_max=108, mp=420, mp_max=420,
                                   level=7, unspent_attributes=2)
            and state['resources'] == previous['resources'] and state['world'] == previous['world']
            and state['custody'] == previous['custody'],
            'Sovereign Legacy: approved progression, defense, locks, wagons or historical custody differ')
    require(all(state['money'][field] == previous['money'][field] for field in
                ('provisional_historic_gp_sp', 'office_petty_gp_sp')),
            'Sovereign Legacy: historical cash exclusions changed')
    evidence = state['provenance']
    require(evidence['historical_checkpoint_ref'] == PRIOR + '.json'
            and evidence['adoption_source_ref'] == DAY145_SOURCE and evidence['exact_room'] == 'Grand Council Hall'
            and evidence['conditional_defense'] == 51
            and evidence['current_equipment'] == previous['provenance']['current_equipment'] | {'evidence_ref': None}
            and evidence['day145_readings'] == dict(hp=108, mp=420, nexus_mp=180, source_ref=DAY145_SOURCE)
            and evidence['mp_bridge'] == dict(from_mp=410,to_mp=420,difference_mp=10,
                    classification='NARRATED ENDPOINTS — INTERMEDIATE BRIDGE INCOMPLETE',recovery_events=[])
            and evidence['current_presence'] == dict(status='UNKNOWN', evidence_ref=None)
            and state['context']['companions_present'] == [],
            'Sovereign Legacy: ending observations or incomplete bridge differ')


def validate_finances(root, state, ledger):
    previous_state = read_json(root / (PRIOR + '.json'))
    previous = read_json(root / (PRIOR + '-finance-ledger.json'))
    previous_academy = read_json(root / (PRIOR + '-dsi-finance-ledger.json'))
    registries = read_json(root / (PRIOR + '-dsi-registries.json'))
    session_westbridge.validate_checkpoint(root, previous_state)
    session_westbridge.validate_finances(root, previous_state, previous, academy=previous_academy,
                                         registries=registries)
    scene = dict(previous['as_of'], date=state['date'], annual_day=145,
                 time=state['time'], location=state['location'], session_status=state['status'])
    require(ledger['schema_version'] == 10 and ledger['previous_ledger_ref'] == PRIOR + '-finance-ledger.json'
            and ledger['as_of'] == scene and ledger['source'] == DAY145_SOURCE,
            'Sovereign Legacy: ledger schema, provenance or scene differs')
    preserved = set(previous) - {'schema_version', 'previous_ledger_ref', 'as_of', 'source', 'qualification',
                                'transactions', 'bridge', 'endpoint', 'controlled_cash', 'commitments'}
    require(all(previous[k] == ledger[k] for k in preserved), 'Sovereign Legacy: historical ledger metadata changed')
    historical = previous['transactions']
    rows = ledger['transactions']
    require(rows[:len(historical)] == historical, 'Sovereign Legacy: historical transactions changed')
    ids = [row['id'] for row in rows]
    require(len(ids) == len(set(ids)), 'Sovereign Legacy: duplicate posting')
    rewards, commissions = {}, {}
    totals, settlements = Counter(), Counter()
    for row in rows[len(historical):]:
        amount, category = row['amount_cp'], row['category']
        integer(amount, 'Sovereign Legacy posting', 1)
        income = category in {'guild-reward', 'estate-net-transfer'}
        require(category in {'guild-reward', 'guild-commission', 'estate-net-transfer', 'session-expense'}
                and row['cash_effect_cp'] == (amount if income else -amount)
                and row['source_ref'] == DAY145_SOURCE and row['account_id'] is None
                and row['advance'] is False
                and (row['kind'], row['direction'], row['status']) ==
                    (('revenue', 'inflow', 'received') if income else ('expense', 'outflow', 'paid')),
                'Sovereign Legacy: unsupported transaction or metadata')
        settlements[row['settlement_day']] += row['cash_effect_cp']
        totals[category] += amount
        if category in {'guild-reward', 'guild-commission'}:
            contract = row['contract_id']
            suffix = 'reward' if income else 'commission'
            require(row['id'] == f'{contract}-{suffix}', 'Sovereign Legacy: duplicate contract posting')
            (rewards if income else commissions)[contract] = amount
    contracts = {f'WG-853-SL{n:02}' for n in range(1, 15)}
    require(set(rewards) == set(commissions) == contracts
            and all(rewards[c] == 10 * commissions[c] for c in contracts),
            'Sovereign Legacy: fourteen contracts with one ten-percent commission each required')
    require(dict(totals) == {'guild-reward': 1225000, 'guild-commission': 122500,
                             'estate-net-transfer': 458000, 'session-expense': 239500},
            'Sovereign Legacy: transaction totals differ')
    reports = ledger['estate_operating_reports']
    require([row['day'] for row in reports] == [70, 100, 143]
            and [row['net_transferred_cp'] for row in reports] == [98000, 150000, 210000]
            and all(sum(row['categories_gp'].values()) * 100 == row['gross_cp']
                    and row['gross_cp'] - row['expenses_cp'] == row['net_transferred_cp'] for row in reports),
            'Sovereign Legacy: estate operating reconciliation differs')
    opening = previous['controlled_cash']['total_cp']
    closing = opening
    balances = {}
    for day in (71, 100, 145):
        closing += settlements[day]
        balances[str(day)] = closing
    require(set(settlements) == {71,100,145} and list(balances.values()) == [27867300,28304300,28892800],
            'Sovereign Legacy: settlement balance differs')
    require(ledger['bridge'] == dict(opening_cp=opening, settlement_balances_cp=balances,
                                    gross_guild_cp=1225000,guild_commissions_cp=122500,
                                    expedition_expenses_cp=59000,estate_net_transfers_cp=458000,
                                    net_gain_cp=closing-opening,closing_cp=closing)
            and ledger['controlled_cash'] == dict(total_cp=closing,accounts=[],
                                                   allocation_status=state['money']['allocation_status'])
            and ledger['endpoint'] == dict(previous['endpoint'],as_of=scene,total_cp=closing,source_ref=DAY145_SOURCE)
            and copper(state['money']['total_gp_sp'], 'Day 145 treasury') == closing,
            'Sovereign Legacy: controlled treasury differs')
    salary = ledger['commitments']['research_salary_review']
    require(salary['potential_outstanding_cp'] == 7500 and salary['paid'] is False
            and sum(row['amount_cp'] for row in rows[len(historical):] if 'salaries' in row['name']) == 15000,
            'Sovereign Legacy: outstanding salary treated as paid')
    validate_academy(root, state, previous_academy)
    validate_registries(root)


def validate_academy(root, state, previous):
    ledger = read_json(root / 'state/dsi-finance-ledger.json')
    require(set(ledger) == set(previous) | {'sovereign_legacy_reconciliation'}
            and ledger['previous_ledger_ref'] == PRIOR + '-dsi-finance-ledger.json'
            and all(ledger[k] == previous[k] for k in previous if k != 'previous_ledger_ref'),
            'Sovereign Legacy DSI: historical ledger changed')
    current = ledger['sovereign_legacy_reconciliation']
    require(current['source_ref'] == DAY145_SOURCE and current['tithe_percent'] == 25
            and set(current['conditional_eligibility']) == CONDITIONAL
            and current['separate_deposit_cp'] == 1500 and current['deposit_disposition'] is None,
            'Sovereign Legacy DSI: tithe, qualification or deposit changed')
    old = previous['westbridge_reconciliation']
    cash, allocated = old['accounted_cp'], sum(old['remaining_allocations_cp'].values())
    student = sum(row['remaining_cp'] for row in old['student_distributions'].values())
    require([x['day'] for x in current['settlements']] == [69,92,129],
            'Sovereign Legacy DSI: settlement sequence differs')
    for row in current['settlements']:
        require(row['opening_cp'] == cash and row['tithe_cp'] * 4 == row['paid_rewards_cp'],
                'Sovereign Legacy DSI: opening cash or tithe mismatch')
        capital = sum(row['capital_cp'].values())
        cash += row['tithe_cp'] - capital - row['staff_cp']
        allocated -= capital
        student += row['paid_rewards_cp'] - row['tithe_cp'] - row['student_purchases_cp']
        require((cash,allocated,cash-allocated,student) ==
                tuple(row[k] for k in ('closing_cp','allocated_cp','unallocated_cp','student_cp')),
                'Sovereign Legacy DSI: settlement arithmetic differs')
    require((cash,allocated,student) == (154750,40000,223050)
            and copper(state['context']['academy']['latest_reported_cash_gp_sp'], 'Day 145 DSI') == cash,
            'Sovereign Legacy DSI: final balances differ')
    balances = current['individual_balances_cp']
    require(set(balances) == INITIATED | F_LEVEL_TWO | CONDITIONAL | {'cedric-vale','lethara-mossveil'}
            and sum(balances.values()) == student, 'Sovereign Legacy DSI: individual totals or recipients differ')
    for amount in balances.values():
        integer(amount, 'Sovereign Legacy DSI individual balance')


def validate_registries(root):
    def registry(path, language):
        text = (root / path).read_text()
        match = re.search(r'```' + language + r'\n(.*?)\n```', text, re.S)
        require(match is not None, 'Sovereign Legacy DSI: missing registry')
        return json.loads(match[1], object_pairs_hook=unique_json)
    roster = registry('entities/factions/dragon-slayer-academy.md','dsi-roster')
    expected = {person:dict(guild_rank=rank,general_level=level)
                for people,rank,level in ((INITIATED,'E',3),(F_LEVEL_TWO,'F',2),(F_LEVEL_ONE,'F',1))
                for person in people}
    require(len(roster) == 27 and {p:r for p,r in roster.items() if r['guild_rank'] is not None} == expected
            and roster['mira-thorne'] == dict(guild_rank=None,general_level=None)
            and {person for person, row in roster.items() if 'conditional_registration' in row} == CONDITIONAL,
            'Sovereign Legacy DSI: ordinary roster or Mira correction differs')
    disciples = registry('entities/mechanics/way-of-the-dragon.md','dragon-slayer-registry')
    require(disciples == {p:dict(rank='F',level=5 if p in SENIORS else 2) for p in INITIATED},
            'Sovereign Legacy DSI: corrected six Dragon Slayers must remain F Rank')
