---
id: hollowstone-mine
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-05-dungeon-approval.md
- entities/mechanics/dungeon-design-proposals.md
- entities/mechanics/dungeon-ecology-and-hazards.md
- entities/rules/dungeon-exploration.md
---

# Hollowstone Mine — approved design

Same identity as dungeon-proposal:hollowstone-mine. This mechanics profile is a public design model, not a discovered location, actual entrance, secret room solution, current inhabitant or seeded treasure cache. Internal area topology is schematic and conditional; no travel or gameplay is performed.

```json
{
  "schema_version": 1,
  "dungeon_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
    "proposal_id": "dungeon-proposal:hollowstone-mine",
    "name": "Hollowstone Mine",
    "purpose_and_history_design": "Abandoned extraction workings form the design background. Moisture and decaying material could sustain fungi and prey; no dated closure, survey, current mine or ore deposit is asserted.",
    "regional_association": {
      "classification": "PROPOSED",
      "candidate_region_id": "stoneford",
      "description": "Stoneford quarry hills; exact hillside, land title and approach unsurveyed.",
      "verified_entrance_id": null,
      "exact_coordinates": null,
      "access_route_ids": []
    },
    "difficulty": {
      "domain": "dungeon-threat",
      "design_label": "D",
      "legacy_proposed_label": "D",
      "compatible_rank": "D",
      "mapping_status": "DESIGN REFERENCE ONLY",
      "combat_integration_phase": "PR8"
    },
    "areas": [
      {
        "id": "design-area:hollowstone-mine:collapsed-entrance",
        "name": "Collapsed entrance",
        "description": "Damaged portal and debris apron, with load-bearing/air/exit questions.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:cave-in",
          "hazard-design:darkness"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:hollowstone-mine:lift-shaft",
        "name": "Lift shaft",
        "description": "Old shaft with possible stairs/service ledges and nonfunctional equipment until verified.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:unstable-machinery",
          "hazard-design:cave-in"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:hollowstone-mine:flooded-gallery",
        "name": "Flooded gallery",
        "description": "Low workings with groundwater/inflow/drainage uncertainties and no safe air assumed.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:flooding",
          "hazard-design:low-oxygen"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:hollowstone-mine:fungus-chambers",
        "name": "Fungus chambers",
        "description": "Moist organic pockets could support fungi, insects, spiders and burrowers only where food/air exist.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:toxic-spores",
          "hazard-design:darkness"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:hollowstone-mine:sealed-survey-office",
        "name": "Sealed survey office",
        "description": "Finite former record room; access, record condition, title and contents unverified.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:collapsing-floor",
          "hazard-design:darkness"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      }
    ],
    "connections": [
      {
        "from_area_id": "design-area:hollowstone-mine:collapsed-entrance",
        "to_area_id": "design-area:hollowstone-mine:lift-shaft",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:hollowstone-mine:lift-shaft",
        "to_area_id": "design-area:hollowstone-mine:flooded-gallery",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:hollowstone-mine:flooded-gallery",
        "to_area_id": "design-area:hollowstone-mine:sealed-survey-office",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:hollowstone-mine:sealed-survey-office",
        "to_area_id": "design-area:hollowstone-mine:fungus-chambers",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:hollowstone-mine:fungus-chambers",
        "to_area_id": "design-area:hollowstone-mine:collapsed-entrance",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:hollowstone-mine:lift-shaft",
        "to_area_id": "design-area:hollowstone-mine:fungus-chambers",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      }
    ],
    "entry_interface_area_ids": [
      "design-area:hollowstone-mine:collapsed-entrance"
    ],
    "retreat_path_designs": [
      [
        "design-area:hollowstone-mine:sealed-survey-office",
        "design-area:hollowstone-mine:flooded-gallery",
        "design-area:hollowstone-mine:lift-shaft",
        "design-area:hollowstone-mine:collapsed-entrance"
      ],
      [
        "design-area:hollowstone-mine:sealed-survey-office",
        "design-area:hollowstone-mine:fungus-chambers",
        "design-area:hollowstone-mine:collapsed-entrance"
      ]
    ],
    "access_and_rest_limits": "Air, water, sound rock and equipment must be verified. No functioning lift, breathable shaft or alternative surface exit is implied. Rest needs independently verified safe air, shelter, conditions and supplies; no free healing or mana recovery.",
    "resource_requirements": [
      "Finite light/marking and suitable navigation tools",
      "Actual safe transport/load and appropriate climbing/water/temperature capability",
      "Food, water, rest, competent willing help and existing spell costs if used"
    ],
    "ecology_design": "Possible spiders need insect/small-animal prey; fungal detritivores need nutrients and moisture; bats would need actual food, airflow and exits. These are habitat hypotheses, not current counts.",
    "ecological_boundary": "Potential inhabitants need actual viable sustenance, water/air/refuge or bounded supported energy, finite numbers and agency. No current population, hostility, energy source or automatic respawn.",
    "encounter_designs": [
      {
        "id": "encounter-design:hollowstone-mine:navigation",
        "classification": "PROPOSED",
        "types": [
          "exploration",
          "stealth",
          "resource-management"
        ],
        "area_id": "design-area:hollowstone-mine:collapsed-entrance",
        "premise": "Survey only actually observable terrain, mark a lawful return and limit light/time use; no map or hidden route is revealed.",
        "monster_reference_ids": [],
        "options": "Observe, pause, reduce disturbance or withdraw; abilities must already exist.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:hollowstone-mine:hazard-assessment",
        "classification": "PROPOSED",
        "types": [
          "environmental-hazard",
          "mechanical-trap"
        ],
        "area_id": "design-area:hollowstone-mine:lift-shaft",
        "premise": "A verified physical warning could call for assessment of support, water, air or damaged apparatus. No trigger or disarm occurs here.",
        "monster_reference_ids": [],
        "options": "Avoid, document, seek qualified help or choose a verified alternative; no guaranteed mitigation.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:hollowstone-mine:possible-inhabitant",
        "classification": "PROPOSED",
        "types": [
          "creature-encounter",
          "negotiation"
        ],
        "area_id": "design-area:hollowstone-mine:flooded-gallery",
        "premise": "Only if actual inhabitants are established, consider territorial/nest defense, original guardian duty, fear, avoidance and finite resources.",
        "monster_reference_ids": [
          "monster-reference:giant-cave-spider",
          "monster-reference:fungal-burrower"
        ],
        "options": "Keep distance, avoid interference, negotiate only where communication/agency permit, disengage or resolve under existing combat rules.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:hollowstone-mine:recovery-ethics",
        "classification": "PROPOSED",
        "types": [
          "moral-decision"
        ],
        "area_id": "design-area:hollowstone-mine:fungus-chambers",
        "premise": "Possible records/materials/cultural rights raise questions of access and ownership, not automatic loot. No secret answer or working ward is supplied.",
        "monster_reference_ids": [],
        "options": "Observe without taking, preserve context, seek lawful permission/competent identification or leave.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:hollowstone-mine:rescue-retreat",
        "classification": "PROPOSED",
        "types": [
          "rescue",
          "retreat"
        ],
        "area_id": "design-area:hollowstone-mine:sealed-survey-office",
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
      "Tools",
      "Limited mineral samples subject to title",
      "Damaged survey-record categories"
    ],
    "recovery_rule_ref": "dungeon-exploration",
    "treasure_policy": "Finite potential categories only, not seeded contents or a reward roll. Before any actual recovery establish specific location/source, finite quantity/availability, discovery, recoverability, title, legal rights, transport and approved original inventory/finance evidence. No known cache or legendary item.",
    "legal_owner_ref": "justice-and-jurisdiction",
    "legal_access_design": "Verify actual jurisdiction, land/mining claims, protected cultural rights, dangerous-magic restrictions, salvage title, contract/permit scope and willing custodians. Existence/rank/guild interest grants no permit or ownership.",
    "prospective_faction_interests": [
      {
        "faction_id": "greenward-covenant",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "ironhand-smiths-compact",
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
        "faction_id": "black-pick-syndicate",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "thornless-circle",
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
