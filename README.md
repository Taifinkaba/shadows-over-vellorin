# Shadows Over Vellorin — Entity-Based Canon Repository (v2)

**Source of truth:** `entities/` contains small, authoritative entity records. `state/checkpoint.json` is the current snapshot, **not** a replacement for historical events. `index.json` provides ID/type/path lookup.

## Retrieval (normal ChatGPT)
1. Fetch `README.md`, `governance/precedence.md`, and `state/checkpoint.json`.
2. Search `index.json` for the **specific character, location, quest, item or mechanic**. Fetch only relevant `entities/<type>/<id>.md` files (usually 1–4).
   For verified Theron mechanics, fetch `entities/mechanics/theron-abilities.md`, `entities/mechanics/theron-skills.md`, or `entities/mechanics/theron-spells.md`. Financial ownership and custody boundaries are in `entities/mechanics/party-finances.md`. None requires full-repository ingestion.
3. For disputes, follow the entity's `source_refs` into the historical modules or `archive/session-handoffs/`; the original three intact documents remain under `archive/`.
4. GM-secret entries must not be narrated as Theron's knowledge. The repository is intended to be **private**.
5. Avoid full-repository ingestion. For scene recaps, use current checkpoint plus relevant entities.

## Codex change flow
Work in a `lore/*`, `session/*` or `reconcile/*` branch, or an explicitly user-requested maintenance branch. Change targeted entity files and, if in-game progress occurred, update `state/checkpoint.json` in the **same PR**. Update `changes/CHANGELOG.md`. Install `requirements-dev.txt`, run `python scripts/validate.py` and `python -m unittest discover -s tests -v`; wait for user approval to merge. No direct pushes to protected `main`.

## Data model
Each entity Markdown file has YAML frontmatter: `id`, `type`, `status`, `visibility`, `source_refs`. `index.json` is the machine-readable routing directory. `archive/legacy-modules` preserves original split files **as evidence, not current instructions**. Earlier source material was not rewritten or discarded. Optional `checkpoint_values` expose established snapshot facts for comparison with the checkpoint; they do not advance the campaign. See `docs/validation.md` for the schema, test commands and limits, and `archive/README.md` for source-path resolution.

## Geography and travel

[Travel retrieval guide](docs/geography-and-travel.md) routes to the indexed location hierarchy, road registry and travel procedure. Historical reports, proposed corridors and unknown conditions remain distinct; no automatic travel or resource spending.

## Settlements and services

[Settlement directory](docs/settlement-directory.md) routes eleven existing locality/property profiles and parent-scoped business/service records. Unknown owners, prices and stock stay unknown; no automatic income, purchases or NPC assignments.

## Justice and custody

[Justice/custody directory](docs/justice-and-custody-directory.md) links existing authorities, explicitly proposed institutions and the single custody register. Unknown jurisdictions, receiving officers and prison destinations stay unknown; no automatic transfers or legal outcomes.

## Guilds and contracts

[Guild/contract directory](docs/guild-and-contract-directory.md) routes existing independent organizations, historical contract references and the proposed Concord. Archived branch designs, rank domains, funding and legal authority remain separate; no automatic payouts, licensing or enrollment.

## Dungeons and exploration

[Dungeon/exploration directory](docs/dungeon-and-exploration-directory.md) routes existing sites, source-derived section states, ecology/hazard references and unapproved designs. Existing owners retain exploration, inventory and outcomes; no automatic resets, respawns, loot or clearing.

## Property and economy

[Property/economy directory](docs/property-and-economy-directory.md) routes existing property and business owners, payroll/construction/pricing/trade procedures and read-only financial reports. The existing finance ledger stays the single cash authority; no automatic income, payment, valuation or ownership change.

## Current checkpoint
Year848 Suncrest36 Day156, **20:15**, Ashvale Estate family sitting room; **ENDED**. HP100/100 MP378/400, DEF49 normally,51 only wearing Night Sovereign (currently carried). Nexus156/180; separate Sovereign Expedition Wagon60/60. Vanguard completed mundane, no mana pool. Controlled771gp9sp;317gp committed/unpaid,454gp9sp uncommitted.

[Current finance ledger](state/finance-ledger.json), [Day156 player-established chronicle](changes/chronicles/year848-day156-end-session.md), [next-chat handoff](state/next-chat-handoff.md), [verification queue](state/open-verifications.md). Prior checkpoints remain history; no automatic income or gameplay advance.

## Caveat
This is a **curated entity extraction**, not a verified transcription of every historical chat message. The entity set covers major named people, creatures, places, items, quests, factions and core rules. Secondary locations and NPCs remain discoverable in the archived registry and can be promoted into entities on demand, with evidence.

## Character reference sheets

[Approved character-design directory](changes/chronicles/character-reference-design-approval.md) routes to 26 character sheets and anonymous-reference directions. Sheets separate recorded facts from player-approved appearance, clothing and mannerisms; historical and mystery gaps remain explicit. Use these descriptions for consistent image generation.

## Character card artwork

[View the 26 approved character reference portraits](artwork/character-references/README.md), paired with their character sheets.

[View the labeled party card gallery](artwork/player-cards/README.md) for Theron Ashvale, Garrick Vale, Nyx Thorne, and Lyra Moonvale.

[Browse all campaign artwork](artwork/README.md), including family, animal companions, Vaeltharion, and location concepts.
