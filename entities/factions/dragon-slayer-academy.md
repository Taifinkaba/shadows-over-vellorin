---
id: dragon-slayer-academy
type: factions
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/year853-day52.md
- changes/chronicles/year853-end-session.md
- changes/chronicles/year852-day365-end-session.md
- changes/chronicles/year852-day1-end-session.md
- changes/chronicles/year851-day160-end-session.md
- changes/chronicles/year848-suncrest262-end-session.md
- archive/session-handoffs/year847-day153-user-handoff.txt
- archive/session-handoffs/year847-day472-user-handoff.txt
- archive/session-handoffs/year848-day124-user-handoff.txt
---

## Year 848, Suncrest 262 update

The independent academy in Greyhaven Valley is co-founded by Theron and the free, independent Vaeltharion, and managed by Master Beren. The academy and the Wayfarers’ Guild are separate institutions. Guild cards and ranks are distinct from DSI enrollment, field assessment and professional certifications.

### Roster (13)

Six active guild registrants:

- [Elias Renn](../characters/elias-renn.md) — E Rank, Level 2, standard supervised contracts
- [Kaela](../characters/kaela.md) — E Rank, Level 2, standard supervised contracts
- [Gorren](../characters/gorren.md) — E Rank, Level 2, standard supervised contracts
- [Nessa](../characters/nessa.md) — E Rank, Level 2, standard supervised contracts
- [Talia Fen](../characters/talia-fen.md) — F Rank, Level 1, supervised low-risk assignments only
- [Rowan Hale](../characters/rowan-hale.md) — F Rank, Level 1, supervised low-risk assignments only

Seven without guild cards: [Mira Thorne](../characters/mira-thorne.md), [Dalen Reed](../characters/dalen-reed.md), [Sera Willow](../characters/sera-willow.md), [Tobin Marsh](../characters/tobin-marsh.md), [Elowen Briar](../characters/elowen-briar.md), [Perrin Oak](../characters/perrin-oak.md), [Faye Linden](../characters/faye-linden.md).

The four E-rank adventurers completed supervised field contracts and the independent academy assessment. Talia and Rowan passed entry assessments and still need supervised missions and progressive assessments.

### Funding and training

The [independent tithe ledger](../../state/dsi-finance-ledger.json) records the academy’s 10% share after contracted rewards are paid. Adventurers retain 90%. Tithes support food, clothing, housing, wages and instructors, equipment, repairs, maintenance, operations and reserves. Academy treasury and student savings are independent of lodge and party cash.

The four horse owners completed injury-free introductory mounted training on Suncrest 262 covering stopping, turning, group spacing, horse comfort, mounting/dismounting and basic travel formation. Elias rode steadily, Kaela adapted quickly, Gorren needs practice and Nessa noticed crowding affecting Willow. Vaeltharion observed independently and emphasized responsible care. Stable arrangements, feed and care, winter reserves, instruction and safe equipment replacement remain unfunded. Future receipts depend on completed and paid contracts.

## Earlier record

# Dragon Slayer Academy / Initiative

## Year 853 Day 52

19 students, 10 Guild-registered adventurers, six probationary recruits and five waitlisted applicants. Guild progress is unchanged. Six registered non-disciples earned income from four independent contracts. Current separate accounted cash is 1,225 GP, including 1,140 GP in remaining allocations and 85 GP unallocated. Across students, accounted recent earnings total 768 GP. Use the [academy ledger](../../state/dsi-finance-ledger.json) for individual proceeds and exclusions. Dormitory inspection found foundation preparation complete and framing underway. Only the 60 GP deposit was paid. Theron has not received the dormitory or Buried Lantern Hall reports.

Launched in Greyhaven Valley; pilot day school, Vaeltharion Dragon Master and Theron cofounder. Elias Renn adult participant; Mira Thorne minor day student with guardian Maera; Master Beren and Maera assist. Do not confuse Mira Thorne with lodge helper Mira15.

