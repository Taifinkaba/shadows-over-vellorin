---
id: dungeon-exploration
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/dungeon-exploration-registry-design.md
- entities/mechanics/shady-salvage.md
- entities/mechanics/seven-bells-inventory.md
- entities/mechanics/launder.md
- entities/mechanics/party-finances.md
- entities/rules/story-mode.md
- entities/mechanics/contract-registry.md
- changes/chronicles/phase2-05-dungeon-approval.md
---

# Exploration, ecology and finite loot procedure

The retrieval and no-mutation rules are maintenance canon. Physical categories, threat scale, ecology/hazard templates and future finite-loot generation are PROPOSED design, not retroactive dungeon classifications or new encounters.

## Retrieve a site or revisit a section

1. Resolve the site ID in dungeon-registry and its existing location, or its exact source label when no location entity exists. Never merge the Hollows, aqueduct/workshop labels or separate structures from similar names. Registry membership does not make an ordinary house a dungeon.
2. Read only the relevant section source in exploration-sections and the original location/quest history. Distinguish unexplored, partial, visited, searched and protected. No new default room contents, map, combat, undiscovered passage or fresh chest is supplied by a lookup.
3. Check linked creature/hazard sources, actual last observations and current uncertainty. Returning does not reset rooms, restore defeated creatures, kill a contained creature or move an independent guardian home. Pale Devourer remains contained, not defeated, per its existing source. A supported later event is required before changing a population; no automatic respawn, scaling or arbitrary matching to Theron's rank.
4. Check original inventory/evidence ownership, prior recoveries, quantities already removed and protected/installed/isolated materials. Lookup, appraisal and processing never grant title, duplicate a batch or certify safe crafting. Do not move a protected original or add historical counts to a later expedition.
5. Check actual objective/contract owner and its source. First Hour resumption is a specific achieved objective, not blanket gallery exploration or whole-site clearance. Site explored/cleared, secret discovered, threat removed, rescue, route opened, investigation and contract completion remain independent facts. Never complete an unrelated quest or pay a historical bounty from a visit.
6. For access, use only a sourced entrance and route relationship. Shared region/nearby mountain/related quest does not prove a road reaches a dungeon door. Unknown approaches remain unknown; no historical times, magic shortcuts or automatic character travel. Existing spell range/cost/anchor/concentration limits and finite resources remain in their owners.
7. During actual play, present sourced known conditions and explicitly unresolved details without pretending unknown contents are historical facts. Warn fairly about established danger, preserve meaningful choices, Story Mode and permanent-death rules. Low-level threats need not scale up to a powerful party; credible higher danger needs actual cause. No battle or hazard is triggered by maintenance.
8. Searching, salvage, creature encounters and trap work require actual approved play: record actor/time/source, exact section, observation versus inference, action/result, costs and changes in the existing owner. A disarm needs its own observed outcome and limits, not a generic “cleared” switch. No retroactive trap in an already explored room without a supported later causal event.
9. Before leaving or returning later, preserve actual last section state and independent creature positions; report missing current information rather than reset it. New occupants need plausible cause, elapsed time and a recorded event, not a timer. No automatic treasure refill, vegetation restoration, secret reset or remote success.
10. Update normal location/quest/salvage/creature owners, chronicle, finance and checkpoint only after a played or explicitly approved event; never maintain a competing current-state file. END SESSION stops play and follows narration-format.md. Use attributed dialogue and independently closed disclosures for long registers; player knowledge requires discovery provenance even for gm-reference sources.

## Proposed ecology and hazard design

A creature/group template supports ID, species, known location, threat if established, behavior, territory, diet/sustenance, social structure, intelligence, hostility/neutrality, abilities, weaknesses, last status and encounter sources. Unknowns stay unknown; no current group sizes, new habitats, stat blocks or abilities are created. Historical affiliation is not permanent physical presence.

Hazards support source-backed location, trigger, detectability, effect, disarm/avoidance, state and source. Mechanical traps, wards, poison, collapse, flooding, darkness, extreme temperatures, curses, unstable portals and hostile magic are categories only until sourced. No category implies it exists in every room; no disarm recipe or unrevealed solution is generated here.

## Proposed finite-loot procedure

Before future generation, assess actual site history, prior inhabitants/wealth, earlier exploration and removals, environmental damage, ownership, rarity, carrying capacity and law. Establish finite plausible contents only through approved play; a high threat label does not guarantee a legendary item or unlimited rare material. Empty/recovered caches do not refill automatically. This chunk rolls nothing and generates no objects for unexplored rooms.

