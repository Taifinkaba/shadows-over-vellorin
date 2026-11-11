# Shadows Over Vellorin — Entity-Based Canon Repository (v2)

**Source of truth:** `entities/` contains small, authoritative entity records. `state/checkpoint.json` is the current snapshot, **not** a replacement for historical events. `index.json` provides ID/type/path lookup.

## Retrieval (normal ChatGPT)
1. Fetch `README.md`, `governance/precedence.md`, and `state/checkpoint.json`.
2. Search `index.json` for the **specific character, location, quest or item**. Fetch only relevant `entities/<type>/<id>.md` files (usually 1–4).
3. For disputes, follow the entity's `source_refs` into `archive/legacy-modules/`; the original three intact documents remain under `archive/`.
4. GM-secret entries must not be narrated as Theron's knowledge. The repository is intended to be **private**.
5. Avoid full-repository ingestion. For scene recaps, use current checkpoint plus relevant entities.

## Codex change flow
Work in a `lore/*`, `session/*` or `reconcile/*` branch. Change targeted entity files and, if in-game progress occurred, update `state/checkpoint.json` in the **same PR**. Update `changes/CHANGELOG.md`. Run `python scripts/validate.py`; wait for user approval to merge. No direct pushes to protected `main`.

## Data model
Each entity Markdown file has YAML-style frontmatter: `id`, `type`, `status`, `visibility`, `source_refs`. `index.json` is the machine-readable routing directory. `archive/legacy-modules` preserves original split files **as evidence, not current instructions**. Earlier source material was not rewritten or discarded.

## Current checkpoint
Year 847, Day 46, 09:15, Mount Vaelspire; Theron HP 100/100 MP 376/400 DEF 26; total 495 gp 2 sp. Campaign paused.

## Caveat
This is a **curated entity extraction**, not a verified transcription of every historical chat message. The entity set covers major named people, creatures, places, items, quests, factions and core rules. Secondary locations and NPCs remain discoverable in the archived registry and can be promoted into entities on demand, with evidence.
