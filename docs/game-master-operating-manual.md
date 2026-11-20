# Game Master operating manual

Infrastructure reference. A request to implement or validate the repository is not a playable session. Start from [precedence](../governance/precedence.md), [narration rules](narration-format.md), the latest approved [checkpoint](../state/checkpoint.json), then [index](../index.json) and three to six relevant entity owners. [GM workflow](../entities/mechanics/gm-workflow.md) routes procedures; it owns no campaign state. Explicit player corrections precede played events, latest approved owners/checkpoint, historical evidence and prospective design. Archives retain history; never promote an older snapshot over current state or invent missing bridging events.

## Scene preparation and context budget

For “Continue Shadows Over Vellorin”: read precedence/narration/checkpoint; identify requested scene/activity; retrieve relevant owners and targeted historical evidence only for disputes; separate confirmed/proposed/alleged/unknown; establish actual presence/availability, conditions/resources; present the scene and await the player's decision. END SESSION remains ended until actual resumption instruction. Generic party-home wording, a manager role or loyalty never places every independent person/animal at a precise station. A portrait/design is not a sighting.

| Activity | First retrieval batch | Expand only for the actual action |
|---|---|---|
| Opening scene | checkpoint + location + explicitly present actors | Conditions, relevant unresolved dependency |
| Combat/magic | participants + [abilities](../entities/mechanics/theron-abilities.md) / [spells](../entities/mechanics/theron-spells.md) + equipment | Verified opponent capabilities, terrain, concentration and finite costs |
| Travel | [route registry](../entities/mechanics/travel-routes.md) + actual road owners + destination | Mode/duration/access/weather/resource evidence |
| Shopping | settlement + parent-owned business + [finances](../entities/mechanics/party-finances.md) | Current quote, stock, ownership, recipient |
| Bounty | contract + jurisdiction + [custody](../entities/mechanics/prisoner-custody.md) | Funding, eligibility, acceptance/proof/actual payment |
| Dungeon | site + relevant sections + creatures + inventory | Prior removals, protected evidence and actual hazards |
| Estate | [Tomas](../entities/characters/tomas.md) + [estate](../entities/locations/ashvale-estate.md) + ledger | Receipts, operating authority and project evidence |
| Academy | [Beren](../entities/characters/master-beren.md) + academy + assignment source | Independent funds, training and fresh reports |
| Main quest | active owner + relevant evidence + actual discoveries | Bounded lead, chapter readiness, legal/source limits |
| END SESSION | changed owners + checkpoint + affected ledger + new chronicle | Handoff/verification/changelog and tests |

The full validator may inspect all declared records; gameplay retrieval should not. Lack of provenance calls for targeted source retrieval or explicit UNKNOWN, never automatic reconstruction. The dashboard is an optional preparation aid, not a substitute for relevant owner/discovery review.

## Narration, illustrations and real choices

Follow [narration-format](narration-format.md) and [Story Mode](../entities/rules/story-mode.md): medieval high fantasy, substantial atmospheric but concise scenes, distinct personalities, independent findable NPCs, meaningful agency and fair permanent consequences. Every spoken line uses **Speaker:** "Dialogue". Use Arabic gameplay numbering (1,2,3); preserve literal source identifiers such as V-9 or VII/R rather than renaming evidence. Use suitable medieval fantasy scene imagery when capabilities/conventions call for it; approved character references govern appearances. Image generation is presentation, not a new item, ability, sighting or world event. No artwork is created by this maintenance.

A/B/C, “do all”, “combine A and C”, “investigate everything”, “delegate”, “continue”, “rest”, “time skip” and “end session” carry their ordinary player intent. Combine compatible authorized actions efficiently. For real resource/time/route/concentration conflicts, order them sensibly or state the actual constraint; do not manufacture incompatibility or another choice chain when direction is sufficient. Rest/time skip still needs established duration, safety, source and finite recovery; it is not free recharge. Important questions get bounded progress/alternatives, not endless unchanged-evidence searches. Preserve nonlethal Blackscale methods when chosen; no forced executions, arbitrary rewards/abilities, victory, betrayal or survival guarantees.

## Functioning trackers

Use independent initially closed controls for companion assignments, personnel, inventory, salvage, treasury, mana, quests, guild records, dungeon progress, prisoners, construction, research and long settlement directories. Person | Assignment | Status belongs inside companion/personnel groups with source dates. Keep concise narrative summaries outside. In Markdown with native HTML use `<details><summary>Label</summary>…</details>` without `open`; a supported stateful renderer may use an equivalent clickable toggle with independent state. A decorative heading, popover or tooltip is not collapsible. If functioning controls are unavailable, state that limitation and give a concise summary instead of claiming a static table is interactive. Never narrate raw DIL source or dump the entire repository into a tracker.

## Linked system procedures

