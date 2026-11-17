"""Finite, read-only economic design validation; no posting or simulation API."""
import json
import re

APPROVAL = 'changes/chronicles/phase2-06-economic-approval.md'
EXTENSIONS = {'economy-accounting': 'approved_economic_design',
              'property-financial-references': 'approved_property_procedures',
              'payroll-construction-and-trade': 'approved_commercial_procedures',
              'service-price-references': 'approved_service_adjustment'}
DOMAINS = ['cash-ownership', 'received-revenue', 'documented-expenses',
           'distributions-and-transfers', 'assets-and-liabilities']
OWNERSHIP = ['personal', 'party-controlled', 'operating', 'restricted', 'third-party']
AUTHORITIES = dict(ledger='state/finance-ledger.json', cash='party-finances', prices_wages='service-price-references',
                   property='property-financial-references', employment_logistics='payroll-construction-and-trade',
                   settlements='settlement-services', trade='settlement-trade', communications='settlement-communications',
                   law='justice-and-jurisdiction', guilds='guild-membership-and-contracts',
                   illicit='illicit-commerce-design', salvage='dungeon-exploration')
CYCLE_FIELDS = set('period beginning_cash inventory_available demand_evidence delivered received_revenue material_costs wages maintenance transportation security taxes other_contractual_expenses net_operating_result approved_distributions internal_transfers ending_cash outstanding_liabilities evidence_refs'.split())
PROPERTY_FIELDS = set('procedure property seller buyer verified_title consideration jurisdiction consent payment_evidence transfer_date original_owner_update ledger_update evidence_refs'.split())
SHIPMENT_FIELDS = set('seller buyer goods quantity ownership origin destination carrier transport_method verified_route departure expected_delivery_window costs risks receipt settlement_status evidence_refs'.split())
WAGE_FIELDS = set('worker employer role skill work_period contract_consent supervision travel_compensation hazard_premium employer_obligations gross_pay deductions payment_evidence dispute_forum evidence_refs'.split())
COSTS = ('material_costs', 'wages', 'maintenance', 'transportation', 'security', 'taxes', 'other_contractual_expenses')
SECTORS = set('agriculture livestock forestry mining quarrying smithing textiles fisheries river-transport caravans healing-supplies lodging retail professional-services'.split())
INFLUENCES = ['seasonal-harvest', 'weather', 'labor-availability', 'transport-disruption', 'political-instability',
              'local-production', 'storage-loss', 'quality', 'competition', 'negotiation']
PROCEDURES = ['land-purchase', 'building-purchase', 'inheritance', 'lease', 'rent', 'repair', 'construction',
              'appraisal', 'property-tax', 'business-permit', 'ownership-dispute', 'secured-obligation', 'sale',
              'foreclosure', 'lawful-seizure', 'transfer-documentation']
FEES = ['market-fee', 'port-charge', 'trade-tariff', 'property-tax', 'licensing-fee', 'commercial-permit',
        'guild-assessment', 'transport-toll']


def need(condition, message):
    if not condition:
        raise ValueError('phase2 economy: ' + message)


def nonnegative(value):
    need(type(value) is int and value >= 0, 'finite nonnegative integer required; UNKNOWN is not zero')
    return value


def cycle_result(beginning_cash, received_revenue, paid_costs, distributions=0, net_transfers=0):
    """Illustrative cash math only, not a full accrual statement or ledger event."""
    for value in (beginning_cash, received_revenue, distributions):
        nonnegative(value)
    need(isinstance(paid_costs, dict) and set(paid_costs) == set(COSTS), 'complete paid operating costs required')
    for value in paid_costs.values():
        nonnegative(value)
    need(type(net_transfers) is int, 'signed integer internal transfers required')
    result = received_revenue - sum(paid_costs.values())
    ending = beginning_cash + result - distributions + net_transfers
    need(ending >= 0, 'cash cannot be overspent; financing needs separate evidence')
    return dict(cash_operating_result_cp=result, ending_cash_cp=ending)


