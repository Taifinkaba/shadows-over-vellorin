---
id: exploration-sections
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/dungeon-exploration-registry-design.md
- entities/mechanics/shady-salvage.md
- entities/locations/north-return-house.md
---

# Section identity and source-state routing

Stable section IDs identify existing recorded areas, not invented corridors/floors/secrets/boss rooms. A whole-site row uses a scoped “recorded-area” handle and does not assert the site consists of one room. State_ref points to the original row/inspection; it never stores an editable competing status. Contents, recoveries, restrictions and objectives remain with linked owners. Protected quarters imply protected access, not unexplored/sealed/cleared. A visited site is not fully explored.

```json
{
  "schema_version": 1,
  "allowed_exploration_statuses": [
    "unknown",
    "unexplored",
    "partially-explored",
    "visited",
    "explored",
    "cleared",
    "sealed",
    "inaccessible",
    "destroyed"
  ],
  "sections": [
    {
      "section_id": "section:hollow-first-hour:supply-annex",
      "site_id": "site:hollow-first-hour",
      "name": "Hollow supply annex",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Hollow supply annex"
      },
      "contents_owner_refs": [
        "shady-salvage",
        "launder"
      ],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [
        "shady-salvage",
        "launder"
      ],
      "remaining_objective_owner_refs": [
        "first-hour-restoration",
        "open-quests"
      ],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:hollow-first-hour:western-gallery",
      "site_id": "site:hollow-first-hour",
      "name": "Hollow western gallery",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Hollow western gallery"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [
        "first-hour-restoration",
        "open-quests"
      ],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:hollow-first-hour:keeper-quarters",
      "site_id": "site:hollow-first-hour",
      "name": "Hollow Keeper quarters",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Hollow Keeper quarters"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [
        "first-hour-restoration",
        "open-quests"
      ],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:abbey-bellkeeper-residence:recorded-area",
      "site_id": "site:abbey-bellkeeper-residence",
      "name": "Abbey bellkeeper residence",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Abbey bellkeeper residence"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:nine-star-shrine:accessible-rooms",
      "site_id": "site:nine-star-shrine",
      "name": "Nine-Star Shrine accessible rooms",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Nine-Star Shrine accessible rooms"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:vaelspire-observatory:lower-rooms",
      "site_id": "site:vaelspire-observatory",
      "name": "Vaelspire observatory lower rooms",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Vaelspire observatory lower rooms"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:seven-bells-lower-foundations:recorded-area",
      "site_id": "site:seven-bells-lower-foundations",
      "name": "Seven Bells lower foundations",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Seven Bells lower foundations"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:northwatch-old-aqueduct:recorded-area",
      "site_id": "site:northwatch-old-aqueduct",
      "name": "Northwatch old aqueduct",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Northwatch old aqueduct"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:western-roadside-fortress:recorded-area",
      "site_id": "site:western-roadside-fortress",
      "name": "Western roadside fortress",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Western roadside fortress"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:whisperstone-hollow:recorded-area",
      "site_id": "site:whisperstone-hollow",
      "name": "Whisperstone Hollow",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Whisperstone Hollow"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:frostglass-western-ridge:recorded-area",
      "site_id": "site:frostglass-western-ridge",
      "name": "Frostglass western ridge",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Frostglass western ridge"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:old-copperworks:recorded-area",
      "site_id": "site:old-copperworks",
      "name": "Old Copperworks",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Old Copperworks"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:ravencrest-waystation:recorded-area",
      "site_id": "site:ravencrest-waystation",
      "name": "Ravencrest waystation",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/mechanics/shady-salvage.md",
        "locator_kind": "table-row",
        "locator": "Ravencrest waystation"
      },
      "contents_owner_refs": [],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [],
      "remaining_objective_owner_refs": [],
      "last_verified_state_ref": "entities/mechanics/shady-salvage.md",
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "note": "Source label identifies only the recorded area, not a generated room plan. Status is read from owner; searched/visited/protected never implies cleared. No copied inventory."
    },
    {
      "section_id": "section:north-return-house:cellar",
      "site_id": "site:north-return-house",
      "name": "Recorded cellar inspection",
      "classification": "CONFIRMED CANON",
      "state_ref": {
        "source_ref": "entities/locations/north-return-house.md",
        "locator_kind": "inspection-phrase",
        "locator": "No additional prisoners found in inspected cellar."
      },
      "contents_owner_refs": [
        "seven-bells-inventory"
      ],
      "access_ref": null,
      "hazard_reference_ids": [],
      "encounter_history_refs": [],
      "recovered_inventory_owner_refs": [
        "seven-bells-inventory"
      ],
      "remaining_objective_owner_refs": [
        "seven-bells-investigation"
      ],
      "last_verified_state_ref": "entities/locations/north-return-house.md",
      "source_refs": [
        "entities/locations/north-return-house.md"
      ],
      "note": "Inspection observed; no whole-room or site clearance inferred. Exact findings remain in original owner, not copied here."
    }
  ],
  "new_exploration_events": []
}
```
