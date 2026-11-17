---
id: npc-autonomy-and-time
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-07-autonomy-approval.md
- changes/chronicles/npc-autonomy-framework-maintenance.md
- state/checkpoint.json
- entities/mechanics/outstanding-projects.md
- entities/items/guardian-links.md
- entities/items/first-hours-accord.md
- entities/mechanics/party-finances.md
- entities/mechanics/theron-abilities.md
- entities/mechanics/travel-routes.md
- entities/rules/payroll-construction-and-trade.md
---

# NPC autonomy, communication and time advancement

## Independence and limits

People retain personality, motives, knowledge, relationships, skills, resources, duties, physical limits, consent, safety and mortality. Loyalty does not erase judgment or the ability to refuse, disagree or request help. Preserve established personalities; sensible initiative, mistakes and success/failure arise in actual play, never fabricated gap-filling. Work needs money/time/equipment/materials/transport/training/personnel/physical and magical capacity/safety/legal authority. A manager cannot conjure paid construction; a researcher does not discover hidden functions by elapsed text; a guard cannot automatically convict. No free progress, mana, income or materials.

## Remote communication and delegation

Identify sender/recipient, exact request, scope of authority/budget, means, source and desired report destination. Distinguish proposed/sent/delivered/acknowledged/accepted/reported/closed; none implies the next. Check last verified position and its freshness, available messenger/letter route and access, plausible distance and time, or a specifically established magical channel/range/cost/recipient consent. Unknown route/range/arrival stays unknown. Guardian Links' limited tested functions and First Hour recognition are not universal communications. No modern telecommunications, instantaneous report, automatic delivered letter, teleported recall or invented acknowledgment.

Record a send/delivery/reply only after actual supported action in the relevant owner/chronicle; charge real resource costs only once in their original authority. Ask rather than compel cooperation; define delegation limits and check willingness. Tomas can exercise existing ordinary management authority without a new permission request for each ordinary decision, but cannot spend unrestricted personal purse funds. Beren remains independent; Vaeltharion supplies no automatic gift/ride/mana. Requesting an update does not produce one. Recall or ending a task needs communication and practical return travel; acceptance, departure, arrival, handover and cessation are separately verified. A revocation cannot retroactively undo work or reach an unavailable NPC instantly.

## Explicit time advancement — GM procedure, never an automatic job

1. Read the current checkpoint/status/locks, owner records and sources. END SESSION has ended play; this maintenance advances no time.
2. Identify the player's explicit requested advance or played scene, interval/endpoints and scope. Missing chronology is a gap, not an advance authorization; no Day156→181 bridge is invented.
3. Retrieve relevant assignments and source dates. Separate accepted/active-last-verified from proposed/offered/pending/unknown; check later supersession, availability, consent and dependencies. Old observations are not eternally current.
4. Retrieve only relevant existing faction claims; distinguish confirmed, historical, alleged, proposed and unknown-current. Filter GM/player knowledge before presentation.
5. Evaluate plausible sourced triggers and elapsed-time requirements. Proposed categories/clocks create no guaranteed events; do not copy archived clock values as current.
6. Respect actual geography, travel mode/distance/access, communication delay and weather where established. Proposed road links grant no functioning journey.
7. Check money/equipment/materials/personnel/training/magic/physical limits, safety, legal authority and authorization. No assumptions of unlimited manager spending, free work or automatic resource refresh.
8. Preserve independent NPC choices, willingness and motives; allow sensible initiative/refusal/delay and requests for assistance, not forced outcomes or arbitrary punishment.
9. Determine actual results through established gameplay rules and player agency, including fair consequences. No automatic success, research certification, healing mastery, contract completion or dungeon encounter.
10. Record only occurred results with stable event IDs, trigger/action/outcome evidence and date/uncertainty; no balancing history or second editable timeline.
11. Update affected character/creature/faction/quest/project owners and assignment evidence without overwriting historical observations. Maintain identity, custody, bond and knowledge distinctions.
12. Update checkpoint and dated chronicle together only for actual authorized play; update handoff/narration as appropriate. Do not mutate them merely to run retrieval.
13. Record actual money/inventory/resource effects once in their existing authorities, using shared event refs; no duplicate payroll, modeled income or construction payment.
14. Keep hidden outcomes separate from character knowledge. Disclose only discoveries with explicit evidence; secret simulation requires safe storage first. When ending session, checkpoint/handoff and stop play.

