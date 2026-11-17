---
id: quest-resolution-proposals
type: mechanics
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/main-quest-framework-maintenance.md
- state/checkpoint.json
- state/open-verifications.md
---

# Proposed finite main-quest architecture

PROPOSED / REQUIRES APPROVAL: five chapters with3/3/3/3/2 major-scene targets (14 total), not a historical sequence, forced encounter count or approved ending. Graph edges describe an editorial route to a finite ending, not mandatory travel/order. Scenes may combine/reorder/skip redundant work consistently with evidence and player choices. A major scene advances a required objective, answers an important question or creates a consequential decision. No runtime quest status changes.

Seven proposed essential objectives permit a costly/imperfect conclusion. Dependencies concern informed decision readiness, never every side quest, all minor arrests, unanimous faction approval, a particular interrogation or a conviction. Addressing central harm may mean documented lawful containment/disposition rather than personally resolving every independent court matter. Independent Thane/Sorn reviews, unrelated notices and optional identities can remain consequences pending with explicit handoff; do not erase unresolved victims or falsely certify safety.

Each critical objective has two unfilled distinct clue-route slots. They are design requirements, not two existing operational paths. After a fixed answer is approved and safely stored, provide at least one actionable source-consistent route per required question, preferably two materially distinct methods. Supply geography/access/resource/discovery support, reachable scene transitions and an alternative to any single unwilling witness, failed check or Mental Probe. Current readiness is BLOCKED by missing answers/routes, not silently playable or baseline-invalid.

No unchanged evidence must be searched repeatedly to unlock new mandatory mystery layers. Retain a decisive obtained clue; if information genuinely cannot be recovered, permit a consequential partial/setback route, bounded alternate lead or player-approved ruling rather than infinite retries. Obstacles may cost time/resources or require preparation but must not indefinitely hide necessary approved answers. Optional lore never silently becomes mandatory. Each approved scene needs success/partial/setback possibilities and exit to meaningful progress; no guaranteed survival, cooperation, victory, betrayal, execution or specific method.

Investigation, negotiation, nonlethal capture, stealth, intimidation, lawful cooperation, magical research, confrontation, combined approaches, delegation and postponement remain choices. Nonlethal Blackscale style and NPC agency persist. Permanent/failure consequences follow actual play and established rules, not an automatic penalty from plan metadata. Side quests continue independently after an ending; the campaign is not completed by the main plot's conclusion.


