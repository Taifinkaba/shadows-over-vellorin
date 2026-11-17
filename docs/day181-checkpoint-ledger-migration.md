# Day181 endpoint adoption and finance compatibility

Prepared on main `1e3e2aa11f08f5d2d0ebff9fe8a29833e40f312e`, including merged audit PR21. Explicit player authorization adopts the supplied endpoint for this reconciliation PR; it does not authorize merge, new gameplay or reconstructed history. [Adoption source](../changes/chronicles/year848-day181-endpoint-adoption.md).

| Field | Historical Day156 | Adopted Day181 |
|---|---|---|
| Date/time | Year848 Suncrest36 Day156,20:15 | Year848 Suncrest61 Day181,19:30 |
| Location/status | Estate family sitting room; ENDED | Ashvale Estate; exact room and session status UNKNOWN |
| Personal HP/MP |100/100;378/400|100/100;400/400|
| Defense/pools | normal49;51 only worn; Nexus156/180; magic wagon60/60 | Same explicit numerical targets; current Night Sovereign wearing/configuration UNKNOWN |
| Cash / unpaid commitment / available |77190cp /31700cp /45490cp|74590cp /31700cp /42890cp|
| Individual allocations |11 dated historical accounts |UNRECONCILED / UNKNOWN; no currently certified accounts|

The2600cp difference is **UNEXPLAINED ENDPOINT DIFFERENCE — PROVENANCE UNRESOLVED**, not any type of financial event. It is not assigned to Blackscale, operations or a fictitious account. The lower available amount is the same difference, not a second expense. +22 personal MP is **UNEXPLAINED ENDPOINT CHANGE — PROVENANCE UNRESOLVED** with no recovery events. No rest, assimilation, spell, potion or transfer is invented. Calendar labels supply no intervening scenes. Construction remains committed/unpaid/not started under the explicit instruction; no new invoice, payment or work occurs.

## One live authority and immutable history

Only [state/checkpoint.json](../state/checkpoint.json) and [state/finance-ledger.json](../state/finance-ledger.json) are live authorities. Historical checkpoint5, ledger2 and three affected entity records are archived under `archive/checkpoints/year848-day156-*`; these are evidence, not another editable current checkpoint/ledger. Exact original bytes/content are hash-protected, and every old ledger2 arithmetic/ownership validator still runs when finance3 validates its historical reference. Original chronicles and unrelated campaign records remain unchanged.

Checkpoint6 preserves existing numerical/core field ownership and adds source-qualified provenance. Current companion presence/roles are empty because unverified; UNKNOWN never means everyone disappeared. Current equipment is unknown, distinct from the old carried/not-equipped observation. Other world/context/custody facts route the last-verified historical checkpoint, not a newly observed Day181 result. Rank, level, attributes, locks, abilities, assignments, bonds, ownership, quests and custody outcomes are unchanged. [Handoff](../state/next-chat-handoff.md) and [verification queue](../state/open-verifications.md) retain the gaps. UNKNOWN session status is not an active session or a new END SESSION event.

Finance3 contains:

- `historical_day156_ref`: immutable historical ledger2; its115990cp opening, five actual historical events and77190cp closing remain mathematically intact. Its allocations/restitution/previous modeled surplus stay history, already applied once.
- `endpoint`: explicitly supplied74590cp at Day18119:30, with adoption provenance.
- `bridge`: historical77190 minus endpoint74590 equals2600; `is_transaction:false`, `assigned_account_id:null`. This disclosure never enters current cash arithmetic.
- `account_verifications`: initially empty; future sourced/approved **opening allocations of the endpoint total**, with ownership/control scope, date, evidence and authorized actors. Verification does not create cash. Do not substitute a later post-transaction balance as an opening balance; subsequent movements belong in actual events.
- `transactions`: empty in this PR. Later actual events affect current cash/account balances/commitments, never the historical arc or endpoint bridge.
- `controlled_cash`: endpoint plus signed effects of actual transactions; only verified current account balances, with unknown/partial/full allocation qualification. A remaining unallocated aggregate is not an invented account or the2600cp gap.
- `commitments`:31700 committed,0 paid,31700 outstanding,42890 uncommitted, not started. Actual linked construction payments reduce controlled cash and outstanding commitment once; they do not automatically certify construction progress/completion.
- Exclusions retain historical qualifications and stay outside controlled cash: provisional/office/personal/academy/deposit/custody/merchant/evidence/salvage/noncash property. No liquidation, new title, rent or restitution duplicate.