## Minimal gameplay retrieval

Resolve the requested actor/assignment/faction through index and registry; inspect only relevant original dated sections, newer supersessions and project dependencies. Return last verified activity/location with source date, known progress, unknown current developments and a next available action (e.g. request a report through a supported channel). A suggested action is not sent or completed. Unknown last observation date remains UNKNOWN; generic “party home” never recalls all independent people/animals. Do not print source-private intelligence, hidden intentions, whole faction files or secret event outcomes.

Use independently expandable, initially closed personnel groups per narration-format (native details in Markdown or functioning equivalent). A compact Person | Assignment | Status table inside each group may show source dates; keep concise outside summaries. No raw repository dump or huge permanent tracker. Raze/Aegis remain ability contexts, Alpha independent, patients free, staff paid with existing restrictions. This procedure is authorized reference architecture, not a new event, ability, relationship, power or time-advance engine.


```json
{
  "schema_version": 1,
  "assignment_owner_ref": "independent-assignments",
  "faction_owner_ref": "faction-activity",
  "event_owner_ref": "world-event-references",
  "proposal_owner_ref": "world-development-proposals",
  "communication_owner_refs": [
    "guardian-links",
    "first-hours-accord"
  ],
  "resource_owner_refs": [
    "party-finances",
    "theron-abilities",
    "payroll-construction-and-trade"
  ],
  "road_owner_ref": "travel-routes",
  "communication_states": [
    "proposed",
    "sent",
    "delivered",
    "acknowledged",
    "accepted",
    "reported",
    "closed"
  ],
  "new_communications": [],
  "new_time_advances": [],
  "new_abilities": [],
  "new_relationships": [],
  "new_resource_postings": [],
  "automatic_writes": false,
  "approved_autonomy_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-07-autonomy-approval.md",
    "character_design_ids": [
      "elowen-marcrest",
      "cassian-thornmere",
      "aveline-hartwell",
      "durnek-stonevein",
      "liora-thistlebloom",
      "selene-harrow",
      "orrin-valecrest",
      "mira-hearthwick"
    ],
    "authority_refs": {
      "assignments": "independent-assignments",
      "factions": "faction-activity",
      "chronology": "world-event-references",
      "communications": "settlement-communications",
      "travel": "travel-routes",
      "law": "justice-and-jurisdiction",
      "guilds": "guild-membership-and-contracts",
      "economy": "economy-accounting",
      "ledger": "state/finance-ledger.json"
    },
    "action_states": [
      "proposed-schedule",
      "planned-action",
      "attempted-action",
      "completed-action",
      "verified-outcome"
    ],
    "activity_categories": [
      "working",
      "traveling",
      "training",
      "resting",
      "shopping",
      "socializing",
      "business-management",
      "meetings",
      "investigation",
      "family-care",
      "personal-interests"
    ],
    "event_categories": [
      "political-developments",
      "merchant-negotiations",
      "trade-disputes",
      "seasonal-harvests",
      "weather-disruptions",
      "guild-elections",
      "professional-disputes",
      "construction",
      "local-celebrations",
      "criminal-investigations",
      "frontier-conflicts",
      "personal-milestones",
      "natural-disasters",
      "community-projects"
    ],
    "relationship_domains": [
      "trust",
      "friendship",
      "rivalry",
      "professional-respect",
      "family-bonds",
      "political-alliances",
      "business-partnerships",
      "personal-disagreements",
      "reputation",
      "betrayal",
      "reconciliation"
    ],
    "faction_interests": [
      "recruitment",
      "trade",
      "political-influence",
      "professional-training",
      "territorial-interests",
      "diplomacy",
      "competition",
      "internal-reform",
      "economic-survival"
    ],
    "pacing_factors": [
      "local-relevance",
      "consequence-severity",
      "information-availability",
      "existing-obligations",
      "time-elapsed",
      "player-proximity",
      "narrative-importance"
    ],
    "schedule_template": {
      "actor": null,
      "proposed_interval": null,
      "activity": null,
      "origin": null,
      "destination": null,
      "verified_route": null,
      "transport": null,
      "weather": null,
      "physical_limits": null,
      "obligations": null,
      "resources": null,
      "consent": null,
      "evidence": null,
      "status": null
    },
    "event_template": {
      "trigger": null,
      "initiating_actor_or_environment": null,
      "actor_knowledge": null,
      "time": null,
      "location": null,
      "resources": null,
      "relationships": null,
      "applicable_law": null,
      "action": null,
      "immediate_outcome": null,
      "resource_changes": null,
      "knowledge_changes": null,
      "longer_term_consequences": null,
      "source_refs": null,
      "owner_updates": null,
      "time_advance_evidence": null,
      "discovery_evidence": null,
      "participants": null
    },
    "actual_schedules": [],
    "actual_events": [],
    "actual_knowledge_changes": [],
    "actual_relationship_changes": [],
    "automatic_resolution": false
  }
}
```

