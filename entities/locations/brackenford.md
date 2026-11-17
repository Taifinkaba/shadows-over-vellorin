---
id: brackenford
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year848-day156-end-session.md
- changes/chronicles/phase2-02-settlement-approval.md
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
  "territory_id": "vellorin",
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Brackenford",
    "population": {
      "amount": 180,
      "qualifier": "approximately",
      "classification": "CONFIRMED CANON",
      "source_ref": "changes/chronicles/year848-day156-end-session.md"
    },
    "households": {
      "amount": 42,
      "classification": "CONFIRMED CANON",
      "source_ref": "changes/chronicles/year848-day156-end-session.md"
    },
    "geographic_identity": "Existing village in Northern Marches, Vellorin. House Ashvale’s cottage remains private property, not village government.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Village bridge and market",
      "Western Mill Lane",
      "Farm lanes and grazing margins"
    ],
    "government": "Reeve Elsbeth Marrin and council; Captain Ressa Vale and six part-time watch members remain as historically recorded. No extra judicial power is granted.",
    "housing_and_classes": "Preserve the historical approximately180 residents and42 households. Small farmhouses, shared grazing and millstream access require neighbor agreements; no cottage occupancy or rent is inferred.",
    "customs_and_daily_life": "Proposed seasonal seed exchanges and shared bridge inspection build on farm life. Public notices may be read aloud at the market or Willow Lantern, subject to permission. No market weekday or festival date is fixed.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Grazing rights, water use, seasonal milling queues and disputed repair obligations are possible village disputes. Existing historical mysteries are not expanded.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "brackenford:industry-farm-mill",
        "goods_services": "Farming, milling and local markets",
        "producers": "Independent farmers and millers; Harlan Wicks’s recorded profession does not assign a specific mill",
        "buyers": "Local households, inn and market customers",
        "raw_materials": "Land access, grain, water, seed and milling agreement",
        "workers_skills": "Farmhands, millers and seasonal market vendors",
        "storage": "Dry grain and flour; clean shared containers",
        "transport": "Local foot/handcart carriage; onward road service unknown",
        "seasonality": "Harvest, stream flow and milling queues",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "False measures, grain theft and disputed water access"
      },
      {
        "id": "brackenford:industry-services",
        "goods_services": "Smithing, lodging and local trade",
        "producers": "Existing forge, Willow Lantern and herbalist; preserve Borin, Mara and Seren’s recorded roles",
        "buyers": "Villagers and willing travelers with verified access",
        "raw_materials": "Lawfully acquired iron, fuel, bedding, food and herbs",
        "workers_skills": "Existing operators and any separately verified paid helpers",
        "storage": "Secure customer tools; dry bedding and identified herbs",
        "transport": "Local collection; historical routes do not guarantee arrival",
        "seasonality": "Fuel, harvest demand and illness constrain work",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Stolen goods, unlicensed remedies and exploitative credit"
      }
    ],
    "businesses": [
      {
        "id": "brackenford:willow-lantern",
        "name": "Willow Lantern",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": "brackenford:willow-lantern",
        "district": "Village center; exact premises unchanged/unknown",
        "categories": [
          "inn"
        ],
        "services": [
          "Existing lodging; proposed meal and notice-reading service is design only"
        ],
        "ownership_status": "Inherited from existing parent-owned record; operator is not owner",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Existing operator roles remain in their historical owner; additional paid adult helpers need consent, competence and verification. No hire or duty assignment is created.",
        "supplier_industry_ids": [
          "brackenford:industry-services"
        ],
        "customers": "Villagers and travelers",
        "price_reference_ids": [
          "simple-bed",
          "private-room",
          "hot-meal"
        ],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "lawful-design",
        "current_license": null,
        "adult_workers_only": null,
        "worker_agency": "Workers retain independent agency, rest, agreed pay and the right to decline unsafe work.",
        "operating_costs": [
          "Premises, fuel/water and maintenance",
          "Lawfully sourced supplies and storage",
          "Agreed staff pay; any local fees require verification"
        ],
        "limitations": "Design availability only. Finite labor, premises, materials, local permission, hygiene and opening hours require verification. No current license, stock, room vacancy or operating schedule is certified.",
        "stock_counts": null,
        "cash_balance_cp": null,
        "operational_status": "UNKNOWN",
        "source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
        "suppliers": [
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established.",
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN."
        ]
      },
      {
        "id": "brackenford:forge",
        "name": "Brackenford forge / blacksmith service",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": "brackenford:forge",
        "district": "Existing forge; address unknown",
        "categories": [
          "blacksmith"
        ],
        "services": [
          "Existing smithing; future tools depend on materials and Borin’s acceptance"
        ],
        "ownership_status": "Inherited from existing parent-owned record; operator is not owner",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Existing operator roles remain in their historical owner; additional paid adult helpers need consent, competence and verification. No hire or duty assignment is created.",
        "supplier_industry_ids": [
          "brackenford:industry-services"
        ],
        "customers": "Villagers and lawful repair clients",
        "price_reference_ids": [
          "iron-sword"
        ],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "lawful-design",
        "current_license": null,
        "adult_workers_only": null,
        "worker_agency": "Workers retain independent agency, rest, agreed pay and the right to decline unsafe work.",
        "operating_costs": [
          "Premises, fuel/water and maintenance",
          "Lawfully sourced supplies and storage",
          "Agreed staff pay; any local fees require verification"
        ],
        "limitations": "Design availability only. Finite labor, premises, materials, local permission, hygiene and opening hours require verification. No current license, stock, room vacancy or operating schedule is certified.",
        "stock_counts": null,
        "cash_balance_cp": null,
        "operational_status": "UNKNOWN",
        "source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
        "suppliers": [
          "Rights-holding material producers, fuel sellers and tool makers; provenance, quality and load limits must be verified."
        ]
      },
      {
        "id": "brackenford:herbalist",
        "name": "Seren Willowmere’s herbalist service",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": "brackenford:herbalist",
        "district": "Existing service; shop address unknown",
        "categories": [
          "herbalist"
        ],
        "services": [
          "Existing herbalist role; proposed identified-herb bundles need an actual quote"
        ],
        "ownership_status": "Inherited from existing parent-owned record; operator is not owner",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Existing operator roles remain in their historical owner; additional paid adult helpers need consent, competence and verification. No hire or duty assignment is created.",
        "supplier_industry_ids": [
          "brackenford:industry-services"
        ],
        "customers": "Households and travelers",
        "price_reference_ids": [
          "healing-herbs"
        ],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "regulated-design",
        "current_license": null,
        "adult_workers_only": null,
        "worker_agency": "Workers retain independent agency, rest, agreed pay and the right to decline unsafe work.",
        "operating_costs": [
          "Premises, fuel/water and maintenance",
          "Lawfully sourced supplies and storage",
          "Agreed staff pay; any local fees require verification"
        ],
        "limitations": "Design availability only. Finite labor, premises, materials, local permission, hygiene and opening hours require verification. No current license, stock, room vacancy or operating schedule is certified.",
        "stock_counts": null,
        "cash_balance_cp": null,
        "operational_status": "UNKNOWN",
        "source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
        "suppliers": [
          "Identified lawful herb growers/gatherers and clean dressing suppliers; treatment limits need independent verification."
        ]
      },
      {
        "id": "brackenford:watermill",
        "name": "Brackenford watermill",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": "brackenford:watermill",
        "district": "Existing watermill and millstream",
        "categories": [
          "milling"
        ],
        "services": [
          "Milling service proposal only; do not appoint Harlan to this mill"
        ],
        "ownership_status": "Inherited from existing parent-owned record; operator is not owner",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Existing operator roles remain in their historical owner; additional paid adult helpers need consent, competence and verification. No hire or duty assignment is created.",
        "supplier_industry_ids": [
          "brackenford:industry-farm-mill"
        ],
        "customers": "Farmers and households",
        "price_reference_ids": [],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "lawful-design",
        "current_license": null,
        "adult_workers_only": null,
        "worker_agency": "Workers retain independent agency, rest, agreed pay and the right to decline unsafe work.",
        "operating_costs": [
          "Premises, fuel/water and maintenance",
          "Lawfully sourced supplies and storage",
          "Agreed staff pay; any local fees require verification"
        ],
        "limitations": "Design availability only. Finite labor, premises, materials, local permission, hygiene and opening hours require verification. No current license, stock, room vacancy or operating schedule is certified.",
        "stock_counts": null,
        "cash_balance_cp": null,
        "operational_status": "UNKNOWN",
        "source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
        "suppliers": [
          "Local independent producers; specific suppliers and agreements remain UNKNOWN."
        ]
      },
      {
        "id": "brackenford:market",
        "name": "Brackenford village market",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": "brackenford:market",
        "district": "Existing village market",
        "categories": [
          "market"
        ],
        "services": [
          "Existing market; proposed rotating produce stalls do not establish vendors or stock"
        ],
        "ownership_status": "Inherited from existing parent-owned record; operator is not owner",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Existing operator roles remain in their historical owner; additional paid adult helpers need consent, competence and verification. No hire or duty assignment is created.",
        "supplier_industry_ids": [
          "brackenford:industry-farm-mill"
        ],
        "customers": "Village households",
        "price_reference_ids": [
          "rations"
        ],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "lawful-design",
        "current_license": null,
        "adult_workers_only": null,
        "worker_agency": "Workers retain independent agency, rest, agreed pay and the right to decline unsafe work.",
        "operating_costs": [
          "Premises, fuel/water and maintenance",
          "Lawfully sourced supplies and storage",
          "Agreed staff pay; any local fees require verification"
        ],
        "limitations": "Design availability only. Finite labor, premises, materials, local permission, hygiene and opening hours require verification. No current license, stock, room vacancy or operating schedule is certified.",
        "stock_counts": null,
        "cash_balance_cp": null,
        "operational_status": "UNKNOWN",
        "source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
        "suppliers": [
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established."
        ]
      }
    ],
    "criminal_faction_refs": [],
    "unlawful_activity_designs": [
      {
        "category": "fencing-and-fraud",
        "legal_design": "prohibited-design",
        "description": "Stolen tools, falsely described goods or forged work/cargo papers are possible illicit offers; no vendor, location, victim or completed act is established.",
        "finite_constraints": "Requires actual goods, willing buyers and access; proceeds, loss and enforcement are not generated.",
        "events": []
      },
      {
        "category": "unlicensed-games",
        "legal_design": "tolerated-design",
        "description": "Small informal adult games may be tolerated only after local custom and stakes are verified. This is conditional cultural design, not a license or current gambling operation.",
        "finite_constraints": "Finite consenting adult stakes; no automatic debt, house profits or compulsory play.",
        "events": []
      }
    ]
  }
}
```
