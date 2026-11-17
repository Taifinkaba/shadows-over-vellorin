---
id: prisoner-custody
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- archive/session-handoffs/year847-day472-user-handoff.txt
- archive/session-handoffs/year848-day124-user-handoff.txt
- changes/chronicles/year848-day137-end-session.md
---

## Current update — Day137, 09:30, ENDED

Immediate Greyvein four-prisoner review completed: two released; one retained under documented proceedings; one medically transferred, hearing pending. Individual identities, exact locations and mapping to older detainees were not supplied; do not invent them. Halden Marr rescued, free and voluntarily protected at Ashvale Estate, not a prisoner. Earlier North Return House custody is historical and does not certify current placement.

## Historical record through Day124 (superseded where explicit above)


# Prisoner custody register

## Current expedition — Year848 Suncrest4 Day124 01:45

Perrin, Dask and [lodge supervisor Corven](../characters/corven-north-return-house.md) are the **three current expedition detainees**, alive and unharmed under Garrick’s nonlethal guard at North Return House. Perrin/Dask cooperatively surrendered; Corven surrendered after confrontation. No punishment, execution or transfer. Sella cooperates voluntarily and remains free; Orenic remains free with no established involvement. No additional prisoners found in inspected cellar. Zero fatalities and zero party injuries.

## Last verified historical custody — Year847 Day472

Malrec/Caldra guarded at Hollow; Edran/Sera/Corvin Hale at fortified wagon camp. Two previously paid contracted guards reinforced camp. Valcrest captured alive separately, exact location unverified. Those older positions are historical only: intervening dispositions/current whereabouts unknown, with no inferred release, death or transfer. Do not count those five as present expedition detainees. Corvin Hale, Corvin Halbrecht, older Corven and lodge supervisor Corven are not automatically identified with one another.

## Justice workflow and source routing — Chunk 4

This extends this single custody owner with workflow and source routing, not new case outcomes. The latest dated section above is Day137; later Day156 review sources are linked below and supersede only their explicit overlapping facts. Historical North Return House/Day472 text never certifies current placement. Case status, guilt, receiving officer and destination are not copied into a parallel snapshot. No new receipt, person identity, court decision or transfer is supplied by this maintenance.

```json
{
  "schema_version": 1,
  "workflow_ref": "justice-and-jurisdiction",
  "history_routing": [
    {
      "id": "custody-source:early-greyhaven-rusk",
      "scope": "identity-gap",
      "source_refs": [
        "archive/session-handoffs/year847-day472-user-handoff.txt"
      ],
      "note": "Rusk/mill checks are not handover receipts; original handover identity/destination/sequence UNKNOWN. No matching to later groups."
    },
    {
      "id": "custody-source:third-bell-era",
      "scope": "identity-gap",
      "source_refs": [
        "archive/legacy-modules/codex/11-v1-5-final-cross-session-verification-audit-out-of-world-no-gamep.md",
        "entities/items/third-bell-clapper.md"
      ],
      "note": "Historical custody-money/suspect aggregate and clapper evidence do not identify a modern prisoner destination. No group mapping inferred."
    },
    {
      "id": "custody-source:day472-five",
      "scope": "historical",
      "source_refs": [
        "entities/mechanics/prisoner-custody.md"
      ],
      "note": "Use original dated section; no present placement inferred."
    },
    {
      "id": "custody-source:separate-day472-capture",
      "scope": "historical",
      "source_refs": [
        "entities/characters/severin-valcrest.md"
      ],
      "note": "Separate source; do not fold into five-person group."
    },
    {
      "id": "custody-source:north-return-house",
      "scope": "historical",
      "source_refs": [
        "entities/mechanics/prisoner-custody.md",
        "entities/locations/north-return-house.md"
      ],
      "note": "Original Day124 section is historical, not a current transport receipt."
    },
    {
      "id": "custody-source:greyvein-review",
      "scope": "historical",
      "source_refs": [
        "entities/mechanics/prisoner-custody.md"
      ],
      "note": "Aggregate remains distinct; no identities assigned."
    },
    {
      "id": "custody-source:later-v9-review",
      "scope": "later-source",
      "source_refs": [
        "entities/quests/seven-bells-investigation.md",
        "changes/chronicles/year848-day156-end-session.md"
      ],
      "note": "Later source pointer only; do not map cases to older aggregates or vessels."
    },
    {
      "id": "custody-source:pending-civilian-review",
      "scope": "later-source",
      "source_refs": [
        "entities/characters/maelor-thane.md"
      ],
      "note": "Read latest source; no sentence or prison destination inferred."
    },
    {
      "id": "custody-source:pending-military-review",
      "scope": "later-source",
      "source_refs": [
        "entities/characters/edrick-sorn.md"
      ],
      "note": "Read military review source separately; no civilian conviction inferred."
    },
    {
      "id": "custody-source:unlocated-person",
      "scope": "non-detention-reference",
      "source_refs": [
        "entities/characters/halric-dene.md"
      ],
      "note": "No detention asserted by this reference."
    },
    {
      "id": "custody-source:voluntary-protection",
      "scope": "non-detention-reference",
      "source_refs": [
        "entities/characters/halden-marr.md"
      ],
      "note": "Protection is not detention; no new custody record."
    }
  ],
  "evidence_owner_refs": [
    "seven-bells-inventory",
    "shady-salvage",
    "launder",
    "party-finances"
  ],
  "new_case_records": [],
  "new_transfer_records": [],
  "new_evidence_records": [],
  "automatic_custody_actions": false
}
```
