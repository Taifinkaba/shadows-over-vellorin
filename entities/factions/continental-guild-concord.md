---
id: continental-guild-concord
type: factions
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/guild-concord-contracts-design.md
---

# Continental Guild Concord — proposal

PROPOSED federation coordinating independent guilds, not replacing their authorities, histories, memberships or finances. Not operational; no country/continent-wide jurisdiction, headquarters, branches, treasury, staff, members or licenses established. These names describe divisions for review only. Approval of this design does not complete a historical examination, activate a branch or fund a reward.

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "operational": false,
  "approval_status": "REQUIRES APPROVAL",
  "approval_source_ref": null,
  "headquarters_location_id": null,
  "branch_location_ids": [],
  "leadership_ids": [],
  "member_organization_ids": [],
  "treasury_cp": null,
  "membership_fee_cp": null,
  "exam_fee_cp": null,
  "commission_percent": null,
  "divisions": [
    {
      "id": "concord-division:adventurers",
      "name": "Adventurers Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Exploration, escorts and rescue coordination"
      ],
      "membership_requirements": [
        "Identity/competence review relevant to chosen work"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Exploration, escorts and rescue coordination"
      ],
      "contract_types": [
        "Escort",
        "Exploration",
        "Rescue"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "wayfarers-guild"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:monster-hunters",
      "name": "Monster Hunters Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Demonstrated threat assessment and lawful monster-related work"
      ],
      "membership_requirements": [
        "Relevant tracking/safety/containment demonstration, not inherited combat rank"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Demonstrated threat assessment and lawful monster-related work"
      ],
      "contract_types": [
        "Monster removal",
        "Hazard containment"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "wayfarers-guild",
        "archived:stonewatch"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:bounty-hunters",
      "name": "Bounty Hunters Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Verify notices, legal limits, evidence and humane handover"
      ],
      "membership_requirements": [
        "Notice/warrant knowledge and lawful apprehension/custody demonstration"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Verify notices, legal limits, evidence and humane handover"
      ],
      "contract_types": [
        "Authorized bounty work"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "wayfarers-guild"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:merchants",
      "name": "Merchants Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Trade records, contracts and provenance"
      ],
      "membership_requirements": [
        "Trade/accounting competency, not monster combat"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Trade records, contracts and provenance"
      ],
      "contract_types": [
        "Trade support",
        "Supply coordination"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "archived:river-charter"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:craftsmen",
      "name": "Craftsmen Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Craft quality and material provenance"
      ],
      "membership_requirements": [
        "Relevant practical craft demonstration"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Craft quality and material provenance"
      ],
      "contract_types": [
        "Repair",
        "Craft commission"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "archived:ironhand"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:healers",
      "name": "Healers Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Consent-based care, professional competence and referral"
      ],
      "membership_requirements": [
        "Relevant healing/herbal practice assessment and safety"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Consent-based care, professional competence and referral"
      ],
      "contract_types": [
        "Medical support",
        "Escort care"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "archived:seven-lamps",
        "dragon-slayer-academy"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:dungeon-registrars",
      "name": "Dungeon Registrars Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Record site identity, permits, surveys and exploration reports"
      ],
      "membership_requirements": [
        "Recordkeeping, map and safety assessment"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Record site identity, permits, surveys and exploration reports"
      ],
      "contract_types": [
        "Survey",
        "Mapping",
        "Research"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "wayfarers-guild",
        "archived:scribes"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    },
    {
      "id": "concord-division:transport-navigators",
      "name": "Transport and Navigators Division",
      "classification": "PROPOSED",
      "responsibilities": [
        "Route planning, cargo care and navigation"
      ],
      "membership_requirements": [
        "Relevant transport/navigation competence"
      ],
      "licensing": "Profession-specific design; actual credential, validity, fees and authority UNKNOWN",
      "ranking": "Profession-specific assessment design; labels/thresholds unapproved and independent of combat power",
      "services": [
        "Route planning, cargo care and navigation"
      ],
      "contract_types": [
        "Caravan escort",
        "Navigation",
        "Transport"
      ],
      "funding_model": "Proposed disclosed dues/service funding and identified client escrow where agreed; no amount, treasury or guarantee established",
      "regional_representation": "Proposed independent local representation; territories, delegates, branches and agreements UNKNOWN",
      "existing_guild_relationship_ids": [
        "wayfarers-guild",
        "archived:river-charter"
      ],
      "legal_limitations": "No automatic police, judicial, national or cross-border authority; participating guilds retain independence",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/guild-concord-contracts-design.md"
      ]
    }
  ],
  "financial_postings": []
}
```
