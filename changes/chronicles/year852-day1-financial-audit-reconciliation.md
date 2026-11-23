# Year 852 Day 1 financial audit reconciliation

At the existing Year 852 Day 1, 12:00 AM checkpoint, ordinary controlled cash remains **7,145 gp provisional**, including the 100 gp personal purse target. This maintenance records the player’s financial continuity ruling and reconciles existing campaign entries. The net cash adjustment is **0 gp**. Independent vouchers remain unverified where only played continuity supports the amounts. [Checkpoint](../../state/checkpoint.json) · [Finance ledger](../../state/finance-ledger.json)

## Historical 317 gp expansion

The original line was a 317 gp estate expansion estimate, later reserved within controlled cash and called the lodge expansion in the earlier reconciliation. At Year 848 Day 196 the archive records **317 gp committed, 0 gp paid, 317 gp outstanding**, with construction recorded as not started. The record identifies a budget commitment, with itemized construction scope, contractor and invoice still unknown. [Day 137 ledger](../../archive/checkpoints/year848-day137-finance-ledger.json) · [Day 181 reconciliation](year848-day181-cottage-mana-reconciliation.md) · [Day 196 ledger](../../archive/checkpoints/year848-day196-finance-ledger.json#L245)

**Later status — COMPLETED / PAID IN PLAYED CONTINUITY — PAYMENT DOCUMENTATION UNVERIFIED.** The player’s financial audit handoff confirms that the original expansion was authorized, completed and paid in full in played continuity. That ruling resolves the narrative obligation. Review of the Day 196, Suncrest 262, Day 160 and current posting histories found no identifiable standalone 317 gp outflow or linked installments totaling 317 gp for this project. The current commitment amounts stay unknown in the ledger. Contractor, invoices, date, funding account, transaction references and inclusion in a specific historical endpoint remain open. [Suncrest 262 ledger](../../archive/checkpoints/year848-suncrest262-finance-ledger.json) · [Day 160 ledger](../../archive/checkpoints/year851-day160-finance-ledger.json) · [Current ledger](../../state/finance-ledger.json)

The arena, land acquisition and retreat total 2,370 gp under three separate completed project records. The Briarstone Cottage repair rows `briarstone-repair-deposit-day158` (8 gp) and `briarstone-repair-final-day165` (18 gp) have their own property and scope. None of these five postings establishes the original expansion settlement. The reconciliation adds no payable, reserve, expense or cash deduction. [Day 160 chronicle](year851-day160-end-session.md) · [Cottage repair reconciliation](year848-day181-cottage-mana-reconciliation.md)

## Reconciled events and paid capital projects

Each amount below is in gp. All transaction IDs refer to existing entries. The two festivals and the observatory feast are distinct events.

| Event | Received | Paid | Result | Existing ledger references |
|---|---:|---:|---:|---|
| First Grand Dragon Festival | 4,336 | 3,110 | +1,226 | `general-tickets`, `premium-tickets`, `merchant-commission`, `lodging`, `stall-and-venue-fees`, `caravan-services`, `food-concessions`, `champion-prize-kaela`, `other-festival-expenses` |
| Permanent Ashvale Grand Arena | 0 | 1,750 | Paid, 0 outstanding | `arena-build` |
| Additional 20 acres from Merrick Vale | 0 | 280 | Paid, 0 outstanding | `land-registration` |
| Dragon Friendship Retreat | 0 | 340 | Paid, 0 outstanding | `retreat-build` |
| First monthly Ashvale Market Fair | 184 | 100 | +84 | `first-fair-receipts`, `first-fair-expenses` |
| Private Observatory celebration, Day 326 | 0 | 96 | Paid and closed | `observatory-feast-initial-payment` (70), `observatory-feast-final-settlement` (26, date unknown) |
| Year-end Grand Festival, Day 365 | 9,888 | 3,700 | +6,188 | Itemized below |
| Historical two-week Lodge report | 160 | 111 | +49 | `included_lodge_report`, marked already included in the Suncrest 262 endpoint |

The first festival’s 176 gp merchant commission was estate revenue. The paid 100 gp prize belongs to Kaela personally and is included in the 3,110 gp expense total. Vaeltharion, Aurelith and Tharosyn attended voluntarily. The first festival, all three capital payments and the first fair already reconcile to the Day 160 close: 2,133 + 1,226 − 2,370 + 84 = **1,073 gp**. [Day 160 chronicle](year851-day160-end-session.md) · [Historical ledger](../../archive/checkpoints/year851-day160-finance-ledger.json)

The completed and certified arena seats 1,200, comprising 800 general, 300 reserved and 100 premium seats. The 1,800-seat option remains unbuilt and uncertified. The 20-acre purchase brought Theron’s separately owned commercial estate from 120 to 140 acres. The retreat includes a private pavilion, strategy space and natural-form resting terraces for voluntary dragon visitors. These assets are noncash. Retreat income requires evidence of actual paying customers. [Arena](../../entities/locations/ashvale-grand-arena.md) · [Commercial estate](../../entities/locations/therons-commercial-estate.md) · [Retreat](../../entities/locations/dragon-friendship-retreat.md)

The player’s fair breakdown reconciles to the two existing aggregate rows. Receipts were 116 admission and reserved seating, 32 stall and venue fees, 18 commissions and 18 estate food services. Paid costs were 35 staff and security, 20 performers and instructors, 24 supplies and food, and 21 cleaning and arena maintenance. The monthly fair and annual festival schedule establishes planned frequency. Each further event and Lodge operating period needs its own evidence. [Day 160 chronicle](year851-day160-end-session.md) · [Lodge record](../../entities/locations/ashvale-lodge.md)

Both observatory payments share `event: private-celebration`. Their 96 gp total closes the feast with no revenue or remaining feast payable. Time Chamber and Observatory research and construction costs require their own evidence. [Day 1 chronicle](year852-day1-end-session.md#friends-family-and-celebrations) · [Observatory](../../entities/locations/observatory-of-first-light.md)

### Year-end festival entries

| Receipt ID | gp | Paid expense ID | gp |
|---|---:|---|---:|
| `year-end-general-tickets` | 3,900 | `year-end-security` | 620 |
| `year-end-reserved-tickets` | 2,900 | `year-end-medical` | 270 |
| `year-end-premium-tickets` | 1,500 | `year-end-food-supplies` | 720 |
| `year-end-registration` | 128 | `year-end-staff-referees` | 380 |
| `year-end-merchant-pitches` | 150 | `year-end-emberpears` | 360 |
| `year-end-camping-rentals` | 270 | `year-end-emberpear-nursery-stock` | 120 |
| `year-end-merchant-profit-share` | 300 | `year-end-entertainment` | 210 |
| `year-end-lodge-stays` | 240 | `year-end-advertising` | 130 |
| `year-end-food-concessions` | 500 | `year-end-camping-cleanup` | 240 |
| | | `year-end-dsi-logistics` | 150 |
| | | `year-end-maeryn-prize` | 100 |
| | | `year-end-utilities-staging` | 250 |
| | | `year-end-repairs` | 150 |
| **Receipts** | **9,888** | **Paid expenses** | **3,700** |

The festival’s 25% fee applies to 1,200 gp qualifying merchant profit and yields 300 gp to the estate. Merchant gross sales of 2,400 gp remain merchant property. The ordinary 22% commission does not also apply to those sales. Pitch, Lodge and concession receipts are already included. The 360 gp fruit supply and 120 gp nursery stock each appear once, and nursery receipts require an actual harvest and sale. [Day 1 chronicle](year852-day1-end-session.md#grand-festival-financial-ledger) · [Ledger](../../state/finance-ledger.json)

## Open financial verifications

- **20 gp gap — unresolved, no adjustment authorized.** The bridge compares the 1,073 gp Day 160 close with the 1,053 gp Day 326 opening. It remains unposted and unassigned. The separately recorded Day 196 `y848-d196-companion-compensation` paid Garrick and Nyx 20 gp, with independent purpose and provenance. The current played reconciliation is 1,053 − 96 + 6,188 = **7,145 gp provisional**. [Current bridge](../../state/finance-ledger.json#L31) · [Day 196 compensation](../../archive/checkpoints/year848-day196-finance-ledger.json#L214)
- **317 gp accounting documentation.** Closed in played continuity. The contractor, invoices, payee, date, paying account, posting references and historical endpoint coverage still need evidence.
- **Time Chamber.** Materials, research, labor, supplier invoices, energy, cooling, maintenance, repairs, prior payments and open obligations remain unverified. The feast is fully settled within its own scope.
- **Operating periods and allocation.** Missing Lodge, market, retreat and estate reports, earlier unexplained endpoint differences, current purse contents and account allocations remain open. A purse refill is a transfer with zero effect on total controlled cash. See the checkpoint’s [historical verification queue](../../state/open-verifications.md) for other open evidence.
- **Ownership and exclusions.** DSI’s treasury and student savings, restricted Stoneward coinage and unsold commercial instruments, Lyanna’s cash, disputed custody funds, merchant gross, unreconciled salvage, noncash property and separately held funds remain outside ordinary controlled cash. [Party finances](../../entities/mechanics/party-finances.md) · [Independent DSI ledger](../../state/dsi-finance-ledger.json)
