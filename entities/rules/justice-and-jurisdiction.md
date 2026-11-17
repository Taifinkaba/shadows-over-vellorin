---
id: justice-and-jurisdiction
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/justice-courts-prisons-design.md
- archive/legacy-modules/world/04-4-government-law-and-justice.md
- entities/mechanics/prisoner-custody.md
- changes/chronicles/phase2-03-government-approval.md
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
  "automatic_custody_actions": false,
  "approved_legal_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
    "realm_ids": [
      "valedorn",
      "elyndor",
      "ironhollow-holds",
      "rivermere-league",
      "frostmarch"
    ],
    "exclusive_cross_realm_court": false,
    "historical_authority_owner_ref": "justice-authorities",
    "custody_owner_ref": "prisoner-custody",
    "finance_owner_ref": "party-finances",
    "court_levels": [
      "local",
      "regional",
      "realm"
    ],
    "jurisdiction_policy": "Each realm retains separate traditions and competent courts. Verify territory, local mandate and subject-matter power; ambiguous borders need negotiated forum and rights review. No court owns all Vellorin or all five realms. Brackenford’s realm remains unknown: preserve reeve/council, Ressa Vale and six part-time members without assigning a new superior or tax.",
    "proof_standards": {
      "investigation": "Credible particularized information justifies proportionate inquiry, not guilt.",
      "search_arrest": "Verify competent authority, lawful written warrant or separately justified urgent necessity, particular scope and reviewable reasons.",
      "civil": "Hear both sides and assess credible documents/testimony; distinguish civil breach or restitution from criminal guilt.",
      "criminal": "Require reliable corroborated proof, a meaningful opportunity to challenge it and an independent reasoned finding; doubt, coerced confessions and mental magic cannot be automatic conviction.",
      "serious_penalty": "Enhanced independent review, medical/identity safeguards, reasoned lawful sentence and appeal; no automatic grave punishment."
    },
    "process_steps": [
      "Establish jurisdiction, independent reviewer and conflicts",
      "Document complaint/allegation and preserve original evidence",
      "Obtain/verify bounded warrant or documented urgent necessity",
      "Record actual arrest only with lawful authority and evidence; explain reasons and assess care",
      "Review identity, grounds, evidence and property chain without forced confession",
      "Consider lawful release/conditions or proportionate reviewed remand",
      "Hold a fair hearing/trial with challenge and reliable corroboration",
      "Record supported acquittal/conviction separately from sentence",
      "Hear independent appeal and wrongful-conviction/redress claims",
      "Record actual release/transfer/restitution only in existing owners with evidence"
    ],
    "offenses": [
      {
        "id": "offense:theft",
        "classification": "APPROVED DESIGN",
        "conduct": "Taking property without lawful title/consent; mistaken ownership requires investigation.",
        "offense_class": "minor-to-serious",
        "evidence_requirements": "Ownership, possession, taking and intent; recovery is not a reward grant.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:burglary",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful entry connected to theft or another proved offense.",
        "offense_class": "serious",
        "evidence_requirements": "Entry authority, premises rights, conduct and reliable identification.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:assault",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful violence, threat or harmful compulsion; necessity/self-defense are investigated.",
        "offense_class": "minor-to-grave",
        "evidence_requirements": "Injury/threat evidence, circumstances and proportionate defense; magic is no shortcut to guilt.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:murder",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful intentional killing; death alone does not identify an offender.",
        "offense_class": "grave",
        "evidence_requirements": "Cause, identity, intent and independent corroboration; distinguish lawful defense and accident.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:fraud",
        "classification": "APPROVED DESIGN",
        "conduct": "Knowing material deception causing wrongful gain/loss.",
        "offense_class": "minor-to-serious",
        "evidence_requirements": "False claim, knowledge, reliance, loss and competing explanations.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:forgery",
        "classification": "APPROVED DESIGN",
        "conduct": "Fabricating or knowingly using false documents, seals or warrants.",
        "offense_class": "serious",
        "evidence_requirements": "Original/copy provenance, seal authority, handwriting testimony and actual use; do not invent authenticity.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:bribery-corruption",
        "classification": "APPROVED DESIGN",
        "conduct": "Improper inducement, secret official benefit or abuse of public trust.",
        "offense_class": "serious",
        "evidence_requirements": "Authority, benefit/request, intent and conflict evidence; gift or lobbying alone is not conviction.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:smuggling",
        "classification": "APPROVED DESIGN",
        "conduct": "Knowing evasion of applicable lawful cargo restrictions/customs.",
        "offense_class": "serious",
        "evidence_requirements": "Prove the applicable rule, territorial authority, goods, movement and knowledge; unknown law is not guilt.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:extortion",
        "classification": "APPROVED DESIGN",
        "conduct": "Threat or abuse used to extract money, labor or property.",
        "offense_class": "serious-to-grave",
        "evidence_requirements": "Threat, demand, coercive circumstances and identity; coercive protection fees are not lawful tolls.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:illegal-detention",
        "classification": "APPROVED DESIGN",
        "conduct": "Confinement or continued holding without adequate lawful authority.",
        "offense_class": "serious-to-grave",
        "evidence_requirements": "Legal basis, scope, necessity, review and actual custody; private force confers no blanket police power.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:kidnapping",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful taking or holding of a person.",
        "offense_class": "serious-to-grave",
        "evidence_requirements": "Person’s independent account, movement/control, consent and lawful-basis review.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:trafficking",
        "classification": "APPROVED DESIGN",
        "conduct": "Obtaining, moving or controlling persons for exploitation through coercion or other unlawful means.",
        "offense_class": "grave",
        "evidence_requirements": "Coercion, confinement, document/earnings control and exploitation; consensual adult work is distinct.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:property-destruction",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful damage to another’s property or community works.",
        "offense_class": "minor-to-grave",
        "evidence_requirements": "Title, damage, causation and intent; distinguish accident and necessary rescue.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:illegal-magical-experimentation",
        "classification": "APPROVED DESIGN",
        "conduct": "Nonconsensual, prohibited or unlawfully dangerous magical experiments on persons/wards.",
        "offense_class": "serious-to-grave",
        "evidence_requirements": "Consent, demonstrated acts/risk and applicable prohibition; magical talent or ancestry is no offense.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:unlicensed-dangerous-magic",
        "classification": "APPROVED DESIGN",
        "conduct": "Dangerous magical activity requiring a demonstrably applicable authorization.",
        "offense_class": "serious",
        "evidence_requirements": "Prove the rule, jurisdiction, actual activity and risk; no newly invented spell or universal magic ban.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:unlawful-mining",
        "classification": "APPROVED DESIGN",
        "conduct": "Extraction without lawful title/access or in breach of applicable safety restrictions.",
        "offense_class": "minor-to-grave",
        "evidence_requirements": "Resource rights, place, actions and relevant safety/permit rules; no mine ownership inferred.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:unlawful-timber",
        "classification": "APPROVED DESIGN",
        "conduct": "Unlawful felling, timber theft or breach of applicable woodland access limits.",
        "offense_class": "minor-to-serious",
        "evidence_requirements": "Timber provenance, land/customary rights, actual cutting and applicable limits.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:contract-fraud",
        "classification": "APPROVED DESIGN",
        "conduct": "Deliberate deception in contracting, performance records or payment claims.",
        "offense_class": "minor-to-serious",
        "evidence_requirements": "Agreed terms, capacity/authority, misrepresentation and actual loss; ordinary breach can remain civil.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:cargo-theft",
        "classification": "APPROVED DESIGN",
        "conduct": "Taking entrusted or carried goods without lawful title.",
        "offense_class": "serious",
        "evidence_requirements": "Cargo ownership, bailment/manifest evidence and custody chain; manifests do not automatically transfer title.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:organized-crime",
        "classification": "APPROVED DESIGN",
        "conduct": "Proved knowing participation in specific unlawful coordinated conduct.",
        "offense_class": "serious-to-grave",
        "evidence_requirements": "Individual acts/knowledge and corroborated links; faction label, association or ancestry is not guilt.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      },
      {
        "id": "offense:obstruction",
        "classification": "APPROVED DESIGN",
        "conduct": "Knowing unlawful interference with a lawful investigation or evidence.",
        "offense_class": "minor-to-serious",
        "evidence_requirements": "First prove lawful investigative authority and intentional interference; petition, appeal or silence is not automatic obstruction.",
        "realm_treatment": [
          {
            "realm_id": "valedorn",
            "investigation_authority_id": "government:valedorn-watch",
            "trial_authority_id": "government:valedorn-regional-courts",
            "appeal_authority_id": "government:valedorn-high-court",
            "local_variation": "Magistrates apply proved Crown/local law; noble privilege and royal requests do not remove hearings or appeal.",
            "local_trial_authority_id": "government:valedorn-local-courts"
          },
          {
            "realm_id": "elyndor",
            "investigation_authority_id": "government:elyndor-watch",
            "trial_authority_id": "government:elyndor-regional-courts",
            "appeal_authority_id": "government:elyndor-high-court",
            "local_variation": "Community mediation may resolve voluntary civil matters; harm/coercion needs independent adjudication. Conservation/custom needs proof and cannot compel consent.",
            "local_trial_authority_id": "government:elyndor-local-courts"
          },
          {
            "realm_id": "ironhollow-holds",
            "investigation_authority_id": "government:ironhollow-holds-watch",
            "trial_authority_id": "government:ironhollow-holds-regional-courts",
            "appeal_authority_id": "government:ironhollow-holds-high-court",
            "local_variation": "Clan and work-right evidence matters; an interested clan speaker or employer must recuse. Worker debt gives no forced-labor right.",
            "local_trial_authority_id": "government:ironhollow-holds-local-courts"
          },
          {
            "realm_id": "rivermere-league",
            "investigation_authority_id": "government:rivermere-league-watch",
            "trial_authority_id": "government:rivermere-league-regional-courts",
            "appeal_authority_id": "government:rivermere-league-high-court",
            "local_variation": "Charter/customs and cargo documents need authentication; merchant arbitration cannot substitute for serious criminal due process.",
            "local_trial_authority_id": "government:rivermere-league-local-courts"
          },
          {
            "realm_id": "frostmarch",
            "investigation_authority_id": "government:frostmarch-watch",
            "trial_authority_id": "government:frostmarch-regional-courts",
            "appeal_authority_id": "government:frostmarch-high-court",
            "local_variation": "Witnessed clan custom and rights require proof. Winter necessity is documented, proportionate and reviewable; weather is no excuse for indefinite detention.",
            "local_trial_authority_id": "government:frostmarch-local-courts"
          }
        ],
        "sanctions": "Only after a supported lawful finding: proportionate restitution, fine, limited custody or relevant license restriction as locally authorized; grave sanctions require enhanced independent review and explicit lawful basis. No tariff, mandatory sentence, exile or execution is enacted or applied by this record.",
        "appeal_and_limits": "Independent appeal, disputed evidence review, conflict recusal and correction/redress procedures. No collective punishment, forced labor/debt bondage, torture or automatic confiscation; historical judgments are unchanged.",
        "actual_cases": []
      }
    ],
    "business_regulations": [
      {
        "id": "business-law:hospitality",
        "name": "Inns and taverns",
        "classification": "APPROVED DESIGN",
        "categories": [
          "inn",
          "tavern"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Hygiene, fire safety, honest charges, safe lodging and voluntary adult employment; no current opening/license is inferred.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:gambling",
        "name": "Gambling houses",
        "classification": "APPROVED DESIGN",
        "categories": [
          "gambling"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "TOLERATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "TOLERATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Voluntary finite adult stakes, transparent rules and no coerced credit; toleration requires verified local custom.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:adult-entertainment",
        "name": "Brothels and pleasure houses",
        "classification": "APPROVED DESIGN",
        "categories": [
          "brothel",
          "pleasure-house"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "TOLERATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "All workers are consenting adults with independent agency and control of earnings, documents and personal boundaries; can refuse clients and leave. Coercion, confinement, trafficking, debt bondage and violence are prohibited exploitation.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:pawnshops",
        "name": "Pawnshops",
        "classification": "APPROVED DESIGN",
        "categories": [
          "pawnshop"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Document lawful pledge/title, agreed redemption terms and stolen-property handling; no ownership transfer or debt is fabricated.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:markets",
        "name": "Markets and general commerce",
        "classification": "APPROVED DESIGN",
        "categories": [
          "market",
          "general-store"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "LAWFUL",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "LAWFUL",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "LAWFUL",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "LAWFUL",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "LAWFUL",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Honest weights/description, lawful title and reviewable local access/fees; no new vendor tax or stock.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:couriers",
        "name": "Courier businesses",
        "classification": "APPROVED DESIGN",
        "categories": [
          "courier",
          "caravan"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Packet custody, privacy, willing lawful carriers, route compatibility and evidence-backed delivery; no guaranteed receipt or universal courier power.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:warehouses",
        "name": "Warehouses",
        "classification": "APPROVED DESIGN",
        "categories": [
          "warehouse"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Cargo custody, fire/flood handling, access permissions and documented loss review; inspection needs lawful scope.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:mercenaries",
        "name": "Mercenary companies",
        "classification": "APPROVED DESIGN",
        "categories": [],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Document lawful contract/command, weapons conduct and finite personnel; contracts and rank confer no general arrest or sentencing power.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:magical-shops",
        "name": "Magical shops",
        "classification": "APPROVED DESIGN",
        "categories": [],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Truthful appraisal, demonstrated ability and item provenance; dangerous activity needs applicable permission and consent. No enchanted stock or new spell is granted.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:healing",
        "name": "Healing establishments",
        "classification": "APPROVED DESIGN",
        "categories": [
          "healer",
          "herbalist",
          "apothecary"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Competence, botanical identification, consent, confidentiality and safe treatment; no miracle, patient appointment or fee is inferred.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:extraction",
        "name": "Mining and forestry operations",
        "classification": "APPROVED DESIGN",
        "categories": [
          "forestry",
          "quarry-supplier",
          "mason"
        ],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "REGULATED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Lawful title/access, conservation and trained safe paid labor; no automatic concession, resource yield or workplace assignment.",
        "current_licenses": [],
        "actual_enforcement_events": []
      },
      {
        "id": "business-law:exploitation",
        "name": "Coercive exploitation and unlawful commerce",
        "classification": "APPROVED DESIGN",
        "categories": [],
        "realm_statuses": [
          {
            "realm_id": "valedorn",
            "design_status": "PROHIBITED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "elyndor",
            "design_status": "PROHIBITED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "ironhollow-holds",
            "design_status": "PROHIBITED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "rivermere-league",
            "design_status": "PROHIBITED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          },
          {
            "realm_id": "frostmarch",
            "design_status": "PROHIBITED",
            "qualification": "Design policy only. Establish actual jurisdiction, applicable law/custom, permission and compliance before classifying a particular operation; no license or actual immunity."
          }
        ],
        "compliance": "Coercion, trafficking, violent debt enforcement, stolen goods and forged permits are prohibited conduct, distinct from lawful consensual work.",
        "current_licenses": [],
        "actual_enforcement_events": []
      }
    ],
    "business_links": [
      {
        "business_id": "caelthorne:crownstep-exchange",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:pawnshops",
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "caelthorne:lampwright-house",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "caelthorne:hearthbell-inn",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "caelthorne:three-copper-cups",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:gambling"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "caelthorne:amber-curtain",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:adult-entertainment"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "caelthorne:blue-thimble",
        "parent_location_id": "caelthorne",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "eastrun:bushel-and-bridle",
        "parent_location_id": "eastrun",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "eastrun:oat-crown-yard",
        "parent_location_id": "eastrun",
        "regulation_ids": [
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "eastrun:millrace-iron",
        "parent_location_id": "eastrun",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "eastrun:orchard-rest",
        "parent_location_id": "eastrun",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "eastrun:green-measure",
        "parent_location_id": "eastrun",
        "regulation_ids": [
          "business-law:healing"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "briarfall-crossing:copper-hoop-yard",
        "parent_location_id": "briarfall-crossing",
        "regulation_ids": [
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "briarfall-crossing:sawyers-table",
        "parent_location_id": "briarfall-crossing",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "briarfall-crossing:bridge-rest",
        "parent_location_id": "briarfall-crossing",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "briarfall-crossing:fern-and-kettle",
        "parent_location_id": "briarfall-crossing",
        "regulation_ids": [
          "business-law:healing"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "rivermere:reedseal-stores",
        "parent_location_id": "rivermere",
        "regulation_ids": [
          "business-law:markets",
          "business-law:couriers",
          "business-law:warehouses"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "rivermere:net-and-needle",
        "parent_location_id": "rivermere",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "rivermere:saltbell-kitchen",
        "parent_location_id": "rivermere",
        "regulation_ids": [
          "business-law:hospitality"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "rivermere:river-lantern",
        "parent_location_id": "rivermere",
        "regulation_ids": [
          "business-law:adult-entertainment"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "rivermere:nine-knots",
        "parent_location_id": "rivermere",
        "regulation_ids": [
          "business-law:gambling",
          "business-law:pawnshops"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "ironhollow-hold:true-spark",
        "parent_location_id": "ironhollow-hold",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "ironhollow-hold:plumbline-yard",
        "parent_location_id": "ironhollow-hold",
        "regulation_ids": [
          "business-law:extraction"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "ironhollow-hold:hearthgate-provisions",
        "parent_location_id": "ironhollow-hold",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "ironhollow-hold:clan-road-rest",
        "parent_location_id": "ironhollow-hold",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "brackenford:willow-lantern",
        "parent_location_id": "brackenford",
        "regulation_ids": [
          "business-law:hospitality"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "brackenford:forge",
        "parent_location_id": "brackenford",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "brackenford:herbalist",
        "parent_location_id": "brackenford",
        "regulation_ids": [
          "business-law:healing"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "brackenford:watermill",
        "parent_location_id": "brackenford",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "brackenford:market",
        "parent_location_id": "brackenford",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "silverbrook:honeycomb-bench",
        "parent_location_id": "silverbrook",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "silverbrook:green-spoon",
        "parent_location_id": "silverbrook",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "silverbrook:leafmark-yard",
        "parent_location_id": "silverbrook",
        "regulation_ids": [
          "business-law:extraction"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "stoneford:straightedge-yard",
        "parent_location_id": "stoneford",
        "regulation_ids": [
          "business-law:extraction"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "stoneford:fordpantry",
        "parent_location_id": "stoneford",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "stoneford:resting-plumb",
        "parent_location_id": "stoneford",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "southbank-landing:grainstep-stores",
        "parent_location_id": "southbank-landing",
        "regulation_ids": [
          "business-law:markets",
          "business-law:warehouses"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "southbank-landing:reed-oar",
        "parent_location_id": "southbank-landing",
        "regulation_ids": [
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "southbank-landing:netmenders-bowl",
        "parent_location_id": "southbank-landing",
        "regulation_ids": [
          "business-law:hospitality"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "southbank-landing:banklight-ledger",
        "parent_location_id": "southbank-landing",
        "regulation_ids": [
          "business-law:pawnshops",
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "windmere:wool-and-salt",
        "parent_location_id": "windmere",
        "regulation_ids": [
          "business-law:markets"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      },
      {
        "business_id": "windmere:shearers-hearth",
        "parent_location_id": "windmere",
        "regulation_ids": [
          "business-law:hospitality",
          "business-law:couriers"
        ],
        "actual_legal_status": null,
        "actual_license": null,
        "jurisdiction_verified": false
      }
    ],
    "organized_crime_responses": [
      {
        "design_label": "Gilded Hand",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Extortion, forged instruments and unlawful games",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Thornless Circle",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Restricted botanical provenance and stolen-artifact title",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Black Pick Syndicate",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Mine access, ore/title records and counterfeit material",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Sable Current",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Cargo manifests, custody and actual lawful customs scope",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Red Antler Brotherhood",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Raid/extortion complaints, identity and frontier jurisdiction",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Veiled Coin Exchange",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Documented provenance and specific proceeds tracing",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Broken Seal Society",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Seal/warrant authentication and document custody",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      },
      {
        "design_label": "Nightglass Circle",
        "scope": "Legal-response context only; organizational owner/profile remains PR4",
        "investigative_focus": "Evidence of specific unlawful experiments and restricted objects",
        "required_safeguards": "Prove specific conduct and individual knowledge; warrants, custody, reliable evidence, financial source tracing and independent review. No guilt from association.",
        "actual_investigations": [],
        "secret_connections": []
      }
    ],
    "oversight": {
      "investigation": "Preserve original warrants, testimony, item provenance and custody chains. Investigators must have verified authority and record exculpatory as well as inculpatory evidence.",
      "financial_fraud": "Trace actual title, invoices, counterparties and once-only source-backed records; only the sole finance authority posts actual money. No speculative balance, seizure, fine, restitution or tax is entered.",
      "cross_jurisdiction": "Request competent local cooperation with bounded purpose, evidence sharing consent/lawful authority and independently verified transport; no automatic extradition or treaty.",
      "witnesses_informants": "Consent, safety review, careful reliability assessment and access-limited storage are required. This public repository stores no confidential witness/informant identities, locations or promises. Protection is not detention by default.",
      "official_misconduct": "Recuse interested officers/judges, preserve complaints, permit independent review and appeals, protect safe reporting and assess redress. No official is declared corrupt here.",
      "wrongful_conviction": "Reconsider reliable new/exculpatory evidence through independent process; supported release/correction/redress needs an actual lawful decision. Do not reverse an old judgment through maintenance."
    },
    "rank_and_capture_limits": "Guild/adventurer rank, wealth, noble title, fame, private property and nonlethal preferences confer no unlimited police power. Citizen intervention needs an established local basis; guild discipline, military review, private restitution and civilian judgments remain distinct.",
    "action_template": {
      "action_id": null,
      "action_type": null,
      "status": "proposed",
      "arresting_authority_id": null,
      "sending_authority_id": null,
      "legal_basis": null,
      "subject_ref": null,
      "date": null,
      "time": null,
      "location_id": null,
      "custody_officer_id": null,
      "evidence_inventory_ref": null,
      "property_inventory_ref": null,
      "receiving_authority_id": null,
      "destination_facility_id": null,
      "receiving_officer_id": null,
      "transport_requirements": null,
      "departure_ref": null,
      "arrival_ref": null,
      "transfer_receipt_ref": null,
      "medical_condition": null,
      "review_order_ref": null,
      "release_or_disposition_status": null,
      "source_refs": []
    },
    "actual_arrests": [],
    "actual_transfers": [],
    "actual_judgments": [],
    "actual_tax_fine_or_fee_events": [],
    "actual_political_events": [],
    "automatic_outcomes": false
  }
}
```

## Phase 2 legal approval scope

The original top-level PROPOSED process/taxonomy records remain a dated baseline. approved_legal_design now owns approved fictional procedures, offenses and conditional realm/business rules; it does not enact a historical statute or appoint a court. Existing authority/custody/evidence/finance records retain precedence and all actual event slots remain empty. No historical gap or judgment is filled. Facility design approval alone cannot satisfy the existing validate_transfer operational/authority checks.
