---
id: justice-authorities
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/justice-courts-prisons-design.md
- entities/locations/caelthorne.md
- entities/locations/brackenford.md
- entities/locations/blackthorn-watch.md
- entities/factions/wayfarers-guild.md
- entities/locations/ashvale-estate.md
---

# Existing justice authority references

Scoped IDs below identify existing functions, not new organizations. Headquarters, stations, detention powers, boundaries and receiving officers remain unknown unless sourced. Magistrates/watch/council/command/contract/private roles are distinct. Leadership references preserve existing responsibilities and do not appoint receiving officers. Citizen intervention and adventurer rank confer no automatic police powers. Government labels describe source context only; Vellorin's political type and Valedorn's relationship remain unknown.

```json
{
  "schema_version": 1,
  "authorities": [
    {
      "id": "justice:caelthorne-magistrates",
      "name": "Existing Caelthorne magistrates",
      "classification": "CONFIRMED CANON",
      "authority_kind": "judicial",
      "government_affiliation": "Crown administrative context; nation and external boundaries unverified",
      "jurisdiction_location_ids": [
        "caelthorne"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing magistrate review function; precise powers require case source"
      ],
      "limitations": [
        "No new court building, judge, extraterritorial warrant or blanket authority"
      ],
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/caelthorne.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/caelthorne.md",
          "quote": "Crown administrative center with magistrates, watch and archives."
        }
      ]
    },
    {
      "id": "justice:caelthorne-watch",
      "name": "Existing Caelthorne watch",
      "classification": "CONFIRMED CANON",
      "authority_kind": "civilian-law-enforcement",
      "government_affiliation": "Existing local Crown context",
      "jurisdiction_location_ids": [
        "caelthorne"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing watch function; exact arrest/detention powers UNKNOWN"
      ],
      "limitations": [
        "No verified station address, receiving officer or prison capacity"
      ],
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/caelthorne.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/caelthorne.md",
          "quote": "Crown administrative center with magistrates, watch and archives."
        }
      ]
    },
    {
      "id": "justice:brackenford-government",
      "name": "Brackenford reeve and council",
      "classification": "CONFIRMED CANON",
      "authority_kind": "civil-government",
      "government_affiliation": "Existing village governance",
      "jurisdiction_location_ids": [
        "brackenford"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing communal village governance"
      ],
      "limitations": [
        "Cottage ownership grants no municipal powers; external jurisdiction UNKNOWN"
      ],
      "leadership_ids": [
        "elsbeth-marrin"
      ],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Village government reeve and council."
        }
      ]
    },
    {
      "id": "justice:brackenford-watch",
      "name": "Brackenford watch",
      "classification": "CONFIRMED CANON",
      "authority_kind": "civilian-law-enforcement",
      "government_affiliation": "Existing village watch",
      "jurisdiction_location_ids": [
        "brackenford"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing village watch function"
      ],
      "limitations": [
        "Six part-time members; exact patrol boundary, gaol and receiving officer UNKNOWN"
      ],
      "leadership_ids": [
        "ressa-vale"
      ],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/brackenford.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/brackenford.md",
          "quote": "Watch captain Ressa Vale45 human with six part-time watch members."
        }
      ]
    },
    {
      "id": "justice:blackthorn-command",
      "name": "Blackthorn watch command",
      "classification": "CONFIRMED CANON",
      "authority_kind": "military-watch",
      "government_affiliation": "Affiliation beyond existing watch context UNKNOWN",
      "jurisdiction_location_ids": [
        "blackthorn-watch"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing watch, refuge and healing functions"
      ],
      "limitations": [
        "Military/watch command is not automatically civilian judicial authority; current commander/receiving officer UNKNOWN"
      ],
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/blackthorn-watch.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/blackthorn-watch.md",
          "quote": "Watch command and refuge/healing services;"
        }
      ]
    },
    {
      "id": "justice:wayfarers-contracts",
      "name": "Wayfarers contractual administration",
      "classification": "CONFIRMED CANON",
      "authority_kind": "guild-contractual",
      "government_affiliation": "Guild contractual context; not a government",
      "jurisdiction_location_ids": [],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Registered contract/report administration"
      ],
      "limitations": [
        "No automatic police power, criminal sentencing or immunity; no retrospective fee"
      ],
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/factions/wayfarers-guild.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/factions/wayfarers-guild.md",
          "quote": "Contracts, escorts, expeditions and bounties; Caelthorne HQ with established branches."
        }
      ]
    },
    {
      "id": "justice:ashvale-private-security",
      "name": "Ashvale estate private management/security",
      "classification": "CONFIRMED CANON",
      "authority_kind": "private-security",
      "government_affiliation": "Private estate under existing Crown law",
      "jurisdiction_location_ids": [
        "ashvale-estate"
      ],
      "jurisdiction_boundary": null,
      "legal_powers": [
        "Existing estate management and security"
      ],
      "limitations": [
        "No municipal charter, royal police power or prison authority from ownership/reputation"
      ],
      "leadership_ids": [
        "tomas"
      ],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "source_refs": [
        "entities/locations/ashvale-estate.md"
      ],
      "evidence": [
        {
          "source_ref": "entities/locations/ashvale-estate.md",
          "quote": "Privately managed commercial settlement, no separate municipal charter."
        }
      ]
    }
  ],
  "protected_official_ids": [
    "mara-vey",
    "aldric-voss",
    "ressa-vale",
    "elsbeth-marrin"
  ],
  "verified_receiving_facilities": [],
  "automatic_custody_actions": false
}
```
