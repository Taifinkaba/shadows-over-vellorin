---
id: ashvale-estate
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year853-day145-reconciliation.md
- changes/chronicles/year852-day365-end-session.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- archive/legacy-modules/codex/10-v1-4-reconciliation-of-roster-routes-and-evidence-out-of-world.md
- archive/legacy-modules/codex/03-system-3-quests-consequences-faction-clocks.md
- archive/legacy-modules/codex/11-v1-5-final-cross-session-verification-audit-out-of-world-no-gamep.md
- archive/session-handoffs/year847-day472-user-handoff.txt
- changes/chronicles/year848-day137-end-session.md
- changes/chronicles/year848-day156-end-session.md
---

## Year 853 Day 145 reconciliation

Ancestral property distinct from Theron’s Commercial Estate. Family recovered a supplementary Expedition 47-B witness record here on Day 64.

## Earlier and standing records

# Ashvale Estate — Day156 current canon

Final checkpoint Year848 Suncrest36 Day156,20:15 in family sitting room; session ENDED. Party home, family safe, no injuries/deaths. Aric and mother informed on return. Expansion317gp committed/unpaid; no construction or cash transfer on commitment. House Ashvale separately owns Briarstone Cottage since Day154; no rent yet. New operating surplus69gp posted once; no automatic income.


## Historical record before Day156 (superseded only where explicit above)


# Ashvale Estate — Day137 session end

Year848 Suncrest17 Day137,09:30: Theron at Ashvale Estate; session ENDED. Halden Marr rescued, free and voluntarily protected here. Lyra continues his care and Healing Springs research. Tomas independently manages estate operations. No construction completion supplied.

The player-approved eight-period operating reconstruction is current financial canon, qualified as a continuity reconstruction rather than discovered receipts. [Current finances](../mechanics/party-finances.md) and [integer-copper ledger](../../state/finance-ledger.json) contain revenue270gp/period, expenses205gp/period, surplus65gp/period and the once-only520gp distribution. Future actual periods require Tomas receipts and expense records or another explicit player-approved accounting ruling. No automatic monthly65gp award. Historical120 acres/252gp purchase is already paid; proposed317gp expansion remains unspent. Operating till100gp remains policy, not additional cash.

## Historical record through Day124 (superseded where explicit above)


# Ashvale Estate

Theron owns the estate and commercial buildings, including lodge and additional120-acre expansion acquired for recorded252gp. Privately managed commercial settlement, no separate municipal charter. Tomas operates independently with autonomous daily activity and weekly reporting; no invented revenue or guaranteed profit.

Operations: lodge and natural Healing Springs;22% contractual fee on participating merchants’ on-site gross sales;20 merchant storage bays; rental cottages; bakery, market, nighttime entertainment, caravan facilities; Lantern Exchange for paid intelligence, verified trade reports and private meetings; guards, warehouse staff, overnight security and public facilities. Operating till floor100gp is a policy, not a verified cash balance.

Verified distributable free surplus allocation: general treasury25%, emergency15%, monthly operating15%, savings10%, expedition10%, development10%, research5%, Theron purse5%, Blackscale private5% (total100%). Do not apply percentages to gross receipts or book income without Tomas accounting.

## Historical record through Day 153 (superseded where corrected above)

# Ashvale Estate

Aric and Theron’s mother at home; legitimate family contact and smith commission records. Ashvale Estate to Eastrun historically a little over two hours by road.


## Character reference retrieval

