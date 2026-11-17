---
id: service-price-references
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/settlements-businesses-services-design.md
- archive/legacy-modules/world/05-5-economy-and-prices.md
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
  "automatic_financial_postings": false
}
```
