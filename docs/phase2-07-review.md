# Phase 2 PR7 — NPC autonomy and test reduction review

PR number and URL: PR_LINK_PENDING.

Base: `a507e9831bbbf5893ae5a294d5aeab83a513e6d5`, latest main including merged PRs #24–#29. Branch: `lore/phase2-07-npc-autonomy`. Scope: PR7 only; no merge, PR8 work or gameplay.

## Eight-character inventory and identity reuse

| Character owner ID | Age | Design association | Design focus and limits |
|---|---:|---|---|
| elowen-marcrest |47|Valedorn|Court/petition responsibilities, legitimacy, public services, diplomacy and local autonomy; no current royal appointment or actual authority certified.|
| cassian-thornmere |39|Valedorn|Household/property interests, lawful bargaining, economic sustainability and political respect; no estate, current conspiracy, secret allegiance or actual mandate created.|
| aveline-hartwell |54|Valedorn|Independent evidence review, humane process, recusal and legal ethics; existing proposal identity reused, Chief Justice appointment remains unapproved.|
| durnek-stonevein |132|Ironhollow Holds|Clan negotiation, craft integrity, safe extraction and durable engineering; no mine, crew, clan-speaker appointment or new affiliation.|
| liora-thistlebloom |86|Elyndor|Woodland/ecological stewardship, careful botanical study and voluntary neighboring-community cooperation; no species, actual job, residence, healing qualification or powers assigned.|
| selene-harrow |34|Rivermere|River commerce, cargo custody, navigation standards, crew safety and professional ambition; no active vessel, crew, patrol or command assigned.|
| orrin-valecrest |28|Frostmarch|Seasonal preparation, frontier constraints, prospective clan/community obligations and independent choices; no clan rank, current residence, patrol or survival qualification.|
| mira-hearthwick |42|Brackenford|Fair local commerce, community consultation, transparent costs and personal responsibilities; no business ownership, civic office, existing official replacement or actual residence established.|

Five original character IDs are reused; three new IDs are Liora, Orrin and Mira Hearthwick. Targeted identity/name searches across index, entity records and historical modules found no existing matches for those three full names. Mira Hearthwick is separate from Mira Thorne and the lodge helper; Orrin is no alias for Orenic, Orven Pell or another similarly named person. The index changes only by appending three entries:243→246 entities, with every original entry preserved as structured data.

Each owner contains one bounded public autonomy design with identity/age/region, qualified role, traits, values, public motivations, preferences/concerns/ambitions, long/short goals, prospective relationships, obligations, decision priorities, cooperation/refusal conditions, possible consequences, knowledge/routine limits and historical source routing. Known resources are not invented; funds, possessions, inventory, staffing, availability, condition and location remain UNKNOWN. Current jobs/offices/locations are null and actual appointment/action/schedule/relationship-change/secret arrays remain empty. The original PR3 character_design payloads are unchanged.

## Autonomy, time and event framework

The existing npc-autonomy-and-time owner gains approved_autonomy_design. It references original assignment, faction, chronology, communications, travel, law, guild, economy and sole finance-ledger authorities. No duplicate NPC roster, editable timeline, event log, scheduler, clock engine or financial ledger is introduced.

People retain independent motivations, responsibility, judgment and refusal. A goal confers no completed act; loyalty does not compel obedience. The five stages—proposed schedule, planned action, attempted action, completed action and verified outcome—are separate evidence claims. Eleven activity categories cover work, travel, training, rest, shopping, social life, business management, meetings, investigation, family care and personal interests. Plans must reconcile actual time, distance/mode/route, weather evidence, physical limits, money/materials, consent and existing obligations. Maintenance simulates no interval; independent action while Theron is occupied still requires an authorized elapsed interval and supported resolution.

Fourteen potential event categories cover politics, merchant negotiation, trade/professional disputes, harvest/weather, guild elections, construction, celebrations, investigations, frontier conflict, personal milestones, disasters and community projects. Categories are not active events. The empty causal template requires trigger, actor/environment, participants, actor knowledge, time/place, finite resources, relationships/law, action, immediate outcome, resource/knowledge changes, longer consequences, sources, original-owner updates, time-advance and discovery evidence. Completeness guards authenticate no document, prove no truth and guarantee no success. Existing historical chronicle contracts retain their source-qualified unknown dates; unknown chronology cannot justify a time-dependent completion. Link a single actual event ID across its original owners/chronicle/checkpoint/resource authorities when play genuinely occurs.

The original eleven legacy event-candidate categories and proposed clocks remain intact; the expanded fourteen-category design is a procedural reference, not a rewrite of recorded historical events or automatic activation of old clock proposals. No current event, outcome, timer, date, deadline or relationship score is populated.

## Knowledge, relationships and pacing

PR2 communication governs information travel: sender/source, channel, route/cost, dispatch, receipt, discovery and acceptance remain separate. Private plans, conversations, identities, finance details, unreported crimes, unsent messages and distant events are not automatically known. Rumor remains UNVERIFIED RUMOR; a receipt/source locator alone establishes no authenticity or universal shared knowledge.