Latest reported independent treasury:34gp cash plus15gp refundable lease deposit (noncash held deposit, not spendable cash). No prior academy ledger exists in the pre-sync repo to refine the handoff’s earlier report; report date and later transactions unverified. Council support/future contracts not booked without verified payment. Excluded from party/lodge555gp. Academy name does not unlock Theron’s Dragon Slayer ability.

## Authoritative update — Year 847 Day 472, 16:10, session ENDED

Founding phase: farm expanded, six hens, grain cellar, repaired defenses, instructors and trainees. Vaeltharion independent and free, Theron cofounder; Theron has not chosen Dragon Slayer certification. Earlier34gp/15gp figures remain historical only; no verified later ledger and no academy funds added to controlled673gp9sp.

## Update — Year 848 Suncrest 4 Day 124, 01:45

Beren manages the independent academy; Vaeltharion remains free and an independent cofounder. DSI Guild preliminary assessment opportunity offered, not completed. Earlier cash/deposit remain historical; no income or remote result invented.

## Guild and contract references — Chunk 5

This structured section belongs to this existing organization. Original prose/frontmatter is unchanged and retains precedence by date. It is not a new guild ledger, branch building, assignment or current contract board. Unknowns are JSON null; paid history is not payable again.

```json
{
  "schema_version": 1,
  "profile": {
    "guild_id": "dragon-slayer-academy",
    "name": "Dragon Slayer Academy / Initiative",
    "organization_type": "independent academy, not a Concord division",
    "classification": "CONFIRMED CANON",
    "headquarters_location_id": null,
    "branches": [
      {
        "id": "dragon-slayer-academy:greyhaven-site",
        "classification": "CONFIRMED CANON",
        "role": "independent-academy-site",
        "settlement_id": "greyhaven-valley",
        "building_location_id": null,
        "responsible_officer_id": null,
        "services": [
          "Established academy site; no new license or assessment result"
        ],
        "contract_board": null,
        "membership_registration": null,
        "supplies_facilities": null,
        "route_ids": [
          "route-eastrun-greyhaven-valley"
        ],
        "operational_status": "Established academy; current public availability UNKNOWN",
        "source_refs": [
          "entities/factions/dragon-slayer-academy.md"
        ],
        "source_quote": "Launched in Greyhaven Valley; pilot day school,"
      }
    ],
    "leadership": [
      {
        "role": "Managing independent academy",
        "source_quote": "Beren manages the independent academy;",
        "entity_id": "master-beren"
      },
      {
        "role": "Cofounder",
        "source_quote": "Theron cofounder.",
        "entity_id": "theron-ashvale"
      },
      {
        "role": "Dragon Master and independent cofounder",
        "source_quote": "Vaeltharion Dragon Master",
        "entity_id": "vaeltharion"
      }
    ],
    "membership_structure": null,
    "services": [
      "Established pilot day school/training; public fees/access UNKNOWN"
    ],
    "ranks": null,
    "licensing": null,
    "contract_types": [],
    "funding": null,
    "commission_policy": null,
    "jurisdiction": "No automatic police, judicial or extraterritorial powers",
    "other_guild_relationships": null,
    "last_verified_date": null,
    "source_refs": [
      "entities/factions/dragon-slayer-academy.md"
    ]
  },
  "contracts": [],
  "new_memberships": [],
  "license_changes": [],
  "new_contracts": [],
  "automatic_financial_postings": false
}
```

## First Grand Dragon Festival

Six of the 16 public competitors were Guild registrants from DSI. Students also demonstrated academy practice. Kaela won and received the 100 gp non-Guild prize directly, without a tithe or promotion. Tournament-safe gear leaves personal loadouts intact. Beren independently manages the 13-student academy. Its 10% post-payment Guild mission tithe and independent accounts remain in force.

## Year 851 Day 365 festival

