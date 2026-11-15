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

## Historical checkpoint schema2 (preserved Day153)

Day153 is the first explicitly versioned checkpoint. Required keys: `schema_version` (integer2), date (`Year N Day N`), 24-hour time (`HH:MM`), location, theron, money, world, status (`PAUSED`), source (existing root-relative file), context. The prior unversioned Day46 snapshot is preserved unchanged under `archive/checkpoints/`; it is historical, not silently rewritten to schema2.

- `theron`: integer hp/hp_max, mp/mp_max, defense, level, str/dex/con/int/wis/cha and unspent_attributes; nonempty rank. Nonnegative values (positive maxima); HP/MP within maxima.
- `money`: central_gp_sp, emergency_gp_sp, reserve_gp_sp, operating_gp_sp, development_gp_sp, total_gp_sp. Exact integer-copper accounting; no floating values. Five cash accounts sum to total. Former companion personal balances are historical after voluntary consolidation; they must not be re-added.
- `world`: integer vaeltharion_chains_attached and protective_anchors_retained. Distinct counts; old junction testing is historical and is not a release/anchor count.
- `context`: safety text, companions_present IDs, party_roles keyed by IDs, projects text mapping, academy mapping, outstanding_clues list, recent_mp_costs mapping, mp_before_recent_casts integer. IDs must resolve. Recent starting MP minus summed costs must equal current MP; the Day153 starting400 is arithmetic from337+63, not evidence of an invented rest.
- Academy mapping: entity ID, latest_reported_cash_gp_sp, refundable_lease_deposit_gp_sp, balance_date note, included_in_party_total (must be false).34gp cash and15gp deposit are latest reported earlier values with unknown report date; no newly verified later balance implied. Deposit remains separate noncash. No academy amount enters party cash.

## Historical schema2 structured entity agreement

| Owner | Required checkpoint facts |
|---|---|
| theron-ashvale | date, time, location, status, every theron field |
| vaeltharion | both world counts |
| party-finances | every money field |

Owned values must match current checkpoint exactly (currency by integer copper). Other entities may not add undeclared snapshot ownership. Changing canon requires updating snapshot, structured entity values, prose and changelog together. Validator rules do not freeze specific numerical canon permanently.

Regression checks cover metadata, paths, archival coverage, account sums/separation, recent MP spending, new schema, entity agreement and the current core/new spell costs. Unknown companion numerical HP/MP, missing transaction details and chronological gaps stay unknown. Historical custody38gp2sp, merchant goods, evidence and noncash estimates remain excluded.

The validator checks declared facts and references; it does not infer truth from arbitrary prose, prove testimony, determine guilt, expose GM secrets, resolve concentration timing or interpret artwork. Human review preserves those distinctions. Source path existence establishes findability, not independent historical verification.

## Current checkpoint schema3 — Day472 END SESSION

Schema3 retains date/time/location, Theron base stats, world counts, source and context; session status is `ENDED`. Schema2 remains supported for historical snapshots and regression fixtures. The index schema remains2.

- `resources`: nonnegative integer equipped_defense/bracers_defense_bonus, staff_mp/staff_mp_max, wagon_mp/wagon_mp_max; positive maxima; pools cannot exceed maxima. Equipped DEF must equal Theron permanent base plus equipment bonus. Boolean chronos_eye_locked and dragon_slayer_locked must remain true under the supplied player ruling.
- `money`: exact-copper total_gp_sp, blackscale_private_gp_sp, expedition_gp_sp, excluded_lyanna_gp_sp, scene_opening_gp_sp, scene_recovery_gp_sp, scene_cost_gp_sp, plus nonempty allocation_status beginning `unverified`. Known controlled components cannot exceed total. Opening + recovery − cost equals total. Lyanna is excluded, never added. There is no invented residual account or requirement to balance stale allocations.
- `context.recent_mp_costs` is empty and `mp_before_recent_casts` null because individual final-release costs/starting mana are unavailable. This does not authorize free casting or future recharge: final personal MP and resource pools must agree with authoritative entity values. Other context keys retain schema2 shape; academy values explicitly remain earlier reports, not newly verified balances.
- Theron owns schema2 Theron/date/time/location/status fields plus every `resources.*` value. Party-finances owns every schema3 monetary currency field. Vaeltharion retains the two last-verified world counts; Aeloryn's restraint release does not change them.

