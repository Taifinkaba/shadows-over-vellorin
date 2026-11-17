---
id: world-geography
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-01-geography-approval.md
- changes/chronicles/world-geography-travel-design.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- archive/legacy-modules/world/03-3-world-map-and-regions.md
- entities/locations/brackenford.md
- entities/locations/hollow-first-hour.md
- entities/locations/hollow-veil.md
- changes/chronicles/phase2-02-settlement-approval.md
---

# Geographic hierarchy and location directory

This directory is an authoritative routing/classification record, not approval of every node or edge. CONFIRMED CANON classifies established identity only, not every archived description. Empty parents mean UNKNOWN placement. A proposed parent edge never inherits canon from either endpoint. No exact coordinates or new borders.

Hierarchy supports continent → territory/nation → region/province → city/town/village/hamlet → property/site. Missing layers stay absent. APPROVED DESIGN distinguishes player-approved fictional geography from historical observations; it does not certify current conditions or Theron’s knowledge. Realm nodes use kind territory. Elyndor and Frostmarch now have approved realm identities. Province, hamlet and entrance detail can be added only with sources. Existing dungeon sites have no newly surveyed entrance coordinates.

The following single JSON block owns directory membership and containment edges. Location entities own site facts; route entities own road data. All existing location IDs are reused. Greyhaven Mill/Valley and the two Hollows remain distinct; the hidden woodland lodge has no asserted identity with Ashvale Lodge. Known Brackenford streets/services remain in Brackenford, not duplicated as new settlements.

```json
{
  "schema_version": 1,
  "nodes": [
    {
      "id": "ashvale-estate",
      "kind": "property",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "blackthorn-watch",
      "kind": "watch-station",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "mount-vaelspire",
      "kind": "landmark",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "greyhaven-mill",
      "kind": "landmark",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "eastrun",
      "kind": "settlement",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "briarfall-crossing",
      "kind": "settlement",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "caelthorne",
      "kind": "city",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "valedorn",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "ninth-vault",
      "kind": "dungeon-site",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "mirror-foundation",
      "kind": "dungeon-site",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "frostspire-peaks",
      "kind": "wilderness",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "hollow-veil",
      "kind": "sanctuary",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "mount-vaelspire",
          "classification": "CONFIRMED CANON",
          "source_refs": [
            "entities/locations/hollow-veil.md"
          ]
        }
      ]
    },
    {
      "id": "ashvale-lodge",
      "kind": "property",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "northern-freight-enclosure",
      "kind": "landmark",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "greyhaven-valley",
      "kind": "region",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "hollow-first-hour",
      "kind": "dungeon-site",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "mount-elarion",
          "classification": "CONFIRMED CANON",
          "source_refs": [
            "entities/locations/hollow-first-hour.md"
          ]
        }
      ]
    },
    {
      "id": "north-return-house",
      "kind": "landmark",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "briarstone-cottage",
      "kind": "property",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "brackenford",
          "classification": "CONFIRMED CANON",
          "source_refs": [
            "entities/locations/brackenford.md"
          ]
        }
      ]
    },
    {
      "id": "brackenford",
      "kind": "village",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "northern-marches",
          "classification": "CONFIRMED CANON",
          "source_refs": [
            "entities/locations/brackenford.md"
          ]
        }
      ]
    },
    {
      "id": "aethoria",
      "kind": "continent",
      "classification": "PROPOSED",
      "parents": []
    },
    {
      "id": "vellorin",
      "kind": "territory",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "aethoria",
          "classification": "PROPOSED",
          "source_refs": [
            "changes/chronicles/world-geography-travel-design.md"
          ]
        }
      ]
    },
    {
      "id": "northern-marches",
      "kind": "region",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "vellorin",
          "classification": "CONFIRMED CANON",
          "source_refs": [
            "entities/locations/brackenford.md"
          ]
        }
      ]
    },
    {
      "id": "blackthorn-north-waystation",
      "kind": "watch-station",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "ironhollow-hold",
      "kind": "settlement",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "ironhollow-holds",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "rivermere",
      "kind": "settlement",
      "classification": "CONFIRMED CANON",
      "parents": [
        {
          "id": "rivermere-league",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "elyndor",
      "kind": "territory",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "frostmarch",
      "kind": "territory",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "mount-elarion",
      "kind": "landmark",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "seven-bells-witness-entry",
      "kind": "dungeon-entrance",
      "classification": "CONFIRMED CANON",
      "parents": []
    },
    {
      "id": "valedorn",
      "kind": "territory",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "ironhollow-holds",
      "kind": "territory",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "rivermere-league",
      "kind": "territory",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-01-geography-approval.md"
          ]
        }
      ]
    },
    {
      "id": "silverbrook",
      "kind": "village",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-02-settlement-approval.md"
          ]
        }
      ]
    },
    {
      "id": "stoneford",
      "kind": "settlement",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-02-settlement-approval.md"
          ]
        }
      ]
    },
    {
      "id": "southbank-landing",
      "kind": "settlement",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-02-settlement-approval.md"
          ]
        }
      ]
    },
    {
      "id": "windmere",
      "kind": "village",
      "classification": "APPROVED DESIGN",
      "parents": [
        {
          "id": "vellorin",
          "classification": "APPROVED DESIGN",
          "source_refs": [
            "changes/chronicles/phase2-02-settlement-approval.md"
          ]
        }
      ]
    }
  ]
}
```
