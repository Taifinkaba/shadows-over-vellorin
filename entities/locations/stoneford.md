---
id: stoneford
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-02-settlement-approval.md
---

# Stoneford

APPROVED DESIGN settlement identity, not a census, visit or current operation. Approved quarrying settlement in Vellorin; exact river ford, quarry hills, realm and approaches are unsurveyed. No dungeon entrance is established.

## Approved settlement expansion — Phase 2

This is approved fictional design. Historical personnel and events keep their original owners; nothing here is a census or current operation.

```json
{
  "schema_version": 1,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Stoneford",
    "population": {
      "amount": 940,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Approved quarrying settlement in Vellorin; exact river ford, quarry hills, realm and approaches are unsurveyed. No dungeon entrance is established.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Quarry Gate",
      "Masons Yard",
      "Ford Market homes"
    ],
    "government": "Proposed local council and works clerk administer public notices and repair petitions; identity and legal powers remain unknown, with no new magistrate.",
    "housing_and_classes": "Masons use durable stone cottages; quarry crews need paid lodging and safe daylight transport. Household numbers and occupied buildings are unknown.",
    "customs_and_daily_life": "A proposed mason’s measure fair displays work samples; stone-setting apprentices require trained supervision, safe lifting and rest.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Quarry safety, damaged lanes, unequal access to clean water and building-quality disputes are possible hooks, not current accidents.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "stoneford:industry-quarry",
        "goods_services": "Quarrying, masonry and construction materials",
        "producers": "Rights-holding quarry workers, stone dressers and masons",
        "buyers": "Local builders and prospective Caelthorne commissions",
        "raw_materials": "Stone access, safe lifting gear, fuel and work specifications",
        "workers_skills": "Quarriers, masons, riggers and paid apprentices",
        "storage": "Stable marked block stacks; dry mortar ingredients",
        "transport": "Heavy wagons after road/bridge load review",
        "seasonality": "Frost and saturated ground limit extraction",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Illegal quarrying, stolen blocks and fraudulent contracts"
      }
    ],
    "businesses": [
      {
        "id": "stoneford:straightedge-yard",
        "name": "Straightedge Yard",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Masons Yard",
        "categories": [
          "mason",
          "quarry-supplier"
        ],
        "services": [
          "Dressed stone and independently agreed lifting commissions"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "stoneford:industry-quarry"
        ],
        "customers": "Builders and quarry clients",
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
          "Rights-holding material producers, fuel sellers and tool makers; provenance, quality and load limits must be verified."
        ]
      },
      {
        "id": "stoneford:fordpantry",
        "name": "Fordpantry",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Ford Market",
        "categories": [
          "general-store",
          "baker",
          "market"
        ],
        "services": [
          "Bread, provisions and basic site supplies"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "stoneford:industry-quarry"
        ],
        "customers": "Workers and households",
        "price_reference_ids": [
          "rations",
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
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established."
        ]
      },
      {
        "id": "stoneford:resting-plumb",
        "name": "Resting Plumb",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Quarry Gate",
        "categories": [
          "inn",
          "tavern",
          "courier"
        ],
        "services": [
          "Paid lodging, meals and conditional messenger booking"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "stoneford:industry-quarry"
        ],
        "customers": "Workers and visitors",
        "price_reference_ids": [
          "simple-bed",
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
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