Day153 mutation tests load the unchanged archived snapshot and saved historical entity values; separate current-checkpoint tests cover schema3 partial allocations, excluded cash, finite pools, locks, defense separation, missing mana history and entity agreement. Unknown chronology and exact spell repricing remain human-review limits, not fabricated data.

## Current checkpoint schema4 — Year848 Suncrest4 Day124

Schema4 preserves schema2/3 validation for archived checkpoints and structured owner fixtures. The current session is `PAUSED`; `date` remains `Year 848 Day 124` with `calendar.season`/`day_of_season` recording Suncrest4, without assuming a year length or inventing dates across the gap.

- Resources and Theron/world structured ownership retain schema3 rules.
- Money has `total_gp_sp`, `provisional_historic_gp_sp`, `office_petty_gp_sp`, plus nonempty `allocation_status`, `provisional_status` and `office_status`. Party-finances owns the three currency values. Total is controlled spendable only; provisional approximately9gp1sp14cp and house6gp4sp are excluded, never summed into total. Unknown transactions/account allocations remain explicit; no invented opening/cost fields to force a reconciliation. Exact copper conversion preserves the supplied unnormalized14cp denomination while the text retains its approximate status.
- `context.recent_mp_recovery` records ability, amount, uninterrupted minutes, usable ambient source and personal-only scope. Assimilation II requires24MP per complete uninterrupted10 minutes; reject partial intervals, missing source or other-pool recovery. Latest starting375 minus Mental Probe13 plus24 equals386, capped at personal maximum400. No inference about earlier unspecified expenditure logs or concentration overlap.
- `custody` records unique character IDs for current detainees/free people, guard, fatalities and party injuries. References must resolve; free people cannot simultaneously be detained. Regression checks pin this supplied snapshot to three detainees, Sella/Orenic free and zero deaths/injuries. Older custody is historical, not a current location assertion.

Validators do not infer guilt, prove same-name identities, certify recovered materials, verify arbitrary status prose, or fill missing historical events. New regression cases exercise mana recovery prerequisites/arithmetic/cap, segregated money, finite pools, custody references and current exact snapshot. Historical schema2/3 regression suites use their preserved checkpoints and structured entity values.

## Current checkpoint schema5 — Year848 Suncrest17 Day137 END SESSION

Schema5 retains schema4 money fields and structured ownership. `status` is ENDED;
calendar records Suncrest17 and checkpoint date/time are Year848 Day137,09:30.
Allocation status now records the approved reconstruction and unresolved legacy split.
`context.recent_mp_costs` is empty and `mp_before_recent_casts` null, with no
`recent_mp_recovery`: final personalMP400 is explicitly supplied, intermediate
expenditures/recoveries are unknown. The historical schema4 recovery rules still apply
to its preserved Day124 fixture; no guessed recovery or free casting is implied.

`custody` records aggregate `reviewed`, `released`, `retained`, and
`medically_transferred` nonnegative integer counts, a boolean `hearing_pending`,
plus `identities_status` and `halden_status` text. Counts must sum; no mapping to
older detainees is invented. Current supplied counts are4/2/1/1, hearing pending.

`entities/mechanics/party-finances.md` routes to **state/finance-ledger.json**, the
separate authoritative detailed financial record (ledger schema1). No duplicate
finance entity or index schema change. The ledger uses integer copper (100cp/gp,
10cp/sp), distinguishes cash ownership/accounts, category revenue and expenses,
net surplus/distribution, excluded property/assets/deposits/estimates and open
historical discrepancies. Its date, source, total and excluded amounts must agree
with the checkpoint; the finance entity's three money values remain exact owners.

Validation enforces category sums, merchant commission separation, eight-period
multiplication, net-only percentages totaling100%, one distribution, baseline
purse/legacy inclusion, account totals, neutral expense-history arithmetic, zero
internal-transfer cash effect, excluded holdings, already-paid land and unspent
estimates. The128gp historical gap stays open without a current adjustment.
No automatic future65gp award; future actual periods require Tomas receipts and
expense records or another explicit player-approved accounting ruling.

Day124 snapshot and structured owner values are preserved under archive/checkpoints/;
its tests restore those fixtures in disposable copies. Schema2/3 fixtures remain
unchanged. Day137 mutation tests exercise double-counting, exclusions, commission,
percentages, repeat expenses/distributions, estimates, locks, mana and custody.
