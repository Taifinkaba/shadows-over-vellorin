---
id: dungeon-ecology-and-hazards
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/dungeon-exploration-registry-design.md
- entities/mechanics/outstanding-projects.md
- entities/mechanics/seven-bells-inventory.md
- entities/creatures/vaeltharion.md
- entities/creatures/aeloryn.md
---

# Ecology and hazard reference boundaries

This is a source-pointer framework, not a new bestiary, population, current-location tracker or trap inventory. Creature entities retain species/abilities/outcomes. Historical guardian context does not turn independent beings into hostile dungeon residents. Pale Devourer containment and the Winter Warden visit remain in outstanding-projects without adding an entity, rank or map. Named-reference classification does not assert either name is a newly instantiated species/group.

Hazard pointers refer to existing physical records, not additional objects. Installed, removed, isolated, dangerous and safely disabled are different states; neither removal nor temporary isolation certifies safety. Full effects, triggers, weaknesses and solutions are not copied into this public framework. No retroactive room trap, respawn or encounter is added.

```json
{
  "schema_version": 1,
  "ecology_references": [
    {
      "reference_id": "ecology:vaeltharion",
      "name": "Vaeltharion",
      "creature_entity_id": "vaeltharion",
      "reference_kind": "existing-creature-context",
      "historical_site_ids": [
        "site:hollow-veil"
      ],
      "current_location_id": null,
      "population_count": null,
      "threat_rank": null,
      "behavior_ref": "entities/creatures/vaeltharion.md",
      "species_ref": "entities/creatures/vaeltharion.md",
      "territory": null,
      "diet": null,
      "group_structure": null,
      "intelligence_ref": null,
      "hostility": null,
      "special_abilities_owner_ref": "vaeltharion",
      "weaknesses": null,
      "last_verified_status_ref": "entities/creatures/vaeltharion.md",
      "encounter_history_refs": [],
      "source_refs": [
        "entities/creatures/vaeltharion.md"
      ],
      "note": "Historical context only, not current habitation, hostility, defeat, revival or a population. For named references species/abilities/whereabouts remain UNKNOWN; original source decides status."
    },
    {
      "reference_id": "ecology:aeloryn",
      "name": "Aeloryn",
      "creature_entity_id": "aeloryn",
      "reference_kind": "existing-creature-context",
      "historical_site_ids": [
        "site:hollow-first-hour"
      ],
      "current_location_id": null,
      "population_count": null,
      "threat_rank": null,
      "behavior_ref": "entities/creatures/aeloryn.md",
      "species_ref": "entities/creatures/aeloryn.md",
      "territory": null,
      "diet": null,
      "group_structure": null,
      "intelligence_ref": null,
      "hostility": null,
      "special_abilities_owner_ref": "aeloryn",
      "weaknesses": null,
      "last_verified_status_ref": "entities/creatures/aeloryn.md",
      "encounter_history_refs": [],
      "source_refs": [
        "entities/creatures/aeloryn.md"
      ],
      "note": "Historical context only, not current habitation, hostility, defeat, revival or a population. For named references species/abilities/whereabouts remain UNKNOWN; original source decides status."
    },
    {
      "reference_id": "ecology:pale-devourer",
      "name": "Pale Devourer",
      "creature_entity_id": null,
      "reference_kind": "named-reference-unclassified",
      "historical_site_ids": [],
      "current_location_id": null,
      "population_count": null,
      "threat_rank": null,
      "behavior_ref": null,
      "species_ref": null,
      "territory": null,
      "diet": null,
      "group_structure": null,
      "intelligence_ref": null,
      "hostility": null,
      "special_abilities_owner_ref": null,
      "weaknesses": null,
      "last_verified_status_ref": "entities/mechanics/outstanding-projects.md",
      "encounter_history_refs": [],
      "source_refs": [
        "entities/mechanics/outstanding-projects.md"
      ],
      "note": "Historical context only, not current habitation, hostility, defeat, revival or a population. For named references species/abilities/whereabouts remain UNKNOWN; original source decides status."
    },
    {
      "reference_id": "ecology:winter-warden",
      "name": "Winter Warden",
      "creature_entity_id": null,
      "reference_kind": "named-reference-unclassified",
      "historical_site_ids": [],
      "current_location_id": null,
      "population_count": null,
      "threat_rank": null,
      "behavior_ref": null,
      "species_ref": null,
      "territory": null,
      "diet": null,
      "group_structure": null,
      "intelligence_ref": null,
      "hostility": null,
      "special_abilities_owner_ref": null,
      "weaknesses": null,
      "last_verified_status_ref": "entities/mechanics/outstanding-projects.md",
      "encounter_history_refs": [],
      "source_refs": [
        "entities/mechanics/outstanding-projects.md"
      ],
      "note": "Historical context only, not current habitation, hostility, defeat, revival or a population. For named references species/abilities/whereabouts remain UNKNOWN; original source decides status."
    }
  ],
  "hazard_references": [
    {
      "hazard_id": "hazard:er7",
      "name": "E-R-7 fitting reference",
      "location_site_id": null,
      "section_id": null,
      "trigger": null,
      "detectability": null,
      "effect": null,
      "disarm_or_avoidance": null,
      "state_ref": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "locator_kind": "table-row",
        "locator": "E-R-7 fractured-seat fitting"
      },
      "source_refs": [
        "entities/mechanics/seven-bells-inventory.md"
      ],
      "new_trigger_events": [],
      "note": "Reference to existing inventory/evidence owner only. Installed versus removed/isolated state stays in source; no new trap placement, activation, disarm method or safety certification."
    },
    {
      "hazard_id": "hazard:viir",
      "name": "Removed VII/R fitting reference",
      "location_site_id": null,
      "section_id": null,
      "trigger": null,
      "detectability": null,
      "effect": null,
      "disarm_or_avoidance": null,
      "state_ref": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "locator_kind": "table-row",
        "locator": "Removed hostile fitting `VII / R`"
      },
      "source_refs": [
        "entities/mechanics/seven-bells-inventory.md"
      ],
      "new_trigger_events": [],
      "note": "Reference to existing inventory/evidence owner only. Installed versus removed/isolated state stays in source; no new trap placement, activation, disarm method or safety certification."
    },
    {
      "hazard_id": "hazard:command-plate",
      "name": "Removed command plate reference",
      "location_site_id": null,
      "section_id": null,
      "trigger": null,
      "detectability": null,
      "effect": null,
      "disarm_or_avoidance": null,
      "state_ref": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "locator_kind": "table-row",
        "locator": "Black-metal counterfeit command plate"
      },
      "source_refs": [
        "entities/mechanics/seven-bells-inventory.md"
      ],
      "new_trigger_events": [],
      "note": "Reference to existing inventory/evidence owner only. Installed versus removed/isolated state stays in source; no new trap placement, activation, disarm method or safety certification."
    },
    {
      "hazard_id": "hazard:isolated-sliver",
      "name": "Isolated contaminated material reference",
      "location_site_id": null,
      "section_id": null,
      "trigger": null,
      "detectability": null,
      "effect": null,
      "disarm_or_avoidance": null,
      "state_ref": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "locator_kind": "source-phrase",
        "locator": "Contaminated violet sliver stays isolated."
      },
      "source_refs": [
        "entities/mechanics/seven-bells-inventory.md"
      ],
      "new_trigger_events": [],
      "note": "Reference to existing inventory/evidence owner only. Installed versus removed/isolated state stays in source; no new trap placement, activation, disarm method or safety certification."
    }
  ],
  "new_encounter_events": [],
  "new_population_events": [],
  "automatic_respawn": false,
  "automatic_scaling": false
}
```
