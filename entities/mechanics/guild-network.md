---
id: guild-network
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/guild-concord-contracts-design.md
- entities/factions/wayfarers-guild.md
- entities/factions/dragon-slayer-academy.md
- archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md
- entities/factions/northern-provisioning-consortium.md
---

# Guild identity and relationship crosswalk

Routing/classification authority only. Canon profiles and contracts belong to their existing faction owners. Archived design rows do not create new operational guilds, halls, officers or branches. Classification vocabulary also supports historical organizations and unknown identities, but no unsourced instance is invented. Proposed Continental Guild Concord is a legitimate federation design, not identified with any criminal conspiracy or existing faction. Overlapping functions never prove organizational identity, subordination or membership.

```json
{
  "schema_version": 1,
  "classifications": [
    "CONFIRMED CANON",
    "HISTORICAL ORGANIZATION",
    "ARCHIVED DESIGN",
    "PROPOSED",
    "UNKNOWN IDENTITY",
    "REQUIRES APPROVAL"
  ],
  "profile_owner_ids": [
    "wayfarers-guild",
    "dragon-slayer-academy"
  ],
  "organizations": [
    {
      "id": "wayfarers-guild",
      "entity_id": "wayfarers-guild",
      "classification": "CONFIRMED CANON",
      "organization_type": "guild",
      "archived_name": null,
      "archived_site_labels": [],
      "compatibility": "Independent guild; proposed Concord coordination cannot replace its authority",
      "approval_status": null,
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ]
    },
    {
      "id": "dragon-slayer-academy",
      "entity_id": "dragon-slayer-academy",
      "classification": "CONFIRMED CANON",
      "organization_type": "academy",
      "archived_name": null,
      "archived_site_labels": [],
      "compatibility": "Independent academy; no Concord membership or leadership transfer",
      "approval_status": null,
      "source_refs": [
        "entities/factions/dragon-slayer-academy.md"
      ]
    },
    {
      "id": "northern-provisioning-consortium",
      "entity_id": "northern-provisioning-consortium",
      "classification": "CONFIRMED CANON",
      "organization_type": "professional procurement organization, not automatically a guild",
      "archived_name": null,
      "archived_site_labels": [],
      "compatibility": "Original owner remains authoritative; not automatically a Concord member or active supplier",
      "approval_status": null,
      "source_refs": [
        "entities/factions/northern-provisioning-consortium.md"
      ]
    },
    {
      "id": "archived:ironhand",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "Ironhand Smiths’ Compact",
      "archived_site_labels": [
        "Ironhollow",
        "Caelthorne chapter"
      ],
      "compatibility": "Craft/material provenance overlap; no merger",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    },
    {
      "id": "archived:seven-lamps",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "Circle of Seven Lamps",
      "archived_site_labels": [
        "Caelthorne",
        "Blackthorn healers’ affiliate"
      ],
      "compatibility": "Healing overlap; no forced membership",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    },
    {
      "id": "archived:scribes",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "Scribes’ Collegium",
      "archived_site_labels": [
        "Caelthorne",
        "vault archive offices"
      ],
      "compatibility": "Records overlap; no new access rights",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    },
    {
      "id": "archived:river-charter",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "River Charter League",
      "archived_site_labels": [
        "Rivermere",
        "Southbank Landing"
      ],
      "compatibility": "Transport/trade overlap; no new toll authority",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    },
    {
      "id": "archived:greenward",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "Greenward Covenant",
      "archived_site_labels": [
        "Elderwood/Silverbrook"
      ],
      "compatibility": "Ranger/spirit work overlap; local customs not superseded",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    },
    {
      "id": "archived:stonewatch",
      "entity_id": null,
      "classification": "ARCHIVED DESIGN",
      "organization_type": "archived professional organization design",
      "archived_name": "Stonewatch Wardens",
      "archived_site_labels": [
        "Blackthorn",
        "northern roads"
      ],
      "compatibility": "Rescue/patrol overlap; not automatically Blackthorn Watch or a justice authority",
      "approval_status": "REQUIRES APPROVAL",
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ]
    }
  ],
  "branch_candidates": [
    {
      "id": "branch-proposal:wayfarers-eastrun",
      "guild_id": "wayfarers-guild",
      "candidate_settlement_id": "eastrun",
      "classification": "ARCHIVED DESIGN",
      "building_location_id": null,
      "responsible_officer_id": null,
      "operational_status": "UNVERIFIED — NOT AN OPERATIONAL BRANCH ASSERTION",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ],
      "note": "Archived named branch candidate; current entity confirms unnamed branches, not this specific site. No premises, staff, supplies, opening or fees inferred."
    },
    {
      "id": "branch-proposal:wayfarers-briarfall-crossing",
      "guild_id": "wayfarers-guild",
      "candidate_settlement_id": "briarfall-crossing",
      "classification": "ARCHIVED DESIGN",
      "building_location_id": null,
      "responsible_officer_id": null,
      "operational_status": "UNVERIFIED — NOT AN OPERATIONAL BRANCH ASSERTION",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ],
      "note": "Archived named branch candidate; current entity confirms unnamed branches, not this specific site. No premises, staff, supplies, opening or fees inferred."
    },
    {
      "id": "branch-proposal:wayfarers-rivermere",
      "guild_id": "wayfarers-guild",
      "candidate_settlement_id": "rivermere",
      "classification": "ARCHIVED DESIGN",
      "building_location_id": null,
      "responsible_officer_id": null,
      "operational_status": "UNVERIFIED — NOT AN OPERATIONAL BRANCH ASSERTION",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "archive/legacy-modules/world/06-6-guilds-factions-and-local-operations.md"
      ],
      "note": "Archived named branch candidate; current entity confirms unnamed branches, not this specific site. No premises, staff, supplies, opening or fees inferred."
    }
  ],
  "concord_proposal_id": "continental-guild-concord",
  "automatic_financial_postings": false
}
```