## Future real-event contract — validation only

`finance_v3.py` validates candidate data; no writer, scheduler or actual posting API is added. Future actual updates remain reviewable owner/chronicle/checkpoint edits, with the same ledger authoritative. Each transaction requires unique `id` and `source_event_id`, actual date/time, evidence `{source_ref,quote}`, verified/player-approved status, category/direction, integer-copper amount/effects, payer/recipient labels, verified account, authorized actor, optional transfer destination, commitment/property/business/contract links, controlled ownership scope and application_count1.

Supported categories: business revenue, wages, supplies, construction payment, property purchase, contract reward, internal transfer, owner distribution, restitution disbursement and other source-backed receipts/expenses. Unknown income is not posted. Transfers/distributions inside controlled cash are not new income; external distributions reduce cash without becoming revenue. Noncash appraisals are not transaction categories. Historical event IDs/rewards and any pre-adoption/adoption/reference source cannot be recycled as a new payment. Actual funding/event evidence must use a new dated chronicle, not an old generic business description or the old520gp reconstruction. No transaction may cite this adoption as proof the2600cp difference was spent.

Funding account verification must precede its transaction, be independently sourced/approved and fit within the endpoint allocation; authority and available verified balance constrain spending. Unknown Day181 allocation authorizes no account-specific payment. A real incoming receipt also needs a verified receiving account/ownership classification. Account-owner labels, actual evidence truth, legal title, consent and whether a business quote represents only the eligible commission still require human source review; existence of a file/quote is not independent verification.

Arithmetic is integer copper only:1gp=100cp,1sp=10cp. Current total =74590cp + actual cash effects; remaining expansion =31700cp − actual linked payments; available = current total − remaining commitment. A100cp construction payment in a disposable fixture yields74490cp cash,31600cp outstanding and42890cp available. No such payment is real in this PR. Ordinary expenses reduce available funds; source-backed internal transfers change account balances only. Future progress needs separate actual evidence, not a payment inferred as work.

## Dashboard, reporting and compatibility

The read-only dashboard supports historical checkpoint5/ledger2 and current checkpoint6/ledger3. It displays Day181 supplied continuity,745gp9sp controlled/317gp unpaid/428gp9sp available, MP400/400, normal49/conditional51, unchanged Nexus/wagon pools, unknown wearing/companions/current allocations and explicit26gp/+22MP gaps. Historical account figures appear separately, with Day156 qualification. Source fingerprints plus strict view comparison reject saved Day156 views after migration. Reports never turn historical allocations into current funding or the bridge into an expense.

Historical Day156 tests explicitly restore the byte-preserved snapshot/three records in disposable roots. Older checkpoint fixtures and historical validators remain supported. Only the seven approved current-state files have revised entries in existing preservation manifests; before/after hashes and adoption provenance are retained. A new migration manifest protects the original snapshots and every unrelated campaign authority. No historical hash is replaced with invented history.

Run normal/optimized validation, full unittest discovery, whitespace checks, dashboard JSON/Markdown generation and saved-view verification, plus the read-only economy report. Future legitimate updates review relevant current preservation expectations deliberately; immutable historical snapshots/chronicles do not change. Main-quest secret designs/private storage and all unrelated approvals remain separate. No visibility action or new playable session occurs.