All thirteen students were invited. Qualified students participated according to approval and availability. Only established individual results and equipment should be used. The champion’s prize was a tournament award outside the 10% post-payment Guild mission tithe. The event’s estate logistics expense remains separate from DSI finances.

## Year 852 close

Beren remains the independent operational leader. The established 13 students and six Guild registrations stand. Independent student earnings and tax policy remain separate from Theron’s funded expedition. Beren’s Watchpost safety procedures exclude students from the restricted area. [Watchpost](../locations/forgotten-watchpost.md) · [Session evidence](../../changes/chronicles/year852-day365-end-session.md#dsi-academy)

## Year 853 session

The independent academy is at [Greyhaven Valley](../locations/greyhaven-valley.md), separate from the commercial estate and Wayfarers’ Guild. Cofounders Theron and Vaeltharion retain their roles. Beren independently manages procurement, recruitment, staffing, training and spending. Record activities during play when Theron is absent. Visits require actual travel and do not establish the proposed Eastrun corridor.

Six of 16 applicants were admitted, five waitlisted, and five withdrew or were not accepted. Current roster follows. Guild rank, general level, academy membership and Dragon Slayer progression are distinct.

```dsi-roster
{
  "elias-renn": {
    "guild_rank": "E",
    "general_level": 2
  },
  "kaela": {
    "guild_rank": "E",
    "general_level": 2
  },
  "gorren": {
    "guild_rank": "E",
    "general_level": 2
  },
  "nessa": {
    "guild_rank": "E",
    "general_level": 2
  },
  "talia-fen": {
    "guild_rank": "E",
    "general_level": 2
  },
  "rowan-hale": {
    "guild_rank": "E",
    "general_level": 2
  },
  "dalen-reed": {
    "guild_rank": "F",
    "general_level": 1
  },
  "sera-willow": {
    "guild_rank": "F",
    "general_level": 1
  },
  "tobin-marsh": {
    "guild_rank": "F",
    "general_level": 1
  },
  "elowen-briar": {
    "guild_rank": "F",
    "general_level": 1
  },
  "mira-thorne": {
    "guild_rank": null,
    "general_level": null
  },
  "perrin-oak": {
    "guild_rank": null,
    "general_level": null
  },
  "faye-linden": {
    "guild_rank": null,
    "general_level": null
  },
  "cedric-vale": {
    "guild_rank": null,
    "general_level": null
  },
  "lethara-mossveil": {
    "guild_rank": null,
    "general_level": null
  },
  "brom-ironroot": {
    "guild_rank": null,
    "general_level": null
  },
  "marielle-fenwick": {
    "guild_rank": null,
    "general_level": null
  },
  "aren-duskwell": {
    "guild_rank": null,
    "general_level": null
  },
  "rhea-thornfield": {
    "guild_rank": null,
    "general_level": null
  }
}
```

The [independent ledger](../../state/dsi-finance-ledger.json) preserves past 10% tithes. Future paid Guild mission rewards after legitimate Guild deductions use 25%, with 75% retained by students. Gifts, tournament prizes, assets and Theron’s expedition proceeds are outside the policy. Savings remain personal. Beren manages the founder-funded development and reserve allocations. Contracts, disbursements, completions and new hires remain pending.

- Training equipment repaired.
- Group training reorganized.
- Stable care rotations established.
- Feed replenished.
- Farm planting expanded.
- Existing dormitory accommodation reorganized.
- Bedding replenished.

These are existing-facility improvements, not completed new buildings.

### Academy traditions

- Dragon's Journal: Personal adventure and training records.
- Returned Flame: Shared meal celebrating safe field-team returns.
- Senior mentorship: Experienced students instruct newer students.
- Empty Mask: Unissued dragon mask symbolizing future opportunities.
- Weekly strategy night.
- Commencement of the Dragon's Flame: Formal ceremony recognizing earned milestones.

[The Way of the Dragon](../mechanics/way-of-the-dragon.md) · [Mission history](../mechanics/dsi-independent-mission-history.md)
