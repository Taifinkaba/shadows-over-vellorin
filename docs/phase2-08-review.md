# Phase 2 PR8 — magic, combat and final world integration review

PR number and URL: [#31](https://github.com/Taifinkaba/shadows-over-vellorin/pull/31).

Base: `3489528cacd30c73d9477dbc62acf5be002bf216`, latest main including merged PRs #24–#30. Branch: `lore/phase2-08-magic-combat-integration`. PR8 only; no merge, Phase3 or gameplay.

## Owners, scope and eight schools

New indexed ID: magic-and-combat-integration, a mechanics/procedure owner. Index246→247; every prior entry is unchanged as structured data. It routes original spell, ability, skill, item, creature, dungeon, travel, law, guild, economy, autonomy and quest authorities. It does not own current resources or grant spells. The only revised preexisting entity is dungeon-ecology-and-hazards, which gains descriptive profiles keyed to its five original monster-reference IDs. Every original JSON field remains intact.

| School | Existing associations / boundaries |
|---|---|
| Elemental | Frost Lance, Frost Veil, Glacial Step, Rime Snare; established cryomancy only. Fire/water/wind/earth are reference families, with unsupported spell modes ungranted. No unlimited matter, energy, air or permanent terrain. |
| Restoration | Minor Restoration and the three maternal healing spells. Finite living-target healing/stabilization/condition treatment, not universal cure, mana restoration or resurrection. |
| Runecraft | Rune Barrier, Greater Rune Barrier, Runic Edge, Ward Sense classified by recorded rune/ward reference; detailed unknown detection/effect scope is not expanded. Finite materials, knowledge, preparation/activation and power; no completed unfinished system. |
| Mental | Mental Probe, Dreamfall Mastered, Mirror Mind, Mental Link; consent/resistance, actual memory/target limits and evidence apply. No perfect knowledge, universal mind defense or irresistible effect. |
| Spatial | Spatial Step, Extended Spatial Transfer; verify original mode, prepared-anchor requirements where applicable, destination, access/containment and actual limits. No new teleport destination, universal ward bypass or unlimited distance/load. |
| Temporal | No active player spell is supplied. Chronos Eye stays locked; theory/progress, independent beings and proposed Meridian anomalies confer no foresight, time travel or reversal. |
| Spirit | Existing AssimilationII and voluntary spirit context; no new spell or compulsory spirit activation. Conditions/cap are personal-only; constructs/items/companions generate no free mana. |
| Shadow | Umbral Bolt, Umbral Murmur, Shadow Mantle, Phantom Procession; recorded scope, light/range/duration/concentration apply. No guaranteed invisibility, fear, silence or mind control. |

Each school supplies principles, applications, limitations/resource requirements, training, casting/failure conditions, defensive interactions, ethical/legal limits and unresolved knowledge. Classification adds no effect or ability to anyone. Associated names route back to theron-spells; existing mastery/specializations remain in theron-skills.

## Spell-cost compatibility, efficiency and recovery

The actual current spell owner was compared against the supplied continuity references. Existing historical/revision text is preserved byte for byte, with no silent repricing:

| Supplied reference | Listed MP in current owner | Result |
|---|---:|---|
| Frost Lance |6|Preserved|
| Umbral Bolt |7|Preserved|
| Rune Barrier |9|Preserved|
| Minor Restoration |11|Preserved|
| Spatial Step |9|Preserved|
| Runic Edge |6|Preserved|
| Ward Sense |5|Preserved|
| Mental Probe |13|Preserved; Day124 also confirms actual13MP use|
| Extended Spatial Transfer |21|Preserved; full original anchor/range/load details remain incomplete|
| Greater Rune Barrier |28|Preserved|
| Dreamfall / existing Dreamfall Mastered |21|Same existing identity; no duplicate spell|
| Shadow Mantle |16|Preserved; Day124 confirms actual use|
| Phantom Procession |18|Preserved|
| Deep Mend |UNKNOWN|Supplied17MP reference is absent from current spell owner; no grant/adoption|
| Greater Healing |UNKNOWN|Supplied21MP reference is absent from current spell owner; no grant/adoption|
| Umbral Murmur |9|Preserved; Day124 confirms actual use|

Additional original Day156 maternal costs remain Deep Restoration36MP, Regenerative Weave32MP and Master Restoration Weave48MP. Existing limitations/full-cost exceptions and no resurrection remain authoritative. Stabilization, physical HP recovery, condition treatment and resurrection are not interchangeable.

Governing revisions: the earlier ledger/Day153 tables retain established ordinary costs under the older30% discount and rounded-up procedure. The Year847Day472 authoritative update establishes40% ordinary efficiency, also recorded by the staff/ability owners, but explicitly leaves updated per-spell prices unverified without original bases/approved repricing. Day124 verifies several continued listed prices and Day156 confirms the maternal costs. No reverse-engineering, stacking, second discount, new rounding formula or cost overwrite occurs. Missing bases, eligibility and updated prices need source recovery or a player ruling before unsupported repricing.

Dreamfall remains21MP,60ft range,20ft radius, caster-selectable1–30minutes, concentration, recordedDC18 mental save and waking on damage/shaking/end concentration under its existing rules. No permanent, unlimited or irresistible version is created. Existing dual-mind/dual-casting mastery adds no new concentration slot, save or stacking permission.

Spirit Mana AssimilationII remains24 personal MP per complete uninterrupted10minutes with usable ambient mana/concentration, capped at Theron's sourced maximum400. The historical378→400 example is22 actual/2 excess, not a new event; staff/wagon/other beings are excluded. Pure preview arithmetic checks finite integers, affordability, conditions, interval completeness and caps; it posts nothing and independently verifies no funding, time or capability. No rest/reset/recharge rate is invented.

## Combat and environment integration

Sixteen procedures cover initiative/order, movement, attacks, defense, damage, healing, spellcasting, concentration, statuses, hazards, retreat, nonlethal options, defeat/death, rest/recovery, expenditure and persistent consequences. Existing stakes/cost/DC declaration and d20+relevant modifier versus declaredDC resolution are reused where applicable. They do not invent a universal initiative, action economy, attack-vs-DEF formula, speed, damage, resistance, critical-hit, HP-zero, concentration-save or rest system. Missing rules remain unresolved.

Track actual range, line of sight, terrain, equipment/condition, target/consent/resistance, duration, concentration, consumables, finite pools, morale and collateral effects. Preserve Theron's preference for restraint, disarmament, intimidation, negotiation, incapacitation and capture while allowing resistance, surrender, flight, dialogue and retreat. No automatic success or nonlethal conversion. Actual injury/defeat/permanent death remains possible with established rules, warning and agency; no resurrection exception is introduced.

Twelve environment references cover fire/combustibles, ice/water, electricity only where a source supports it (no current electrical spell verified), darkness/visibility, sound/stealth, water/breathing, heat/endurance, poison/biology, spatial barriers, mental defenses, magical wards and structures. They require actual exposure/conditions, source-backed effects, resources and resolution, without new immunity, numerical modifiers, automatic damage, free air, unlimited ward energy or guaranteed collapse/escape.

## Five monster-reference status reports

No monster identity, original statistic or PR5 numerical-null field changes. New descriptive rows point to the original approved_reference_design.monster_references array rather than creating another numerical bestiary.

| Existing reference ID | HP /MP /DEF /rank | Descriptive completion | Combat readiness |
|---|---|---|---|
| monster-reference:giant-cave-spider |24 /0 /12 /D|Bounded arthropod/nest/prey design, conditional crawl/contact bite/grip, avoidance and retreat; no venom/web power granted.|NOT FULLY READY|
| monster-reference:fungal-burrower |36 /0 /14 /D|Finite moist-ground detritivore, suitable-substrate movement and conditional contact/avoidance/refuge; no stone teleport or spore attack.|NOT FULLY READY|
| monster-reference:ash-sentinel |85 /40 /20 /B|Forge-custody construct, supported physical movement/interposition, verified mandate/energy and stand-down boundaries; no fire spell or heat immunity.|NOT FULLY READY|
| monster-reference:waterbound-guardian |110 /80 /23 /A|Archive-custody guardian, conditional physically supported movement/blocking and finite mandate/energy; no granted water jet, phasing, drowning spell or breathing immunity.|NOT FULLY READY|
| monster-reference:ancient-reliquary-warden |190 /160 /30 /S|Ceremonial custody, conditional movement/contact/restraint, independent mandate/dialogue/withdrawal; no legendary action, new spell or automatic repair.|NOT FULLY READY|

Every profile covers physical characteristics, qualitative movement, attacks/limits, defense, environment, resource-cost unknowns, behavior, retreat, noncombat options, ecological routing, defeat consequences and loot limits. Anatomy, actual capabilities, current instances and operational support remain unverified. Hunting/feeding/rest/nest protection apply plausibly to living designs; constructs require finite maintained support and a mandate rather than compulsory predator behavior. Cooperation/negotiation requires actual capability and willingness.

Original attack_bonus, damage_formula, movement, resistances and current_instance_count stay null; combat_usable stays false. No numerical attack/damage/movement/resistance/spell-cost rule has an approved basis to fill those gaps. MP is finite capacity reference, not an automatically usable spell list or refill. Defeat grants no automatic salvage, mana absorption, reset, respawn or loot; PR5 title/recovery/transport and PR6 inventory/actual sale accounting apply.

## Dungeon and rank compatibility

Hollowstone Mine, Ashen Anvil, Drowned Archive, Pale Reliquary and Shattered Meridian are unchanged. Their25 design areas,30 conditional physical connections,25 proposed encounters and12 hazards remain finite and prospective. No discovery, entrance, access, route, actual inhabitant, encounter, damage or salvage is created.

Existing rank domains distinguish dungeon-threat design, combat power, adventurer/guild licensing, professional certification and contract difficulty. That separation does not validateSS as an adventurer rank. Meridian retains raw proposedSS, compatible_rank null and UNRESOLVED LEGACY SS; the original proposal conflict remains explicit. No global rank, silentS+ mapping or change to Theron'sS+ rank occurs. PR8 completes descriptive integration while numerical/rank rulings remain open; the old PR8 integration-phase tag is preserved as provenance, not a claim that all mechanics are solved.

## Equipment, progression and other systems

All equipment owners remain byte-identical. Sovereign Nexus retains independent156/180, established40% ordinary efficiency, voluntary Caelrix status and original construction/unfinished-system limits. Separate expedition wagon retains60/60, existing capacity/systems and no free recharge; mundane Vanguard remains distinct. Dawnbreaker's Promise remains Lyanna's, with original source-owned tested/subsystem limits and no newly certified automatic long-range rescue. Source-restricted subsystem details are not republished. Night Sovereign remains completed/paid with its existing conditional effects; normal49→51 only when worn, current wearing UNKNOWN. No new item, power, material, pool, construction completion or cost is added.

Theron staysS+,Level5 with existing attributes, skills/masteries/training and locked Chronos Eye/Dragon Slayer. Caelrix, Alpha, Shade and every other companion retain original identity, independence, resources and choices. Raze/Aegis do not supply free casting or mana.

Seven phase links explicitly retain geography/access/preparation, willing settlement providers and actual communications/transactions, jurisdiction/due process, voluntary guild/organizational limits, prospective dungeon encounters, finite PR6 property/economics and PR7 time/knowledge/capability/intent/outcome evidence. Magic grants no routes, assets, licenses, appointments, secret knowledge, NPC abilities or automatic activity.

## Cross-system audit and unresolved issues

`python scripts/magic_combat.py --audit` runs full validation and a read-only18-topic audit with derived counts and current preservation checks. No posting, casting, simulation or write API exists. Review results:

| Audit area | Result / practical limit |
|---|---|
| Entity identities and references |247 unique indexed owners; one new procedure ID; five existing monster IDs reused; all prior index entries preserved. Public authority and phase links resolve.|
| Spell costs |14 supplied owner-backed costs plus three maternal costs preserved; two supplied names remain unverified and ungranted.40% repricing/rounding remains unresolved.|
| HP/MP/DEF and finite resources |Checkpoint/full validators and byte preservation pass. Normal49/conditional51 stay qualified; no personal/item/ally pooling.|
| Rank compatibility |F–S+ adventurer taxonomy unchanged;SS remains an unresolved dungeon design label.|
| Travel and magical access |Original routes/geography unchanged; no spatial bypass, destinations, duration or instant delivery. Missing anchor details remain open.|
| Magical resources/equipment |No new power, pool, recharge or completion; original item owners preserved.|
| Property/finance |Original title, liabilities, ledger4, allocations/restrictions, costs/commissions and history preserved; no competing authority.|
| Appointments/world events |PR3/PR7 guards remain active; no actual office, schedule, independent cast or event created.|
| Quests/timeline |No progress, time advance, fabricated bridge, recovery or encounter. Existing ending blockers remain.|
| Companion identities |Original people/creatures/bonds unchanged; Alpha and Shade remain separate.|
| Monster stats/populations |Five exact templates preserved, all numerical gaps and not-ready status retained; no spawn/respawn/loot.|
| Dungeon discoveries |Five designs/25 areas/30 connections/25 encounters/12 hazards preserved; no new entrance or actual exploration.|
| Public safety |New references require public metadata and carry safe procedure only; no secret payload. Existing mixed-knowledge sources are not certified spoiler-clean.|
| Canon preservation |One authorized existing-owner revision, original JSON comparison and338 unchanged campaign-file hashes verified against merged main.|

Remaining ruling/source needs: original base prices and discount/full-cost eligibility; Deep Mend/Greater Healing governing owner evidence; universal initiative/action/movement/damage/status/HP-zero/rest rules if actual use requires them; monster numerical attack/damage/movement/resistance/cost packages and any demonstrated noncombat abilities; full spatial preparation/anchor details;SS exceptional classification if desired. Equipment unverified functions, legal authority, current routes/conditions, stock, personal resources and knowledge still require original evidence. No choice is fabricated to make integration appear operationally complete.

## Preservation and privacy

The preservation manifest records the base SHA, before/after digest for dungeon-ecology-and-hazards, its complete original JSON payload and338 untouched campaign files. Earlier fixture changes update only that authorized current-owner hash and retain previous before/after evidence. The PR5 legacy comparison explicitly removes the new PR8 extension before asserting its original fields; no historical fixture is discarded. The older autonomy entity-total assertion now derives the index count so adding a legitimate unique procedure owner does not falsify its identity check.

Before/after checkpoint: Year848 Suncrest61 Day18119:30 Ashvale Estate; HP100/100 MP400/400, S+/Level5, normal equippedDEF49 /conditional51 if worn, current configuration UNKNOWN; Nexus156/180, wagon60/60. Controlled74590cp, unpaid31700cp, uncommitted42890cp; ledger4 accounts remain UNRECONCILED / UNKNOWN. No time, location, title, cottage repairs, inventory, equipment, resource, relationship, custody, companion, appointment, finance, quest or historical-event change.

Repository is public and visibility is unchanged. New content is safe reference classification/descriptive design; no secret identities, motives, source-restricted item details, private outcomes, hidden solutions or future answers are added. gm-reference is not player discovery or access control. Existing mixed-knowledge material remains a separate privacy limitation and is not reproduced or certified safe here.

## Tests and validation

Baseline on merged main:184 tests passed in131.330s; normal and optimized validators passed with246 entities. Ten new consolidated tests passed in3.613s, covering school/cost authority, every preserved cost, Dreamfall, efficiency, finite personal recovery, defense/locks/equipment, monsters, dungeon/rank/no-loot, public/cross-system references and read-only preservation. Final ordinary discovery is194, inside180–220; the PR7 reduction remains in place with no hidden/disabled tests or restored old suite.

Implementation: normal and optimized validators passed with247 entities;194 tests passed in132.170s. Economy report, dashboard generation/freshness, quest readiness, existing finance consistency, historical preservation, relevant magic/combat validators,18-topic cross-system audit,194-case inventory/range check and diff checks passed. The audit verified338 unchanged campaign-file hashes without mismatches; no introduced failure remains.

Economy report, dashboard generation/freshness, quest readiness, finance/history preservation, combat/magic guards, test-count audit and Phase2 reference audit results are recorded after execution. Story-ending readiness remains incomplete:18 pending answer approvals and14 unfilled clue routes. Design completion does not mean numerical combat readiness, gameplay activation or story completion.

No gameplay occurred. No combat/casting/recovery, monster spawn, loot, experience/mastery, unlock, item completion, finance posting, NPC move, quest progress, visibility action, merge or Phase3. Stop after this single PR8 for player review.

## Added and modified files

- `README.md`
- `changes/CHANGELOG.md`
- `changes/chronicles/phase2-08-magic-combat-approval.md`
- `docs/phase2-08-review.md`
- `docs/phase2-final-integration-summary.md`
- `entities/mechanics/dungeon-ecology-and-hazards.md`
- `entities/mechanics/magic-and-combat-integration.md`
- `index.json`
- `scripts/dungeons.py`
- `scripts/magic_combat.py`
- `scripts/validate.py`
- `tests/case_support.py`
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
- `tests/fixtures/phase2-07-preservation.json`
- `tests/fixtures/phase2-08-preservation.json`
- `tests/test_phase2_autonomy.py`
- `tests/test_phase2_dungeons.py`
- `tests/test_phase2_magic_combat.py`
