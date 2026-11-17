---
id: economy-accounting
type: mechanics
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
---

# Economy accounting and reporting

This is a procedure/template owner, not a ledger. `state/finance-ledger.json` alone owns current detailed cash; party-finances owns checkpoint money. Location, organization and inventory records retain title, facilities and assets. Template fields create no events. All new actual financial events belong in the existing ledger through a separately sourced, approved schema migration; these templates are not a posting engine.

Five domains: cash ownership; revenue received; expenses incurred/paid (separate recognition and settlement); internal transfers/distributions; assets/liabilities. Control, legal ownership, management, custody and spending permission are different facts. Preserve ledger owner labels verbatim; “Theron-managed controlled funds” is not proof of sole personal legal title. Explicitly check personal/party/estate/reserve/restricted/third-party/academy scope and account access before spending.

Use integer copper:1gp=10sp=100cp,1sp=10cp; bool/float values are invalid money. Every future amount needs amount_cp (null only if UNKNOWN), display_amount, currency, source_ref, ownership, status, verified_date (null if unverified). Preserve approximation/original denomination wording as qualification, even if derived display is normalized.

Revenue categories: rooms, meals, stabling, springs, eligible merchant commissions, rent, forge repairs, Lantern Exchange, guild contracts, bakery, storage and other sourced business receipts. Expense categories: wages, supplies/food, maintenance, repairs, security, taxes, construction, transport, equipment and professional services. Categories are not receipts, taxes enacted or unpaid bills. Liability/receivable needs counterparty, source, recognition date, due date if known, settlement reference and status; an estimate is neither payable nor cash. Third-party deposits, restricted evidence and noncash appraisals are excluded from controlled cash.

A future entry needs unique event/transaction IDs, recognition type, ownership scope, source event and quote, period, account references, signed effects, currency and amount metadata. Reuse historical event IDs; count each source event once. Internal transfers require two controlled accounts, zero total effect and revenue_recognized_cp=0. Reserve allocation and purse distribution are transfers, not income. Approved surplus percentages in the estate owner apply once to verified free surplus, never gross receipts or automatically to a month.

Participating eligible on-site merchant gross uses22% estate commission. Exact illustrative100gp gross=22gp estate/78gp merchant before merchant expenses; this example is not posted. If percentage multiplication leaves fractional copper, require an explicit rounding policy rather than silently rounding. Merchant gross/stock remain merchant property. Existing historical10% guild design is not a new estate fee or retroactive deduction.

## Read-only reporting procedure

Run `python scripts/economy.py --report` (optional `--root PATH`); output is derived JSON, never a saved authority. Run repository validation first. Read ledger as_of/qualification, accounts/owner labels, commitments and exclusions. Display controlled, committed and uncommitted separately; unpaid commitments remain in controlled cash. Do not aggregate excluded amounts as a current third-party cash total: several are stale, approximate or noncash.

Report income by sourced period: distinguish modeled eight-period operating reconstruction from actual receipts; current-period revenue/expense/net remain UNKNOWN without receipt coverage. The69gp net posting does not reveal gross revenue or expenses. Derive the historical reconstruction and distribution views from their archived owner, marked already applied; do not re-post. Report the pre-arc reconciliation's opening, classified net inflows/outflows, closing and arithmetic difference, retaining the unitemized125gp bridge as an evidence gap. Arithmetic equality does not prove receipt completeness.

Route assets/equipment/inventory to original owners without a grand appraisal sum. Show known committed obligation separately from payable invoices, plus UNKNOWN wages owed, receivables, other liabilities and current business performance. Include sources/as-of/ownership/status on derived amounts. Never create balancing entries, infer Day181 spending, or expose GM secrets as player knowledge. Detailed campaign reports follow narration-format independently closed disclosures.


```json
{
  "schema_version": 1,
  "ledger_ref": "state/finance-ledger.json",
  "mechanics_owner_ref": "party-finances",
  "currency": {
    "unit": "cp",
    "cp_per_gp": 100,
    "cp_per_sp": 10
  },
  "automatic_postings": false,
  "new_transactions": [],
  "new_payroll": [],
  "new_construction_events": [],
  "new_shipments": [],
  "classification": "CONFIRMED CANON",
  "amount_fields": [
    "amount_cp",
    "display_amount",
    "currency",
    "source_ref",
    "ownership",
    "status",
    "verified_date"
  ],
  "construction_statuses": [
    "proposed",
    "approved",
    "committed",
    "in-progress",
    "partially-paid",
    "paid",
    "completed",
    "canceled"
  ],
  "price_kinds": [
    "historical-transaction",
    "verified-current-quotation",
    "proposed-reference",
    "regional-estimate",
    "unknown"
  ],
  "proposed_modifiers": [
    "supply-shortages",
    "seasonal-conditions",
    "trade-route-distance",
    "competition",
    "local-taxes",
    "transport-cost",
    "rarity",
    "security-risk"
  ]
}
```
