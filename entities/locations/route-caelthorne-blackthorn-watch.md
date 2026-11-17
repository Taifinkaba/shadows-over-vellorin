---
id: route-caelthorne-blackthorn-watch
type: locations
status: research
visibility: gm-reference
source_refs:
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- changes/chronicles/world-geography-travel-design.md
---

# Caelthorne–Blackthorn Watch corridor proposal

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "start": "caelthorne",
  "destination": "blackthorn-watch",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": "northeastern roads",
  "distance": null,
  "durations": [
    {
      "mode": "wagon",
      "minimum": 3,
      "maximum": 4,
      "unit": "days",
      "qualifier": "One-way laden wagon, ordinary weather; rest schedule not specified. Not convertible to an exact hourly distance.",
      "basis": "proposed-estimate"
    }
  ],
  "accessibility": {
    "walking": null,
    "riding": null,
    "wagon": null,
    "caravan": null
  },
  "terrain": "northeastern roads",
  "road_condition": null,
  "known_hazards": null,
  "patrol_jurisdiction": null,
  "toll_requirements": null,
  "seasonal_restrictions": null,
  "last_verified_status": "PROPOSED; no field verification or player approval",
  "source_refs": [
    "archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md"
  ],
  "integration_points": [
    {
      "role": "magistrates/watch; court/prison directory pending",
      "target_id": "caelthorne",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "caelthorne"
    },
    {
      "role": "guild hall location unresolved within endpoint",
      "target_id": "wayfarers-guild",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint-service",
      "at_location": "caelthorne"
    },
    {
      "role": "destination services and access",
      "target_id": "blackthorn-watch",
      "classification": "PROPOSED",
      "placement": "endpoint",
      "at_location": "blackthorn-watch"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```
