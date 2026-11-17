# END SESSION Codex template

Copy this instruction and empty structure only after actual play. This document is a template, not a session record or second checkpoint. UNKNOWN stays null with a source/gap explanation; do not populate figures from memory or invent an opening/transaction to balance cash. No secret answer, concealed identity/location/mechanism, private intention or undiscovered outcome goes into a public PR.

```text
Repository: Taifinkaba/shadows-over-vellorin
END SESSION: Stop advancing the story now. Produce the final handoff from played or explicitly approved outcomes only; no further scene, travel, spell, task or event.

1. Read AGENTS.md, README.md, governance/precedence.md, docs/narration-format.md and the latest approved state/checkpoint.json; use index.json for only relevant owners.
2. Read affected actor, quest, inventory, custody, finance and project owners; follow targeted sources where provenance is missing.
3. Apply only played or explicitly approved outcomes with dated evidence and discovery boundaries. Preserve historical unknowns, protected victories, identity separation, finite pools and third-party ownership.
4. Update only affected entity IDs; agree with checkpoint projections. No broad rewrite of unrelated entities.
5. Update supported checkpoint fields together with affected owners; preserve unknown last decision/dates/conditions rather than fabricate them.
6. Update state/finance-ledger.json only for actual affected money, once per event. Distinguish internal transfers, commitments, received income, paid costs and excluded/noncash property.
7. Update single custody and inventory owners only for supported actual handovers/acquisitions/consumption; preserve receipts, lawful authority, evidence and possessions.
8. Add a new dated chronicle with source/qualification. Keep existing historical chronicles unchanged.
9. Update state/next-chat-handoff.md from actual ending facts; retain independent assignments and UNKNOWN remote outcomes.
10. Update state/open-verifications.md for supported resolutions/new gaps, preserving history. No Day181 adoption without separate reconciliation authorization.
11. Update changes/CHANGELOG.md; index only if needed for genuine new approved entities.
12. Run python scripts/validate.py; python -m unittest discover -s tests -v; python -O scripts/validate.py; git diff --check. Report baseline/new failures separately and derive entity totals from index.
13. Inspect unrelated diffs and preservation boundaries. List explicitly unchanged systems. Never publish hidden answers or private knowledge distinctions.
14. Open a session/* branch and session PR with source evidence and validation; this is future-session instruction, not authorization to create a session PR during infrastructure work.
15. Wait for explicit player approval to merge. Do not continue the story after END SESSION.
```

Fill the following fields only from actual sources when later using this template. Provide source references and verified-as-of alongside each filled group; a source must establish that claim rather than merely exist. Current companion maxima are not current pools, approvals are not payments, and pending reviews are not convictions. Refer to [manual](game-master-operating-manual.md) and [world status](world-status.md).

```json
{
  "schema_version": 1,
  "template_only": true,
  "stop_story": true,
  "merge_requires_approval": true,
  "apply_only_supported_outcomes": true,
  "handoff": {
    "session_identification": {
      "date": null,
      "time": null,
      "location": null,
      "session_status": null,
      "last_scene": null,
      "last_player_decision": null
    },
    "character_resources": {
      "hp": null,
      "mp": null,
      "defense_base": null,
      "defense_equipped": null,
      "conditional_defense": null,
      "equipped_items": null,
      "staff_resources": null,
      "wagon_resources": null,
      "conditions": null,
      "skill_progress": null
    },
    "companions": {
      "present": null,
      "elsewhere": null,
      "assignments": null,
      "safety": null,
      "last_verified_updates": null
    },
    "finances": {
      "opening_balance": null,
      "verified_income": null,
      "verified_spending": null,
      "internal_transfers": null,
      "closing_balance": null,
      "committed_funds": null,
      "excluded_holdings": null,
      "unresolved_discrepancies": null
    },
    "inventory": {
      "new_acquisitions": null,
      "consumed_items": null,
      "transfers": null,
      "protected_evidence": null,
      "provisional_salvage": null
    },
    "world_changes": {
      "quests": null,
      "factions": null,
      "relationships": null,
      "custody": null,
      "dungeon_states": null,
      "property": null,
      "construction": null,
      "research": null,
      "legal_outcomes": null
    },
    "open_issues": {
      "mysteries": null,
      "pending_responses": null,
      "deferred_work": null,
      "historical_discrepancies": null,
      "approval_requirements": null
    },
    "codex_instructions": {
      "affected_entity_ids": null,
      "affected_files": null,
      "source_evidence": null,
      "checkpoint_changes": null,
      "required_validation": null,
      "explicitly_unchanged_systems": null,
      "discovery_boundaries": null
    }
  },
  "source_refs": [],
  "verified_as_of": null
}
```
