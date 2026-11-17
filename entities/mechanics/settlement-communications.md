---
id: settlement-communications
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-02-settlement-approval.md
- entities/rules/npc-autonomy-and-time.md
- entities/mechanics/travel-routes.md
- entities/items/guardian-links.md
- entities/items/first-hours-accord.md
- entities/mechanics/theron-spells.md
---

# Medieval communications and postal design

Design procedures supplement, rather than replace, npc-autonomy-and-time and existing magical item/spell owners. No messages are sent by this framework. Every actual message must identify sender, recipient, actual carrier, departure date/time, intended route, fee or explicit unknown quotation, reasoned delivery window, independent status and source-backed evidence. Unknown routes do not authorize a dispatch. No instantaneous delivery or inferred acknowledgment.

Before sending, verify origin/destination and route topology, method compatibility, current conditions/season, rest/feed/supplies, willingness, custody and legal access. Record the delivery fee once only through the existing finance authority after an actual sourced payment; a price reference is no payment. Store an unknown estimate as null with a reason, never zero travel time. A send event does not establish arrival. Delivery needs a distinct dated receipt/source; delay, loss, refusal and interruption remain possible. No automatic resending, reply, delegation acceptance or NPC recall. For actual events use the relevant owner and chronicle, not a second editable message ledger here. Beacon signals require surveyed facilities and a shared finite vocabulary; none is installed. Magic follows existing costs/limits and cannot fill mundane route gaps.

```json
{
  "schema_version": 1,
  "classification": "APPROVED DESIGN",
  "autonomy_owner_ref": "npc-autonomy-and-time",
  "road_owner_ref": "travel-routes",
  "finance_owner_ref": "party-finances",
  "methods": [
    {
      "id": "mounted-courier",
      "carrier": "Paid rider and horse",
      "requirements": "A compatible riding route, daylight/rest, horse water/feed, sealed packet and willing carrier; no universal riding speed."
    },
    {
      "id": "guild-messenger",
      "carrier": "Willing authorized guild messenger",
      "requirements": "Verified guild relationship and actual carrier; rank grants neither access nor instant delivery."
    },
    {
      "id": "caravan-post",
      "carrier": "Consenting caravan carrier",
      "requirements": "Actual caravan departure, packet custody and compatible wagon/pack route; no fixed daily timetable."
    },
    {
      "id": "river-dispatch",
      "carrier": "Consenting boat crew",
      "requirements": "Surveyed navigable reach, landing permissions, water level, daylight/rest and finite boat capacity; no current river route certified."
    },
    {
      "id": "beacon-signal",
      "carrier": "Willing trained signal keepers",
      "requirements": "Verified staffed towers, line of sight, fuel, weather and a shared predefined code. Only agreed codes such as request aid or hazard warning; no arbitrary letter text or invented tower chain."
    },
    {
      "id": "limited-magic",
      "carrier": "Willing user of an existing verified magical channel",
      "requirements": "Retrieve guardian-links/first-hours-accord/theron-spells as applicable; prove established function, range, recipient, consent, concentration and finite costs. No new spell, unlimited network or automatic reply."
    }
  ],
  "message_template": {
    "id": null,
    "sender": null,
    "recipient": null,
    "carrier": null,
    "method": null,
    "departure_date": null,
    "departure_time": null,
    "origin": null,
    "destination": null,
    "intended_route_ids": [],
    "delivery_fee_cp": null,
    "estimated_delivery_window": {
      "earliest": null,
      "latest": null,
      "basis": null
    },
    "actual_delivery_status": "proposed",
    "receipt_evidence": [],
    "dispatch_evidence": [],
    "spell_rule_ref": null,
    "resource_evidence": [],
    "source_ref": null
  },
  "messages": [],
  "automatic_delivery": false,
  "automatic_resource_postings": false
}
```