Use the existing authoritative item/batch owner once. Keep unclaimed objects, provisional salvage, party-owned inventory, merchant goods, protected evidence, dangerous isolated materials, third-party/prisoner property, consumed materials, sold items and unknown title distinct. Recovery does not establish ownership; processing does not launder title. Disposal, sale, crafting, consumption and payment require separately supported authorization/events. Existing finance/custody/protected evidence remain unchanged.

## Objective and contract integration

A site-related contract must resolve through contract-registry to its original issuer/funder/objective/eligibility/reward/proof/status owner and a verified specific site where known. No current site-linked offered contract is supplied in this chunk. Source-backed completion of one objective does not imply all rooms searched, inhabitants defeated, secrets revealed or other contracts fulfilled. No duplicate payouts or automatic loot rewards.

```json
{
  "schema_version": 1,
  "classification_framework": "PROPOSED",
  "physical_categories": [
    "natural-cave",
    "abandoned-mine",
    "ancient-ruin",
    "underground-fortress",
    "magical-vault",
    "cursed-site",
    "monster-lair",
    "ruined-temple",
    "lost-laboratory",
    "sealed-historical-site"
  ],
  "hazard_categories": [
    "mechanical-trap",
    "magical-ward",
    "poisonous-environment",
    "collapsing-structure",
    "flooded-passage",
    "darkness",
    "extreme-temperature",
    "cursed-object",
    "unstable-portal",
    "hostile-magic"
  ],
  "loot_ownership_categories": [
    "unclaimed",
    "provisional-salvage",
    "party-owned",
    "merchant-owned",
    "protected-evidence",
    "dangerous-isolated",
    "third-party-prisoner-property",
    "consumed",
    "sold",
    "unknown-title"
  ],
  "completion_kinds": [
    "rescue",
    "threat-removed",
    "artifact-secured",
    "route-opened",
    "system-stabilized",
    "investigation",
    "contract",
    "safely-sealed"
  ],
  "creature_fields": [
    "creature-id",
    "species",
    "known-location",
    "threat",
    "behavior",
    "territory",
    "diet",
    "group-structure",
    "intelligence",
    "hostility",
    "abilities",
    "weaknesses",
    "last-status",
    "encounter-history"
  ],
  "section_fields": [
    "id",
    "state-source",
    "known-contents-owner",
    "access-source",
    "hazard-references",
    "encounter-sources",
    "recovered-inventory-owner",
    "remaining-objective-owner",
    "last-source"
  ],
  "rank_domains": [
    "dungeon-threat",
    "combat-power",
    "guild-license",
    "professional-certification",
    "contract-difficulty"
  ],
  "new_loot_records": [],
  "new_combat_events": [],
  "automatic_chest_refill": false,
  "automatic_quest_completion": false,
  "approved_exploration_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-05-dungeon-approval.md",
    "design_owner_ref": "dungeon-design-proposals",
    "reference_owner_ref": "dungeon-ecology-and-hazards",
    "historical_sections_owner_ref": "exploration-sections",
    "finance_owner_ref": "party-finances",
    "legal_owner_ref": "justice-and-jurisdiction",
    "magic_owner_refs": [
      "theron-spells",
      "theron-abilities"
    ],
    "salvage_owner_refs": [
      "shady-salvage",
      "launder",
      "seven-bells-inventory"
    ],
    "recovery_template": {
      "event_id": null,
      "status": "proposed",
      "dungeon_design_id": null,
      "area_id": null,
      "item_description": null,
      "source_ref": null,
      "quantity": null,
      "unit": null,
      "verified_available_quantity": null,
      "discovery_evidence_ref": null,
      "recovery_evidence_ref": null,
      "ownership_provenance_ref": null,
      "transport_capacity_ref": null,
      "legal_authority_ref": null,
      "inventory_owner_ref": null,
      "approved_update_evidence_ref": null,
      "finance_transaction_ref": null
    },
    "procedure": "Design graphs and references are not discovered map facts or active hazards. Confirm actual location, lawful access, information, environmental evidence, finite resources and abilities before play. Declare stakes/costs/checks under existing rules; record observed outcomes only in original owners. Any actual recovery requires finite positive quantity within verified availability, evidence, title, lawful handling, transport and an approved original inventory/finance update.",
    "actual_recoveries": [],
    "actual_damage_events": [],
    "actual_discoveries": [],
    "actual_resource_postings": [],
    "automatic_population": false,
    "automatic_damage": false,
    "automatic_loot": false,
    "automatic_recovery": false,
    "potential_reward_categories": [
      "coins",
      "tools",
      "craft-materials",
      "mineral-samples",
      "historical-records",
      "salvage-equipment",
      "decorative-objects",
      "rare-materials",
      "research-fragments",
      "relics-for-review"
    ]
  }
}
```
