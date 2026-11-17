---
id: windmere
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-02-settlement-approval.md
---

# Windmere

APPROVED DESIGN settlement identity, not a census, visit or current operation. Approved pastoral village in Vellorin; realm, exact terrain boundaries and roads remain unlocated.

## Approved settlement expansion — Phase 2

This is approved fictional design. Historical personnel and events keep their original owners; nothing here is a census or current operation.

```json
{
  "schema_version": 1,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Windmere",
    "population": {
      "amount": 310,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Approved pastoral village in Vellorin; realm, exact terrain boundaries and roads remain unlocated.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Shearing Green",
      "Wool Lane",
      "Storebank cottages"
    ],
    "government": "Proposed village meeting and pasture stewards handle notices and grazing petitions; no chief, reeve or magistrate is appointed.",
    "housing_and_classes": "Shepherd households share winter fodder responsibilities by agreement; spinners work near home and seasonal drovers need shelter. No household count is supplied.",
    "customs_and_daily_life": "A proposed shearing gathering, wool grading and communal winter-store inspection fit seasonal pastoral life; migration follows lawful pasture access and weather, not a fixed current schedule.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Pasture disputes, poor wool prices, winter fodder gaps and coercive wool debts are possible problems.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "windmere:industry-pastoral",
        "goods_services": "Sheep, wool, preserved food and seasonal trade",
        "producers": "Independent shepherds, spinners and lawful food preservers",
        "buyers": "Local households and prospective Eastrun cloth/food buyers",
        "raw_materials": "Pasture rights, fodder, shears, salt, clean water and wool",
        "workers_skills": "Shepherds, shearers, spinners and food handlers",
        "storage": "Dry graded wool, ventilated fodder and protected salted/dried food",
        "transport": "Pack animals or carts after approach review",
        "seasonality": "Lambing, shearing, grazing migration and winter storage",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Wool adulteration, livestock theft and coercive tied credit"
      }
    ],
    "businesses": [
      {
        "id": "windmere:wool-and-salt",
        "name": "Wool and Salt",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Wool Lane",
        "categories": [
          "general-store",
          "market"
        ],
        "services": [
          "Graded wool, preserved food and household supplies"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "windmere:industry-pastoral"
        ],
        "customers": "Shepherds and village households",
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
        "id": "windmere:shearers-hearth",
        "name": "Shearer’s Hearth",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Shearing Green",
        "categories": [
          "inn",
          "tavern",
          "courier"
        ],
        "services": [
          "Seasonal paid lodging, meals and conditional pack-post handoff"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "windmere:industry-pastoral"
        ],
        "customers": "Drovers, shearers and households",
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
