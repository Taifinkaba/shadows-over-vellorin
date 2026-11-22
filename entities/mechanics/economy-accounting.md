---
id: economy-accounting
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year852-day1-end-session.md
- changes/chronicles/phase2-06-economic-approval.md
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
  ],
  "approved_economic_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-06-economic-approval.md",
    "authority_refs": {
      "ledger": "state/finance-ledger.json",
      "cash": "party-finances",
      "prices_wages": "service-price-references",
      "property": "property-financial-references",
      "employment_logistics": "payroll-construction-and-trade",
      "settlements": "settlement-services",
      "trade": "settlement-trade",
      "communications": "settlement-communications",
      "law": "justice-and-jurisdiction",
      "guilds": "guild-membership-and-contracts",
      "illicit": "illicit-commerce-design",
      "salvage": "dungeon-exploration"
    },
    "accounting_domains": [
      "cash-ownership",
      "received-revenue",
      "documented-expenses",
      "distributions-and-transfers",
      "assets-and-liabilities"
    ],
    "cash_ownership_categories": [
      "personal",
      "party-controlled",
      "operating",
      "restricted",
      "third-party"
    ],
    "cycle_template": {
      "period": null,
      "beginning_cash": null,
      "inventory_available": null,
      "demand_evidence": null,
      "delivered": null,
      "received_revenue": null,
      "material_costs": null,
      "wages": null,
      "maintenance": null,
      "transportation": null,
      "security": null,
      "taxes": null,
      "other_contractual_expenses": null,
      "net_operating_result": null,
      "approved_distributions": null,
      "internal_transfers": null,
      "ending_cash": null,
      "outstanding_liabilities": null,
      "evidence_refs": null
    },
    "supply_demand_influences": [
      "seasonal-harvest",
      "weather",
      "labor-availability",
      "transport-disruption",
      "political-instability",
      "local-production",
      "storage-loss",
      "quality",
      "competition",
      "negotiation"
    ],
    "sector_integrations": [
      {
        "sector": "agriculture",
        "industry_refs": [
          "eastrun:industry-grain",
          "brackenford:industry-farm-mill"
        ],
        "procedure": "Harvest and milling consume seed, water, labor and fuel; verify dry storage, spoilage and actual grain weight before a sale."
      },
      {
        "sector": "livestock",
        "industry_refs": [
          "eastrun:industry-animals",
          "windmere:industry-pastoral"
        ],
        "procedure": "Fodder, water, welfare, handling labor and breeding cycles limit supply; sheep/wool and horses/feed are distinct stocks, never automatic herd growth."
      },
      {
        "sector": "forestry",
        "industry_refs": [
          "briarfall-crossing:industry-wood",
          "silverbrook:industry-woodland"
        ],
        "procedure": "Verify cutting rights, mature timber, seasoning time and usable yield; offcuts and storage loss reduce finite deliverable stock."
      },
      {
        "sector": "mining",
        "industry_refs": [
          "ironhollow-hold:industry-metals"
        ],
        "procedure": "Rights, ore grade, safe extraction, fuel and smelting yield constrain production; a deposit is no recovered ore."
      },
      {
        "sector": "quarrying",
        "industry_refs": [
          "stoneford:industry-quarry",
          "ironhollow-hold:industry-stone"
        ],
        "procedure": "Block quality, lifting capacity, dressing waste and bridge load constrain usable stone; a commission is no delivered masonry."
      },
      {
        "sector": "smithing",
        "industry_refs": [
          "ironhollow-hold:industry-metals",
          "brackenford:industry-services"
        ],
        "procedure": "Customer-owned material stays segregated; iron, fuel, skill and workshop capacity constrain output and repair queues."
      },
      {
        "sector": "textiles",
        "industry_refs": [
          "rivermere:industry-textiles",
          "windmere:industry-pastoral",
          "caelthorne:industry-luxury-crafts"
        ],
        "procedure": "Wool/flax, dyes, water and drying constrain cloth and sailcloth; finished quality and waste require evidence."
      },
      {
        "sector": "fisheries",
        "industry_refs": [
          "rivermere:industry-fish",
          "southbank-landing:industry-river-food"
        ],
        "procedure": "Catch and lawful access must be verified; spoilage and preservation consume salt, labor and storage capacity."
      },
      {
        "sector": "river-transport",
        "industry_refs": [
          "rivermere:industry-shipping",
          "southbank-landing:industry-river-food"
        ],
        "procedure": "Cargo custody, willing crew, landing rights, water level and navigable channels must be verified; geography supplies no barge schedule."
      },
      {
        "sector": "caravans",
        "industry_refs": [
          "briarfall-crossing:industry-wagons",
          "eastrun:industry-animals"
        ],
        "procedure": "Repair capacity, sound vehicles, feed, driver and guard contracts constrain loads; wagon hire excludes driver/feed and creates no caravan."
      },
      {
        "sector": "healing-supplies",
        "industry_refs": [
          "silverbrook:industry-woodland",
          "brackenford:industry-services"
        ],
        "procedure": "Identification, lawful gathering, shelf life, safe storage and practitioner competence constrain saleable herbs; no treatment outcome is guaranteed."
      },
      {
        "sector": "lodging",
        "industry_refs": [
          "brackenford:industry-services"
        ],
        "procedure": "Willing customers, usable rooms/bedding, food and staff capacity constrain delivered nights; vacancy never produces receipts."
      },
      {
        "sector": "retail",
        "industry_refs": [
          "caelthorne:industry-civic-services",
          "eastrun:industry-grain"
        ],
        "procedure": "Only verified titled stock can be sold; consignment ownership, weights, spoilage and customer payment remain separate."
      },
      {
        "sector": "professional-services",
        "industry_refs": [
          "caelthorne:industry-civic-services",
          "ironhollow-hold:industry-stone"
        ],
        "procedure": "Voluntary accepted scope, competence, client delivery and approved expenses precede a fee; certification or referral alone earns nothing."
      }
    ],
    "settlement_owner_refs": [
      "caelthorne",
      "eastrun",
      "briarfall-crossing",
      "rivermere",
      "ironhollow-hold",
      "brackenford",
      "silverbrook",
      "stoneford",
      "southbank-landing",
      "windmere"
    ],
    "actual_cycles": [],
    "actual_conditions": [],
    "automatic_postings": false
  }
}
```

## Phase 2 economic procedures

The five domains are separate reporting views of the sole schema 4 ledger, never new accounts or balances. Current personal/party/operating/restricted ownership allocations remain UNKNOWN; the controlled aggregate does not prove title. Third-party and restricted property cannot fund an unapproved purchase. Forecasts, orders, deposits, borrowings, appraisals and internal transfers are not received business revenue. An unidentified inflow remains unclassified. Document paid expenses separately from incurred-but-unpaid liabilities and unaccepted quotes; an expansion commitment is no contractor invoice. Distributions require authority and reduce the paying account once without creating consolidated income. Avoid counting the same asset at property, inventory and ledger levels.

Each prospective cycle uses the empty template. Establish a period, beginning cash, finite titled inventory and evidenced demand; record actual deliveries and receipts independently, then the seven paid cost classes, net result, authorized distributions/transfers, ending cash and separately evidenced unpaid liabilities. Cash operating result = received revenue minus paid operating costs; it may be positive, negative or zero and is not full accrual profit. Ending cash = beginning cash + received revenue - paid costs - distributions + net internal transfers. Borrowing/capital/deposits need separately classified ledger evidence outside that simplified example. Inventory ending = beginning + actual receipts - deliveries - verified losses, within capacity; services need finite staff/facility capacity. Null is UNKNOWN, never zero. No cycle is completed here, and time creates no customers, production, interest or revenue.

Sector integrations reuse all 17 industry chains, ten settlement owners and their 41 business designs; they neither assign existing operators to new work nor replace the 12 PROPOSED trade relationships. Lodging and retail apply wherever an existing business owner supports that service, without creating a new industry or venue. Every inter-settlement dependency still needs PR 2 logistics, actual willing counterparties and a verified usable route. No road, navigable channel, duration, cargo, demand or current shortage is asserted.

Supply/demand influences are bounded possibilities. A supported event must establish affected location, finite stock/labor/capacity, quality, duration and evidence before a negotiated quote changes. Location, season, transport, labor, law and existing contracts qualify reference prices. No global fixed multiplier, inflation, famine, shortage or boom follows from this design.

Guild references remain in PR 4: apprenticeship can require supervised training/materials; certification and standards can support quality review, referrals and procurement, but do not guarantee work, contracts or revenue. Voluntary contracts must identify training expenses, assessment consent and dispute forum. No enrollment, dues collection or new Wayfarers/Academy assessment occurs; Concord membership stays voluntary.

Illicit commerce uses PR 4's finite contexts. Stolen goods retain original title; counterfeits require quality/authenticity review; smuggling and illegal mining add jurisdiction and recovery risk; fraud and forged contracts do not establish enforceable claims. Extortion, bribery and criminal debt confer no lawful authority; laundering cannot turn an unexplained transfer into revenue or lawful title. Possible loss, restitution, seizure, investigation and contract disputes require actual evidence and lawful process. No crime, fund, debt or stolen inventory is created.

Dungeon salvage remains governed by PR 5 recovery evidence, finite availability, legal title, transport and original inventory provenance. Potential treasure is no asset; appraisal is no sale. Only verified sale receipts less documented transaction costs can affect the sole ledger, once. Protected evidence and third-party goods are not saleable by assumption.

## Year-end event fee

For the Day 365 Grand Festival of the Year’s End, the 25% fee on verified event operating profit replaces the ordinary 22% gross-sales commission for affected sales. Vendor gross of 2,400 gp less 1,200 gp eligible costs yields 1,200 gp operating profit, a 300 gp estate fee and 900 gp retained merchant profit. Vendor gross remains merchant property. The [ledger](../../state/finance-ledger.json) records only the estate fee.
