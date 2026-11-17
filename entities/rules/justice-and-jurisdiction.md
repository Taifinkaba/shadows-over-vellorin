---
id: justice-and-jurisdiction
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/justice-courts-prisons-design.md
- archive/legacy-modules/world/04-4-government-law-and-justice.md
- entities/mechanics/prisoner-custody.md
---

# Custody destination and proposed legal procedure

The operational lookup/recording procedure below is maintenance canon. The proposed legal process and detention taxonomy are design pending approval, not a newly enacted statute, warrant, sentence or prison. Not every person passes through every stage; allegation, surrender, detention, charge, verdict and sentence are distinct. Confession or mental magic is not automatic proof. S+ rank, wealth and Blackscale reputation confer no royal authority.

## Capture and destination lookup

1. Record the actual capture location/time and stable case ID; use a verified identity only when known. Do not fill a named suspect from resemblance or anonymous aggregate counts.
2. Resolve the settlement or road through index.json and the existing geography/settlement owners. Keep unknowns and proposed road links explicit.
3. Read justice-authorities and justice-road-links for sourced jurisdiction. An endpoint watch is not proof of road jurisdiction. Do not assume Valedorn has authority in Vellorin or elsewhere.
4. Distinguish civilian enforcement, military command, courts, guild contracts, private security and citizen intervention. Check lawful authority and case-specific legal basis; do not invent a universal citizen-arrest power.
5. Find an actually verified receiving facility, authority, capacity/access and acceptance. No new receiving prison is verified in this chunk. Proposed building records cannot receive anyone.
6. Verify the receiving officer. A named watch captain is not automatically the person who accepted custody; unknown receiver is a gap, not an invented name.
7. Plan humane medical assessment, equipment/animal care, transport, routes, rest and safeguards. Explain unresolved approvals and route gaps before departure; no automatic travel, magical containment or transfer.
8. Record departure and actual handover only when played or explicitly approved. A plan has no arrival or receipt. Keep partial original transfers as historically incomplete; do not apply prospective completeness requirements retroactively to manufacture receipts.
9. Link the existing evidence/material/finance owners and actual handover inventories. Unknown ownership stays unknown; seized goods, custody money and protected originals never become personal loot by processing or detention.
10. Record later review, remand, release, verdict, sentence or transfer only from its own supported outcome. A conviction requires its legal decision source; military discipline, civil disputes, guild proceedings and Crown investigations are separate tracks. Update normal campaign owners/checkpoint/handoff only during authorized play, never maintenance.

If an essential destination/officer/jurisdiction field is missing, report UNKNOWN and propose a source-backed, separately approved institutional decision or establish it in actual gameplay. Approval of a building design never supplies an old prisoner transfer. Planning records are not actual stages and must not alter current custody.

## Proposed court process

Subject to local law and approval: arrest → booking/medical assessment → evidence and warrant verification → judicial review → bail/conditional release or lawful remand → trial → supported conviction/acquittal → lawful sentencing where applicable → appeal → restitution/release/authorized transfer. No fixed deadlines, tariffs, bail entitlement, sentencing scale or extraterritorial powers are enacted. Guild discipline cannot sentence a person to prison, and military command cannot automatically replace a civilian magistrate. Restitution may coexist with a pending review; it is not automatic immunity or final guilt.

## Proposed detention taxonomy and safeguards

Type1: temporary watchhouse cells for initial booking/short detention. Type2: district gaols for judicial remand/lawful short detention. Type3: regional prisons for serious sentences or authorized longer detention. Type4: specialist containment only where demonstrated abilities, lawful basis and proportionate safeguards justify it. Magical ability alone never establishes danger, guilt or grounds for special confinement. Medical needs, consent where relevant, review and humane conditions remain mandatory design considerations; no ward capability is certified by a label.

## Evidence and personal-property chain

Use existing item/batch IDs or a stable case exhibit label without duplicating physical objects. Record original owner if known, actual seizing person/date, custodian, storage, each supported transfer, restrictions and current disposition. Source uncertainty stays visible. Evidence transfer is separate from prisoner transfer; neither implies transfer of title. No punishment confiscation, sale, salvage award, double counted stock or relocation of protected originals is authorized. Existing evidence custodians remain unchanged.

The schema block specifies fields, not current cases. Future approved events go into the existing prisoner-custody owner; no second register. Public directory views expose offices/procedures only; case/evidence sources require an explicit knowledge review before narration.

```json
{
  "schema_version": 1,
  "workflow_stages": [
    "apprehended",
    "awaiting-transport",
    "in-transit",
    "received-at-station",
    "booked",
    "awaiting-judicial-review",
    "released",
    "remanded",
    "transferred",
    "convicted",
    "sentenced",
    "final-disposition-recorded"
  ],
  "legal_process_classification": "PROPOSED",
  "detention_types": [
    {
      "type": 1,
      "classification": "PROPOSED",
      "label": "Temporary watchhouse cells"
    },
    {
      "type": 2,
      "classification": "PROPOSED",
      "label": "District gaols"
    },
    {
      "type": 3,
      "classification": "PROPOSED",
      "label": "Regional prisons"
    },
    {
      "type": 4,
      "classification": "PROPOSED",
      "label": "Special containment"
    }
  ],
  "transfer_fields": [
    "case_id",
    "prisoner_id",
    "status",
    "sending_authority_id",
    "receiving_authority_id",
    "destination_facility_id",
    "legal_basis",
    "departure_ref",
    "arrival_ref",
    "receiving_officer_id",
    "custody_receipt_ref",
    "evidence_inventory_ref",
    "property_inventory_ref",
    "source_refs"
  ],
  "evidence_fields": [
    "evidence_id",
    "original_owner_id",
    "seizing_person_id",
    "seizure_date",
    "custodian_id",
    "storage_location_id",
    "transfer_history",
    "legal_restrictions",
    "current_disposition",
    "source_refs"
  ],
  "automatic_custody_actions": false
}
```
