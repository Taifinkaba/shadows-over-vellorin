---
id: travel-routes
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year853-day52.md
- changes/chronicles/world-geography-travel-design.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
---

# Road and route registry

## Year 853 Day 52

Preserve the expedition's played arrival at Westbridge.

### Newly surveyed itinerary

Hollow Veil, Mount Vaelspire → mountain descent → regional trade roads → Caelthorne → Westbridge.

The journey, contracts, rest and supply activities occupied seven days.

This is an observed combined expedition interval, not a universal certified travel duration.

Update existing proposed corridors only to the extent supported by played observation and the approved reconciliation.

Do not invent:

- Precise mileage.
- Named intermediate roads.
- Additional settlements.
- Permanent wagon accessibility across every segment.
- Toll requirements.
- Patrol jurisdiction.
- Seasonal closures.
- Standard reverse-travel durations.

Preserve unknown route fields.

Maintain distinct geographic locations:

1. Aric's ancestral Ashvale Estate.
2. Theron's Commercial Estate.
3. Ashvale Lodge and relevant commercial facilities.
4. Ashvale Grand Arena.
5. DSI Academy in Greyhaven Valley.
6. Hollow Veil at Mount Vaelspire.
7. Observatory of First Light.
8. Forgotten Watchpost.
9. Westbridge.
10. Mirror Foundation.
11. Mirror Repository.

Do not make DSI part of Theron's commercial estate.

Travel between distinct locations must occur through gameplay.

Routing only: follow each ID through index.json. Road entities are the sole owners of road facts. CONFIRMED CANON route data records limited historical information, never current safety. PROPOSED corridors are excluded from canonical navigation until approved; disconnected canon is intentional where evidence is missing. Bidirectional is a planning default; reverse_status retains whether reverse travel is confirmed. No reverse historical journey is manufactured.

```json
{
  "schema_version": 1,
  "route_ids": [
    "route-ashvale-eastrun",
    "route-eastrun-briarfall",
    "route-waystation-brackenford",
    "route-brackenford-cottage",
    "route-caelthorne-ashvale-estate",
    "route-caelthorne-eastrun",
    "route-caelthorne-briarfall-crossing",
    "route-caelthorne-blackthorn-watch",
    "route-caelthorne-ironhollow-hold",
    "route-caelthorne-rivermere",
    "route-caelthorne-frostspire-peaks",
    "route-ashvale-estate-ashvale-lodge",
    "route-eastrun-greyhaven-mill",
    "route-eastrun-greyhaven-valley",
    "route-blackthorn-watch-blackthorn-north-waystation",
    "route-caelthorne-mount-vaelspire",
    "route-caelthorne-elyndor",
    "route-caelthorne-frostmarch",
    "route-northern-marches-frostmarch",
    "route-elyndor-woodland-passage"
  ]
}
```
