---
id: justice-proposals
type: mechanics
status: research
visibility: gm-reference
source_refs:
- changes/chronicles/justice-courts-prisons-design.md
- changes/chronicles/phase2-03-government-approval.md
---

# Justice approval crosswalk and proposed institutions

Phase 2 PR3 now adds approved_facility_designs for exactly seven original proposal IDs, without verifying their operations or changing the other proposals. The Aveline identity pointer promotes the same proposed person into a character design; her Chief Justice office remains unapproved. The original proposal tables/explanations below are the dated baseline. Vellorin/Valedorn geography is superseded by PR1; no new jurisdiction or historical event follows.

Explicit review candidates, not enacted World Bible2.2 canon. No candidate becomes an indexed building, faction or character merely through this crosswalk. No approved jurisdiction maps Valedorn to Vellorin, Aethoria or any other nation. Seven roles are evaluated against existing functions before considering any new organization; equivalent references do not subordinate those existing offices.

Twelve building candidates have only source-supported settlement references or null candidate placement. Stonegate and the Warded Annex are unlocated. No capacity, current prisoner population, warden assignment, exact address, protection or medical provision is invented. Sixteen officer candidates remain names for review, not NPCs Theron has met. Review links identify collision risks only, never aliases or kinship; existing biographies are not copied.

