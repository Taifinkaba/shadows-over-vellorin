---
id: quest-evidence-and-mysteries
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/main-quest-framework-maintenance.md
- state/checkpoint.json
- state/open-verifications.md
- entities/mechanics/seven-bells-inventory.md
- entities/quests/first-hour-restoration.md
- entities/quests/first-oath-conspiracy.md
- entities/quests/seven-bells-investigation.md
- entities/quests/freight-ward-conspiracy.md
- entities/quests/a07-signature.md
- entities/quests/fifth-bell-threat.md
- entities/quests/artificial-witness.md
- entities/quests/v9-memories.md
---

# Evidence and unresolved-question routing

Eighteen unanswered-question handles and seventeen evidence-reference scopes, not new mysteries invented from silence or copied inventory. Each question exists in its original quest/verification sources. CONFIRMED CANON confirms that source-backed question/evidence scope only; proposed ending roles are not approved obligations. Answer values remain null. Empty alleged/disproven arrays mean no separately indexed classification in this routing, not that all source claims are proven or nothing was disproven. Read owner text for confirmed/alleged/refuted/unknown distinctions and later supersessions.

Evidence types separate authenticated documents, physical evidence, testimony, confession, limited mental-probe observations, historical records, theories, deliberate misinformation and unverified allegations. Only source-established authentication is labeled authenticated; designation alone proves no authorship, guilt or consent. A confession is a statement with limits, not automatic conviction. Corven's interrupted surface probe did not yield unrestricted memories or certify every suspicion. The damaged ...ven signature identifies no person. Ashvale resonance remains a theory. Third Bell clapper is not Fifth Bell; V-9 vessels are not cases or persons; A-07 is not automatically AV-07.

Clues route the original owner/locator, actual discovery narrative and custody owner. They do not add physical objects, holder/storage, found-location coordinates or a second recovered batch. Original third leaf stays protected in situ; its transcription is a copy. E-R-7 remains installed, VII/R and command plate remain distinct dangerous/isolated evidence. Registers being located does not supply every person's testimony or a new inventory transfer. Unknown container/custodian stays UNKNOWN. Older custody/presence is not current destination.

Future clue records in original owners support clue ID/source/found-place/discovery event/type/custody, narrow proves/does-not-prove claims, associated question, Theron/companion discovery evidence, GM knowledge boundary, reliability/uncertainty and supported next lead. Those fields are a contract, not a public dump of hidden answers. No party member automatically shares knowledge. Each next-action key is a possible investigation request, not travel, a guaranteed cooperative witness, a clue already found or an approved secret location. Read existing office/workshop/source geography and limitations before offering choices.


