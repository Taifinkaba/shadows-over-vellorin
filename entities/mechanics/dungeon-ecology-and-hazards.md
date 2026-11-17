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
- changes/chronicles/phase2-05-dungeon-approval.md
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
  "automatic_scaling": false,
  "approved_reference_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
    "final_combat_integration_phase": "PR8",
    "monster_references": [
      {
        "id": "monster-reference:giant-cave-spider",
        "name": "Giant Cave Spider",
        "classification": "PROPOSED",
        "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
        "hp": 24,
        "mp": 0,
        "defense": 12,
        "reference_rank": "D",
        "compatibility": "Finite nonnegative HP/MP/DEF reference fields fit existing resource concepts; attacks, balance, movement, saves, resistances and costs remain unverified. No established creature is overwritten.",
        "combat_usable": false,
        "attack_bonus": null,
        "damage_formula": null,
        "movement": null,
        "resistances": null,
        "current_instance_count": null,
        "ecological_constraints": "Predator needs viable prey, water and a suitable nest. Territorial/nest defense, avoidance and retreat are possibilities, not compulsory attacks."
      },
      {
        "id": "monster-reference:fungal-burrower",
        "name": "Fungal Burrower",
        "classification": "PROPOSED",
        "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
        "hp": 36,
        "mp": 0,
        "defense": 14,
        "reference_rank": "D",
        "compatibility": "Finite nonnegative HP/MP/DEF reference fields fit existing resource concepts; attacks, balance, movement, saves, resistances and costs remain unverified. No established creature is overwritten.",
        "combat_usable": false,
        "attack_bonus": null,
        "damage_formula": null,
        "movement": null,
        "resistances": null,
        "current_instance_count": null,
        "ecological_constraints": "Burrowing herbivore/detritivore design needs moisture, food and viable ground; it may avoid light or stronger threats without any numeric weakness granted."
      },
      {
        "id": "monster-reference:ash-sentinel",
        "name": "Ash Sentinel",
        "classification": "PROPOSED",
        "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
        "hp": 85,
        "mp": 40,
        "defense": 20,
        "reference_rank": "B",
        "compatibility": "Finite nonnegative HP/MP/DEF reference fields fit existing resource concepts; attacks, balance, movement, saves, resistances and costs remain unverified. No established creature is overwritten.",
        "combat_usable": false,
        "attack_bonus": null,
        "damage_formula": null,
        "movement": null,
        "resistances": null,
        "current_instance_count": null,
        "ecological_constraints": "Forge-protection construct design needs a verified finite stored charge or maintained source; lack of support would limit activity. No current source or working forge is established."
      },
      {
        "id": "monster-reference:waterbound-guardian",
        "name": "Waterbound Guardian",
        "classification": "PROPOSED",
        "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
        "hp": 110,
        "mp": 80,
        "defense": 23,
        "reference_rank": "A",
        "compatibility": "Finite nonnegative HP/MP/DEF reference fields fit existing resource concepts; attacks, balance, movement, saves, resistances and costs remain unverified. No established creature is overwritten.",
        "combat_usable": false,
        "attack_bonus": null,
        "damage_formula": null,
        "movement": null,
        "resistances": null,
        "current_instance_count": null,
        "ecological_constraints": "Archive-protection guardian design needs a lawful original mandate and finite supported energy, not unlimited ambient mana or a current hostile identity."
      },
      {
        "id": "monster-reference:ancient-reliquary-warden",
        "name": "Ancient Reliquary Warden",
        "classification": "PROPOSED",
        "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
        "hp": 190,
        "mp": 160,
        "defense": 30,
        "reference_rank": "S",
        "compatibility": "Finite nonnegative HP/MP/DEF reference fields fit existing resource concepts; attacks, balance, movement, saves, resistances and costs remain unverified. No established creature is overwritten.",
        "combat_usable": false,
        "attack_bonus": null,
        "damage_formula": null,
        "movement": null,
        "resistances": null,
        "current_instance_count": null,
        "ecological_constraints": "Ceremonial-custody guardian design requires a supported finite energy/mandate model, proportionate behavior and possible dialogue/withdrawal; no current warden is instantiated."
      }
    ],
    "hazard_references": [
      {
        "id": "hazard-design:cave-in",
        "classification": "APPROVED DESIGN",
        "trigger": "Loose supports, vibration or weakened rock may fail.",
        "observable_warnings": "Fresh dust, creaking timber, displaced stone or visible cracks.",
        "exposure": "Occupying or loading an unstable area after local observation.",
        "possible_consequences": "Possible obstruction, falling debris or separation; actual effects require declared stakes and play.",
        "avoidance_or_mitigation": "Avoid unsafe spans, unload/reassess and seek qualified structural help; no guaranteed shoring recipe.",
        "required_resources": "Light, appropriate equipment, time and trained willing help.",
        "failure_conditions": "Continued movement or failed assessment may leave no safe onward path.",
        "recovery_limitations": "Do not assume a collapse reversible or anyone unharmed; rescue needs actual access and resources.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:flooding",
        "classification": "APPROVED DESIGN",
        "trigger": "Changing inflow, blocked drainage or failure of a water barrier.",
        "observable_warnings": "Rising marks, stronger flow, damp debris or audible water.",
        "exposure": "Entering a wet reach without confirmed water/escape conditions.",
        "possible_consequences": "Possible loss of footing, trapped routes, damaged records or drowning risk.",
        "avoidance_or_mitigation": "Observe levels, verify exit/air and choose safe delay or withdrawal; no free underwater travel.",
        "required_resources": "Appropriate lines, lighting, breathing/rescue capability where actually available.",
        "failure_conditions": "Rapid flow, lost visibility or blocked exits may defeat a planned approach.",
        "recovery_limitations": "No automatic drainage, restored supplies, dry records or recovered victim.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:toxic-spores",
        "classification": "APPROVED DESIGN",
        "trigger": "Disturbing a potentially harmful fungal patch in suitable conditions.",
        "observable_warnings": "Visible growth/dust, musty air or observed irritation; not automatic diagnosis.",
        "exposure": "Actual inhalation/contact in a verified affected space.",
        "possible_consequences": "Possible illness, obscured vision or lost work time, with effects declared in play.",
        "avoidance_or_mitigation": "Limit disturbance, avoid exposure and seek competent identification/care.",
        "required_resources": "Verified protective equipment, clean air, competent medical support and time.",
        "failure_conditions": "Protection may be unsuitable or exposure uncertain; do not guarantee immunity.",
        "recovery_limitations": "No automatic cure, diagnosis or restoration; existing healing rules apply.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:extreme-heat",
        "classification": "APPROVED DESIGN",
        "trigger": "Entering a hot zone or approaching stored heat.",
        "observable_warnings": "Radiant warmth, hot surfaces, distorted air or observed heat damage.",
        "exposure": "Time spent near actual heat without adequate protection/retreat.",
        "possible_consequences": "Possible injury, fatigue or damaged equipment; no fixed automatic damage.",
        "avoidance_or_mitigation": "Assess from safe distance and withdraw when limits are unknown.",
        "required_resources": "Water, safe protective gear, rest and a verified cooler route.",
        "failure_conditions": "Cooling/gear may be insufficient and retreat conditions may deteriorate.",
        "recovery_limitations": "No instant cooling, free healing or unlimited tolerated exposure.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:smoke",
        "classification": "APPROVED DESIGN",
        "trigger": "Combustion residue or disturbed ash in poorly ventilated spaces.",
        "observable_warnings": "Haze, odor, coughing or impaired visibility.",
        "exposure": "Inhaling or navigating actual contaminated air.",
        "possible_consequences": "Possible breathing/visibility problems and separation.",
        "avoidance_or_mitigation": "Avoid smoky areas and verify fresh-air escape before committing.",
        "required_resources": "Suitable protection, lighting/communication, air assessment and rescue support.",
        "failure_conditions": "Unverified ventilation or lost route marks can make entry untenable.",
        "recovery_limitations": "No assumption smoke clears on a timer or that magical treatment is free.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:unstable-bridge",
        "classification": "APPROVED DESIGN",
        "trigger": "Weight, motion or wear exceeds a damaged crossing’s condition.",
        "observable_warnings": "Missing supports, movement, frayed lines or visible gaps.",
        "exposure": "Committing persons or loads to an unverified crossing.",
        "possible_consequences": "Possible fall, isolation or loss of cargo; exact outcome requires play.",
        "avoidance_or_mitigation": "Inspect, reduce unsafe commitment, use another verified path or retreat.",
        "required_resources": "Appropriate lines, anchors only if verified, skilled help and time.",
        "failure_conditions": "No sound anchors, unsuitable gear or unexpected movement can block crossing.",
        "recovery_limitations": "No automatic repair, recovered cargo or safe fall.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:collapsing-floor",
        "classification": "APPROVED DESIGN",
        "trigger": "A weakened surface is loaded or disturbed.",
        "observable_warnings": "Sagging, cracks, washed mortar or fallen debris.",
        "exposure": "Stepping onto an actually unstable span.",
        "possible_consequences": "Possible fall or blocked passage, not automatic HP loss.",
        "avoidance_or_mitigation": "Observe surfaces, avoid questionable loads and choose verified stable ground.",
        "required_resources": "Light, careful assessment, suitable equipment and rescue capacity.",
        "failure_conditions": "Damage may be hidden or an alternate span unsafe.",
        "recovery_limitations": "No floor resets or automatic rescue after collapse.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:low-oxygen",
        "classification": "APPROVED DESIGN",
        "trigger": "Entering a confined area with exhausted or displaced breathable air.",
        "observable_warnings": "Poor flame behavior or observed distress is a warning, not a precise air test.",
        "exposure": "Actual occupancy with insufficient air; pockets are never assumed safe.",
        "possible_consequences": "Possible impaired judgment or serious injury, determined only during play.",
        "avoidance_or_mitigation": "Avoid unverified air and maintain a verified fresh-air return plan.",
        "required_resources": "Appropriate demonstrated breathing/assessment capability, time and rescue resources.",
        "failure_conditions": "An apparent pocket may be inadequate; unsupported entry cannot rely on it.",
        "recovery_limitations": "No infinite air pocket, automatic replenishment or free recovery.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:darkness",
        "classification": "APPROVED DESIGN",
        "trigger": "Light is absent, lost or obstructed in a confined space.",
        "observable_warnings": "Fading light, blind corners or inability to confirm footing.",
        "exposure": "Moving/working without actual adequate perception.",
        "possible_consequences": "Possible navigation error, delay, separation or fall.",
        "avoidance_or_mitigation": "Use available light/perception within actual limits, slow down or return.",
        "required_resources": "Finite light sources, marking materials and communication.",
        "failure_conditions": "Light can run out or perception be insufficient; no universal darkvision.",
        "recovery_limitations": "No free lighting, automatic map or hidden-path revelation.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:magical-residue",
        "classification": "APPROVED DESIGN",
        "trigger": "Contact or disturbance of a damaged magical environment, if verified.",
        "observable_warnings": "Observable effects or a supported sensory observation, not an automatic spell diagnosis.",
        "exposure": "Actual exposure to the evidenced source under its conditions.",
        "possible_consequences": "Possible danger or interference to be declared under existing rules.",
        "avoidance_or_mitigation": "Keep distance, gather lawful evidence and use only established abilities/costs when appropriate.",
        "required_resources": "Qualified voluntary expertise, finite mana/materials and safe withdrawal.",
        "failure_conditions": "Unknown function/range, failed understanding or depleted resources can block progress.",
        "recovery_limitations": "No free neutralization, mana, new spell, ownership or guaranteed ward shutdown.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:spatial-instability",
        "classification": "APPROVED DESIGN",
        "trigger": "Moving into an actually evidenced distorted physical/magical boundary.",
        "observable_warnings": "Inconsistent apparent alignment or an observed discontinuity, not a secret map answer.",
        "exposure": "Crossing or navigating the verified affected space.",
        "possible_consequences": "Possible disorientation, obstructed path or dangerous position; no automatic teleport or time advance.",
        "avoidance_or_mitigation": "Observe from a verified position, maintain cautious return references or withdraw.",
        "required_resources": "Finite lighting/markers, skilled assessment and existing abilities only.",
        "failure_conditions": "Apparent continuity may be unreliable; no ability or magic bypass is assumed.",
        "recovery_limitations": "No new temporal/spatial power, free anchor, solved route or reversible distortion.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      },
      {
        "id": "hazard-design:unstable-machinery",
        "classification": "APPROVED DESIGN",
        "trigger": "Touching, loading or releasing damaged mechanical equipment.",
        "observable_warnings": "Loose fittings, strain, corrosion or unexpected movement.",
        "exposure": "Actual proximity/operation in a verified danger zone.",
        "possible_consequences": "Possible crushing, falls, jammed routes or damaged tools.",
        "avoidance_or_mitigation": "Do not operate unverified equipment; assess, isolate by lawful safe means or avoid it.",
        "required_resources": "Appropriate tools, skilled help, sound supports and time.",
        "failure_conditions": "Unknown loading, worn parts or inadequate isolation can prevent safe work.",
        "recovery_limitations": "No functioning lift/forge is restored or created by a design note.",
        "numerical_effects": null,
        "automatic_damage": false,
        "current_placement_ids": null
      }
    ],
    "actual_population_events": [],
    "actual_encounters": [],
    "actual_damage_events": [],
    "automatic_respawn": false,
    "automatic_scaling": false
  }
}
```
