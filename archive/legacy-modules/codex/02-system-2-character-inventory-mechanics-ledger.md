# SYSTEM 2 — CHARACTER, INVENTORY & MECHANICS LEDGER

## 2.1 Frozen checkpoint: Day 46, 9:15 AM
| Field | Value |
|---|---|
| Character | Theron Ashvale / Blackscale, S+ |
| Location | Mount Vaelspire, with Vaeltharion and nearby companions |
| HP / MP / Defense | **100/100 · 376/400 · 26** |
| STR / DEX / CON / INT / WIS / CHA | **12 / 20 / 16 / 20 / 19 / 19** |
| Stat points | **0 unspent** |
| Chronos Eye / Dragon Slayer | Locked ~10% / Locked |
| Draconic Resonance | 1/5 |
| Staff/efficiency | 20% + 10% = 30% discount to ordinary spell costs, rounded up |
| Assimilation | +12 MP per uninterrupted 20 minutes, max 400 |
| Last full rest | Overnight Day 45→46, restored to 400; Junction I test spent 24 MP |
| Mental constructs | Raze analysis/simulation, Aegis defense; no free casting or mana |
| Physical state | HP full, no recorded injuries or fatigue at checkpoint |

## 2.2 Currency by owner — DO NOT POOL WITHOUT PERMISSION
| Holder | Gold | Silver | Equivalent gp |
|---|---:|---:|---:|
| Theron | 91 | 8 | 91.8 |
| Garrick | 95 | 8 | 95.8 |
| Nyx | 94 | 8 | 94.8 |
| Lyra | 92 | 8 | 92.8 |
| Shared expedition reserve | 120 | 0 | 120.0 |
| **Combined accounting total** | | | **495 gp 2 sp** |

Currency: 10 cp = 1 sp; 10 sp = 1 gp. Personal wealth belongs to that person. Custody/evidence gold and salvage stock are **not** automatically available spending money.

## 2.3 Equipment and material ownership
| Item | Quantity | Holder/location | Origin / limitations |
|---|---:|---|---|
| Black Dragon-Scale Runeblade | 1 | Theron | Aric's gift, legendary, 1d8+3 |
| White matched blade | 1 | Theron | Recovered in first dungeon investigation; provenance incomplete |
| Staff | 1 | Theron | 20% ordinary spell cost reduction |
| Oathbearer Token | 1 | Theron | Eighth Witness; no unlimited authority |
| Dragonveil Mask | 1 | Theron | Existing equipment, no invented powers |
| Previously gifted shed dragon scales | 3 | Theron | Distinct from Vaeltharion's research stock |
| Moonstones | 2 | Theron | Previously valued 10 gp each; valuation ≠ liquid coin |
| Empty crystal housing | 1 | Theron | No storage matrix, **0 stored MP** |
| Mana draughts | 0 | Theron | Do not spontaneously replenish |
| Unused mature shed scales | 40 | Vaeltharion's cavern | Permission for joint research; not Theron's personal loot |
| Unused small fragments | 122 | Vaeltharion's cavern | As above |
| Untouched elder scales | 7 | Vaeltharion's cavern | As above |
| Experimental reinforced scale | 1 | Vaeltharion's cavern | Constructed from 1 mature + 4 fragments; mana containment leaks |
| Supply wagon | 1 | Lower mountain camp | Salvaged Ashvale expedition wagon |
| Horses | Bracken, Morrow | Lower camp | Need feed, water, rest |

**Scale accounting:** Survey began 41 mature / 126 fragments / 7 elder. Prototype used 1 mature and 4 fragments, leaving 40 / 122 / 7 plus one prototype. The three previously gifted scales are a **separate** stock. No scales may be sold, removed or consumed beyond consent.

## 2.4 Party, animals and location/knowledge
| Actor | Last confirmed location | Status / independence | Known immediate focus |
|---|---|---|---|
| Garrick | Vaelspire cavern vicinity | Healthy; independent | Defense, logistics, wagon |
| Nyx | Vaelspire cavern vicinity | Healthy; independent | Scouting, Ember, information |
| Lyra | Vaelspire cavern vicinity | Healthy; independent | Healing, civilian care |
| Shade | With Theron | Bond 5/5 | Companion wolf |
| Ember | With Nyx | Bond 5/5 | Companion wolf |
| Alpha | Vaelspire vicinity | Independent Frostfang | May depart or patrol by choice |
| Vaeltharion | Hollow Veil sanctuary | Physically bound, consenting research partner | Protection and freedom |
| Lyanna | Blackthorn Watch, last verified | Safe at last report | Recovery, independent investigation |
| Caelan | Blackthorn Watch, last verified | Recovering, stable at last report | Healing, testimony |
| Aric | Ashvale Estate, at home with Theron’s mother | Former adventurer and A-rank swordsman; researching First Oath, Mirror Foundation and dragon lore | Knows the identity of the master smith he hired to forge the black Runeblade; knows the details of his own commission. Whether he knew of the white blade remains unknown. |

**Companion numerical HP/MP:** Prior earlier-session numbers (Lyra 38/38 MP80/80, Nyx 32/32 MP23/120, Garrick 42/42 MP60/60, Lyanna 36/36) are **historical**, not validated Day 46 values. Obtain the latest post-Day 10 updates before displaying current numerical values; do not silently assume unchanged.

## 2.5 Spell reference (current established ordinary costs)
| Spell | MP | Spell | MP |
|---|---:|---|---:|
| Frost Lance | 6 | Umbral Bolt | 7 |
| Rune Barrier | 9 | Minor Restoration | 11 |
| Spatial Step | 9 | Runic Edge | 6 |
| Ward Sense | 5 | Mental Probe | 13 |
| Mental Link | 9 | Controlled Memory Resonance | 11 |
| Mirror Mind | 6 | Vital Resonance | 14 |
| Arcane Disruption | 11 | Communication Spoof | 7 |
| Extended Spatial Transfer | 21 | Greater Rune Barrier | 28 |
| Veiled Memory Trace | 13 | Perceptual Interception | 7 |
| Dreamfall Mastered | 21 | Oath Sight | 8 |

Dreamfall: 20-ft radius, 60-ft range, DC18 mental save, caster chooses 1–30 min maximum, concentration, wake on damage/shaking/end concentration. Some major procedures have full-cost pricing and are **not** automatically eligible for ordinary discount. Costs for new spells must be stated before casting and logged.

## 2.6 Skill progression
**Mastered:** Mental Magic 5/5; Advanced Runecrafting 5/5; Independent Dual-Mind 3/3; Spirit Mana Assimilation 5/5; Mana Efficiency 5/5; Guardian Interposition 3/3; Dual-casting 5/5; Sacred Healing Theory 3/3; Mana Siphoning 5/5.  
**Locked:** Chronos Eye (~10% research), Dragon Slayer; no draconic essence accepted.  
**Progress updates:** `skill | old progress | training/trial | time | MP/materials | roll/DC | new progress | ability unlocked?`.

## 2.7 Transaction and action ledger schema
`EVENT-ID | in-world timestamp | actor | action | starting HP/MP/gp/items | declared cost | check and consequence | ending HP/MP/gp/items | witness/source`
Example, already played: `ACT-046-001 | D46 08:45–09:15 | Theron | isolate/restore Junction I | 400 MP | 24 MP | 19+5=24 vs DC22; stable | 376 MP | campaign scene`. **Example is a record, not a new action.**

---