## Phase 2 autonomy design

The world does not revolve around Theron. A person may independently plan, cooperate, decline, negotiate, reconsider or ask for help; loyalty is no obedience override. Public traits/preferences/values and design goals guide plausible decisions without deciding them. Existing canon governs actual personality, kinship, employment, equipment, relationships and resources. New safe design interests are not secret motives or discoveries. The eight character owners retain bounded designs, not a second NPC roster or current positions.

Scheduling is prospective. Before an actual interval, identify the actor's last verified state and explicit campaign-time authorization, then reconcile work, rest, family/personal obligations, physical limits, material/money/magic capacity, mode, distance, route access and evidenced weather. Existing commitments take precedence; compatible activities can be considered while Theron is occupied, but no unrequested days/months/years are simulated. A proposed schedule is not a plan, a plan is not an attempt, and attempted/completed/verified are distinct evidence claims. Delays, refusal, partial success and failure are possible. No goal automatically fills any stage.

The fourteen event types are bounded possibilities. An actual resolution needs a supported trigger and initiating actor/environment, actor knowledge from credible sources, a supported time interval and place, willing participants, finite resources, relevant relationships/law, actual action/outcome and independently evidenced consequences. Use the empty event template; unknown chronology stays unknown and cannot prove time-dependent completion. The existing chronicle contract still governs historical recording and source-qualified unknown dates. Link one actual event ID across original owners, dated chronicle, checkpoint when required and sole resource/ledger updates; never invent a second editable timeline or balancing history. Completeness checks cannot prove event truth or guarantee success.

Information travels through PR2 communication: sender, source, content, channel, route/cost, dispatch, receipt and discovery evidence remain separate. No unsent message, private conversation, hidden identity, distant event, crime or private financial detail becomes NPC knowledge by convenience. Direct observation and credible reports need dated/source-qualified evidence; rumor remains unverified and may be wrong. Receipt does not prove agreement or acceptance. Knowledge gained by one actor is not automatically shared with another or Theron.

Relationship/reputation procedures require an actual interaction or supported independent event, identified parties, prior evidence, qualitative change, date/uncertainty and original-owner/discovery review. Trust, friendship, rivalry, professional respect, family ties, alliances, partnerships, disagreement, reputation, betrayal and reconciliation are distinct domains. No numeric score, romance, automatic gratitude, faction-wide knowledge or forced betrayal is introduced; existing bonds and relationships are unchanged.

Alpha remains the separate larger independent unbound Frostfang alpha wolf; Shade remains the smaller gray bonded wolf with existing progression. No automatic recall, ownership, movement, training, bond or resource changes. Other companions retain their identities, loyalties, abilities, equipment, needs, refusal and independent responsibilities; wishes confer no new powers or source of mana.

Faction decisions require actual members/leadership, resources, location, consent, opportunity and evidence; the interests list activates no proposed criminal group, secret leader or operation. Government/settlement decisions use PR2 services and PR3 actual jurisdiction, with finite public works, lawful disputes, negotiations, appointments, investigations and community responses only through supported events. No title confers office, and existing Brackenford officials/businesses remain intact. PR4 guild/Concord membership is voluntary; no enrollment/election/assessment occurs here. PR6 ownership, labor, inventory, transport, contracts and actual payment evidence constrain every economic action; no independent initiative generates free funds, stock, wages, taxes, construction or assets.

Pacing selects relevant, consequential supported developments within elapsed time and information availability, with existing obligations, proximity and narrative importance informing presentation rather than causing events. Not every action needs narration; important developments reach Theron only by credible observation, witness, delivered message or investigation. Offscreen independent outcomes are not automatic player knowledge. Keep private GM outcomes, confidential informants, hidden plans/identities, unrevealed betrayals and conspiracies outside this public framework; no secret payload or visibility change is authorized.
