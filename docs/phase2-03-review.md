# Phase 2 PR 3 — governments, law and criminal justice review

PR number and URL: PR_LINK_PENDING (filled with GitHub’s assigned number immediately after opening).

Base: `e61dfa4556d2bff31065a31376339d4b6e95e701`, latest main with merged PR #24 and #25. Branch: `lore/phase2-03-governments`. Scope: PR 3 only; no merge or PR 4 implementation.

## Five-realm government inventory

| Realm owner | Approved form | Scoped office models | Scope |
|---|---|---:|---|
| valedorn | Hereditary monarchy |14| Crown/household, royal council, landholders/lords, municipalities, treasury, watch, local/regional/realm courts, custody, diplomacy and military. Caelthorne remains capital. |
| elyndor | Circle of Rootwardens |10| Circle/community councils, grove and land/botanical stewardship, safety, local/regional/realm hearings/custody and envoys. |
| ironhollow-holds | Clan confederation |10| Assemblies/speakers, delegated confederation, work/mining safety, investigation, local/clan/regional/realm review/custody and trade envoys. |
| rivermere-league | Merchant federation |10| Chartered towns/councils, limited federation, port/customs, warehouse inspection, patrol roles, local/commercial/criminal/appeal courts, custody and envoys. |
| frostmarch | Chiefs and seasonal assemblies |9| Chiefs/councils, seasonal assembly, grazing/hunting stewardship, frontier safety, local/interclan/realm review/custody and defense/caravan envoys. |

The 53 office models are scoped design IDs inside existing realm owners, not newly operational factions, offices, buildings or appointees. Each realm defines leadership selection/succession, title/property/inheritance, taxation/contribution authority without rates, industrial/labor duties, independent legal traditions, defense/emergency limits, proposed diplomacy and corruption safeguards. Twenty finite political-interest contexts represent households, councils, workers, merchants, stewards and reform petitioners without active movements or events. There is no current treasury, named heir, treaty, order, war or appointment.

[Government, character, facility and business-law inventory](phase2-government-and-law.md) provides the human-readable crosswalk. Government facts belong to each realm’s government_design; geography and settlement owners retain their old domains. The three existing justice owners receive bounded extensions rather than competing registries.

## New and reused IDs

Five new indexed character design IDs: `elowen-marcrest` (47), `cassian-thornmere` (39), `durnek-stonevein` (132), `selene-harrow` (34), `aveline-hartwell` (54). Total indexed entities: 223. No new facility location, government faction, criminal faction, quest, item or custody entity is created.

Aveline reuses `proposal:officer-aveline-hartwell`, promoting that same proposed person into a character design. The original Chief Justice candidate office remains unapproved, with no actual appointment. Her one existing proposal pointer and identity-review wording are the only legacy proposal-field changes. All other officer proposals and all existing character files remain unchanged.

Reused realm entities: `valedorn`, `elyndor`, `ironhollow-holds`, `rivermere-league`, `frostmarch`. Existing `justice-authorities`, `justice-proposals` and `justice-and-jurisdiction` retain their original ownership. `prisoner-custody`, finance, evidence, geography and all ten settlement/business owners remain unchanged.

Character biographies provide approved background, appearance, personality, public-reputation design, motivations, loyalties, potential relationships/conflicts and duties/limits. Titles are not actual appointments; no prior meeting with Theron, historical decision, current location, secret fact or completed action is supplied. Broader autonomy remains PR 7.

## Court and prison facility inventory

| Existing scoped proposal ID | Facility | Existing candidate location | Design role |
|---|---|---|---|
| proposal:building-crown-hall | Crown Hall of Justice | Caelthorne | Court/appeal hearings and records; no detention use certified. |
| proposal:building-central-watchhouse | Caelthorne Central Watchhouse | Caelthorne | Initial lawful booking/brief holding pending review. |
| proposal:building-eastrun-gaol | Eastrun District Gaol | Eastrun | District judicial remand/short custody. |
| proposal:building-briarfall-gaol | Briarfall District Gaol | Briarfall Crossing | District judicial remand with verified transport/access. |
| proposal:building-blackthorn-gaol | Blackthorn Regional Gaol | Blackthorn Watch context only | Regional serious-case remand/lawful sentence; not identity with Watch or North Waystation. |
| proposal:building-stonegate | Stonegate Royal Prison | UNKNOWN | Serious lawful sentences after independent process. |
| proposal:building-warded-annex | Warded Custody Annex | UNKNOWN | Individually justified specialist custody; no ward capability established. |

