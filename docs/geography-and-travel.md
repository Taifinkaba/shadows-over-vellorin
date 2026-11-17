# Phase 2 approved geography and travel

Read [Phase 2 source approval](../changes/chronicles/phase2-01-geography-approval.md) and [map specification](phase2-geography-map-spec.md) first. The earlier Chunk 2 guide below remains a dated baseline; its claims that no realms were approved and Elyndor/Frostmarch lack types are superseded by this section and the current directory.

APPROVED DESIGN is a geographic node/containment classification distinct from CONFIRMED CANON historical observations and PROPOSED unsurveyed corridors. It uses canon entity metadata plus explicit approval provenance and `approved-design` indexing; it grants no player knowledge or operational travel. Route classifications remain the original two-value schema, so realm approval cannot promote a road or duration into historical fact.

Retrieve Vellorin, proposed Aethoria, Northern Marches and the five realm IDs `valedorn`, `elyndor`, `ironhollow-holds`, `rivermere-league`, `frostmarch` through index.json. `world-geography` owns all containment; realm profiles own safe terrain, climate, resources, government type and broad border design. Existing `ironhollow-hold` and `rivermere` stay settlements, separate from their realm IDs. Caelthorne is Valedorn’s capital. No existing officials, current conditions or historical outcomes change.

The road registry now includes the Northern Marches–Frostmarch corridor and Elyndor Woodland Passage. Four requested existing corridor IDs are reused. All six remain PROPOSED and require topology/mode/condition review. The approved map has no invented distances, coordinates, exact borders, road operations or toll charges. Unknowns remain null; approved resources are not inventory.

Repository visibility is public, verified before editing. Metadata is not access control; all added design is safe reference material, and no hidden answers are stored here. No repository visibility action is authorized.

---

# Geography and travel — GM retrieval guide

The [geographic directory](../entities/mechanics/world-geography.md), [route registry](../entities/mechanics/travel-routes.md) and [travel procedure](../entities/rules/travel-procedure.md) extend the Chunk1 ownership plan. Retrieve an entity by ID through [index.json](../index.json). No existing location has moved; no campaign state changed.

## Read this before planning a journey

CONFIRMED CANON means a limited sourced identity or connection, not current passability or proof Theron traveled it. PROPOSED means a review candidate requiring player approval before use. UNKNOWN is represented by JSON `null`, not zero distance, free tolls, safe roads, an empty countryside or absent seasonal restrictions. `[]` for durations means no baseline is available. Unspecified intermediates use `null`; a future verified empty list would mean none are recorded on that specific leg.

Existing entity metadata has no `proposed` status. New unapproved geographic placeholders/routes therefore use `status: research`, tag `proposed`, and explicit `classification: PROPOSED` in the directory/route body. Framework/directory/procedure records use `canon` for the maintenance rules themselves; that never approves their proposed contents. `last-verified` place records preserve established names without promoting their entire archival design.

Hierarchy membership and containment edges belong to `world-geography`; physical facts belong to locations. Road facts belong to the single JSON block in each `entities/locations/route-*.md`. `travel-routes` owns only a list of route IDs. These tables explain retrieval; they are not another editable road database.

## Existing identity and containment

All18 preexisting location entities remain byte-for-byte intact. A sourced Seven Bells independent Witness entrance record is also promoted from the existing investigation without adding an access route or discoveries. New evidence-backed place records promote Vellorin (territorial name, political type unknown), Northern Marches, Blackthorn North Waystation, Ironhollow Hold, Rivermere and Mount Elarion. The archived map supports established Ironhollow Hold/Rivermere names; the later atlas explicitly marks their long-distance route estimates as prospective.

Confirmed containment: Briarstone Cottage → Brackenford → Northern Marches → Vellorin; Hollow Veil at Mount Vaelspire; Hollow of the First Hour beneath Mount Elarion. Vellorin → Aethoria is only PROPOSED. Aethoria is a proposed continent framework; Elyndor and Frostmarch are unlocated proposed names of unknown geographic type. No new nation, ruler, border or province has been approved.

Cities/towns/villages, properties, watch stations, wilderness and named sites use existing location IDs. The hierarchy supports province/hamlet/dungeon-entrance kinds without creating invented examples. The Seven Bells record identifies a historically used entry; no new surface coordinates or universal access are certified. Other dungeon records identify sites, not newly surveyed door coordinates. No inferred containment of every Crown-region place inside a freshly drawn national boundary.

Unresolved identities remain separate: Greyhaven Mill versus Greyhaven Valley versus the northern freight enclosure; Ashvale Lodge versus the historical hidden woodland lodge; Blackthorn Watch versus Blackthorn North Waystation; Frostmarch versus Frostspire; Hollow of the First Hour versus Hollow Veil. “Greyhaven” and “Ironhollow” in the request are search labels, not evidence of additional duplicate settlements or automatic aliases.

## Sourced travel information

