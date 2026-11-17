# Phase 2 settlement retrieval update

The [approved settlement and business inventory](phase2-settlements-and-services.md) and [trade/postal framework guide](phase2-trade-and-communications.md) supersede the old guide’s unapproved population/empty-business-design limitations below. The historical eleven localities and fourteen services remain distinct, with their evidence unchanged; they are not ten new towns or forty-one current operating businesses. The current directory owns only routing, while each location’s approved_design object owns its approved expansion. Existing person/property/business authority retains precedence. Geography remains with world-geography, routes with route owners, prices with service-price-references and cash with the sole finance ledger. No gameplay or current-condition verification occurs.

---

# Settlement, business and service directory — Chunk 3

This is retrieval, not another source of truth. Resolve IDs through [index.json](../index.json); each location owns its `Settlement and business references — Chunk 3` section. [Settlement/service routing](../entities/mechanics/settlement-services.md) lists profile owners, not copied town facts. Business IDs are scoped as `parent-location:slug`; they are records within that parent, not separate locations or a new entity type.

Eleven existing profiles are integrated: four named settlement centers plus seven watch, valley, freight, mill or private-property sites. They are not eleven newly declared towns. Fourteen source-backed business/service records include venues and facilities, not fourteen confirmed independent proprietors. No proposed business instances, new NPCs, new settlements or governments are added.

## Profile lookup

All entries below refer to established identities (CONFIRMED CANON). Profile nulls mean UNKNOWN, not “there is no service.” No current vacancy, counted stock, quoted tariff, opening schedule or new visit is established by this directory.

| ID / authoritative record | Type and stable reference | Known service/institution retrieval | Main unknowns |
|---|---|---|---|
| [eastrun](../entities/locations/eastrun.md) | Existing settlement; historical Estate and Briarfall connections | No individually verified shop record promoted | Population, nation/region, named local government, precise buildings, merchants, accommodations, healer/stables and district plan |
| [briarfall-crossing](../entities/locations/briarfall-crossing.md) | Crossing settlement and surrounding woodland | Northern trade road supports wagons; shorter woodland route does not | Specific merchants, inn/stable addresses, town officers, population and alignment of foot report versus wagon road |
| [greyhaven-mill](../entities/locations/greyhaven-mill.md) | Established mill site, not an invented Greyhaven town | Mill name/site only; no retail business certified | Operator, ownership, public milling terms, services, connection to valley/enclosure and missing historical wagon journey |
| [greyhaven-valley](../entities/locations/greyhaven-valley.md) | Valley / academy site | Existing [independent academy](../entities/factions/dragon-slayer-academy.md), managed by Beren; original personnel retained | Town identity, population, shops, local government and current public access/fees |
| [northern-freight-enclosure](../entities/locations/northern-freight-enclosure.md) | Separate freight site | No public shop, inn or active supply chain established here | Ownership, access, ordinary services, routes and current operating schedules; no investigation details repeated |
| [blackthorn-watch](../entities/locations/blackthorn-watch.md) | Existing watch/refuge site | Watch command and refuge/healing services | Current officer, civilian judicial authority, gaol, fees/capacity, inn/stables/trade infrastructure and street layout |
| [caelthorne](../entities/locations/caelthorne.md) | Crown administrative center | Existing magistrates, watch, archives and [Wayfarers headquarters](../entities/factions/wayfarers-guild.md) | Named current officials, ward map, market/inn/merchant addresses, courthouse/gaol addresses, public access and fees |
| [brackenford](../entities/locations/brackenford.md) | Village in Northern Marches, Vellorin; approximately180 residents | Reeve Elsbeth Marrin/council; watch captain Ressa Vale with six part-time members; five business records below | Court/magistrate location, exact shop addresses/hours/prices/stock, guild premises and additional districts |
| [ashvale-estate](../entities/locations/ashvale-estate.md) | Private estate/commercial settlement, no separate municipal charter | Seven facility/venue records; Tomas stewardship; lodge links | Public access, exact schedules, individual merchants, vacancies and customer tariffs; nation/region placement not invented |
| [ashvale-lodge](../entities/locations/ashvale-lodge.md) | Developed lodge property, not a surrounding town | Hospitality/stables and paid repair forge; existing staff roles | Individual adult staff names/rates, room count/vacancies, current quotes and equivalence with the historical hidden woodland lodge |
| [briarstone-cottage](../entities/locations/briarstone-cottage.md) | Separate House Ashvale property at7 Western Mill Lane, Brackenford | Private property; not listed as an inn or rental business | Future use, repairs and access terms; no rent yet and no municipal ownership or authority |

