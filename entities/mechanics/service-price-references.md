---
id: service-price-references
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/settlements-businesses-services-design.md
- archive/legacy-modules/world/05-5-economy-and-prices.md
- changes/chronicles/phase2-02-settlement-approval.md
---

# Service price distinctions and reference routing

No new prices are enacted. The current examples are PROPOSED archived reference bands, not player-approved prices. Current quotes and counted stock remain UNKNOWN. Business historical paid costs stay with their parent and never become charges. Accepted coin/exchange/credit policy at each merchant is independently unknown; global denomination conversion does not promise acceptance.

```json
{
  "schema_version": 1,
  "currency": {
    "cp_per_gp": 100,
    "cp_per_sp": 10
  },
  "price_kinds": [
    "historically-paid",
    "current-verified-quote",
    "approved-reference",
    "proposed-regional-estimate"
  ],
  "reference_bands": [
    {
      "id": "simple-food",
      "item": "Bread, vegetables, simple daily food",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 2,
      "maximum_cp": 5,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Bread, vegetables, simple daily food | 2–5 cp |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    },
    {
      "id": "meal",
      "item": "Hearty tavern meal",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 10,
      "maximum_cp": 30,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Hearty tavern meal | 1–3 sp |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    },
    {
      "id": "common-bed",
      "item": "Common inn bed, night",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 30,
      "maximum_cp": 70,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Common inn bed, night | 3–7 sp |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    },
    {
      "id": "private-room",
      "item": "Private inn room, night",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 100,
      "maximum_cp": 200,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Private inn room, night | 1–2 gp |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    },
    {
      "id": "stable-feed",
      "item": "Horse stable/feed, night",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 10,
      "maximum_cp": 30,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Horse stable/feed, night | 1–3 sp per horse |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    },
    {
      "id": "healing-herbs",
      "item": "Common healing herbs/bandages",
      "kind": "proposed-regional-estimate",
      "classification": "PROPOSED",
      "minimum_cp": 20,
      "maximum_cp": 80,
      "unit": "Source reference unit; see item wording",
      "source_ref": "archive/legacy-modules/world/05-5-economy-and-prices.md",
      "source_quote": "| Common healing herbs/bandages | 2–8 sp |",
      "note": "Archived LOCKED DESIGN reference band; not approved here, not a merchant quote or paid purchase."
    }
  ],
  "automatic_financial_postings": false,
  "approved_references": [
    {
      "id": "simple-bed",
      "item": "Simple inn bed",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 50,
      "maximum_cp": 50,
      "unit": "night",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "private-room",
      "item": "Private inn room",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 100,
      "maximum_cp": 100,
      "unit": "night",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "hot-meal",
      "item": "Hot meal",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 20,
      "maximum_cp": 20,
      "unit": "meal",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "horse-feed",
      "item": "Horse stabling/feed",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 30,
      "maximum_cp": 30,
      "unit": "day",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "rations",
      "item": "Travel rations",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 50,
      "maximum_cp": 50,
      "unit": "day",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "healing-herbs",
      "item": "Basic healing herbs",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 80,
      "maximum_cp": 80,
      "unit": "bundle",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "rope",
      "item": "Rope",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 100,
      "maximum_cp": 100,
      "unit": "50 feet",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "iron-sword",
      "item": "Standard iron sword",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 800,
      "maximum_cp": 800,
      "unit": "sword",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "wagon-hire",
      "item": "Local wagon hire excluding driver/feed",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 80,
      "maximum_cp": 80,
      "unit": "day",
      "reference_type": "price",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "farm-labor",
      "item": "Farm laborer",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 20,
      "maximum_cp": 20,
      "unit": "day",
      "reference_type": "wage",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "caravan-guard",
      "item": "Caravan guard",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 50,
      "maximum_cp": 50,
      "unit": "day",
      "reference_type": "wage",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "skilled-blacksmith",
      "item": "Skilled blacksmith",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 60,
      "maximum_cp": 60,
      "unit": "day",
      "reference_type": "wage",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "experienced-healer",
      "item": "Experienced healer",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 80,
      "maximum_cp": 80,
      "unit": "day",
      "reference_type": "wage",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    {
      "id": "master-artisan",
      "item": "Master artisan",
      "kind": "approved-reference",
      "classification": "APPROVED DESIGN",
      "minimum_cp": 100,
      "maximum_cp": 200,
      "unit": "day",
      "reference_type": "wage",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    }
  ]
}
```

## Phase 2 interpretation

The approved_references table now supplies prospective settlement baselines. The preceding six archival bands retain their original classifications, units and evidence. Use an actual existing contract or verified quote first; otherwise distinguish the approved baseline from the archived range. Skilled blacksmith6sp/day is a specific approved role reference, while the older1–3gp/day skilled-craft band remains unapproved broader design. Stabling/feed is per day here and per night in the older band; do not silently equate periods. No tariff, wages owed, quote or transaction is enacted. Full economic reconciliation remains PR6.
