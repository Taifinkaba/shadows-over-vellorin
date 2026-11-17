---
id: quest-history-and-identities
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/main-quest-framework-maintenance.md
- state/checkpoint.json
- state/open-verifications.md
- entities/characters/severin-valcrest.md
- entities/characters/maelor-thane.md
- entities/characters/edrick-sorn.md
- entities/characters/halric-dene.md
- entities/characters/varian-morthal.md
- entities/characters/corvin-dareth.md
- entities/characters/selvar-renn.md
- entities/characters/damaris-keld.md
- entities/characters/oren-veyl.md
- entities/characters/aldric-voss.md
- entities/characters/elian-voss.md
- entities/characters/malrec.md
- entities/characters/corven.md
- entities/characters/corven-north-return-house.md
- entities/characters/corvin-hale.md
- entities/characters/corvin-halbrecht.md
- entities/characters/rellan-sorn.md
- entities/quests/v9-memories.md
- entities/quests/first-hour-restoration.md
- entities/quests/fifth-bell-threat.md
- entities/items/fifth-bell.md
- entities/quests/first-oath-conspiracy.md
- entities/quests/artificial-witness.md
---

# Historical objective and identity crosswalk

Thirteen references protect established achievements/observations with their exact scope. CONFIRMED CANON refers to historical source evidence, not a new event, conviction, permanent Fifth Bell neutralization or main quest completion. Read owner freshness before stating present custody. No old rescue, Lyanna restoration, First Hour release or prevented activation becomes mandatory work again.

Seventeen indexed people remain distinct. Malrec Voss uses existing ID malrec, not a guessed new file. Aldric/Elian/Malrec share no inferred kinship or universal role; Severin Valcrest remains CROWN-07. Newer AV-07/SS-41 figures do not replace him. Corven the older adversary and North Return supervisor are not automatically one person; Corvin Hale/Halbrecht/Dareth and Rellan/Edrick Sorn are not aliases or proven relatives. Keeper, Registrar, Commander, Custodian and Witness are titles, not identity keys. Oren Veyl's further role is unspecified, not evidence he is a mastermind or accomplice.

For exact command-role claims retrieve the original person/quest owner: SS-41 drafting, exceptional countersignature, receipt and distribution are separate sourced actions, not identical culpability. Thane's authority, Sorn's field responsibility and Dene's capture-team role remain separate from earlier Voss routing marks. Aldric-authorized amendments do not prove he directed theft or sabotage. Documented role, confession, allegation, suspect status and conviction are distinct. No identity merger, family relationship, guilt extension or transfer is created here.


