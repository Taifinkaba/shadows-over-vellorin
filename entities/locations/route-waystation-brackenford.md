---
id: route-waystation-brackenford
type: locations
status: canon
visibility: gm-reference
source_refs:
- entities/locations/brackenford.md
- changes/chronicles/world-geography-travel-design.md
---

# Northern-road village branch

```json
{
  "schema_version": 1,
  "classification": "CONFIRMED CANON",
  "start": "blackthorn-north-waystation",
  "destination": "brackenford",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": "village branch of northern road",
  "distance": null,
  "durations": [
    {
      "mode": "wagon",
      "minimum": 35,
      "maximum": 35,
      "unit": "minutes",
      "qualifier": "Approximately35 minutes by wagon; source estimate.",
      "basis": "historical-report",
      "source_ref": "entities/locations/brackenford.md",
      "source_quote": "~35 minutes by wagon"
    }
  ],
  "accessibility": {
    "walking": null,
    "riding": null,
    "wagon": true,
    "caravan": null
  },
  "terrain": null,
  "road_condition": null,
  "known_hazards": null,
  "patrol_jurisdiction": null,
  "toll_requirements": null,
  "seasonal_restrictions": null,
  "last_verified_status": "Historical source only; present road status UNKNOWN",
  "source_refs": [
    "entities/locations/brackenford.md"
  ],
  "integration_points": [
    {
      "role": "reeve/watch and political jurisdiction details",
      "target_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "brackenford"
    },
    {
      "role": "watch station",
      "target_id": "blackthorn-north-waystation",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "blackthorn-north-waystation"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```
