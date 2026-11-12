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
Year 847, Day 153, 22:05, woodland north of the northern freight enclosure near Greyhaven; Theron HP100/100 MP337/400 DEF26 S+ Level5, with Nyx and Shade, safe/not in combat. Party/lodge cash555gp; academy separate. Campaign paused.

The [cumulative user handoff](archive/session-handoffs/year847-day153-user-handoff.txt) supplies the newly played developments; the [chronicles](changes/chronicles/year847-day153-development.md) label confidence and timeline gaps. Current checkpoint schema2 replaces separate personal campaign balances with voluntarily consolidated accounts and distinguishes removed chains from retained anchors. The [Day46 checkpoint](archive/checkpoints/year847-day046-0915.json) remains historical. Written current canon overrides older artwork and legacy snapshots.

## Caveat
This is a **curated entity extraction**, not a verified transcription of every historical chat message. The entity set covers major named people, creatures, places, items, quests, factions and core rules. Secondary locations and NPCs remain discoverable in the archived registry and can be promoted into entities on demand, with evidence.

## Character card artwork

[View the labeled party card gallery](artwork/player-cards/README.md) for Theron Ashvale, Garrick Vale, Nyx Thorne, and Lyra Moonvale.

[Browse all campaign artwork](artwork/README.md), including family, animal companions, Vaeltharion, and location concepts.