Each profile explicitly stores nation/territory/region references, type, population/qualification, government, principal official, watch/officer, court, connecting route IDs, neighborhoods, nearby location IDs, institution references, service links, local-problem references and source/evidence references. Vellorin remains a confirmed territorial name with unknown political type; nation_id remains null. Unknown nation/region assignments stay null even if an archived regional design looks plausible. Medical services derive only from the listed healer/herbalist/refuge records; no additional medical provider, religious establishment or magical retailer is established. Guild presence is limited to verified headquarters/academy references; archived professional organizations and local branch proposals are not silently approved.

## Business/service lookup

A descriptive label is not a new trading name or proof of a dedicated storefront. Unknown proprietor remains null even where an operator is known. Estate ownership here concerns established premises/facilities; participating merchants retain their property and stock.

| Parent-scoped ID | Service / known personnel | Boundaries |
|---|---|---|
| `brackenford:willow-lantern` | Willow Lantern; Mara Fenwick innkeeper; six rooms | Owner, vacancies, meals/stabling, hours and current room price UNKNOWN |
| `brackenford:forge` | Existing forge/blacksmith service; Borin Emberhand | Owner, specialty goods, stock and current commission availability UNKNOWN |
| `brackenford:herbalist` | Seren Willowmere's herbalist service | Shop name/address, ownership, available herbs and treatment capabilities UNKNOWN |
| `brackenford:watermill` | Established mill premises | Harlan Wicks is a known local miller; assignment to this specific mill and ownership not proven |
| `brackenford:market` | Established village market | Vendors, goods, schedule and administration UNKNOWN |
| `ashvale-estate:healing-springs` | Existing natural Healing Springs; estate under Tomas | No newly certified healing effects, public treatment or magical powers |
| `ashvale-estate:merchant-storage` | Twenty storage bays | Capacity is not availability, goods ownership or counted merchant inventory |
| `ashvale-estate:rental-cottages` | Existing rental accommodation | Occupancy, price, capacity and future receipts UNKNOWN |
| `ashvale-estate:bakery` | Existing bakery; baked-goods category | No counted loaves, price quotation, completed sale or supply delivery |
| `ashvale-estate:market` | Estate market/stall venue | Existing22% eligible merchant fee remains policy; no revenue posted or merchant stock claimed |
| `ashvale-estate:lantern-exchange` | Lantern Exchange, existing paid information/report/private-meeting service | Not a newly established bank, money exchange, guaranteed intelligence source or secret-reveal mechanism |
| `ashvale-estate:caravan-facilities` | Existing caravan facilities | Specific stock, suppliers, capacity and current services UNKNOWN |
| `ashvale-lodge:hospitality` | Existing rooms/meals/stabling under Tomas | One hospitality complex; staffing pool is not a new assignment. Existing safe optional paid youth-work conditions retained |
| `ashvale-lodge:forge` | Existing paid repair work; Tomas stewardship, smith operator unknown | Bren's construction/maintenance role does not appoint him blacksmith; no new construction or expense |

Tomas remains estate/lodge steward/accountant; Bren retains construction/maintenance. Mira, Joren and Elsi remain the existing supervised helpers with unconditional shelter/meals/schooling and no hazardous, forge or night work. Unnamed adult staffing remains unnamed. No new owner, manager, payroll, transfer, relationship or meeting is created.

The schema supports taverns, general stores, armorers, weaponsmiths, caravan suppliers, alchemists, healers, herbalists, tailors, leatherworkers, carpenters/builders, produce/animal merchants, libraries/scribes, magical services and historically established lawful money custodians. A category is not proof that such a business exists in any settlement. Ordinary stores acquire no high-level magic items or unlimited stock.

## Price, currency and inventory retrieval

[Service price references](../entities/mechanics/service-price-references.md) distinguish historically paid, current verified quote, approved reference, proposed regional estimate and unknown price. Currency stays100cp/gp and10cp/sp, using integer copper. Merchant acceptance of denominations, barter, credit or exchange policy remains independently UNKNOWN.

