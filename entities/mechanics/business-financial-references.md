---
id: business-financial-references
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/economy-framework-maintenance.md
- state/finance-ledger.json
- entities/mechanics/party-finances.md
- archive/checkpoints/year848-day137-finance-ledger.json
- entities/locations/ashvale-estate.md
- entities/locations/ashvale-lodge.md
- entities/locations/briarstone-cottage.md
- entities/factions/dragon-slayer-academy.md
- entities/locations/brackenford.md
- entities/mechanics/settlement-services.md
---

# Business financial retrieval

Fourteen existing parent-scoped service records, not fourteen new businesses or cash accounts. Resolve owner/manager/operator, staff, services, restrictions and price evidence from each original parent. Unknown proprietors remain unknown. The estate owns premises, not participating merchant stock. Beren remains independent academy manager; this table appoints nobody.

For future receipt/expense evidence support business_id, parent property, owner/manager/operator source, category, period, amount, ownership scope, status, source event and ledger transaction reference. Unknown current amounts below are null, never zero income or guaranteed profit. Historical receipt links are aggregate modeled category evidence, not evidence every linked business received a particular amount; Lantern Exchange has no separately certified receipt. Hospitality rooms/meals/stabling stay one record; avoid allocating the same combined category to several businesses. Rental cottage venue is distinct from vacant Briarstone Cottage.

Expense categories are reusable possibilities; staff wage expense is already included in the modeled operating periods. No daily income, automatic monthly surplus, hire, charge or sale arises from these references. Future business reports need actual receipts/expenses or explicit player-approved reconstruction. Stock held, merchant sales, contracted work and available capacity do not establish received revenue.


```json
{
  "schema_version": 1,
  "businesses": [
    {
      "business_id": "brackenford:willow-lantern",
      "parent_location_id": "brackenford",
      "source_ref": "entities/locations/brackenford.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": null,
      "historical_qualification": "UNKNOWN",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "brackenford:forge",
      "parent_location_id": "brackenford",
      "source_ref": "entities/locations/brackenford.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": null,
      "historical_qualification": "UNKNOWN",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "brackenford:herbalist",
      "parent_location_id": "brackenford",
      "source_ref": "entities/locations/brackenford.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": null,
      "historical_qualification": "UNKNOWN",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "brackenford:watermill",
      "parent_location_id": "brackenford",
      "source_ref": "entities/locations/brackenford.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": null,
      "historical_qualification": "UNKNOWN",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "brackenford:market",
      "parent_location_id": "brackenford",
      "source_ref": "entities/locations/brackenford.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": null,
      "historical_qualification": "UNKNOWN",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:healing-springs",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:merchant-storage",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:rental-cottages",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:bakery",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:market",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": "entities/locations/ashvale-estate.md",
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:lantern-exchange",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-estate:caravan-facilities",
      "parent_location_id": "ashvale-estate",
      "source_ref": "entities/locations/ashvale-estate.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-lodge:hospitality",
      "parent_location_id": "ashvale-lodge",
      "source_ref": "entities/locations/ashvale-lodge.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    },
    {
      "business_id": "ashvale-lodge:forge",
      "parent_location_id": "ashvale-lodge",
      "source_ref": "entities/locations/ashvale-lodge.md",
      "classification": "CONFIRMED CANON",
      "identity_fields_from_owner": [
        "owner_id",
        "manager_id",
        "operator_id",
        "staff_ids",
        "staff_notes",
        "services",
        "prices",
        "source_refs"
      ],
      "revenue_categories_from_owner": true,
      "expense_categories_ref": "economy-accounting",
      "historical_receipts_ref": "archive/checkpoints/year848-day137-finance-ledger.json",
      "historical_qualification": "Aggregate modeled categories only; no fabricated individual receipt attribution",
      "current_receipts_cp": null,
      "current_expenses_cp": null,
      "commission_policy_ref": null,
      "automatic_revenue": false
    }
  ],
  "automatic_postings": false
}
```