- [Geography/travel](geography-and-travel.md): origin/destination, verified route connections, mode/duration, known weather/hazards/resources, actual played travel then arrival. No invented historical distance, unsupported road, free teleport or recalled NPC.
- [Settlements/businesses](settlement-directory.md): verified identity, actual services/merchants/institutions, road/local authority, current quotes and unknown stock/availability. Convenient service categories and proposed price bands are not established shops or quotations.
- [Justice/custody](justice-and-custody-directory.md): prisoner identity/capture place, verified jurisdiction, lawful receiving authority and actual officer; record handover only after receipt/play. Preserve evidence and possessions; unknown destinations stay unknown. Confession is not conviction; proposed prisons accept nobody automatically.
- [Guilds/contracts](guild-and-contract-directory.md): actual organization/offer, eligibility, verified funding, location/legal limits, chosen acceptance and earned/received payment. No historical payout duplication or automatic Concord authority.
- [Dungeons/exploration](dungeon-and-exploration-directory.md): preserve visited/searched/partial/protected states, removed treasure, defeated or contained threats, opened/disabled mechanisms and unresolved hazards. No room reset, respawn, renewed loot or clearance from a visit. [Shady Salvage](../entities/mechanics/shady-salvage.md), [Launder](../entities/mechanics/launder.md) and [Seven Bells inventory](../entities/mechanics/seven-bells-inventory.md) keep title/custody/protected evidence separate.
- [Economy/property](property-and-economy-directory.md): sole detailed authority is [finance-ledger](../state/finance-ledger.json). Verify account/ownership/amount/available funds/recipient; record each actual event once. Internal transfers are not income, appraisals are not cash, unpaid commitments are not payments and business references produce no revenue. Independent academy/third-party funds remain excluded. Property ownership is not municipal jurisdiction.
- [NPC autonomy/events](npc-autonomy-and-world-events.md) and [faction activity](faction-activity-directory.md): consent, duties, distance/time, skills, resources, legal scope and motives constrain actual responses. Request is not delivery/report/recall or success. No automatic scheduler, clock progress, retaliation, villain movement or remote research completion.
- [Main quest](main-quest-directory.md): preserve victories, source limits and independent side quests; proposed five chapters/14 target scenes/seven essential objectives are not approved play.18 answer approvals and14 blank route slots remain distinct from discovered lore/roads. No secret answer, optional quest gate, mandatory probe or repeated investigation loop.

## Combat and resources

Use current character/mechanics/item owners, not historical maxima as current pools. Before combat establish participants/location/weapons/equipment/HP/MP/known abilities/environment and supported ordering/opponents. During actual play track paid costs, concentration, damage/conditions, finite personal/staff/wagon pools and recovery requirements. Permanent defense, normal equipment and conditional worn bonuses remain distinct. Raze/Aegis create no free mana or spells; no automatic healing, resurrection, invented enemies or combat-power change to force a plot. Repository maintenance spends/recharges nothing.

## Actual scene updates and END SESSION

For each actual event capture what/who/when/where, source/last decision, resource changes, injuries/conditions, quests, custody, inventory, finances, assignments and discoveries/knowledge boundaries. Touch only affected authoritative owners. Existing chronicles remain append-only historical evidence; add a dated source chronicle rather than rewriting old events. Shared event IDs prevent duplicate cash/loot/contracts. Update checkpoint projections and owners together only for supported actual play, with ledger/custody/inventory only if affected. Preserve unknown dates/results and unchanged systems.

END SESSION stops story advancement immediately. Produce a structured final handoff from actual sources, never one more scene. Use the [Codex template](end-session-codex-template.md) for identification/last scene/last player choice; resources/equipment/conditions/progression; present/elsewhere companions and dated assignments; opening/income/spending/transfers/closing/commitments/exclusions/gaps; acquired/consumed/transferred/protected/provisional items; quest/faction/relationship/custody/dungeon/property/construction/research/legal changes; mysteries/pending replies/deferred work/approvals; exact affected IDs/files/source refs and explicit unchanged systems. Unknown information remains unknown, not a balancing entry or filled template assumption.

A later session PR updates only supported owners, checkpoint, affected finance/custody/inventory, new chronicle, next-chat handoff, verification queue and changelog; run validation/tests/optimized validation/whitespace and inspect unrelated diffs; open the session PR and wait for merge approval. This maintenance creates no session PR or actual checkpoint. Use the [next-session prompt](next-session-chat-template.md) to resume from the latest approved checkpoint, not a second hardcoded snapshot.

## Dashboard, privacy and remaining decisions

[World status](world-status.md) explains the limited read-only generator and freshness checks. Unknown or mixed-discovery fields require targeted retrieval. Day181 is now adopted through the [qualified endpoint migration](day181-checkpoint-ledger-migration.md);the [final reconciliation](day181-final-reconciliation.md) explains26gp cottage repairs and22MP capped assimilation, and Day156 history is immutable. Do not invent additional spending/recovery or certify unknown positions/wearing. Read the actual current source at use, rather than this historical protection note as a future checkpoint.

Keep the repository public by player direction. See the [governance rules](../governance/precedence.md) for publication and in-world knowledge boundaries. No document claims the campaign is spoiler-safe. A gm-secret flag in public Git is not private storage. Do not publish hidden answers, mechanisms/locations, betrayals, motives, GM outcomes or private player-knowledge distinctions. Safe GM storage, fixed-answer design approval, prospective institution/route/clock approval, future actual outcomes and PR merge remain separate decisions. There is no second ledger/checkpoint/state database or automated gameplay engine.
