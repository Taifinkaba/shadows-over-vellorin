---
id: faction-activity
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/npc-autonomy-framework-maintenance.md
- state/checkpoint.json
- entities/mechanics/outstanding-projects.md
- entities/factions/wayfarers-guild.md
- entities/factions/dragon-slayer-academy.md
- entities/factions/northern-provisioning-consortium.md
- entities/factions/wardens.md
- entities/factions/crown-black-ledger.md
- entities/factions/continental-guild-concord.md
---

# Faction activity source routing

Routes all six existing faction entities without copying their leadership, affiliations, activities, intelligence or secret content. Fields in each original owner may mix confirmed facts, historical reports, allegations, designs and unknowns. Apply precedence and discovery review per claim; metadata gm-reference alone is not player clearance. The template supports territory/presence, leadership, members, objectives, allies/rivals, resources, legal status, last activity, relationships, quests, pending investigations, sources and knowledge classification. Missing current activity is UNKNOWN, not peaceful, destroyed, inactive or a new operation.

Existing organizations remain independent. A captured/surrendered official does not prove an organization destroyed or every member guilty. Crown-related evidence is case-specific; original Wardens are not automatically responsible for later abuses. Consortium routing involvement is not universal culpability. Guild contractual authority is not police power. The Continental Guild Concord stays a PROPOSED organization with unapproved authority, membership and operations, as its existing research owner records. No new leader, member, branch, alliance, rival, legal power, territory or faction action is asserted here.

Do not copy concealed leadership, undiscovered criminal operations, intentions, betrayals or GM outcomes into public directories. Human claim-level redaction and positive discovery provenance are required before player presentation; a source link is retrieval, never a declaration the player knows its contents.


```json
{
  "schema_version": 1,
  "factions": [
    {
      "faction_id": "wayfarers-guild",
      "source_ref": "entities/factions/wayfarers-guild.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "faction_id": "dragon-slayer-academy",
      "source_ref": "entities/factions/dragon-slayer-academy.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "faction_id": "northern-provisioning-consortium",
      "source_ref": "entities/factions/northern-provisioning-consortium.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "faction_id": "wardens",
      "source_ref": "entities/factions/wardens.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "faction_id": "crown-black-ledger",
      "source_ref": "entities/factions/crown-black-ledger.md",
      "classification": "CONFIRMED CANON",
      "knowledge": "requires-discovery-review"
    },
    {
      "faction_id": "continental-guild-concord",
      "source_ref": "entities/factions/continental-guild-concord.md",
      "classification": "PROPOSED",
      "knowledge": "requires-discovery-review"
    }
  ],
  "owner_field_contract": [
    "name",
    "territory_presence",
    "leadership",
    "members",
    "objectives",
    "allies",
    "rivals",
    "resources",
    "legal_status",
    "last_verified_activity",
    "relationships",
    "active_quests",
    "pending_investigations",
    "source_refs",
    "knowledge"
  ],
  "activity_kinds": [
    "confirmed",
    "historical",
    "alleged",
    "proposed",
    "unknown-current"
  ],
  "new_activity": [],
  "new_memberships": [],
  "new_legal_powers": [],
  "automatic_activity": false
}
```
