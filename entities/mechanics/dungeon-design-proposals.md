---
id: dungeon-design-proposals
type: mechanics
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/dungeon-exploration-registry-design.md
---

# Future dungeon design approval crosswalk

Five design candidates only; none is an active site entity, placed entrance, visited location, generated encounter or loot cache. Counts are planning material, not a world census. Locations/inhabitants/treasure/history stay unknown/uninstantiated. Preserve raw SS label as a conflict with the separately proposed F–S+ scale; do not normalize it or silently extend that scale. Approving a concept never invents a previous expedition or identifies it with an old site.

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "world_census_count": null,
  "proposed_threat_scale": [
    "F",
    "E",
    "D",
    "C",
    "B",
    "A",
    "S",
    "S+"
  ],
  "proposals": [
    {
      "proposal_id": "dungeon-proposal:hollowstone-mine",
      "name": "Hollowstone Mine",
      "classification": "PROPOSED",
      "proposed_threat_label": "D",
      "scale_compatibility": "PROPOSED SCALE LABEL ONLY",
      "candidate_location_id": null,
      "existing_site_id": null,
      "current_inhabitants": null,
      "treasure": null,
      "exploration_history": [],
      "collision_review_site_ids": [
        "site:hollow-first-hour",
        "site:hollow-veil",
        "site:whisperstone-hollow"
      ],
      "collision_note": "Shared name fragment/function is not identity or connection. Pale naming is not a link to Pale Devourer. No current rooms, population or wealth proposed.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/dungeon-exploration-registry-design.md"
      ]
    },
    {
      "proposal_id": "dungeon-proposal:ashen-anvil",
      "name": "Ashen Anvil",
      "classification": "PROPOSED",
      "proposed_threat_label": "B",
      "scale_compatibility": "PROPOSED SCALE LABEL ONLY",
      "candidate_location_id": null,
      "existing_site_id": null,
      "current_inhabitants": null,
      "treasure": null,
      "exploration_history": [],
      "collision_review_site_ids": [
        "site:old-copperworks"
      ],
      "collision_note": "Shared name fragment/function is not identity or connection. Pale naming is not a link to Pale Devourer. No current rooms, population or wealth proposed.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/dungeon-exploration-registry-design.md"
      ]
    },
    {
      "proposal_id": "dungeon-proposal:drowned-archive",
      "name": "Drowned Archive",
      "classification": "PROPOSED",
      "proposed_threat_label": "A",
      "scale_compatibility": "PROPOSED SCALE LABEL ONLY",
      "candidate_location_id": null,
      "existing_site_id": null,
      "current_inhabitants": null,
      "treasure": null,
      "exploration_history": [],
      "collision_review_site_ids": [
        "site:northern-depository",
        "site:seven-bells-receiving-chambers"
      ],
      "collision_note": "Shared name fragment/function is not identity or connection. Pale naming is not a link to Pale Devourer. No current rooms, population or wealth proposed.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/dungeon-exploration-registry-design.md"
      ]
    },
    {
      "proposal_id": "dungeon-proposal:pale-reliquary",
      "name": "Pale Reliquary",
      "classification": "PROPOSED",
      "proposed_threat_label": "S",
      "scale_compatibility": "PROPOSED SCALE LABEL ONLY",
      "candidate_location_id": null,
      "existing_site_id": null,
      "current_inhabitants": null,
      "treasure": null,
      "exploration_history": [],
      "collision_review_site_ids": [],
      "collision_note": "Shared name fragment/function is not identity or connection. Pale naming is not a link to Pale Devourer. No current rooms, population or wealth proposed.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/dungeon-exploration-registry-design.md"
      ]
    },
    {
      "proposal_id": "dungeon-proposal:shattered-meridian",
      "name": "Shattered Meridian",
      "classification": "PROPOSED",
      "proposed_threat_label": "SS",
      "scale_compatibility": "CONFLICT / REQUIRES APPROVAL",
      "candidate_location_id": null,
      "existing_site_id": null,
      "current_inhabitants": null,
      "treasure": null,
      "exploration_history": [],
      "collision_review_site_ids": [],
      "collision_note": "Shared name fragment/function is not identity or connection. Pale naming is not a link to Pale Devourer. No current rooms, population or wealth proposed.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/dungeon-exploration-registry-design.md"
      ]
    }
  ],
  "automatic_instantiation": false
}
```