| Route ID | Source-backed information | Limits |
|---|---|---|
| `route-ashvale-eastrun` | Estate–Eastrun road: a little over two hours | Mode UNKNOWN; numeric120 minutes is a strict lower bound with no upper bound, not a two-hour promise. |
| `route-eastrun-briarfall` | Eastrun–Briarfall: approximately three hours walking | Alignment relative to wagon-capable northern road and shorter wagon-inaccessible woodland route UNKNOWN; do not apply foot timing to wagons. |
| `route-waystation-brackenford` | Northern-road village branch: approximately35 minutes by wagon | Start is Blackthorn North Waystation, not Blackthorn Watch. Present road status UNKNOWN. |
| `route-brackenford-cottage` | Western Mill Lane: approximately eight minutes walking | From village center to cottage; other modes/times UNKNOWN. |

No verified distance is stored for any route. The reports do not establish current weather, safe travel, inn vacancies or where a character is today. Bidirectional planning is supported, while reverse travel is explicitly marked PROPOSED until supported/approved; a reverse assumption is never recorded as a historical trip.

## Proposed network

Seven routes reproduce only the later archived atlas's one-way laden-wagon estimates from Caelthorne: Ashvale Estate (~2 days), Eastrun (2–3), Briarfall Crossing (1–2), Blackthorn Watch (3–4), Ironhollow Hold (4–6), Rivermere (3–5) and Frostspire Peaks (7–12). IDs are `route-caelthorne-<destination-id>`. All are PROPOSED, not observed journeys. Normal road/weather assumptions and undefined daily rest schedule prevent precise conversion to elapsed hours or mileage. Do not add/subtract these legs to assert cross-country distances.

Seven additional connectors have no duration, distance or invented alignment:

| Route ID | Purpose / unresolved facts |
|---|---|
| `route-ashvale-estate-ashvale-lodge` | Access planning; does not equate the developed lodge with the old hidden woodland lodge or assert a separate distant site. |
| `route-eastrun-greyhaven-mill` | Rural mill connection candidate; no reconstruction of the Day44→46 wagon transfer. |
| `route-eastrun-greyhaven-valley` | Independent academy access candidate; no mill/valley merger. |
| `route-blackthorn-watch-blackthorn-north-waystation` | Possible network connection; distance, alignment and station identity remain separate. |
| `route-caelthorne-mount-vaelspire` | Northern approach candidate; passability/access/route to sanctuary unspecified. |
| `route-caelthorne-elyndor` | Review placeholder; not proof of direct adjacency or a road to an approved nation. |
| `route-caelthorne-frostmarch` | Review placeholder; not a route to Frostspire under another name. |

Canon-only traversal is deliberately disconnected. Approval of a route proposal must establish its missing topology and conditions before the GM can rely on it; broad approval of a document does not fabricate missing historical journeys.

## Cross-system links for Chunks3–6

Route integration points specify target ID, classification, placement and `at_location`; a service at an endpoint is not a roadside stop. Existing links cover Caelthorne magistrates/watch and Wayfarers HQ; Brackenford market, Willow Lantern inn and local authority directory; cottage private property; Blackthorn North Waystation; Greyhaven Valley academy; and Hollow Veil as an unlocated sanctuary/entrance integration point. Service capacity, permission and access remain with their owner records.

Future integrations: settlement/business directories should resolve actual inn/market/guild-hall premises; justice records should supply territorial patrol scope, courts and prison destinations only when established; dungeon registry should reference Ninth Vault/Mirror Foundation, the two distinct Hollows and Seven Bells evidence without moving entrances or transferring protected originals. Trade/border records should identify genuine crossings, toll authority and seasonal controls. None of those systems is newly implemented by this chunk; a linked watch or court never grants custody, access, immunity or current staffing.

## GM procedure and remaining gaps

Use the ten-step [travel procedure](../entities/rules/travel-procedure.md). Before departure state compatible-mode baseline, terrain/condition uncertainty, rest/supply assumptions and any proposed forward estimate. Riding, caravans, night/weather travel, animal care and delays have no invented universal speed multipliers. Costs, rest and encounters happen only during authorized play. Magical movement uses existing spell limits and finite resources; no new teleport network.

If blocked, retain the last established position and offer waiting, returning or a documented alternative. An unsourced bypass is a proposal requiring a persistent record and approval. “Closest settlement” is UNKNOWN without a sourced current position and route geometry. Presently Theron remains at the unchanged checkpoint, not on any road.

Open geography decisions: complete versioned expansion source; continent/nation topology and borders; Elyndor/Frostmarch identities; Greyhaven and lodge equivalences; missing intermediate settlements; exact mileage, riding/caravan baselines; road surfaces, hazards, current patrol coverage, toll schedules, seasonal closures, rest availability and dungeon approach coordinates. Do not fill these from similarly named places or archived initial faction-clock values. The preexisting Day156/Day181 reconciliation remains out of scope.
