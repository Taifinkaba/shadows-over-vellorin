# Phase 2 approved dungeon/exploration update

Read the [five approved design profiles and reference guide](phase2-dungeons-and-exploration.md) and [PR5 review](phase2-05-review.md) first. The original five scoped proposals now each route to one public mechanics profile, with finite architecture, ecology/hazards, proposed encounters and recovery constraints. Old unapproved-design statements below remain a dated baseline, superseded only for these bounded design fields. No actual location/entrance, route, population, damage, discovery, loot or historical event is instantiated. Original eighteen site/context labels, fourteen historical section records, creatures, salvage/evidence and state remain untouched. Legacy SS remains unresolved outside the unchanged proposed F–S+ scale; final combat integration remains PR8.

---

# Dungeon and exploration retrieval — Chunk 6

The [dungeon registry](../entities/mechanics/dungeon-registry.md) routes 18 existing site/context labels. The [section directory](../entities/mechanics/exploration-sections.md) supplies14 source-bound section handles; [ecology/hazard references](../entities/mechanics/dungeon-ecology-and-hazards.md) point to existing owners. [Design proposals](../entities/mechanics/dungeon-design-proposals.md) and [exploration procedure](../entities/rules/dungeon-exploration.md) provide approval boundaries. Resolve entity IDs through [index.json](../index.json).

These are retrieval references, not a second exploration, inventory, quest or creature-state database. All preexisting entity/state/archive files remain unchanged. No new location or creature entity is created. Site/context count is not a world dungeon census, and a scoped site ID does not turn an ordinary structure into a dungeon.

## Existing sites and identity boundaries

| Site ID suffix (`site:…`) | Original authority / record kind | What remains uncertain |
|---|---|---|
| `ninth-vault` | [Ninth Vault](../entities/locations/ninth-vault.md); investigation site | Exact approach, entrance, room plan, danger rank and current inhabitants |
| `mirror-foundation` | [Mirror Foundation](../entities/locations/mirror-foundation.md); investigation site | Precise structure/access and room state; no invented doorway or identity with another site |
| `hollow-first-hour` | [Hollow of the First Hour](../entities/locations/hollow-first-hour.md), First Hour quest and salvage owners | Whole-site clearance, unexplored areas and source-unspecified present conditions |
| `hollow-veil` | [Hollow Veil](../entities/locations/hollow-veil.md); sanctuary at Mount Vaelspire | Approach and present occupants; not Hollow of the First Hour beneath Mount Elarion |
| `north-return-house` | [North Return House](../entities/locations/north-return-house.md); ordinary structure/investigation site | Current access/occupancy; original cellar findings remain with their owners |
| `northern-depository` | Existing Seven Bells investigation/evidence owners; no standalone location entity | Entrance/coordinates/routes and surveyed sections not supplied here |
| `seven-bells-receiving-chambers` | Existing Seven Bells investigation/salvage reference | Exact topology and relationship to other recorded areas |
| `whisperstone-hollow` | Shady Salvage named-site reference | Region, physical type, entrance, sections and inhabitants |
| `old-copperworks` | Shady Salvage visited-site reference | Physical function, rooms, hazards and degree beyond recorded visit |
| `nine-star-shrine` | Shady Salvage accessible-room reference | Other rooms, precise location, access and site-wide state |
| `vaelspire-observatory` | Shady Salvage lower-room reference | Exact position, approach and identity relative to other Vaelspire structures |
| `northwatch-old-aqueduct` | Shady Salvage infrastructure reference | No automatic identity with the later aqueduct workshop or Seven Bells structures |
| `western-roadside-fortress` | Shady Salvage fortress reference | Which road, entrance, occupation and current danger |
| `frostglass-western-ridge` | Shady Salvage wilderness-area reference | Exact geography, route and current conditions; no unproved regional alias |
| `abbey-bellkeeper-residence` | Shady Salvage ordinary residence reference | No assumption it is an entire dungeon or identical to another abbey site |
| `ravencrest-waystation` | Shady Salvage ordinary waystation reference | Current service/access, exact road and conditions |
| `seven-bells-lower-foundations` | Distinct exploration-area label from Shady Salvage | Not automatically the receiving chambers, a newly separate dungeon or a proven connecting passage |
| `seven-bells-witness-entry` | Existing [historical entrance reference](../entities/locations/seven-bells-witness-entry.md) | No surveyed surface route, wagon passage, universal access or teleport anchor |

