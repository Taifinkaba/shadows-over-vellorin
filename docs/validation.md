# Validation and structured snapshot facts

Install the pinned development dependency and run the same checks as CI:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
python -O scripts/validate.py
```

Python 3.12 is used in GitHub Actions. Tests copy campaign data into temporary directories and mutate only those copies. The validator reads files without changing them; failures exit with status 1 and an explicit error. `--root PATH` validates an alternate snapshot. No check depends on Python `assert`.

## Entity schema and routing

`index.json` schema version 2 indexes every file under `entities/`. IDs and paths must be unique; each path must be `entities/<type>/<id>.md`. Supported types are characters, creatures, items, locations, quests, factions, rules, and mechanics. Index ID/type/status/visibility must match the entity frontmatter.

Every entity starts with a YAML mapping between `---` delimiters. Required fields:

- `id`: nonempty lowercase slug, matching its filename and index ID.
- `type`: one of the supported types above.
- `status`: canon, last-verified, gm-secret-locked, active, research, completed, or user-locked.
- `visibility`: gm-reference or gm-secret. A gm-secret-locked record must have gm-secret visibility.
- `source_refs`: nonempty list of unique file paths resolved from the repository root.

Single-quoted, double-quoted and unquoted YAML strings are supported. Duplicate mapping keys, unsafe YAML object tags, missing fields and unknown fields are rejected. Paths must be normalized repository-relative POSIX paths, name existing files, and remain inside the repository after symlink resolution. Frontmatter ends at its closing delimiter; text in the Markdown body cannot supply missing metadata.

`checkpoint_values` is the optional structured snapshot mapping described below. New metadata fields or enum values require an explicit schema update with tests.

## Checkpoint agreement

The checkpoint remains the current campaign snapshot. The following entities now also expose their already-established current facts in `checkpoint_values` for mechanical comparison:

| Entity | Dotted checkpoint keys |
|---|---|
| theron-ashvale | date, time, location, status, theron.hp, theron.hp_max, theron.mp, theron.mp_max, theron.defense, theron.rank, money.theron_gp_sp |
| garrick-vale | money.garrick_gp_sp |
| nyx-thorne | money.nyx_gp_sp |
| lyra-moonvale | money.lyra_gp_sp |
| vaeltharion | world.vaeltharion_chains_attached, world.junctions_tested, world.junctions_untested |
| party-finances | money.reserve_gp_sp, money.total_gp_sp |

Values were transcribed from existing records without advancing the campaign. The validator declares ownership of these keys, requires every owned value, and compares it with the checkpoint. It does not hardcode today's numerical canon as permanent limits. For an actual approved scene, update the checkpoint, authoritative structured values, explanatory entity prose and changelog together. A disagreement is an error to investigate, not permission to choose or invent a replacement value.

HP, MP, maxima, defense and world counts require integers (booleans do not qualify); HP/MP must remain within positive maxima. Date/time formatting and paused status are checked. Currency uses exact integer copper: 1 gp = 100 cp, 1 sp = 10 cp. Whole gp/sp/cp components are accepted; fractional, negative, repeated or unknown units are rejected. Equivalent denominations compare equally. Personal shares plus shared reserve must equal the spendable accounting total.

The historical 38 gp 2 sp custody funds are excluded from spendable totals. Unknown current companion HP/MP remain unknown; old values are not promoted to current facts. No money, chain count, time or other campaign value changed in this maintenance.

These checks validate structured facts, metadata and declared file references. They do not infer numerical facts from arbitrary Markdown prose, prove historical claims, resolve mysteries, or decide what Theron knows. Human review must keep prose and evidence aligned. Source paths establish findability, not proof of a claim's content.

## Archive routing

Every module path in `archive/legacy-index.json` is checked, including modules not cited by an entity. Every archived module must also be indexed. Each original-document `source` basename resolves beneath `archive/`; see `archive/README.md`. Historical originals and split modules are preserved unchanged.
