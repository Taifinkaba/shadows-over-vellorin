# Phase 2 PR 1 — geography and travel review

Base: `9178c3c5dfa0a05766eedda30cb2204b0a8991d6` (`main`, merged Day181 reconciliation PR 23). Branch: `lore/phase2-01-geography`. Only PR 1 is implemented; no merge or next phase is authorized. The PR number/link is supplied by GitHub when opened; this report is its review evidence.

## Implemented design and ownership

Five approved realm profiles establish Valedorn’s hereditary monarchy and Caelthorne capital, Elyndor’s Circle of Rootwardens, Ironhollow Holds’ clan confederation, Rivermere League’s merchant-town federation, and Frostmarch’s chiefs/seasonal assemblies. Profiles provide terrain, climate, finite resource themes, rivers/watersheds, forest/mountain/frontier belts and broad border character without exact survey claims. They appoint no officials and assert no present operations.

Vellorin remains the historical territorial umbrella, with Northern Marches and the original Brackenford/Cottage hierarchy intact. Proposed Aethoria remains the working continental framework. The sole `world-geography` directory owns new approved containment; existing place profiles, route owners, road registry and justice-road lookup retain their domains. Realm and settlement identities are separate. The map specification defines approved versus unsurveyed layers and unplaced labels.

APPROVED DESIGN is restricted to geographic nodes/edges, with canon metadata, approved-design indexing and approval-source checks. Historical observations remain CONFIRMED CANON; unverified corridors remain PROPOSED. A historical containment edge cannot inherit confirmation from a design-only node, and a route cannot use the new classification. No player knowledge or operational road is generated.

Four requested existing corridors are reused: Caelthorne–Eastrun/Rivermere/Ironhollow Hold and Eastrun–Greyhaven Valley. Two new region-scale proposals cover Northern Marches–Frostmarch and Elyndor Woodland Passage. Mode/terrain/weather/rest/season/authority/toll review is explicit; no invented time or distance is added. Justice lookup adds unknown-only links for coverage, with no new legal powers. All 18 existing distance/duration payloads, including four historical reports and seven archived wagon estimates, remain unchanged.

## Indexed IDs

New: `valedorn`, `ironhollow-holds`, `rivermere-league`, `route-northern-marches-frostmarch`, `route-elyndor-woodland-passage`.

Reused and promoted from placeholders: `elyndor`, `frostmarch`. Existing `aethoria`, `vellorin`, `caelthorne`, `ironhollow-hold`, `rivermere`, `northern-marches` and all route IDs remain distinct. No duplicated person, business, settlement or organization is created. Total indexed entity count: 212.

## Canon and state preserved

All state files, historical snapshots, archives and preexisting historical chronicles remain byte-for-byte unchanged. The new preservation manifest pins every untouched campaign authority and records before/after hashes for only 11 authorized geography owners. Older preservation-fixture updates change only those owner digests; historical source evidence is not rewritten. The justice test’s fixed 18-road count becomes exact indexed-route coverage to accommodate the two additions.

The Day 181 19:30 Ashvale Estate endpoint, HP 100/100, MP 400/400, S+/Level 5, normal DEF 49/conditional 51, Nexus 156/180, wagon 60/60, controlled 745 gp 9 sp, unpaid 317 gp and uncommitted 428 gp 9 sp remain unchanged. House Ashvale retains Briarstone Cottage. Chronos Eye/Dragon Slayer stay locked. Unknown current equipment, account allocations, companion locations and undocumented events remain unknown. No historical travel, resource posting, movement, appointment, custody action, quest progress or automatic NPC event is invented.

Distinct Northern Marches/Frostmarch/Frostspire, Greyhaven Mill/Valley, Blackthorn Watch/North Waystation and the two Hollows remain protected; no new Crown jurisdiction is inferred from realm membership.

## Unknowns and conflicts

Continental outline, exact borders, realm adjacency, most existing places’ realm membership, river courses/confluences, distances and coordinates remain unsurveyed. Northern Marches has no inferred realm assignment. Elyndor Passage uses region scopes, with local gates and onward junctions unresolved; it cannot supply an executable itinerary. Existing route estimates are not observed travel or evidence of road operations. Current weather/passability, rest/feed availability, crossing rights, patrols, tolls and resource quantities need source-backed verification. No unresolved conflict blocks design review, but these gaps block automatic travel use.

## Privacy and spoilers

Repository metadata was verified as public before editing; visibility is unchanged. All added content is safe design/reference material. No secret leaders, hidden answers, undiscovered operations or mystery resolutions are added. gm-reference metadata provides no access control. Existing repository contents are not certified spoiler-safe by this scoped change, and no genuinely private answer store is claimed.

## Validation and readiness

Validation passed: `python scripts/validate.py`; `python -O scripts/validate.py`; full `python -m unittest discover -s tests -v` (795 tests,172.680s); `python scripts/economy.py --report`; dashboard generation and `--check-view` freshness verification; quest readiness report; `git diff --check`. Seven new geography regression tests and the updated justice suite pass. Existing quest readiness still reports18 pending answer approvals/14 unfilled clue routes; this PR changes neither and does not declare the ending ready.

Ready for player review after passing checks. No automatic merge, gameplay or PR 2 start. Continue only after explicit player approval and merge of PR 1.

## Files added (10)

- `changes/chronicles/phase2-01-geography-approval.md`
- `docs/phase2-01-review.md`
- `docs/phase2-geography-map-spec.md`
- `entities/locations/ironhollow-holds.md`
- `entities/locations/rivermere-league.md`
- `entities/locations/route-elyndor-woodland-passage.md`
- `entities/locations/route-northern-marches-frostmarch.md`
- `entities/locations/valedorn.md`
- `tests/fixtures/phase2-01-preservation.json`
- `tests/test_phase2_geography.py`

## Files modified (26)

- `changes/CHANGELOG.md`
- `docs/geography-and-travel.md`
- `docs/validation.md`
- `entities/locations/aethoria.md`
- `entities/locations/elyndor.md`
- `entities/locations/frostmarch.md`
- `entities/locations/route-caelthorne-eastrun.md`
- `entities/locations/route-caelthorne-ironhollow-hold.md`
- `entities/locations/route-caelthorne-rivermere.md`
- `entities/locations/route-eastrun-greyhaven-valley.md`
- `entities/locations/vellorin.md`
- `entities/mechanics/justice-road-links.md`
- `entities/mechanics/travel-routes.md`
- `entities/mechanics/world-geography.md`
- `index.json`
- `scripts/travel.py`
- `tests/fixtures/chunk10-preservation.json`
- `tests/fixtures/chunk4-preservation.json`
- `tests/fixtures/chunk5-preservation.json`
- `tests/fixtures/chunk6-preservation.json`
- `tests/fixtures/chunk7-preservation.json`
- `tests/fixtures/chunk8-preservation.json`
- `tests/fixtures/chunk9-preservation.json`
- `tests/fixtures/day181-final-reconciliation.json`
- `tests/fixtures/day181-migration.json`
- `tests/test_justice.py`