Eleven relationship domains distinguish trust, friendship, rivalry, professional respect, family, political alliance, business partnership, disagreement, reputation, betrayal and reconciliation. Actual change needs an interaction or supported independent event, prior evidence, identified parties, dated/source-qualified review and original-owner/discovery updates. No automatic romance, friendship, gratitude, betrayal, numerical score or bond progression occurs.

Pacing considers local relevance, severity, information availability, obligations, elapsed time, proximity and narrative importance without causing events for dramatic convenience. Not every action needs narration; important developments reach Theron only through credible observation, witnesses, received messages or investigation. NPC/private outcomes do not become player knowledge automatically.

## Companion, faction, government and economic integration

Alpha remains the larger independent unbound Frostfang alpha wolf; Shade remains the separate smaller gray bonded wolf with the existing3/5 progression superseding older5/5. Their files and all other companions/creatures, bonds, abilities, equipment, loyalties, locations and resources remain unchanged. No recall, training, movement, summoning or new power is inferred. Existing independent responsibilities and refusal rights persist.

PR4 faction interests cover recruitment, trade, influence, training, territory, diplomacy, competition, reform and economic survival. Actual activity requires verified members/leadership, resources, location, opportunity and evidence. Proposed criminal groups remain unactivated, without invented leaders or operations. Voluntary Concord/guild membership and existing independent organizations are preserved.

PR2/PR3 settlement/government procedures support lawful civic decisions, disputes, public works, negotiations, appointments, investigations and community responses only through supported events. Design titles confer no office. Brackenford's officials, businesses and property are unchanged; no facilities, taxes, borders or public decisions are enacted.

PR6 five-domain economics and sole schema4 ledger constrain ownership, existing funds, finite stock, labor, time, transport, agreements and payment evidence. Initiative generates no free revenue, wages, taxes, assets or construction. Existing routes/geographic uncertainty and communication limits still apply; no travel duration or delivery is invented.

## Test audit and reduction

[Per-original-test audit](phase2-07-test-audit.csv) inventories all1000 original discovered cases by file, class, method, protected system, conservative risk, redundancy-review group, file-level fixture dependencies, measured execution time, disposition and replacement. Redundancy-review labels are grouping hints, not proof that different guards are equivalent. [Machine-readable statistics](phase2-07-test-reduction.json) and [original-to-replacement method/table mapping](phase2-07-test-mapping.json) make the consolidation reviewable. All historical fixtures remain available.

| Measure | Baseline | Implementation |
|---|---:|---:|
| Ordinary discovered cases |1000|184|
| Discovered cases reduced |—|816 /81.6%|
| Full-suite runtime |219.984s|136.378s|
| Measured runtime reduction |—|83.606s /about38.0%|
| Full-suite result |PASS|PASS|

The result is inside the requested180–220 range. No load_tests hook, skipped directory, disabled test, renamed hidden test archive or discovery filter reduces the count. Ordinary `python -m unittest discover -s tests -v` discovers the smaller suite. `python scripts/test_inventory.py --check-range` reports the actual IDs/file/class counts without filtering.

Disposition of the1000 original cases:704 map to consolidated named assertion groups;285 generated wrappers become explicit rejection tables, including schema3/schema4 inherited coverage;7 remain standalone where override/return behavior matters;4 redundant hash-only wrappers are removed and replaced by the central fingerprint test. The four removed bodies were the whole-campaign hash tests in AutonomyTests, EconomyTests, DashboardTests and DungeonTests; their audit rows name the replacement. Eleven other repeated whole-file hash loops are centralized, while subsystem-specific legacy payload, prefix, provenance, ownership and behavior assertions remain.

Subcases preserve distinct diagnostic labels and isolate temporary file/container mutations even after a failure. Shared fixtures avoid a full repository copy for every wrapper. Isolation tests cover rollback, deletion/new-file handling, failed assertions, symlink write-through protection and refusal to roll back the real checkout. JSON-only rejection helpers call the relevant unchanged production subsystem validators, reusing only identical validated frontmatter parses. Index, schema, source/metadata, CLI, current/historical finance, dashboard and representative full-repository integration checks still use their full entry points. No production validation rule was relaxed to accommodate consolidation.

Critical retained protections include entity/index identity, checkpoint/schema continuity, ledger/reconciliation/restricted ownership, resource/spell costs, historical events, NPC/companion distinctions, time/travel, quests/contracts, property/noncash liquidity, public references and actual validation/reporting behavior. New autonomy tests exercise eight identities, no appointments/possessions/schedules/events/finance/relationship changes, public payload/provenance, causal completeness, finite evidence, schedule stages and knowledge/communication boundaries.

