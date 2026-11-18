---
id: wayfarers-guild
type: factions
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year848-day196-end-session.md
- archive/session-handoffs/year847-day153-user-handoff.txt
- archive/session-handoffs/year847-day472-user-handoff.txt
- changes/chronicles/year848-day156-end-session.md
---

# Wayfarers Guild — Day156 current canon

SS-41 registry revoked. Specific Crown SS-41 apprehension instruction withdrawn by magistrate; independent other notices not automatically canceled. No new reward. Authority chain: Corvin Dareth → Varian Morthal exceptional countersignature → Selvar Renn receipt → Damaris Keld distribution.


## Historical record before Day156 (superseded only where explicit above)


# Wayfarers’ Guild

Contracts, escorts, expeditions and bounties; Caelthorne HQ with established branches. Existing reporting and registered-contract commission policy preserved; do not apply an extra deduction retrospectively to confirmed payouts.

G-215 escort completed/paid26gp; G-216 ward repair paid32gp; B-83 missing inspector bounty paid40gp. Separate bandit raid22gp cash and approximately6gp estimated forfeited equipment. Already included in later cumulative accounting; do not add again. Merchant-owned goods and evidence not party loot.

## Authoritative update — Year 847 Day 472, 16:10, session ENDED

Day458 main-party measurements are in individual character entities; animal certification in [registry](../mechanics/guild-animal-registry.md). S+ Theron, A+ Lyanna/Garrick/Nyx/Lyra, all Level5. No new guild payment or automatic unlock.

## Guild and contract references — Chunk 5

This structured section belongs to this existing organization. Original prose/frontmatter is unchanged and retains precedence by date. It is not a new guild ledger, branch building, assignment or current contract board. Unknowns are JSON null; paid history is not payable again.

