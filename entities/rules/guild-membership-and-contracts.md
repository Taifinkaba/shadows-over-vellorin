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
  "automatic_world_events": false
}
```
