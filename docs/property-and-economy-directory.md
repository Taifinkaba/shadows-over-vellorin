# Property and economy retrieval — Chunk 7

This directory routes existing authorities; it owns no balances, titles, payroll or inventory. Resolve IDs through [index](../index.json). Read only needed owner records, their dates and qualification, then supporting evidence where disputed. GM-reference does not establish Theron's knowledge. No hidden main-quest answers are added to this public repository; visibility remains unchanged.

## Authority map

| Domain | Owner / procedure | Boundary |
|---|---|---|
| Current detailed finances | [finance ledger](../state/finance-ledger.json), [party finances](../entities/mechanics/party-finances.md) | Single current ledger3; Day181 endpoint projection is qualified, with Day156 preserved as history. Old tills/reserves are not extra cash. Control does not prove sole personal legal title. |
| Accounting / reports | [economy-accounting](../entities/mechanics/economy-accounting.md), `scripts/economy.py --report` | Read-only five-domain procedure; no posting engine or competing ledger. |
| Business finances | [business-financial-references](../entities/mechanics/business-financial-references.md), [settlement directory](settlement-directory.md) | Fourteen existing parent-scoped references, owner/manager/operator dereferenced from parents. Null current receipts/expenses; no daily profit. |
| Property / equipment | [property-financial-references](../entities/mechanics/property-financial-references.md) | Four property contexts plus original equipment/animal/inventory owners; no appraisal total or ownership change. |
| Payroll / construction / prices / trade | [procedures](../entities/rules/payroll-construction-and-trade.md) | Future evidence templates only; no hires, rates, invoices, shipments or modifiers applied. |
| Price bands | [service-price-references](../entities/mechanics/service-price-references.md) | Six archived PROPOSED bands, no current customer quotations. |
| Road / guild / contracts | [travel-routes](../entities/mechanics/travel-routes.md), [guild directory](guild-and-contract-directory.md) | Proposed roads are not active supply chains; existing payouts are already accounted. |
| Salvage / evidence / custody | Existing Shady Salvage, Launder, Seven Bells inventory and prisoner-custody records | Processing is not title. Restricted evidence, dangerous materials, merchant/prisoner possessions and third-party deposits are unsold and excluded. |

## Property retrieval

| Existing context | What the original owner establishes | Unknown / excluded |
|---|---|---|
| [Ashvale Estate](../entities/locations/ashvale-estate.md) | Theron owns premises; Tomas manages. Additional120 acres paid252gp; businesses and allocation policy retained. | Total acreage/current appraisal, exact legal account ownership and project invoices. No municipal charter. |
| [Ashvale Lodge](../entities/locations/ashvale-lodge.md) | Developed commercial lodge, paid Phase I; forge72gp, research28gp, courtyard18gp paid. Tomas/Bren/staff conditions retained. | Individual rates, current vacancies/quotes; equivalence to older hidden woodland lodge unproven. |
| [Briarstone Cottage](../entities/locations/briarstone-cottage.md) | House Ashvale;7 Western Mill Lane,1.4 acres;55gp historical noncash restitution appraisal; original buildings/condition preserved. | No current market quote, rental receipts or municipal rights. Manager/repair bill unknown; vacant/habitable/minor repairs. |
| [Independent academy](../entities/factions/dragon-slayer-academy.md) | Greyhaven Valley site; Beren management, independent academy operations. | Premises legal title, current cash/deposit/rent and later accounts unknown. Cofounder status does not make funds or premises personal property. |

Each property reference supports name/location/type/owner/manager, land/buildings/facilities/improvements, acquisition/cost/appraisal, liabilities/maintenance/revenue/restrictions and last verified condition through its original authority. Missing detail is UNKNOWN, never a fabricated value. Estate/lodge overlap is not summed; cottage appraisal is not cash. Items/horses/wagons retain inventory IDs and unresolved identity mappings; consumed scales are not restocked. No new asset quantities or valuations.

