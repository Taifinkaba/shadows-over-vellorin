"""Read-only economy templates and derived reports. No posting or write API."""
import argparse
import json
from pathlib import Path
import re

HELPERS = {'economy-accounting', 'business-financial-references', 'property-financial-references',
           'payroll-construction-and-trade'}
AMOUNT_FIELDS = {'amount_cp', 'display_amount', 'currency', 'source_ref', 'ownership', 'status', 'verified_date'}
STATUSES = ['proposed', 'approved', 'committed', 'in-progress', 'partially-paid', 'paid', 'completed', 'canceled']
PRICE_KINDS = ['historical-transaction', 'verified-current-quotation', 'proposed-reference', 'regional-estimate', 'unknown']
MODIFIERS = ['supply-shortages', 'seasonal-conditions', 'trade-route-distance', 'competition', 'local-taxes',
             'transport-cost', 'rarity', 'security-risk']


def check(condition, message):
    if not condition:
        raise ValueError('economy: ' + message)


def cp(value, nullable=False):
    check((nullable and value is None) or (type(value) is int and value >= 0), 'nonnegative integer copper required')
    return value


def copper(gp=0, sp=0, copper_pieces=0):
    for value in (gp, sp, copper_pieces): cp(value)
    return gp * 100 + sp * 10 + copper_pieces


def display(value):
    cp(value)
    return f'{value // 100} gp {(value % 100) // 10} sp {value % 10} cp'


def commission(gross_cp):
    cp(gross_cp)
    check(gross_cp * 22 % 100 == 0, 'fractional copper requires explicit rounding policy')
    estate = gross_cp * 22 // 100
    return {'merchant_gross_cp': gross_cp, 'estate_revenue_cp': estate, 'merchant_share_cp': gross_cp-estate}


def amount(value, source_ref, ownership, status, verified_date=None):
    cp(value, nullable=True)
    return dict(amount_cp=value, display_amount=display(value) if value is not None else 'UNKNOWN', currency='cp',
                source_ref=source_ref, ownership=ownership, status=status, verified_date=verified_date)


def validate_amount(value):
    check(isinstance(value, dict) and set(value) == AMOUNT_FIELDS, 'amount fields differ')
    cp(value['amount_cp'], nullable=True)
    check(value['currency'] == 'cp', 'currency must be cp')
    check(value['display_amount'] == (display(value['amount_cp']) if value['amount_cp'] is not None else 'UNKNOWN'),
          'display does not match copper')
    for field in ('source_ref', 'ownership', 'status'):
        check(isinstance(value[field], str) and bool(value[field].strip()), f'{field} required')
    check(value['verified_date'] is None or isinstance(value['verified_date'], str) and bool(value['verified_date'].strip()),
          'invalid verified date')


def source_evidence(root, reference, quote):
    # Reuse normalized path and symlink checks from the repository validator.
    if __package__: from .validate import repository_file
    else: from validate import repository_file
    path = repository_file(root, reference, 'economy evidence')
    check(isinstance(quote, str) and bool(quote.strip()) and quote in path.read_text(), 'source quote missing')


