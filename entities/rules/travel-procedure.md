---
id: travel-procedure
type: rules
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/world-geography-travel-design.md
- archive/legacy-modules/codex/04-system-4-geography-travel-atlas.md
- entities/mechanics/theron-spells.md
- entities/rules/story-mode.md
---

# Travel planning and narration procedure

Maintenance procedure; no active journey or automatic spending. It preserves the archived travel procedure and established magic limits. New numeric speed, ration, toll and fatigue formulas are deliberately not enacted.

1. Read the current checkpoint for Theron’s location/time, then relevant companions/vehicles independently. Lookup `travel-routes` and `world-geography`; follow the IDs through index.json. Location presence never recalls an NPC or transfers custody.
2. Select origin, destination, intermediate stops and mode with the player. Exclude PROPOSED routes/containment from canonical navigation until approved. Null fields mean UNKNOWN. If no confirmed connection exists, report the gap and present the stored proposal for approval; do not improvise an alleged historical road. Reverse travel requires checking direction restrictions; proposed reverse estimates are not verified history.
3. Walking uses only the walking baseline; riding requires mount suitability, load, water and rest; horse wagons require width/surface/passability and care of each horse. A caravan must account for the slowest wagon and coordination stops; do not assume that riding halves wagon time or that every walkable lane takes a wagon. An unspecified-mode report cannot supply mode-specific speed.
4. Before departure state baseline duration/range, source, mode and uncertainty. Separate movement time from rest, camp, loading, ferry waits and interruptions; if a source reports days, preserve days unless its daily schedule is known. Check terrain, surface, load, daylight, weather, seasonal access, patrol boundaries and tolls. No invented precise mileage or favorable current weather. If numeric effects are absent, declare a proposed forward estimate and its assumptions before player choice; do not rewrite old duration evidence.
5. Difficult ground, gradients, mud/snow, darkness, fatigue or injury can change access and duration. Night travel needs light, navigation and watch/rest tradeoffs. Do not grant nonstop travel or automatic safety. State any proposed delay or alternative before committing to it; no mandatory random encounter result is pre-generated as an event.
6. Plan rest at a source-backed accessible inn/camp/refuge. Location services are not a vacancy guarantee; ask about capacity, price, permission and opening status in play. Supplies need party/animal counts, trip duration, available stock, water and consumption. Existing inventory and currency remain unchanged until actual authorized play. No automatic purchases, consumption, payroll, income or toll deduction. Unknown prices/quantities remain UNKNOWN; verify with finance/property owners.
7. Patrols use established jurisdiction, finite personnel and evidence-based notices. An endpoint watch is not proof it patrols the entire corridor. Link courts/prisons as future service records; do not invent officers, immunity, transfers or verdicts. Encounters need causal context, fair warning and player agency; proposals are not completed outcomes.
8. If blocked, stop at the last established position. Report the cause only if known; offer waiting, returning or an already documented alternate. A proposed bypass needs approval and its own persistent record before use. Never teleport around a closure or infer a connecting leg by subtracting Caelthorne estimates.
9. Magical movement uses the existing spell record, confirmed scope/range, current cost, concentration, anchor/target/access requirements and available finite mana. Unknown requirements or unverified repricing need clarification before casting. No new teleport links, anchor network, unlimited range or free restoration. No canonical route is implied by spatial magic.
10. During authorized play log departure, route ID/direction, conditions, party/animal positions, supply/MP costs, rests, interruptions and arrival with source. Update the existing checkpoint/owner records, chronicle and handoff together under normal governance; never create a second current-state file. END SESSION stops play and follows narration-format.md.

## GM narration lookup

- **Where is Theron?** Current checkpoint; later supplied snapshots are not silently adopted.
- **Which road?** Active journey source if any; otherwise he is not traveling. Route ID/title is not necessarily a formal road name.
- **Closest settlement?** A sourced position/landmark along the active route is required. No coordinates or intermediate chain means UNKNOWN, not whichever endpoint seems plausible.
- **Jurisdiction?** Route field, then linked local authority record; UNKNOWN if only endpoint authority is known.
- **How long?** Compatible-mode sourced baseline plus declared conditions/rest/delays. Proposed estimates remain marked PROPOSED.
- **What lies along it?** Recorded intermediates and integration-point placement; endpoint services are not automatically wayside services.
- **Where to rest?** Existing accessible service/permission/capacity, not an invented inn.
- **Blocked road?** Preserve position, offer documented alternatives and player decisions; record any approved prospective bypass.

Attribute dialogue and use independently closed functioning disclosures for long itinerary/supply tables per docs/narration-format.md. Do not expose GM-only locations or hidden dungeon entrances merely because index retrieval found them.
