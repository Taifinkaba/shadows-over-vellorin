---
id: brackenford
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year848-day156-end-session.md
---

# Brackenford — Day156 current canon

Briarstone Cottage, 7 Western Mill Lane, Brackenford, Northern Marches, Vellorin. Formerly Edrick Sorn's private property, House Ashvale owns after Year848 Suncrest34 Day154 restitution. 1.4 acres, appraised55gp noncash, two-story stone/timber house, 2 bedrooms, kitchen, sitting room, pantry, loft, storehouse, woodshed, fenced pasture, garden, 6 apple trees, well and millstream access. Vacant, habitable, minor repairs needed, no rent yet, ownership no village-government rights.
Brackenford: approx180 residents, 42 households, ~35 minutes by wagon from Blackthorn North Waystation along northern-road village branch; cottage ~8 minutes walk from village center on Western Mill Lane. Bracken River, village stone bridge, market, watermill, forge, inn, farms. Village government reeve and council. Reeve Elsbeth Marrin52 human. Blacksmith Borin Emberhand68 dwarf. Innkeeper Mara Fenwick41 human of Willow Lantern six-room inn. Herbalist Seren Willowmere29 elf. Miller Harlan Wicks57 human western neighbor. Watch captain Ressa Vale45 human with six part-time watch members. Eastern neighbor widow Alda Perrin66 and grandson Corin14 (not equated to North Return House Perrin). North birch copse; south village grazing association pasture; west watermill/millstream. Cottage built Year786 by Edwin and Mara Briar; road expansion Year817; Sorn purchased Year837 and occasionally used for military correspondence; House Ashvale acquired Year848. Old built-in correspondence compartment currently empty by transfer inspection, marks/history uninvestigated. Possible AV-07 lead via historic visitors, inn ledgers, miller; no automatic secrets found or free income. All named residents autonomous.


House Ashvale cottage ownership grants no village-government rights. Named residents are independently indexed characters.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "brackenford",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": "northern-marches",
  "settlement_type": "village",
  "population": {
    "amount": 180,
    "qualifier": "approximately"
  },
  "government": "Reeve and council",
  "principal_official_id": "elsbeth-marrin",
  "watch": "Watch captain and six part-time watch members",
  "watch_official_id": "ressa-vale",
  "court": null,
  "route_ids": [
    "route-waystation-brackenford",
    "route-brackenford-cottage"
  ],
  "neighborhoods": [
    "Western Mill Lane (street, not an invented district)"
  ],
  "nearby_location_ids": [
    "briarstone-cottage",
    "blackthorn-north-waystation"
  ],
  "institutions": [
    {
      "kind": "reeve",
      "label": "Reeve and village council",
      "entity_id": "elsbeth-marrin",
      "classification": "CONFIRMED CANON"
    },
    {
      "kind": "watch",
      "label": "Watch captain, six part-time members",
      "entity_id": "ressa-vale",
      "classification": "CONFIRMED CANON"
    }
  ],
  "service_links": [],
  "local_problem_refs": [],
  "notes": "UNKNOWN fields are not absent services. Site/property entry is not a newly declared town. Current availability and exact locations require in-play verification.",
  "source_refs": [
    "entities/locations/brackenford.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/brackenford.md",
      "quote": "Village government reeve and council."
    }
  ],
  "businesses": [
    {
      "id": "brackenford:willow-lantern",
      "name": "Willow Lantern",
      "display_label": "Willow Lantern",
      "parent_location_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "inn"
      ],
      "owner_id": null,
      "manager_id": null,
      "operator_id": "mara-fenwick",
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Accommodation"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": {
        "unit": "rooms",
        "amount": 6
      },
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [
        "private-room",
        "common-bed"
      ],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": "Year848 Suncrest36 Day156",
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Innkeeper Mara Fenwick41 human of Willow Lantern six-room inn."
        }
      ],
      "automatic_financial_postings": false
    },
    {
      "id": "brackenford:forge",
      "name": null,
      "display_label": "Brackenford forge / blacksmith service",
      "parent_location_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "blacksmith"
      ],
      "owner_id": null,
      "manager_id": null,
      "operator_id": "borin-emberhand",
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Blacksmith services; specific commissions UNKNOWN"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": "Year848 Suncrest36 Day156",
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Blacksmith Borin Emberhand68 dwarf."
        }
      ],
      "automatic_financial_postings": false
    },
    {
      "id": "brackenford:herbalist",
      "name": null,
      "display_label": "Brackenford herbalist service",
      "parent_location_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "herbalist"
      ],
      "owner_id": null,
      "manager_id": null,
      "operator_id": "seren-willowmere",
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Herbalist advice; treatment scope UNKNOWN"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [
        "healing-herbs"
      ],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": "Year848 Suncrest36 Day156",
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Herbalist Seren Willowmere29 elf."
        }
      ],
      "automatic_financial_postings": false
    },
    {
      "id": "brackenford:watermill",
      "name": null,
      "display_label": "Brackenford watermill",
      "parent_location_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "milling"
      ],
      "owner_id": null,
      "manager_id": null,
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": "Local miller Harlan Wicks is recorded separately; assignment to this specific mill and ownership not proven.",
      "services": [
        "Mill premises; public milling terms UNKNOWN"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": "Year848 Suncrest36 Day156",
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Bracken River, village stone bridge, market, watermill, forge, inn, farms."
        }
      ],
      "automatic_financial_postings": false
    },
    {
      "id": "brackenford:market",
      "name": null,
      "display_label": "Brackenford market",
      "parent_location_id": "brackenford",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "food-market"
      ],
      "owner_id": null,
      "manager_id": null,
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Market venue; specific vendors/goods UNKNOWN"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": "Year848 Suncrest36 Day156",
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Bracken River, village stone bridge, market, watermill, forge, inn, farms."
        }
      ],
      "automatic_financial_postings": false
    }
  ],
  "territory_id": "vellorin"
}
```