Six contexts reuse indexed location entities; twelve remain exact source labels with no invented geography. Separate routing labels do not assert that every Seven Bells context is physically separate or connected. Aliases are empty: common words, related investigations or recovered objects prove neither identity nor a traversable passage. No existing site is relocated.

## Section-state retrieval and revisits

Section IDs use `section:<site>:<recorded-area>`. A source-wide salvage row has a descriptive recorded-area handle; it is not a newly generated one-room plan. Source locators read current authoritative wording rather than store a second mutable status. Existing area identities do not create corridors, floors, hidden rooms, boss areas or exits.

The following are baseline historical observations, not promises of current safety. Always read the linked owner for later explicit updates:

| Scope | Existing observation | Correct interpretation |
|---|---|---|
| Hollow western gallery | Unexplored | Remains unexplored; no generated contents |
| Hollow Keeper quarters | Protected | Protected access; exploration degree UNKNOWN, not automatically unexplored/sealed/cleared |
| Hollow supply annex | Searched/recovered | Searched area; quantities/title/disposition remain in Shady Salvage and Launder; not site-wide clearance |
| Abbey residence / Nine-Star accessible rooms | Searched | Only recorded scope searched; no new rooms or site-wide completion |
| Vaelspire observatory lower rooms / Northwatch aqueduct / western fortress | Unexplored | No prior search, inhabitants, encounter or treasure invented |
| Seven Bells lower foundations / Whisperstone / Frostglass western ridge | Partially explored | Partial exploration, not a full clear |
| Old Copperworks / Ravencrest waystation | Visited | A visit is not complete exploration, clearing or a reset to unexplored |
| North Return House cellar | Inspection recorded | An observation/visit, not certification all spaces were searched or the site cleared |

The normalized vocabulary supports unknown, unexplored, partially explored, visited, explored, cleared, sealed, inaccessible and destroyed. “Searched” maps to explored only for that recorded scope; protected is a separate access observation. Raw historical wording is retained by the reader. Unknown degree does not erase a recorded visit, nor does an unfamiliar label get silently promoted to cleared. No section has an editable duplicate status field.

First Hour's safe resumption remains a specific established objective in its quest owner, separate from gallery exploration and eventual custody matters. Wider quests and sections are not completed by that outcome. Existing historical custody is untouched and not mirrored in a dungeon status table. Returning uses the original state and actual later events rather than automatically resetting rooms, caches, threats or secret discoveries.

## Creatures, ecology and hazard pointers

Four reference contexts are provided: existing Vaeltharion and Aeloryn creature owners, plus named Pale Devourer and Winter Warden references in outstanding-projects. No new creature/group, species, abilities, count, diet, territory, hostility, rank or present location is asserted. Independent guardians are not automatically hostile dungeon inhabitants. Historical context does not imply current presence. Pale Devourer remains contained rather than defeated; the Winter Warden visit does not establish a new monster classification or address.

Ecology templates support ID/species/location/threat, behavior/territory/sustenance, group/intelligence/hostility, abilities/weaknesses and last-status/encounter sources. Unknowns remain null. Defeated creatures do not revive and contained creatures do not die through maintenance. New populations need plausible cause, elapsed time and a recorded world event; no automatic respawning or scaling to Theron's rank.

Four hazard pointers refer to existing records: installed E-R-7 fitting, removed VII/R fitting, removed command plate and isolated contaminated material. Exact states/restrictions remain in [Seven Bells inventory](../entities/mechanics/seven-bells-inventory.md), not copied into another object list. No current hazard location, effect, trigger, weakness, disarm method or safety guarantee is invented. Installed, isolated, removed, dangerous and safely disabled are different facts. A past residual effect is not a fresh trap activation when the party returns.

Mechanical traps, wards, poisonous environments, collapse, flooding, darkness, temperature, curses, unstable portals and hostile magic are reusable categories only. No new trap is retroactively installed in an explored room. Source-backed trap detection/disarm and changed conditions need actual recorded play; no hazard is triggered here. No unrevealed dungeon solution is published in these references.

## Loot, evidence and ownership

Existing owners remain [Shady Salvage](../entities/mechanics/shady-salvage.md), [Launder](../entities/mechanics/launder.md), [Seven Bells inventory](../entities/mechanics/seven-bells-inventory.md), individual items and [party finances](../entities/mechanics/party-finances.md). The registry stores owner links, not copied objects, coin, quantities, titles or current storage. An owner link does not place every object in that inventory at the referenced site. Check each original object's provenance and scope.

