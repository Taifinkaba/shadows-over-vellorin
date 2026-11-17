---
id: settlement-services
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/settlements-businesses-services-design.md
- entities/locations/eastrun.md
- entities/locations/briarfall-crossing.md
- entities/locations/greyhaven-mill.md
- entities/locations/greyhaven-valley.md
- entities/locations/northern-freight-enclosure.md
- entities/locations/blackthorn-watch.md
- entities/locations/caelthorne.md
- entities/locations/brackenford.md
- entities/locations/ashvale-estate.md
- entities/locations/ashvale-lodge.md
- entities/locations/briarstone-cottage.md
- changes/chronicles/phase2-02-settlement-approval.md
---

# Settlement and service routing

Phase 2 adds `approved_design_location_ids` as a second retrieval scope in this same directory. The original eleven historical locality/property profiles and fourteen service records remain unchanged inside their legacy fields. Approved expansions live only in the parent location’s `approved_design` object; for Brackenford, scoped references enrich the five existing services rather than duplicate them. Business/service designs are not current stock, quotes, appointments or income. The following original baseline explanation applies to the legacy fields.

Routing and schema policy only. Profile/business facts belong to the existing parent location; no second town or business database. A parent-scoped ID uses `location-id:service-slug` and is not an index entity ID. Resolve its prefix in index.json, then that owner's structured section. Categories support later records but do not assert any unlisted shop, bank, magical inventory or supplier. All current business instances are source-backed; no proposed business instances are added. Profiles also cover watch/valley/freight sites and private properties without declaring them towns.

```json
{
  "schema_version": 1,
  "location_ids": [
    "eastrun",
    "briarfall-crossing",
    "greyhaven-mill",
    "greyhaven-valley",
    "northern-freight-enclosure",
    "blackthorn-watch",
    "caelthorne",
    "brackenford",
    "ashvale-estate",
    "ashvale-lodge",
    "briarstone-cottage"
  ],
  "business_categories": [
    "inn",
    "tavern",
    "general-store",
    "blacksmith",
    "armorer",
    "weaponsmith",
    "stable",
    "caravan-supplier",
    "alchemist",
    "healer",
    "herbalist",
    "tailor",
    "leatherworker",
    "carpenter",
    "builder",
    "food-market",
    "produce-merchant",
    "animal-trader",
    "library-scribe",
    "magical-service",
    "bank",
    "exchange",
    "lawful-money-custodian",
    "milling",
    "storage"
  ],
  "automatic_financial_postings": false,
  "approved_design_location_ids": [
    "caelthorne",
    "eastrun",
    "briarfall-crossing",
    "rivermere",
    "ironhollow-hold",
    "brackenford",
    "silverbrook",
    "stoneford",
    "southbank-landing",
    "windmere"
  ]
}
```
