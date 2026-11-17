---
id: caelthorne
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

# Caelthorne

Crown administrative center with magistrates, watch and archives. Prospective route durations in World Bible are not past journeys.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "caelthorne",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": null,
  "settlement_type": "Crown administrative center",
  "population": null,
  "government": "Existing Crown administrative institutions",
  "principal_official_id": null,
  "watch": "Existing watch; officer and station address UNKNOWN",
  "watch_official_id": null,
  "court": "Existing magistrates; names, court address and gaol UNKNOWN",
  "route_ids": [
    "route-caelthorne-ashvale-estate",
    "route-caelthorne-eastrun",
    "route-caelthorne-briarfall-crossing",
    "route-caelthorne-blackthorn-watch",
    "route-caelthorne-ironhollow-hold",
    "route-caelthorne-rivermere",
    "route-caelthorne-frostspire-peaks",
    "route-caelthorne-mount-vaelspire",
    "route-caelthorne-elyndor",
    "route-caelthorne-frostmarch"
  ],
  "neighborhoods": null,
  "nearby_location_ids": [],
  "institutions": [
    {
      "kind": "magistrate",
      "label": "Existing magistrates; no new named court",
      "entity_id": null,
      "classification": "CONFIRMED CANON"
    },
    {
      "kind": "watch",
      "label": "Existing watch",
      "entity_id": null,
      "classification": "CONFIRMED CANON"
    },
    {
      "kind": "archive",
      "label": "Existing archives; access terms UNKNOWN",
      "entity_id": null,
      "classification": "CONFIRMED CANON"
    },
    {
      "kind": "guild",
      "label": "Existing Wayfarers headquarters",
      "entity_id": "wayfarers-guild",
      "classification": "CONFIRMED CANON"
    }
  ],
  "service_links": [],
  "local_problem_refs": [],
  "notes": "UNKNOWN fields are not absent services. Site/property entry is not a newly declared town. Current availability and exact locations require in-play verification.",
  "source_refs": [
    "entities/locations/caelthorne.md",
    "entities/factions/wayfarers-guild.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/caelthorne.md",
      "quote": "Crown administrative center with magistrates, watch and archives."
    },
    {
      "source_ref": "entities/factions/wayfarers-guild.md",
      "quote": "Caelthorne HQ with established branches."
    }
  ],
  "businesses": [],
  "territory_id": null,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Caelthorne",
    "population": {
      "amount": 38000,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Capital of Valedorn; realm membership is the approved PR1 edge, not surveyed jurisdiction.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Crown Steps civic quarter",
      "Lantern Ward shops and apprentices’ courts",
      "Weavers Lane workshops",
      "South Gate yards and lodging"
    ],
    "government": "Existing Crown magistrates and watch; clerks keep petitions and public notices. No named official or new court is appointed.",
    "housing_and_classes": "Merchants and officials rent larger houses above tradespeople’s courts; porters and apprentices share modest lodgings. Water, fuel and bread compete with rent in household budgets.",
    "customs_and_daily_life": "A proposed charter-day procession celebrates civic crafts; workshop masters may offer apprenticeships, while public shrines and neighborhood collections support mutual aid. Calendar dates and actual observance are unknown.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Rent pressure, forged work certificates and exclusion from apprenticeships are possible tensions, not current incidents.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "caelthorne:industry-civic-services",
        "goods_services": "Administration, guild services and education",
        "producers": "Independent clerks, teachers and existing institutions within their authority",
        "buyers": "Petitioners, families and lawful guild clients",
        "raw_materials": "Parchment, ink, trained time and authorized records",
        "workers_skills": "Literate clerks, tutors, copyists and consenting apprentices",
        "storage": "Dry locked record chests; separate customer documents",
        "transport": "Hand delivery and mounted messenger proposals",
        "seasonality": "Weather and school/work duties can delay attendance",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Forged seals, bribery and exclusion from training"
      },
      {
        "id": "caelthorne:industry-luxury-crafts",
        "goods_services": "Tailoring and luxury craftwork",
        "producers": "Independent tailors and finishing workshops",
        "buyers": "Households, merchants and commissioning clients",
        "raw_materials": "Cloth, thread, dyes, leather and lawful commissioned materials",
        "workers_skills": "Tailors, embroiderers, finishers and trained apprentices",
        "storage": "Dry cloth racks, secured commissioned work",
        "transport": "Pack loads or wagons after route review",
        "seasonality": "Cloth deliveries and festival demand vary",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "Counterfeit cloth, stolen commissions and debt pressure"
      }
    ],
    "businesses": [
      {
        "id": "caelthorne:crownstep-exchange",
        "name": "Crownstep Exchange",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Lantern Ward",
        "categories": [
          "general-store",
          "tailor",
          "pawnshop",
          "market"
        ],
        "services": [
          "Cloth, household wares, alterations and documented pledges"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-luxury-crafts"
        ],
        "customers": "Households and visiting merchants",
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
          "Prospective cloth, thread, fiber and dye producers with documented lawful title; no current stock or contract.",
          "Consenting adult customers and documented lawful pledged goods only; reject stolen property and coercive credit."
        ]
      },
      {
        "id": "caelthorne:lampwright-house",
        "name": "Lampwright House",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Crown Steps",
        "categories": [
          "scribe",
          "education",
          "courier"
        ],
        "services": [
          "Copying, fee-based lessons, public notice reading and messenger booking"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-civic-services"
        ],
        "customers": "Petitioners, apprentices and courier clients",
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
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied.",
          "Independent parchment, ink and book suppliers; teachers retain duties and consent."
        ]
      },
      {
        "id": "caelthorne:hearthbell-inn",
        "name": "Hearthbell Inn",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "South Gate yards",
        "categories": [
          "inn",
          "tavern",
          "stable",
          "caravan"
        ],
        "services": [
          "Beds, meals, stabling and caravan introductions"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-luxury-crafts"
        ],
        "customers": "Travelers and local diners",
        "price_reference_ids": [
          "simple-bed",
          "private-room",
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
        "id": "caelthorne:three-copper-cups",
        "name": "Three Copper Cups",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Lantern Ward",
        "categories": [
          "gambling",
          "tavern"
        ],
        "services": [
          "Table games, refreshments and clearly posted stake limits"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-civic-services"
        ],
        "customers": "Consenting adult patrons",
        "price_reference_ids": [
          "hot-meal"
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Consenting adult customers and documented lawful pledged goods only; reject stolen property and coercive credit."
        ]
      },
      {
        "id": "caelthorne:amber-curtain",
        "name": "Amber Curtain",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Weavers Lane",
        "categories": [
          "brothel",
          "pleasure-house",
          "bathhouse"
        ],
        "services": [
          "Adult companionship, private hospitality and bathing by consent"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-luxury-crafts"
        ],
        "customers": "Adult patrons; every entertainment worker is an independent adult",
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
        "id": "caelthorne:blue-thimble",
        "name": "Blue Thimble Atelier",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Weavers Lane",
        "categories": [
          "tailor",
          "luxury-craft"
        ],
        "services": [
          "Commissioned tailoring, embroidery and paid training"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "caelthorne:industry-luxury-crafts"
        ],
        "customers": "Households and commissioning merchants",
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
          "Prospective cloth, thread, fiber and dye producers with documented lawful title; no current stock or contract."
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