Coverage limitations: a discovered method is not an assertion or scenario. Much of the original negative-scenario coverage remains as subcases;81.6% fewer discovered cases does not mean81.6% fewer invariants, nor equivalent branch/line coverage. Four repeated hash-only bodies and eleven repeated loops were removed, not historical evidence. Narrow JSON mutation tests no longer execute every unrelated validator on every row; full integration tests provide representative cross-system protection rather than exhaustive combinations. No branch/line coverage or universal secret-detection equivalence is claimed. Some pure helper and schema3/schema4 scenarios intentionally overlap to protect compatibility. Grouped tests can take longer per method, and temporary copies remain per integration group.

## Preservation, unknowns and privacy

The new preservation manifest records the base, six authorized existing-owner before/after SHA256 pairs, complete original JSON payloads and329 untouched campaign-file hashes. Revised owners are the five reused characters and npc-autonomy-and-time. Earlier fixture updates change only current hashes for those six authorized owners; original before hashes and prior-phase after evidence are retained. All original structured fields are preserved. Three added character designs and one approval provenance document are new safe reference material, not historical events.

Before/after: Year848 Suncrest61 Day18119:30 Ashvale Estate; HP100/100, MP400/400, normal equippedDEF49 and conditional51 only when Night Sovereign worn (current configuration UNKNOWN); Nexus156/180, wagon60/60. Controlled74590cp, unpaid31700cp, uncommitted42890cp; current allocations remain UNRECONCILED / UNKNOWN. Ledger4, checkpoint, history, property, companions, resources, quests, contracts, custody/evidence,20 roads,41 businesses,17 industries and12 proposed trade relationships remain unchanged. No current location, funds, possession, office, knowledge or actual relationship is inferred from the new designs.

Repository metadata was checked as public and visibility remains unchanged. Public content contains safe design traits/values/concerns and established canon only: no secret motivations, hidden identities, conspiracies, informants, secret faction plans, unrevealed betrayals or private GM outcomes are added. gm-reference metadata is not proof of Theron's knowledge; claim-level source/discovery review remains required. Secret simulation/outcomes need separate safe storage and are outside this public framework.

## Validation results

Baseline on the exact merged-main checkout: normal and optimized validation passed with243 entities;1000 tests passed in219.984s. Implementation: normal/optimized validation passed with246 entities;184 tests passed in136.378s. Focused new autonomy checks passed8/8, preservation3/3 and fixture-isolation3/3. Existing finance consistency, historical preservation and earlier subsystem checks pass within the consolidated full suite.

Economy report, dashboard generation/freshness, quest readiness, test-count audit and diff checks pass. Current cash remains74590cp. Ending design remains blocked pending the existing18 answer approvals and14 clue routes; no final story readiness or new world-event outcome is claimed. The dashboard was regenerated after the final index/documentation formatting changes and its freshness check passed.

No gameplay occurred: no time advance, NPC movement, event execution, revenue, payment, resource/bond/relationship change, official appointment, inventory/title change, quest progress or repository visibility action. Open this single PR, do not merge or begin PR8, then stop for player review.

## Added and modified files

- `changes/CHANGELOG.md`
- `changes/chronicles/phase2-07-autonomy-approval.md`
- `docs/npc-autonomy-and-world-events.md`
- `docs/phase2-07-review.md`
- `docs/phase2-07-test-audit.csv`
- `docs/phase2-07-test-mapping.json`
- `docs/phase2-07-test-reduction.json`
- `entities/characters/aveline-hartwell.md`
- `entities/characters/cassian-thornmere.md`
- `entities/characters/durnek-stonevein.md`
- `entities/characters/elowen-marcrest.md`
- `entities/characters/liora-thistlebloom.md`
- `entities/characters/mira-hearthwick.md`
- `entities/characters/orrin-valecrest.md`
- `entities/characters/selene-harrow.md`
- `entities/rules/npc-autonomy-and-time.md`
- `index.json`
- `scripts/autonomy.py`
- `scripts/autonomy_designs.py`
- `scripts/governments.py`
- `scripts/test_inventory.py`
- `tests/case_support.py`
- `tests/fixtures/chunk10-preservation.json`
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
- `tests/test_autonomy.py`
- `tests/test_case_support.py`
- `tests/test_day137_finance.py`
- `tests/test_day156.py`
- `tests/test_day181.py`
- `tests/test_day181_final.py`
- `tests/test_dungeons.py`
- `tests/test_economy.py`
- `tests/test_gm_dashboard.py`
- `tests/test_guilds.py`
- `tests/test_justice.py`
- `tests/test_north_return_house.py`
- `tests/test_phase2_autonomy.py`
- `tests/test_phase2_dungeons.py`
- `tests/test_phase2_economy.py`
- `tests/test_phase2_geography.py`
- `tests/test_phase2_governments.py`
- `tests/test_phase2_guild_underworld.py`
- `tests/test_phase2_settlements.py`
- `tests/test_preservation.py`
- `tests/test_quest_framework.py`
- `tests/test_settlements.py`
- `tests/test_travel.py`
- `tests/test_validate.py`
