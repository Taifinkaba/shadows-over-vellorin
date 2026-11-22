# Campaign calendar — 365-day annual rollover

Player-approved rule: **365 days in each year**, valid annual day numbers 1–365. Normalize a positive annual day D by advancing `floor((D-1)/365)` years and using `((D-1) % 365) + 1` as the annual day. The next day after Day 365 is the following year's Day 1.

For Year 848 historical Suncrest records only, the repository explicitly documents **annual Day = Suncrest day + 120**. This does **not** establish the calendar's complete season boundaries. Avoid output like `Suncrest 1135`, do not assign a new season name without evidence, and show `Year Y, Day N` when normalized.

Preserve literal historical dates in archived chronicles and past checkpoint source evidence. Their derived normalized annotations do not rewrite past events or certify intervening travel or time passage. Conflicting legacy dates must be reconciled separately.

Mental or simulated time does not advance outside time. Repository maintenance does not advance campaign time.

The prior *chat-played* label Year 848, Suncrest 1135 gives annual day 1255 => **Year 851, Day 160, 7:00 PM** (Theron's Estate), subject to the documented +120 offset and unverified full seasonal calendar. This is a display correction for in-progress play, NOT an END SESSION adoption. Retain the existing repository checkpoint until the user's END SESSION handoff is integrated.

See [reconciliation](../../changes/chronicles/calendar-365-day-reconciliation.md) and [active-play calendar note](../../state/active-play-calendar-note.md).
