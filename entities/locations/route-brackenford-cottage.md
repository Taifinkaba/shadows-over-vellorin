---
id: route-brackenford-cottage
type: locations
status: canon
visibility: gm-reference
source_refs:
- entities/locations/brackenford.md
- entities/locations/briarstone-cottage.md
- changes/chronicles/world-geography-travel-design.md
---

# Western Mill Lane approach

```json
{
  "schema_version": 1,
  "classification": "CONFIRMED CANON",
  "start": "brackenford",
  "destination": "briarstone-cottage",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": "Western Mill Lane",
  "road_type": "village lane",
  "distance": null,
  "durations": [
    {
      "mode": "walking",
      "minimum": 8,
      "maximum": 8,
      "unit": "minutes",
      "qualifier": "Approximately8 minutes from village center; not from village boundary.",
      "basis": "historical-report",
      "source_ref": "entities/locations/brackenford.md",
      "source_quote": "~8 minutes walk from village center"
    }
  ],
  "accessibility": {
    "walking": true,
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
    "entities/locations/brackenford.md",
    "entities/locations/briarstone-cottage.md"
  ],
  "integration_points": [
    {
      "role": "market/Willow Lantern inn and local watch directory",
      "target_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "brackenford"
    },
    {
      "role": "private property, no public rest entitlement",
      "target_id": "briarstone-cottage",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint",
      "at_location": "briarstone-cottage"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```