Character references: [Theron's mother](../characters/therons-mother.md), [Halden Marr](../characters/halden-marr.md), [Serrik Vale](../characters/serrik-vale.md). New visual design does not establish genealogy, an additional arrival or a financial event.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "ashvale-estate",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": null,
  "settlement_type": "private estate / commercial settlement",
  "population": null,
  "government": "Private stewardship under Crown law; no separate municipal charter",
  "principal_official_id": null,
  "watch": null,
  "watch_official_id": null,
  "court": null,
  "route_ids": [
    "route-ashvale-eastrun",
    "route-caelthorne-ashvale-estate",
    "route-ashvale-estate-ashvale-lodge"
  ],
  "neighborhoods": null,
  "nearby_location_ids": [
    "eastrun"
  ],
  "institutions": [],
  "service_links": [
    "ashvale-lodge:hospitality",
    "ashvale-lodge:forge"
  ],
  "local_problem_refs": [],
  "notes": "Ownership is not municipal authority. Tomas management, paid construction,22% eligible merchant fee and finance allocations remain in original sources. No cash, rents, wages, income or expansion payment posted.",
  "source_refs": [
    "entities/locations/ashvale-estate.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/ashvale-estate.md",
      "quote": "Privately managed commercial settlement, no separate municipal charter."
    }
  ],
  "businesses": [
    {
      "id": "ashvale-estate:healing-springs",
      "name": null,
      "display_label": "Natural Healing Springs",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "healer"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Natural springs; certified treatment effects and public access UNKNOWN"
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
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "Operations: lodge and natural Healing Springs;"
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
      "id": "ashvale-estate:merchant-storage",
      "name": null,
      "display_label": "Merchant storage bays",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "storage"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Merchant storage premises"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": {
        "unit": "storage-bays",
        "amount": 20
      },
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "20 merchant storage bays;"
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
      "id": "ashvale-estate:rental-cottages",
      "name": null,
      "display_label": "Estate rental cottages",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "inn"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Rental accommodation; occupancy UNKNOWN"
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
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "rental cottages; bakery, market, nighttime entertainment, caravan facilities;"
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
      "id": "ashvale-estate:bakery",
      "name": null,
      "display_label": "Estate bakery",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "food-market"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Bakery service; specific stock UNKNOWN"
      ],
      "goods_categories": [
        "Baked goods; no counted inventory"
      ],
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": null,
      "prices": [],
      "price_reference_ids": [
        "simple-food"
      ],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "rental cottages; bakery, market, nighttime entertainment, caravan facilities;"
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
      "id": "ashvale-estate:market",
      "name": null,
      "display_label": "Estate market and merchant stalls",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "food-market"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Market/stall rental venue; vendors retain their goods"
      ],
      "goods_categories": null,
      "stock_counts": null,
      "capacity": null,
      "schedule": null,
      "accepted_currency": null,
      "payment_practices": "Existing22% contractual fee on participating merchants’ on-site gross sales. No booking of receipts; merchant goods are not estate inventory.",
      "prices": [],
      "price_reference_ids": [],
      "supplier_relationships": [],
      "existing_contracts": null,
      "licenses": null,
      "operational_status": "Established service/facility in source; current availability UNKNOWN",
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "rental cottages; bakery, market, nighttime entertainment, caravan facilities;"
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
      "id": "ashvale-estate:lantern-exchange",
      "name": "Lantern Exchange",
      "display_label": "Lantern Exchange",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "exchange"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Paid intelligence, verified trade reports and private meetings; no banking service inferred"
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
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "Lantern Exchange for paid intelligence, verified trade reports and private meetings;"
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
      "id": "ashvale-estate:caravan-facilities",
      "name": null,
      "display_label": "Estate caravan facilities",
      "parent_location_id": "ashvale-estate",
      "classification": "CONFIRMED CANON",
      "address": null,
      "categories": [
        "caravan-supplier"
      ],
      "owner_id": "theron-ashvale",
      "manager_id": "tomas",
      "operator_id": null,
      "staff_ids": [],
      "staff_notes": null,
      "services": [
        "Caravan facilities; scope/stock/capacity UNKNOWN"
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
      "last_verified_date": null,
      "last_verified_note": "No new visit or verification in this maintenance",
      "source_refs": [
        "entities/locations/ashvale-estate.md",
        "entities/characters/tomas.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "rental cottages; bakery, market, nighttime entertainment, caravan facilities;"
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

## Year 852 return and healing wing

The party returned safely or was accounted for. The grand council closed at Ashvale Estate. The healing wing has four regenerative beds and eight functioning calibrated cartridges. One defective cartridge was replaced under warranty without additional capital charge. Theron’s mother directs qualified care. Normal coverage supports up to three concurrent patients, with a fourth when staffing permits. Follow-up for defined minor injuries is underway. No universal healing rate or revenue is established. [Session evidence](../../changes/chronicles/year852-day365-end-session.md#ashvale-healing-wing)
