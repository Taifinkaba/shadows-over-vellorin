# Phase 2 PR 2 — settlement expansion review

PR number and URL: [#25](https://github.com/Taifinkaba/shadows-over-vellorin/pull/25).

Base: `f3680306d202a96aac0395d73e25afa9d9005b5b`, latest main including merged geography PR 24. Branch: `lore/phase2-02-settlements`. Scope: PR 2 only, no merge or PR 3 implementation.

## Design and inventory

Ten parent-owned settlement designs cover Caelthorne (38,000), Eastrun (4,800), Briarfall Crossing (1,650), Rivermere (12,000), Ironhollow Hold (9,200), Brackenford (approximately 180), Silverbrook (620), Stoneford (940), Southbank/Southbank Landing (2,300) and Windmere (310). Populations are approved estimates, not a census or historical growth; Brackenford retains its original approximate population and 42 historical households. All other household counts remain unknown.

Each profile supplies districts/landmarks, government qualifications, housing/classes, community services, occupations/production, paid employment/skills, customs/festivals, household expense categories, notices, maintenance/emergency possibilities, local problems, communications, trade and lawful/unlawful commercial context. No current festival, emergency, harvest, work offer or operating condition is asserted.

[Settlement and complete business/service inventory](phase2-settlements-and-services.md) lists all 41 scoped entries: Caelthorne 6; Eastrun 5; Briarfall 4; Rivermere 5; Ironhollow 4; Brackenford 5; Silverbrook 3; Stoneford 3; Southbank 4; Windmere 2. Five entries enrich existing Brackenford service IDs, so there are 36 new venue designs and five inherited service enrichments. The larger village list is supported by existing canon, not newly invented extra businesses. Suppliers, customers, staffing, pricing basis, unknown ownership, operating-cost categories and limitations live with each parent record.

Seventeen industry chains identify producers/buyers, raw materials, skills/workers, finite resources, storage, transport, seasonal constraints, shortages and legal/criminal risks. Twelve proposed trade relationships cover all ten settlements, with existing route dependencies or explicit missing-road/river gaps. Proposed trade is not a supply contract or completed shipment. No road, river channel, crossing, distance or current transport service is invented.

[Trade and communication coverage](phase2-trade-and-communications.md) describes mounted couriers, guild messengers, caravan post, river dispatch, limited predefined beacon codes and rare existing-rule magic. The empty template separates sender, recipient, carrier, departure date/time, intended route, fee, reasoned delivery window, actual status and independent dispatch/receipt evidence. No actual dispatch, receipt, fee, reply, communication device or new magical capability is created. Actual future events must remain in their original actor/event owner and chronicle, not a second editable message ledger.

## New and reused IDs

New indexed locations: `silverbrook`, `stoneford`, `southbank-landing`, `windmere`. New mechanics: `settlement-trade`, `settlement-communications`. Total indexed entities: 218.

Six existing settlement identities reused: `caelthorne`, `eastrun`, `briarfall-crossing`, `rivermere`, `ironhollow-hold`, `brackenford`. Existing geography, routing, price, finance, property, NPC and magical owners retain their domains. No new NPC or faction entity is created. Business IDs remain parent-scoped, outside index entity IDs.

Silverbrook and Southbank Landing promote archived concepts rather than duplicate settlements. Southbank is explicitly mapped to the archived full name Southbank Landing for this implementation; no historical rename is asserted. Approved 620/2300 estimates supersede older unplayed 420/900 design estimates only, with archives untouched. Stoneford/Windmere had no indexed owner. All four gain only Vellorin membership, with no realm assignment or exact location. Elderwood is not equated with Elyndor; precise Southbank/Rivermere settlement boundaries remain unverified.

## Lawful and unlawful establishment coverage

The inventory includes general stores, smiths, tailors, bakers, butchers, apothecaries/healers, inns/taverns, stables, warehouses/markets, bathhouses, gambling, pawnshops, couriers/caravans and river transport. Legal classifications are conditional design policies, not enacted laws, actual licenses or legal judgments. PR 3 owns jurisdiction/legal institution development.

Amber Curtain and River Lantern House are non-explicit adult entertainment designs: all entertainment workers must be independent adults, able to refuse, retain control of earnings/documents and leave. Coercion, trafficking, confinement and debt bondage are distinct prohibited abuse. No existing youth staff is assigned. Informal games are only conditionally tolerated after local custom review. Fencing, forgery, smuggling, illegal extraction, exploitative labor/credit, protection demands and corruption remain bounded risk/hooks, not active events or criminal shop operations. No secret leaders, hideouts, guilty officials, investigations or hidden conspiracy connections are stored. All criminal_faction_refs remain empty; authoritative faction dossiers stay in PR 4.

## Source ownership, prices and preservation

Approved design remains explicitly distinct from confirmed historical fields and unresolved proposals. Existing top-level settlement/business JSON payloads are unchanged; approved_design is a separately classified extension in the same parent-owned JSON block. The eleven legacy locality/property profiles and fourteen historical service records retain their original scope. No second town, business, payroll or cash authority is introduced.

The existing price owner gains nine approved price baselines and five wage references, without replacing six archived bands or historical payments. New references do not enact tariffs, quotes, payroll or expenses. Earlier broad skilled-craft bands and per-night stabling retain their scope; specific approved blacksmith/day rates and per-day stabling remain separately qualified. Full economy implementation is deferred to PR 6.

The preservation fixture pins 290 untouched campaign files and records before/after hashes for nine authorized current owners. It also compares old settlement payloads exactly after removal of the approved extension. Older preservation digests are adjusted only for those authorized owner/prefix changes; original historical before-digests and archival evidence remain intact. All 20 route files are byte-for-byte unchanged.

All state, archives, preexisting historical chronicles, characters, creatures, items, quests, factions, companion assignments, spell progression, equipment and property ownership remain unchanged. Brackenford retains Elsbeth Marrin, Ressa Vale, Borin Emberhand, Mara Fenwick, Seren Willowmere and Harlan Wicks, without new duties. House Ashvale retains Briarstone Cottage, its 55 gp noncash valuation and already completed 26 gp repair history; no rent, new repairs, residents or title transfer. Lodge 22% eligible merchant commission remains unchanged.

Checkpoint remains Year 848 Suncrest 61 Day 181 19:30, Ashvale Estate. HP 100/100, MP 400/400, S+/Level 5, normal DEF 49/conditional 51 only with Night Sovereign worn (wearing unknown), Nexus 156/180, wagon 60/60. Controlled 745 gp 9 sp, unpaid expansion 317 gp and uncommitted 428 gp 9 sp remain unchanged under schema 4 finance ledger. Account allocations and current companion positions remain unknown. Locked skills remain locked.

## Unknowns and design limits

Actual owners of new venues, staff, opening schedules, stock, cash, licenses, tax/toll quotes and availability remain unknown. Population estimates are no current census. Exact coordinates, most realm assignments, river course/landing rights, local approach topology and transportation compatibility remain unsurveyed. Commercial partners are types, not new contract counterparties. A historical walking report does not establish wagon passage; proposed routes remain proposed. No active crime, current shortage, guilty official, delivered letter or event outcome is inferred.

The Southbank short-label mapping is explicit and reviewable, while the older full name remains intact. Old unplayed population designs are superseded only in the approved design layer. No unresolved conflict blocks review; route, permission, condition, staffing and operational gaps must be resolved before actual use.

## Privacy and spoiler assessment

GitHub metadata verified the repository is public before editing. Visibility is unchanged. All added design is safe reference material; no hidden mystery answers, secret faction operations or private GM facts are introduced. gm-reference metadata is not access control or proof of player knowledge. This scoped PR does not certify existing public contents spoiler-safe or claim a genuinely private store.

## Test results and readiness

Clean base: normal and optimized validators pass; 795 tests pass (152.307s). No preexisting failures found.

Implementation: normal and optimized validators pass (218 indexed entities); all 832 tests pass (170.474s), including 37 new tests for identity/population/provenance, parents, inherited services, ownership/legal classification, consent, finite supplies, price/wage references, trade route limits, empty messages, dispatch/receipt separation, method compatibility, magic evidence and immutability. No introduced failures remain.

Economy report passes with unchanged 74590 cp controlled cash, 31700 cp unpaid commitment and 42890cp uncommitted; dashboard generation and --check-view freshness verification pass. Quest readiness remains unchanged at 18 pending answer approvals and 14 unfilled clue routes; no ending-readiness claim is made. git diff --check and staged diff checks pass.

Ready for player review. No gameplay occurred: no time advanced, money spent/generated, shipments/messages completed, NPC outcomes, companion movement, quests, custody or resources changed. Open one PR, do not merge, do not begin PR 3, then stop for player review.

## Files added (13)

- `changes/chronicles/phase2-02-settlement-approval.md`
- `docs/phase2-02-review.md`
- `docs/phase2-settlements-and-services.md`
- `docs/phase2-trade-and-communications.md`
- `entities/locations/silverbrook.md`
- `entities/locations/southbank-landing.md`
- `entities/locations/stoneford.md`
- `entities/locations/windmere.md`
- `entities/mechanics/settlement-communications.md`
- `entities/mechanics/settlement-trade.md`
- `scripts/settlement_expansion.py`
- `tests/fixtures/phase2-02-preservation.json`
- `tests/test_phase2_settlements.py`

## Files modified (27)

- `README.md`
- `changes/CHANGELOG.md`
- `docs/settlement-directory.md`
- `docs/validation.md`
- `entities/locations/brackenford.md`
- `entities/locations/briarfall-crossing.md`
- `entities/locations/caelthorne.md`
- `entities/locations/eastrun.md`
- `entities/locations/ironhollow-hold.md`
- `entities/locations/rivermere.md`
- `entities/mechanics/service-price-references.md`
- `entities/mechanics/settlement-services.md`
- `entities/mechanics/world-geography.md`
- `index.json`
- `scripts/settlements.py`
- `scripts/travel.py`
- `scripts/validate.py`
- `tests/fixtures/chunk10-preservation.json`
- `tests/fixtures/chunk3-preservation.json`
- `tests/fixtures/chunk5-preservation.json`
- `tests/fixtures/chunk6-preservation.json`
- `tests/fixtures/chunk7-preservation.json`
- `tests/fixtures/chunk8-preservation.json`
- `tests/fixtures/chunk9-preservation.json`
- `tests/fixtures/day181-final-reconciliation.json`
- `tests/fixtures/day181-migration.json`
- `tests/fixtures/phase2-01-preservation.json`
