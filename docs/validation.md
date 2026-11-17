# Validation and structured snapshot facts

Use the pinned `requirements-dev.txt` dependency (PyYAML6.0.3), then run CI checks:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
python -O scripts/validate.py
```

Python3.12 is used in CI. Tests mutate disposable copies only. The validator is read-only, fails with exit1 and explicit messages, supports `--root PATH`, and does not rely on Python assertions.

## Entity schema and routing

`index.json` schema2 indexes every file under `entities/`; IDs and paths unique, path `entities/<type>/<id>.md`. Types: characters, creatures, items, locations, quests, factions, rules, mechanics. Frontmatter: `id`, `type`, `status`, `visibility`, nonempty unique `source_refs`, optional `checkpoint_values`. Metadata must agree with the index. Status: canon, last-verified, gm-secret-locked, active, research, completed, user-locked; visibility: gm-reference/gm-secret. Locked secrets require gm-secret.

Safe YAML supports quoted/unquoted values; duplicate keys, unsafe types and unknown metadata fields rejected. Source refs must be normalized root-relative existing file paths, with no traversal or escaping symlinks. The preserved cumulative handoff under `archive/session-handoffs/` is valid evidence; original legacy archives retain their own index and original basename resolution.

## Historical checkpoint schema2 (preserved Day153)

Day153 is the first explicitly versioned checkpoint. Required keys: `schema_version` (integer2), date (`Year N Day N`), 24-hour time (`HH:MM`), location, theron, money, world, status (`PAUSED`), source (existing root-relative file), context. The prior unversioned Day46 snapshot is preserved unchanged under `archive/checkpoints/`; it is historical, not silently rewritten to schema2.

- `theron`: integer hp/hp_max, mp/mp_max, defense, level, str/dex/con/int/wis/cha and unspent_attributes; nonempty rank. Nonnegative values (positive maxima); HP/MP within maxima.
- `money`: central_gp_sp, emergency_gp_sp, reserve_gp_sp, operating_gp_sp, development_gp_sp, total_gp_sp. Exact integer-copper accounting; no floating values. Five cash accounts sum to total. Former companion personal balances are historical after voluntary consolidation; they must not be re-added.
- `world`: integer vaeltharion_chains_attached and protective_anchors_retained. Distinct counts; old junction testing is historical and is not a release/anchor count.
- `context`: safety text, companions_present IDs, party_roles keyed by IDs, projects text mapping, academy mapping, outstanding_clues list, recent_mp_costs mapping, mp_before_recent_casts integer. IDs must resolve. Recent starting MP minus summed costs must equal current MP; the Day153 starting400 is arithmetic from337+63, not evidence of an invented rest.
- Academy mapping: entity ID, latest_reported_cash_gp_sp, refundable_lease_deposit_gp_sp, balance_date note, included_in_party_total (must be false).34gp cash and15gp deposit are latest reported earlier values with unknown report date; no newly verified later balance implied. Deposit remains separate noncash. No academy amount enters party cash.

## Historical schema2 structured entity agreement

| Owner | Required checkpoint facts |
|---|---|
| theron-ashvale | date, time, location, status, every theron field |
| vaeltharion | both world counts |
| party-finances | every money field |

Owned values must match current checkpoint exactly (currency by integer copper). Other entities may not add undeclared snapshot ownership. Changing canon requires updating snapshot, structured entity values, prose and changelog together. Validator rules do not freeze specific numerical canon permanently.

Regression checks cover metadata, paths, archival coverage, account sums/separation, recent MP spending, new schema, entity agreement and the current core/new spell costs. Unknown companion numerical HP/MP, missing transaction details and chronological gaps stay unknown. Historical custody38gp2sp, merchant goods, evidence and noncash estimates remain excluded.

The validator checks declared facts and references; it does not infer truth from arbitrary prose, prove testimony, determine guilt, expose GM secrets, resolve concentration timing or interpret artwork. Human review preserves those distinctions. Source path existence establishes findability, not independent historical verification.

## Current checkpoint schema3 — Day472 END SESSION

Schema3 retains date/time/location, Theron base stats, world counts, source and context; session status is `ENDED`. Schema2 remains supported for historical snapshots and regression fixtures. The index schema remains2.

- `resources`: nonnegative integer equipped_defense/bracers_defense_bonus, staff_mp/staff_mp_max, wagon_mp/wagon_mp_max; positive maxima; pools cannot exceed maxima. Equipped DEF must equal Theron permanent base plus equipment bonus. Boolean chronos_eye_locked and dragon_slayer_locked must remain true under the supplied player ruling.
- `money`: exact-copper total_gp_sp, blackscale_private_gp_sp, expedition_gp_sp, excluded_lyanna_gp_sp, scene_opening_gp_sp, scene_recovery_gp_sp, scene_cost_gp_sp, plus nonempty allocation_status beginning `unverified`. Known controlled components cannot exceed total. Opening + recovery − cost equals total. Lyanna is excluded, never added. There is no invented residual account or requirement to balance stale allocations.
- `context.recent_mp_costs` is empty and `mp_before_recent_casts` null because individual final-release costs/starting mana are unavailable. This does not authorize free casting or future recharge: final personal MP and resource pools must agree with authoritative entity values. Other context keys retain schema2 shape; academy values explicitly remain earlier reports, not newly verified balances.
- Theron owns schema2 Theron/date/time/location/status fields plus every `resources.*` value. Party-finances owns every schema3 monetary currency field. Vaeltharion retains the two last-verified world counts; Aeloryn's restraint release does not change them.

Day153 mutation tests load the unchanged archived snapshot and saved historical entity values; separate current-checkpoint tests cover schema3 partial allocations, excluded cash, finite pools, locks, defense separation, missing mana history and entity agreement. Unknown chronology and exact spell repricing remain human-review limits, not fabricated data.

## Current checkpoint schema4 — Year848 Suncrest4 Day124

Schema4 preserves schema2/3 validation for archived checkpoints and structured owner fixtures. The current session is `PAUSED`; `date` remains `Year 848 Day 124` with `calendar.season`/`day_of_season` recording Suncrest4, without assuming a year length or inventing dates across the gap.

- Resources and Theron/world structured ownership retain schema3 rules.
- Money has `total_gp_sp`, `provisional_historic_gp_sp`, `office_petty_gp_sp`, plus nonempty `allocation_status`, `provisional_status` and `office_status`. Party-finances owns the three currency values. Total is controlled spendable only; provisional approximately9gp1sp14cp and house6gp4sp are excluded, never summed into total. Unknown transactions/account allocations remain explicit; no invented opening/cost fields to force a reconciliation. Exact copper conversion preserves the supplied unnormalized14cp denomination while the text retains its approximate status.
- `context.recent_mp_recovery` records ability, amount, uninterrupted minutes, usable ambient source and personal-only scope. Assimilation II requires24MP per complete uninterrupted10 minutes; reject partial intervals, missing source or other-pool recovery. Latest starting375 minus Mental Probe13 plus24 equals386, capped at personal maximum400. No inference about earlier unspecified expenditure logs or concentration overlap.
- `custody` records unique character IDs for current detainees/free people, guard, fatalities and party injuries. References must resolve; free people cannot simultaneously be detained. Regression checks pin this supplied snapshot to three detainees, Sella/Orenic free and zero deaths/injuries. Older custody is historical, not a current location assertion.

Validators do not infer guilt, prove same-name identities, certify recovered materials, verify arbitrary status prose, or fill missing historical events. New regression cases exercise mana recovery prerequisites/arithmetic/cap, segregated money, finite pools, custody references and current exact snapshot. Historical schema2/3 regression suites use their preserved checkpoints and structured entity values.

## Current checkpoint schema5 — Year848 Suncrest17 Day137 END SESSION

Schema5 retains schema4 money fields and structured ownership. `status` is ENDED;
calendar records Suncrest17 and checkpoint date/time are Year848 Day137,09:30.
Allocation status now records the approved reconstruction and unresolved legacy split.
`context.recent_mp_costs` is empty and `mp_before_recent_casts` null, with no
`recent_mp_recovery`: final personalMP400 is explicitly supplied, intermediate
expenditures/recoveries are unknown. The historical schema4 recovery rules still apply
to its preserved Day124 fixture; no guessed recovery or free casting is implied.

`custody` records aggregate `reviewed`, `released`, `retained`, and
`medically_transferred` nonnegative integer counts, a boolean `hearing_pending`,
plus `identities_status` and `halden_status` text. Counts must sum; no mapping to
older detainees is invented. Current supplied counts are4/2/1/1, hearing pending.

`entities/mechanics/party-finances.md` routes to **state/finance-ledger.json**, the
separate authoritative detailed financial record (ledger schema1). No duplicate
finance entity or index schema change. The ledger uses integer copper (100cp/gp,
10cp/sp), distinguishes cash ownership/accounts, category revenue and expenses,
net surplus/distribution, excluded property/assets/deposits/estimates and open
historical discrepancies. Its date, source, total and excluded amounts must agree
with the checkpoint; the finance entity's three money values remain exact owners.

Validation enforces category sums, merchant commission separation, eight-period
multiplication, net-only percentages totaling100%, one distribution, baseline
purse/legacy inclusion, account totals, neutral expense-history arithmetic, zero
internal-transfer cash effect, excluded holdings, already-paid land and unspent
estimates. The128gp historical gap stays open without a current adjustment.
No automatic future65gp award; future actual periods require Tomas receipts and
expense records or another explicit player-approved accounting ruling.

Day124 snapshot and structured owner values are preserved under archive/checkpoints/;
its tests restore those fixtures in disposable copies. Schema2/3 fixtures remain
unchanged. Day137 mutation tests exercise double-counting, exclusions, commission,
percentages, repeat expenses/distributions, estimates, locks, mana and custody.

## Day156 ledger schema2

The checkpoint retains compatible schema5 and structured ownership; the carried
Night Sovereign leaves normal equipped DEF49. Conditional worn DEF51 and spell
limits are recorded in its indexed item entity and checkpoint project notes.
The existing wagon pool remains60/60; mundane Vanguard has its own item entity
and no pool. Day137 custody aggregates remain historical, explicitly separate
from the newly reviewed V-9 cases.

Finance ledger schema2 replaces schema1's current-account assumptions while
schema1 remains validated against preserved Day137 fixtures. It records exact
integer-copper final allocations, the five once-only arc events,15400cp cash
restitution separately from5500cp noncash appraisal,31700cp committed/unpaid
expansion and45490cp uncommitted cash. The historical52000cp reconstruction
is referenced once; the12800cp discrepancy is resolved by player ruling with
no invented receipts or current adjustment. The103490cp→115990cp bridge remains
unitemized. Tests reject duplicate postings, fractional/boolean copper,
noncash awards, paid expansion, invented settlement finality and automatic income.

Validation checks declared accounting and references; it does not independently
substantiate the player's scene reconstruction, legal claims, NPC identities,
conditional concentration behavior or unrecorded historical transactions.

## Geography and travel extension — Chunk2

Index schema2 and existing frontmatter fields/types/statuses remain unchanged. The geographic directory (`entities/mechanics/world-geography.md`), route registry (`entities/mechanics/travel-routes.md`) and each indexed `entities/locations/route-*.md` own one fenced JSON block with integer `schema_version: 1`. `entities/rules/travel-procedure.md` owns procedure, not state. No parallel state JSON file.

`world-geography.nodes` lists every physical location ID once, a geographic kind, `CONFIRMED CANON` or `PROPOSED`, and parent edges with classification and source refs. Empty parents means unknown placement. Parent graphs must be acyclic; no self-parent or canonical containment through proposed nodes. Proposed placeholders have existing metadata status `research`; known-name-only records may use `last-verified`. Exact normalized duplicate canonical location titles are rejected; similar-name identity remains human review.

`travel-routes.route_ids` must cover every indexed route ID once. Routes use location entities with `route-` IDs; frontmatter remains the existing schema, with structured road data in the JSON body. Required route keys: schema_version, classification, start, destination, bidirectional, reverse_status, intermediate_settlements, road_name, road_type, distance, durations, accessibility, terrain, road_condition, known_hazards, patrol_jurisdiction, toll_requirements, seasonal_restrictions, last_verified_status, source_refs, integration_points, notes. Null values preserve unknowns; empty durations means no known time. Start/end must be distinct physical locations, never character/item/route/continent endpoints. Canon routes cannot traverse proposed nodes; registry/index duplicates and missing references fail.

Durations record mode, positive integer minimum, optional integer maximum, unit(minutes/hours/days), qualifier and basis. Approximation and open lower bound semantics remain in the qualifier; a day is not automatically24 movement hours. Canon historical reports additionally require an exact source_quote and source_ref. A deliberately narrow evidence parser compares the four current reports against their source wording; unknown historical evidence is rejected with a clear message until the parser is extended, not guessed. Proposed durations use `proposed-estimate`; historical mode/time cannot silently change. No historical distance survey is currently supported; a proposed distance may use a positive integer and m/km/miles. Future verified distances need explicit evidence support before adoption.

Accessibility fields walking/riding/wagon/caravan accept boolean or null; no duration for a forbidden mode. Integration points contain role, target_id, classification, placement and at_location; IDs must resolve, endpoint placements must match a route endpoint, and secret records require a separate GM view. This checks referential consistency, not whether a watch actually patrols a corridor or an inn has vacancies.

The main validator invokes `scripts/travel.py` in both direct CLI and package-import modes, including optimized Python. Historical fixture trees with no travel records remain valid; partial current directories/registries fail. `tests/test_travel.py` exercises malformed graphs, proposal promotion, source contradictions, inaccessible modes, exact mileage fabrication, missing services and read-only behavior. These checks do not certify borders, current safety, implied intermediate locations, testimony or semantic identity from similar names. No legitimate unknown field is filled or rejected merely for being incomplete.

## Settlements/businesses extension — Chunk3

Index schema2/frontmatter types/statuses are unchanged. New mechanics entities `settlement-services`, `service-price-references` and `local-settlement-activity` own routing/schema policy, proposed price references and activity categories respectively. Parent locations own one JSON block under the exact `Settlement and business references — Chunk 3` heading; existing prose is preserved. Business IDs are `parent-id:slug`, unique across profiles, and resolve through their parent index entry. No new business entity type or competing state/finance file.

Profiles record identity/classification, separate nation/territory/region refs, type/population, government/officers/watch/court, route IDs, neighborhoods, nearby refs, institution/service links, local-problem refs, notes and evidence. Null means unknown; site/property profiles never imply a new settlement. Routing must cover all marked profiles exactly. Routes must resolve to real route entities with that parent as an endpoint. Their classification is read from the existing route owner, not copied into a town or supply chain. Normal travel validation continues checking canonical location uniqueness and proposal boundaries.

Business fields: id, name, display_label, parent_location_id, classification, address, categories, owner_id, manager_id, operator_id, staff_ids, staff_notes, services, goods_categories, stock_counts, capacity, schedule, accepted_currency, payment_practices, prices, price_reference_ids, supplier_relationships, existing_contracts, licenses, operational_status, last_verified_date, last_verified_note, source_refs, evidence and automatic_financial_postings. Categories are vocabulary only. Owners/operators/managers are distinct; null owner is valid. Existing estate/lodge premises ownership/management and Brackenford village authority have explicit guards. Future independently approved changes must update those guards with source evidence, not bypass them.

All source refs must resolve inside the repository. Evidence quotes must exist in original source text before the appended profile section; a new claim cannot quote itself as evidence. This establishes provenance/findability, not full semantic proof of every field. Population is checked against existing approximate population text; no unsupported new historical count. No secret entity link is allowed in these public-facing reference blocks; human review still checks prose and knowledge provenance.

Integer-copper prices preserve100cp/gp and10cp/sp; positive or zero price ranges cannot contain floats/booleans or invert bounds. Historical paid forge cost is checked against original72gp wording, not recharged. Current baseline has no supplied merchant quote/approved tariff: proposed archived bands cannot become current/approved prices. Source-band conversion is checked independently. Additional sourced price/stock/supplier contracts in later chunks require extending these deliberate evidence guards; unknown values are accepted now. Capacity is not stock. Automatic financial postings, triggered activity events, automatic progression, invented counted stock, deliveries and unsupplied business licenses/contracts are rejected.

`scripts/settlements.py` runs from both script and import modes, including optimized Python. Historical repositories with no settlement extension remain valid; partial frameworks fail. Tests mutate disposable copies, preserve unknown owners/prices, and exercise routing, scope IDs, original-source quotes, ownership/authority, price kinds/conversion, financial/event boundaries and read-only behavior. The narrow `tests/fixtures/chunk3-preservation.json` contains hashes, not campaign text: it verifies original profile prefixes and unchanged current state/staff sources against merged Chunk2. It is a maintenance regression fixture, not a rule freezing future player-approved canon. Existing broader checkpoint/finance/travel regression tests remain active.

## Justice extension — Chunk4

Existing entity/index metadata schema remains unchanged. New indexed records: `justice-authorities` (mechanics/canon), `justice-proposals` (mechanics/research), `justice-road-links` (mechanics/canon), `justice-and-jurisdiction` (rules/canon). Each has one fenced JSON schema_version1 body. Canon framework metadata never approves proposed content. Existing `prisoner-custody` keeps its original prefix and adds one JSON block under `Justice workflow and source routing — Chunk 4`; no competing state or case file.

Scoped `justice:` authority IDs reference existing functions only. Location, leadership and source references must resolve, exact source quotes must exist, and existing civilian/military/guild/private distinctions are guarded. No new headquarters, precise boundary, operational receiving facility or cross-border agreement is supplied. Brackenford leadership and protected existing officials remain distinct. Unknowns/nulls and empty lists of verified relationships are legitimate, not evidence an institution is absent historically.

`justice-proposals` holds seven roles, twelve building candidates, sixteen official candidates and five approval categories. All remain PROPOSED/REQUIRES APPROVAL with null approval provenance. Review IDs are unique across candidate kinds, not new entity IDs. Valid existing candidate settlements do not establish addresses, capacities or cells. Stonegate/Warded Annex stay unlocated. No staffing, court assignment, kinship, operational status, existing-person alias or newly enacted jurisdiction is accepted. Exact established-name collisions require review; similar spelling alone proves no identity. Later approved canon requires sourced schema/test updates, not silently changing a classification.

Road lookup must cover every existing `route-` entity once. Endpoint contacts must match both road endpoint and authority's sourced local context. Since all current road patrol fields are unknown, responsible corridor authority, region, nearest station, court and remand destination remain null. References do not change route classification or transport. Existing travel and settlement validators remain active.

Workflow stages and evidence/transfer field sets must be complete; proposed court process/taxonomy cannot become enacted law via a metadata edit. Custody source pointers have only ID/scope/source_refs/note; no hidden status or destination snapshot. New case/transfer/evidence lists remain empty and automatic actions false. References to GM-secret entities are excluded from public lookup records. This does not prove arbitrary linked gm-reference prose is player-known; human source/knowledge review is required.

`scripts/justice.py` exposes a read-only prospective transfer validator, exercised with explicitly synthetic contexts. Stable case ID supports unknown person identity. Plans cannot claim departure/arrival/receipt; transit requires actual departure and verified authority/operational destination but no arrival/receipt. Completed transfers additionally need receiving officer, arrival/receipt and both evidence/property inventory source references. Proposed/nonoperational facilities or proposed authorities cannot conduct actual transfers. Source-file existence is necessary, not proof of handover, legal competence, dates or testimony. No new completion fields are forced retrospectively onto incomplete historical text.

The main validator invokes justice validation in CLI/import/optimized modes and accepts older repositories with no justice extension; partial current frameworks fail. Mutation tests check reference/approval errors, phantom transfers/convictions/property changes, road proximity assumptions, secret references and read-only behavior. `tests/fixtures/chunk4-preservation.json` hashes unchanged state, selected public officials/evidence/quest sources, every road and the original custody prefix against merged Chunk3; it adds no case narrative. It is a maintenance regression fixture, not permanent authority to freeze future player-approved outcomes. Full protected-directory byte comparisons supplement the fixture before publication.

## Guild and contract extension — Chunk5

Existing frontmatter/index schema is unchanged. Four new entities: guild-network (mechanics/canon), continental-guild-concord (factions/research), contract-registry (mechanics/canon), guild-membership-and-contracts (rules/canon). Existing Wayfarers and academy owners keep original prefixes and one added JSON block under Guild and contract references — Chunk 5. No duplicate quest, membership, rank or financial ledger.

Guild-network owns identity/classification/compatibility routing, not copied current profiles or balances. It distinguishes three confirmed organization references from six archived designs requiring approval; overlapping functions cannot merge identities. Named Eastrun/Briarfall/Rivermere Wayfarers branches remain archived candidates with no hall, officer, approval or operational claim. Canon branch/site references remain Caelthorne HQ, unlocated established branches and the independent Greyhaven Valley academy. Locations/routes must resolve and route endpoints match each site; no proposed road promotion, invented branch or new guildmaster.

Parent-owned profiles provide headquarters/branches/leadership, membership/services/ranks/licenses/contracts/funding/commission/jurisdiction/relationships/source/date fields with explicit unknowns. The academy preserves Beren/Theron/Vaeltharion roles; the guild's unknown leaders stay unknown. Concord and all eight divisions must remain proposed, nonoperational and unapproved, with no branches/leaders/members/fees/treasury/postings. Compatibility links resolve to crosswalk IDs, not implied memberships. Existing rank owners remain authoritative across five distinct domains. New enrollments/licenses/staff/events stay empty/false.

Contracts use original IDs under the existing Wayfarers owner; contract-registry contains only ID-to-owner pointers and future dungeon-work categories. No current offer, site event or quest completion is generated. Contract fields include issuer/registry, funder identity/name/source/quote/commitment, objective/site/difficulty/eligibility, legal authorization, acceptance/assignment/deadline, reward/fees, evidence/conditions/completion, payment/history, current-availability classification, existing quest/source/date and empty posting lists. Unknowns are valid; historical paid records do not need fabricated original funders. Paid amounts are separate from future advertised rewards and may only be referenced once. Existing four record IDs/statuses/payments and SS-41's narrow withdrawal are guarded; unrelated notices cannot be canceled.

`scripts/guilds.py` exposes read-only prospective contract validation. Guaranteed future reward requires canonical issuer/context, identifiable funding party, existing commitment source/quote and integer-copper committed budget >= reward. Proposed organization or paid history cannot generate a new guarantee. File existence/quote/arithmetic does not independently prove title, enforceability, legal competence or actual budget; human source review remains necessary. Bounty alone cannot set apprehension_authorized without a separate source. No acceptance, completion or payout occurs in code. All finance postings stay empty; source10% policy is preserved without retrospective application or gross/net inversion. New fees, academy income and Concord revenue are forbidden in this maintenance baseline.

Main validation supports direct/import/optimized modes and older repositories without this extension, rejecting partial current frameworks. Tests exercise unique organization/branch/contract IDs, proposal/identity/branch errors, unknown fields, academy independence, funding constraints, duplicate rewards, fee/license boundaries, legal links and no mutation. Preservation hashes pin original faction prefixes and unchanged state/ranks/academy/animal/custody/roads/property/quest sources to merged Chunk4. They protect maintenance scope, not permanent authority to freeze future approved canon. One preexisting negative test now accepts either missing-owner or earlier missing-finance-source rejection, because the new rules explicitly cite the existing finance authority; the invalid repository must still fail.

Public lookup references reject GM-secret entity/source links, but metadata alone cannot establish character knowledge. No concealed answers or motives are copied into new directory material. Human knowledge review remains required before narrating linked gm-reference content.

## Dungeon and exploration extension — Chunk6

Existing entity/frontmatter/index schema stays unchanged. New entities: dungeon-registry, exploration-sections, dungeon-ecology-and-hazards (mechanics/canon), dungeon-design-proposals (mechanics/research), dungeon-exploration (rules/canon). Each owns one fenced JSON schema_version1 body. Framework canon does not approve designs or make ordinary sites dungeons. No old entity or state file is edited.

The registry contains18 unique source-backed site/context IDs, optional existing location/entrance refs, unknown region/category/rank/whole-site state, section/creature/hazard handles, original inventory/evidence/quest/contract owners and source references. Indexed physical locations cannot be duplicated; aliases require future sourced reconciliation and are empty now. The two Hollows and ordinary structure roles have guards. Candidate current road access and site-bound offered contracts remain empty because none is supplied. Proximity and shared names cannot create a route, entrance, alias or reward. Source labels prove findability, not full semantic identity or present access.

Sections use stable scoped IDs with unique source locators, original contents/inventory/objective owners and no editable duplicate status. read_section_state reads the owner's table/inspection and returns a normalized observation without writing it. Searched maps to explored only in that scope, visited stays visited, partial stays partial, protected gives unknown degree plus protected access. Unknown/unfamiliar wording is retained without inventing degree. Supported vocabulary includes unknown, unexplored, partially-explored, visited, explored, cleared, sealed, inaccessible and destroyed; no added clearing or exploration events. An inspection does not certify full exploration. Source updates flow through lookup; approved future source changes must update preservation fixtures deliberately rather than override with a second snapshot.

Ecology/hazard records hold references only. No new creature locations/populations/stats/abilities/encounters or trap placement/solutions/effects/triggers. Installed/removed/isolated status stays with original inventory owners. No implicit restoration, defeat, hostility or reset. A prospective population-event validator accepts an uninstantiated proposal with unknowns; recorded changes require cause, elapsed-time source and actual event source. It validates completeness only and executes no spawn. Human review must establish causality and source truth.

Five proposals remain PROPOSED/REQUIRES APPROVAL and unplaced/uninstantiated, with no inhabitants/treasure/history/census. Raw supplied D/B/A/S/SS labels are preserved. SS must retain a conflict marker because the separately proposed scale stops at S+; it cannot be silently converted or accepted into that scale. Physical category and threat/rank-domain boundaries remain proposed, without retroactive site ratings.

New inventory/objective/encounter/population/loot/combat lists stay empty; auto-respawn/scaling/chest refill/loot/completion flags false. Reference links cannot relocate an existing inventory to another site or assign recovered goods to an unexplored section. Existing batches, legal title, protected originals and consumed stock remain with existing owners, with no quantity copies or financial postings. Contract-registry remains the original contract lookup; no bounty duplication or newly offered site contract.

scripts/dungeons.py runs in direct/import/optimized modes. Historical repositories without this extension remain supported; partial current frameworks fail. Mutation tests cover IDs/refs/status vocabulary, alias/route mistakes, inventory/evidence boundaries, no-reset observations, no events, proposals/rank conflict, secret refs and source immutability. tests/fixtures/chunk6-preservation.json hashes protected existing state/exploration/creature/item/quest/guild/road/property files against merged Chunk5. Full local byte comparison verifies every preexisting entity/state/archive is untouched. These are maintenance checks, not a permanent freeze on later approved canon. The prior guild partial-framework test accepts either its original missing-framework error or the new earlier missing-contract-source error; rejection is still mandatory.

Public records exclude GM-secret entity/source links and copy no hidden solutions or case identities. Metadata, reference existence and state parsing do not independently prove player knowledge, testimony, legal title, true geography or current safety. Human source/discovery review is still required before narration.

## Economy and property framework — Chunk 7

Four indexed helper records contain one schema1 JSON block each. `economy-accounting` owns procedure vocabulary/empty maintenance event slots; business references route all14 parent-owned services; property references route four existing contexts and ten inventory owners; payroll/construction/trade rules route existing prices/roads/guilds/contracts. Current finance remains schema2 in `state/finance-ledger.json`, unchanged. Frontmatter and entity types are unchanged.

`scripts/economy.py` is read-only: `--report` validates the repository then derives a dated/source-qualified report. It distinguishes modeled history from unknown current-period receipts, internal distributions from revenue, and committed cash from paid bills. The report never writes a ledger or cache. On an unsupported ledger schema it fails closed.

`validate_economy` checks coverage, classifications, currency, original owner links, unknown current values, empty new events/valuations/modifiers and no automatic income. Prospective `validate_transactions` / `validate_payroll` check integer copper, amount metadata, unique IDs/events, controlled account ownership, internal-transfer income exclusion, payment evidence and expense coverage. These helpers validate candidate inputs only; they do not authorize or post events. A separately sourced/approved migration is required for future actual ledger records. File/quote existence does not establish event truth. Existing ledger validators still enforce once-only historical events, exclusions, account sums, unpaid commitments and checkpoint agreement.

Chunk7 preservation hashes freeze this maintenance baseline in regression tests, not in runtime campaign validation. All preexisting entities/state/archive are byte-preserved, including history, evidence, prisoners, equipment and property. Future legitimate campaign changes require deliberate fixture review. Human review remains necessary for legal title, staff work safety, receipts, price increases, trade evidence and player knowledge. See [property/economy directory](property-and-economy-directory.md). Run normal validator, unittest discovery, optimized validator and `git diff --check`.

## NPC autonomy, factions and events — Chunk 8

Five indexed helpers use one schema1 JSON block each: independent-assignments routes30 actor identities,20 scoped responsibility/request/history pointers and two construct ability-context handles; faction-activity routes six owners; world-event-references routes six original chronicle documents (not six new occurrences); world-development-proposals remains metadata research/PROPOSED with empty clock/relationship arrays; npc-autonomy-and-time owns manual procedure links. Existing frontmatter/status/index/checkpoint schemas are unchanged. Proposed workflow labels are body vocabulary, not entity statuses.

`scripts/autonomy.py` validates unique IDs, original owner/type/source alignment, source quote location, freshness links, claim/knowledge classifications, source contracts and zero new events, clocks, communications, abilities, membership, legal powers, relationships or resource postings. Whole-framework absence is supported for older snapshots; a partial extension fails. No write API, scheduler, automatic simulation or player-visible source-dump command exists.

Prospective candidate validators check event IDs, duplicate history, references, explicit time-advance/played-scene evidence, trigger/action/outcome and discovery evidence; missing exact date/time is null, not invented. Proposed events cannot assert outcomes/resource effects. Clock validation allows unstarted neutral proposals only, never archived progress promotion, active countdowns or secret storage. Evidence-file/quote existence is not independent historical truth, consent, legal power, knowledge or approval: human source review is required. A gm-reference file may still contain restricted passages; public-directory schemas intentionally exclude editable leadership/operations text, and no raw source renderer is supplied.

Regression tests mutate disposable copies only. Chunk8 preservation hashes cover every preexisting entity/state/archive/historical chronicle, preserving positions, resources, finances, abilities, custody, relationships, bonds, quests and history. The single entity-count assertion in the earlier economy suite now uses index length so later authorized frameworks do not require a frozen count. Future real campaign changes require deliberate fixture review, not bypassing authority. Run normal validator, unittest discovery, optimized validator and `git diff --check`; see [NPC retrieval](npc-autonomy-and-world-events.md) and [faction directory](faction-activity-directory.md).

## Main quest, evidence and finite proposal — Chunk9

Six indexed helper records use one schema1 JSON block each. main-quest-map routes original public-reference quest owners without copied statuses; quest-history-and-identities routes13 protected objective/observation scopes and17 distinct people; quest-evidence-and-mysteries routes17 clue scopes and18 unanswered questions; quest-resolution-proposals and quest-answer-blueprint remain metadata research/PROPOSED; quest-continuation-and-completion is a manual procedure. Frontmatter/index/checkpoint schemas remain unchanged. Outcome/workflow labels do not extend entity statuses.

`scripts/quest_framework.py` validates references/source locators/freshness, identity separation, no duplicate clue scope/item, historical-versus-proposed classifications, no new outcomes/rewards/transfers/disclosures, unfilled secret-answer values and explicit private-storage/approval gaps. A finite DAG check enforces reachable entry-to-ending chapter coverage, no mandatory cycles/repeated objectives and no dependencies on nonexistent or optional nodes. Five target counts sum14; seven essential objectives remain proposed. Fourteen clue-route slots remain unfilled design obligations, not functioning geography or actual clues.

Main validation prints a nonfatal readiness note:18 pending answer approvals /14 unfilled routes. `python scripts/quest_framework.py --readiness` validates then returns only neutral pending IDs, classifications and counts, never source text or answer values. These blockers prevent claiming the design is activated; they do not fail baseline solely for unapproved prospective lore. No simulation/write/post/complete API exists. Secret values cannot be stored publicly even after a future approval flag; safe private storage/workflow must be designed separately.

Regression negatives cover routing/identity/evidence and source knowledge, preservation of completed achievements, blank answer metadata, optional-vs-core separation, graph reachability/cycles, automatic outcomes/rewards/world events and source/state preservation. Hashes cover all preexisting campaign entities/state/archive/historical chronicles. Runtime checks establish declared schema/reference/arithmetic/graph properties, not testimony truth, legal guilt, actual consent, narrative adequacy or player discovery. A file/quote's existence and gm-reference metadata never authorize source disclosure; human claim-level review remains necessary. See [main quest directory](main-quest-directory.md).

## GM workflow and dashboard continuity — Chunk10

One indexed mechanics/canon `gm-workflow` record routes nine existing integration directories, four new workflow documents, original system authorities and targeted retrieval selectors. It has no checkpoint values or evolving balances. New frontend sources include docs; older test repositories now copy docs/governance as well as entities/state/archive/changes so document links are genuinely validated. One dungeon partial-extension negative test accepts the earlier GM-router missing-source diagnostic; rejection remains mandatory. Partial workflow installation fails; historical repositories without this entire extension remain supported.

`scripts/gm_dashboard.py` integrates read-only continuity validation: unique/known owner/source references, exact workflow policy, no cached values or automatic event/post/disclosure slots, required END SESSION fields and flags, empty template values, current-authority next-chat retrieval, local workflow link containment/existence and no competing state/dashboard JSON files. Existing validators still cover IDs/index paths, provenance, snapshot/entity/defense/resource agreement, finance/reserves/posting uniqueness, travel/jurisdiction, contracts/loot/evidence, autonomy/clocks and quest proposal/identity/history constraints. No new numerical gameplay authority is introduced.

The CLI validates the repository then prints JSON or initially closed Markdown disclosures. It reads only reviewed checkpoint/ledger selectors, neutral index/routing fields, bounded item/review phrases and normalized section enums into output. It never renders arbitrary context, handoff/verification narrative, hidden answers/intentions, secret entities or private player-knowledge distinctions. Every display leaf has source/as-of/qualification; unknown current presence, outcomes, conditions and mixed-discovery detail require targeted owner review. Metadata active does not negate completed subobjectives. Role/manager does not imply presence, title or income.

Projection source fingerprints plus `--check-view PATH` reject stale/edited or unsupported views, with strict JSON types and duplicate-key rejection. Regeneration reads actual changed source fields; saved views are never authorities. CLI supports `--root PATH`, `--format json|markdown` and only stdout output; no cache, timer, session/event writer, second checkpoint or ledger. Full validation may scan declared records for integrity, while gameplay context retrieval remains three to six relevant owners rather than full ingestion.

Negative tests cover documents/template completeness, source/index/visibility/ownership errors, cached state, automatic actions, outdated views, float/bool substitutions, raw mixed-narrative/secret filtering and stale-schema failure. Existing historical checkpoint fixtures and all preexisting campaign entity/state/archive/chronicle bytes are preservation-tested. Secret filtering is deliberately limited: this is a reviewed-field projection, not proof every gm-reference passage or the public repository is safe to disclose. Human source/claim/discovery review and genuinely private answer storage remain necessary. See [GM manual](game-master-operating-manual.md), [world status](world-status.md), [END SESSION template](end-session-codex-template.md) and [next-chat template](next-session-chat-template.md).
