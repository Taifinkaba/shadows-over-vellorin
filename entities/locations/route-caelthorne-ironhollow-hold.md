---
id: route-caelthorne-ironhollow-hold
type: locations
status: research
visibility: gm-reference
source_refs:
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- changes/chronicles/world-geography-travel-design.md
---

# Caelthorne–Ironhollow Hold corridor proposal

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "start": "caelthorne",
  "destination": "ironhollow-hold",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": "western mountain roads",
  "distance": null,
  "durations": [
    {
      "mode": "wagon",
      "minimum": 4,
      "maximum": 6,
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
  "terrain": "western mountain roads",
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
      "target_id": "ironhollow-hold",
      "classification": "PROPOSED",
      "placement": "endpoint",
      "at_location": "ironhollow-hold"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```
