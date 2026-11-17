---
id: property-financial-references
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-06-economic-approval.md
- changes/chronicles/economy-framework-maintenance.md
- state/finance-ledger.json
- entities/mechanics/party-finances.md
- archive/checkpoints/year848-day137-finance-ledger.json
- entities/locations/ashvale-estate.md
- entities/locations/ashvale-lodge.md
- entities/locations/briarstone-cottage.md
- entities/factions/dragon-slayer-academy.md
- entities/items/ashvale-wagon.md
- entities/items/vanguard-wagon.md
- entities/items/sovereign-expedition-wagon.md
- entities/items/night-sovereign.md
- entities/items/dragon-scales-stock.md
- entities/mechanics/guild-animal-registry.md
- entities/mechanics/seven-bells-inventory.md
- entities/mechanics/shady-salvage.md
- entities/mechanics/launder.md
- entities/mechanics/prisoner-custody.md
---

# Property and asset retrieval

Property identity/ownership/condition stay in location records, academy operational facts in its faction record, and money in the ledger. These are retrieval pointers, not a second property-title or asset-value ledger. Co-founding/management is not proof of academy premises title. House Ashvale is the source's ownership label, not a newly created organization or inferred personal transfer to Theron.

Estate land includes the historical additional120-acre acquisition paid252gp; total acreage/current appraisal are UNKNOWN. Lodge Phase I and forge72gp/research room28gp/courtyard18gp are already paid facilities, not new payable bills. Do not equate developed lodge with the old hidden woodland lodge. Briarstone is1.4 acres at7 Western Mill Lane with the sourced55gp historical noncash restitution appraisal, vacant/habitable/minor repairs; no rent or municipal rights. Academy current property value/legal premises title, rent terms and later treasury are UNKNOWN. Earlier34gp cash/15gp refundable deposit are independent stale reports, not current personal cash.

Read equipment, horses, wagons and facilities through asset owners below. Never total property and inventory copies of the same asset; do not assign market values. Ashvale wagon identity versus magic expedition wagon and historical horse-name mappings remain unresolved, not extra assets. Vanguard is separate mundane wagon; consumed scale stock is not available inventory. Salvage processing does not establish title. Protected Seven Bells evidence, isolated dangerous material, prisoner possessions, merchant property and third-party deposits remain segregated and unsold. No appraisal becomes spendable cash.


