---
id: world-development-proposals
type: mechanics
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/npc-autonomy-framework-maintenance.md
- state/checkpoint.json
- entities/mechanics/outstanding-projects.md
---

# Proposed clocks and relationship domains

PROPOSED / REQUIRES APPROVAL. Category vocabulary only: no active clocks, starting values, progress scores, deadlines, future operations, numerical reputation or relationship changes. Archived faction clocks are prospective designs, not current verified starting values; none is copied or advanced here. A category is not an event guarantee.

Before creating a clock: identify an existing faction/project owner, bounded starting condition with evidence, verified progress/date if any, trigger conditions, possible (not guaranteed) consequences, visibility/discovery boundary and explicit approval. Keep unknown initial progress/date null. An active clock requires a separately approved, sourced record after privacy/storage review; maintenance creates none. Do not store secret clocks or consequences publicly. Future secret simulation needs a safe separate storage/visibility approach first; no visibility setting changes here.

Reputation distinguishes personal trust, professional/guild/government standing, public notoriety, criminal fear, faction alliances, friendships and family. Proposed future relationship records need subject/counterparty, domain, witnessed evidence/date, visibility, discovery and change source; qualitative evidence precedes any approved numeric scale. Existing bonds/family/relationships retain their owners. Blackscale notoriety does not reveal Theron's identity to anyone without an established discovery; no automatic shared knowledge, forced betrayal or arbitrary punishment. Possible future injury/exhaustion/delay/failure/disagreement/absence/permanent death follow circumstances and established fair-play rules, never a maintenance consequence.


```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "approval_status": "REQUIRES APPROVAL",
  "workflow_states": [
    "proposed",
    "offered",
    "accepted",
    "active-last-verified",
    "paused",
    "blocked",
    "awaiting-response",
    "completed",
    "failed",
    "canceled",
    "outcome-unknown"
  ],
  "event_categories": [
    "merchant-negotiations",
    "guild-recruitment",
    "military-patrols",
    "criminal-movements",
    "political-negotiations",
    "supply-shortages",
    "construction",
    "research",
    "investigations",
    "diplomatic-responses",
    "rival-expeditions"
  ],
  "clock_categories": [
    "political-tensions",
    "criminal-investigations",
    "merchant-activity",
    "construction",
    "training",
    "guild-activity",
    "dungeon-threats",
    "regional-conflicts",
    "seasonal-conditions",
    "npc-personal-goals"
  ],
  "clock_fields": [
    "clock_id",
    "owner_ref",
    "starting_condition_ref",
    "source_refs",
    "current_verified_progress",
    "trigger_refs",
    "possible_consequences",
    "visibility",
    "last_verified_date",
    "approval_ref"
  ],
  "relationship_domains": [
    "personal-trust",
    "professional-standing",
    "guild-reputation",
    "government-reputation",
    "public-notoriety",
    "criminal-fear",
    "faction-alliances",
    "friendships",
    "family"
  ],
  "relationship_fields": [
    "subject_id",
    "counterparty_id",
    "domain",
    "evidence_ref",
    "date",
    "visibility",
    "discovery_ref",
    "change_source_ref"
  ],
  "clocks": [],
  "relationship_changes": [],
  "automatic_advancement": false
}
```