```json
{
  "schema_version": 1,
  "classification": "PROPOSED",
  "roles": [
    {
      "id": "proposal:role-royal-ministry",
      "name": "Royal Ministry of Justice",
      "classification": "PROPOSED",
      "proposed_purpose": "National legal administration, court coordination and oversight",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [
        "justice:caelthorne-magistrates"
      ],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-crown-marshals",
      "name": "Crown Marshals",
      "classification": "PROPOSED",
      "proposed_purpose": "Cross-regional warrants, fugitives and serious investigations within lawful authority",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-regional-constabulary",
      "name": "Regional Constabulary",
      "classification": "PROPOSED",
      "proposed_purpose": "Regional investigation, rural roads, patrol coordination and lawful transport",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [
        "justice:blackthorn-command"
      ],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-town-watch",
      "name": "Town Watch",
      "classification": "PROPOSED",
      "proposed_purpose": "Municipal public order, investigation and lawful arrest",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [
        "justice:caelthorne-watch",
        "justice:brackenford-watch"
      ],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-village-constables",
      "name": "Village Constables",
      "classification": "PROPOSED",
      "proposed_purpose": "Complaints, protection and lawful temporary detention",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [
        "justice:brackenford-watch",
        "justice:brackenford-government"
      ],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-prison-service",
      "name": "Prison Service",
      "classification": "PROPOSED",
      "proposed_purpose": "Lawful detention, administration, transfers and custody records",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:role-court-officers",
      "name": "Court Officers",
      "classification": "PROPOSED",
      "proposed_purpose": "Court security, warrants and judicial procedure",
      "government_affiliation": "Valedorn proposal; geographic scope UNKNOWN",
      "jurisdiction_location_ids": [],
      "legal_powers": null,
      "limitations": "No authority enacted or existing office replaced",
      "leadership_ids": [],
      "headquarters_location_id": null,
      "subordinate_station_ids": [],
      "court_relationship_ids": [],
      "prison_relationship_ids": [],
      "cross_border_agreements": [],
      "existing_equivalent_ids": [
        "justice:caelthorne-magistrates"
      ],
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    }
  ],
  "buildings": [
    {
      "id": "proposal:building-crown-hall",
      "name": "Crown Hall of Justice",
      "classification": "PROPOSED",
      "candidate_location_id": "caelthorne",
      "location_entity_id": null,
      "building_kind": "court",
      "detention_type": null,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [
        "justice:caelthorne-magistrates"
      ],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-central-watchhouse",
      "name": "Caelthorne Central Watchhouse",
      "classification": "PROPOSED",
      "candidate_location_id": "caelthorne",
      "location_entity_id": null,
      "building_kind": "watchhouse",
      "detention_type": 1,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [
        "justice:caelthorne-watch"
      ],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-eastrun-station",
      "name": "Eastrun Watch Station",
      "classification": "PROPOSED",
      "candidate_location_id": "eastrun",
      "location_entity_id": null,
      "building_kind": "watchhouse",
      "detention_type": 1,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-briarfall-watchhouse",
      "name": "Briarfall Crossing Watchhouse",
      "classification": "PROPOSED",
      "candidate_location_id": "briarfall-crossing",
      "location_entity_id": null,
      "building_kind": "watchhouse",
      "detention_type": 1,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-blackthorn-constabulary",
      "name": "Blackthorn Regional Constabulary",
      "classification": "PROPOSED",
      "candidate_location_id": "blackthorn-watch",
      "location_entity_id": null,
      "building_kind": "office",
      "detention_type": null,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [
        "justice:blackthorn-command"
      ],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-harbor-watch",
      "name": "Rivermere Harbor Watch",
      "classification": "PROPOSED",
      "candidate_location_id": "rivermere",
      "location_entity_id": null,
      "building_kind": "watchhouse",
      "detention_type": 1,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-eastrun-gaol",
      "name": "Eastrun District Gaol",
      "classification": "PROPOSED",
      "candidate_location_id": "eastrun",
      "location_entity_id": null,
      "building_kind": "gaol",
      "detention_type": 2,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-briarfall-gaol",
      "name": "Briarfall District Gaol",
      "classification": "PROPOSED",
      "candidate_location_id": "briarfall-crossing",
      "location_entity_id": null,
      "building_kind": "gaol",
      "detention_type": 2,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-blackthorn-gaol",
      "name": "Blackthorn Regional Gaol",
      "classification": "PROPOSED",
      "candidate_location_id": "blackthorn-watch",
      "location_entity_id": null,
      "building_kind": "gaol",
      "detention_type": 3,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-crown-remand",
      "name": "Caelthorne Crown Remand House",
      "classification": "PROPOSED",
      "candidate_location_id": "caelthorne",
      "location_entity_id": null,
      "building_kind": "gaol",
      "detention_type": 2,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [
        "justice:caelthorne-magistrates"
      ],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-stonegate",
      "name": "Stonegate Royal Prison",
      "classification": "PROPOSED",
      "candidate_location_id": null,
      "location_entity_id": null,
      "building_kind": "prison",
      "detention_type": 3,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:building-warded-annex",
      "name": "Warded Custody Annex",
      "classification": "PROPOSED",
      "candidate_location_id": null,
      "location_entity_id": null,
      "building_kind": "special-containment",
      "detention_type": 4,
      "operating_authority_id": null,
      "responsible_officer_id": null,
      "capacity": null,
      "security_arrangements": null,
      "medical_access": null,
      "court_authority_id": null,
      "transfer_rules": null,
      "operational_status": "PROPOSED — NOT OPERATIONAL",
      "reconciliation_authority_ids": [],
      "reconciliation_note": "Existing office/function is not proof of this named building, cells or regional powers. Candidate placement only; no coordinates or address. Blackthorn Watch is not North Waystation.",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    }
  ],
  "officers": [
    {
      "id": "proposal:officer-aveline-hartwell",
      "name": "Chief Justice Aveline Hartwell",
      "classification": "PROPOSED",
      "existing_character_id": "aveline-hartwell",
      "candidate_office_id": null,
      "identity_review_ids": [],
      "identity_review": "Phase2 approved character design promotes this same proposed identity; Chief Justice office and any actual appointment remain unapproved. Existing magistrates remain authoritative.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md",
        "changes/chronicles/phase2-03-government-approval.md"
      ]
    },
    {
      "id": "proposal:officer-idris-bellmont",
      "name": "Captain Idris Bellmont",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [],
      "identity_review": "No indexed identity match or office appointment.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-mara-ellwick",
      "name": "Captain Mara Ellwick",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "mara-vey",
        "mara-fenwick"
      ],
      "identity_review": "Shared given name; distinct from both existing Maras.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-darius-fenwick",
      "name": "Captain Darius Fenwick",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "mara-fenwick"
      ],
      "identity_review": "Shared surname does not establish kinship or identity.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-rhea-stone",
      "name": "Commander Rhea Stone",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "ressa-vale",
        "aldric-voss"
      ],
      "identity_review": "Similar name/rank or command context is not identity; no existing commander replaced.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-yselle-hart",
      "name": "Captain Yselle Hart",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [],
      "identity_review": "No indexed identity match or appointment.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-harlan-reed",
      "name": "Warden Harlan Reed",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "harlan-wicks"
      ],
      "identity_review": "Shared given name; existing miller is not appointed warden.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-nessa-corwin",
      "name": "Warden Nessa Corwin",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "corven",
        "corven-north-return-house",
        "corvin-hale"
      ],
      "identity_review": "Corwin/Corven/Corvin similarity is not identity.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-garron-vale",
      "name": "Warden Garron Vale",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "garrick-vale",
        "ressa-vale",
        "serrik-vale",
        "hessa-vale"
      ],
      "identity_review": "Similar given name/shared surname is not kinship, identity or appointment.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-elira-doss",
      "name": "Warden Elira Doss",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [],
      "identity_review": "No indexed identity match or appointment.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-teren-ashford",
      "name": "Marshal Teren Ashford",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "theron-ashvale"
      ],
      "identity_review": "Similar spelling establishes no identity, kinship or royal authority.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-ivara-sen",
      "name": "Magister Ivara Sen",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [],
      "identity_review": "No indexed identity match; title grants no demonstrated abilities.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-elian-wren",
      "name": "Magistrate Elian Wren",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "elian-voss"
      ],
      "identity_review": "Shared given name is not identity; no historical biography imported.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-sela-morcant",
      "name": "Magistrate Sela Morcant",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "sella"
      ],
      "identity_review": "Sela and Sella are not equated.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-amara-holt",
      "name": "Judge Amara Holt",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "evara-holt"
      ],
      "identity_review": "Shared surname is not identity or kinship.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:officer-corvin-dales",
      "name": "Justice Corvin Dales",
      "classification": "PROPOSED",
      "existing_character_id": null,
      "candidate_office_id": null,
      "identity_review_ids": [
        "corvin-hale",
        "corvin-dareth",
        "corvin-halbrecht",
        "corven",
        "corven-north-return-house"
      ],
      "identity_review": "All similarly named records remain distinct; no new office for an existing person.",
      "relationships_to_theron": null,
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    }
  ],
  "other_approval_items": [
    {
      "id": "proposal:approval-jurisdictions",
      "subject": "jurisdictions",
      "classification": "PROPOSED",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:approval-laws",
      "subject": "laws",
      "classification": "PROPOSED",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:approval-court-procedures",
      "subject": "court-procedures",
      "classification": "PROPOSED",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:approval-prison-capacities",
      "subject": "prison-capacities",
      "classification": "PROPOSED",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    },
    {
      "id": "proposal:approval-transfer-arrangements",
      "subject": "transfer-arrangements",
      "classification": "PROPOSED",
      "approval_status": "REQUIRES APPROVAL",
      "approval_source_ref": null,
      "source_refs": [
        "changes/chronicles/justice-courts-prisons-design.md"
      ]
    }
  ],
  "automatic_custody_actions": false,
  "approved_facility_designs": [
    {
      "proposal_id": "proposal:building-crown-hall",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": "caelthorne",
      "governing_design_authority_id": "government:valedorn-high-court",
      "court_design_authority_id": "government:valedorn-high-court",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "Court hearings, appellate review and records; not a prison.",
      "prisoner_classification": "No holding population; court visitors only",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-central-watchhouse",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": "caelthorne",
      "governing_design_authority_id": "government:valedorn-watch",
      "court_design_authority_id": "government:valedorn-regional-courts",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "Initial safety, booking and brief lawful holding pending independent review.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-eastrun-gaol",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": "eastrun",
      "governing_design_authority_id": "government:valedorn-custody-service",
      "court_design_authority_id": "government:valedorn-regional-courts",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "District judicial remand and lawful short custody.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-briarfall-gaol",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": "briarfall-crossing",
      "governing_design_authority_id": "government:valedorn-custody-service",
      "court_design_authority_id": "government:valedorn-regional-courts",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "District judicial remand with transport/bridge access verification.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-blackthorn-gaol",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": "blackthorn-watch",
      "governing_design_authority_id": "government:valedorn-custody-service",
      "court_design_authority_id": "government:valedorn-regional-courts",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "Regional serious-case remand or lawful sentences; not identity with Watch or North Waystation.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-stonegate",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": null,
      "governing_design_authority_id": "government:valedorn-custody-service",
      "court_design_authority_id": "government:valedorn-high-court",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "Lawfully sentenced serious cases after competent court process; location unknown.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    },
    {
      "proposal_id": "proposal:building-warded-annex",
      "classification": "APPROVED DESIGN",
      "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
      "candidate_location_id": null,
      "governing_design_authority_id": "government:valedorn-custody-service",
      "court_design_authority_id": "government:valedorn-high-court",
      "jurisdiction_condition": "Valedorn-style institutional model only. Caelthorne’s realm membership is approved; all other candidate territorial reach, receiving authority and charters require verification. No actual judicial or patrol jurisdiction is inferred from a proposed location.",
      "purpose": "Proportionate specialist custody only for individually evidenced risk and lawful authority; no demonstrated ward capability.",
      "prisoner_classification": "Individual remand/sentence/special-risk classification requires evidence, review and separation by legal/medical needs; no person assigned.",
      "staffing_roles": [
        "Qualified independent judicial/process staff appropriate to purpose",
        "Trained humane custody/escort staff where lawful holding is intended",
        "Medical practitioner, record keeper and independent inspector roles; no names or hires"
      ],
      "security_design": "Controlled keys/access, witnessed inventories and proportionate searches; no punishment restraints. Any wards require independently verified function, finite resources and medical safeguards.",
      "intake_release": "Verify identity or stable anonymous case label, legal basis, competent sending/receiving officers, order and medical needs. Give reason for custody, document property, seek prompt review; release requires its own supported lawful decision.",
      "custody_documentation": "Use the existing prisoner-custody owner and justice-and-jurisdiction action/evidence templates. Distinguish arrest, remand, verdict, sentence, transfer and release; no copied case ledger.",
      "medical_and_conditions": "Clean water, adequate food, shelter, sanitation, rest and access to independent care; record injuries without inventing them. No torture, coercive confession or punitive denial of treatment.",
      "transport_requirements": "Verify lawful authority/acceptance, end-to-end compatible route, willing lawful escorts, weather/rest/feed, humane restraint and medical transport. Record actual departures and independent receipts only after evidence.",
      "inspection_and_oversight": "Independent court and civilian/realm inspection with records, complaint access, conflict recusal and review of detention necessity; no appointment or completed inspection.",
      "emergency_procedures": "Protect life, preserve evidence and record necessity; evacuation/medical help needs verified safe destinations, custody continuity and later independent review, never automatic prisoner relocation.",
      "capacity_limits": "Design has finite space, trained staff, food, care and safe separation requirements. Exact capacity and current availability remain UNKNOWN, not zero or unlimited.",
      "actual_governing_authority_id": null,
      "responsible_officer_id": null,
      "current_staffing": null,
      "exact_capacity": null,
      "current_prisoners": null,
      "operational_status": "UNKNOWN",
      "actual_transfers": [],
      "actual_intakes": []
    }
  ]
}
```