def validate_transactions(rows, accounts, root, historical_event_ids=()):
    """Validate a prospective batch only, never insert it or change balances.

    File/quote checks establish evidence location, not event truth; human approval
    and a separately reviewed ledger-schema migration remain necessary.
    """
    check(isinstance(rows, list), 'transactions must be a list')
    ids, events = set(), set(historical_event_ids)
    fields = {'id', 'event_id', 'kind', 'account_id', 'to_account_id', 'amount', 'source_quote',
              'ownership_scope', 'revenue_recognized_cp', 'status', 'period'}
    for row in rows:
        check(isinstance(row, dict) and set(row) == fields, 'transaction fields differ')
        for field in ('id', 'event_id', 'period'):
            check(isinstance(row[field], str) and bool(row[field].strip()), f'{field} required')
        check(row['id'] not in ids, 'duplicate transaction id'); ids.add(row['id'])
        check(row['event_id'] not in events, 'duplicate or already posted historical event'); events.add(row['event_id'])
        validate_amount(row['amount']); check(row['amount']['amount_cp'] is not None, 'transaction amount unknown')
        check(row['account_id'] in accounts, 'unknown account')
        check(row['ownership_scope'] == 'controlled-cash', 'third-party/noncash cannot be controlled cash')
        check(row['kind'] in ('revenue', 'expense', 'transfer'), 'unsupported cash transaction kind')
        check(row['status'] == 'paid' and row['amount']['status'] == 'paid', 'commitment is not payment')
        check(row['amount']['verified_date'] is not None, 'payment date required')
        check(row['amount']['ownership'] == accounts[row['account_id']]['owner'], 'account ownership mismatch')
        cp(row['revenue_recognized_cp'])
        if row['kind'] == 'transfer':
            check(row['to_account_id'] in accounts and row['to_account_id'] != row['account_id'], 'transfer needs distinct valid accounts')
        else: check(row['to_account_id'] is None, 'nontransfer destination forbidden')
        check(row['revenue_recognized_cp'] == (row['amount']['amount_cp'] if row['kind'] == 'revenue' else 0),
              'transfer/expense is not income')
        source_evidence(root, row['amount']['source_ref'], row['source_quote'])


def validate_payroll(rows, transactions, employee_ids, root, covered_period_ids=()):
    check(isinstance(rows, list), 'payroll must be a list')
    txs = {x['id']: x for x in transactions}
    seen, used_tx = set(), set()
    fields = {'employee_id','employee_label','employer','job','pay_rate','pay_period','hours_or_work','gross_pay',
              'deductions','payment_status','payment_date','ledger_transaction_ref','source_ref','source_quote','expense_coverage_id'}
    for row in rows:
        check(isinstance(row, dict) and set(row) == fields, 'payroll fields differ')
        check(row['employee_id'] is None or row['employee_id'] in employee_ids, 'unknown employee')
        for key in ('employee_label','employer','job','pay_period','expense_coverage_id'):
            check(isinstance(row[key], str) and bool(row[key].strip()), 'payroll identity/period/coverage required')
        key = (row['employee_id'] or row['employee_label'], row['pay_period'])
        check(key not in seen and row['expense_coverage_id'] not in covered_period_ids, 'duplicate payroll expense coverage')
        seen.add(key)
        validate_amount(row['gross_pay']); cp(row['deductions'], nullable=True)
        rate=row['pay_rate']
        check(rate is None or isinstance(rate,dict) and set(rate)=={'amount','unit'}, 'pay rate needs amount/unit or UNKNOWN')
        if rate is not None:
            validate_amount(rate['amount'])
            check(isinstance(rate['unit'],str) and bool(rate['unit'].strip()), 'pay rate unit required')
        check(row['hours_or_work'] is None or isinstance(row['hours_or_work'],str) and bool(row['hours_or_work'].strip()), 'work description invalid')
        check(row['gross_pay']['amount_cp'] is not None, 'gross pay unknown')
        if row['deductions'] is not None: check(row['deductions'] <= row['gross_pay']['amount_cp'], 'deductions exceed gross')
        check(row['payment_status'] in ('incurred-unpaid','paid'), 'invalid payroll payment status')
        source_evidence(root, row['source_ref'], row['source_quote'])
        if row['payment_status'] == 'paid':
            ident = row['ledger_transaction_ref']
            check(ident in txs and ident not in used_tx, 'missing/duplicate payroll payment transaction')
            used_tx.add(ident); tx=txs[ident]
            check(tx['kind'] == 'expense' and tx['status'] == 'paid', 'payroll needs paid expense')
            check(row['deductions'] is not None, 'paid payroll deductions must be established')
            check(tx['amount']['amount_cp'] == row['gross_pay']['amount_cp']-row['deductions'], 'payroll payment mismatch')
            check(row['payment_date'] is not None and row['payment_date'] == tx['amount']['verified_date'], 'payroll date mismatch')
        else:
            check(row['payment_date'] is None and row['ledger_transaction_ref'] is None, 'unpaid wage cannot have cash payment')


def load_payload(path, unique_json=None):
    blocks = re.findall(r'^```json\n(.*?)\n```$', path.read_text(), re.M|re.S)
    check(len(blocks) == 1, 'one JSON block required')
    return json.loads(blocks[0], object_pairs_hook=unique_json)


