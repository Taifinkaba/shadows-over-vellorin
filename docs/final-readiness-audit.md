# Final readiness audit — World Bible integration

**Audited main:** `549e07a8376c3c19c1d979cc7da187468623a3ac` (merged Chunk10). This is a documentation-only review, not another integration chunk, session, approval of proposed lore or change of campaign state.

**Overall: READY WITH LIMITATIONS for ordinary play from the approved Day156 checkpoint.** Known scenes, supported abilities, established services and source-backed investigations can proceed on player instruction. This is not unrestricted world coverage or a general gameplay write-back engine. **BLOCKED:** activation/completion of the proposed five-chapter ending until critical design/private storage/clue coverage are resolved. **REQUIRES APPROVAL:** adopting Day181, future schema migrations and prospective worldbuilding actually needed by the chosen activity. No need to approve the entire atlas or every optional mystery before ordinary local play.

## Integration and ownership verification

GitHub reports PRs [#11](https://github.com/Taifinkaba/shadows-over-vellorin/pull/11), [#12](https://github.com/Taifinkaba/shadows-over-vellorin/pull/12), [#13](https://github.com/Taifinkaba/shadows-over-vellorin/pull/13), [#14](https://github.com/Taifinkaba/shadows-over-vellorin/pull/14), [#15](https://github.com/Taifinkaba/shadows-over-vellorin/pull/15), [#16](https://github.com/Taifinkaba/shadows-over-vellorin/pull/16), [#17](https://github.com/Taifinkaba/shadows-over-vellorin/pull/17), [#18](https://github.com/Taifinkaba/shadows-over-vellorin/pull/18), [#19](https://github.com/Taifinkaba/shadows-over-vellorin/pull/19) and [#20](https://github.com/Taifinkaba/shadows-over-vellorin/pull/20) merged. All ten merge commits independently pass `git merge-base --is-ancestor <merge-sha> HEAD` at this main revision; merge status alone was not treated as proof of ancestry.

[Index](../index.json), [precedence](../governance/precedence.md), [GM workflow](../entities/mechanics/gm-workflow.md) and validation confirm functioning routes for all ten integration chunks. Entity identity/state remains in original owners; the checkpoint owns the current scene and detailed money remains in the sole finance ledger. Directories, helper registries, dashboards and empty templates supply routing/procedures, not additional editable balances or positions. No new competing authority was found. Existing duplicated Day156 prose across quest/faction records is a drift risk, not another ledger; dated older headings and the Chunk1 audit are historical baselines, not the current inventory of implemented systems.

## A. Ten gameplay domains

| Domain | Verdict | Specific authority/retrieval and practical boundary |
|---|---|---|
| Geography/travel | READY WITH LIMITATIONS | [Travel guide](geography-and-travel.md), [route registry](../entities/mechanics/travel-routes.md), individual route owners. Four limited historical connections coexist with proposed corridors; unknown duration/access/borders and unsupported entrance connections must stay unknown. Approve only a needed new route; never infer a journey from adjacency. |
| Settlements/businesses | READY WITH LIMITATIONS | [Settlement directory](settlement-directory.md), parent location/service owners.11 profiles/14 references are retrievable; current stock, vacancies, quotes and many proprietors remain unknown. Six price bands are proposals, not actual offers. |
| Combat/magic/resources | READY WITH LIMITATIONS | [Theron](../entities/characters/theron-ashvale.md), [abilities](../entities/mechanics/theron-abilities.md), [spells](../entities/mechanics/theron-spells.md), [skills](../entities/mechanics/theron-skills.md), equipment and [Story Mode](../entities/rules/story-mode.md). Finite pools/defense/locks agree with checkpoint. Establish relevant opponents/companion current pools and missing spell bases before use; no inferred full pools, extra discount, free recovery or new powers. |
| Economy/property | READY WITH LIMITATIONS | [Ledger](../state/finance-ledger.json), [party finances](../entities/mechanics/party-finances.md), [economy directory](property-and-economy-directory.md). Current reporting, commitments and exclusions work. **Financial write-back limitation below must be addressed before persisting a new cash/paid-construction outcome.** Rates, business receipts and current academy accounts remain unknown. |
| NPC autonomy/factions/events | READY WITH LIMITATIONS | [Assignment guide](npc-autonomy-and-world-events.md), [faction directory](faction-activity-directory.md), original actors/chronicles. Roles and request handles are not fresh positions or successes. Verify consent, current availability, communication, elapsed time and resources. No active clocks or automatic remote results. |
| Guilds/contracts | READY WITH LIMITATIONS | [Guild directory](guild-and-contract-directory.md), original guild profiles and [contract registry](../entities/mechanics/contract-registry.md). Historical rewards are already accounted; no blanket active offer board or approved Concord. Need a real funded offer, eligibility and chosen acceptance for new work. |
| Dungeons/salvage | READY WITH LIMITATIONS | [Dungeon guide](dungeon-and-exploration-directory.md), site/section and original salvage/evidence owners.18 context references/14 scoped states are retrievable, not18 fully specified dungeons. No respawn, clearance from a visit, new entrance road or regenerated loot. Five new designs remain unlocated/unapproved. |
| Justice/custody | READY WITH LIMITATIONS | [Justice guide](justice-and-custody-directory.md), [custody owner](../entities/mechanics/prisoner-custody.md), later case/character sources. Existing offices/limits work; actual handover is **BLOCKED for that action** until jurisdiction, operational recipient/officer, lawful transport and receipt are verified. New prison proposals supply none of these. |
| Quests/evidence | READY WITH LIMITATIONS; proposed ending BLOCKED | [Main quest directory](main-quest-directory.md), original quest owners, [historical crosswalk](../entities/mechanics/quest-history-and-identities.md). Existing victories/known leads persist;18 blank answers and14 unfilled route slots are not playable resolutions or geography. First Hour's completed objective coexists with wider active restoration; completed Lyanna restoration does not close other V-9 cases. |
| GM/dashboard/END SESSION | READY WITH LIMITATIONS | [Operating manual](game-master-operating-manual.md), [dashboard guide](world-status.md), [Codex template](end-session-codex-template.md), [next-chat template](next-session-chat-template.md). Retrieval, source-qualified projection, closed disclosures, combined-action guidance and empty handoffs work. Templates themselves are READY; actual updates still need played evidence, affected-owner synchronization and merge approval. Dashboard supports checkpoint5/ledger2 and deliberately omits mixed/private detail. |

### Action-specific write-back blocker

[Finance validation](../scripts/validate.py#L365) accepts exactly five historical arc events with fixed amounts and ties their closing balance to current cash; it also requires the expansion unpaid/unstarted and the restitution account at its original amount. [Economy procedure](../entities/mechanics/economy-accounting.md) explicitly anticipates a separately reviewed ledger migration for new actual events. A disposable-copy probe adding one synthetic event was rejected as `ledger: duplicate or missing arc event`; no real posting was attempted.

Therefore the current framework cannot simply append an ordinary new expense, pay construction, spend restitution funds or adopt the lower Day181 total through a normal data-only session edit. Before such an outcome is persisted, extend the **same** ledger/validator with sourced current-period events or an explicitly qualified endpoint/reconciliation representation while preserving the Day156 arc as history. Do not alter historical opening/events to force a new closing balance, add a fake balancing transaction, weaken checks without review or create a second ledger. This is a documented architectural boundary, not a failing baseline regression. Existing maintenance-preservation fixtures also require deliberate review for genuinely approved future owner changes; historical archives/chronicles must remain preserved.

## B. Proposed ending: approval checklist without answers

Sources: [question routing](../entities/mechanics/quest-evidence-and-mysteries.md), [chapter/objective plan](../entities/mechanics/quest-resolution-proposals.md), [empty answer crosswalk](../entities/mechanics/quest-answer-blueprint.md), `python scripts/quest_framework.py --readiness`.

The current proposal maps **10 core-design questions** to its seven essential objectives. These are design/readiness dependencies, not orders to capture every named person or force every truth to become a player discovery. Approve bounded scope/causality/evidence access, not automatic verdicts or outcomes. All boxes below remain unchecked.

| Approval to review | Proposed chapter coverage |
|---|---|
| [ ] `mystery:surviving-crown` — supported surviving command/opposition scope |1 /3|
| [ ] `mystery:v9-controller` — distinguish controller from known authorization |1|
| [ ] `mystery:v9-transferred` — remaining transferred-case facts and lawful possibilities |2|
| [ ] `mystery:v9-other-cases` — distinct remaining central harms and bounded disposition |2|
| [ ] `mystery:dene` — supported lead/scope; not mandatory capture of every subordinate |3|
| [ ] `mystery:acting-receiver` — verify alleged role/network links without guessed identity |3|
| [ ] `mystery:fb5` — bounded foreign-layer threat and resolution/containment design |4|
| [ ] `mystery:northern-index` — source-compatible discovery and evidential purpose |4|
| [ ] `mystery:er7-safety` — bounded command/safety problem, not assumed neutralization |4|
| [ ] `mystery:witness-authority` — essential authenticity/authority and informed Witness choice |4 /5|

**Eight optional-design questions are not ending prerequisites:** `thane-review`, `sorn-review`, `remaining-notices`, `a07-consent`, `correspondent`, `watcher`, `freight-director`, `damaged-channels` (all under `mystery:`). Independent proceedings and optional identities/lore can remain consequences pending, with honest handoffs. New case decisions still require actual lawful process/play/rulings; a design approval cannot prewrite a conviction, release or transfer. If changing the core/optional mapping, approve that scope change explicitly rather than silently expanding the ending gates.

**Fourteen route slots:** `clue-route:<objective>:1` and `:2` for `command-chain`, `v9-harm`, `fifth-bell`, `counterfeit-authority`, `surviving-opposition`, `witness-choice`, `immediate-consequences`. At least one actionable path in **each pair**, with coverage of every required question, is essential; neither slot number has special priority. A second materially distinct path is preferred resilience, not automatically seven more mandatory searches. No route currently has an approved answer/method/location/discovery record. Finite graph reachability passes, but does not make these blank routes traversable.

Before activating the ending:

- [ ] Approve the five-chapter3/3/3/3/2 pacing proposal and seven-objective scope, retaining scene combination/reordering, nonlethal alternatives and independent side quests.
- [ ] Establish genuinely private GM storage/access and a discovery/publication policy **before** writing unrevealed values.
- [ ] Review the10 core designs against played evidence/victories/identity distinctions; keep unrevealed answers out of this public report/PR.
- [ ] Design executable source-compatible clue coverage, actual geography/access/resources and success/partial/setback exits; no sole mandatory probe or endlessly repeated unchanged evidence.
- [ ] Review activation/storage/schema support separately: current public validators intentionally require blank values/route slots. Do not populate them or claim activation merely because this audit merges.

## C. Worldbuilding decisions: approve only what the next activity needs

| Candidate / source | Dependency or canon conflict | Priority |
|---|---|---|
| Local recipient/jurisdiction, [justice crosswalk](../entities/mechanics/justice-proposals.md) | Verify an existing competent office, receiving officer and facility first.7 proposed roles/12 buildings/16 officials are not operational; private estate ownership gives no municipal powers. | High only before an actual capture/handover; no need to enact a national prison network. |
| Needed road, service quote, staffing/payroll term | Original route/business/person owner, access evidence and authority/budget; unknown stock/wages are not free/unlimited. Existing lodge/springs/information price-increase provenance remains incomplete. | High when that journey/purchase/work decision is chosen. |
| [Geography](../entities/mechanics/world-geography.md) | Aethoria is proposed continent; Elyndor/Frostmarch are unclassified proposed names. Vellorin's territorial identity does not prove a new political type/borders. Valedorn justice geography/relationship to Vellorin is unresolved. | Low for established local play; settle before cross-border authority/world map use. |
| [Guild network](../entities/mechanics/guild-network.md), [Concord](../entities/factions/continental-guild-concord.md) | Three archived Wayfarers branch candidates need actual premises/staff/source approval; six professional designs and eight Concord divisions do not supersede independent Wayfarers/academy. No automatic fees, members, commissions or officials. | Approve a needed local branch/service first; continental redesign optional. |
| Proposed officials | Resolve similar-name collisions and exact office/powers/place without replacing current officials, merging identities or fabricating relationships. | Only when needed for an approved institution; otherwise defer all16. |
| [Dungeon designs](../entities/mechanics/dungeon-design-proposals.md) | Five candidates lack approved placement/access/history. Shattered Meridian's supplied SS label conflicts with the proposed F–S+ scale; do not silently normalize it. Preserve existing locations/exploration and protected loot boundaries. | Only before choosing a new designed expedition; not needed for existing sites. |
| [Clocks/reputation](../entities/mechanics/world-development-proposals.md) | No active clocks/starting progress. Need sourced owner/start, triggers, possible consequences, approval and safe visibility; archived prospective values are not current. | Optional; manual supported NPC responses already possible during actual play. |

## D. Day156 versus supplied Day181 — no adoption

Current authority: [checkpoint](../state/checkpoint.json), [ledger](../state/finance-ledger.json), [handoff](../state/next-chat-handoff.md). Supplied endpoint provenance: the user's original Chunk1 instruction, preserved in the [integration audit comparison](world-bible-integration-audit.md). It is not an independently recovered Day181 transcript or approved current snapshot.

| Compared field | Authoritative Day156 | Supplied Day181 | Gap / required decision |
|---|---|---|---|
| Day/date | Year848 Day156 | Year848 Day181 |25-day label difference; intervening played chronology not supplied. |
| Season day | Suncrest36 | Suncrest61 |+25 season-day labels; no invented events from calendar arithmetic. |
| Time |20:15|19:30|Endpoint clock time differs; no fabricated elapsed activity or rest. |
| Location precision |Ashvale Estate family sitting room|Ashvale Estate|Same estate; exact room unspecified, not proof of movement to another room. |
| Personal MP |378/400|400/400|+22 arithmetic difference; no verified casting/recovery sequence and no invented recovery transaction. |
| Controlled cash |771gp9sp =77190cp|745gp9sp =74590cp|−26gp/2600cp; no verified expense, ownership adjustment or account allocation. |
| Uncommitted cash |454gp9sp =45490cp|428gp9sp =42890cp|−26gp derived availability difference; not a second outflow. |

**Equal supplied fields:** Year848, Suncrest season, HP100/100, normal49/conditional51 defense convention, Nexus156/180, magic wagon60/60 and317gp committed/unpaid. Actual mask wearing is unspecified later: carried/not equipped is the Day156 observation, not confirmed Day181 attire. The later endpoint does not independently supply base defense, equipment list, session status, exact room, conditions, companion stations, skills, account breakdown, construction progress or other world/case/quest changes. Missing fields are not asserted differences or permission to fill them. The26gp coincidence with an old reserve balance does not identify which funds changed.

Safe separate reconciliation sequence:

1. Approve adopting the **supplied endpoint** explicitly, including how to mark unsupplied status/room/equipment/account allocation and retained last-verified observations. This audit grants no adoption.
2. Supply any actual intervening evidence available; otherwise explicitly retain chronology,26gp and22MP provenance gaps. No invented expenditure/recovery, suspense balancing entry or assumed reserve withdrawal.
3. Review a compatible same-ledger/schema extension separating historical Day156 arc/accounts from the new endpoint and unknown breakdown. Keep317gp unpaid and exclusions/noncash ownership intact; no second ledger or pretend itemized receipts.
4. Preserve old checkpoint/entity values as historical fixtures; update only explicitly approved current owners, checkpoint, qualified ledger, new reconciliation chronicle, handoff, verification queue and changelog together in a separate PR. Review all affected maintenance fixtures and report support before calling the endpoint current.
5. Validate/test normal and optimized modes, regenerate dashboard, verify old views stale, inspect unrelated diffs and obtain merge approval. Do not advance play to manufacture the missing bridge.

## E. Privacy and discovery

Live GitHub repository metadata confirms **public** visibility at this audit. [Governance](../governance/precedence.md) still requires privacy/spoiler separation; the conflict remains unresolved. No visibility setting was changed. This report does not list or reproduce concealed answers, identities, mechanisms, motives, locations or private knowledge distinctions, and does not certify existing repository contents/history spoiler-safe.

Genuinely private storage is required before adding unrevealed fixed answers, secret faction/NPC intentions, hidden event/clock outcomes, undiscovered dungeon solutions and confidential discovery/disclosure distinctions. A gm-secret frontmatter flag in public Git is not access control. If already-public sensitive material needs remediation, review access/history implications privately; this report is not permission to migrate, redact history or change visibility. Player knowledge needs positive claim-level discovery evidence, not repository access, faction membership or gm-reference metadata. Dashboard tests demonstrate conservative selector filtering, not universal semantic redaction of every source passage.

## F. Validation and preservation

At the audited main revision:

- Normal and optimized `scripts/validate.py`: PASS;207 indexed entities/41 archived modules. The18-answer/14-route note is an expected nonfatal design-readiness warning.
- `python -m unittest discover -s tests -v`: **642 tests PASS**. No preexisting failures or audit regressions; no code/test changes are part of this report.
- Dashboard JSON and Markdown generation, `--check-view` on the generated JSON, quest readiness and economy reporting: PASS. Markdown supplies13 independent initially closed groups. Freshness/visibility/negative cases also pass in the full suite.
- `git diff --check`: PASS. Audit diff is limited to this report, its README link and governance-required changelog entry. Campaign entities, index, state, archive, original chronicles, scripts, tests and existing preservation fixtures remain byte-for-byte unchanged.

Structural references and ownership routes are valid. Remaining semantic freshness gaps include old “current” headings, unverified actor stations/pools, undefined jurisdiction/receivers, missing prices/payroll/receipts and unresolved identity matches; these require targeted source review, not invented refreshes. No duplicate mutable checkpoint/ledger/world database was found. The manual/templates describe future updates; preservation fixtures and snapshot-specific validators still need reviewed evolution for genuinely new approved outcomes.

## Approval order and safe next action

1. Choose resume-from-approved-Day156 versus a **separate** Day181 adoption review. Ordinary known Day156 scenes need no global worldbuilding approval, but require an actual player resumption instruction.
2. Before the first new money/construction write-back, approve the scoped same-authority schema/fixture migration; before any handover, verify its real receiving/legal facts. These are activity-specific gates, not permission to fabricate events.
3. Choose genuinely private answer storage/discovery policy; then approve essential ending scope,10 core designs and executable clue coverage. Review optional8 only if desired; do not turn them into mandatory gates.
4. Approve only route/service/institution/branch/dungeon details needed by the selected next activity; defer continental politics, extra officials, broad clock systems and unrelated designs.
5. Review/approve merging this documentation-only audit separately. Merge approval does not approve lore, endpoint adoption, transactions, secret publication or gameplay.

No campaign state changed. No gameplay, session PR, clock tick, financial/mana transaction, custody transfer, quest outcome or secret answer was generated; nothing was merged by this audit.
