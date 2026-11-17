---
id: rivermere
type: locations
status: last-verified
visibility: gm-reference
source_refs:
- archive/legacy-modules/world/03-3-world-map-and-regions.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- changes/chronicles/phase2-02-settlement-approval.md
---

# Rivermere

CONFIRMED CANON established river-trade place name. Specific current services/government remain archival design unless confirmed elsewhere. Prospective Caelthorne route is not a played journey; no new port operations.

## Approved settlement expansion — Phase 2

This is approved fictional design. Historical personnel and events keep their original owners; nothing here is a census or current operation.

```json
{
  "schema_version": 1,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Rivermere",
    "population": {
      "amount": 12000,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "River-trade settlement within approved Rivermere League; not the whole federation.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Quayside",
      "Sailcloth Ward",
      "Warehouse Reach",
      "Old Market homes and shrines"
    ],
    "government": "Preserve any established harbor/merchant authority; role-based quay clerks and council petition days are civic design only, not new appointments or charters.",
    "housing_and_classes": "Boat crews and fishworkers use compact waterside rooms; warehouse merchants occupy larger courts; flood-prone cheap housing creates unequal risk.",
    "customs_and_daily_life": "A proposed river-blessing and net-mending gathering supports rescue collections; textile apprentices share dye-yard duties. Vessel departures depend on water, cargo and willing crews.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Flood damage, cargo misdescription, spoiled fish, dock debt and unsafe crowding are potential tensions.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "rivermere:industry-shipping",
        "goods_services": "Shipping, warehouses and merchant services",
        "producers": "Independent boat owners, warehouse keepers and cargo brokers",
        "buyers": "Merchants, local shops and prospective Caelthorne buyers",
        "raw_materials": "Sound boats, ropes, dry stores, lawful cargo and willing crews",
        "workers_skills": "Boat crews, porters, tally clerks and repair trades",
        "storage": "Separated dry cargo, secure ledgers, fire and flood precautions",
        "transport": "Barges and dispatch boats; navigability unverified",
        "seasonality": "Flood, low water and ice can interrupt traffic",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Cargo fraud, smuggling and extortion"
      },
      {
        "id": "rivermere:industry-fish",
        "goods_services": "Fisheries and fish preservation",
        "producers": "Independent fishers and salters",
        "buyers": "Households, inns and prospective regional buyers",
        "raw_materials": "Lawful fishing access, nets, salt and clean water",
        "workers_skills": "Fishers, netmakers and food handlers",
        "storage": "Fresh catch rapid sale; salted/dried stock kept clean and dry",
        "transport": "Local baskets, boats or timed cart delivery",
        "seasonality": "Weather, breeding restrictions and spoilage",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Stolen nets, unsafe food and landing-fee abuse"
      },
      {
        "id": "rivermere:industry-textiles",
        "goods_services": "Textiles, dyeing and sailcloth",
        "producers": "Weavers, dyers and cloth finishers",
        "buyers": "Boat owners, tailors and households",
        "raw_materials": "Wool/flax, dyes, clean water and fuel",
        "workers_skills": "Weavers, dyers, cutters and supervised apprentices",
        "storage": "Dry cloth stores; separate dyes from food",
        "transport": "Barges or wagons after route review",
        "seasonality": "Water supply and drying weather constrain finishing",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Adulterated dyes, cloth theft and withheld wages"
      }
    ],
    "businesses": [
      {
        "id": "rivermere:reedseal-stores",
        "name": "Reedseal Stores",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Warehouse Reach",
        "categories": [
          "warehouse",
          "general-store",
          "courier"
        ],
        "services": [
          "Dry cargo custody, tallying and dispatch-boat booking"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "rivermere:industry-shipping"
        ],
        "customers": "Boat owners and merchants",
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
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "rivermere:net-and-needle",
        "name": "Net and Needle",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Sailcloth Ward",
        "categories": [
          "tailor",
          "netmaker",
          "market"
        ],
        "services": [
          "Sailcloth, clothes, net repairs and graded textile lots"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "rivermere:industry-textiles"
        ],
        "customers": "Fishers, households and boat crews",
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
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established.",
          "Prospective cloth, thread, fiber and dye producers with documented lawful title; no current stock or contract."
        ]
      },
      {
        "id": "rivermere:saltbell-kitchen",
        "name": "Saltbell Kitchen",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Quayside",
        "categories": [
          "fishmonger",
          "tavern",
          "inn"
        ],
        "services": [
          "Preserved fish, meals and crew lodging"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "rivermere:industry-fish"
        ],
        "customers": "Crews and households",
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
        "id": "rivermere:river-lantern",
        "name": "River Lantern House",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Old Market",
        "categories": [
          "pleasure-house",
          "brothel",
          "bathhouse"
        ],
        "services": [
          "Consensual adult companionship, hospitality and bathing"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "rivermere:industry-shipping"
        ],
        "customers": "Adult patrons; workers can refuse or end any engagement",
        "price_reference_ids": [],
        "pricing_basis": "Use service-price-references approved_references, not archival bands, for linked baselines. Other services need an actual quote; no charges or payroll.",
        "legal_design": "regulated-design",
        "current_license": null,
        "adult_workers_only": true,
        "worker_agency": "All entertainment workers are adults, can refuse clients, set boundaries, retain earnings/control of documents and leave without debt bondage. Independent consent cannot be inferred from employment; coercion, trafficking, violence and confinement are prohibited abuse.",
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN."
        ]
      },
      {
        "id": "rivermere:nine-knots",
        "name": "Nine Knots Counter",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Quayside",
        "categories": [
          "pawnshop",
          "gambling"
        ],
        "services": [
          "Documented pledges and declared-stake adult games"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "rivermere:industry-shipping"
        ],
        "customers": "Adult crews and merchants",
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