def validate_economy(root, records, require, repository_file, unique_json):
    if not HELPERS.intersection(records): return
    require(HELPERS <= records.keys(), 'economy: incomplete framework')
    def payload(ident):
        return load_payload(root/f"entities/{records[ident]['type']}/{ident}.md", unique_json)
    def ref(ident, kind=None):
        require(isinstance(ident,str) and ident in records, 'economy: broken entity reference')
        require(kind is None or records[ident]['type'] == kind, 'economy: wrong reference type')
        require(records[ident]['visibility'] == 'gm-reference', 'economy: secret reference forbidden')
    def source(path):
        repository_file(root, path, 'economy source')
        if path.startswith('entities/'): ref(Path(path).stem)
    def shape(d, keys):
        expected = set(keys.split())
        for extension in ('approved_economic_design', 'approved_property_procedures', 'approved_commercial_procedures'):
            if isinstance(d, dict) and extension in d: expected.add(extension)
        require(isinstance(d,dict) and set(d)==expected, 'economy: unexpected fields')
        require(type(d.get('schema_version')) is int and d['schema_version']==1, 'economy: invalid schema')
    a=payload('economy-accounting')
    shape(a,'schema_version ledger_ref mechanics_owner_ref currency automatic_postings new_transactions new_payroll new_construction_events new_shipments classification amount_fields construction_statuses price_kinds proposed_modifiers')
    require(a['ledger_ref']=='state/finance-ledger.json' and a['mechanics_owner_ref']=='party-finances','economy: competing financial authority')
    require(a['currency']==dict(unit='cp',cp_per_gp=100,cp_per_sp=10) and all(type(a['currency'][x]) is int for x in ('cp_per_gp','cp_per_sp')), 'economy: incorrect currency')
    require(a['automatic_postings'] is False and all(a[x]==[] for x in ('new_transactions','new_payroll','new_construction_events','new_shipments')), 'economy: maintenance cannot post events')
    require(a['classification']=='CONFIRMED CANON' and set(a['amount_fields'])==AMOUNT_FIELDS and len(a['amount_fields'])==len(AMOUNT_FIELDS), 'economy: invalid classification/amount template')
    require(a['construction_statuses']==STATUSES and a['price_kinds']==PRICE_KINDS and a['proposed_modifiers']==MODIFIERS,'economy: invalid procedure vocabulary')
    b=payload('business-financial-references');shape(b,'schema_version businesses automatic_postings')
    require(b['automatic_postings'] is False and isinstance(b['businesses'],list),'economy: automatic business postings forbidden')
    owners={}
    for ident,record in records.items():
        if record['type']=='locations':
            p=root/f'entities/locations/{ident}.md'
            if '## Settlement and business references — Chunk 3' in p.read_text():
                for business in load_payload(p,unique_json)['businesses']:owners[business['id']]=(ident,business)
    require(len(b['businesses'])==len(owners)==14 and {x['business_id'] for x in b['businesses']}==set(owners),'economy: business coverage/duplicate differs')
    for row in b['businesses']:
        expected={'business_id','parent_location_id','source_ref','classification','identity_fields_from_owner','revenue_categories_from_owner','expense_categories_ref','historical_receipts_ref','historical_qualification','current_receipts_cp','current_expenses_cp','commission_policy_ref','automatic_revenue'}
        require(set(row)==expected,'economy: business fields differ')
        loc,original=owners[row['business_id']]
        require(row['parent_location_id']==loc and row['source_ref']==f'entities/locations/{loc}.md','economy: business owner mismatch')
        require(row['classification']=='CONFIRMED CANON' and row['automatic_revenue'] is False and row['current_receipts_cp'] is None and row['current_expenses_cp'] is None,'economy: fabricated business income/expense')
        require(row['identity_fields_from_owner']==['owner_id','manager_id','operator_id','staff_ids','staff_notes','services','prices','source_refs'] and row['revenue_categories_from_owner'] is True and row['expense_categories_ref']=='economy-accounting','economy: duplicated business authority')
        expected_history=None if loc=='brackenford' else 'archive/checkpoints/year848-day137-finance-ledger.json'
        require(row['historical_receipts_ref']==expected_history,'economy: unsupported historical receipt attribution')
        require(row['historical_qualification']==('UNKNOWN' if expected_history is None else 'Aggregate modeled categories only; no fabricated individual receipt attribution'),'economy: modeled receipt qualification required')
        require(row['commission_policy_ref']==('entities/locations/ashvale-estate.md' if row['business_id']=='ashvale-estate:market' else None),'economy: commission applied to excluded service')
        source(row['source_ref'])
    p=payload('property-financial-references');shape(p,'schema_version properties asset_owner_refs new_ownership_events new_valuations')
    require(p['new_ownership_events']==[] and p['new_valuations']==[], 'economy: no title/value changes in maintenance')
    expected_properties={'ashvale-estate','ashvale-lodge','briarstone-cottage','dragon-slayer-academy'}
    require(isinstance(p['properties'],list) and len(p['properties'])==4 and {x['property_id'] for x in p['properties']}==expected_properties,'economy: property coverage differs')
    for row in p['properties']:
        ident=row['property_id'];ref(ident)
        require(set(row)=={'property_id','source_ref','classification','fact_owner_ref','legal_owner_id','legal_owner_label','manager_id','current_market_value_cp','cash_inclusion','fields_from_owner','unknown_field_policy','source_refs'},'economy: property fields differ')
        require(row['fact_owner_ref']==ident and row['source_ref']==f"entities/{records[ident]['type']}/{ident}.md" and row['source_refs']==[row['source_ref']],'economy: property authority mismatch')
        require(row['legal_owner_id']==('theron-ashvale' if ident in ('ashvale-estate','ashvale-lodge') else None) and row['legal_owner_label']==('House Ashvale' if ident=='briarstone-cottage' else None),'economy: unsupported legal title')
        require(row['manager_id']==('master-beren' if ident=='dragon-slayer-academy' else 'tomas' if ident in ('ashvale-estate','ashvale-lodge') else None),'economy: unsupported property manager')
        for field in ('legal_owner_id','manager_id'):
            if row[field] is not None:ref(row[field],'characters')
        require(row['classification']=='CONFIRMED CANON' and row['current_market_value_cp'] is None and row['cash_inclusion'] is False,'economy: unsupported valuation or property cash')
        require(row['fields_from_owner']==['name','location','property_type','land_area','buildings','facilities','improvements','acquisition','historical_price','appraisal','liabilities','maintenance','revenue_sources','legal_restrictions','last_verified_condition'] and row['unknown_field_policy']=='UNKNOWN, never inferred or zero','economy: property fact routing differs')
        source(row['source_ref'])
    assets={'ashvale-wagon','vanguard-wagon','sovereign-expedition-wagon','night-sovereign','dragon-scales-stock','guild-animal-registry','seven-bells-inventory','shady-salvage','launder','prisoner-custody'}
    require(isinstance(p['asset_owner_refs'],list) and len(p['asset_owner_refs'])==len(assets) and {x['entity_id'] for x in p['asset_owner_refs']}==assets,'economy: asset coverage differs')
    for row in p['asset_owner_refs']:
        require(set(row)=={'entity_id','source_ref','classification','valuation_cp','cash_inclusion'},'economy: asset fields differ')
        ref(row['entity_id']);record=records[row['entity_id']]
        require(row['source_ref']==f"entities/{record['type']}/{row['entity_id']}.md" and row['classification']=='CONFIRMED CANON' and row['valuation_cp'] is None and row['cash_inclusion'] is False,'economy: unsupported asset value/title')
        source(row['source_ref'])
    workflow=payload('payroll-construction-and-trade')
    shape(workflow,'schema_version staff_owner_ref price_owner_ref road_owner_ref guild_owner_ref contract_owner_ref new_payroll new_construction suppliers shipments active_price_modifiers automatic_postings')
    require(workflow['staff_owner_ref']=='entities/locations/ashvale-lodge.md','economy: staffing owner mismatch')
    for key,ident in [('price_owner_ref','service-price-references'),('road_owner_ref','travel-routes'),('guild_owner_ref','guild-network'),('contract_owner_ref','contract-registry')]:
        require(workflow[key]==ident,'economy: workflow authority mismatch');ref(ident)
    require(workflow['automatic_postings'] is False and all(workflow[x]==[] for x in ('new_payroll','new_construction','suppliers','shipments','active_price_modifiers')),'economy: maintenance events/modifiers forbidden')

    if __package__: from .economy_expansion import validate_expansion
    else: from economy_expansion import validate_expansion
    validate_expansion(root, records, require, repository_file, unique_json)


