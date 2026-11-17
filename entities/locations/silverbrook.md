---
id: silverbrook
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-02-settlement-approval.md
- archive/legacy-modules/world/03-3-world-map-and-regions.md
---

# Silverbrook

APPROVED DESIGN settlement identity, not a census, visit or current operation. Promoted archived Elderwood-edge settlement. Elderwood/Elyndor equivalence and realm membership are unknown; only Vellorin membership is added.

## Approved settlement expansion — Phase 2

This is approved fictional design. Historical personnel and events keep their original owners; nothing here is a census or current operation.

```json
{
  "schema_version": 1,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Silverbrook",
    "population": {
      "amount": 620,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Promoted archived Elderwood-edge settlement. Elderwood/Elyndor equivalence and realm membership are unknown; only Vellorin membership is added.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Bee Gardens",
      "Herb Lane",
      "Timber Common"
    ],
    "government": "Archived council/warden concepts remain unverified personnel design. A local council and woodland-use petitions are proposed administration; no named liaison is appointed.",
    "housing_and_classes": "Beekeepers and gatherers occupy timber cottages around gardens; forestry households balance access rights, winter stores and paid seasonal labor.",
    "customs_and_daily_life": "A proposed first-honey gathering and shared hive wintering encourage mutual aid; herbal apprentices learn identification and safe collection, never automatic healing powers.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Poor flowering, contaminated herbs, timber-right disputes and restricted botanical trading are possible tensions.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "silverbrook:industry-woodland",
        "goods_services": "Honey, herbs, forestry and beekeeping",
        "producers": "Independent beekeepers, herbal gatherers and rights-holding cutters",
        "buyers": "Local households and prospective Briarfall apothecaries/workshops",
        "raw_materials": "Healthy hives, flowers, verified plant identification and lawful timber rights",
        "workers_skills": "Beekeepers, herbalists, cutters and paid gatherers",
        "storage": "Sealed honey pots, labeled dry herbs and seasoned timber",
        "transport": "Pack loads and carts only after approach verification",
        "seasonality": "Flowering, herb season and winter hive care",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Adulterated honey, restricted plants and illegal timber"
      }
    ],
    "businesses": [
      {
        "id": "silverbrook:honeycomb-bench",
        "name": "Honeycomb Bench",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Bee Gardens",
        "categories": [
          "general-store",
          "market"
        ],
        "services": [
          "Sealed honey, verified-source herbs and household goods"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "silverbrook:industry-woodland"
        ],
        "customers": "Villagers and prospective traders",
        "price_reference_ids": [
          "rations",
          "healing-herbs"
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
        "id": "silverbrook:green-spoon",
        "name": "Green Spoon Hearth",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Herb Lane",
        "categories": [
          "inn",
          "tavern",
          "courier"
        ],
        "services": [
          "Small lodging, meals and conditional caravan-post handoff"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "silverbrook:industry-woodland"
        ],
        "customers": "Visitors and local households",
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
      },
      {
        "id": "silverbrook:leafmark-yard",
        "name": "Leafmark Yard",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Timber Common",
        "categories": [
          "forestry",
          "carpenter"
        ],
        "services": [
          "Lawful timber lots, simple joinery and hive repairs"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "silverbrook:industry-woodland"
        ],
        "customers": "Beekeepers and builders",
        "price_reference_ids": [],
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
          "Rights-holding material producers, fuel sellers and tool makers; provenance, quality and load limits must be verified."
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
