# Player-approved calendar correction — 365-day years

This is a rules-and-display reconciliation, **not an END SESSION** and not a gameplay event. User approved the 365-day year and requested the correction in the repository. It does not advance time, spend money, award skills, or replace older checkpoint evidence.

## Rule

- One campaign year has **365 days**, numbered **1–365**.
- On the day after Year Y, Day 365, advance to Year Y+1, Day 1. No Year Y, Day 366 or larger is valid as a normalized annual date.
- When a legacy annual day counter exceeds 365, normalize by subtracting 365 repeatedly and advancing the year equivalently. In general, for positive day D: rolloverYears = floor((D-1)/365); normalizedYear = Y + rolloverYears; normalizedDay = ((D-1) mod 365)+1.
- The repository's historic **Year 848 Suncrest-to-annual offset of 120 days** is documented, but complete season boundaries and rollover naming are **not established**. Do not carry Suncrest labels beyond their documented seasonal range; show Year and annual Day until the seasonal calendar is authorized.
- Mental simulations, imaginary training years, maintenance work and research planning do not advance external campaign time.
- Keep original dates literally in historical chronicle sources. Display normalized date as an *annotation*, not a silent rewrite of the source. Where old dates conflict across records, queue review rather than inventing missing time advances.

## Examples (arithmetic conversion only; not claims of new play)

- Year 848, Suncrest 61 = historic annual Day 181 = normalized **Year 848, Day 181**.
- Year 848, Suncrest 76 = historic annual Day 196 = normalized **Year 848, Day 196**.
- Year 848, Suncrest 262 = historic annual Day 382 = normalized **Year 849, Day 17**.
- Year 847, annual Day 472 = normalized **Year 848, Day 107**, preserving the older document's literal timestamp.
- Most recent *chat-played* label: Year 848, Suncrest 1135. Under the historical +120 offset this is annual Day 1255, normalized **Year 851, Day 160, 7:00 PM**, at Theron's Estate/Ashvale Grand Arena. This is a provisional in-progress chat-play timeline, **not** the currently committed END SESSION checkpoint. No season name is verified for Day 160.

## Continuity boundaries

- The existing `state/checkpoint.json` remains the latest *repository-recorded completed session* at Year 848, Suncrest 262 (historic annual Day 382). Its historical literal date, resource values, and location are not silently replaced by the later chat-played material.
- The later chat-played estate/audience/economy and dragon arcs have not yet undergone normal END SESSION reconciliation; do not make this calendar-only change a claim that their other state is validated in the repository.
- Retain owner-specific provenance and chronology precedence in `governance/precedence.md`.
- See `state/active-play-calendar-note.md` for the derived ongoing display date; it is not a second authoritative state ledger.