```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "approval_status": "REQUIRES APPROVAL",
  "entry_chapter_id": "chapter:gray-ledger",
  "ending_chapter_id": "chapter:judgment",
  "chapters": [
    {
      "chapter_id": "chapter:gray-ledger",
      "title": "The Gray Ledger",
      "target_scenes": 3,
      "objective_ids": [
        "objective:command-chain"
      ],
      "mystery_ids": [
        "mystery:surviving-crown",
        "mystery:v9-controller"
      ],
      "next_ids": [
        "chapter:last-v9-cases"
      ],
      "classification": "PROPOSED",
      "activation": "BLOCKED PENDING ANSWER APPROVAL",
      "mandatory_repeat": false,
      "can_combine_or_reorder": true
    },
    {
      "chapter_id": "chapter:last-v9-cases",
      "title": "The Last V-9 Cases",
      "target_scenes": 3,
      "objective_ids": [
        "objective:v9-harm"
      ],
      "mystery_ids": [
        "mystery:v9-transferred",
        "mystery:v9-other-cases"
      ],
      "next_ids": [
        "chapter:surviving-conspiracy"
      ],
      "classification": "PROPOSED",
      "activation": "BLOCKED PENDING ANSWER APPROVAL",
      "mandatory_repeat": false,
      "can_combine_or_reorder": true
    },
    {
      "chapter_id": "chapter:surviving-conspiracy",
      "title": "The Surviving Conspiracy",
      "target_scenes": 3,
      "objective_ids": [
        "objective:surviving-opposition"
      ],
      "mystery_ids": [
        "mystery:surviving-crown",
        "mystery:dene",
        "mystery:acting-receiver"
      ],
      "next_ids": [
        "chapter:fifth-bell"
      ],
      "classification": "PROPOSED",
      "activation": "BLOCKED PENDING ANSWER APPROVAL",
      "mandatory_repeat": false,
      "can_combine_or_reorder": true
    },
    {
      "chapter_id": "chapter:fifth-bell",
      "title": "The Fifth Bell",
      "target_scenes": 3,
      "objective_ids": [
        "objective:fifth-bell",
        "objective:counterfeit-authority"
      ],
      "mystery_ids": [
        "mystery:fb5",
        "mystery:northern-index",
        "mystery:er7-safety",
        "mystery:witness-authority"
      ],
      "next_ids": [
        "chapter:judgment"
      ],
      "classification": "PROPOSED",
      "activation": "BLOCKED PENDING ANSWER APPROVAL",
      "mandatory_repeat": false,
      "can_combine_or_reorder": true
    },
    {
      "chapter_id": "chapter:judgment",
      "title": "Judgment of the Witness",
      "target_scenes": 2,
      "objective_ids": [
        "objective:witness-choice",
        "objective:immediate-consequences"
      ],
      "mystery_ids": [
        "mystery:witness-authority"
      ],
      "next_ids": [],
      "classification": "PROPOSED",
      "activation": "BLOCKED PENDING ANSWER APPROVAL",
      "mandatory_repeat": false,
      "can_combine_or_reorder": true
    }
  ],
  "objectives": [
    {
      "objective_id": "objective:command-chain",
      "target": "Determine the responsible command chain within the supported central scope.",
      "depends_on": [],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:v9-harm",
      "target": "Address remaining central V-9 harm or establish lawful disposition; keep distinct cases and completed restoration.",
      "depends_on": [],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:fifth-bell",
      "target": "Neutralize or lawfully contain the central Fifth Bell threat without destroying preserved safeguards by assumption.",
      "depends_on": [],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:counterfeit-authority",
      "target": "Resolve essential surviving counterfeit-authority risk without reopening the ended Empty Seat channel.",
      "depends_on": [],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:surviving-opposition",
      "target": "Face the responsible surviving opposition through supported player-chosen methods.",
      "depends_on": [],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:witness-choice",
      "target": "Make a consequential informed decision about the relevant Witness system.",
      "depends_on": [
        "objective:fifth-bell",
        "objective:counterfeit-authority"
      ],
      "required_for_ending": true,
      "classification": "PROPOSED"
    },
    {
      "objective_id": "objective:immediate-consequences",
      "target": "Establish immediate political/personal consequences, leaving independent proceedings with their lawful owners.",
      "depends_on": [
        "objective:command-chain",
        "objective:v9-harm",
        "objective:surviving-opposition",
        "objective:witness-choice"
      ],
      "required_for_ending": true,
      "classification": "PROPOSED"
    }
  ],
  "clue_route_slots": [
    {
      "route_id": "clue-route:command-chain:1",
      "objective_id": "objective:command-chain",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:command-chain:2",
      "objective_id": "objective:command-chain",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:v9-harm:1",
      "objective_id": "objective:v9-harm",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:v9-harm:2",
      "objective_id": "objective:v9-harm",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:fifth-bell:1",
      "objective_id": "objective:fifth-bell",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:fifth-bell:2",
      "objective_id": "objective:fifth-bell",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:counterfeit-authority:1",
      "objective_id": "objective:counterfeit-authority",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:counterfeit-authority:2",
      "objective_id": "objective:counterfeit-authority",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:surviving-opposition:1",
      "objective_id": "objective:surviving-opposition",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:surviving-opposition:2",
      "objective_id": "objective:surviving-opposition",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:witness-choice:1",
      "objective_id": "objective:witness-choice",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:witness-choice:2",
      "objective_id": "objective:witness-choice",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:immediate-consequences:1",
      "objective_id": "objective:immediate-consequences",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    },
    {
      "route_id": "clue-route:immediate-consequences:2",
      "objective_id": "objective:immediate-consequences",
      "answer_ref": null,
      "method": null,
      "location_id": null,
      "discovery_ref": null,
      "activation": "BLOCKED PENDING ANSWER APPROVAL"
    }
  ],
  "outcome_labels": [
    "active",
    "objective-completed",
    "main-quest-completed",
    "failed",
    "abandoned",
    "deferred",
    "partially-resolved",
    "consequences-pending",
    "outcome-unknown"
  ],
  "optional_domains": [
    "estate-expansion",
    "academy",
    "companion-training",
    "magic-research",
    "dungeon-exploration",
    "optional-bounties",
    "independent-legal-proceedings",
    "guild-progression",
    "family-relationships",
    "property-management",
    "unrelated-faction-disputes"
  ],
  "new_scene_outcomes": [],
  "new_quest_completions": [],
  "automatic_rewards": false
}
```
