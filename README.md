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

## Current checkpoint
Year 847, Day 472, **16:10**, Hollow of the First Hour; session **ENDED**. Theron HP100/100, personal MP312/400, permanent DEF46 / equipped49 with Frostguard Bracers, S+ Level5. Staff156/180, wagon60/60. Controlled cash673gp9sp; other account allocations unverified. Chronos Eye approximately19% and Dragon Slayer remain locked.

The [authoritative supplied checkpoint](archive/session-handoffs/year847-day472-user-handoff.txt), [First Hour chronicle](changes/chronicles/year847-day472-first-hour.md) and [next-chat handoff](state/next-chat-handoff.md) record the session end. First Hour resumed safely; other Guardian channels remain damaged. No prisoner transfers, Fifth Bell toll or additional reward. [Day153](archive/checkpoints/year847-day153-2205.json) and Day46 snapshots remain historical. Schema3 records partial cash allocation and unknown individual mana expenditures without inventing them.

Read [permanent narration rules](docs/narration-format.md): every spoken line identifies its speaker; detailed bookkeeping uses functioning independent, initially closed collapsible controls. See [open verifications](state/open-verifications.md) for missing historical bridges.

## Caveat
This is a **curated entity extraction**, not a verified transcription of every historical chat message. The entity set covers major named people, creatures, places, items, quests, factions and core rules. Secondary locations and NPCs remain discoverable in the archived registry and can be promoted into entities on demand, with evidence.

## Character card artwork

[View the labeled party card gallery](artwork/player-cards/README.md) for Theron Ashvale, Garrick Vale, Nyx Thorne, and Lyra Moonvale.

[Browse all campaign artwork](artwork/README.md), including family, animal companions, Vaeltharion, and location concepts.