```json
{
  "schema_version": 1,
  "profile": {
    "guild_id": "wayfarers-guild",
    "name": "Wayfarers Guild",
    "organization_type": "independent guild",
    "classification": "CONFIRMED CANON",
    "headquarters_location_id": "caelthorne",
    "branches": [
      {
        "id": "wayfarers-guild:caelthorne-hq",
        "classification": "CONFIRMED CANON",
        "role": "headquarters",
        "settlement_id": "caelthorne",
        "building_location_id": null,
        "responsible_officer_id": null,
        "services": [
          "Contracts",
          "Escorts",
          "Expeditions",
          "Bounties"
        ],
        "contract_board": null,
        "membership_registration": null,
        "supplies_facilities": null,
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
        "operational_status": "Established reference; current opening/capacity/acceptance UNKNOWN",
        "source_refs": [
          "entities/factions/wayfarers-guild.md"
        ],
        "source_quote": "Contracts, escorts, expeditions and bounties; Caelthorne HQ with established branches."
      },
      {
        "id": "wayfarers-guild:unlocated-branches",
        "classification": "CONFIRMED CANON",
        "role": "established-branches-unlocated",
        "settlement_id": null,
        "building_location_id": null,
        "responsible_officer_id": null,
        "services": [],
        "contract_board": null,
        "membership_registration": null,
        "supplies_facilities": null,
        "route_ids": [],
        "operational_status": "Established reference; current opening/capacity/acceptance UNKNOWN",
        "source_refs": [
          "entities/factions/wayfarers-guild.md"
        ],
        "source_quote": "Caelthorne HQ with established branches."
      }
    ],
    "leadership": [],
    "membership_structure": null,
    "services": [
      "Contracts",
      "Escorts",
      "Expeditions",
      "Bounties",
      "Established registration/reference functions; joining process UNKNOWN"
    ],
    "ranks": null,
    "licensing": null,
    "contract_types": [
      "escort",
      "expedition",
      "bounty",
      "ward-repair"
    ],
    "funding": null,
    "commission_policy": {
      "reference_percent": 10,
      "source_ref": "archive/legacy-modules/people/06-v-economic-guild-and-legal-behavior.md",
      "source_quote": "Wayfarers takes 10% on registered contracts",
      "applicability": "Existing registered-contract policy reference; future terms and historical gross/net interpretation require confirmation",
      "retroactive_deductions": false,
      "financial_postings": []
    },
    "jurisdiction": "No automatic police, judicial or extraterritorial powers",
    "other_guild_relationships": null,
    "last_verified_date": null,
    "source_refs": [
      "entities/factions/wayfarers-guild.md",
      "archive/legacy-modules/people/06-v-economic-guild-and-legal-behavior.md",
      "changes/chronicles/guild-concord-contracts-design.md"
    ]
  },
  "contracts": [
    {
      "contract_id": "G-215",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": "wayfarers-guild",
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": "Escort",
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": null,
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": "historical-completed",
      "payment_status": "historically-paid",
      "historical_payment_cp": 2600,
      "historical_application_count": 1,
      "current_availability": "historical-not-current-offer",
      "existing_quest_ref": null,
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ],
      "source_quote": "G-215 escort completed/paid26gp;",
      "last_verified_date": null,
      "last_verified_note": "Existing historical record only; no new acceptance, completion, payment or current offer",
      "funding_source_quote": null
    },
    {
      "contract_id": "G-216",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": "wayfarers-guild",
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": "Ward repair",
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": null,
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": null,
      "payment_status": "historically-paid",
      "historical_payment_cp": 3200,
      "historical_application_count": 1,
      "current_availability": "historical-not-current-offer",
      "existing_quest_ref": null,
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ],
      "source_quote": "G-216 ward repair paid32gp;",
      "last_verified_date": null,
      "last_verified_note": "Existing historical record only; no new acceptance, completion, payment or current offer",
      "funding_source_quote": null
    },
    {
      "contract_id": "B-83",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": "wayfarers-guild",
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": "Missing inspector",
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": null,
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": null,
      "payment_status": "historically-paid",
      "historical_payment_cp": 4000,
      "historical_application_count": 1,
      "current_availability": "historical-not-current-offer",
      "existing_quest_ref": null,
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ],
      "source_quote": "B-83 missing inspector bounty paid40gp.",
      "last_verified_date": null,
      "last_verified_note": "Existing historical record only; no new acceptance, completion, payment or current offer",
      "funding_source_quote": null
    },
    {
      "contract_id": "SS-41",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": null,
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": null,
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": null,
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": null,
      "payment_status": "unknown",
      "historical_payment_cp": null,
      "historical_application_count": 0,
      "current_availability": "revoked-specific-notice",
      "existing_quest_ref": "first-oath-conspiracy",
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ],
      "source_quote": "SS-41 registry revoked. Specific Crown SS-41 apprehension instruction withdrawn by magistrate; independent other notices not automatically canceled.",
      "last_verified_date": null,
      "last_verified_note": "Existing historical record only; no new acceptance, completion, payment or current offer",
      "funding_source_quote": null
    },
    {
      "contract_id": "WG-848-196-EASTRUN",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": null,
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": "Eastrun Road Bandit Capture",
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": [
        "garrick-vale",
        "nyx-thorne"
      ],
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": "session-completed",
      "payment_status": "session-paid",
      "historical_payment_cp": null,
      "historical_application_count": 0,
      "current_availability": "completed-not-current-offer",
      "existing_quest_ref": null,
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "changes/chronicles/year848-day196-end-session.md"
      ],
      "source_quote": "Two wanted robbers were taken alive and lawfully transferred.",
      "last_verified_date": "Year 848 Day 196",
      "last_verified_note": "Verified by session close. Exact completion date, route, funding and underlying legal documents are unknown.",
      "funding_source_quote": null
    },
    {
      "contract_id": "WG-848-196-BRIARFALL",
      "classification": "CONFIRMED CANON",
      "issuing_organization_id": null,
      "registry_organization_id": "wayfarers-guild",
      "funding_party_id": null,
      "funding_party_name": null,
      "funding_source_ref": null,
      "funding_committed_cp": null,
      "objective": "Briarfall Missing Caravan Investigation",
      "location_id": null,
      "difficulty": null,
      "eligibility_requirements": null,
      "legal_authorization_ref": null,
      "apprehension_authorized": false,
      "acceptance_status": null,
      "assigned_party_ids": [
        "garrick-vale",
        "nyx-thorne"
      ],
      "deadline": null,
      "reward_cp": null,
      "reward_guaranteed": false,
      "expenses_fees": null,
      "evidence_requirements": null,
      "completion_conditions": null,
      "completion_status": "session-completed",
      "payment_status": "session-paid",
      "historical_payment_cp": null,
      "historical_application_count": 0,
      "current_availability": "completed-not-current-offer",
      "existing_quest_ref": null,
      "independent_notices_cancelled": false,
      "financial_postings": [],
      "source_refs": [
        "changes/chronicles/year848-day196-end-session.md"
      ],
      "source_quote": "The missing caravan was located, surviving merchants were escorted, and stolen cargo was returned to its owners.",
      "last_verified_date": "Year 848 Day 196",
      "last_verified_note": "Verified by session close. Exact completion date, route, funding and underlying legal documents are unknown.",
      "funding_source_quote": null
    }
  ],
  "new_memberships": [],
  "license_changes": [],
  "new_contracts": [],
  "automatic_financial_postings": false
}
```

## Day 182–196 completed contracts

Both new contracts are recorded in the registry below. Gross rewards and deductions are in the [sole finance ledger](../../state/finance-ledger.json). The earlier SS-41 withdrawal and paid records retain their existing status.