```json
{
  "schema_version": 1,
  "clues": [
    {
      "clue_id": "clue:third-leaf",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "Original third sealed leaf"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:leaf-transcription",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "Returned-leaf exact transcription"
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:er7",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "E-R-7 fractured-seat fitting"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:viir",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "Removed hostile fitting `VII / R`"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:counterfeit-plate",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "Black-metal counterfeit command plate"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:blue-case",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "Blue case"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:wa17",
      "owner_ref": "seven-bells-inventory",
      "source_locator": {
        "source_ref": "entities/mechanics/seven-bells-inventory.md",
        "quote": "WA-17 empty silver fitting housing with violet residue"
      },
      "evidence_type": "physical-evidence",
      "custody_owner_ref": "seven-bells-inventory",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:witness-registers",
      "owner_ref": "first-hour-restoration",
      "source_locator": {
        "source_ref": "entities/quests/first-hour-restoration.md",
        "quote": "Three Witness registers recovered, authenticated and protected:"
      },
      "evidence_type": "authenticated-document",
      "custody_owner_ref": "first-hour-restoration",
      "discovery_owner_ref": "first-hour-restoration",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:v9-registers",
      "owner_ref": "first-oath-conspiracy",
      "source_locator": {
        "source_ref": "entities/quests/first-oath-conspiracy.md",
        "quote": "V-9 original registers located."
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "first-oath-conspiracy",
      "discovery_owner_ref": "first-oath-conspiracy",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:ss41-chain",
      "owner_ref": "first-oath-conspiracy",
      "source_locator": {
        "source_ref": "entities/quests/first-oath-conspiracy.md",
        "quote": "SS-41 bounty: originally drafted by Corvin Dareth,"
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "first-oath-conspiracy",
      "discovery_owner_ref": "first-oath-conspiracy",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:limited-probe",
      "owner_ref": "seven-bells-investigation",
      "source_locator": {
        "source_ref": "entities/quests/seven-bells-investigation.md",
        "quote": "Connection ended on resistance, no deeper memory extraction/alteration."
      },
      "evidence_type": "limited-mental-probe",
      "custody_owner_ref": "seven-bells-investigation",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:freight-records",
      "owner_ref": "freight-ward-conspiracy",
      "source_locator": {
        "source_ref": "entities/quests/freight-ward-conspiracy.md",
        "quote": "certified correspondence obtained."
      },
      "evidence_type": "authenticated-document",
      "custody_owner_ref": "freight-ward-conspiracy",
      "discovery_owner_ref": "freight-ward-conspiracy",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:a07",
      "owner_ref": "a07-signature",
      "source_locator": {
        "source_ref": "entities/quests/a07-signature.md",
        "quote": "Authenticity, consent, motive and custody unknown."
      },
      "evidence_type": "unverified-allegation",
      "custody_owner_ref": "a07-signature",
      "discovery_owner_ref": "a07-signature",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:resonance",
      "owner_ref": "first-oath-conspiracy",
      "source_locator": {
        "source_ref": "entities/quests/first-oath-conspiracy.md",
        "quote": "Ashvale resonance theory not proven."
      },
      "evidence_type": "theory",
      "custody_owner_ref": "first-oath-conspiracy",
      "discovery_owner_ref": "first-oath-conspiracy",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:damaged-signature",
      "owner_ref": "seven-bells-investigation",
      "source_locator": {
        "source_ref": "entities/quests/seven-bells-investigation.md",
        "quote": "Damaged signature ends approximately `...ven`, not an identified person."
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "seven-bells-investigation",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:anonymous-letter",
      "owner_ref": "seven-bells-investigation",
      "source_locator": {
        "source_ref": "entities/quests/seven-bells-investigation.md",
        "quote": "Anonymous Witness letter indicated eastern independent passage; sender unknown."
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "seven-bells-investigation",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    },
    {
      "clue_id": "clue:watcher-map",
      "owner_ref": "seven-bells-investigation",
      "source_locator": {
        "source_ref": "entities/quests/seven-bells-investigation.md",
        "quote": "watcher remains unidentified/free."
      },
      "evidence_type": "historical-record",
      "custody_owner_ref": "seven-bells-investigation",
      "discovery_owner_ref": "seven-bells-investigation",
      "knowledge": "requires-discovery-review",
      "new_item": false
    }
  ],
  "mysteries": [
    {
      "mystery_id": "mystery:fb5",
      "quest_owner_id": "fifth-bell-threat",
      "question": "What is the unresolved foreign layer/FB-5, and what bounded threat resolution is justified?",
      "confirmed_refs": [
        "entities/quests/fifth-bell-threat.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:resonance"
      ],
      "last_status_owner_ref": "fifth-bell-threat",
      "freshness_refs": [
        "entities/quests/fifth-bell-threat.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "review-bell-evidence",
      "proposed_objective_ids": [
        "objective:fifth-bell"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:northern-index",
      "quest_owner_id": "seven-bells-investigation",
      "question": "Where is the referenced Northern Witness Index and what does it establish?",
      "confirmed_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:third-leaf",
        "clue:damaged-signature"
      ],
      "last_status_owner_ref": "seven-bells-investigation",
      "freshness_refs": [
        "entities/quests/seven-bells-investigation.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "review-index-references",
      "proposed_objective_ids": [
        "objective:counterfeit-authority"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:er7-safety",
      "quest_owner_id": "seven-bells-investigation",
      "question": "What authority/safety remains in the installed E-R-7 fitting?",
      "confirmed_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:er7",
        "clue:viir",
        "clue:counterfeit-plate"
      ],
      "last_status_owner_ref": "seven-bells-investigation",
      "freshness_refs": [
        "entities/quests/seven-bells-investigation.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "assess-existing-fitting",
      "proposed_objective_ids": [
        "objective:counterfeit-authority"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:witness-authority",
      "quest_owner_id": "artificial-witness",
      "question": "Which surviving claims of Witness authority are authentic, counterfeit or unauthorized?",
      "confirmed_refs": [
        "entities/quests/artificial-witness.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:third-leaf",
        "clue:witness-registers",
        "clue:counterfeit-plate"
      ],
      "last_status_owner_ref": "artificial-witness",
      "freshness_refs": [
        "entities/quests/artificial-witness.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "compare-protected-records",
      "proposed_objective_ids": [
        "objective:counterfeit-authority",
        "objective:witness-choice"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:surviving-crown",
      "quest_owner_id": "first-oath-conspiracy",
      "question": "Which surviving operations and responsible command links are supported by evidence?",
      "confirmed_refs": [
        "entities/quests/first-oath-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:ss41-chain",
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "first-oath-conspiracy",
      "freshness_refs": [
        "entities/quests/first-oath-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "review-command-records",
      "proposed_objective_ids": [
        "objective:command-chain",
        "objective:surviving-opposition"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:v9-transferred",
      "quest_owner_id": "v9-memories",
      "question": "What is the lawful verified disposition of the unresolved transferred case?",
      "confirmed_refs": [
        "entities/quests/v9-memories.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "v9-memories",
      "freshness_refs": [
        "entities/quests/v9-memories.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "seek-case-disposition",
      "proposed_objective_ids": [
        "objective:v9-harm"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:v9-other-cases",
      "quest_owner_id": "v9-memories",
      "question": "What remains for distinct documented V-9 cases beyond Lyanna and the already reviewed releases?",
      "confirmed_refs": [
        "entities/quests/v9-memories.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "v9-memories",
      "freshness_refs": [
        "entities/quests/v9-memories.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "review-distinct-cases",
      "proposed_objective_ids": [
        "objective:v9-harm"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:dene",
      "quest_owner_id": "first-oath-conspiracy",
      "question": "Where is Halric Dene and what further evidence or lawful response is available?",
      "confirmed_refs": [
        "entities/quests/first-oath-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "first-oath-conspiracy",
      "freshness_refs": [
        "entities/quests/first-oath-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "seek-sourced-location",
      "proposed_objective_ids": [
        "objective:surviving-opposition"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:thane-review",
      "quest_owner_id": "first-oath-conspiracy",
      "question": "What independent legal review follows Thane surrender?",
      "confirmed_refs": [
        "entities/quests/first-oath-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "first-oath-conspiracy",
      "freshness_refs": [
        "entities/quests/first-oath-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "request-lawful-review",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:sorn-review",
      "quest_owner_id": "first-oath-conspiracy",
      "question": "What military review follows relinquished command?",
      "confirmed_refs": [
        "entities/quests/first-oath-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "first-oath-conspiracy",
      "freshness_refs": [
        "entities/quests/first-oath-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "request-lawful-review",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:remaining-notices",
      "quest_owner_id": "first-oath-conspiracy",
      "question": "Which independent notices, if any, still apply after the specific SS-41 withdrawal?",
      "confirmed_refs": [
        "entities/quests/first-oath-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:ss41-chain"
      ],
      "last_status_owner_ref": "first-oath-conspiracy",
      "freshness_refs": [
        "entities/quests/first-oath-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "verify-notice-scope",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:a07-consent",
      "quest_owner_id": "a07-signature",
      "question": "Was the historical A-07 signature authentic and freely given, and in what circumstances?",
      "confirmed_refs": [
        "entities/quests/a07-signature.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:a07"
      ],
      "last_status_owner_ref": "a07-signature",
      "freshness_refs": [
        "entities/quests/a07-signature.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "verify-signature-context",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:correspondent",
      "quest_owner_id": "seven-bells-investigation",
      "question": "Who sent the anonymous Witness letter?",
      "confirmed_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:anonymous-letter"
      ],
      "last_status_owner_ref": "seven-bells-investigation",
      "freshness_refs": [
        "entities/quests/seven-bells-investigation.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "trace-existing-correspondence",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:watcher",
      "quest_owner_id": "seven-bells-investigation",
      "question": "Who was the hooded watcher and is there evidence of a link to the correspondent?",
      "confirmed_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:watcher-map"
      ],
      "last_status_owner_ref": "seven-bells-investigation",
      "freshness_refs": [
        "entities/quests/seven-bells-investigation.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "review-watcher-evidence",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:freight-director",
      "quest_owner_id": "freight-ward-conspiracy",
      "question": "Who directed the confirmed freight/ward crimes and are broader links actually proven?",
      "confirmed_refs": [
        "entities/quests/freight-ward-conspiracy.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:freight-records"
      ],
      "last_status_owner_ref": "freight-ward-conspiracy",
      "freshness_refs": [
        "entities/quests/freight-ward-conspiracy.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "trace-certified-routing",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:acting-receiver",
      "quest_owner_id": "seven-bells-investigation",
      "question": "What can be verified about alleged receiving-office/workshop roles?",
      "confirmed_refs": [
        "entities/quests/seven-bells-investigation.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:blue-case",
        "clue:wa17",
        "clue:limited-probe"
      ],
      "last_status_owner_ref": "seven-bells-investigation",
      "freshness_refs": [
        "entities/quests/seven-bells-investigation.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "follow-existing-office-leads",
      "proposed_objective_ids": [
        "objective:surviving-opposition"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:damaged-channels",
      "quest_owner_id": "first-hour-restoration",
      "question": "What remains of other damaged Guardian channels after the completed First Hour restoration?",
      "confirmed_refs": [
        "entities/quests/first-hour-restoration.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:witness-registers"
      ],
      "last_status_owner_ref": "first-hour-restoration",
      "freshness_refs": [
        "entities/quests/first-hour-restoration.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "scope-remaining-restoration",
      "proposed_objective_ids": [],
      "main_ending_role": "OPTIONAL OR CONSEQUENCE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    },
    {
      "mystery_id": "mystery:v9-controller",
      "quest_owner_id": "v9-memories",
      "question": "Does evidence establish a specific V-9 controller beyond the known authorization chain?",
      "confirmed_refs": [
        "entities/quests/v9-memories.md"
      ],
      "alleged_refs": [],
      "disproven_refs": [],
      "unknown_answer": null,
      "clue_ids": [
        "clue:v9-registers"
      ],
      "last_status_owner_ref": "v9-memories",
      "freshness_refs": [
        "entities/quests/v9-memories.md",
        "state/checkpoint.json",
        "state/open-verifications.md"
      ],
      "knowledge": "requires-discovery-review",
      "next_action_key": "separate-controller-from-authority",
      "proposed_objective_ids": [
        "objective:command-chain"
      ],
      "main_ending_role": "PROPOSED CORE",
      "answer_approval": "REQUIRES APPROVAL",
      "classification": "CONFIRMED CANON"
    }
  ],
  "clue_field_contract": [
    "clue_id",
    "source_record",
    "found_location",
    "discovery_event",
    "evidence_type",
    "custody",
    "proves",
    "does_not_prove",
    "question_id",
    "theron_discovery",
    "companion_discovery",
    "gm_boundary",
    "reliability",
    "next_supported_lead"
  ],
  "evidence_types": [
    "authenticated-document",
    "physical-evidence",
    "witness-testimony",
    "confession",
    "limited-mental-probe",
    "historical-record",
    "theory",
    "deliberate-misinformation",
    "unverified-allegation"
  ],
  "new_evidence_items": [],
  "new_discoveries": [],
  "new_resolutions": []
}
```
