---
id: guild-membership-and-contracts
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/guild-concord-contracts-design.md
- entities/factions/wayfarers-guild.md
- entities/factions/dragon-slayer-academy.md
- entities/mechanics/guild-animal-registry.md
- entities/mechanics/party-finances.md
- entities/rules/justice-and-jurisdiction.md
- changes/chronicles/phase2-04-guild-underworld-approval.md
---

# Guild membership, rank and contract procedure

The lookup and preservation rules are maintenance canon; joining/examination/review designs remain PROPOSED until approved. No enrollment, assessment, promotion, suspension or revocation is performed here.

## Retrieval and professional independence

Resolve guild-network, then only the relevant faction profile and its branch or contract ID. Known headquarters city does not certify a hall address, public board, officer, opening hours, stock or availability. Unnamed branches remain unlocated. Inspect branch route owners for classification; a proposed connection is not a functioning trade/supply network. Archived professional designs stay archived until individually approved. No new NPC is appointed from a role label.

## Rank and certification boundaries

Keep guild license rank, character combat power, dungeon threat rank, professional skill certification and contract difficulty distinct. Preserve existing labels as recorded, including the source term Guild measurements: Theron S+, Lyanna/Garrick/Nyx/Lyra A+, Level5. Do not relabel them as newly issued Concord licenses, revoke existing guild standing or assume universal professional competence. Existing character owners retain numerical/rank authority; skills stay with their mechanic owners. Animal measured ranks/maxima remain with guild-animal-registry and creature owners, not automatically current pools or professional licenses. Dragon Slayer remains locked by player choice; academy participation and an offered preliminary assessment are not completed certification.

## Proposed membership/examination process

Registration → identity/consent review → relevant entry assessment → practical demonstration → profession-specific placement → documented specialization/advancement → renewal where approved → notice/review of suspension → independent appeal → supported license revocation if lawfully decided. These are review steps, not a mandatory completed history. Assess the profession: a merchant demonstrates trade/accounting, not monster combat; a healer demonstrates care and safety, a craftsperson craft competence. No numeric DCs, fees, deadlines, badges or ranks are newly awarded. Existing membership and licenses stay unchanged.

## Contract intake, funding and completion

A future contract records original ID/issuer/registry, identifiable funding party and source, actual committed budget, objective/site, difficulty/eligibility, legal basis, acceptance/assignment/deadline, reward/fees, proof/conditions, completion/payment and dated source. Unknown fields stay null. An estimate or issuer name alone does not guarantee a reward: require a verified identifiable funder, source-backed commitment and sufficient budget before treating a stated reward as guaranteed. No unlimited guild cash or automatic contract generation.

Three historical payouts already included in party accounting remain reference-only; paid amounts are not new offers, free money or unpaid reward claims. Do not infer gross/net amounts or apply another10% from the archived commission reference. Existing costs/dues already paid are not deducted again. Future fees need explicit proposed/approved classification and source-backed terms; no fee, wage, commission, academy revenue or Concord dues are posted by maintenance. Independent academy funds, merchant goods and property stay excluded under party-finances.

During actual authorized play, record acceptance and actual evidence-based completion separately, review conditions and disputes, then use the existing finance ledger for one supported payment with a stable event key; internal transfers are not income. Ledger code and current balances are unchanged here. Historical paid-contract extraction needs no fictional original budget or bridge receipt; funding may remain unknown for history without blocking validation.

## Bounty, legal and dungeon boundaries

A guild contract is not an arrest warrant, allegation is not guilt, and authorized apprehension is not custody transfer, court review, conviction or sentence. Follow justice-and-jurisdiction and the single prisoner-custody owner; never place someone in an unapproved prison. A proposed Concord division grants no police power, immunity or retrospective title to seized goods. SS-41's specific guild registry revocation and withdrawn instruction do not cancel unrelated notices. Dispute resolution and any court must be sourced for the case; no new magistrate is invented.

Dungeon-related work may reference a known site and require exploration/rescue/survey/escort/containment/salvage/research proof. Site IDs must resolve, and no contract implies a dungeon is cleared, monsters defeated, materials owned or treasure payable. Chunk6 will integrate dungeon records; this chunk creates no site encounter or loot. Detailed NPC autonomy and scheduling remain for Chunk8.

Public lookup views contain ordinary services and proposals only. No hidden motives, identities or quest answers are copied; gm-reference links still require player-knowledge review before narration. Follow narration-format.md for attributed dialogue and independent closed bookkeeping disclosures.

