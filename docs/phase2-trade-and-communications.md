# Settlement trade and communications — Phase 2 PR 2

This guide routes to settlement-trade and settlement-communications; it is not a shipment register or a second message ledger. Industry/supplier facts live in parent settlements, physical routes in their existing road owners, prices in service-price-references, resources in original item/spell/finance owners and actual events in their dated owners/chronicles. Nothing here advances time or certifies current conditions.

## Proposed trade inventory

All twelve relationships are PROPOSED / UNVERIFIED PROPOSAL. They cover all ten settlements. A supplier/buyer type is no named counterparty, order, contract, shipment or income. Even a historical route observation is only a planning dependency here, not verification of a loaded wagon, current passage or reverse journey.

| Origin | Destination | Goods/services | Transport proposal | Route dependency or gap |
|---|---|---|---|---|
| eastrun | caelthorne | Grain, flour and livestock market introductions | wagon | `route-caelthorne-eastrun` |
| briarfall-crossing | eastrun | Lawfully marked timber and wagon materials | wagon | `route-eastrun-briarfall` |
| ironhollow-hold | caelthorne | Tools, ironwork and commissioned weapons | wagon | `route-caelthorne-ironhollow-hold` |
| rivermere | caelthorne | Textiles and merchant carriage services | wagon | `route-caelthorne-rivermere` |
| caelthorne | rivermere | Document copying, education and lawful commission services | mounted-courier | `route-caelthorne-rivermere` |
| brackenford | eastrun | Local flour and farm produce | wagon | No compatible surveyed road/river route |
| silverbrook | briarfall-crossing | Honey, identified herbs and lawful timber | pack-animal | No compatible surveyed road/river route |
| stoneford | caelthorne | Dressed stone and masonry commissions | heavy-wagon | No compatible surveyed road/river route |
| southbank-landing | rivermere | Fish, grain transport and ferry referrals | river-boat | No compatible surveyed road/river route |
| windmere | eastrun | Wool and preserved food | pack-animal | No compatible surveyed road/river route |
| eastrun | ironhollow-hold | Food and animal feed | wagon | No compatible surveyed road/river route |
| rivermere | windmere | Finished cloth in exchange for prospective wool purchases | pack-animal | No compatible surveyed road/river route |

Every relationship identifies the origin-owned industry, supplier type, buyer type, storage/handling, seasonality, legal obligations, finite criminal risks and unresolved operations. No river reach or new road is surveyed here. Empty dependencies mean no known usable path, never free transportation; geographic containment is not a route. Specifically Southbank–Rivermere river commerce remains a commercial proposal with unknown channels/landings, water conditions and permissions. Briarfall–Eastrun’s historical walking report does not verify a wagon passage. On every proposed movement verify full topology, direction, mode/load, weather/season, rests/feed, stock/title, lawful access, carriers, prices and actual delivery before recording outcomes.

## Medieval postal methods

| Method | Design limitations |
|---|---|
| Mounted couriers | Willing rider, suitable horse and riding-compatible route; rest, water/feed and current conditions; no universal speed. |
| Guild messengers | Willing authorized messenger and actual route/access; guild rank grants neither teleportation nor police power. |
| Caravan post | Actual willing carrier and departure; sealed packet/custody, compatible loaded route and space; no automatic daily service. |
| River dispatch boats | Verified navigable reach, water/season, landings, permissions, boat/crew and capacity; no current channel is asserted. |
| Beacon signals | Only shared predefined finite codes; verified staffed towers, sightlines, fuel and weather. No tower chain or text network is installed. |
| Rare limited magic | Existing spell/item function, range, concentration, finite cost, recipient and consent must be checked at the original owner. No new ability, mana pool or instantaneous reply. |

Local venues offer designed bookings/holding points, not current departures. Notice reading may serve people who cannot read; public notices reveal only deliberately shared information, never GM secrets. Courier schedules are intentions that require a real carrier, route and readiness, not a timetable inferred from population.

## Message record and delivery procedure

The empty template names id, sender, recipient, carrier, method, departure date/time, origin/destination, intended route IDs, delivery fee in copper, estimated delivery window (earliest/latest/basis), actual delivery status, distinct dated dispatch/receipt evidence, source, and existing magical rule/resource evidence when relevant. No message is created in this PR. Actual records belong with the original actor/event owner and chronicle, not in an automatically updated postal feed.

1. Verify authority, willing carrier/recipient as applicable, actual last-known positions and an end-to-end compatible route; unknown topology prevents a claim of dispatch readiness.
2. Establish current terrain/weather/season, transport, rest/supply, access and costs. An unknown delivery quote/window remains explicitly unknown with a basis; do not use zero cost or immediate arrival as defaults.
3. Record an actual source-backed departure separately from proposed intent. Use the existing finance authority once for an actual paid fee and the existing resource owner for any actual magical cost.
4. Keep sent, delayed, lost, refused, delivered and acknowledged separate. A dispatch is no receipt or delegation acceptance. Actual delivery requires independent dated evidence; do not manufacture confirmation, replies or completed work.
5. Verify source truth, legal access, current route conditions and timing in human review. Pure validate_dispatch checks shape/route/method/reverse and receipt separation only, with synthetic tests; it sends nothing, resolves nothing and proves no historical event.

The canonical design has messages=[] and a completely empty proposed template. There is no writer, timer, dispatch engine, completed-message archive or new communications ledger. Existing npc-autonomy-and-time and guardian/spell limits remain unchanged.

## Reference prices and wages

The existing service-price-references owner adds nine approved price baselines and five wage references from the player’s Phase2 decisions. Business price_reference_ids in approved_design resolve specifically to approved_references, not to the six archival reference_bands. Approved values are prospective references; they are not current quotes, wage obligations, payroll, payments or changes to an existing contract.

Simple bed5sp/night; private room1gp/night; meal2sp; horse feed/stabling3sp/day; rations5sp/day; herbs8sp/bundle;50feet rope1gp; standard iron sword8gp; local wagon hire8sp/day excluding driver/feed. Daily wages: farm labor2sp; caravan guard5sp; skilled blacksmith6sp; experienced healer8sp; master artisan1–2gp. Old archived bands retain original classification/units; in particular day versus night cannot be silently equated, and broad old skilled-craft bands do not overwrite the specific new role reference. Existing quotes and contracts control their actual scope first. Full pricing/economy implementation remains PR6.

Current cash, unpaid commitments, noncash property and22% eligible lodge commission are unchanged. No source-backed financial event exists merely because someone might produce, carry, work, entertain, gamble or sell.
