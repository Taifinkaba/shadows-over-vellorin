---
id: dungeon-registry
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/dungeon-exploration-registry-design.md
- entities/mechanics/shady-salvage.md
- entities/mechanics/seven-bells-inventory.md
- entities/quests/seven-bells-investigation.md
- entities/locations/ninth-vault.md
- entities/locations/mirror-foundation.md
- entities/locations/hollow-first-hour.md
- entities/locations/hollow-veil.md
- entities/locations/north-return-house.md
- entities/locations/seven-bells-witness-entry.md
---

# Dungeon and exploration site routing

Site IDs below are retrieval handles, not newly created locations or a dungeon census. Some entries are ordinary structures, investigations, a sanctuary, wilderness or a historical entrance reference. No blanket dungeon/threat classification. Existing location/quest/salvage owners remain authoritative; null status does not erase a more specific historical observation in a linked source. All preexisting records are unchanged.

Every old section/state/inventory fact is resolved through its owner. No map edge, door-opening recipe, hidden solution, live occupant, item count, title, reward or current visit is copied here. The two Hollows remain distinct. Foundations/receiving/entry labels are separate routing contexts without asserting either physical equivalence or disconnection. Sources, not convenient map topology, decide future identity questions.

```json
{
  "schema_version": 1,
  "sites": [
    {
      "site_id": "site:ninth-vault",
      "name": "Ninth Vault",
      "classification": "CONFIRMED CANON",
      "record_kind": "investigation-site",
      "location_entity_id": "ninth-vault",
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [
        "artificial-witness",
        "first-oath-conspiracy"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/ninth-vault.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:mirror-foundation",
      "name": "Mirror Foundation",
      "classification": "CONFIRMED CANON",
      "record_kind": "investigation-site",
      "location_entity_id": "mirror-foundation",
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [
        "artificial-witness"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/mirror-foundation.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:hollow-first-hour",
      "name": "Hollow of the First Hour",
      "classification": "CONFIRMED CANON",
      "record_kind": "historical-site",
      "location_entity_id": "hollow-first-hour",
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:hollow-first-hour:supply-annex",
        "section:hollow-first-hour:western-gallery",
        "section:hollow-first-hour:keeper-quarters"
      ],
      "creature_context_ids": [
        "ecology:aeloryn"
      ],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [
        "shady-salvage",
        "launder"
      ],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [
        "first-hour-restoration",
        "open-quests"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": "entities/locations/hollow-first-hour.md",
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/hollow-first-hour.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:hollow-veil",
      "name": "Hollow Veil",
      "classification": "CONFIRMED CANON",
      "record_kind": "sanctuary",
      "location_entity_id": "hollow-veil",
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [
        "ecology:vaeltharion"
      ],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [
        "vaeltharion-freedom"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/hollow-veil.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:north-return-house",
      "name": "North Return House",
      "classification": "CONFIRMED CANON",
      "record_kind": "ordinary-structure-investigation-site",
      "location_entity_id": "north-return-house",
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:north-return-house:cellar"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [
        "seven-bells-inventory"
      ],
      "protected_evidence_owner_refs": [
        "seven-bells-inventory"
      ],
      "associated_quest_ids": [
        "seven-bells-investigation"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/north-return-house.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:northern-depository",
      "name": "Northern Depository",
      "classification": "CONFIRMED CANON",
      "record_kind": "investigation-site",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [
        "seven-bells-inventory"
      ],
      "associated_quest_ids": [
        "seven-bells-investigation"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "source_refs": [
        "entities/mechanics/shady-salvage.md",
        "entities/mechanics/seven-bells-inventory.md",
        "entities/quests/seven-bells-investigation.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:seven-bells-receiving-chambers",
      "name": "Seven Bells receiving chambers",
      "classification": "CONFIRMED CANON",
      "record_kind": "investigation-site",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [
        "seven-bells-inventory"
      ],
      "protected_evidence_owner_refs": [
        "seven-bells-inventory"
      ],
      "associated_quest_ids": [
        "seven-bells-investigation"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "source_refs": [
        "entities/mechanics/shady-salvage.md",
        "entities/quests/seven-bells-investigation.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:whisperstone-hollow",
      "name": "Whisperstone Hollow",
      "classification": "CONFIRMED CANON",
      "record_kind": "named-site-unclassified",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:whisperstone-hollow:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:old-copperworks",
      "name": "Old Copperworks",
      "classification": "CONFIRMED CANON",
      "record_kind": "named-site-unclassified",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:old-copperworks:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:nine-star-shrine",
      "name": "Nine-Star Shrine",
      "classification": "CONFIRMED CANON",
      "record_kind": "shrine-site",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:nine-star-shrine:accessible-rooms"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:vaelspire-observatory",
      "name": "Vaelspire observatory",
      "classification": "CONFIRMED CANON",
      "record_kind": "observatory-context",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:vaelspire-observatory:lower-rooms"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:northwatch-old-aqueduct",
      "name": "Northwatch old aqueduct",
      "classification": "CONFIRMED CANON",
      "record_kind": "infrastructure-site",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:northwatch-old-aqueduct:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:western-roadside-fortress",
      "name": "Western roadside fortress",
      "classification": "CONFIRMED CANON",
      "record_kind": "fortress-site",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:western-roadside-fortress:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:frostglass-western-ridge",
      "name": "Frostglass western ridge",
      "classification": "CONFIRMED CANON",
      "record_kind": "wilderness-area",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:frostglass-western-ridge:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:abbey-bellkeeper-residence",
      "name": "Abbey bellkeeper residence",
      "classification": "CONFIRMED CANON",
      "record_kind": "ordinary-structure",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:abbey-bellkeeper-residence:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:ravencrest-waystation",
      "name": "Ravencrest waystation",
      "classification": "CONFIRMED CANON",
      "record_kind": "ordinary-structure",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:ravencrest-waystation:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:seven-bells-lower-foundations",
      "name": "Seven Bells lower foundations",
      "classification": "CONFIRMED CANON",
      "record_kind": "exploration-area-label",
      "location_entity_id": null,
      "entrance_location_id": null,
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [
        "section:seven-bells-lower-foundations:recorded-area"
      ],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [
        "seven-bells-inventory"
      ],
      "associated_quest_ids": [
        "seven-bells-investigation"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/mechanics/shady-salvage.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    },
    {
      "site_id": "site:seven-bells-witness-entry",
      "name": "Seven Bells independent Witness entry",
      "classification": "CONFIRMED CANON",
      "record_kind": "entrance-reference",
      "location_entity_id": "seven-bells-witness-entry",
      "entrance_location_id": "seven-bells-witness-entry",
      "region_id": null,
      "access_route_ids": [],
      "category": null,
      "danger_classification": null,
      "exploration_state_ref": null,
      "section_ids": [],
      "creature_context_ids": [],
      "hazard_reference_ids": [],
      "recovered_inventory_owner_refs": [],
      "protected_evidence_owner_refs": [],
      "associated_quest_ids": [
        "seven-bells-investigation"
      ],
      "guild_contract_ids": [],
      "last_verified_visit_ref": null,
      "access_source_refs": [],
      "source_refs": [
        "entities/locations/seven-bells-witness-entry.md"
      ],
      "aliases": [],
      "note": "Known identity/record context only. Missing location/entrance/route/category/threat/whole-site status remains UNKNOWN. Shared Seven Bells or Hollow naming proves neither identity nor a connecting passage. Source pointer is not automatic player knowledge."
    }
  ],
  "sections_owner_ref": "exploration-sections",
  "ecology_hazards_owner_ref": "dungeon-ecology-and-hazards",
  "contract_registry_ref": "contract-registry",
  "new_inventory_records": [],
  "new_objective_outcomes": [],
  "automatic_respawn": false,
  "automatic_loot": false
}
```
