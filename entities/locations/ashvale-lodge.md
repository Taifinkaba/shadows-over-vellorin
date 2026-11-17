---
id: ashvale-lodge
type: locations
status: canon
visibility: gm-reference
source_refs:
- archive/session-handoffs/year847-day153-user-handoff.txt
- archive/session-handoffs/year847-day472-user-handoff.txt
---

# Ashvale Lodge

Operating lodge developed from basic lodging/stables through fully completed and paid Phase I: guest rooms, kitchen, secure storage, stable repairs, removable merchant stalls and road access. Forge/workshop72gp, research room28gp and training courtyard18gp signed and paid; facilities accepted by Day137. Forge performs actual paid repair jobs. Services: rooms, meals, stabling, market rental and forge work.

Tomas: steward/accounting; Bren: construction/maintenance. Adult housekeeper, kitchen assistant, adult stable worker and part-time bookkeeper hired/trialed; wages included in operating ledger. Exact individual names, rates and unpaid future obligations unspecified; continue staffing costs, not free labor.

Youth helpers from Briarfall children’s home: **Mira15, Joren16, Elsi14**, retained here as staff to avoid confusing Mira with academy student Mira Thorne. Tasks optional, supervised, safe, light and paid; shelter, meals and schooling not conditional on work. No hazardous, forge or night work.

Restricted development chest under Tomas with Theron override:0gp, approved construction paid. Separate operating till61gp8sp; private emergency chest30gp accessible only to Theron; expedition reserve155gp2sp separately earmarked. See [party finances](../mechanics/party-finances.md). The handoff does not explicitly identify this developed lodge with the older hidden woodland lodge; no exact site equivalence, new route or relocation is inferred.

## Authoritative update — Year 847 Day 472, 16:10, session ENDED

Estate commercial lodge and natural Healing Springs operate under Tomas; see [estate](ashvale-estate.md) for current policy. Historical completed construction remains preserved; no newly posted revenue, expansion payment or guaranteed profit.


## Character reference retrieval

Player-approved visual/personality reference sheets: [Bren](../characters/bren.md), [Mira — lodge helper](../characters/mira-lodge-helper.md), [Joren](../characters/joren.md), [Elsi](../characters/elsi.md). These designs do not change staffing terms, wages or historical ages.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "ashvale-lodge",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": null,
  "settlement_type": "lodge property",
  "population": null,
  "government": null,
  "principal_official_id": null,
  "watch": null,
  "watch_official_id": null,
  "court": null,
  "route_ids": [
    "route-ashvale-estate-ashvale-lodge"
  ],
  "neighborhoods": null,
  "nearby_location_ids": [],
  "institutions": [],
  "service_links": [
    "ashvale-estate:market"
  ],
  "local_problem_refs": [],
  "notes": "Market/stall rental routes to the estate venue record; exact premises relationship not expanded. Hospitality is one rooms/meals/stabling business, not three duplicate shops. Hidden woodland lodge identity remains UNKNOWN.",
  "source_refs": [
    "entities/locations/ashvale-lodge.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/ashvale-lodge.md",
      "quote": "Services: rooms, meals, stabling, market rental and forge work."
    }
  ],
  "businesses": [
    {
      "id": "ashvale-lodge:hospitality",
      "name": "Ashvale Lodge",
      "display_label": "Ashvale Lodge hospitality",
      "parent_location_id": "ashvale-lodge",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "inn",
        "stable"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [
        "bren",
        "mira-lodge-helper",
        "joren",
        "elsi"
      ],
      "staff_notes": "Bren: construction/maintenance, not reassigned to hospitality. Adult housekeeper, kitchen assistant, stable worker and part-time bookkeeper are unnamed. Youth helpers retain optional supervised safe light paid work; shelter/meals/schooling unconditional, no hazardous/forge/night work. Individual tasks/wages unknown.",
      "services": [
        "Rooms",
        "Meals",
        "Stabling"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [
        "common-bed",
        "private-room",
        "meal",
        "stable-feed"
      ],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-lodge.md",
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-lodge.md",
          "quote": "Services: rooms, meals, stabling, market rental and forge work."
        },
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "Theron owns the estate and commercial buildings, including lodge"
        },
        {
          "source_ref": "entities/characters/tomas.md",
          "quote": "Later established as Ashvale Lodge steward and accountant."
        },
        {
          "source_ref": "entities/characters/tomas.md",
          "quote": "Independently manages estate operations."
        }
      ],
      "automatic_financial_postings": false
    },
    {
      "id": "ashvale-lodge:forge",
      "name": null,
      "display_label": "Lodge forge/workshop",
      "parent_location_id": "ashvale-lodge",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "blacksmith"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Existing paid repair jobs; commission availability UNKNOWN"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [
        {
          "kind": "historically-paid",
          "item": "Forge/workshop construction",
          "minimum_cp": 7200,
          "maximum_cp": 7200,
          "unit": "completed construction",
          "source_ref": "entities/locations/ashvale-lodge.md",
          "source_quote": "Forge/workshop72gp",
          "note": "Already paid; not a repair quote or new charge."
        }
      ],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-lodge.md",
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-lodge.md",
          "quote": "Forge performs actual paid repair jobs."
        },
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "Theron owns the estate and commercial buildings, including lodge"
        },
        {
          "source_ref": "entities/characters/tomas.md",
          "quote": "Later established as Ashvale Lodge steward and accountant."
        },
        {
          "source_ref": "entities/characters/tomas.md",
          "quote": "Independently manages estate operations."
        }
      ],
      "automatic_financial_postings": false
    }
  ],
  "territory_id": null
}
```