Hollow and Seven Bells batches remain distinct unless a source reconciles them. Processing follows recovery but grants no legal title. Protected originals are not loot; installed fittings are not recovered stock; removed/isolated dangerous objects are not certified safe materials. Party inventory, merchant property, prisoner/third-party goods, consumed materials, sold objects and unknown title remain separate. Historical currency and processing charges are already accounted, never new awards or repeated expenses. Latest item owners supersede older stock snapshots where explicit; consumed materials do not reappear on a revisit.

The future loot procedure remains PROPOSED: consider site history/wealth and inhabitants, earlier removals/exploration, damage, ownership, rarity, carrying capacity and law before any supported generation during approved play. Treasure is finite. No chest refill, unlimited rare materials or guaranteed legendary reward from a high threat label. This chunk rolls nothing, seeds no unexplored room and sells/crafts/consumes nothing.

## Proposed future sites and rank conflict

All five candidates are review records, not active dungeon instances. No exact location, current inhabitant, treasure, room history or world count is supplied.

| Proposal | Supplied rank | Identity/approval boundary |
|---|---|---|
| Hollowstone Mine | D | Shared Hollow naming proves no identity with either established Hollow or Whisperstone |
| Ashen Anvil | B | No identity with Old Copperworks or an established forge |
| Drowned Archive | A | Archive theme does not merge it with the Depository or receiving chambers |
| Pale Reliquary | S | “Pale” does not connect it to Pale Devourer |
| Shattered Meridian | SS | **CONFLICT / REQUIRES APPROVAL:** supplied SS label exceeds separately proposed F–S+ scale |

The F/E/D/C/B/A/S/S+ scale and ten physical categories are proposed design, not retroactive ratings or classifications. SS is preserved literally for review, neither converted to S+ nor silently added to the scale. Dungeon threat remains distinct from combat power, guild license, professional certification and contract difficulty. Existing sites get no unsupported rank, and no enemy is inflated to match Theron. Story Mode, fair warning and permanent-death rules remain unchanged.

## Guild, travel and objective integration

The registry links [contract-registry](../entities/mechanics/contract-registry.md) and each site's existing quests. No current site-bound offered contract was supplied, so per-site guild-contract lists remain empty. Future links must resolve the original contract ID/issuer/funder/objective/eligibility/reward/proof/completion owner and a verified site. No historical bounty is copied, paid again or assigned to a convenient dungeon. A contract alone never clears a site or grants artifact title.

All18 road/corridor records remain unchanged. None currently supplies a verified road-to-these-entrances link; site access-route lists therefore remain empty/UNKNOWN, not “no road exists.” A road ending at a nearby mountain or related town is not proof of a dungeon-door connection. Existing entrance/quest sources may establish historical access details after knowledge review; no new path, coordinates, travel duration, magical capability or player movement is inferred. Shared Seven Bells names prove no connecting passage.

Completion is objective-specific: rescue, threat removal, artifact secured, route opened, system stabilized, investigation, contract or safe sealing. A site can be explored without cleared, cleared without every secret found, or fulfill a contract without full exploration. Only actual supported outcomes update owners. No broader quest, custody case or independent assignment is completed here.

## Minimal GM retrieval procedure

1. Resolve site ID and original location/source label; read only relevant section/quest history.
2. Read the section source-state, actual last observation and access uncertainty. On return, preserve it unless a supported later event changes it.
3. Check relevant creature/hazard owners and uncertainty; never invent current occupants, respawns, trap placement or arbitrary danger scaling.
4. Check prior inventory/protected evidence, ownership and removals before any search/salvage decision. A pointer is not an additional physical batch.
5. Check actual objective/contract terms, funding, legal limits, access route and available resources. Unknowns remain unknown; proposed features need approval before operation.
6. Present known environment with source/knowledge boundaries and meaningful choices. Searching, encounters, disarming, recovery, combat and departures require actual approved play.
7. Record only that played/approved action in existing owners, chronicle/checkpoint/handoff as appropriate; do not create a competing world-state file. Leaving/returning does not reset anything automatically.

Follow narration-format.md for attributed dialogue and independently closed bookkeeping disclosures. `gm-reference` does not mean player-known. This public directory contains source routing, ordinary known observations and design proposals, not hidden answers, identities, motives or access solutions. The existing public/private governance inconsistency is unchanged; repository visibility is not modified. Remaining gaps include precise locations/entrances/routes, current section/access conditions, occupants/ecology, hazards and full item provenance. Five designs, categories/scale and the SS conflict require explicit approval. No Day156→181 reconciliation, Chunk7 work or merge authorization.
