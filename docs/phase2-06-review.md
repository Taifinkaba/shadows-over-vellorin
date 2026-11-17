# Phase 2 PR 6 — economy and property review

PR number and URL: [#29](https://github.com/Taifinkaba/shadows-over-vellorin/pull/29).

Base: `19ef74e4642c5307dce7c2883ec1205f828606ef`, latest main including merged PR #24–#28. Branch: `lore/phase2-06-economy-property`. PR 6 only; no merge, PR 7–8 implementation or gameplay.

## Authority map and IDs

No new entity IDs or second ledger. All 243 indexed entities retain their identity and routing. Four existing owners gain one approved extension each, with every preexisting JSON field preserved:

| Owner | New extension / responsibility |
|---|---|
| economy-accounting | approved_economic_design: five domains, finite cycle, ten settlement pointers and fourteen sector integrations |
| property-financial-references | approved_property_procedures: original-owner routing and empty property evidence template |
| payroll-construction-and-trade | approved_commercial_procedures: employment, shipment and jurisdiction-sensitive potential fees |
| service-price-references | approved_service_adjustment: explicitly confirmed scoped 10% player ruling |

The only money authority is `state/finance-ledger.json`, schema 4; party-finances owns ownership/restriction interpretation. Business-financial-references retains its14 historical business pointers, distinct from PR2's41 approved settlement designs. Original location/faction/item owners retain actual title, condition, staff, inventory and historical operations. No new property/business registry is introduced.

Reused authority IDs: party-finances, business-financial-references, settlement-services, settlement-trade, settlement-communications, travel-routes, guild-network, contract-registry, justice-and-jurisdiction, guild-membership-and-contracts, illicit-commerce-design and dungeon-exploration. Original Ashvale estate/lodge/cottage and academy records are unchanged. Reference validation rejects competing authority paths and private/broken routing.

## Prices, wages and lodge scope

The existing PR2 approved_references table remains byte-equivalent as structured data. The following is a review inventory, not another tariff or verified quote:

| Existing reference ID | Prospective baseline |
|---|---|
| simple-bed | 5 sp/night |
| private-room | 1 gp/night |
| hot-meal | 2 sp/meal |
| horse-feed | 3 sp/day |
| rations | 5 sp/day |
| healing-herbs | 8 sp/bundle |
| rope | 1 gp/50 feet |
| iron-sword | 8 gp/sword |
| wagon-hire | 8 sp/day, excluding driver/feed |
| farm-labor | 2 sp/day |
| caravan-guard | 5 sp/day |
| skilled-blacksmith | 6 sp/day |
| experienced-healer | 8 sp/day |
| master-artisan | 1–2 gp/day |

Six older archival bands retain their PROPOSED status and original units. Actual accepted contracts/verified quotes take precedence; quality, location, available stock, season, law, transport, demand and negotiation can qualify baselines. No uniform eight-hour day, hiring, accrual or compensation change is assumed. The employment procedure covers agreed periods/skill, supervised voluntary apprenticeships, seasonal/contract work, travel and hazard terms, employer duties, payment evidence and lawful disputes.

The explicit PR6 instruction resolves earlier uncertainty about the service adjustment's rate:10% for applicable lodge, springs and information services. Original qualifying tariff bases and effective date remain UNKNOWN. Merchant rents remain excluded absent separate canon; no generic baseline is multiplied or historical receipt changed. The distinct22% eligible merchant-gross lodge commission and existing distribution policies remain unchanged. Fractional-copper commissions still require an explicit rounding policy.

## Accounting and finite operations

Current read-only reporting now exposes cash ownership, received revenue, documented expenses, distributions/transfers and assets/liabilities separately. Current allocations among personal, party-controlled, operating and restricted funds remain UNKNOWN; third-party amounts cannot be inferred from controlled cash. Historical allocated balances remain explicitly historical. Empty current schedules do not mean zero business performance.

Direction alone is insufficient to classify an inflow as revenue or an outflow as expense. The report preserves unclassified cash movements separately; explicit receipt/payment classification is needed. Transfers and distributions have zero consolidated income effect. Forecasts, loans, deposits, historical net postings and appraisals are not received business revenue. Unknown current asset totals, receivables and other liabilities remain unknown; unpaid commitments are separately displayed, not paid expenses.

The empty cycle template covers beginning cash/inventory, demand evidence, actual delivery, received revenue, materials, wages, maintenance, transportation, security, taxes, other contractual costs, net operating result, approved distributions/transfers, ending cash and liabilities. Pure example arithmetic supports profit, loss and zero; it does not simulate sales or post entries. The simplified cash model excludes borrowing/capital/deposits unless separately evidenced and classified, and does not claim accrual profit. Finite inventory checks account for receipts, deliveries and losses within verified capacity. No unknown cost is silently zero and no overspending is allowed.

## Settlement economic integration

All41 businesses,17 industry chains and12 PROPOSED trade relationships remain in their original files, unchanged. Fourteen sector links reuse existing scoped industry IDs rather than creating new venues or active suppliers. These are prospective relationships, never orders, deliveries or current demand:

| Existing settlement | Integrated economic constraints and prospective links |
|---|---|
| Caelthorne | Civic/professional and luxury-craft services; client scope and competence precede fees; existing regional grain, tools, textiles and stone dependencies remain proposed. |
| Eastrun | Grain/milling and livestock/feed; finite harvest, water, husbandry and dry storage; existing Caelthorne, Ironhollow and neighboring trade dependencies. |
| Briarfall Crossing | Lawful forestry and wagon repair; cutting rights, seasoning, skilled labor and vehicle capacity; existing Eastrun materials proposal. |
| Rivermere | Shipping, fisheries and textiles; willing crews, navigability, landing rights, salt, dyes and spoilage; existing Caelthorne/Windmere proposals. |
| Ironhollow Hold | Mining/smithing and stone engineering; ore grade, fuel, title, safe extraction, lifting and customer-owned stock; existing Caelthorne output and Eastrun feed proposals. |
| Brackenford | Farm/mill and smith/lodging/herbal services; actual material stock, room/staff capacity and storage; existing Eastrun produce proposal. |
| Silverbrook | Honey, healing herbs and forestry; plant identification, hives, shelf life and lawful gathering; existing Briarfall materials proposal. |
| Stoneford | Quarrying/masonry; block quality, dressing waste and bridge/load limits; existing Caelthorne stone proposal. |
| Southbank Landing | Fisheries, ferries and grain carriage; titled cargo, crew, landing access and fresh-food turnover; existing Rivermere dependency. |
| Windmere | Pastoral wool and preserved food; finite feed, husbandry and storage; existing Eastrun output/Rivermere cloth proposals. |

Retail and lodging procedures apply only where existing business owners support them; they create no new industry. Local production, seasonal harvest/weather, labor availability, transport disruption, politics, storage loss, quality, competition and negotiation are bounded possible influences. Supported localized events and evidence must precede an actual consequence/quote. No new road, duration, navigable channel, current shortage, famine, inflation or automatic boom is asserted.

## Property, trade and institutional compatibility

Property procedures cover land/building purchases, inheritance, leases/rent, repairs/construction, appraisal, taxes/permits, disputes, supported secured obligations, sales, foreclosure/lawful seizure and transfer records. Actual actors, verified title, consideration or explicit lawful noncash basis, competent jurisdiction, consent, dated evidence, payment where applicable and original-owner/sole-ledger updates are required. The completeness guard authenticates nothing by itself. Management/use rights are not title; refundable deposits are not earned rent. A debt creates no automatic seizure or new mortgage.

Actual shipments require identified seller/buyer, finite goods/quantity/title, origin/destination, carrier/method, verified route, departure/window evidence, costs/risks, receipt and settlement status. Verify available stock, storage, load, crossings, lawful access and current conditions. Payment, dispatch, delivery and settlement remain distinct; PR2 communications/logistics apply. No shipment, cargo, caravan or travel time is created.

Guild economics reuse PR4's annual reference dues1/3/8/2gp for apprentice/journeyman/master/traveling membership. No dues collection, certification, membership, hire or new Academy/Wayfarers assessment occurs; Concord remains voluntary. Apprenticeship, standards, referrals, contracts, disputes, procurement and training costs require accepted scope/evidence and do not guarantee income.

PR3 law owns actual jurisdiction. Market/port/tariff/property/license/permit/guild/toll categories create no enacted rate, assessment, debt or collection; no authority may tax beyond its established lawful scope. PR4 illicit contexts constrain stolen/counterfeit goods, smuggling, illegal mining, fraud/forgeries, extortion, bribery, criminal debt and laundering with finite accounting and original title. No illicit funds, secret transaction, stolen stock or criminal event is introduced.

PR5 salvage remains potential until actual recovery, finite availability, legal title, capacity and original inventory provenance are established. Appraisal is no cash; only verified sale receipts/costs may affect the sole ledger once. No loot, asset, sale or recovery is generated.

## Before/after preservation and unknowns

| Check | Before and after |
|---|---|
| Checkpoint | Year848 Suncrest61 Day18119:30, Ashvale Estate |
| Controlled / unpaid / uncommitted | 74590 / 31700 / 42890 cp |
| Current cash allocations | empty accounts; UNRECONCILED / UNKNOWN |
| Cottage | House Ashvale,7 Western Mill Lane,1.4 acres;55gp historical noncash appraisal; completed26gp repairs already accounted |
| Resources | HP100/100, MP400/400, S+ Level5; normal equippedDEF49, conditional51 only when Night Sovereign worn; wearing unknown; Nexus156/180, wagon60/60 |
| Campaign writes | No state, inventory, title, payroll, finance, route, guild, quest or historical-event changes |

The new preservation manifest records base SHA, before/after digests for only four authorized owners, their original JSON payloads, and330 unchanged campaign files. Earlier fixture hashes are updated only for these authorized owner revisions; original before hashes and the prior after hash for the earlier price-owner revision remain recorded. Every legacy owner JSON value, current ledger, historical balance/allocation, restriction, asset, liability and transaction is preserved. Index and unrelated campaign files are unchanged.

Unresolved: current subaccount title/allocation, current receipts/costs/full business performance, property market values, actual new jurisdictions/rates/permits, working tariff bases/date, contracts, stock/capacity, delivery evidence and route conditions. No historical balancing entry, account reconstruction or pricing date is invented.

## Privacy and validation

Repository visibility was observed as public and remains unchanged. New material is safe economic procedure/design and explicit player approval, without credentials, secret answers, private dialogue, hidden locations or player-unknown revelations. Public routing requires gm-reference authorities; source references do not promote GM-only knowledge into narration. Tests enforce declared public-reference structure, not a universal secret detector.

Baseline: normal/optimized validators passed at243 entities;970 tests passed in227.395s on the exact merged-main tree. Implementation: normal and optimized validators passed at243 entities;1000 tests passed in242.214s (970 existing +30 new); focused economy tests passed30/30 in4.895s. Economy report, dashboard generation/freshness, quest readiness, existing finance consistency/preservation and diff checks passed. Ending readiness remains18 pending answer approvals/14 unfilled clue routes..

The30 added deterministic tests cover five domains/ownership, transfer/forecast/commitment separation, appraisal liquidity, operating costs and positive/negative/zero results, finite stock/capacity, property/shipment evidence, prices/wages/commission, jurisdiction-sensitive no-assessment rules, no automatic events, authority/provenance/public routing and source preservation. Existing finance consistency and earlier preservation tests run in the full suite.

No gameplay occurred. No time advance, resource use, income, wage/dues/tax payment, holding/title change, inventory change, shipment, quest resolution, repository visibility action or merge. Stop after this PR for player review.

## Added and modified files

- `changes/CHANGELOG.md`
- `changes/chronicles/phase2-06-economic-approval.md`
- `docs/phase2-06-review.md`
- `docs/property-and-economy-directory.md`
- `entities/mechanics/economy-accounting.md`
- `entities/mechanics/property-financial-references.md`
- `entities/mechanics/service-price-references.md`
- `entities/rules/payroll-construction-and-trade.md`
- `scripts/economy.py`
- `scripts/economy_expansion.py`
- `scripts/settlements.py`
- `tests/fixtures/chunk10-preservation.json`
- `tests/fixtures/chunk7-preservation.json`
- `tests/fixtures/chunk8-preservation.json`
- `tests/fixtures/chunk9-preservation.json`
- `tests/fixtures/day181-final-reconciliation.json`
- `tests/fixtures/day181-migration.json`
- `tests/fixtures/phase2-01-preservation.json`
- `tests/fixtures/phase2-02-preservation.json`
- `tests/fixtures/phase2-03-preservation.json`
- `tests/fixtures/phase2-04-preservation.json`
- `tests/fixtures/phase2-05-preservation.json`
- `tests/fixtures/phase2-06-preservation.json`
- `tests/test_phase2_economy.py`