```json
{
  "schema_version": 1,
  "rank_domains": [
    "guild-license",
    "combat-power",
    "dungeon-threat",
    "professional-certification",
    "contract-difficulty"
  ],
  "rank_owner_ids": [
    "theron-ashvale",
    "lyanna-ashvale",
    "garrick-vale",
    "nyx-thorne",
    "lyra-moonvale"
  ],
  "membership_procedure_classification": "PROPOSED",
  "membership_steps": [
    "registration",
    "identity-verification",
    "entry-examination",
    "practical-demonstration",
    "rank-advancement",
    "specialization",
    "renewal",
    "suspension-review",
    "appeal",
    "revocation-review"
  ],
  "npc_role_categories": [
    "guildmaster",
    "reception-clerk",
    "contract-officer",
    "examiner",
    "field-captain",
    "merchant-representative",
    "researcher",
    "independent-adventuring-party"
  ],
  "justice_workflow_ref": "justice-and-jurisdiction",
  "custody_owner_ref": "prisoner-custody",
  "finance_owner_ref": "party-finances",
  "new_license_records": [],
  "new_staff_records": [],
  "automatic_world_events": false,
  "approved_professional_rules": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md",
    "applies_to_guild_ids": [
      "ironhand-smiths-compact",
      "circle-of-seven-lamps",
      "scribes-collegium",
      "river-charter-league",
      "greenward-covenant",
      "stonewatch-wardens"
    ],
    "annual_dues_references": [
      {
        "membership": "apprentice",
        "amount_cp": 100,
        "period": "year",
        "kind": "approved-reference",
        "source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md"
      },
      {
        "membership": "journeyman",
        "amount_cp": 300,
        "period": "year",
        "kind": "approved-reference",
        "source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md"
      },
      {
        "membership": "master",
        "amount_cp": 800,
        "period": "year",
        "kind": "approved-reference",
        "source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md"
      },
      {
        "membership": "traveling-member",
        "amount_cp": 200,
        "period": "year",
        "kind": "approved-reference",
        "source_ref": "changes/chronicles/phase2-04-guild-underworld-approval.md"
      }
    ],
    "dues_scope": "Prospective rate references for separately agreed professional membership only, not retroactive charges. Traveling membership is a mode, not a fourth competence rank. No automatic stacking, Concord fee or application to existing Wayfarers/academy arrangements.",
    "professional_certification_levels": [
      "apprentice",
      "journeyman",
      "master"
    ],
    "traveling_member_is_rank": false,
    "automatic_combat_rank_equivalence": false,
    "combat_scale_policy": "Preserve existing Wayfarers F through S+ ranks and all current character ranks with their original meaning. A master craftsperson receives no automatic adventurer rank, spell, license or combat power.",
    "membership_and_elections": [
      "Voluntary application, identity and relevant skills review without invented past enrollment",
      "Willing paid/safe apprenticeship terms and supervised instruction",
      "Profession-specific examination with recorded criteria and independent review",
      "Certification only after an actual supported result, never from raw mana or combat rank alone",
      "Elected accountable guild delegates, recusal and member/worker representation; no current appointment",
      "Bounded privileges, work referrals and safe services without immunity or guaranteed work",
      "Misconduct inquiry with evidence, notice, defense, proportionate suspension and independent appeal",
      "Voluntary resignation/renewal and separately verified terms; no debt bondage or compelled labor"
    ],
    "contract_design_categories": [
      "apprenticeship-agreement",
      "skilled-labor",
      "caravan-protection",
      "research-commission",
      "material-procurement",
      "craft-certification",
      "merchant-arbitration",
      "guild-notice",
      "contract-dispute",
      "professional-discipline"
    ],
    "contract_template": {
      "id": null,
      "kind": null,
      "status": "proposed",
      "issuer": null,
      "worker_or_counterparty": null,
      "scope": null,
      "professional_competence": null,
      "consent_ref": null,
      "legal_authority_ref": null,
      "route_or_site_refs": [],
      "materials_and_safety": null,
      "term_or_deadline": null,
      "compensation_quote_cp": null,
      "verified_funding_ref": null,
      "acceptance_evidence": null,
      "completion_evidence": null,
      "payment_evidence": null,
      "source_refs": []
    },
    "association_statuses": [
      {
        "id": "lawful-guild",
        "classification": "APPROVED DESIGN",
        "meaning": "Recognized professional association; actual recognition must have applicable lawful evidence, not just a design label."
      },
      {
        "id": "unrecognized-association",
        "classification": "APPROVED DESIGN",
        "meaning": "Recognition unverified/absent; not automatically criminal, banned or deprived of ordinary rights."
      },
      {
        "id": "suspended-guild",
        "classification": "APPROVED DESIGN",
        "meaning": "Only an actual competent disciplinary decision with notice, reasons, defense and appeal can establish suspension."
      },
      {
        "id": "outlawed-organization",
        "classification": "APPROVED DESIGN",
        "meaning": "Requires a verified jurisdiction, competent lawful prohibition and reviewable decision; never a blanket worldwide ban."
      },
      {
        "id": "criminal-faction",
        "classification": "APPROVED DESIGN",
        "meaning": "Organizational unlawful-interest design; actual individual crimes, bans, warrants and seizures still require their own lawful evidence."
      }
    ],
    "legal_consequences": "Only an actual competent lawful decision can establish recognition, suspension or outlawing. Possible effects include bounded suspension of association privileges, restrictions on use of a credential, withdrawal of a particular registration or court-supervised activity restrictions in a proved jurisdiction, with notice, defense and appeal. This does not punish unrelated members/clients or cancel independent contracts/title. A criminal-design label or guild notice issues no warrant, convicts nobody, seizes nothing and transfers no property; each coercive act needs separate lawful authority and evidence.",
    "legal_decision_template": {
      "organization_id": null,
      "jurisdiction_id": null,
      "decision_kind": null,
      "competent_authority_id": null,
      "legal_basis_ref": null,
      "decision_evidence_ref": null,
      "notice_and_defense_ref": null,
      "appeal_or_review_ref": null,
      "effective_scope": null
    },
    "justice_owner_ref": "justice-and-jurisdiction",
    "finance_owner_ref": "party-finances",
    "autonomy_owner_ref": "npc-autonomy-and-time",
    "actual_memberships": [],
    "actual_examinations": [],
    "actual_certifications": [],
    "actual_dues_events": [],
    "actual_legal_bans": [],
    "actual_suspensions": [],
    "actual_contracts": [],
    "actual_hires": []
  }
}
```

## Phase 2 professional approval scope

approved_professional_rules adds prospective professional rules and dues, without altering original rank owners, licenses, membership records or contracts. Traveling membership is not combat rank. Association design classes are not actual registration, suspension or banning decisions. Actual future agreements need willing parties, competence, lawful scope, finite resources and original contract/finance owners. All new event slots are empty.
