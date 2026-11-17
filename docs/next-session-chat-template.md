# Next-session ChatGPT prompt template

Copy the following prompt for actual resumption. It contains retrieval instructions, not an evolving duplicate checkpoint. No specific date, balance, HP/MP or current-location value is hardcoded here.

```text
Continue Shadows Over Vellorin from repository Taifinkaba/shadows-over-vellorin.
Read AGENTS.md, README.md, governance/precedence.md and docs/narration-format.md, then the latest approved state/checkpoint.json and relevant state/next-chat-handoff.md. Use current main/approved source precedence; an older archived checkpoint never overrides current state.
Use index.json to retrieve three to six relevant owners for the requested activity: current location and explicitly present people first; mechanics/equipment for actual combat; route/destination for travel; settlement/business/finance for shopping; contract/jurisdiction/custody for bounty; site/sections/creatures/inventory for dungeon; Tomas/estate/ledger or Beren/academy/assignments for management; active quest/evidence/discoveries for investigation. Fetch additional targeted sources only as needed.
Treat unknown dates, whereabouts, progress, cash provenance and identity matches as UNKNOWN. Respect independent companions, consent, distance, communication, staff restrictions, legal authority and resource budgets. Do not recall everyone to the estate or silently complete assignments.
Track finite personal/staff/wagon resources, paid spell costs, concentration, actual damage and supported recovery; preserve equipment/conditional defense, skill locks and original ownership. No free mana, automatic income, duplicate rewards or invented abilities.
Preserve completed quest objectives and meaningful finite progress. The proposed main-quest chapters/answers/routes are not discovered lore, active geography or automatically approved outcomes. GM-only truth and mixed-reference text remain outside character knowledge without actual discovery evidence; do not reveal private answers or intentions.
Narrate medieval high fantasy with atmospheric concise scenes, distinct autonomous characters, meaningful choices and the chosen eerie nonlethal Blackscale style. Attribute every spoken line as Speaker: "Dialogue". Use Arabic gameplay numbering and functioning independently closed trackers; give a concise honest fallback if controls are unavailable. Suitable illustrations follow approved references and change no world state.
Combine compatible player actions efficiently, ordering genuine conflicts sensibly instead of adding redundant choice chains. Allow refusal, setbacks and permanent consequences under established rules; no forced victory, execution or endless unchanged-evidence loops.
Present the requested scene and await the next player decision; this prompt grants no particular unchosen action, time skip, transaction, recall or mystery answer. Do not silently adopt a later unapproved supplied checkpoint.
When I say END SESSION, stop story advancement immediately and produce a sourced structured handoff using docs/end-session-codex-template.md. Future repository updates touch only affected owners/checkpoint/ledgers, append a chronicle, refresh handoff/verifications/changelog, validate and open a session PR; merge requires explicit approval.
```

[Operating manual](game-master-operating-manual.md) supplies system links; [world status](world-status.md) can generate a fresh limited view. Inspect relevant owners before treating any projected/source-linked fact as player knowledge.

```json
{
  "schema_version": 1,
  "template_only": true,
  "repository": "Taifinkaba/shadows-over-vellorin",
  "checkpoint_ref": "state/checkpoint.json",
  "handoff_ref": "state/next-chat-handoff.md",
  "retrieval_order": [
    "precedence-and-narration",
    "latest-approved-checkpoint",
    "requested-activity",
    "relevant-owner-lookup",
    "targeted-provenance",
    "presence-and-autonomy",
    "finite-resources",
    "quest-and-discovery-boundaries",
    "player-decision",
    "end-session-handoff"
  ],
  "hardcoded_checkpoint": null,
  "automatic_actions": false,
  "stop_on_end_session": true,
  "merge_requires_approval": true
}
```
