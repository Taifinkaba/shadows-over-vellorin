# Phase 2 government and justice approval update

Read the [approved government/legal directory](phase2-government-and-law.md) and [PR3 review](phase2-03-review.md) first. PR1/2 established the five realm designs and settlements; PR3 adds government structures, legal procedures, five character designs and bounded design approval for exactly seven existing facility IDs. The earlier unknown-geography/unapproved-design explanations below are a dated baseline, superseded only for those approved fields. No operational building, actual appointment, jurisdiction expansion, prisoner, investigation, judgment or transfer is certified. The original historical authority/custody/evidence owners remain authoritative. Aveline’s existing proposal now resolves to the same character design; the proposed Chief Justice appointment is still unapproved.

---

# Justice and custody retrieval — Chunk 4

This directory links authority records and procedural design; it is not another custody register. Resolve entity IDs in [index.json](../index.json). Current custody remains in [prisoner-custody](../entities/mechanics/prisoner-custody.md), its dated sources and the existing checkpoint. Read the new source-routing section before treating older “current” headings as present placements. No historical outcome or current case state is copied here.

## Existing authorities

[justice-authorities](../entities/mechanics/justice-authorities.md) owns the scoped authority IDs, limited jurisdiction references and source quotes. These are existing functions, not new factions. A settlement is a contact context, not proof of a surveyed boundary, active patrol, available cell or receiving officer.

| Authority ID | Established reference | Preserved limits |
|---|---|---|
| `justice:caelthorne-magistrates` | Magistrates in [Caelthorne](../entities/locations/caelthorne.md) | Names, precise legal reach, court address and receiving/remand facility UNKNOWN |
| `justice:caelthorne-watch` | Existing Caelthorne watch | Station address, receiving officer, detention capacity and corridor coverage UNKNOWN |
| `justice:brackenford-government` | Reeve Elsbeth Marrin and council in [Brackenford](../entities/locations/brackenford.md) | Communal village governance; cottage ownership grants Theron no municipal authority |
| `justice:brackenford-watch` | Watch Captain Ressa Vale and six part-time members | Existing village watch; no inferred gaol, blanket road jurisdiction or named handover recipient |
| `justice:blackthorn-command` | Watch command/refuge functions at [Blackthorn Watch](../entities/locations/blackthorn-watch.md) | Civilian judicial power and current commander/receiver UNKNOWN; not North Waystation |
| `justice:wayfarers-contracts` | Existing [Wayfarers](../entities/factions/wayfarers-guild.md) contractual administration | Contracts confer no automatic police powers, immunity or criminal sentencing authority |
| `justice:ashvale-private-security` | Existing private estate management/security under Crown law | Tomas remains manager, not an appointed public police or prison officer; no municipal charter |

Mara Vey, Aldric Voss, Ressa Vale, Elsbeth Marrin and other established officials retain their existing records. No new station, rank, location, identity or receiving appointment is assigned to them. Military command, civilian enforcement, judicial review, civil disputes, guild discipline and private security remain different domains. Citizen intervention requires an established legal basis; neither adventurer rank nor reputation supplies one.

No independently verified named court/prison building or operational receiving facility is added by this chunk. Existing offices and historical guard positions do not certify an institutional building can accept a new prisoner today.

## Proposed hierarchy and approvals

[justice-proposals](../entities/mechanics/justice-proposals.md) is the authoritative approval crosswalk, metadata `research`, all entries explicitly PROPOSED/REQUIRES APPROVAL. Scoped proposal IDs are review records, not new indexed organizations, people or buildings. Valedorn's geographic identity, government and relationship to Vellorin are UNKNOWN; there is no claim it controls other nations.

| Proposed role | Existing function to reconcile before creating an organization |
|---|---|
| Royal Ministry of Justice | Existing magistrates; national administration/oversight remains only design |
| Crown Marshals | No verified equivalent cross-regional service; warrant scope/agreements unresolved |
| Regional Constabulary | Existing watch command; do not convert Blackthorn's command into a new civilian service |
| Town Watch | Existing Caelthorne/Brackenford watch; no replacement or new superiors |
| Village Constables | Existing village watch/reeve; no duplicate force or new powers |
| Prison Service | Operational institutions, staff and jurisdiction UNKNOWN |
| Court Officers | Existing magistrates remain authoritative; security/process posts unapproved |

To approve a missing institution: identify the exact claim and existing equivalent; supply its source; resolve geography, powers/limits, government affiliation and conflicting offices; explicitly approve that bounded proposal; then promote only sourced records in a separate PR with appropriate tests. A design discussion or PR approval does not establish an old event. Buildings, officers, jurisdictions, laws, court procedures, capacities and transfer arrangements have separate approval entries. No approval source is supplied in this chunk.