All seven reuse their original IDs, candidate placements and historical proposal fields. Their bounded approved_facility_designs extension supplies conditional governing/court models, intended purpose/classification, staffing roles, security, intake/release, custody documents, medical/basic conditions, transport, oversight, emergency continuity and finite capacity requirements. Actual authority, responsible officer, staff, exact capacity, current prisoners and operations remain unknown. Empty new-event lists are not zero historical inmates.

Authority/court links are Valedorn-style design models, not actual local mandates. Caelthorne’s realm membership is approved; Eastrun/Briarfall/Blackthorn placement does not establish Valedorn jurisdiction, and Stonegate/Annex remain unlocated. Other five building proposals remain unapproved. No verified receiving facility is added; the original actual-transfer validator still rejects these design-only facilities.

## Jurisdiction, criminal code and business law

Local hearing roles handle minor claims/preliminary review, regional courts serious proceedings, and realm panels appeals within their own verified authority. No single court governs all five realms. Current jurisdiction depends on actual territory, local mandate and subject matter; proposed routes, endpoint contacts and broad realm designs do not expand it. Brackenford retains its council, Elsbeth Marrin, Ressa Vale and six part-time members without a new superior, tax or arrest.

Twenty-one offense categories cover all requested theft/burglary, violence/murder, fraud/forgery, corruption, smuggling/extortion, unlawful detention/kidnapping/trafficking, damage, unlawful experimentation/dangerous magic, mining/timber, contracts/cargo, proved organized crime and obstruction. Each supplies conduct/severity, evidentiary distinctions, five realm-specific investigation/local/regional/appeal references and bounded sanctions/appeals. Guild rank, noble title, private property, fame and nonlethal capture preferences confer no unlimited police authority. Military review, private restitution, civil disputes and criminal judgments remain separate.

Twelve business-law areas cover inns/taverns, gambling, adult entertainment, pawnshops, markets, couriers, warehouses, mercenaries, magical shops, healing, extraction and prohibited exploitation. All 41 PR 2 scoped business designs have routing links to applicable design rules without modifying their actual facts, classifications or unknown licenses. LAWFUL, REGULATED, TOLERATED and PROHIBITED remain jurisdiction-sensitive design policies; a venue receives no actual license or immunity.

Adult entertainment is non-explicit and requires consenting independent adult workers controlling earnings, documents and boundaries, able to refuse and leave. Coercion, confinement, trafficking, debt bondage and violence are prohibited exploitation. No existing youth staff is assigned, new worker hired or operating business created.

## Process, custody and corruption safeguards

The process separates allegation, inquiry, bounded warrant/urgency, actual arrest, care/booking, independent review, lawful release/remand, hearing, reasoned verdict, separate sentence, appeal/correction and supported disposition. Reliable corroboration and meaningful challenge matter; intimidation, coerced confession and mental magic are not automatic guilt. No automatic grave punishment, torture, collective punishment, forced labor, confiscation, fine, exile or execution is authorized. Exact local tariffs, penalty limits and charters remain unknown and require verification before actual sanctions.

An empty arrest/transfer template records authority, legal basis, subject, date/time/location, officers, evidence/property inventories, receiving authority/facility, medical condition, transport, departure/arrival/receipt, review and disposition. Actual future records remain in the existing custody owner and original sources, not this template. No historical incomplete receipt is filled, prisoner moved, evidence copied, case reopened or judgment changed.

Eight criminal labels appear only as legal-response contexts; no PR 4 organizations, active crimes/investigations, secret leaders, hideouts or mystery connections are created. Oversight includes authentic warrants/documents, exculpatory evidence, financial provenance, bounded cooperation without automatic extradition, witness/informant consent/safety/reliability, conflict recusal, independent misconduct review, safe reporting, appeals and wrongful-conviction redress through an actual lawful decision. No person is declared corrupt or guilty by affiliation.

## Preservation evidence

The new manifest pins 298 unrelated campaign files and records before/after hashes for eight authorized existing owners: five realm profiles and the three justice owners. It compares original legal JSON payloads with only the approved extension removed, testing Aveline’s explicit identity delta separately. Old preservation fixtures update only these current-owner digests and retain original before-digests/prior approved after-digests.

All state, prior characters, creatures, companions, equipment, spells, quests, custody/evidence owners, archives, preexisting historical chronicles, twenty road files, geographic hierarchy and all PR 2 settlement/business/trade/communication/price data remain byte-for-byte unchanged. House Ashvale’s Briarstone Cottage title, 55 gp noncash value and completed 26 gp repair history remain unchanged; no tenants, rent, repairs or title transfer. Lodge 22% eligible commission and schema 4 ledger remain authoritative.