```json
{
  "schema_version": 1,
  "properties": [
    {
      "property_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "fact_owner_ref": "ashvale-estate",
      "legal_owner_id": "theron-ashvale",
      "legal_owner_label": null,
      "manager_id": "tomas",
      "current_market_value_cp": null,
      "cash_inclusion": false,
      "fields_from_owner": [
        "name",
        "location",
        "property_type",
        "land_area",
        "buildings",
        "facilities",
        "improvements",
        "acquisition",
        "historical_price",
        "appraisal",
        "liabilities",
        "maintenance",
        "revenue_sources",
        "legal_restrictions",
        "last_verified_condition"
      ],
      "unknown_field_policy": "UNKNOWN, never inferred or zero",
      "source_refs": [
        "entities/locations/ashvale-estate.md"
      ]
    },
    {
      "property_id": "ashvale-lodge",
      "source_ref": "entities/locations/ashvale-lodge.md",
      "classification": "CONFIRMED CANON",
      "fact_owner_ref": "ashvale-lodge",
      "legal_owner_id": "theron-ashvale",
      "legal_owner_label": null,
      "manager_id": "tomas",
      "current_market_value_cp": null,
      "cash_inclusion": false,
      "fields_from_owner": [
        "name",
        "location",
        "property_type",
        "land_area",
        "buildings",
        "facilities",
        "improvements",
        "acquisition",
        "historical_price",
        "appraisal",
        "liabilities",
        "maintenance",
        "revenue_sources",
        "legal_restrictions",
        "last_verified_condition"
      ],
      "unknown_field_policy": "UNKNOWN, never inferred or zero",
      "source_refs": [
        "entities/locations/ashvale-lodge.md"
      ]
    },
    {
      "property_id": "briarstone-cottage",
      "source_ref": "entities/locations/briarstone-cottage.md",
      "classification": "CONFIRMED CANON",
      "fact_owner_ref": "briarstone-cottage",
      "legal_owner_id": null,
      "legal_owner_label": "House Ashvale",
      "manager_id": null,
      "current_market_value_cp": null,
      "cash_inclusion": false,
      "fields_from_owner": [
        "name",
        "location",
        "property_type",
        "land_area",
        "buildings",
        "facilities",
        "improvements",
        "acquisition",
        "historical_price",
        "appraisal",
        "liabilities",
        "maintenance",
        "revenue_sources",
        "legal_restrictions",
        "last_verified_condition"
      ],
      "unknown_field_policy": "UNKNOWN, never inferred or zero",
      "source_refs": [
        "entities/locations/briarstone-cottage.md"
      ]
    },
    {
      "property_id": "dragon-slayer-academy",
      "source_ref": "entities/factions/dragon-slayer-academy.md",
      "classification": "CONFIRMED CANON",
      "fact_owner_ref": "dragon-slayer-academy",
      "legal_owner_id": null,
      "legal_owner_label": null,
      "manager_id": "master-beren",
      "current_market_value_cp": null,
      "cash_inclusion": false,
      "fields_from_owner": [
        "name",
        "location",
        "property_type",
        "land_area",
        "buildings",
        "facilities",
        "improvements",
        "acquisition",
        "historical_price",
        "appraisal",
        "liabilities",
        "maintenance",
        "revenue_sources",
        "legal_restrictions",
        "last_verified_condition"
      ],
      "unknown_field_policy": "UNKNOWN, never inferred or zero",
      "source_refs": [
        "entities/factions/dragon-slayer-academy.md"
      ]
    }
  ],
  "asset_owner_refs": [
    {
      "entity_id": "ashvale-wagon",
      "source_ref": "entities/items/ashvale-wagon.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "vanguard-wagon",
      "source_ref": "entities/items/vanguard-wagon.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "sovereign-expedition-wagon",
      "source_ref": "entities/items/sovereign-expedition-wagon.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "night-sovereign",
      "source_ref": "entities/items/night-sovereign.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "dragon-scales-stock",
      "source_ref": "entities/items/dragon-scales-stock.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "guild-animal-registry",
      "source_ref": "entities/mechanics/guild-animal-registry.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "seven-bells-inventory",
      "source_ref": "entities/mechanics/seven-bells-inventory.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "shady-salvage",
      "source_ref": "entities/mechanics/shady-salvage.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "launder",
      "source_ref": "entities/mechanics/launder.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    },
    {
      "entity_id": "prisoner-custody",
      "source_ref": "entities/mechanics/prisoner-custody.md",
      "classification": "CONFIRMED CANON",
      "valuation_cp": null,
      "cash_inclusion": false
    }
  ],
  "new_ownership_events": [],
  "new_valuations": [],
  "approved_property_procedures": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-06-economic-approval.md",
    "law_owner_ref": "justice-and-jurisdiction",
    "ledger_ref": "state/finance-ledger.json",
    "procedures": [
      "land-purchase",
      "building-purchase",
      "inheritance",
      "lease",
      "rent",
      "repair",
      "construction",
      "appraisal",
      "property-tax",
      "business-permit",
      "ownership-dispute",
      "secured-obligation",
      "sale",
      "foreclosure",
      "lawful-seizure",
      "transfer-documentation"
    ],
    "transaction_template": {
      "procedure": null,
      "property": null,
      "seller": null,
      "buyer": null,
      "verified_title": null,
      "consideration": null,
      "jurisdiction": null,
      "consent": null,
      "payment_evidence": null,
      "transfer_date": null,
      "original_owner_update": null,
      "ledger_update": null,
      "evidence_refs": null
    },
    "actual_transactions": [],
    "new_holdings": [],
    "automatic_postings": false
  }
}
```

## Phase 2 economic procedures

These are procedures, not executed transfers. Purchase/sale requires willing identified parties, verified title/encumbrances, terms, jurisdiction, consent, payment and dated transfer evidence; update the original property owner and sole ledger once where cash changes. Inheritance instead requires verified decedent/estate, beneficiaries and lawful succession evidence; consideration/payment fields must explicitly document a lawful noncash/not-applicable basis, never invented cash. Leases/rent specify term, permitted use, repair duties, deposits and return conditions; use rights do not convey title. Deposits are segregated refundable liabilities, not earned rent until lawfully applied.

Repairs/construction need accepted scope, authorization, safe labor, permits where applicable, staged evidence and actual payment; commitment, invoice, payment and completion are distinct. Existing completed cottage repairs are already paid; unpaid estate expansion remains unstarted. Appraisals identify date, purpose, method, comparable evidence and uncertainty and never credit cash. Taxes/permits require actual lawful jurisdiction, enacted obligation and documented assessment; no rate, debt or universal levy is enacted here. Unknown jurisdiction remains UNKNOWN, and a realm cannot tax outside its established lawful authority.

Disputes preserve competing claims and evidence without automatic possession changes. Secured obligations require supported local law, consenting creditor/debtor, collateral title, terms and verified registration where required; a design never invents a mortgage. Foreclosure/seizure needs lawful authority, notice, hearing/remedy rights and an actual order/receipt; debt alone does not transfer title. Each case records responsible actors, legal basis, affected property, consideration or explicit lawful noncash basis, dated evidence and original owner/ledger updates where applicable. A populated completeness template proves no title or consent by itself. No actual holdings, valuations, encumbrances or transfers are created.
