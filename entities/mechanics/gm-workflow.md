---
id: gm-workflow
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/gm-continuity-maintenance.md
- state/checkpoint.json
- state/finance-ledger.json
- docs/narration-format.md
- docs/geography-and-travel.md
- docs/settlement-directory.md
- docs/justice-and-custody-directory.md
- docs/guild-and-contract-directory.md
- docs/dungeon-and-exploration-directory.md
- docs/property-and-economy-directory.md
- docs/npc-autonomy-and-world-events.md
- docs/faction-activity-directory.md
- docs/main-quest-directory.md
- docs/game-master-operating-manual.md
- docs/world-status.md
- docs/end-session-codex-template.md
- docs/next-session-chat-template.md
- entities/rules/story-mode.md
- entities/rules/knowledge-boundaries.md
- entities/mechanics/theron-abilities.md
- entities/mechanics/theron-skills.md
- entities/mechanics/theron-spells.md
- entities/mechanics/travel-routes.md
- entities/mechanics/settlement-services.md
- entities/rules/justice-and-jurisdiction.md
- entities/mechanics/prisoner-custody.md
- entities/mechanics/guild-network.md
- entities/mechanics/contract-registry.md
- entities/mechanics/dungeon-registry.md
- entities/mechanics/exploration-sections.md
- entities/mechanics/party-finances.md
- entities/mechanics/property-financial-references.md
- entities/mechanics/independent-assignments.md
- entities/mechanics/faction-activity.md
- entities/mechanics/world-event-references.md
- entities/mechanics/main-quest-map.md
- entities/mechanics/quest-history-and-identities.md
- entities/mechanics/quest-resolution-proposals.md
- entities/mechanics/quest-answer-blueprint.md
---

# GM workflow and continuity routing

Procedure/source routing only; no checkpoint values, evolving world cache, financial balance or session outcome. Read the operating manual and current owners. Framework canon never approves proposed institutions, routes, clocks, secret answers or ending design. Dashboard output is ephemeral, source-qualified and limited to reviewed fields; it grants no character knowledge. END SESSION templates are empty instructions, not a new session.

```json
{
  "schema_version": 1,
  "directory_refs": [
    "docs/geography-and-travel.md",
    "docs/settlement-directory.md",
    "docs/justice-and-custody-directory.md",
    "docs/guild-and-contract-directory.md",
    "docs/dungeon-and-exploration-directory.md",
    "docs/property-and-economy-directory.md",
    "docs/npc-autonomy-and-world-events.md",
    "docs/faction-activity-directory.md",
    "docs/main-quest-directory.md"
  ],
  "document_refs": [
    "docs/game-master-operating-manual.md",
    "docs/world-status.md",
    "docs/end-session-codex-template.md",
    "docs/next-session-chat-template.md"
  ],
  "authority_refs": [
    "story-mode",
    "knowledge-boundaries",
    "theron-abilities",
    "theron-skills",
    "theron-spells",
    "travel-routes",
    "settlement-services",
    "justice-and-jurisdiction",
    "prisoner-custody",
    "guild-network",
    "contract-registry",
    "dungeon-registry",
    "exploration-sections",
    "party-finances",
    "property-financial-references",
    "independent-assignments",
    "faction-activity",
    "world-event-references",
    "main-quest-map",
    "quest-history-and-identities",
    "quest-resolution-proposals",
    "quest-answer-blueprint"
  ],
  "retrieval_scenarios": {
    "opening-scene": [
      "checkpoint",
      "location-owner",
      "present-actors"
    ],
    "combat": [
      "participants",
      "theron-abilities",
      "theron-spells",
      "equipment-owner"
    ],
    "travel": [
      "travel-routes",
      "route-owners",
      "destination-owner"
    ],
    "shopping": [
      "settlement-services",
      "business-parent",
      "party-finances"
    ],
    "bounty": [
      "contract-registry",
      "justice-and-jurisdiction",
      "prisoner-custody"
    ],
    "dungeon": [
      "dungeon-registry",
      "section-owner",
      "creature-owner",
      "inventory-owner"
    ],
    "estate": [
      "tomas",
      "ashvale-estate",
      "finance-ledger"
    ],
    "academy": [
      "master-beren",
      "dragon-slayer-academy",
      "independent-assignments"
    ],
    "main-quest": [
      "active-quest-owner",
      "evidence-owner",
      "discovery-source"
    ],
    "end-session": [
      "changed-owners",
      "checkpoint",
      "finance-ledger",
      "chronicle"
    ]
  },
  "dashboard_policy": "REVIEWED FIELDS ONLY",
  "checkpoint_ref": "state/checkpoint.json",
  "finance_ref": "state/finance-ledger.json",
  "new_session_events": [],
  "new_resource_postings": [],
  "new_knowledge_disclosures": [],
  "automatic_writes": false
}
```