def financial_report(root):
    ledger_ref='state/finance-ledger.json'
    ledger=json.loads((root/ledger_ref).read_text())
    if type(ledger.get('schema_version')) is int and ledger['schema_version'] in (3,4,5,6,7,8,9,10):
        historical_ref=ledger['historical_day156_ref']
        historical=json.loads((root/historical_ref).read_text())
        result=_legacy_financial_report(root,historical,historical_ref)
        result['historical_day156_reconciliation']=result.pop('reconciliation')
        result['as_of']=ledger['as_of'];result['source_ref']=ledger_ref;result['qualification']=ledger['qualification']
        stamp=' '.join(filter(None, (ledger['as_of']['date'], ledger['as_of']['time'])))
        def current(v,pointer,status):return amount(v,ledger_ref+'#'+pointer,'Controlled funds; current subaccount ownership requires verified funding evidence',status,None if provisional else stamp)
        old_accounts=result['cash_position']['accounts'];c=ledger['controlled_cash'];m=ledger['commitments']
        later_endpoint = ledger['schema_version'] in (6,7,8,9,10)
        provisional = ledger.get('endpoint', {}).get('classification') == 'PROVISIONAL PLAYED ENDPOINT'
        working_treasury = ledger.get('endpoint', {}).get('classification') == 'PLAYER-CORRECTED WORKING TREASURY'
        cash_status = ('player-corrected controlled working funds' if working_treasury else
                       'provisional played close; reconciliation pending' if provisional else
                       'player-approved later endpoint' if later_endpoint else
                       'supplied endpoint plus actual recorded events')
        result['cash_position'].update(controlled=current(c['total_cp'],'/controlled_cash/total_cp',cash_status),committed_unpaid=current(m['expansion_outstanding_cp'],'/commitments/expansion_outstanding_cp','unpaid remaining commitment included in controlled cash'),uncommitted=current(m['uncommitted_cp'],'/commitments/uncommitted_cp','uncommitted under existing authority restrictions'),accounts=[dict(id=x['id'],balance=current(x['balance_cp'],'/controlled_cash/accounts','verified current account')) for x in c['accounts']],historical_day156_accounts=old_accounts,allocation_status=c['allocation_status'])
        result['post_arc_transactions']=ledger.get('post_arc_transactions',[])
        if 'approved_session_window' in ledger:
            window = ledger['approved_session_window']
            actual = [t for t in ledger['transactions'] if t['evidence']['source_ref'] == window['source_ref']]
            result['approved_session_cash'] = {
                'window': window,
                'gross_bounty_cp': sum(t['revenue_recognized_cp'] for t in actual),
                'outflows_cp': sum(t['amount_cp'] for t in actual if t['direction'] == 'outflow'),
                'net_cash_effect_cp': sum(t['cash_effect_cp'] for t in actual),
            }
        result['reconciliation']={'endpoint':ledger['endpoint'],('reconciled_endpoint_bridge' if ledger['schema_version'] in (4,5) else 'unexplained_endpoint_bridge'):ledger['bridge'],'actual_transaction_count':len(ledger['transactions']),'current_cash':current(c['total_cp'],'/controlled_cash/total_cp',cash_status),'qualification':'Bridge is a disclosure, not an event, expense or account assignment; historical arc remains unchanged.'}
        if working_treasury:
            result['reconciliation']['working_funds_comparison'] = result['reconciliation'].pop('unexplained_endpoint_bridge')
        if ledger['schema_version'] in (8,9,10):
            result['reconciliation']['year853_cash_bridge'] = result['reconciliation'].pop('unexplained_endpoint_bridge')
            result['reconciliation']['qualification'] = 'Bridge summarizes Year 853 postings. Historical cash gaps retain their original treatment.'
        if ledger['schema_version'] in (7,8,9,10):
            result['reconciliation']['historical_suncrest262_ref'] = ledger['historical_suncrest262_ref']
            result['five_part_completed_projects'] = ledger['completed_projects']
        if later_endpoint:
            result['reconciliation']['historical_day196_ref'] = ledger['historical_day196_ref']
            result['included_lodge_report'] = ledger['included_lodge_report']
        if __package__: from .economy_expansion import DOMAINS, OWNERSHIP, receipt_classification
        else: from economy_expansion import DOMAINS, OWNERSHIP, receipt_classification
        classified = {domain: [] for domain in DOMAINS[1:4]}
        unclassified = []
        for tx in ledger['transactions']:
            domain = receipt_classification(tx)
            (classified[domain] if domain in classified else unclassified).append(tx)
        # Direction alone proves a cash movement, never its economic purpose.
        for domain, field in [('received-revenue', 'actual_received_revenue'), ('documented-expenses', 'actual_paid_expenses')]:
            entries = classified[domain]
            result['income_statement'][field] = current(sum(tx['amount_cp'] for tx in entries), '/transactions', 'Includes player-reported event amounts; vouchers not independently verified' if provisional else 'Explicit classified cash evidence only; not complete period coverage') if entries else None
        result['five_part_accounting'] = {
            'cash-ownership': {'source_ref': ledger_ref+'#/controlled_cash',
                'controlled_cp': c['total_cp'], 'allocation_status': c['allocation_status'],
                'categories': {kind: {'current_amount_cp': None, 'status': 'UNKNOWN; not inferred from aggregate cash'} for kind in OWNERSHIP}},
            'received-revenue': {'source_ref': ledger_ref+'#/transactions', 'classified_transactions': classified['received-revenue'],
                'coverage': 'Only explicit received revenue; no forecasts, financing, transfers or historical net postings'},
            'documented-expenses': {'source_ref': ledger_ref+'#/transactions', 'classified_transactions': classified['documented-expenses'],
                'unpaid_commitments_cp': m['expansion_outstanding_cp'], 'commitment_is_paid_expense': False,
                'other_unpaid_liabilities_cp': None},
            'distributions-and-transfers': {'source_ref': ledger_ref+'#/transactions',
                'classified_transactions': classified['distributions-and-transfers'], 'consolidated_income_effect_cp': 0,
                'historical_distribution_ref': historical_ref+'#/distributions'},
            'assets-and-liabilities': {'property_owner_ref': 'property-financial-references',
                'noncash_appraisals_are_cash': False, 'current_asset_total_cp': None,
                'unpaid_commitments_cp': m['expansion_outstanding_cp'], 'other_liabilities_cp': None}}
        result['unclassified_cash_movements'] = unclassified
        result['five_part_coverage'] = 'Read-only known ledger evidence; empty lists are not complete schedules or zero business performance.'
        return result
    check(type(ledger.get('schema_version')) is int and ledger['schema_version']==2,'report requires supported ledger schema2 or3')
    return _legacy_financial_report(root,ledger,ledger_ref)


