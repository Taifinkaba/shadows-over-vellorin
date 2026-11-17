# Phase 2 — final design integration summary

Phase2's eight requested design layers are integrated for review. They are reference architecture, not gameplay activation. Numerical combat readiness, unresolved canon questions and the campaign ending are not complete. No time, resources, ownership, knowledge or outcomes change merely because a design exists.

## Eight PRs and authoritative owners

| Phase / PR | Completed reference layer | Authoritative retrieval |
|---|---|---|
| 1 / [#24](https://github.com/Taifinkaba/shadows-over-vellorin/pull/24) | Realm/region hierarchy, qualified route dependencies and travel procedure;20 existing route files remain individually owned. | world-geography, travel-routes, travel-procedure; original location/route owners; [review](phase2-01-review.md). |
| 2 / [#25](https://github.com/Taifinkaba/shadows-over-vellorin/pull/25) | Ten settlement designs,41 businesses,17 industry chains,12 proposed trade relationships, prospective prices/wages and communications. | Parent location approved_design; settlement-services, settlement-trade, service-price-references, settlement-communications; [review](phase2-02-review.md). |
| 3 / [#26](https://github.com/Taifinkaba/shadows-over-vellorin/pull/26) | Five government/legal designs, qualified institutions/facilities, jurisdiction-sensitive business/custody procedures and proposed officials. | Original realm owners; justice-authorities, justice-proposals, justice-and-jurisdiction; single prisoner-custody register; [review](phase2-03-review.md). |
| 4 / [#27](https://github.com/Taifinkaba/shadows-over-vellorin/pull/27) | Independent guild/underworld designs, voluntary Concord, professional references, contracts and finite illicit-commerce boundaries. | guild-network, guild-membership-and-contracts, continental-guild-concord, contract-registry, illicit-commerce-design and original faction owners; [review](phase2-04-review.md). |
| 5 / [#28](https://github.com/Taifinkaba/shadows-over-vellorin/pull/28) | Five dungeon design profiles with25 areas,30 conditional connections,25 proposed encounters,12 hazards and finite recovery. | dungeon-design-proposals; hollowstone-mine, ashen-anvil, drowned-archive, pale-reliquary, shattered-meridian; dungeon-ecology-and-hazards and dungeon-exploration; [review](phase2-05-review.md). |
| 6 / [#29](https://github.com/Taifinkaba/shadows-over-vellorin/pull/29) | Five accounting domains, finite operating cycles, scoped price/wage references, property/employment/logistics and supply/demand procedures. | Sole state/finance-ledger.json schema4; party-finances, economy-accounting, property-financial-references, payroll-construction-and-trade; actual facts stay with original owners; [review](phase2-06-review.md). |
| 7 / [#30](https://github.com/Taifinkaba/shadows-over-vellorin/pull/30) | Eight public NPC autonomy designs, independent schedule/event/knowledge/relationship procedures and test consolidation1000→184 cases. | Character owners; npc-autonomy-and-time, independent-assignments, faction-activity, world-event-references; [review and test audit](phase2-07-review.md). |
| 8 / [current PR review](phase2-08-review.md) | Eight-school classification,16 combat procedures,12 environment interactions, five descriptive monster enrichments and cross-system audit. | New magic-and-combat-integration routes existing spell/ability/skill/item authorities; original monster stats remain in dungeon-ecology-and-hazards. No second spellbook, bestiary identity or resource ledger. |

The current phase adds one procedure entity, taking246→247 indexed identities. Five existing monster-reference IDs remain scoped references, not five spawned creatures or new creature entities. All prior index entries and unrelated campaign facts are preserved.

## Single-authority integration

Resolve identity and current snapshot through index/checkpoint, then retrieve only relevant original owners. Magic-and-combat-integration classifies and routes; theron-spells owns listed spells/costs, theron-abilities and theron-skills own abilities/progression, item owners own equipment and finite reservoirs, and creature/character owners retain individual capabilities and consent. School membership is not a spell grant. No NPC, faction or monster may cast merely because its design mentions magic.

Travel still requires actual route, access, conditions, time and supported spatial preparation; settlements require willing providers and finite capacity. Law requires actual jurisdiction and due process, not titles or magical certainty. Guild status grants no new police power. Dungeon designs prove no entrance, population or loot. PR6 requires actual title, money, stock, labor, contracts, transport and payment evidence. PR7 requires supported time, capability, knowledge, intent and outcome evidence for independent activity.

Actual future play must declare supported costs/stakes, resolve independent choices and established mechanics, then record only actual outcomes once in original owners, dated chronicle/checkpoint and appropriate resource/inventory/finance authorities. Time passage, a goal, a proposed contract or a design approval produces nothing automatically. Theron's preference for nonlethal capture remains compatible with resistance, negotiation, surrender, retreat and fair permanent death.

## Completed references and remaining operational gaps

- All eight schools have principles, applications, resources, training, casting/failure/defense/legal limits, existing spell routing and explicit unknowns. Current sourced elemental spells establish cryomancy; other elemental families are not new learned powers. Temporal classification grants no unlocked Chronos Eye, foresight or time travel.
- Existing listed costs and full-cost exceptions are preserved. The later40% ordinary efficiency supersedes the earlier30% arrangement, but original bases and most40% repricing remain unverified; no second discount or new rounding rule is applied. Deep Mend17 and Greater Healing21 lack a current spell-owner entry and remain unverified references without a grant.
- Dreamfall remains21MP,60ft range,20ft radius, selectable1–30minutes, concentration and established resistance/waking conditions. Maternal healing costs36/32/48 and personal-only AssimilationII24MP per uninterrupted10minutes retain their governing sources and limits. No automatic healing, rest reset or reservoir recharge occurs.
- Initiative/action economy, universal movement, many attack/damage/status/resistance/HP-zero rules and unspecified spell ranges/anchor details remain unresolved. Existing d20+modifier versus declared DC resolution does not supply a universal attack-vs-DEF or damage formula.
- The five monster templates retain approved HP/MP/DEF/rank and now have bounded physical, movement, attack/defense, behavioral, ecological, retreat/noncombat and defeat/salvage descriptions. Missing numerical attack, damage, movement, resistance and magical-cost rules keep all five **not fully combat-ready**. No new power, active opponent, respawn or guaranteed loot is created.
- Shattered Meridian retains raw proposedSS in dungeon-threat scope with no compatible adventurer rank; it is not a new step in the F–S+ adventurer taxonomy. Theron remainsS+,Level5.
- Geography/approaches, current conditions, appointments/jurisdictions, tariffs, stock, resources, operational contracts, receipt/delivery and character knowledge remain source-qualified unknowns. Lodge22% eligible merchant commission is distinct from the confirmed10% applicable service adjustment, whose original bases/date remain UNKNOWN. No accounting allocation is inferred.

These are genuine unresolved requirements for actual use or a future ruling, not a reason to invent missing canon. No further phase or gameplay is authorized by this summary.

## Preservation, privacy and readiness

The Day18119:30 Ashvale Estate checkpoint remains unchanged: HP100/100, MP400/400, normal equippedDEF49;51 only if Night Sovereign is worn, current configuration UNKNOWN. Nexus156/180 and separate wagon60/60 remain finite and independent. Chronos Eye and Dragon Slayer remain locked. Controlled745gp9sp, unpaid317gp, uncommitted428gp9sp and unknown current subaccount allocations remain in sole ledger4. Property, cottage repair history, inventory, custody, companions, bonds, appointments, relationships and all historical events are unchanged.

Public integration adds safe classification and procedure only. Source-restricted equipment details, private motivations/outcomes, hidden identities and undiscovered answers are not republished. Existing source material mixes knowledge levels; public metadata is not proof of player knowledge or a repository-wide spoiler-clean certification. Visibility remains unchanged.

Ordinary discovery remains within the player's180–220 target; PR8 adds ten focused tests to the184-case baseline. Table-driven negative scenarios, original validators, representative integration and centralized preservation remain active. Counts measure discovered cases, not branch/line equivalence. See the current review for measured results.

**Story-ending readiness remains incomplete:18 pending answer approvals and14 unfilled clue routes.** Design integration is not mystery resolution, campaign completion, automatic activation or merge approval. Stop after PR8 for player review.
