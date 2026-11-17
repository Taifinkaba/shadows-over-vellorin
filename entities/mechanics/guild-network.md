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
- changes/chronicles/phase2-04-guild-underworld-approval.md
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
  "automatic_financial_postings": false,
  "approved_design_index": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md",
    "professional_guild_ids": [
      "ironhand-smiths-compact",
      "circle-of-seven-lamps",
      "scribes-collegium",
      "river-charter-league",
      "greenward-covenant",
      "stonewatch-wardens"
    ],
    "criminal_faction_ids": [
      "gilded-hand",
      "thornless-circle",
      "black-pick-syndicate",
      "sable-current",
      "red-antler-brotherhood",
      "veiled-coin-exchange",
      "broken-seal-society",
      "nightglass-circle"
    ],
    "archive_promotions": [
      {
        "archived_id": "archived:ironhand",
        "entity_id": "ironhand-smiths-compact",
        "classification": "APPROVED DESIGN"
      },
      {
        "archived_id": "archived:seven-lamps",
        "entity_id": "circle-of-seven-lamps",
        "classification": "APPROVED DESIGN"
      },
      {
        "archived_id": "archived:scribes",
        "entity_id": "scribes-collegium",
        "classification": "APPROVED DESIGN"
      },
      {
        "archived_id": "archived:river-charter",
        "entity_id": "river-charter-league",
        "classification": "APPROVED DESIGN"
      },
      {
        "archived_id": "archived:greenward",
        "entity_id": "greenward-covenant",
        "classification": "APPROVED DESIGN"
      },
      {
        "archived_id": "archived:stonewatch",
        "entity_id": "stonewatch-wardens",
        "classification": "APPROVED DESIGN"
      }
    ],
    "concord_owner_ref": "continental-guild-concord",
    "rules_owner_ref": "guild-membership-and-contracts",
    "illicit_economy_owner_ref": "illicit-commerce-design",
    "activity_owner_ref": "faction-activity",
    "settlement_links": [
      {
        "settlement_id": "caelthorne",
        "classification": "PROPOSED",
        "industry_ids": [
          "caelthorne:industry-civic-services",
          "caelthorne:industry-luxury-crafts"
        ],
        "business_ids": [
          "caelthorne:crownstep-exchange",
          "caelthorne:lampwright-house",
          "caelthorne:hearthbell-inn",
          "caelthorne:three-copper-cups",
          "caelthorne:amber-curtain",
          "caelthorne:blue-thimble"
        ],
        "guild_candidate_ids": [
          "circle-of-seven-lamps",
          "scribes-collegium",
          "ironhand-smiths-compact"
        ],
        "criminal_pressure_candidate_ids": [
          "gilded-hand",
          "broken-seal-society"
        ],
        "trade_dependency_ids": [
          "trade:eastrun--caelthorne",
          "trade:ironhollow-hold--caelthorne",
          "trade:rivermere--caelthorne",
          "trade:caelthorne--rivermere",
          "trade:stoneford--caelthorne"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "eastrun",
        "classification": "PROPOSED",
        "industry_ids": [
          "eastrun:industry-grain",
          "eastrun:industry-animals"
        ],
        "business_ids": [
          "eastrun:bushel-and-bridle",
          "eastrun:oat-crown-yard",
          "eastrun:millrace-iron",
          "eastrun:orchard-rest",
          "eastrun:green-measure"
        ],
        "guild_candidate_ids": [
          "river-charter-league",
          "stonewatch-wardens"
        ],
        "criminal_pressure_candidate_ids": [
          "gilded-hand",
          "red-antler-brotherhood"
        ],
        "trade_dependency_ids": [
          "trade:eastrun--caelthorne",
          "trade:briarfall-crossing--eastrun",
          "trade:brackenford--eastrun",
          "trade:windmere--eastrun",
          "trade:eastrun--ironhollow-hold"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "briarfall-crossing",
        "classification": "PROPOSED",
        "industry_ids": [
          "briarfall-crossing:industry-wood",
          "briarfall-crossing:industry-wagons"
        ],
        "business_ids": [
          "briarfall-crossing:copper-hoop-yard",
          "briarfall-crossing:sawyers-table",
          "briarfall-crossing:bridge-rest",
          "briarfall-crossing:fern-and-kettle"
        ],
        "guild_candidate_ids": [
          "greenward-covenant",
          "stonewatch-wardens",
          "ironhand-smiths-compact"
        ],
        "criminal_pressure_candidate_ids": [
          "thornless-circle",
          "gilded-hand"
        ],
        "trade_dependency_ids": [
          "trade:briarfall-crossing--eastrun",
          "trade:silverbrook--briarfall-crossing"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "rivermere",
        "classification": "PROPOSED",
        "industry_ids": [
          "rivermere:industry-shipping",
          "rivermere:industry-fish",
          "rivermere:industry-textiles"
        ],
        "business_ids": [
          "rivermere:reedseal-stores",
          "rivermere:net-and-needle",
          "rivermere:saltbell-kitchen",
          "rivermere:river-lantern",
          "rivermere:nine-knots"
        ],
        "guild_candidate_ids": [
          "river-charter-league",
          "scribes-collegium"
        ],
        "criminal_pressure_candidate_ids": [
          "sable-current",
          "veiled-coin-exchange"
        ],
        "trade_dependency_ids": [
          "trade:rivermere--caelthorne",
          "trade:caelthorne--rivermere",
          "trade:southbank-landing--rivermere",
          "trade:rivermere--windmere"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "ironhollow-hold",
        "classification": "PROPOSED",
        "industry_ids": [
          "ironhollow-hold:industry-metals",
          "ironhollow-hold:industry-stone"
        ],
        "business_ids": [
          "ironhollow-hold:true-spark",
          "ironhollow-hold:plumbline-yard",
          "ironhollow-hold:hearthgate-provisions",
          "ironhollow-hold:clan-road-rest"
        ],
        "guild_candidate_ids": [
          "ironhand-smiths-compact",
          "scribes-collegium"
        ],
        "criminal_pressure_candidate_ids": [
          "black-pick-syndicate",
          "veiled-coin-exchange"
        ],
        "trade_dependency_ids": [
          "trade:ironhollow-hold--caelthorne",
          "trade:eastrun--ironhollow-hold"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "brackenford",
        "classification": "PROPOSED",
        "industry_ids": [
          "brackenford:industry-farm-mill",
          "brackenford:industry-services"
        ],
        "business_ids": [
          "brackenford:willow-lantern",
          "brackenford:forge",
          "brackenford:herbalist",
          "brackenford:watermill",
          "brackenford:market"
        ],
        "guild_candidate_ids": [
          "stonewatch-wardens",
          "ironhand-smiths-compact",
          "greenward-covenant"
        ],
        "criminal_pressure_candidate_ids": [
          "gilded-hand",
          "red-antler-brotherhood"
        ],
        "trade_dependency_ids": [
          "trade:brackenford--eastrun"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "silverbrook",
        "classification": "PROPOSED",
        "industry_ids": [
          "silverbrook:industry-woodland"
        ],
        "business_ids": [
          "silverbrook:honeycomb-bench",
          "silverbrook:green-spoon",
          "silverbrook:leafmark-yard"
        ],
        "guild_candidate_ids": [
          "greenward-covenant",
          "circle-of-seven-lamps"
        ],
        "criminal_pressure_candidate_ids": [
          "thornless-circle",
          "nightglass-circle"
        ],
        "trade_dependency_ids": [
          "trade:silverbrook--briarfall-crossing"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "stoneford",
        "classification": "PROPOSED",
        "industry_ids": [
          "stoneford:industry-quarry"
        ],
        "business_ids": [
          "stoneford:straightedge-yard",
          "stoneford:fordpantry",
          "stoneford:resting-plumb"
        ],
        "guild_candidate_ids": [
          "ironhand-smiths-compact",
          "stonewatch-wardens"
        ],
        "criminal_pressure_candidate_ids": [
          "black-pick-syndicate",
          "veiled-coin-exchange"
        ],
        "trade_dependency_ids": [
          "trade:stoneford--caelthorne"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "southbank-landing",
        "classification": "PROPOSED",
        "industry_ids": [
          "southbank-landing:industry-river-food"
        ],
        "business_ids": [
          "southbank-landing:grainstep-stores",
          "southbank-landing:reed-oar",
          "southbank-landing:netmenders-bowl",
          "southbank-landing:banklight-ledger"
        ],
        "guild_candidate_ids": [
          "river-charter-league",
          "scribes-collegium"
        ],
        "criminal_pressure_candidate_ids": [
          "sable-current",
          "broken-seal-society"
        ],
        "trade_dependency_ids": [
          "trade:southbank-landing--rivermere"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      },
      {
        "settlement_id": "windmere",
        "classification": "PROPOSED",
        "industry_ids": [
          "windmere:industry-pastoral"
        ],
        "business_ids": [
          "windmere:wool-and-salt",
          "windmere:shearers-hearth"
        ],
        "guild_candidate_ids": [
          "greenward-covenant",
          "river-charter-league",
          "stonewatch-wardens"
        ],
        "criminal_pressure_candidate_ids": [
          "red-antler-brotherhood",
          "gilded-hand"
        ],
        "trade_dependency_ids": [
          "trade:windmere--eastrun",
          "trade:rivermere--windmere"
        ],
        "scope_condition": "Prospective commercial tensions/referrals only. Unknown realm assignment, current faction presence and unsurveyed roads remain unknown. These candidates do not expand a regional faction’s verified scope or assign a proprietor/member.",
        "potential_relationships": "Professional training, title/material checks, voluntary referrals and lawful protection may encounter disputed documents, illicit goods or coercive demands, but no actual business contract, pressure, crime or guild affiliation exists by this record.",
        "actual_affiliations": [],
        "actual_events": []
      }
    ],
    "actual_memberships": [],
    "actual_events": []
  }
}
```

## Phase 2 approved design routing

The original archived rows are a dated source crosswalk. approved_design_index now promotes those same six concepts to one authoritative entity each, without creating a second identity. It separately routes eight criminal designs and prospective ten-settlement links. The old branch and confirmed-owner fields remain unchanged. No new membership, current supplier, route, actual branch or crime is established.
