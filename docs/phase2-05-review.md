# Phase 2 PR 5 — dungeon and exploration review

PR number and URL: [#28](https://github.com/Taifinkaba/shadows-over-vellorin/pull/28).

Base: `90a0fa08d37b639be792c86bb44ab271a0752629`, latest main including merged PR #24–#27. Branch: `lore/phase2-05-dungeons`. Scope: PR 5 only; no merge or PR 6 implementation.

## Five-dungeon inventory, IDs and ranks

| New indexed mechanics owner | Reused scoped proposal ID | Candidate placement | Difficulty design |
|---|---|---|---|
| `hollowstone-mine` | `dungeon-proposal:hollowstone-mine` | Stoneford quarry hills; exact hillside, land title and approach unsurveyed. | D reference |
| `ashen-anvil` | `dungeon-proposal:ashen-anvil` | Abandoned mountain workings in Ironhollow Holds; no precise ridge, entrance or ownership established. | B reference |
| `drowned-archive` | `dungeon-proposal:drowned-archive` | Candidate ruined civic archive beneath a proposed Rivermere canal district; no surveyed canal, building or navigable entrance. | A reference |
| `pale-reliquary` | `dungeon-proposal:pale-reliquary` | Isolated northern highland sanctuary; not placed in Frostmarch, Frostspire or another known site. | S reference |
| `shattered-meridian` | `dungeon-proposal:shattered-meridian` | Isolated mountain plateau; exact location, approach and relation to other observatories unknown. | SS — unresolved legacy mapping |

Each original concept is promoted exactly once, with its existing proposal ID preserved. The five new indexed profiles are mechanics/design owners, not actual location entities, discoveries or duplicate dungeons. Total indexed entities: 243. No creature, item, quest, NPC, actual contract, inventory or finance entity is created.

Existing authoritative owners reused: dungeon-design-proposals adds approved_design_index; dungeon-ecology-and-hazards adds approved_reference_design; dungeon-exploration adds approved_exploration_design. Original top-level JSON fields remain exactly unchanged. The historical dungeon-registry 18 site/context labels, exploration-sections 14 source-bound areas and all prior dungeon identities/events remain intact.

Hollowstone develops abandoned mine/fungal ecology; Ashen Anvil a damaged forge complex; Drowned Archive a flooded civic-record structure; Pale Reliquary ceremonial architecture and ethical relic custody; Shattered Meridian an astronomical ruin with bounded spatial-hazard possibilities. These are approved fictional purposes/histories, not newly played or authenticated historical revelations, current inhabitants, recovered blueprints/documents or active machinery.

The original proposed F/E/D/C/B/A/S/S+ dungeon scale remains unchanged. D/B/A/S are design references distinct from combat/guild/professional/contract ranks. Shattered Meridian retains raw proposed SS with compatible_rank null and UNRESOLVED LEGACY SS; no new SS rank, silent S+ mapping or global taxonomy extension. Final combat/stat integration belongs to PR 8.

## Structure, exploration and retreat

Twenty-five named design areas and thirty conditional physical connections form five finite graphs, each with two internal retreat designs. Graph validation checks unique/owned areas, internal non-self connections, entry connectivity and actual design-edge continuity for retreat. Area count is bounded, with no random room expansion. The named five-area layouts preserve the earlier approved section concepts.

[Full profile, schematic graph, monster, hazard and exploration guide](phase2-dungeons-and-exploration.md) includes all five Mermaid design diagrams. They are safe public architectural models, not surveyed maps, secret solutions, discovered doors, verified traversal or geographic coordinates. Every edge remains unverified; the entry interface is no known surface entrance or safe air supply. Alternate internal paths can fail under actual damage/conditions, and additional surface exits are not fabricated.

Profiles describe access/resource/rest limits, environmental navigation, ecological hypotheses, finite material categories, legal rights, discovery requirements, prospective guild/faction interests and persistent consequences. Current area conditions, inhabitants, contents and recoverable quantity remain null. No resting site, breathable pocket, functioning lift/forge, active ward, mana source or guaranteed rescue is established.

## Encounter and monster-reference coverage

Twenty-five proposed encounter designs cover eleven types: exploration, environmental hazard, creature encounter, magical defense, mechanical trap, resource management, negotiation, stealth, rescue, moral decision and retreat. Options include observation, avoiding disturbance, documenting without removal, lawful consultation, dialogue if possible, disengagement and withdrawal. Rescue designs do not create trapped NPCs. No success, active target, hostility, roll, outcome or contract is generated.

Five exact player-approved reference proposals remain in the existing ecology owner:

| Reference | HP | MP | DEF | Rank |
|---|---:|---:|---:|---|
| Giant Cave Spider |24|0|12|D|
| Fungal Burrower |36|0|14|D|
| Ash Sentinel |85|40|20|B|
| Waterbound Guardian |110|80|23|A|
| Ancient Reliquary Warden |190|160|30|S|

Compatibility audit: finite integer HP/MP/DEF fields align structurally with existing resource concepts, but existing creature/combat sources do not provide a complete attack/damage/movement/resistance/balance package for these new opponents. All remain PROPOSED with combat_usable false, attack/damage/movement/resistance and instance fields null, and PR 8 final-integration gate. No usable enemy, current mana reserve, creature entity, attack formula, spell, resistance or combat calculation is introduced. Current creature owners, line-of-sight/modifier/concentration/morale rules and all magic/resource owners remain unchanged.

## Hazard and ecology coverage

Twelve descriptive hazards cover cave-ins, flooding, toxic spores, extreme heat, smoke, unstable bridges, collapsing floors, low oxygen, darkness, magical residue, spatial instability and unstable machinery. Each specifies trigger, observable warning, exposure, possible consequences, mitigation, resources, failure and recovery limits. Numerical effects/current placements stay unknown; automatic damage is false. Generic caution/withdrawal options are not hidden disarm recipes, safe solutions or guaranteed mitigation. No HP/MP, status, time or item cost is applied.

Ecology models require finite actual food/nutrients, water, air, prey, habitat, refuge or verified supported energy/mandate. Spiders/burrowers/fungi/bats/scavengers/predators are possibilities, not current populations. Guardians/elementals require bounded support; no infinite furnace, mana or oxygen source. Independent creatures may avoid, defend, retreat or communicate where applicable; they are not compulsory attackers. No respawn, scaling, revival, autonomous activity or current ecological condition is invented.

## Treasure, salvage, law and ownership

Ten potential reward categories cover coins, tools, craft materials, mineral samples, records, salvageable equipment, decorations, rare materials, research fragments and relics requiring review. Per-site category lists are finite possibilities, never actual quantities, seeded caches, named legendary objects, authenticated papers, unclaimed ore or hidden treasure coordinates. No area has current contents or a recovery budget.

Actual recovery would require an established source/specific location, finite positive quantity within verified availability, discovery/recovery evidence, ownership/provenance, legal authority, transport capacity and an approved original inventory/finance update. The empty template and pure completeness/quantity helper award nothing, generate no loot and prove no source truth. Unknown quantity is never unlimited. Processing/appraisal does not grant title or duplicate an object; protected evidence, third-party goods and consumed/sold materials retain original ownership/state.

PR 3 law controls actual jurisdiction, land/mining claims, protected culture, dangerous research, excavation, salvage and permission. Guild certificates, site existence or danger rank grant no automatic claim, permit, warrant or expedition authority. Respectful observation, leaving relics in place and seeking lawful custodians are noncombat options. Actual records would remain once-only in existing salvage/item/evidence/chronicle owners and sole finance ledger 4; none is created here.

## Geography, discovery, guilds and persistence

Candidate regions are unverified. Stoneford hills have no surveyed entrance; Ashen’s Ironhollow association supplies no route; the Rivermere canal district is proposed, not a navigable survey. Northern highlands and isolated plateau are not assigned to Frostmarch/Frostspire/Northern Marches or another observatory. All 20 road files and geographic hierarchy remain unchanged; no distance, coordinates, approach, teleport anchor or travel duration is added.

Lead categories are possible lawful archival inquiries, survey/report requests or professional consultations, not actual clues, statements, NPC replies, sent messages, discoveries, player knowledge or quest progress. Actual location/access and information evidence must be established before exploration.

Prospective interests link valid PR 4 professional/criminal-design owners, including Ironhand, Greenward, Scribes, Stonewatch, River Charter, Seven Lamps and relevant Nightglass/Black Pick/Thornless/Sable pressure designs. No faction expedition, monster contract, occupation, hidden base, research success, source energy or secret clue is established. Existing guild/faction/contract records remain byte-for-byte unchanged.

Persistence requires actual supported changes in original exploration/creature/item/quest/chronicle owners. No state is duplicated into a second live tracker; no reset, treasure refill, structural repair, respawn, mana recharge, free recovery, current relocation or objective completion occurs through design lookup. Existing Hollow/Seven Bells sources, prior searches/protected areas, recovered inventories, guardian freedoms and quest achievements remain unchanged.

## Preservation evidence

The new manifest pins 325 unrelated campaign files and before/after hashes for only three authorized current owners: dungeon-design-proposals, dungeon-ecology-and-hazards and dungeon-exploration. It verifies their exact prior JSON payloads after removing the approved extensions. Earlier preservation updates are restricted to these owner digests, retaining old before/prior-after values; historical evidence is never rewritten.

All state/checkpoints, finance, existing creatures/NPCs/companions, equipment, spells/skills/locks, property, custody/evidence, quests, archives and preexisting chronicles remain byte-for-byte unchanged. PR 1–4 geography, roads, settlements, law, guilds, factions, trade, communications, prices and contracts are unchanged. House Ashvale retains Briarstone Cottage title, 55 gp noncash appraisal and completed 26 gp repair history; lodge 22% eligible commission remains unchanged.

Checkpoint remains Year 848 Suncrest 61 Day 181 19:30, Ashvale Estate; HP 100/100, MP 400/400, S+/Level 5, normal DEF 49/conditional 51 only with Night Sovereign worn (wearing unknown), Nexus 156/180 and wagon 60/60. Controlled 745 gp 9 sp, unpaid expansion 317 gp and uncommitted 428 gp 9 sp are unchanged under ledger 4. Accounts/current companion positions/undocumented events remain unknown. Chronos Eye/Dragon Slayer remain locked; no discount, concentration, healing, mental-magic or resource rule changes.

## Unknowns, conflicts and public safety

SS mapping is explicitly unresolved. Monster attack packages and balance remain PR 8 work; none is combat-ready. Exact approaches, entrances, coordinates, permissions, terrain, water/air/heat, energy sources, current populations, sections, contents, condition, title and actual discoveries remain unknown. No unresolved conflict blocks design review, while those gaps prevent unsupported exploration, combat, recovery or loot claims. Original historical/proposed fields and approved design extensions must be read by their classification, not as interchangeable observations.

Repository visibility was verified public and is unchanged. Added material is safe design/reference only: no hidden dungeon solution, secret cache coordinates, undiscovered legendary item, covert creature identity, confidential encounter outcome, hidden conspiracy link or plot answer. gm-reference provides no privacy or player discovery. Existing public contents are not certified spoiler-safe and no private storage service is claimed.

## Validation and readiness

Clean base, same source tree as merged main: normal/optimized validators and 921 tests pass (199.230s), with no preexisting failures. The 49 new tests pass (11.667s); the legacy 61-test dungeon suite passes (12.316s).

Implementation: all 970 tests pass (222.423s), including 49 new regression tests for five identities, rank/SS limits, unknown entrances/routes, finite graph connectivity and retreat, exact reference-only monster values, complete hazards without automatic effects, no spawned creatures/loot, finite quantity/ownership/recovery requirements, no faction operations/hidden answers and historical/resource preservation. No introduced failures remain.

Normal/optimized validation passes with 243 entities. Economy report, dashboard generation/--check-view freshness verification and quest readiness pass. Controlled 74590 cp, unpaid 31700 cp and uncommitted 42890 cp remain unchanged, and all twenty roads are byte-for-byte unchanged. Separate ending-design blockers remain 18 pending answer approvals and 14 unfilled routes; no final ending-readiness claim. Normal/staged diff checks pass.

Ready for player review after completed checks. No gameplay occurred: no time advance, exploration, creature spawn, hazard activation, damage, resource change, loot, finance posting, recovery, quest progression, custody, relocation or visibility change. Open one PR, do not merge or begin PR 6, then stop for player review.

## Files added (11)

- `changes/chronicles/phase2-05-dungeon-approval.md`
- `docs/phase2-05-review.md`
- `docs/phase2-dungeons-and-exploration.md`
- `entities/mechanics/ashen-anvil.md`
- `entities/mechanics/drowned-archive.md`
- `entities/mechanics/hollowstone-mine.md`
- `entities/mechanics/pale-reliquary.md`
- `entities/mechanics/shattered-meridian.md`
- `scripts/dungeon_designs.py`
- `tests/fixtures/phase2-05-preservation.json`
- `tests/test_phase2_dungeons.py`

## Files modified (20)

- `README.md`
- `changes/CHANGELOG.md`
- `docs/dungeon-and-exploration-directory.md`
- `docs/validation.md`
- `entities/mechanics/dungeon-design-proposals.md`
- `entities/mechanics/dungeon-ecology-and-hazards.md`
- `entities/rules/dungeon-exploration.md`
- `index.json`
- `scripts/dungeons.py`
- `scripts/validate.py`
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
