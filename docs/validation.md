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

## Checkpoint schema2

Day153 is the first explicitly versioned checkpoint. Required keys: `schema_version` (integer2), date (`Year N Day N`), 24-hour time (`HH:MM`), location, theron, money, world, status (`PAUSED`), source (existing root-relative file), context. The prior unversioned Day46 snapshot is preserved unchanged under `archive/checkpoints/`; it is historical, not silently rewritten to schema2.

- `theron`: integer hp/hp_max, mp/mp_max, defense, level, str/dex/con/int/wis/cha and unspent_attributes; nonempty rank. Nonnegative values (positive maxima); HP/MP within maxima.
- `money`: central_gp_sp, emergency_gp_sp, reserve_gp_sp, operating_gp_sp, development_gp_sp, total_gp_sp. Exact integer-copper accounting; no floating values. Five cash accounts sum to total. Former companion personal balances are historical after voluntary consolidation; they must not be re-added.
- `world`: integer vaeltharion_chains_attached and protective_anchors_retained. Distinct counts; old junction testing is historical and is not a release/anchor count.
- `context`: safety text, companions_present IDs, party_roles keyed by IDs, projects text mapping, academy mapping, outstanding_clues list, recent_mp_costs mapping, mp_before_recent_casts integer. IDs must resolve. Recent starting MP minus summed costs must equal current MP; the Day153 starting400 is arithmetic from337+63, not evidence of an invented rest.
- Academy mapping: entity ID, latest_reported_cash_gp_sp, refundable_lease_deposit_gp_sp, balance_date note, included_in_party_total (must be false).34gp cash and15gp deposit are latest reported earlier values with unknown report date; no newly verified later balance implied. Deposit remains separate noncash. No academy amount enters party cash.

## Structured entity agreement

| Owner | Required checkpoint facts |
|---|---|
| theron-ashvale | date, time, location, status, every theron field |
| vaeltharion | both world counts |
| party-finances | every money field |

Owned values must match current checkpoint exactly (currency by integer copper). Other entities may not add undeclared snapshot ownership. Changing canon requires updating snapshot, structured entity values, prose and changelog together. Validator rules do not freeze specific numerical canon permanently.

Regression checks cover metadata, paths, archival coverage, account sums/separation, recent MP spending, new schema, entity agreement and the current core/new spell costs. Unknown companion numerical HP/MP, missing transaction details and chronological gaps stay unknown. Historical custody38gp2sp, merchant goods, evidence and noncash estimates remain excluded.

The validator checks declared facts and references; it does not infer truth from arbitrary prose, prove testimony, determine guilt, expose GM secrets, resolve concentration timing or interpret artwork. Human review preserves those distinctions. Source path existence establishes findability, not independent historical verification.
