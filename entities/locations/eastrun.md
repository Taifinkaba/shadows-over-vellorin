---
id: eastrun
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

# Eastrun

Established historical road journey from Ashvale Estate a little over two hours; walking route to Briarfall Crossing ~three hours.

## Settlement and business references — Chunk 3

This structured reference section owns only the settlement/service lookup fields below. Earlier prose remains unchanged and retains its dated qualifications. Business IDs are parent-scoped retrieval labels, not new location entities or visits. UNKNOWN is JSON null; no quote, stock, vacancy or transfer is implied. See the settlement directory and existing finance owner for retrieval.

```json
{
  "schema_version": 1,
  "location_id": "eastrun",
  "classification": "CONFIRMED CANON",
  "nation_id": null,
  "region_id": null,
  "settlement_type": "settlement",
  "population": null,
  "government": null,
  "principal_official_id": null,
  "watch": null,
  "watch_official_id": null,
  "court": null,
  "route_ids": [
    "route-ashvale-eastrun",
    "route-eastrun-briarfall",
    "route-caelthorne-eastrun",
    "route-eastrun-greyhaven-mill",
    "route-eastrun-greyhaven-valley"
  ],
  "neighborhoods": null,
  "nearby_location_ids": [
    "ashvale-estate",
    "briarfall-crossing"
  ],
  "institutions": [],
  "service_links": [],
  "local_problem_refs": [],
  "notes": "UNKNOWN fields are not absent services. Site/property entry is not a newly declared town. Current availability and exact locations require in-play verification.",
  "source_refs": [
    "entities/locations/eastrun.md"
  ],
  "evidence": [
    {
      "source_ref": "entities/locations/eastrun.md",
      "quote": "Established historical road journey from Ashvale Estate"
    }
  ],
  "businesses": [],
  "territory_id": null,
  "approved_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-02-settlement-approval.md",
    "settlement_label": "Eastrun",
    "population": {
      "amount": 4800,
      "qualifier": "approved estimate",
      "classification": "APPROVED DESIGN",
      "source_ref": "changes/chronicles/phase2-02-settlement-approval.md"
    },
    "households": null,
    "geographic_identity": "Established agricultural settlement; realm placement remains unknown in PR1.",
    "geographic_owner_ref": "world-geography",
    "districts": [
      "Cornmarket",
      "Bridle Row",
      "Millrace workshops",
      "Orchard End homes and farms"
    ],
    "government": "Preserve existing agricultural administration and any sourced reeve/merchant authority; no new official is named. Proposed market clerks weigh grain and post notices.",
    "housing_and_classes": "Farm households use yard plots and shared grazing by agreement; drovers lodge above yards, and hired harvest workers need paid seasonal beds.",
    "customs_and_daily_life": "A harvest measure fair proposes public weighing, horse judging and shared meals. Grain sowing, haymaking and harvest determine work; no exact dates or current harvest are asserted.",
    "community_services": "Community shrines/gatherings, clean-water care, public notices and mutual aid are design possibilities. Existing healers retain their limits; no new temple, spell or operating clinic is certified.",
    "market_and_employment": "Proposed market days depend on harvest, weather and willing vendors, with no fixed weekday. Paid work and apprenticeships follow the industry skills below; these are opportunities, not job offers or assignments.",
    "household_expenses": "Food, shelter, fuel, clothes, animal care and occasional treatment; no current household budget or debt is created.",
    "maintenance_and_emergencies": "Road/drain/bridge care needs willing labor, materials, funding and jurisdiction. Fire, flood, disease and supply interruption are possible emergency scenarios, not events.",
    "communication_ref": "settlement-communications",
    "trade_ref": "settlement-trade",
    "communications_local": "Letters may be left with the designed courier/post venue only by agreement; departure schedules depend on an actual willing carrier and verified route. Public notices and proposed beacon codes transmit no automatic knowledge.",
    "local_challenges": "Fodder scarcity, disputed grain measures, livestock disease and horse-document fraud are possible hooks.",
    "commercial_context": "Ordinary listed services follow their proposed legal classification. Unlicensed games may be tolerated only under verified local custom; fencing, forged papers, trafficking, coercive debt and protection rackets are prohibited-abuse designs, never confirmed local operations.",
    "current_conditions": null,
    "events": [],
    "industries": [
      {
        "id": "eastrun:industry-grain",
        "goods_services": "Grain farming, milling, baking and agricultural markets",
        "producers": "Farmers, independent millers, bakers and market growers",
        "buyers": "Local households, lodgers and prospective Caelthorne grain buyers",
        "raw_materials": "Seed, field access, water, mill power, fuel and sacks",
        "workers_skills": "Paid farmhands, millers, bakers and weighers",
        "storage": "Dry raised grain bins; flour pest control and fresh-food turnover",
        "transport": "Wagons or pack loads with route review",
        "seasonality": "Sowing and harvest; wet grain must dry",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "False measures, crop theft and exploitative harvest contracts"
      },
      {
        "id": "eastrun:industry-animals",
        "goods_services": "Horse breeding, livestock and feed",
        "producers": "Breeders, herders and fodder growers",
        "buyers": "Drovers, farmers and prospective caravan clients",
        "raw_materials": "Grazing rights, breeding stock, clean water and hay",
        "workers_skills": "Experienced handlers, farriers and paid herders",
        "storage": "Ventilated pens, segregated sick stock and dry feed",
        "transport": "Led animals and compatible wagons",
        "seasonality": "Foaling, hay harvest, cold-weather feed",
        "potential_shortages": "Finite labor, fuel, raw materials, storage space and transport; no current shortage is asserted.",
        "legal_obligations": "Verify title, land/resource access, weights, safety and any local license/tax before actual operations; detailed jurisdiction remains PR3.",
        "criminal_risks": "False title papers, animal theft and unsafe overstocking"
      }
    ],
    "businesses": [
      {
        "id": "eastrun:bushel-and-bridle",
        "name": "Bushel and Bridle",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Cornmarket",
        "categories": [
          "general-store",
          "market",
          "baker",
          "butcher"
        ],
        "services": [
          "Food staples, bread, inspected meat and agricultural supplies"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "eastrun:industry-grain"
        ],
        "customers": "Farm households and lawful buyers",
        "price_reference_ids": [
          "rations",
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
          "Independent local growers/food handlers and prospective import merchants; no supply agreement or delivery is established."
        ]
      },
      {
        "id": "eastrun:oat-crown-yard",
        "name": "Oat Crown Yard",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Bridle Row",
        "categories": [
          "stable",
          "caravan",
          "animal-trader"
        ],
        "services": [
          "Boarding, feed and introductions to independent horse sellers"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "eastrun:industry-animals"
        ],
        "customers": "Drovers and travelers",
        "price_reference_ids": [
          "horse-feed",
          "wagon-hire"
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "eastrun:millrace-iron",
        "name": "Millrace Iron",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Millrace workshops",
        "categories": [
          "blacksmith",
          "farrier"
        ],
        "services": [
          "Tools, horseshoes and repair commissions"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "eastrun:industry-animals"
        ],
        "customers": "Farmers and handlers",
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
        "id": "eastrun:orchard-rest",
        "name": "Orchard Rest",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Orchard End",
        "categories": [
          "inn",
          "tavern",
          "courier"
        ],
        "services": [
          "Lodging, meals and custody of properly recorded courier letters"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "eastrun:industry-grain"
        ],
        "customers": "Travelers and local households",
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
          "Verified food, clean water, fuel, linen/laundry and lawful feed suppliers as relevant; exact vendors and capacity UNKNOWN.",
          "Willing independent carriers/crews, lawful premises and finite vehicle/boat maintenance; no departure or route operations implied."
        ]
      },
      {
        "id": "eastrun:green-measure",
        "name": "Green Measure Remedies",
        "classification": "APPROVED DESIGN",
        "existing_business_ref": null,
        "district": "Cornmarket",
        "categories": [
          "apothecary",
          "healer"
        ],
        "services": [
          "Identified herbs and separately assessed healing consultations"
        ],
        "ownership_status": "UNKNOWN; independent proprietor/cooperative model, no owner assigned",
        "owner_id": null,
        "staff_ids": [],
        "staffing_model": "Independent paid adult proprietor or cooperative members with trained paid assistants; apprentices need willing supervision. No person appointed or hired.",
        "supplier_industry_ids": [
          "eastrun:industry-grain"
        ],
        "customers": "Farmworkers and households",
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
