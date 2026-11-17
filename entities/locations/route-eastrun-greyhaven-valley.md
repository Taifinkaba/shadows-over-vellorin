---
id: route-eastrun-greyhaven-valley
type: locations
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-01-geography-approval.md
- changes/chronicles/world-geography-travel-design.md
- entities/factions/dragon-slayer-academy.md
---

# Eastrun–Greyhaven Valley connection proposal

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "start": "eastrun",
  "destination": "greyhaven-valley",
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
  "last_verified_status": "PROPOSED corridor approved for design only; alignment, modes and current conditions unverified",
  "source_refs": [
    "changes/chronicles/world-geography-travel-design.md",
    "entities/factions/dragon-slayer-academy.md",
    "changes/chronicles/phase2-01-geography-approval.md"
  ],
  "integration_points": [
    {
      "role": "destination future integration",
      "target_id": "greyhaven-valley",
      "classification": "PROPOSED",
      "placement": "endpoint",
      "at_location": "greyhaven-valley"
    },
    {
      "role": "independent academy; membership/access not granted",
      "target_id": "dragon-slayer-academy",
      "classification": "CONFIRMED CANON",
      "placement": "endpoint-service",
      "at_location": "greyhaven-valley"
    }
  ],
  "notes": "PROPOSED connector only: alignment, intermediates, transport, time and relationship to other routes UNKNOWN. Not an assertion of direct adjacency, site identity, existing road or a previously traveled path. Requires approval before use."
}
```

## Phase 2 corridor review

The player approves this connection as a proposed road/trade corridor. Existing JSON estimates remain proposed, not observations. Alignment and intermediate junctions remain unsurveyed. Walking, riding, wagon and caravan compatibility must be checked separately; an existing wagon estimate does not verify road width, bridges or current passability. Weather must be established before departure. Plan daylight travel, overnight rest, drinking water, animal feed and recovery without inventing fixed daily hours. Seasonal flood, snow and ground conditions require local verification. Road authority, crossing permission, possible toll liability and actual toll amounts remain UNKNOWN. No fee is charged or authority conferred. Do not route travelers until endpoints, intervening topology and mode are compatible.
