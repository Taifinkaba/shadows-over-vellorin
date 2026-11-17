---
id: travel-routes
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/world-geography-travel-design.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
---

# Road and route registry

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
