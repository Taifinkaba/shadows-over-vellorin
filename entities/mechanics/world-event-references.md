---
id: world-event-references
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/npc-autonomy-framework-maintenance.md
- state/checkpoint.json
- entities/mechanics/outstanding-projects.md
- changes/chronicles/year847-day153-development.md
- changes/chronicles/year847-day153-finances.md
- changes/chronicles/year847-day153-freight.md
- changes/chronicles/year847-day472-first-hour.md
- changes/chronicles/year848-day137-end-session.md
- changes/chronicles/year848-day156-end-session.md
---

# Historical chronicle routing and event contract

Existing dated chronicles remain the sole historical chronology authorities; references below are document handles, not six newly generated in-world events. Some documents cover multiple events or the same day; document order does not supply missing relative timing. Preserve exact year/day and source qualifications; no assumed year length or invented interstitial sequence. Maintenance/design chronicles are not in-world time advances.

For future actual event records in the existing dated chronicle, use stable unique event ID, date/time (unknown if missing), location, initiating/participating actors, category, trigger, action, outcome, affected people/factions, quests, resource-effect authority refs, knowledge/discovery and sources. Each occurrence is recorded once; other owners link the same ID rather than re-run its effects. Resource effects are references to actual postings/abilities/inventory owners, not duplicated balances. Missing dates/time/source are explicit unknowns and cannot start deadlines or support guessed travel durations.

A candidate event needs an actual played scene or explicit campaign-time-advance source, plausible trigger and recorded action/outcome before it can be recorded. Proposal approval alone supplies no event. Future outcomes update their actual owners and chronicle only after occurring; no timer, writer, scheduler or automatic state engine is implemented. The candidate checker locates evidence, not independently proving truth or authorizing publication of secret outcomes.


```json
{
  "schema_version": 1,
  "chronicles": [
    {
      "reference_id": "chronicle:year847-day153-development",
      "source_ref": "changes/chronicles/year847-day153-development.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "reference_id": "chronicle:year847-day153-finances",
      "source_ref": "changes/chronicles/year847-day153-finances.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "reference_id": "chronicle:year847-day153-freight",
      "source_ref": "changes/chronicles/year847-day153-freight.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "reference_id": "chronicle:year847-day472-first-hour",
      "source_ref": "changes/chronicles/year847-day472-first-hour.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "reference_id": "chronicle:year848-day137-end-session",
      "source_ref": "changes/chronicles/year848-day137-end-session.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "reference_id": "chronicle:year848-day156-end-session",
      "source_ref": "changes/chronicles/year848-day156-end-session.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    }
  ],
  "event_fields": [
    "event_id",
    "date",
    "time",
    "location_id",
    "initiator_id",
    "participant_ids",
    "category",
    "trigger_ref",
    "action_ref",
    "outcome_ref",
    "affected_actor_ids",
    "affected_faction_ids",
    "quest_ids",
    "resource_effect_refs",
    "knowledge",
    "source_refs",
    "time_advance_ref"
  ],
  "new_events": [],
  "automatic_events": false
}
```