## Financial report and recognition

Run `python scripts/economy.py --report` from the repository (or `--root PATH`). Validation runs before rendering JSON. No files are written. Report source/as-of/qualification, controlled/committed/uncommitted cash, each source account owner label and exclusions separately. The current ledger3 represents the [adopted Day181 endpoint](day181-checkpoint-ledger-migration.md):745gp9sp controlled,317gp unpaid commitment,428gp9sp uncommitted; current account allocations remain UNKNOWN. The earlier Day156771gp9sp/317gp/454gp9sp position is preserved only as historical evidence.

Income statement shows current-period receipts, incurred costs and profit UNKNOWN where coverage is absent. Eight modeled operating periods remain explicitly a player-approved reconstruction:2160gp receipts,1640gp expenses,520gp surplus/distribution already applied once. The69gp later net posting supplies no invented gross receipts or wage breakdown. Reconciliation reports pre-arc opening, posted net inflows/outflows, closing and arithmetic difference, while retaining the125gp unitemized bridge as an evidence gap. Zero arithmetic difference does not certify receipts.

Transfers, purse distributions and reserve allocations have zero new income effect. Only22% of eligible on-site merchant gross is estate revenue; the100gp illustrative example yields22gp estate/78gp merchant and is never posted. Nonintegral copper commissions need an explicit rounding policy. Do not count merchant gross, unsold stock, noncash appraisal, independent academy or provisional custody money as controlled cash.

## Payroll and commitments

Future payroll carries employee/employer/job/rate/unit/period/hours-work/gross/deductions/status/date/source and transaction/expense-coverage references. Rates and wages owed stay UNKNOWN. Check existing aggregate operating-expense coverage before individual payroll; do not charge twice. Unpaid wages, if later actually established, are liabilities rather than cash outflows. Youth helpers retain optional supervised safe paid light work with unconditional shelter/meals/school; no hazardous/forge/night work.

Construction proposal, approval, commitment, progress, payment and completion need separate evidence. All eight requested statuses are supported. The317gp expansion remains committed/unpaid and not started; no invoice, payment or construction is generated. A commitment reduces uncommitted availability while remaining in controlled cash. Already-paid land, facilities, armor, wagon remainder, provisions and restitution are neither credited nor deducted again.

## Pricing, trade and required decisions

Historical prices, verified quotations, proposed references, regional estimates and unknowns remain distinct. Proposed shortage/season/distance/competition/tax/transport/rarity/security modifiers require approval and sourced base prices; none is active. The supplied separate lodge/springs/information price-increase claim lacks a located rate/base/date; preserve it for verification, never substitute merchant commission or apply it to merchant/rent categories.

Trade templates support suppliers, business IDs, classified routes/access, contract, delivery cost, storage/capacity, inventory ownership and legally sourced customs/tolls, plus actual departure/arrival evidence. No supplier, working route, shipment or sale is inferred from the directory. Guild contract funding/outcome and road classification remain with their existing owners.

Remaining UNKNOWN / REQUIRES APPROVAL: individual wage rates/due dates and payroll coverage, current business receipts/expenses, legal ownership detail for managed accounts, current academy accounts/premises title, property values, precise price-increase sources/quotes, active suppliers/customs/tolls, and any future transaction or schema migration. Day181's supplied745gp9sp controlled/317gp committed/428gp9sp uncommitted is now adopted with unresolved26gp provenance and account allocations; it is not an expense or assumed Blackscale withdrawal. No balancing entries.

## Preservation and limits

Chunk7 changes no existing entity, state or archive bytes. The preservation fixture hashes all preexisting campaign records; tests check state, finance history, equipment, custody, contracts, evidence and property unchanged. Future legitimate play may update owners and deliberately revise maintenance fixtures in a separately reviewed change. Validators prove shape, reference location and arithmetic, not historical truth, ownership law or player knowledge; human evidence review is still required. No gameplay advance, Chunk8 or merge authorization.
