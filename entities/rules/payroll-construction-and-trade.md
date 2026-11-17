---
id: payroll-construction-and-trade
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/economy-framework-maintenance.md
- state/finance-ledger.json
- entities/mechanics/party-finances.md
- archive/checkpoints/year848-day137-finance-ledger.json
- entities/locations/ashvale-estate.md
- entities/locations/ashvale-lodge.md
- entities/locations/briarstone-cottage.md
- entities/factions/dragon-slayer-academy.md
- entities/mechanics/service-price-references.md
- entities/mechanics/travel-routes.md
- entities/mechanics/guild-network.md
- entities/mechanics/contract-registry.md
- entities/characters/tomas.md
- entities/characters/bren.md
---

# Payroll, commitments, pricing and trade procedures

## Payroll

Tomas manages operations/accounting; Bren construction/maintenance. Preserve existing unnamed adults and lodge helpers Mira15/Joren16/Elsi14, distinct from Mira Thorne. Work is paid; individual rates/pay periods and wages owed remain UNKNOWN. Youth work must be optional, supervised, safe and light, never forge/hazardous/night work. Shelter, meals and schooling are unconditional. No new assignment or free labor is inferred.

Future payroll fields: employee_id (null for sourced unnamed staff), employee_label, employer, job, pay_rate amount+unit, pay_period, hours_or_work, gross_pay, deductions (only established; unknown is null), payment_status, payment_date, ledger_transaction_ref, source_ref/quote, expense_coverage_id. Only a separately sourced actual payment can be linked to an existing ledger transaction; incurred but unpaid payroll is a liability, not a cash deduction. Check employee+period+coverage and existing operating expense coverage before recording wages; an aggregate wage period cannot be charged again as individual wages. Never extrapolate a historical wage band.

## Construction

Statuses are supported vocabulary, not automatic transitions. Record proposal/approval/commitment/progress/payment/completion independently with source/date and contractor/invoice only if known. Approval is not payment; paid is not completed. The317gp expansion is committed/unpaid, payment0, construction not started, still within controlled cash but reducing uncommitted cash. No contractor invoice or new payable is invented. For future records support project/property, estimate, approved scope, committed amount, amount paid, invoice refs, progress source, completion source, status and ledger transaction refs. A paid event must be an actual sourced ledger payment, never a second deduction of an already-paid facility.

## Prices and market proposals

Read Chunk3 service-price-references for the six PROPOSED bands. Historical paid construction is not a current customer quote. Price provenance distinguishes historical transaction, verified current quotation, proposed reference, regional estimate and UNKNOWN. No modifiers are active: shortages, seasons, route distance, competition, taxes, transport, rarity and security risk remain proposed categories requiring bounded approval and a sourced base quotation; no retroactive price edits.

The supplied requirement to preserve separate lodge/springs/information price increases is retained for source verification in the maintenance provenance. Specific rate/base/date are UNKNOWN after targeted search; do not conflate increases with22% eligible merchant commission, invent current quotes, or apply them to excluded merchant/rent categories.

## Trade

Future trade reference fields: supplier_id/source, business_id, route_ids with classification/access evidence, contract_ref, delivery_cost, storage_ref, transport_capacity/source, inventory_owner, customs/tolls with legal source, shipment_id/status, departure/arrival evidence and ledger payment ref. Current supplier/shipment arrays are empty unknowns, not proof no trade exists. Source a functioning route and actual delivery before recording completion; proposed roads are not active supply chains. Read existing road, guild-network and contract-registry owners; no contract accepted or completed here. Unsold stock is an asset in its own ownership domain, not profit. Transport/storage capacity does not imply vacancy or a shipment. Customs/tolls remain UNKNOWN unless established, never automatic taxes.


```json
{
  "schema_version": 1,
  "staff_owner_ref": "entities/locations/ashvale-lodge.md",
  "price_owner_ref": "service-price-references",
  "road_owner_ref": "travel-routes",
  "guild_owner_ref": "guild-network",
  "contract_owner_ref": "contract-registry",
  "new_payroll": [],
  "new_construction": [],
  "suppliers": [],
  "shipments": [],
  "active_price_modifiers": [],
  "automatic_postings": false
}
```