def _legacy_financial_report(root,ledger,ledger_ref):
    """Historical schema2 reporting remains available without editing its source."""
    date=ledger['as_of'];current_date=date['date']+' '+date['time']
    def money(value,pointer,owner='Controlled funds; legal owner breakdown remains source-qualified',status='current ledger projection',verified=True):
        return amount(value,ledger_ref+'#'+pointer,owner,status,current_date if verified else None)
    cash=ledger['controlled_cash'];commit=ledger['commitments'];arc=ledger['arc_reconciliation']
    hist_ref=ledger['historical_reconstruction']['ledger'];hist=json.loads((root/hist_ref).read_text())
    model=hist['operating_reconstruction']
    def historic(value,pointer):return amount(value,hist_ref+'#'+pointer,'Estate reconstruction','Already applied player-approved model; not discovered receipts',hist['as_of']['date'])
    known_in=sum(x['delta_cp'] for x in arc['events'] if x['delta_cp']>0)
    known_out=-sum(x['delta_cp'] for x in arc['events'] if x['delta_cp']<0)
    return {'as_of':date,'qualification':ledger['qualification'],'source_ref':ledger_ref,
        'cash_position':{'controlled':money(cash['total_cp'],'/controlled_cash/total_cp'),
            'committed_unpaid':money(commit['expansion_committed_cp']-commit['expansion_paid_cp'],'/commitments','Controlled funds; no project-account allocation inferred','committed, unpaid; construction not started'),
            'uncommitted':money(commit['uncommitted_cp'],'/commitments/uncommitted_cp'),
            'accounts':[dict(id=x['id'],basis=x['basis'],balance=money(x['balance_cp'],f'/controlled_cash/accounts/{i}',x['owner'])) for i,x in enumerate(cash['accounts'])],
            'excluded':[dict(id=x['id'],qualification=x['status'],amount=money(x['amount_cp'],f'/excluded_property/{i}',x['status'],'excluded; not current certification',False)) for i,x in enumerate(ledger['excluded_property'])]},
        'income_statement':{'current_period':None,'actual_received_revenue':None,'actual_incurred_expenses':None,'actual_net_profit':None,
            'coverage':'UNKNOWN; no complete current-period receipts/expense schedule. Net postings do not establish gross income.',
            'historical_model':{'periods':model['periods'],'period_dates':None,'qualification':hist['qualification'],
                'receipts':historic(model['gross_estate_receipts_cp'],'/operating_reconstruction/gross_estate_receipts_cp'),
                'expenses':historic(model['operating_expenses_cp'],'/operating_reconstruction/operating_expenses_cp'),
                'surplus':historic(model['net_distributable_surplus_cp'],'/operating_reconstruction/net_distributable_surplus_cp')}},
        'internal_transfers':{'current_period':None,'known_historical_distribution':{'source_ref':hist_ref+'#/distributions','application_count':hist['distributions']['application_count'],
            'allocations':[dict(account=x['account'],percent=x['percent'],amount=historic(x['amount_cp'],f'/distributions/allocations/{i}')) for i,x in enumerate(hist['distributions']['allocations'])],
            'income_effect_cp':0,'qualification':'Historical surplus distribution already applied, not new income'}},
        'assets_and_liabilities':{'property_owner_ref':'entities/mechanics/property-financial-references.md','inventory_value':None,'receivables':None,'wages_owed':None,'other_payables':None,
            'commitments_source_ref':ledger_ref+'#/commitments','qualification':'No asset valuation total. Commitment is not contractor invoice; independent academy and evidence excluded.'},
        'reconciliation':{'period':'Supplied pre-arc baseline to Day156; exact opening date UNKNOWN',
            'opening':money(arc['opening_cp'],'/arc_reconciliation/opening_cp',status='player-approved pre-arc baseline',verified=False),
            'recorded_net_inflows':money(known_in,'/arc_reconciliation/events',status='aggregate posted net inflows, not gross business revenue',verified=False),
            'recorded_outflows':money(known_out,'/arc_reconciliation/events',status='already paid historical outflows',verified=False),
            'closing':money(arc['closing_cp'],'/arc_reconciliation/closing_cp'),
            'arithmetic_difference_cp':arc['closing_cp']-(arc['opening_cp']+known_in-known_out),
            'event_refs':[ledger_ref+f'#/arc_reconciliation/events/{i}' for i in range(len(arc['events']))],
            'evidence_gaps':[arc['day137_bridge'],'Day181 supplied endpoint not adopted;26gp difference unresolved, no balancing event','Individual wage rates, current business receipts, legal ownership detail and later academy ledger UNKNOWN']}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--report',action='store_true',required=True)
    args=parser.parse_args()
    if __package__:from .validate import validate
    else:from validate import validate
    try:
        validate(args.root)
        print(json.dumps(financial_report(args.root),indent=2))
    except (ValueError,OSError) as exc:
        parser.exit(1,f'ERROR: {exc}\n')


if __name__=='__main__':main()
