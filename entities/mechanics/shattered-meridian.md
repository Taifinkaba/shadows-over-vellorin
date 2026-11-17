---
id: shattered-meridian
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-05-dungeon-approval.md
- entities/mechanics/dungeon-design-proposals.md
- entities/mechanics/dungeon-ecology-and-hazards.md
- entities/rules/dungeon-exploration.md
---

# Shattered Meridian — approved design

Same identity as dungeon-proposal:shattered-meridian. This mechanics profile is a public design model, not a discovered location, actual entrance, secret room solution, current inhabitant or seeded treasure cache. Internal area topology is schematic and conditional; no travel or gameplay is performed.

```json
{
  "schema_version": 1,
  "dungeon_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
    "proposal_id": "dungeon-proposal:shattered-meridian",
    "name": "Shattered Meridian",
    "purpose_and_history_design": "Former astronomical sanctuary damaged by an ancient magical disaster is approved design history, not a dated campaign event or new revelation. Its phenomena do not unlock temporal/spatial skills or create a relic.",
    "regional_association": {
      "classification": "PROPOSED",
      "candidate_region_id": null,
      "description": "Isolated mountain plateau; exact location, approach and relation to other observatories unknown.",
      "verified_entrance_id": null,
      "exact_coordinates": null,
      "access_route_ids": []
    },
    "difficulty": {
      "domain": "dungeon-threat",
      "design_label": "SS",
      "legacy_proposed_label": "SS",
      "compatible_rank": null,
      "mapping_status": "UNRESOLVED LEGACY SS",
      "combat_integration_phase": "PR8"
    },
    "areas": [
      {
        "id": "design-area:shattered-meridian:broken-causeway",
        "name": "Broken causeway",
        "description": "Finite damaged approach design; anchoring, weather and actual external access unknown.",
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
        "id": "design-area:shattered-meridian:observatory",
        "name": "Observatory",
        "description": "Collapsed towers and damaged mundane instruments; no authenticated astronomical answer or artifact supplied.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:collapsing-floor",
          "hazard-design:magical-residue"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:shattered-meridian:suspended-terraces",
        "name": "Suspended terraces",
        "description": "Physical terrace/causeway design, not an unlimited floating space or automatic teleport route.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:unstable-bridge",
          "hazard-design:spatial-instability"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:shattered-meridian:warded-chamber",
        "name": "Warded chamber",
        "description": "Damaged research-room design; no functioning ward, hidden solution or new ability granted.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:spatial-instability",
          "hazard-design:magical-residue"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      },
      {
        "id": "design-area:shattered-meridian:collapsed-summit",
        "name": "Collapsed summit",
        "description": "Finite summit remains and exposed ledges; no secret cache or endpoint revelation.",
        "classification": "APPROVED DESIGN",
        "hazard_reference_ids": [
          "hazard-design:cave-in",
          "hazard-design:extreme-heat"
        ],
        "current_state": null,
        "current_inhabitants": null,
        "current_contents": null
      }
    ],
    "connections": [
      {
        "from_area_id": "design-area:shattered-meridian:broken-causeway",
        "to_area_id": "design-area:shattered-meridian:observatory",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:shattered-meridian:observatory",
        "to_area_id": "design-area:shattered-meridian:suspended-terraces",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:shattered-meridian:suspended-terraces",
        "to_area_id": "design-area:shattered-meridian:collapsed-summit",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:shattered-meridian:collapsed-summit",
        "to_area_id": "design-area:shattered-meridian:warded-chamber",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:shattered-meridian:warded-chamber",
        "to_area_id": "design-area:shattered-meridian:broken-causeway",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      },
      {
        "from_area_id": "design-area:shattered-meridian:observatory",
        "to_area_id": "design-area:shattered-meridian:warded-chamber",
        "classification": "APPROVED DESIGN",
        "physical_model": "Finite original access/service passage, stair or ledge relationship consistent with adjacent design areas; no portal or new surface opening.",
        "traversal_condition": "Requires actual width/support, water/air/heat, access rights, equipment and return verification. Design connection is not current passability.",
        "reverse_possible": true,
        "current_passability": null
      }
    ],
    "entry_interface_area_ids": [
      "design-area:shattered-meridian:broken-causeway"
    ],
    "retreat_path_designs": [
      [
        "design-area:shattered-meridian:collapsed-summit",
        "design-area:shattered-meridian:suspended-terraces",
        "design-area:shattered-meridian:observatory",
        "design-area:shattered-meridian:broken-causeway"
      ],
      [
        "design-area:shattered-meridian:collapsed-summit",
        "design-area:shattered-meridian:warded-chamber",
        "design-area:shattered-meridian:broken-causeway"
      ]
    ],
    "access_and_rest_limits": "Plan more than one verified internal return path and safe stopping criteria; damaged spans, weather and distorted appearance can invalidate them. No new teleport, time shift, anchor or ability is supplied. Rest needs independently verified safe air, shelter, conditions and supplies; no free healing or mana recovery.",
    "resource_requirements": [
      "Finite light/marking and suitable navigation tools",
      "Actual safe transport/load and appropriate climbing/water/temperature capability",
      "Food, water, rest, competent willing help and existing spell costs if used"
    ],
    "ecology_design": "Possible sky predators need actual prey, roosts and survivable weather; ancient guardians require supported finite energy and mandate. Spatial residue is a bounded hazard possibility, not an infinite mana source or new ecosystem population.",
    "ecological_boundary": "Potential inhabitants need actual viable sustenance, water/air/refuge or bounded supported energy, finite numbers and agency. No current population, hostility, energy source or automatic respawn.",
    "encounter_designs": [
      {
        "id": "encounter-design:shattered-meridian:navigation",
        "classification": "PROPOSED",
        "types": [
          "exploration",
          "stealth",
          "resource-management"
        ],
        "area_id": "design-area:shattered-meridian:broken-causeway",
        "premise": "Survey only actually observable terrain, mark a lawful return and limit light/time use; no map or hidden route is revealed.",
        "monster_reference_ids": [],
        "options": "Observe, pause, reduce disturbance or withdraw; abilities must already exist.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:shattered-meridian:hazard-assessment",
        "classification": "PROPOSED",
        "types": [
          "environmental-hazard",
          "mechanical-trap"
        ],
        "area_id": "design-area:shattered-meridian:observatory",
        "premise": "A verified physical warning could call for assessment of support, water, air or damaged apparatus. No trigger or disarm occurs here.",
        "monster_reference_ids": [],
        "options": "Avoid, document, seek qualified help or choose a verified alternative; no guaranteed mitigation.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:shattered-meridian:possible-inhabitant",
        "classification": "PROPOSED",
        "types": [
          "creature-encounter",
          "negotiation"
        ],
        "area_id": "design-area:shattered-meridian:suspended-terraces",
        "premise": "Only if actual inhabitants are established, consider territorial/nest defense, original guardian duty, fear, avoidance and finite resources.",
        "monster_reference_ids": [],
        "options": "Keep distance, avoid interference, negotiate only where communication/agency permit, disengage or resolve under existing combat rules.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:shattered-meridian:recovery-ethics",
        "classification": "PROPOSED",
        "types": [
          "moral-decision",
          "magical-defense"
        ],
        "area_id": "design-area:shattered-meridian:warded-chamber",
        "premise": "Possible records/materials/cultural rights raise questions of access and ownership, not automatic loot. No secret answer or working ward is supplied.",
        "monster_reference_ids": [],
        "options": "Observe without taking, preserve context, seek lawful permission/competent identification or leave.",
        "required_resources": "Actual willing actors, observed conditions, lawful access, time/light/supplies and existing capabilities; no costs are deducted by this design.",
        "guaranteed_success": false,
        "current_population_count": null,
        "actual_outcomes": []
      },
      {
        "id": "encounter-design:shattered-meridian:rescue-retreat",
        "classification": "PROPOSED",
        "types": [
          "rescue",
          "retreat"
        ],
        "area_id": "design-area:shattered-meridian:collapsed-summit",
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
      "Damaged mundane instruments",
      "Astronomical research categories",
      "Limited rare-material samples requiring appraisal/title"
    ],
    "recovery_rule_ref": "dungeon-exploration",
    "treasure_policy": "Finite potential categories only, not seeded contents or a reward roll. Before any actual recovery establish specific location/source, finite quantity/availability, discovery, recoverability, title, legal rights, transport and approved original inventory/finance evidence. No known cache or legendary item.",
    "legal_owner_ref": "justice-and-jurisdiction",
    "legal_access_design": "Verify actual jurisdiction, land/mining claims, protected cultural rights, dangerous-magic restrictions, salvage title, contract/permit scope and willing custodians. Existence/rank/guild interest grants no permit or ownership.",
    "prospective_faction_interests": [
      {
        "faction_id": "scribes-collegium",
        "classification": "PROPOSED",
        "interest": "Potential professional study, lawful expedition support, conservation or illicit-resource pressure according to that owner’s design; no specific expedition, discovery, occupation or secret base.",
        "actual_operations": []
      },
      {
        "faction_id": "circle-of-seven-lamps",
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