The forge/workshop's historical72gp construction payment is stored as7200cp with its original source; it is not a current repair price or payable invoice. The research room28gp and training courtyard18gp remain paid facilities in the original lodge record and are not charged again. No current verified customer quote or newly approved reference price is added.

Six archived LOCKED DESIGN bands are carried only as PROPOSED references: simple food2–5cp; meal10–30cp; common bed30–70cp; private room100–200cp; stable/feed10–30cp per horse/night; herbs/bandages20–80cp. They are not actual Willow Lantern, lodge or village shop quotations, not arbitrary inflation and not approval of fixed tariffs. Future confirmed prices need their own source and approval where required. Unknown prices are empty price arrays, never zero-cost offers.

All counted stock is UNKNOWN. Permanent goods categories, six-room inn capacity and twenty-bay storage capacity are separate from sellable quantities or vacancies. No restock, consumption, equipment transfer or delivery is implied. [Party finances](../entities/mechanics/party-finances.md) and the existing finance ledger retain all monetary authority; older till amounts are not copied into this directory. Rental property and merchant stock are not new controlled cash.

## Roads and institutions

Each parent profile links only its actual Chunk2 endpoint route IDs. Read each road owner's classification; listing a PROPOSED route does not make it an active supply chain. All18 road records and their data remain unchanged.

The four limited historical connections serve Estate–Eastrun, Eastrun–Briarfall, North Waystation–Brackenford, and village center–cottage. Duration/mode/uncertainty remain in their route owners. The Caelthorne corridors and lodge/Greyhaven/Watch connectors retain their proposal status; no distances or completed deliveries are introduced. The enclosure has no fabricated public access road. Nearest inn/settlement cannot be determined without a known position, connection and accessibility; do not invent a ranking from map names.

Brackenford's streets/landmarks remain in the village record: Western Mill Lane, Bracken River/bridge, millstream, birch copse, market and communal grazing land; this does not divide it into newly invented wards. Known officials are linked, not replaced. Blackthorn military/watch personnel gain no civilian judicial power. The Valedorn prison network, Crown Hall of Justice, new wardens and Continental Guild Concord are not implemented or approved. Named gaols and prison destinations remain unknown where unsupported.

## Local activity and minimal retrieval procedure

[Local activity framework](../entities/mechanics/local-settlement-activity.md) supplies categories only: merchant disputes, missing supplies, road damage, complaints, seasonal/labor shortages, festivals, construction requests, recruitment and medical emergencies. Its events list is empty. No offer, reward, crime, emergency, festival or world-clock advance is generated during maintenance. Existing work requires its original dated source and knowledge check before presenting it as available; no contracts are reopened or rewards repeated. Detailed autonomous progression remains for Chunk8.

1. Resolve the settlement/site ID in index.json; read that location's profile. Do not treat Greyhaven's separate sites as a town or equate Watch with North Waystation.
2. For buildings/services follow the parent-scoped business ID or existing institution link. Fetch only relevant personnel records when needed. A linked profession does not prove shop ownership or a meeting with Theron.
3. For an inn, healer, blacksmith or stable, report the sourced service and limits. Unknown street location, hours, fees, vacancy, ability or stock remains UNKNOWN. Nearby is not automatically nearest.
4. For goods, use category versus actual stock; confirm quantity, title, price and capacity in play before any purchase. Historical paid costs and proposed bands cannot become current quotes.
5. For government/watch/guild questions use the profile's institution links. If officer, branch premises, courtroom or prison is missing, say UNKNOWN; do not introduce a later-chunk institution.
6. For the next settlement use the relevant route owner and compatible mode. Preserve proposal status and missing intermediates; do not extrapolate route geometry or historical travel.
7. For local work consult original quest/contract records only as a separate GM retrieval step, checking date and character knowledge before disclosure. Directory categories are not jobs.
8. Follow narration-format.md for attributed dialogue and independently closed functioning disclosures for long registers. Directory retrieval changes no location, inventory, cash, staffing, custody or quest state.

The new material contains ordinary service references only; it adds no hidden motives, conspiracy answers, secret dungeon information or new GM-secret dossier. `gm-reference` is not proof of player knowledge, and the directory is not an automatic discovery mechanism. The existing public-repository/private-governance conflict remains unresolved; visibility is unchanged and needs separate resolution.