## Buildings and detention candidates

Every entry below is a World Bible2.2 proposal supplied in the request, **not verified historical premises or an operational destination**. Candidate settlement means proposed placement only, not a new address, political border or surveyed site. Because these are review candidates, no new location entities or coordinates are created. Existing settlement/location records remain the owners of geography.

| Proposal ID suffix (`proposal:building-…`) | Candidate building | Candidate context | Proposed detention type |
|---|---|---|---|
| `crown-hall` | Crown Hall of Justice | Caelthorne; reconcile existing magistrates | Court, no detention category established |
| `central-watchhouse` | Caelthorne Central Watchhouse | Caelthorne; reconcile existing watch | Type1 |
| `eastrun-station` | Eastrun Watch Station | Eastrun; no receiving station verified | Type1 |
| `briarfall-watchhouse` | Briarfall Crossing Watchhouse | Briarfall Crossing; existing trade road is not a verified gaol | Type1 |
| `blackthorn-constabulary` | Blackthorn Regional Constabulary | Blackthorn Watch context only; not identity with Watch/North Waystation | Office; cells UNKNOWN |
| `harbor-watch` | Rivermere Harbor Watch | Existing Rivermere name; no new harbor jurisdiction | Type1 |
| `eastrun-gaol` | Eastrun District Gaol | Eastrun | Type2 |
| `briarfall-gaol` | Briarfall District Gaol | Briarfall Crossing | Type2 |
| `blackthorn-gaol` | Blackthorn Regional Gaol | Blackthorn Watch context; no inferred regional boundary | Type3 |
| `crown-remand` | Caelthorne Crown Remand House | Caelthorne | Type2 |
| `stonegate` | Stonegate Royal Prison | UNKNOWN; no geography supplied | Type3 |
| `warded-annex` | Warded Custody Annex | UNKNOWN; no geography supplied | Type4 |

All have unknown operating authority, responsible officer, capacity, security, medical access, court relationship and transfer arrangements. No current prisoner population is invented. Unknown capacity is not zero inmates or available space. No named official is assigned to a facility by list position.

The proposed taxonomy is in [justice-and-jurisdiction](../entities/rules/justice-and-jurisdiction.md): Type1 temporary watchhouse cells; Type2 district remand/short detention; Type3 authorized longer detention/serious sentences; Type4 specialist containment. Actual demonstrated abilities, lawful basis, proportional safeguards and medical needs must justify special containment. Magic use alone establishes neither danger nor guilt, and the word “warded” certifies no capability.

## Proposed officials and identity review

All16 names remain proposal records with no approved office, character ID, relationship, meeting, biography, powers or prison assignment. The collision references are spelling/role review aids only, not aliases or family connections.

| Candidate | Existing identity or responsibility to preserve |
|---|---|
| Chief Justice Aveline Hartwell | Existing magistrates; no new chief justice approved |
| Captain Idris Bellmont | No indexed match; no appointment |
| Captain Mara Ellwick | Distinct from Mara Vey and Mara Fenwick |
| Captain Darius Fenwick | Shared surname does not relate him to Mara Fenwick |
| Commander Rhea Stone | No replacement of established command; not Ressa Vale or Aldric Voss |
| Captain Yselle Hart | No indexed match; no appointment |
| Warden Harlan Reed | Distinct from miller Harlan Wicks |
| Warden Nessa Corwin | Corwin/Corven/Corvin similarities do not establish identity |
| Warden Garron Vale | Distinct from Garrick, Ressa, Serrik and Hessa Vale; no kinship inferred |
| Warden Elira Doss | No indexed match; no appointment |
| Marshal Teren Ashford | Not Theron Ashvale; no family or royal-authority inference |
| Magister Ivara Sen | Title establishes no demonstrated magical capabilities |
| Magistrate Elian Wren | Not equated with existing Elian Voss |
| Magistrate Sela Morcant | Sela is not automatically Sella |
| Judge Amara Holt | Shared surname does not identify her with Evara Holt |
| Justice Corvin Dales | Distinct from all existing Corvin/Corven records |

## Road-to-authority lookup

[justice-road-links](../entities/mechanics/justice-road-links.md) covers all18 existing roads. It owns only justice lookup links; route identity, canon/proposed status, modes and duration remain with each road owner. No road or settlement data is edited. All source patrol-jurisdiction values are currently UNKNOWN, so every route's responsible authority, region, nearest established station, court and remand destination remains null.

