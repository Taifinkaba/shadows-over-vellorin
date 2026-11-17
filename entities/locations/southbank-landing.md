---
id: southbank-landing
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-02-settlement-approval.md
- archive/legacy-modules/world/03-3-world-map-and-regions.md
---

# Southbank Landing

APPROVED DESIGN settlement identity, not a census, visit or current operation. Archived Southbank Landing promoted; Southbank is the approved short settlement label. Vellorin membership only; precise relation to Rivermere/League and river-course order remain unknown.

## Approved settlement expansion — Phase 2

This is approved fictional design. Historical personnel and events keep their original owners; nothing here is a census or current operation.

```json
{
  "schema_version": 1,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Southbank",
    "population": {
      "amount": 2300,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Archived Southbank Landing promoted; Southbank is the approved short settlement label. Vellorin membership only; precise relation to Rivermere/League and river-course order remain unknown.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Landing Steps",
      "Grainbank",
      "Netmakers Row",
      "Upper Bank homes"
    ],
    "government": "Preserve archived dockmaster concept as unverified design rather than a current appointment. Proposed ferry clerks and local petition meetings do not confer new legal powers.",
    "housing_and_classes": "Crews and fishers live near landing yards; higher-bank plots command better protection from flooding. Rents, residents and land titles remain unknown.",
    "customs_and_daily_life": "Proposed ferry blessing and grain-barge counting days are community customs; notices advertise intended sailings only after crews, water and cargo are verified.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Changing water levels, ferry access disputes, unmarked cargo, grain spoilage and predatory debt are prospective risks.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "southbank-landing:industry-river-food",
        "goods_services": "Fisheries, ferries, barges and grain transport",
        "producers": "Independent fishers, ferry crews, boat owners and grain handlers",
        "buyers": "Local households and prospective Rivermere merchants",
        "raw_materials": "Lawful landing/fishing rights, sound boats, grain, nets and salt",
        "workers_skills": "Boat crews, fishworkers, porters and tally clerks",
        "storage": "Raised dry grain stores; rapid fish turnover and preserved-food separation",
        "transport": "Boats, ferries and short cart movements; channels unsurveyed",
        "seasonality": "Water level, flood, ice and harvest timing",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Cargo substitution, unsafe ferries, smuggling and debt collection"
      }
    ],
    "businesses": [
      {
        "id": "southbank-landing:grainstep-stores",
        "name": "Grainstep Stores",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Grainbank",
        "categories": [
          "warehouse",
          "market"
        ],
        "services": [
          "Dry grain custody and cargo tallying"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "southbank-landing:industry-river-food"
        ],
        "customers": "Farm sellers and prospective merchants",
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
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "southbank-landing:reed-oar",
        "name": "Reed Oar Landing Service",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Landing Steps",
        "categories": [
          "ferry",
          "barge",
          "courier"
        ],
        "services": [
          "Conditional passenger/cargo carriage and dispatch-boat booking"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "southbank-landing:industry-river-food"
        ],
        "customers": "Travelers and merchants",
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
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "southbank-landing:netmenders-bowl",
        "name": "Netmender’s Bowl",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Netmakers Row",
        "categories": [
          "fishmonger",
          "tavern",
          "inn"
        ],
        "services": [
          "Fish, hot meals and small crew lodgings"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "southbank-landing:industry-river-food"
        ],
        "customers": "Fishers and travelers",
        "price_reference_ids": [
          "hot-meal",
          "simple-bed"
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
        "id": "southbank-landing:banklight-ledger",
        "name": "Banklight Counter",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Upper Bank",
        "categories": [
          "pawnshop",
          "general-store"
        ],
        "services": [
          "Documented pledges, rope and work supplies"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "southbank-landing:industry-river-food"
        ],
        "customers": "Boat crews and households",
        "price_reference_ids": [
          "rope"
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
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established.",
          "Consenting adult customers and documented lawful pledged goods only; reject stolen property and coercive credit."
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
