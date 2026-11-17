---
id: briarfall-crossing
type: locations
status: canon
visibility: gm-reference
source_refs:
  - "archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md"
  - "archive/legacy-modules/codex/10-v1-4-reconciliation-of-roster-routes-and-evidence-out-of-world.md"
  - "archive/legacy-modules/codex/03-system-3-quests-consequences-faction-clocks.md"
  - "archive/legacy-modules/codex/11-v1-5-final-cross-session-verification-audit-out-of-world-no-gamep.md"
  - changes/chronicles/phase2-02-settlement-approval.md
---

# Briarfall Crossing

Established historical foot travel from Eastrun ~three hours; hidden lodge in surrounding woodland. Northern trade road wagon-capable; shorter woodland route not.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "briarfall-crossing",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": null,
  "settlement_type": "crossing settlement",
  "population": null,
  "government": null,
  "principal_official_id": null,
  "watch": null,
  "watch_official_id": null,
  "court": null,
  "route_ids": [
    "route-eastrun-briarfall",
    "route-caelthorne-briarfall-crossing"
  ],
  "neighborhoods": null,
  "nearby_location_ids": [
    "eastrun"
  ],
  "institutions": [],
  "service_links": [],
  "local_problem_refs": [],
  "notes": "Northern trade road is wagon-capable; shorter woodland route is not. The three-hour foot report does not identify a wagon alignment. Hidden woodland lodge remains separate from Ashvale Lodge.",
  "source_refs": [
    "entities/locations/briarfall-crossing.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/briarfall-crossing.md",
      "quote": "Northern trade road wagon-capable; shorter woodland route not."
    }
  ],
  "businesses": [],
  "territory_id": null,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Briarfall Crossing",
    "population": {
      "amount": 1650,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Established crossing and woodland settlement; no new realm assignment or surveyed bridge approach.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Bridgehead market",
      "Sawyer Bank",
      "Wheelwright Lane",
      "Woodland Edge cottages"
    ],
    "government": "Existing crossing authorities retain their scope; toll guards or bridge reeve from older designs are not new appointments. Maintenance petitions and public notices are proposed local procedures.",
    "housing_and_classes": "Timber workers rent small cottages; wagon families use lodging yards; repair trades maintain work courts away from crowded housing.",
    "customs_and_daily_life": "A proposed bridge-clearing day combines volunteer civic work with paid specialist repairs; a timber-mark fair honors lawful woodland use. Neither is scheduled at Day181.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Unsafe loads, missing timber marks, bridge repair disputes and illicit felling are prospective problems.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "briarfall-crossing:industry-wood",
        "goods_services": "Timber, forestry and woodland products",
        "producers": "Licensed or rights-holding cutters, gatherers and sawyers",
        "buyers": "Wheelwrights, households and prospective Eastrun workshops",
        "raw_materials": "Lawful woodland access, mature timber, saws and labor",
        "workers_skills": "Paid cutters, sawyers and woodland guides",
        "storage": "Seasoned covered timber stacks; fire separation",
        "transport": "Wagons on compatible roads; woodland pack loads only where feasible",
        "seasonality": "Wet ground and nesting/custom restrictions limit cutting",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Illegal felling, stolen marks and forced timber debts"
      },
      {
        "id": "briarfall-crossing:industry-wagons",
        "goods_services": "Wagon repair and forest trade services",
        "producers": "Independent wheelwrights and repair yards",
        "buyers": "Caravan owners and timber haulers",
        "raw_materials": "Seasoned wood, iron fittings, grease and spare wheels",
        "workers_skills": "Wheelwrights, smiths and trained apprentices",
        "storage": "Covered work bays and secured customer vehicles",
        "transport": "Repairs at yard; finished wagons require verified road access",
        "seasonality": "Winter mud and material drying constrain work",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Substandard axles, cargo liens and protection demands"
      }
    ],
    "businesses": [
      {
        "id": "briarfall-crossing:copper-hoop-yard",
        "name": "Copper Hoop Yard",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Wheelwright Lane",
        "categories": [
          "wheelwright",
          "blacksmith",
          "caravan"
        ],
        "services": [
          "Wagon repair, replacement hoops and conditional local hire"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "briarfall-crossing:industry-wagons"
        ],
        "customers": "Haulers and woodland traders",
        "price_reference_ids": [
          "wagon-hire",
          "rope"
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
          "Rights-holding material producers, fuel sellers and tool makers; provenance, quality and load limits must be verified.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "briarfall-crossing:sawyers-table",
        "name": "Sawyer’s Table",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Sawyer Bank",
        "categories": [
          "general-store",
          "market"
        ],
        "services": [
          "Lawfully marked timber brokerage and camp supplies"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "briarfall-crossing:industry-wood"
        ],
        "customers": "Cutters and repair yards",
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
      },
      {
        "id": "briarfall-crossing:bridge-rest",
        "name": "Bridge Rest",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Bridgehead market",
        "categories": [
          "inn",
          "tavern",
          "stable",
          "courier"
        ],
        "services": [
          "Lodging, meals, stabling and caravan-post booking"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "briarfall-crossing:industry-wagons"
        ],
        "customers": "Travelers and repair clients",
        "price_reference_ids": [
          "simple-bed",
          "hot-meal",
          "horse-feed"
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "briarfall-crossing:fern-and-kettle",
        "name": "Fern and Kettle",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Woodland Edge",
        "categories": [
          "apothecary",
          "bathhouse"
        ],
        "services": [
          "Identified herbs, washing and clean heated water"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "briarfall-crossing:industry-wood"
        ],
        "customers": "Workers and households",
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Identified lawful herb growers/gatherers and clean dressing suppliers; treatment limits need independent verification."
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
