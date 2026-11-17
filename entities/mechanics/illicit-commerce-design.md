---
id: illicit-commerce-design
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-04-guild-underworld-approval.md
---

# Finite illicit commerce design

Safe economic contexts and an empty prospective template only. No functioning market, dealer, stolen object, secret route, debt, payment, price, inventory or second ledger. Current crime and legal guilt require evidence; public safety excludes covert particulars.

```json
{
  "schema_version": 1,
  "classification": "APPROVED DESIGN",
  "approval_source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md",
  "finance_ledger_ref": "state/finance-ledger.json",
  "finance_owner_ref": "party-finances",
  "legal_owner_ref": "justice-and-jurisdiction",
  "trade_owner_ref": "settlement-trade",
  "communication_owner_ref": "settlement-communications",
  "contexts": [
    {
      "id": "illicit-context:stolen-goods",
      "classification": "PROPOSED",
      "description": "Tangible goods with disputed/stolen title",
      "finite_dependencies": "Actual goods, lawful original-owner evidence, buyers, safe storage and transport; theft does not confer title.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:counterfeit-documents",
      "classification": "PROPOSED",
      "description": "False documents or credentials",
      "finite_dependencies": "Actual document/materials and finite skilled time; no forged permit becomes lawful authority.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:smuggled-cargo",
      "classification": "PROPOSED",
      "description": "Cargo movement contrary to proved applicable restrictions",
      "finite_dependencies": "Actual cargo, willing carriers, compatible verified routes, storage and knowledge of the applicable rule; no channel is mapped.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:restricted-ingredients",
      "classification": "PROPOSED",
      "description": "Restricted botanical or magical ingredients",
      "finite_dependencies": "Finite habitat/materials, lawful access barriers, correct identification, storage and existing magical limits; no stock generated.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:illegal-mining-materials",
      "classification": "PROPOSED",
      "description": "Unlawfully extracted ore or stone",
      "finite_dependencies": "Actual materials, provenance, labor/fuel, safe handling and transport; no new mine/deposit.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:forged-certifications",
      "classification": "PROPOSED",
      "description": "Fraudulent craft or trade certification",
      "finite_dependencies": "A real disputed claim, document, assessor evidence and willing counterparties; no automatic credibility or license.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:unlawful-gambling",
      "classification": "PROPOSED",
      "description": "Unlawful or coercive games and stakes",
      "finite_dependencies": "Finite adult stakes, actual consent/status and applicable law; no automatic winnings, debts or house income.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:extortion",
      "classification": "PROPOSED",
      "description": "Coercive demands for property or work",
      "finite_dependencies": "An actual demand/actor and victim account would need evidence; no payment, control, lawful title or contract is created.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:illicit-information",
      "classification": "PROPOSED",
      "description": "Unlawfully acquired records or claims",
      "finite_dependencies": "Actual access, provenance, reliability and lawful disclosure limits; no confidential informant or secret content stored publicly.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:criminal-debt",
      "classification": "PROPOSED",
      "description": "Coercive or fraudulent claimed obligations",
      "finite_dependencies": "Actual parties, terms and evidence; debt bondage and violence are not enforceable normal commerce. No debt imposed.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:bribery",
      "classification": "PROPOSED",
      "description": "Improper inducement and abuse of entrusted office",
      "finite_dependencies": "Specific lawful authority, actual offer/benefit, finite funds and evidence; no official is declared corrupt.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    },
    {
      "id": "illicit-context:fraudulent-transactions",
      "classification": "PROPOSED",
      "description": "Deliberately false commercial claims",
      "finite_dependencies": "Actual representations, actors, goods/title, loss and independent evidence; no profit or successful concealment assumed.",
      "current_seller": null,
      "current_buyer": null,
      "current_inventory": null,
      "current_price_cp": null,
      "actual_events": []
    }
  ],
  "transaction_template": {
    "event_id": null,
    "status": "proposed",
    "seller_ref": null,
    "buyer_ref": null,
    "goods_or_service": null,
    "ownership_provenance_ref": null,
    "quantity": null,
    "quoted_price_cp": null,
    "available_funds_evidence_ref": null,
    "transport_route_refs": [],
    "storage_or_delivery_terms": null,
    "jurisdiction_and_legal_risk": null,
    "consent_or_coercion_evidence_ref": null,
    "event_evidence_ref": null,
    "source_refs": [],
    "finance_transaction_ref": null
  },
  "procedure": "Before any actual event establish seller, buyer, goods/service, title/provenance, finite quantity/funds, price, transport/handling, lawful risks and independently sourced event evidence. Proposals and coercive demands create no accepted contract, lawful ownership, money, shipment or successful crime. Record real resource effects once in original authorities, never in this design record.",
  "actual_transactions": [],
  "current_market_locations": null,
  "current_suppliers": null,
  "current_cash_cp": null,
  "automatic_postings": false
}
```
