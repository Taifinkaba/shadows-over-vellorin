---
id: contract-registry
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year848-day196-end-session.md
- changes/chronicles/guild-concord-contracts-design.md
- entities/factions/wayfarers-guild.md
- entities/rules/justice-and-jurisdiction.md
---

# Contract owner routing and future integration

Routing only; no copied rewards/statuses or second quest ledger. Known contract IDs resolve to their original Wayfarers owner; existing mystery/legal quest outcomes stay in existing quest records. No currently payable contract is generated. Dungeon contract kinds are future integration vocabulary for Chunk6, not instantiated sites, encounters, clearing, discoveries or loot.

```json
{
  "schema_version": 1,
  "contracts": [
    {
      "contract_id": "G-215",
      "owner_entity_id": "wayfarers-guild"
    },
    {
      "contract_id": "G-216",
      "owner_entity_id": "wayfarers-guild"
    },
    {
      "contract_id": "B-83",
      "owner_entity_id": "wayfarers-guild"
    },
    {
      "contract_id": "SS-41",
      "owner_entity_id": "wayfarers-guild"
    },
    {
      "contract_id": "WG-848-196-EASTRUN",
      "owner_entity_id": "wayfarers-guild"
    },
    {
      "contract_id": "WG-848-196-BRIARFALL",
      "owner_entity_id": "wayfarers-guild"
    }
  ],
  "dungeon_contract_kinds": [
    "exploration",
    "rescue",
    "monster-removal",
    "artifact-recovery",
    "survey",
    "escort",
    "mapping",
    "hazard-containment",
    "salvage",
    "research"
  ],
  "automatic_financial_postings": false
}
```
