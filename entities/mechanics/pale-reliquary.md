---
id: pale-reliquary
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-05-dungeon-approval.md
- entities/mechanics/dungeon-design-proposals.md
- entities/mechanics/dungeon-ecology-and-hazards.md
- entities/rules/dungeon-exploration.md
---

# Pale Reliquary — approved design

Same identity as dungeon-proposal:pale-reliquary. This mechanics profile is a public design model, not a discovered location, actual entrance, secret room solution, current inhabitant or seeded treasure cache. Internal area topology is schematic and conditional; no travel or gameplay is performed.

```json
{
  "schema_version": 1,
  "dungeon_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
    "proposal_id": "dungeon-proposal:pale-reliquary",
    "name": "Pale Reliquary",
    "purpose_and_history_design": "A ceremonial order’s shrine and restricted relic-preservation architecture are design background. The order’s identity, dates and artifacts are not new historical discoveries or links to existing mysteries.",
    "regional_association": {
      "classification": "PROPOSED",
      "candidate_region_id": null,
      "description": "Isolated northern highland sanctuary; not placed in Frostmarch, Frostspire or another known site.",
      "verified_entrance_id": null,
      "exact_coordinates": null,
      "access_route_ids": []
    },
    "difficulty": {
      "domain": "dungeon-threat",
      "design_label": "S",
      "legacy_proposed_label": "S",
      "compatible_rank": "S",
      "mapping_status": "DESIGN REFERENCE ONLY",
      "combat_integration_phase": "PR8"
    },
    "areas": [
      {
        "id": "design-area:pale-reliquary:outer-shrine",
        "name": "Outer shrine",
        "description": "Public ceremonial approach design, without verified entrance or present worshippers.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:unstable-bridge",
          "hazard-design:darkness"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:pale-reliquary:pilgrim-crypt",
        "name": "Pilgrim crypt",
        "description": "Finite memorial passages whose rights, occupants and stability are unverified.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:low-oxygen",
          "hazard-design:collapsing-floor"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:pale-reliquary:trial-chambers",
        "name": "Trial chambers",
        "description": "Ceremonial/assessment rooms, with no hidden puzzle answer, mandatory trial or proven working mechanism.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:magical-residue",
          "hazard-design:unstable-machinery"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:pale-reliquary:reliquary",
        "name": "Reliquary",
        "description": "Protected-object preservation space; no named or recoverable artifact is established.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:magical-residue",
          "hazard-design:collapsing-floor"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:pale-reliquary:inner-sanctum",
        "name": "Inner sanctum",
        "description": "Finite inner ritual area; access/mandate and guardian presence remain unknown.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:magical-residue",
          "hazard-design:darkness"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      }
    ],
    "connections": [
      {
        "from_area_id": "design-area:pale-reliquary:outer-shrine",
        "to_area_id": "design-area:pale-reliquary:pilgrim-crypt",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:pale-reliquary:pilgrim-crypt",
        "to_area_id": "design-area:pale-reliquary:trial-chambers",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:pale-reliquary:trial-chambers",
        "to_area_id": "design-area:pale-reliquary:inner-sanctum",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:pale-reliquary:inner-sanctum",
        "to_area_id": "design-area:pale-reliquary:reliquary",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:pale-reliquary:reliquary",
        "to_area_id": "design-area:pale-reliquary:outer-shrine",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:pale-reliquary:pilgrim-crypt",
        "to_area_id": "design-area:pale-reliquary:reliquary",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      }
    ],
    "entry_interface_area_ids": [
      "design-area:pale-reliquary:outer-shrine"
    ],
    "retreat_path_designs": [
      [
        "design-area:pale-reliquary:inner-sanctum",
        "design-area:pale-reliquary:trial-chambers",
        "design-area:pale-reliquary:pilgrim-crypt",
        "design-area:pale-reliquary:outer-shrine"
      ],
      [
        "design-area:pale-reliquary:inner-sanctum",
        "design-area:pale-reliquary:reliquary",
        "design-area:pale-reliquary:outer-shrine"
      ]
    ],
    "access_and_rest_limits": "Local cultural rights and consent may preclude entry/removal. Respectful observation, dialogue if possible, documenting without taking, seeking lawful custodians and withdrawal are distinct noncombat options. Rest needs independently verified safe air, shelter, conditions and supplies; no free healing or mana recovery.",
    "resource_requirements": [
      "Finite light/marking and suitable navigation tools",
      "Actual safe transport/load and appropriate climbing/water/temperature capability",
      "Food, water, rest, competent willing help and existing spell costs if used"
    ],
    "ecology_design": "Possible sentinels/oathbound spirits require a supported finite mandate/energy source, not an automatic link to existing guardians. Predators need access, prey and refuge; their current presence is unverified.",
    "ecological_boundary": "Potential inhabitants need actual viable sustenance, water/air/refuge or bounded supported energy, finite numbers and agency. No current population, hostility, energy source or automatic respawn.",
    "encounter_designs": [
      {
        "id": "encounter-design:pale-reliquary:navigation",
        "classification": "PROPOSED",
        "types": [
          "exploration",
          "stealth",
          "resource-management"
        ],
        "area_id": "design-area:pale-reliquary:outer-shrine",
        "premise": "Survey only actually observable terrain, mark a lawful return and limit light/time use; no map or hidden route is revealed.",
        "monster_reference_ids": [],
        "options": "Observe, pause, reduce disturbance or withdraw; abilities must already exist.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:pale-reliquary:hazard-assessment",
        "classification": "PROPOSED",
        "types": [
          "environmental-hazard",
          "mechanical-trap"
        ],
        "area_id": "design-area:pale-reliquary:pilgrim-crypt",
        "premise": "A verified physical warning could call for assessment of support, water, air or damaged apparatus. No trigger or disarm occurs here.",
        "monster_reference_ids": [],
        "options": "Avoid, document, seek qualified help or choose a verified alternative; no guaranteed mitigation.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:pale-reliquary:possible-inhabitant",
        "classification": "PROPOSED",
        "types": [
          "creature-encounter",
          "negotiation"
        ],
        "area_id": "design-area:pale-reliquary:trial-chambers",
        "premise": "Only if actual inhabitants are established, consider territorial/nest defense, original guardian duty, fear, avoidance and finite resources.",
        "monster_reference_ids": [
          "monster-reference:ancient-reliquary-warden"
        ],
        "options": "Keep distance, avoid interference, negotiate only where communication/agency permit, disengage or resolve under existing combat rules.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:pale-reliquary:recovery-ethics",
        "classification": "PROPOSED",
        "types": [
          "moral-decision",
          "magical-defense"
        ],
        "area_id": "design-area:pale-reliquary:reliquary",
        "premise": "Possible records/materials/cultural rights raise questions of access and ownership, not automatic loot. No secret answer or working ward is supplied.",
        "monster_reference_ids": [],
        "options": "Observe without taking, preserve context, seek lawful permission/competent identification or leave.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:pale-reliquary:rescue-retreat",
        "classification": "PROPOSED",
        "types": [
          "rescue",
          "retreat"
        ],
        "area_id": "design-area:pale-reliquary:inner-sanctum",
        "premise": "If actual exploration later puts a party at risk, finite return, care and transport must be reconsidered; no trapped NPC or rescue outcome is generated.",
        "monster_reference_ids": [],
        "options": "Use a verified return, request help through a valid route/channel, delay safely if possible or abandon onward exploration.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      }
    ],
    "treasure_categories": [
      "Ceremonial/decorative objects as categories only",
      "Unidentified relic categories requiring ownership review",
      "Preservation/craft study opportunities"
    ],
    "recovery_rule_ref": "dungeon-exploration",
    "treasure_policy": "Finite potential categories only, not seeded contents or a reward roll. Before any actual recovery establish specific location/source, finite quantity/availability, discovery, recoverability, title, legal rights, transport and approved original inventory/finance evidence. No known cache or legendary item.",
    "legal_owner_ref": "justice-and-jurisdiction",
    "legal_access_design": "Verify actual jurisdiction, land/mining claims, protected cultural rights, dangerous-magic restrictions, salvage title, contract/permit scope and willing custodians. Existence/rank/guild interest grants no permit or ownership.",
    "prospective_faction_interests": [
      {
        "faction_id": "circle-of-seven-lamps",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "scribes-collegium",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "stonewatch-wardens",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "nightglass-circle",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      }
    ],
    "discovery_requirements": [
      "An actual source-backed lead, not a generated rumor or completed clue",
      "Independent verification of location, access rights, entrance and compatible approach",
      "Player-knowledge evidence separate from public reference design"
    ],
    "lead_categories": [
      "Potential archival inquiry subject to lawful access",
      "Potential local survey/report request without inventing a witness or reply",
      "Potential lawful professional consultation, not an offered or accepted contract"
    ],
    "persistence_rule": "Actual changes persist only through existing dated exploration/creature/item/quest/chronicle owners. No automatic reset, respawn, treasure refill, structural repair, revival, recharge or remote outcome; no section becomes cleared by a design lookup.",
    "current_conditions": null,
    "current_population": null,
    "current_reward_inventory": null,
    "current_recoverable_quantity": null,
    "actual_discoveries": [],
    "actual_exploration_events": [],
    "actual_population_events": [],
    "actual_reward_events": [],
    "actual_quest_outcomes": [],
    "hidden_solutions": [],
    "hidden_treasure_locations": [],
    "unsupported_mystery_connections": [],
    "new_abilities": [],
    "existing_site_id": null
  }
}
```
