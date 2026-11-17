---
id: route-caelthorne-rivermere
type: locations
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-01-geography-approval.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- changes/chronicles/world-geography-travel-design.md
---

# Caelthorne–Rivermere corridor proposal

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "start": "caelthorne",
  "destination": "rivermere",
  "bidirectional": true,
  "reverse_status": "PROPOSED",
  "intermediate_settlements": null,
  "road_name": null,
  "road_type": "southern road/river links",
  "distance": null,
  "durations": [
    {
      "mode": "wagon",
      "minimum": 3,
      "maximum": 5,
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
  "terrain": "southern road/river links",
  "road_condition": null,
  "known_hazards": null,
  "patrol_jurisdiction": null,
  "toll_requirements": null,
  "seasonal_restrictions": null,
  "last_verified_status": "PROPOSED corridor approved for design only; alignment, modes and current conditions unverified",
  "source_refs": [
    "archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md",
    "changes/chronicles/phase2-01-geography-approval.md"
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
      "target_id": "rivermere",
      "classification": "PROPOSED",
      "placement": "endpoint",
      "at_location": "rivermere"
    }
  ],
  "notes": "Reverse traversal is a planning default, not verified past travel. Reassess direction/conditions before departure. Null means UNKNOWN, never zero, free, safe or absent."
}
```

## Phase 2 corridor review

The player approves this connection as a proposed road/trade corridor. Existing JSON estimates remain proposed, not observations. Alignment and intermediate junctions remain unsurveyed. Walking, riding, wagon and caravan compatibility must be checked separately; an existing wagon estimate does not verify road width, bridges or current passability. Weather must be established before departure. Plan daylight travel, overnight rest, drinking water, animal feed and recovery without inventing fixed daily hours. Seasonal flood, snow and ground conditions require local verification. Road authority, crossing permission, possible toll liability and actual toll amounts remain UNKNOWN. No fee is charged or authority conferred. Do not route travelers until endpoints, intervening topology and mode are compatible.