Checkpoint remains Year 848 Suncrest 61 Day 181, 19:30, Ashvale Estate; HP 100/100, MP 400/400, S+/Level 5, normal DEF 49/conditional 51 only if Night Sovereign is worn (wearing unknown), Nexus 156/180 and wagon 60/60. Controlled 745 gp 9 sp, unpaid expansion 317 gp and uncommitted 428 gp 9 sp are unchanged. Accounts, current companion positions and undocumented events remain unknown; locked abilities stay locked. No taxes, fines, fees, wages, confiscations, restitution or revenue are posted.

## Unknowns and conflicts

Most realm boundaries, settlement jurisdiction and operational appointments remain unsurveyed/unverified. Current rulers/officers in exercised offices, heirs, staff, budgets, signed agreements, active patrols, receiving facilities, capacity/security capability, warrants, sentencing scales and current legal outcomes are not inferred. Aveline’s proposed Chief Justice title is deliberately distinct from her approved character design. The archival authority/proposal baseline and approved extensions have different classifications; field-level retrieval is required. No new conflict blocks design review, while these gaps block unsupported enforcement or transfers.

## Privacy and spoiler assessment

The repository was verified public before editing and visibility is unchanged. Added material is safe ordinary political/legal design. No confidential witness/informant identity, location/contact, private intelligence, hidden mystery answer, undiscovered conspiracy link or GM outcome is stored. gm-reference is not access control, and a source link is not player discovery. This scoped PR does not certify existing public contents spoiler-safe or claim a private storage service.

## Validation results and readiness

Clean base, identical source tree to merged main: normal/optimized validators pass; 832 tests pass in 186.142s. No preexisting failures found.

Implementation: normal and optimized validators pass (223 entities); all 872 tests pass in 198.231s, including 40 new regression tests. The legacy 52-test justice suite also passes. Checks protect five governments/ages, no appointments, jurisdiction/court references, all seven facility identities, unknown occupants/capacity, operational transfer blocking, business legal status/adult agency, complete empty intake fields, no investigations/secrets/outcomes, and historical/financial immutability. No introduced failures remain.

Economy reporting, dashboard generation/freshness verification and quest readiness pass. Controlled 74590 cp, unpaid 31700 cp and uncommitted 42890 cp remain unchanged. Existing ending-design blockers remain 18 pending answer approvals and 14 unfilled routes; no ending-readiness claim is made. Normal and staged diff checks pass.

Ready for player review. No gameplay occurred: no time, appointments, political actions, crime resolution, custody, resources, money, companions, quests or visibility changed. Open one PR, do not merge, do not begin PR 4, then stop for review.

## Files added (11)

- `changes/chronicles/phase2-03-government-approval.md`
- `docs/phase2-03-review.md`
- `docs/phase2-government-and-law.md`
- `entities/characters/aveline-hartwell.md`
- `entities/characters/cassian-thornmere.md`
- `entities/characters/durnek-stonevein.md`
- `entities/characters/elowen-marcrest.md`
- `entities/characters/selene-harrow.md`
- `scripts/governments.py`
- `tests/fixtures/phase2-03-preservation.json`
- `tests/test_phase2_governments.py`

## Files modified (25)

- `README.md`
- `changes/CHANGELOG.md`
- `docs/faction-activity-directory.md`
- `docs/justice-and-custody-directory.md`
- `docs/validation.md`
- `entities/locations/elyndor.md`
- `entities/locations/frostmarch.md`
- `entities/locations/ironhollow-holds.md`
- `entities/locations/rivermere-league.md`
- `entities/locations/valedorn.md`
- `entities/mechanics/justice-authorities.md`
- `entities/mechanics/justice-proposals.md`
- `entities/rules/justice-and-jurisdiction.md`
- `index.json`
- `scripts/justice.py`
- `scripts/validate.py`
- `tests/fixtures/chunk10-preservation.json`
- `tests/fixtures/chunk6-preservation.json`
- `tests/fixtures/chunk7-preservation.json`
- `tests/fixtures/chunk8-preservation.json`
- `tests/fixtures/chunk9-preservation.json`
- `tests/fixtures/day181-final-reconciliation.json`
- `tests/fixtures/day181-migration.json`
- `tests/fixtures/phase2-01-preservation.json`
- `tests/fixtures/phase2-02-preservation.json`
