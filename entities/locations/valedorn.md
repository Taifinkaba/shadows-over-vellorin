---
id: valedorn
type: locations
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-01-geography-approval.md
- changes/chronicles/phase2-03-government-approval.md
---

# Valedorn

APPROVED DESIGN — fictional world geography, not observed Day181 conditions or player knowledge.

## Political identity

Hereditary monarchy; Caelthorne is the capital. Existing magistrates and watch retain their recorded authority; no ruler appointment is made here.

## Terrain, climate and resources

Mixed temperate lowlands, cultivated river valleys and wooded uplands. Rain-fed farms, timber, clay and building stone support a varied rural hinterland. Rivers drain agricultural basins toward the wider river-trade network; channels and crossings are unsurveyed.

## Borders and frontier

Woodland margins, rising mountain approaches and northern frontier country are transition zones; no exact international boundary or adjacency to a particular realm is surveyed.

Containment belongs to `world-geography`. Weather, patrols, extraction rights, accessible supplies and occupancy remain UNKNOWN. No precise distances or coordinates are established.

## Approved government design — Phase 2 PR 3

This bounded institutional design does not certify current officeholders, powers exercised, current operations, appointments, orders or Theron’s knowledge. Detailed legal process belongs to justice-and-jurisdiction.

```json
{
  "schema_version": 1,
  "government_design": {
    "classification": "APPROVED DESIGN",
    "approval_source_ref": "changes/chronicles/phase2-03-government-approval.md",
    "realm_id": "valedorn",
    "form": "Hereditary monarchy",
    "capital_id": "caelthorne",
    "selection_and_succession": "Hereditary succession requires a recorded line, witnessed lawful claim and council/court review of disputed descent. A regency requires a lawful instrument and review; no heir, regent, coronation or disputed succession currently exists by this design.",
    "nobility_and_political_rights": "Marcrest royal-house and Thornmere noble-house designs supply political interests, not new relatives, land titles or actual appointments. Noble audiences, estate administration and hereditary claims require documented lawful privilege; nobility gives no exemption from evidence or criminal review. House Ashvale’s established property title is untouched.",
    "taxation_design": "Treasury may propose lawful assessed land/market/customs obligations through recognized instruments, published scope and appeal. Municipal obligations require local authority. No new rate, account, levy, arrears or collection is imposed.",
    "property_and_inheritance": "Recorded title, lawful inheritance and community easements govern use. Contested succession or restitution goes to a competent court; royal favor alone cannot transfer another owner’s property.",
    "industry_and_labor": "Mines, forests, dangerous trades and magical services require verified title/access, safety and applicable permissions; no resource monopoly, Crown ownership of dragons or new guild takeover.",
    "justice_hierarchy": "Local reeves/watch gather complaints; regional magistrates hear serious criminal/property matters; Crown appellate court reviews within Valedorn only. Existing magistrates remain in place; no superior is appointed over them by maintenance. Local hearing benches handle minor matters and preliminary review only within verified powers; serious cases proceed to competent regional courts and independent realm appeal.",
    "defense_and_emergency_limits": "Military orders require lawful command and finite troops/supplies. Civil arrests and prison sentences require distinct legal authority. Emergency orders remain reviewable; no mobilization is ordered.",
    "diplomacy": "Envoys may propose mutual recognition, safe conduct, trade and dispute mediation. Each realm remains independent; no signed treaty, war, current diplomatic mission, shared border or cross-realm court power is asserted.",
    "corruption_and_oversight": "Independent records, conflict disclosure/recusal, petition review, witnessed decisions and appeal constrain abuse. Whistleblowers may seek safe reporting; no person is declared corrupt or a current reform movement active.",
    "legal_owner_ref": "justice-and-jurisdiction",
    "design_figure_ids": [
      "elowen-marcrest",
      "cassian-thornmere"
    ],
    "offices": [
      {
        "id": "government:valedorn-crown",
        "name": "Crown",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-household",
        "name": "Royal household",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-council",
        "name": "Royal council",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-landholders",
        "name": "Noble houses and landholders",
        "level": "regional",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described regional role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-regional-lords",
        "name": "Regional governors or lords",
        "level": "regional",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described regional role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-municipal-councils",
        "name": "Municipal councils and reeves",
        "level": "local",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described local role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-treasury",
        "name": "Royal treasury and tax authority",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-watch",
        "name": "Local and royal watch functions",
        "level": "local",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described local role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-regional-courts",
        "name": "Regional magistrates and courts",
        "level": "regional",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described regional role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-high-court",
        "name": "Crown appellate court",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-custody-service",
        "name": "Court-supervised custody service",
        "level": "regional",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described regional role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-envoys",
        "name": "Diplomatic representatives",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-military",
        "name": "Royal and regional military command",
        "level": "realm",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Only the described realm role within verified jurisdiction; law, evidence, independent review, finite resources and existing offices constrain action.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      },
      {
        "id": "government:valedorn-local-courts",
        "name": "Local magistrates and lawful process officers",
        "level": "local",
        "classification": "APPROVED DESIGN",
        "scope_realm_id": "valedorn",
        "selection_or_mandate": "Requires the realm’s documented selection/delegation procedure and verified local powers; no appointment or charter is made.",
        "powers_and_limits": "Hear minor disputes and conduct preliminary review only within verified local authority. Refer serious offenses to competent regional criminal process; voluntary mediation never authorizes coerced settlement or detention.",
        "assigned_person_ids": [],
        "current_staffing": null,
        "operational_status": "UNKNOWN"
      }
    ],
    "political_interests": [
      {
        "label": "royal-household",
        "goals": "Continuity and legitimacy",
        "finite_resources": "Counsel, lawful revenue and willing staff; no budget or agents created",
        "classification": "APPROVED DESIGN",
        "active_events": []
      },
      {
        "label": "landholding-houses",
        "goals": "Inheritance and estate autonomy",
        "finite_resources": "Documented estates/rights only; no new lands or armed retainers",
        "classification": "APPROVED DESIGN",
        "active_events": []
      },
      {
        "label": "municipal-petitioners",
        "goals": "Fair tax assessment and local services",
        "finite_resources": "Voluntary petitions and finite local contributions",
        "classification": "APPROVED DESIGN",
        "active_events": []
      },
      {
        "label": "guild-and-merchant-lobby",
        "goals": "Predictable market rules and contracts",
        "finite_resources": "Lawful representation, not purchased warrants or immunity",
        "classification": "APPROVED DESIGN",
        "active_events": []
      }
    ],
    "actual_appointments": [],
    "actual_orders": [],
    "actual_political_events": [],
    "current_officeholders": null,
    "current_treaties": [],
    "current_treasury_cp": null
  }
}
```
