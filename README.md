# Shadows Over Vellorin — Entity-Based Canon Repository (v2)

**Source of truth:** `entities/` contains small, authoritative entity records. `state/checkpoint.json` is the current snapshot, **not** a replacement for historical events. `index.json` provides ID/type/path lookup.

## Retrieval (normal ChatGPT)
1. Fetch `README.md`, `governance/precedence.md`, and `state/checkpoint.json`.
2. Search `index.json` for the **specific character, location, quest, item or mechanic**. Fetch only relevant `entities/<type>/<id>.md` files (usually 1–4).
   For verified Theron mechanics, fetch `entities/mechanics/theron-abilities.md`, `entities/mechanics/theron-skills.md`, or `entities/mechanics/theron-spells.md`. Financial ownership and custody boundaries are in `entities/mechanics/party-finances.md`. None requires full-repository ingestion.
3. For disputes, follow the entity's `source_refs` into the historical modules or `archive/session-handoffs/`; the original three intact documents remain under `archive/`.
4. This repository is **public** by player direction. Keep unrevealed GM material in separate private storage, and use claim-level discovery evidence before narrating information as Theron's knowledge.
5. Avoid full-repository ingestion. For scene recaps, use current checkpoint plus relevant entities.

## Codex change flow
Work in a `lore/*`, `session/*` or `reconcile/*` branch, or an explicitly user-requested maintenance branch. Change targeted entity files and, if in-game progress occurred, update `state/checkpoint.json` in the **same PR**. Update `changes/CHANGELOG.md`. Install `requirements-dev.txt`, run `python scripts/validate.py` and `python -m unittest discover -s tests -v`; wait for user approval to merge. No direct pushes to protected `main`.

## Data model
Each entity Markdown file has YAML frontmatter: `id`, `type`, `status`, `visibility`, `source_refs`. `index.json` is the machine-readable routing directory. `archive/legacy-modules` preserves original split files **as evidence, not current instructions**. Earlier source material was not rewritten or discarded. Optional `checkpoint_values` expose established snapshot facts for comparison with the checkpoint; they do not advance the campaign. See `docs/validation.md` for the schema, test commands and limits, and `archive/README.md` for source-path resolution.

## Geography and travel

[Travel retrieval guide](docs/geography-and-travel.md) routes to the indexed location hierarchy, road registry and travel procedure. Historical reports, proposed corridors and unknown conditions remain distinct; no automatic travel or resource spending.

## Settlements and services

[Settlement directory](docs/settlement-directory.md) routes historical locality/property records and the [ten approved Phase 2 settlement designs](docs/phase2-settlements-and-services.md), with parent-scoped business/service records. Unknown owners, prices and stock stay unknown; no automatic income, purchases or NPC assignments.

## Justice and custody

[Justice/custody directory](docs/justice-and-custody-directory.md) links existing authorities, the [approved five-realm government/legal designs](docs/phase2-government-and-law.md), qualified facility proposals and the single custody register. Unknown jurisdictions, receiving officers and prison destinations stay unknown; no automatic transfers or legal outcomes.

## Guilds and contracts

[Guild/contract directory](docs/guild-and-contract-directory.md) routes existing independent organizations, historical contracts and the [approved guild, voluntary Concord and underworld designs](docs/phase2-guilds-and-underworld.md). Archived branch designs, rank domains, funding and legal authority remain separate; no automatic payouts, licensing or enrollment.

## Dungeons and exploration

[Dungeon/exploration directory](docs/dungeon-and-exploration-directory.md) routes historical sites/section states and the [five approved finite dungeon designs](docs/phase2-dungeons-and-exploration.md), with qualified geography, encounters, hazards and reference-only monster stats. Existing owners retain exploration, inventory and outcomes; no automatic resets, respawns, loot or clearing.

## Magic and combat integration

[Phase2 final summary](docs/phase2-final-integration-summary.md) and [PR8 review](docs/phase2-08-review.md) route the eight-school/combat procedure, original spell/item authorities and five descriptive monster references. Numerical gaps, cost repricing, locked abilities and unresolvedSS stay explicit; design completion grants no spell, usable opponent, recovery, discovery or gameplay activation.

## Property and economy

[Property/economy directory](docs/property-and-economy-directory.md) routes existing property and business owners, payroll/construction/pricing/trade procedures and read-only financial reports. The existing finance ledger stays the single cash authority; no automatic income, payment, valuation or ownership change.

## NPC autonomy and world events

[NPC/assignment retrieval](docs/npc-autonomy-and-world-events.md) and [faction activity directory](docs/faction-activity-directory.md) route existing owners and historical chronicles. Manual communication/time-advance procedures preserve consent, resources and discovery boundaries; proposed clocks/categories create no events or automatic progress.

## Main quest and completion design

[Main quest directory](docs/main-quest-directory.md) routes original quest/evidence owners, protected achievements and unresolved questions. The five-chapter/14-scene ending plan remains proposed; unfilled answers and clue routes require approval and private storage. No story progress, new revelations or automatic completion.

## GM workflow, dashboard and session continuity

[World Bible Phase2 final session handoff](docs/phase2-final-session-handoff.md) records the completed development-session audit and next-chat source routing; no gameplay occurred and the canonical checkpoint/finance ledger are unchanged.

[Operating manual](docs/game-master-operating-manual.md) links all integration systems with targeted retrieval and actual-play update procedures. [World status](docs/world-status.md) documents the read-only reviewed-field dashboard and stale-view checks. Use the empty [END SESSION Codex template](docs/end-session-codex-template.md) and [next-session prompt](docs/next-session-chat-template.md) for future sessions; neither stores another checkpoint or starts gameplay. Mixed-knowledge details still require owner/discovery review.

## Final readiness review

[Post-integration readiness audit](docs/final-readiness-audit.md) records verified main/PR ancestry, gameplay limits, ending/private-storage approvals, financial write-back constraints and safe Day181 reconciliation steps. It is a dated baseline review, not campaign advancement or approval of proposed content.

## Current checkpoint

The campaign is paused at **Year 853 Day 52, 8:00 PM** in Westbridge. Controlled treasury is **275,718 gp**. Read the [checkpoint](state/checkpoint.json), [controlled ledger](state/finance-ledger.json), [independent DSI ledger](state/dsi-finance-ledger.json), [chronicle](changes/chronicles/year853-day52.md), [handoff](state/next-chat-handoff.md) and [verification queue](state/open-verifications.md). The [Hollow Veil checkpoint](archive/checkpoints/year853-hollow-veil.json) is historical.

## Caveat
This is a **curated entity extraction**, not a verified transcription of every historical chat message. The entity set covers major named people, creatures, places, items, quests, factions and core rules. Secondary locations and NPCs remain discoverable in the archived registry and can be promoted into entities on demand, with evidence.

## Character reference sheets

[Approved character-design directory](changes/chronicles/character-reference-design-approval.md) routes to 26 character sheets and anonymous-reference directions. Sheets separate recorded facts from player-approved appearance, clothing and mannerisms; historical and mystery gaps remain explicit. Use these descriptions for consistent image generation.

## Character card artwork

[View the 26 approved character reference portraits](artwork/character-references/README.md), paired with their character sheets.

[View the labeled party card gallery](artwork/player-cards/README.md) for Theron Ashvale, Garrick Vale, Nyx Thorne, and Lyra Moonvale.

[Browse all campaign artwork](artwork/README.md), including family, animal companions, Vaeltharion, and location concepts.
