# Codex instructions — Shadows Over Vellorin
Read `README.md`, `governance/precedence.md`, `state/checkpoint.json`, then use `index.json` to locate **only needed entity files**.
`entities/` is current canonical reference; `archive/` is historical evidence and must not override later approved rulings.
Keep user-locked rulings, player agency, medieval fantasy, Story Mode, fair permanent death, NPC independence and findability.
Preserve GM secrets; **never treat hidden truths as Theron's knowledge**. Keep repo PRIVATE.
No invented historical travel, finances, animal identities, NPC whereabouts or outcomes. Unknowns stay unknown.
Edit on `lore/*`, `session/*` or `reconcile/*` branches; open PR with evidence. Do not merge without user approval.
When a session ends, update entity records, checkpoint, and changelog together; maintenance never advances in-game time or resources.
Run `python scripts/validate.py` before PR. For new entities, add an index entry with a unique ID and accurate `source_refs`.

Read [permanent narration rules](docs/narration-format.md) before any campaign response. Attribute every spoken line as **Speaker:** "Dialogue"; use functioning independently closed collapsible controls for detailed bookkeeping. END SESSION produces checkpoint and [next-chat handoff](state/next-chat-handoff.md), never further play. Day472 source supersedes older snapshots; preserve unverified gaps.
