---
id: route-ashvale-eastrun
type: locations
status: canon
visibility: gm-reference
source_refs:
- entities/locations/eastrun.md
- entities/locations/ashvale-estate.md
- changes/chronicles/world-geography-travel-design.md
---

# Ashvale Estate–Eastrun road

```json
{
  "schema_version": 1,
  "classification": "CONFIRMED CANON",
  "start": "ashvale-estate",
  "destination": "eastrun",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": "road",
  "distance": null,
  "durations": [
    {
      "mode": "unknown",
      "minimum": 120,
      "maximum": null,
      "unit": "minutes",
      "qualifier": "A little over two hours; mode unspecified; 120 is a strict lower bound, not an exact duration.",
      "basis": "historical-report",
      "source_ref": "entities/locations/eastrun.md",
      "source_quote": "a little over two hours"
    }
  ],
  "accessibility": {
    "walking": null,
    "riding": null,
    "wagon": null,
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
    "entities/locations/eastrun.md",
    "entities/locations/ashvale-estate.md"
  ],
  "integration_points": [
    {
      "role": "market/rest services",
      "target_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "ashvale-estate"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```