```json
{
  "schema_version": 1,
  "historical_objectives": [
    {
      "resolution_id": "resolution:lyanna-vessels",
      "owner_ref": "v9-memories",
      "evidence_ref": {
        "source_ref": "entities/quests/v9-memories.md",
        "quote": "Three stolen Ashvale memory vessels recovered from V-9."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Recovery objective complete; three vessels are not three people.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:lyanna-restoration",
      "owner_ref": "v9-memories",
      "evidence_ref": {
        "source_ref": "entities/quests/v9-memories.md",
        "quote": "Lyanna’s intact memories restored voluntarily under Lyra’s supervision."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Restoration complete; other V-9 cases remain distinct.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:first-hour",
      "owner_ref": "first-hour-restoration",
      "evidence_ref": {
        "source_ref": "entities/quests/first-hour-restoration.md",
        "quote": "First Hour restoration completed on Day 472; wider Guardian restoration remains active."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Specific objective complete; damaged other channels remain open.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:original-protections",
      "owner_ref": "first-hour-restoration",
      "evidence_ref": {
        "source_ref": "entities/quests/first-hour-restoration.md",
        "quote": "Original Guardian protections preserved."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Protective systems preserved, not universally corrupted or destroyed.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:crown07-identity",
      "owner_ref": "severin-valcrest",
      "evidence_ref": {
        "source_ref": "entities/characters/severin-valcrest.md",
        "quote": "Identified as Crown-07; captured alive at the Citadel of Seven Bells."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Known identification/capture; exact current custody not supplied.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:fifth-activation",
      "owner_ref": "fifth-bell-threat",
      "evidence_ref": {
        "source_ref": "entities/quests/fifth-bell-threat.md",
        "quote": "Fifth Bell activation prevented, original safeguards preserved."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Encounter prevention succeeded; broader permanent threat resolution remains open.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:no-fifth-toll",
      "owner_ref": "fifth-bell",
      "evidence_ref": {
        "source_ref": "entities/items/fifth-bell.md",
        "quote": "Never sounded through Day156."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Checkpoint observation, not a promise about future play.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:av07-authority",
      "owner_ref": "maelor-thane",
      "evidence_ref": {
        "source_ref": "entities/characters/maelor-thane.md",
        "quote": "Original AV-07 authority;"
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Established authority, not a newly inferred universal controller.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:thane-surrender",
      "owner_ref": "maelor-thane",
      "evidence_ref": {
        "source_ref": "entities/characters/maelor-thane.md",
        "quote": "Confronted and surrendered alive; independent legal review pending."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Surrender is established; no conviction or prison destination inferred.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:sorn-field-command",
      "owner_ref": "edrick-sorn",
      "evidence_ref": {
        "source_ref": "entities/characters/edrick-sorn.md",
        "quote": "AV-07 field commander."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Established field responsibility; separate from other similarly named figures.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:sorn-command-relinquished",
      "owner_ref": "edrick-sorn",
      "evidence_ref": {
        "source_ref": "entities/characters/edrick-sorn.md",
        "quote": "active command relinquished pending military review."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Command relinquishment established; military disposition remains pending.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:ss41-specific",
      "owner_ref": "first-oath-conspiracy",
      "evidence_ref": {
        "source_ref": "entities/quests/first-oath-conspiracy.md",
        "quote": "Wayfarers Guild registry revoked; specific Crown SS-41 apprehension instruction withdrawn by magistrate; independent other notices not automatically canceled."
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Only the specified registry/instruction changed; no blanket notice cancellation.",
      "knowledge": "requires-discovery-review"
    },
    {
      "resolution_id": "resolution:empty-seat-channel",
      "owner_ref": "artificial-witness",
      "evidence_ref": {
        "source_ref": "entities/quests/artificial-witness.md",
        "quote": "Empty Seat’s old Keeper-imprint authority ceased functioning"
      },
      "classification": "CONFIRMED CANON",
      "scope_limit": "Resolved old channel; later counterfeit branches do not negate it.",
      "knowledge": "requires-discovery-review"
    }
  ],
  "distinct_people": [
    {
      "character_id": "severin-valcrest",
      "source_ref": "entities/characters/severin-valcrest.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "maelor-thane",
      "source_ref": "entities/characters/maelor-thane.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "edrick-sorn",
      "source_ref": "entities/characters/edrick-sorn.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "halric-dene",
      "source_ref": "entities/characters/halric-dene.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "varian-morthal",
      "source_ref": "entities/characters/varian-morthal.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "corvin-dareth",
      "source_ref": "entities/characters/corvin-dareth.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "selvar-renn",
      "source_ref": "entities/characters/selvar-renn.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "damaris-keld",
      "source_ref": "entities/characters/damaris-keld.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "oren-veyl",
      "source_ref": "entities/characters/oren-veyl.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "aldric-voss",
      "source_ref": "entities/characters/aldric-voss.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "elian-voss",
      "source_ref": "entities/characters/elian-voss.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "malrec",
      "source_ref": "entities/characters/malrec.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "corven",
      "source_ref": "entities/characters/corven.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "corven-north-return-house",
      "source_ref": "entities/characters/corven-north-return-house.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "corvin-hale",
      "source_ref": "entities/characters/corvin-hale.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "corvin-halbrecht",
      "source_ref": "entities/characters/corvin-halbrecht.md",
      "knowledge": "requires-discovery-review"
    },
    {
      "character_id": "rellan-sorn",
      "source_ref": "entities/characters/rellan-sorn.md",
      "knowledge": "requires-discovery-review"
    }
  ],
  "identity_mergers": [],
  "new_custody_events": [],
  "new_historical_outcomes": []
}
```
