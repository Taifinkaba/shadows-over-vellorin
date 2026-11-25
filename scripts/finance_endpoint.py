"""Validate the supplied Suncrest endpoint and independent DSI tithe."""
from pathlib import Path

if __package__:
    from .finance_v3 import validate_checkpoint6, validate_finance_v3
    from .validate import copper, integer, read_json, repository_file, require
else:
    from finance_v3 import validate_checkpoint6, validate_finance_v3
    from validate import copper, integer, read_json, repository_file, require

SOURCE = 'changes/chronicles/year848-suncrest262-end-session.md'
DAY196_CHECKPOINT = 'archive/checkpoints/year848-day196.json'
DAY196_LEDGER = 'archive/checkpoints/year848-day196-finance-ledger.json'
DSI_LEDGER = 'state/dsi-finance-ledger.json'


def validate_endpoint(root: Path, state, ledger):
    historical_state = read_json(repository_file(root, DAY196_CHECKPOINT, 'Day 196 checkpoint'))
    historical = read_json(repository_file(root, DAY196_LEDGER, 'Day 196 ledger'))
    closing = validate_finance_v3(root, historical_state, historical)['total_cp']
    validate_checkpoint6(root, historical_state)
    require(state['source'] == ledger['source'] == SOURCE, 'endpoint: source mismatch')
    require((state['date'], state['calendar'], state['time'], state['location'], state['status']) ==
            ('Year 848 Day 382', {'season': 'Suncrest', 'day_of_season': 262}, '18:00',
             'DSI Academy, Greyhaven Valley', 'ENDED'), 'endpoint: approved scene differs')
    scene = dict(date=state['date'], season=state['calendar']['season'],
                 day_of_season=state['calendar']['day_of_season'], time=state['time'],
                 location=state['location'], session_status=state['status'])
    total = copper(state['money']['total_gp_sp'])
    require(total == 299040 and ledger['as_of'] == scene, 'endpoint: approved total or date differs')
    require(ledger['endpoint'] == dict(as_of=scene, total_cp=total, source_ref=SOURCE,
                                      classification='PLAYER-APPROVED LATER PLAYED ENDPOINT'),
            'endpoint: approved source and cash required')
    require(ledger['historical_day196_ref'] == DAY196_LEDGER
            and ledger['bridge'] == dict(historical_closing_cp=closing, endpoint_total_cp=total,
                                        difference_cp=total-closing, classification='UNRESOLVED HISTORICAL GAP',
                                        is_transaction=False, assigned_account_id=None, source_ref=SOURCE),
            'endpoint: gap must remain an unposted difference')
    require(ledger['transactions'] == ledger['account_verifications'] == []
            and ledger['automatic_future_income'] is False,
            'endpoint: do not post unverified transactions or repeat included receipts')
    require(ledger['controlled_cash'] == dict(
        total_cp=total, accounts=[dict(id='theron-personal-purse', balance_cp=10000)],
        allocation_status=state['money']['allocation_status']), 'endpoint: only purse allocation is verified')
    require(ledger['commitments'] == dict.fromkeys(historical['commitments']),
            'endpoint: present commitments are unknown')
    require(ledger['included_lodge_report'] == dict(receipts_cp=16000, expenses_cp=11100, profit_cp=4900,
                                                  already_in_endpoint=True, source_ref=SOURCE),
            'endpoint: lodge profit is already included')
    for key in ('currency', 'historical_day156_ref', 'post_arc_transactions'):
        require(ledger[key] == historical[key], f'endpoint: historical {key} changed')
    holdings = ledger['excluded_property']
    require(holdings[:len(historical['excluded_property'])] == historical['excluded_property'],
            'endpoint: historical exclusions changed')
    new_holdings = holdings[len(historical['excluded_property']):]
    require(len(new_holdings) == 3 and
            {x['id']: x['amount_cp'] for x in new_holdings} == {
                'restricted_stoneward_coinage': 94000, 'restricted_commercial_instruments': 45000,
                'dsi_and_student_funds': None} and all(x['included_in_controlled_cash'] is False for x in new_holdings),
            'endpoint: restricted and DSI property must remain excluded')
    validate_dsi(root, scene, ledger['currency'])


def validate_dsi(root, scene, currency):
    dsi = read_json(repository_file(root, DSI_LEDGER, 'DSI finance'))
    if dsi['schema_version'] == 2:
        dsi = read_json(repository_file(root, 'archive/checkpoints/year852-day365-dsi-finance-ledger.json',
                                        'historical DSI finance'))
    require(dsi['schema_version'] == 1 and dsi['owner_id'] == 'dragon-slayer-academy'
            and dsi['source_ref'] == SOURCE and dsi['as_of'] == scene and dsi['currency'] == currency,
            'DSI finance: ownership or provenance differs')
    contracts = {'Farmstead predator patrol': 3500, 'Merchant road escort': 4500,
                 'Missing supply caravan recovery': 7000, 'Northern route security': 9000}
    rows = dsi['contracts']
    for row in rows:
        for key in ('gross_paid_cp', 'tithe_cp', 'adventurers_retain_cp'):
            integer(row[key], f'DSI finance: {key}')
    require(dsi['tithe_percent'] == 10 and len(rows) == len(contracts) and
            {row['name']: row['gross_paid_cp'] for row in rows} == contracts
            and all(row['tithe_cp'] * 10 == row['gross_paid_cp']
                    and row['adventurers_retain_cp'] + row['tithe_cp'] == row['gross_paid_cp'] for row in rows),
            'DSI finance: paid contract or tithe differs')
    totals = dsi['totals']
    require(totals == {key: sum(row[key] for row in rows)
                       for key in ('gross_paid_cp', 'tithe_cp', 'adventurers_retain_cp')},
            'DSI finance: incorrect contract totals')
    require(dsi['improvements'] == [
        dict(purpose='Dormitory repairs', amount_cp=1400),
        dict(purpose='Practice protection and training equipment', amount_cp=1000)]
        and dsi['improvement_budget_remaining_cp'] == totals['tithe_cp'] -
        sum(item['amount_cp'] for item in dsi['improvements']), 'DSI finance: incorrect improvement budget')
    require(dsi['historical_report'] == dict(cash_cp=3400, refundable_deposit_cp=1500)
            and dsi['treasury_total_cp'] is None and dsi['reversed_proposed_theron_grant_cp'] == 2400
            and dsi['included_in_party_total'] is False and dsi['automatic_future_income'] is False,
            'DSI finance: historical reports and reversed grant must not create cash')
