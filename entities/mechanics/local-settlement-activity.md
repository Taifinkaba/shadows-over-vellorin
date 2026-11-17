---
id: local-settlement-activity
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/settlements-businesses-services-design.md
---

# Local activity categories and retrieval boundary

Lightweight category framework only, not an event feed, clock or job board of actual offers. Categories do not establish any shortage, crime, disaster, festival, injury, demand, completed contract or reward. Existing work must be sourced through its original owner/quest record with knowledge review before showing it to the player. No offscreen progression; detailed autonomy remains deferred to Chunk8.

```json
{
  "schema_version": 1,
  "categories": [
    "merchant-dispute",
    "missing-supplies",
    "road-damage",
    "bandit-complaint",
    "seasonal-shortage",
    "labor-shortage",
    "local-festival",
    "construction-request",
    "guild-recruitment",
    "medical-emergency"
  ],
  "events": [],
  "automatic_progression": false
}
```