def remaining_inventory(beginning, received, delivered, losses, capacity):
    for value in (beginning, received, delivered, losses, capacity):
        nonnegative(value)
    need(beginning <= capacity and beginning + received <= capacity, 'storage capacity exceeded')
    remaining = beginning + received - delivered - losses
    need(remaining >= 0, 'finite inventory exceeded')
    return remaining


def require_evidence(record, fields):
    """Completeness guard only; callers must independently authenticate all evidence."""
    need(isinstance(record, dict) and set(record) == fields, 'incomplete transaction fields')
    def supported(value):
        if isinstance(value, bool): return value is True
        if isinstance(value, str): return bool(value.strip()) and value.strip().upper() != 'UNKNOWN'
        if type(value) is int: return value >= 0
        if isinstance(value, (list, dict)):
            values = value.values() if isinstance(value, dict) else value
            return bool(value) and all(supported(v) for v in values)
        return False
    need(all(supported(value) for value in record.values()), 'transaction evidence remains UNKNOWN')
    if 'quantity' in record:
        need(type(record['quantity']) is int and record['quantity'] > 0, 'finite positive shipment quantity required')
    return True


def receipt_classification(transaction):
    """Unclassified/financing/transfer inflows never become received business revenue."""
    kind = transaction.get('kind')
    if transaction.get('direction') == 'inflow' and kind == 'revenue' and transaction.get('status') in ('received', 'paid'):
        return 'received-revenue'
    if transaction.get('direction') == 'outflow' and kind == 'expense' and transaction.get('status') == 'paid':
        return 'documented-expenses'
    if kind in ('internal-transfer', 'distribution'):
        return 'distributions-and-transfers'
    return 'unclassified-cash-movement'