Endpoint contacts are sourced only where the endpoint has an established authority: Caelthorne, Brackenford, Blackthorn Watch and Ashvale Estate. A contact at a settlement does not establish that office patrols the connecting corridor, accepts prisoners, has spare cells or is the nearest station. Other endpoints retain unknown authority rather than acquiring a proposed constabulary. Proposed roads do not become patrol routes or functioning transfer links. No distance calculation, cross-border agreement, direct adjacency or automatic transport is inferred.

## Capture, review and handover procedure

Use the ten-step [custody destination procedure](../entities/rules/justice-and-jurisdiction.md): identify capture/place/case → resolve geography → check actual jurisdiction → distinguish authority type → verify receiving facility → verify officer → establish lawful transport and medical safeguards → record actual handover only after play → link evidence/property inventories → record later supported review/disposition.

Unknown facility, officer, court, acceptance, route, authority or legal basis must be reported explicitly. Present a bounded institutional proposal or establish the missing fact in gameplay; do not narrate it as a historical fact. No verified receiving facility is supplied by this implementation, so it cannot automatically select a prison for a new capture.

The workflow supports apprehended, awaiting transport, in transit, received at station, booked, awaiting judicial review, released, remanded, transferred, convicted, sentenced and final disposition. It is not a mandatory linear path or an automatic state machine. Allegations and confessions are not convictions. The proposed court process covers arrest, booking/medical assessment, evidence/warrant checks, review, bail/conditional release, remand, trial, verdict, sentence, appeal, restitution and release/transfer. These are design steps pending local-law approval, not new deadlines, fines or retrospective judgments.

A completed transfer needs a stable case/person reference, sending/receiving authority, lawful basis, departure source, arrival source, receiving officer, custody receipt, evidence inventory and personal-property inventory. A single document may contain several proofs; file existence alone does not prove its contents, legal competence, chronological continuity or that the event occurred. Human source review remains necessary. Planned transfer has no departure/arrival/receipt; transit has no arrival/receipt. A future actual transfer can use only independently verified operational facilities and authorities; proposal approval alone is not an old handover.

Historical incomplete records are preserved as incomplete and are not forced into new template fields. Original guard camps or historic aggregate reviews cannot be mapped to proposed prisons or newly named officials. Restitution may coexist with pending legal review; it does not automatically resolve civil, criminal or military proceedings.

## Custody freshness and evidence routing

The existing custody owner now contains source pointers for early handover verification gaps, older groups, later review sources and non-detention references. It adds no case outcomes, new transfers or evidence entries. Later explicit sources supersede only overlapping facts, preserving separation of older groups, aggregates, individual cases and non-prisoners. No secret identities or case-status dump is added to this public directory.

Targeted historical checks found a later Rusk/mill check reference, not an original handover receipt. The custody-money aggregate and Third Bell object do not identify a modern prisoner group. Missing original handover identity/location/receipt details remain UNKNOWN; this does not claim those events never happened. See the custody source pointers and verification queue rather than fabricate a bridge.

Evidence and property stay with their established owners: existing item/batch records, Seven Bells evidence inventory, Shady Salvage, Launder and party-finance boundaries. Workflow fields record item/exhibit ID, original owner if known, seizing person/date, custodian, storage, transfer history, restrictions and disposition. Unknown original ownership is not a grant to Theron. No protected original, seized money, merchant cargo or salvage is moved, sold, duplicated or confiscated by this implementation.

## Validation, visibility and remaining gaps

Main validation checks scoped IDs, entity/source references, classifications, proposal approval gaps, authority separation, all18 road links, unchanged event slots and prospective transfer completeness. Tests preserve state, finances, original custody text, existing people, evidence owners, quest outcomes and road classifications. Unknown fields remain valid. Human review must still assess legal/source truth and player knowledge.

Remaining gaps: Valedorn's identity/territory, precise jurisdiction boundaries, road patrol coverage, named operational stations/courts/prisons, receiving officers, capacity/security/medical access, cross-border authority, old handover receipts and current placements not explicitly supplied by source. No new nation, political control, prison placement or legal outcome is created to close these gaps.

Repository visibility remains public despite private-governance guidance; no setting is changed. This directory exposes ordinary offices, procedures and explicitly unapproved proposals, not concealed motives, hidden answers or secret case identities. A `gm-reference` source link is not proof Theron knows every fact in that file. Fetch only the relevant case/evidence source after a knowledge check, not the whole archive. Follow narration-format.md for attributed dialogue and independently closed disclosures. Do not begin Chunk5 or merge without explicit player approval.
