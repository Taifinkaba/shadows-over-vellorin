---
id: route-caelthorne-mount-vaelspire
type: locations
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/world-geography-travel-design.md
- entities/locations/hollow-veil.md
---

# Caelthorne–Vaelspire northern approach proposal

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "start": "caelthorne",
  "destination": "mount-vaelspire",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": null,
  "distance": null,
  "durations": [],
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
  "last_verified_status": "PROPOSED; no field verification or player approval",
  "source_refs": [
    "changes/chronicles/world-geography-travel-design.md",
    "entities/locations/hollow-veil.md"
  ],
  "integration_points": [
    {
      "role": "destination future integration",
      "target_id": "mount-vaelspire",
      "classification": "PROPOSED",
      "placement": "endpoint",
      "at_location": "mount-vaelspire"
    },
    {
      "role": "sanctuary/dungeon-entrance integration; exact approach UNKNOWN",
      "target_id": "hollow-veil",
      "classification": "CONFIRMED CANON",
      "placement": "unlocated",
      "at_location": null
    }
  ],
  "notes": "PROPOSED connector only: alignment, intermediates, transport, time and relationship to other routes UNKNOWN. Not an assertion of direct adjacency, site identity, existing road or a previously traveled path. Requires approval before use."
}
```
