# World status — read-only retrieval view

This page is a usage guide, not a saved current checkpoint or live self-updating dashboard. Generate a fresh projection at the time of use:

```sh
python scripts/gm_dashboard.py --format json
python scripts/gm_dashboard.py --format markdown
```

The command validates the repository, resolves original owners through index and prints to stdout only. It never writes campaign files or saves a cache. Optional `--root PATH` selects another repository. A copied JSON view carries source fingerprints; `--check-view PATH` rejects a stale, edited, incompatible or invalid-source view. It does not promote a saved view into authority. Regenerate after owner changes; source hashes do not establish truth or disclosure permission.

| Section | Projection / retrieval authority | Limits |
|---|---|---|
| Current scene | checkpoint date/calendar/time/location/status, explicitly listed present IDs and source reference | Generic home wording never supplies the rest of the party. No raw context/project or narrative dump. |
| Theron | checkpoint HP/MP/base/equipped defense, finite staff/wagon pools and locks; reviewed Night Sovereign worn-bonus item phrase | Equipment/conditions/skill details require relevant owners; no current pool assumed from maxima. |
| Finances | current finance ledger totals/accounts/exclusion amount references and unpaid commitments | No second ledger; owner labels do not prove sole personal legal title. Mixed narrative/gap text is linked rather than rendered wholesale. |
| Companions | original actor/assignment routing with checkpoint-listed presence only | Other current locations, source dates/progress and private knowledge are not reliably normalized; show UNKNOWN / retrieval required rather than infer or expose them. |
| Estate/academy | property reference manager/title fields and original business/project owners | Roles do not certify presence, income, current cash, completed work or ownership of merchant/academy funds. |
| Quests | public-reference quest metadata, historical objective handles and neutral approval counts | Metadata active can contain completed subobjectives. No hidden-answer values, question text or raw mixed-discovery quest prose. |
| World | faction identity classifications, source-derived exploration enums and event/legal source handles | No faction intelligence dump, active event claim, blanket jurisdiction or current safety guarantee. |
| Warnings | fixed warning categories and links to audit/verification/precedence | Missing details are UNKNOWN; source links are not player discovery or permission to narrate whole files. |

Current authority remains the repository's Day156 checkpoint; the later supplied Day181 snapshot is explicitly unadopted and routed through [integration audit](world-bible-integration-audit.md) / [verification queue](../state/open-verifications.md). This guide contains no second numeric checkpoint and does not reconcile the missing history. Snapshot differences are not invented transactions or recovery.

Every projected leaf has a source reference/owner context, source-as-of where known, and qualification. “UNKNOWN” or null is not zero/no problem/no task. Projection creation does not constitute a new observation or discovery. Full validation may scan declared records; the output field allowlist is deliberately narrower. This public repository is not certified spoiler-safe: GM-reference can include restricted text, so broad prose, secret entities, intentions, raw handoff/verifications, hidden answers and private knowledge distinctions are omitted. Human discovery review remains necessary before gameplay presentation.

The Markdown view uses separate initially closed native details controls for resource, treasury, companion/personnel, quest and world sections. Renderers without functioning disclosure support require the concise fallback in [narration rules](narration-format.md); do not pretend a decorative heading is interactive. Use [GM manual](game-master-operating-manual.md) for targeted scene preparation and authoritative updates after actual play. Running a report advances no time, pays nobody, changes no status and creates no session.