def validate_expansion(root, records, require, repository_file, unique_json):
    def payload(ident):
        p = root / f"entities/{records[ident]['type']}/{ident}.md"
        return json.loads(re.search(r'^```json\n(.*?)\n```$', p.read_text(), re.M | re.S)[1], object_pairs_hook=unique_json)
    owners = {ident: payload(ident) for ident in EXTENSIONS if ident in records}
    present = [ident for ident, key in EXTENSIONS.items() if key in owners.get(ident, {})]
    if not present: return  # Existing historical disposable fixtures remain valid.
    require(len(present) == 4, 'phase2 economy: incomplete approved expansion')
    def ref(ident):
        require(ident in records and records[ident]['visibility'] == 'gm-reference', 'phase2 economy: broken/private authority reference')
    def shape(d, fields):
        require(isinstance(d, dict) and set(d) == set(fields.split()), 'phase2 economy: unexpected design fields')
    def empty(d, fields):
        require(isinstance(d, dict) and set(d) == fields and all(v is None for v in d.values()), 'phase2 economy: empty evidence template cannot enact an event')
    for ident in present:
        ref(ident); d = owners[ident][EXTENSIONS[ident]]
        require(d.get('approval_source_ref') == APPROVAL and APPROVAL in records[ident]['source_refs'], 'phase2 economy: wrong approval provenance')
        repository_file(root, APPROVAL, 'economic approval')
        require(d.get('classification') == ('PLAYER RULING' if ident == 'service-price-references' else 'APPROVED DESIGN'), 'phase2 economy: design is not an actual event')
    a = owners['economy-accounting'][EXTENSIONS['economy-accounting']]
    shape(a, 'classification approval_source_ref authority_refs accounting_domains cash_ownership_categories cycle_template supply_demand_influences sector_integrations settlement_owner_refs actual_cycles actual_conditions automatic_postings')
    require(a['authority_refs'] == AUTHORITIES, 'phase2 economy: competing financial authority')
    for ident in AUTHORITIES.values():
        if ident != 'state/finance-ledger.json': ref(ident)
    require(a['accounting_domains'] == DOMAINS and a['cash_ownership_categories'] == OWNERSHIP, 'phase2 economy: five accounting domains/ownership required')
    require(a['actual_cycles'] == [] and a['actual_conditions'] == [] and a['automatic_postings'] is False, 'phase2 economy: no automatic revenue or current conditions')
    require(a['supply_demand_influences'] == INFLUENCES, 'phase2 economy: bounded possible influences required')
    empty(a['cycle_template'], CYCLE_FIELDS)
    settlements = payload('settlement-services')['approved_design_location_ids']
    require(len(a['settlement_owner_refs']) == 10 and set(a['settlement_owner_refs']) == set(settlements), 'phase2 economy: ten settlement coverage required')
    industry_ids = set(); businesses = set()
    for ident in settlements:
        ref(ident); d = payload(ident)['approved_design']
        industry_ids.update(x['id'] for x in d['industries']); businesses.update(x['id'] for x in d['businesses'])
    require(len(industry_ids) == 17 and len(businesses) == 41, 'phase2 economy: preserve 17 industries/41 businesses')
    sectors = a['sector_integrations']; used = set(); seen = set()
    require(isinstance(sectors, list) and len(sectors) == 14, 'phase2 economy: fourteen sectors required')
    for row in sectors:
        shape(row, 'sector industry_refs procedure')
        require(isinstance(row['sector'], str) and row['sector'] in SECTORS and row['sector'] not in seen, 'phase2 economy: duplicate/unsupported sector')
        seen.add(row['sector']); refs = row['industry_refs']
        require(isinstance(refs, list) and refs and all(isinstance(x,str) for x in refs) and len(refs) == len(set(refs)) and set(refs) <= industry_ids, 'phase2 economy: broken/duplicate industry reference')
        used.update(refs)
        require(isinstance(row['procedure'], str) and row['procedure'].strip(), 'phase2 economy: sector procedure required')
    require(used == industry_ids, 'phase2 economy: industry integration coverage differs')
    p = owners['property-financial-references'][EXTENSIONS['property-financial-references']]
    shape(p, 'classification approval_source_ref law_owner_ref ledger_ref procedures transaction_template actual_transactions new_holdings automatic_postings')
    require(p['law_owner_ref'] == 'justice-and-jurisdiction' and p['ledger_ref'] == AUTHORITIES['ledger'], 'phase2 economy: property authority differs')
    require(p['procedures'] == PROCEDURES, 'phase2 economy: incomplete property procedures')
    empty(p['transaction_template'], PROPERTY_FIELDS)
    require(p['actual_transactions'] == [] and p['new_holdings'] == [] and p['automatic_postings'] is False, 'phase2 economy: no holdings/title/payment events')
    w = owners['payroll-construction-and-trade'][EXTENSIONS['payroll-construction-and-trade']]
    shape(w, 'classification approval_source_ref wage_template shipment_template potential_fee_categories law_owner_ref communications_owner_ref actual_contracts actual_assessments automatic_delivery')
    empty(w['wage_template'], WAGE_FIELDS); empty(w['shipment_template'], SHIPMENT_FIELDS)
    require(w['potential_fee_categories'] == FEES and w['law_owner_ref'] == 'justice-and-jurisdiction' and w['communications_owner_ref'] == 'settlement-communications', 'phase2 economy: jurisdiction/communication authority differs')
    require(w['actual_contracts'] == [] and w['actual_assessments'] == [] and w['automatic_delivery'] is False, 'phase2 economy: no contracts/assessments/delivery')
    s = owners['service-price-references'][EXTENSIONS['service-price-references']]
    shape(s, 'classification approval_source_ref percent eligible_services excluded_services base_tariffs effective_date automatic_application')
    require(type(s['percent']) is int and s['percent'] == 10 and s['eligible_services'] == ['lodge-services','springs-services','information-services'] and s['excluded_services'] == ['merchant-rents'], 'phase2 economy: approved service adjustment scope/rate differs')
    require(s['base_tariffs'] is None and s['effective_date'] is None and s['automatic_application'] is False, 'phase2 economy: price base/date remain UNKNOWN; no automatic tariff')
