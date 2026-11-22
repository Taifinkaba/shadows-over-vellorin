---
id: ancient-dragons-encounter-sheets-proposal
type: mechanics
status: research
visibility: gm-reference
source_refs:
  - entities/creatures/vaeltharion.md
  - entities/creatures/aurelith.md
  - entities/creatures/tharosyn.md
  - entities/mechanics/theron-skills.md
  - entities/mechanics/theron-abilities.md
  - entities/mechanics/magic-and-combat-integration.md
  - governance/precedence.md
---

# Ancient Dragons — proposed full tactical, magical and character sheets v2

**STATUS: DESIGN PROPOSAL, NOT APPROVED CANON.** Canon: Vaeltharion is a free ancient black-steel/silver-frost dragon, DSI cofounder, first dragon exhibition champion, zero coercive chains and seven protective anchors retained. Aurelith is the independent ancient silver Keeper of Silverwake, third in the friendly exhibition. Tharosyn is the independent ancient bronze Thunder Archivist of Stormvault, fourth in that friendly exhibition. Each is Theron's friend with an independent will. Festival placements measure that **one consensual exhibition**, not universal power rankings. Neither individual age in years, gender, actual HP, actual MP, complete skill list, hidden history nor a full-power result is presently authenticated in the creature records.

All **numbers, spell titles, combat effects, resistance types, secondary breath types, innate casting, skill modifiers and action economy below are PROPOSED**. They are a balanced ruleset for future approval, NOT claims Theron already witnessed these powers. Public repo proposals are out-of-character; Raze must not mine these for in-world knowledge. Do NOT overwrite the three canon creature entries until player approval. GM should preserve room for each ancient's undiscovered arts instead of declaring these their total possible abilities. Dragon Slayer, Chronos Eye and no-essence state remain LOCKED.

## Core proposed combat engine

- **Scale**: local 5e-inspired rounds of 6 seconds, feet on a grid, d20 initiative (DEX modifier), d20 attack vs AC, d20 save vs DC, damage dice, hit points, conditions. Meet AC/DC succeeds. Natural 1 attack misses and natural 20 attack hits and doubles damage dice only. This is a NEW optional engine.
- **Important Theron compatibility issue**: his 46 base / 49 bracers / 51 with Night Sovereign values are campaign DEF, **not automatically d20 AC**; no d20 attack using those numbers until player approves a translation. Don't strip or reduce his approved DEF. Proposed alternate future bridge to review: keep DEF as separate existing damage/defense mechanic and introduce a player-approved AC or attack-resolution formula after testing. Do not calculate win probabilities now.
- On each turn one action, move up to speed, one reaction until next turn. Multiattack consumes action; cast spell consumes action unless explicitly tagged **bonus action**. Dragons get one bonus action/turn. One concentration effect/dragon at a time; if damaged while concentrating, CON save DC max(10, floor(damage/2)); failure ends the spell. A concentration effect ends on incapacitation. Dispel attempts use existing spells only; none are universally irresistible.
- Each dragon starts at 3 **legendary-action points per round**, restored at the start of its turn, spent at the end of **another** creature's turn; at most one choice at any single end-of-turn; not usable while incapacitated. Legendary actions NEVER cast spells unless specifically listed and priced in MP. All listed options spend their exact points.
- **Breath**: 1 initial use, then d6 at start of dragon's turns while depleted: 5–6 recharges. Breath is a physical/innate feature with its own recharge, not an MP spell. If a spell imitates a breath, it costs MP. Only one breath attack per action.
- **Legendary resistance** 3/day per dragon (PROPOSED): when failing a save, may expend one to succeed; never recharges during combat. This does not confer blanket magical immunity or prevent voluntary restraint.
- **Magic** uses independent **finite personal dragon MP** shown below, not Theron's, not their sanctuaries', and not any historical seven anchors. Every listed spell uses its exact MP (no free discounted casts). No MP regain in combat; **proposed** recovery only after 8 hours actual uninterrupted rest at a suitable place, 1/long rest, and the GM must record whether conditions were met. Healing spells explicitly specified; no implicit regeneration. A dragon cannot use magic if insufficient MP.
- Movement costs, line of sight, known targets and ordinary cover matter. Saving throw success halves damage, rounded down, unless entry specifies no effect. On a hit, an attack applies damage; saving throw effects do not auto-hit. Resistance halves after the save; immunity zero. No unlisted resistance. **Frightened**: creature cannot willingly move closer and has disadvantage on attacks while source visible; re-save as described.
- **Grappled**: speed 0; escape as action with Athletics/Acrobatics d20 vs listed DC. **Restrained**: speed 0; attacks against target advantage and its attacks disadvantage; DEX saves disadvantage. **Prone**: half movement to stand; close melee attacks advantage, ranged attacks disadvantage.
- All attacks below use dragons' proposed + to hit. Breath/DCs are specific; damage on a successful save is half unless specified. Proposed 1/short rest abilities recharge after **1 hour of actual uninterrupted rest**, where listed; per-day powers after the proposed 8-hour rest. This does not silently recharge historical character resources.
- **No forced sparring**: Dragons can decline, retreat, negotiate, switch to nonlethal training or set safety boundaries. Do not treat simulated victories as canon. Collateral damage possible. Genuine dragon combat is extremely dangerous even for an S+ rank Level 5 character. Rank is not a conversion to monster CR or new SS rank.
- **Encounter procedure**: announce visible tells; roll initiative, attack, save, damage, movement, recharge, legendary choices and MP costs; track each round and status. If the player chooses a controlled spar, set specific stop conditions, suppress lethal damage by consent and apply tracked injuries only. Do not declare whole combat sequences as automatically won.

## 1. VAELTHARION — The Black-Steel Sovereign

**CANON**: Ancient black-steel and silver-frost dragon with amber eyes, free guardian of Hollow Veil, seven protective anchors and zero coercive chains; voluntary academy cofounder and first friendly exhibition champion. Actual elemental skills remain unknown. **Theme of proposed spells**: unyielding steel, silver frost, guardianship, protective runes and battlefield denial — **NOT time magic simply because of a mysterious history**.

### Proposed character sheet
- Size Gargantuan, age unknown, alignment independent, exact formal rank/CR/XP UNKNOWN. HP **620/620**, AC **25**, MP **480/480**, initiative **+2**, proficiency-equivalent **+8**.
- Attributes STR 30 (+10), DEX 14 (+2), CON 28 (+9), INT 24 (+7), WIS 22 (+6), CHA 24 (+7).
- Saves STR +18, DEX +10, CON +17, INT +15, WIS +14, CHA +15. Skills Athletics +18, Perception +22, Insight +14, Arcana +15, History +15, Intimidation +15. Passive Perception 32.
- Speed 40 ft, fly 90 ft; burrow/swim UNKNOWN. Blindsight 60 ft, darkvision 120 ft. Converses with Theron; other languages unverified.
- **Proposed** damage resistances cold, nonmagical slashing; no proposed damage immunities. Condition immune frightened only. Vulnerabilities UNKNOWN. Three legendary resistances/day. No innate permanent regeneration.
- **Action — Multiattack**: 1 bite and 2 claws (all three rolled separately).
- Bite +18, reach 15 ft, **3d10+10 piercing**. Claw +18, reach 10 ft, **2d10+10 slashing**. Tail +18, reach 20 ft, **2d12+10 bludgeoning**; Huge or smaller target DC 25 STR or prone.
- **Silver-Frost Breath** (action, recharge 5–6): cone 90 ft, DC 25 CON, **16d8 cold**, half on save; failed save also reduces speed by half through end of victim's next turn. This is proposed magic/biology, not evidenced by his colors alone.
- **Iron-Mantle Presence** (action, 1/short rest): hostile creatures of his choice within 60 ft, DC 23 WIS or frightened until end of next turn, then end; no forced mind control.
- **Reaction — Guarded Pivot** (1/round): when creature within 20 ft leaves reach, tail attack against it if able to react.
- **Legendary**: Appraise (1 point, make Perception or Insight check); Tail (1, one tail attack); Wing Reposition (2, fly up to 40 ft, creatures within 10 ft DC 25 DEX or **2d8 bludgeoning and prone**, success half damage and no prone).
- **Battle intelligence**: denies exits, layers cover, patiently tests repeated patterns. Defensive guardian will value allies' safety and may withdraw to preserve protected space.

### PROPOSED spell catalogue (MP paid, casting action unless stated)
| Magic ability | MP | Range / duration | Mechanics / limits |
|---|---:|---|---|
| Frostbrand Spear | 16 | 120 ft, instantaneous | +15 spell attack, **4d10 cold**, hit reduces speed 10 ft until next turn (minimum 0). |
| Steelhide Ward | 24 | Self, 3 rounds, concentration | +2 AC, does not stack with other AC-granting dragon spells. |
| Glacial Chains | 32 | 90 ft, up to 1 min, concentration | DC 23 STR; failure restrained by conjured ice, target repeats save end of turn; no damage. |
| Silver Bastion | 44 | 30-ft radius centered within 90 ft, 3 rounds, concentration | Covering ward grants chosen allies **resistance to one declared damage type: cold or bludgeoning** while inside; does not block all attacks. |
| Black-Steel Grasp | 28 | 60 ft, instantaneous | DC 24 STR; fail **5d8 bludgeoning** and pulled 20 ft toward chosen clear space, success half and no pull. |
| Winterfront | 48 | 60-ft cone, instantaneous | DC 24 CON, **8d8 cold**, half on success. Separate MP spell; does not alter breath recharge. |
| Guardian Intercession | 20 | 60 ft, reaction | When a visible ally takes damage, reduce that one instance by **3d10+10**, to minimum 0; one reaction/round. |
| Cold-Star Prison | 70 | 120 ft, up to 3 rounds, concentration | One Huge-or-smaller target DC 25 STR or restrained in 20-ft ice sphere; repeat save at end of each turn; sphere AC 20, 60 HP, breakable. |
| Frostveil Passage | 18 | Self, bonus action, instantaneous | Fly or walk 30 ft to visible unoccupied space along valid path, **not teleportation**; does not cross walls or wards. |
| Sanctuary Mend | 52 | Touch, action | One living creature heals **6d10+15 HP** up to its normal maximum; no resurrection or MP restoration. |

**Proposed magic proficiency** +15; listed save DCs override other calculations. Example full-power spell choices trade physical Multiattack and breath for one cast; defensive reaction competes with Guarded Pivot. **No full dragon magic is revealed to Theron until observed or voluntarily taught.**

## 2. AURELITH — Keeper of Silverwake

**CANON**: Ancient independent silver dragon, historical scholar/strategy-game partner, third in one friendly exhibition. **Theme of proposed spells**: moonlit silver, protection, reflection, restorative light, illusion and careful control; not an automatically benevolent universal pacifier.

### Proposed character sheet
- Gargantuan, age/CR/XP unknown. HP **550/550**, AC **24**, MP **560/560**, initiative **+4**, proficiency-equivalent +8.
- STR 28 (+9), DEX 18 (+4), CON 26 (+8), INT 28 (+9), WIS 26 (+8), CHA 26 (+8).
- Saves STR +17, DEX +12, CON +16, INT +17, WIS +16, CHA +16. Skills Perception +24, Insight +24, Arcana +17, History +17, Persuasion +16. Passive Perception 34.
- Speed 40 ft, fly 90 ft, swim 40 ft (proposed). Blindsight 60 ft, darkvision 120 ft. Additional language knowledge unknown.
- Proposed resistance cold and radiant; condition immune frightened; no blanket mind immunity. Legendary resistance 3/day.
- Multiattack bite +17 **3d10+9 piercing**, two claws +17 **2d10+9 slashing** each. Tail +17, 20 ft, **2d12+9 bludgeoning**.
- **Moonfrost Breath** (action, recharge 5–6): cone 90 ft, DC 24 CON, **14d8 cold**, half on success; failed save also can't take reactions until end of next turn.
- **Disarming Mist Breath** (action, consumes same breath charge): cone 60 ft, DC 24 CON, on failure target's speed 0 until end of next turn, success no effect. Deals 0 damage; cannot use both breaths on the same charge.
- **Reaction — Measured Deflection** (1/round): +3 AC against one announced incoming attack, before it resolves; only for that attack.
- **Legendary**: Read Intent (1, Insight check), Tail (1, tail attack), Gliding Withdrawal (2, fly up to 40 ft without triggering opportunity attacks).
- **Battle intelligence**: defends allies, anticipates feints, uses reversible control over lethal force; can choose diplomacy or refusal.

### PROPOSED spell catalogue
| Magic ability | MP | Range / duration | Mechanics / limits |
|---|---:|---|---|
| Moonbeam Lance | 18 | 150 ft, instantaneous | +17 spell attack, **5d8 radiant**, no guaranteed blindness. |
| Mirrorwake Image | 28 | Self, 3 rounds, concentration | First attack against Aurelith each round has disadvantage; images not extra creatures or attackers. |
| Silver Reprieve | 36 | 90 ft, reaction | When a visible ally is hit, reduce one damage instance by **5d10**, to minimum 0; competes with Measured Deflection. |
| Lunar Binding | 38 | 90 ft, up to 1 min, concentration | DC 24 WIS or speed 0 and unable to take reactions; repeat end turn; no domination. |
| Clarifying Radiance | 26 | 30-ft radius within 90 ft, 3 rounds, concentration | Suppresses nonmagical concealment in area and grants allies +2 on Perception checks; no universal true sight or hidden-memory access. |
| Silverwake Restoration | 58 | Touch, action | One living creature heals **8d10+15 HP** up to maximum, no resurrection or curse removal unless separately certified. |
| Tranquil Circle | 42 | 30-ft radius within 90 ft, 3 rounds, concentration | Creatures chosen by Aurelith DC 24 WIS or cannot make opportunity attacks; repeat save at end of turns; attacks and agency otherwise intact. |
| Crescent Shield | 30 | Self or creature within 60 ft, 3 rounds, concentration | Target gains +2 AC; cannot stack with other dragon AC spells. |
| Moonlit Crossing | 24 | Self, bonus action, instantaneous | Move up to 40 ft along a valid unobstructed path without opportunity attacks; **not teleportation**. |
| Gentle Revelation | 34 | Touch, 1 minute, concentration | Reveals mundane ink alterations and surface inscriptions on a single object; magical forgery and truth of content **not** automatically authenticated. |

**Magic proficiency** +17, specified DC 24. Aurelith's larger finite MP supports more control/defensive casts, offset by somewhat lower HP and brute force than Vaeltharion. No in-world player knowledge until revealed.

## 3. THAROSYN — Thunder Archivist of Stormvault

**CANON**: Independent ancient bronze dragon, Stormvault's Thunder Archivist, strategic-game partner, fourth in one friendly exhibition. **Theme of proposed spells**: thunder, lightning, stormcraft, mobility and archival resonance. No fabricated power over all weather, history or memory.

### Proposed character sheet
- Gargantuan, age/CR/XP unknown. HP **590/590**, AC **24**, MP **500/500**, initiative **+5**, proficiency-equivalent +8.
- STR 30 (+10), DEX 20 (+5), CON 27 (+8), INT 26 (+8), WIS 22 (+6), CHA 22 (+6).
- Saves STR +18, DEX +13, CON +16, INT +16, WIS +14, CHA +14. Skills Perception +22, Athletics +18, Arcana +16, History +16, Investigation +16. Passive Perception 32.
- Speed 40 ft, fly 100 ft, swim 40 ft (proposed). Blindsight 60 ft, darkvision 120 ft. Other languages unknown.
- Proposed resistance lightning and thunder; condition immune frightened; no blanket elemental immunity. Legendary resistance 3/day.
- Multiattack bite +18 **3d10+10 piercing**, two claws +18 **2d10+10 slashing** each. Tail +18, reach 20 ft, **2d12+10 bludgeoning**.
- **Stormline Breath** (action, recharge 5–6): 120-ft line, 10 ft wide, DC 25 DEX, **16d8 lightning** half on success.
- **Rolling Thunder Breath** (action, consumes same breath charge): 60-ft cone, DC 25 CON, **8d8 thunder** half on success; failed save also pushed 20 ft to clear space (no automatic cliff fall). Cannot use both on one charge.
- **Reaction — Counterstep**: when a creature within reach misses him, move 15 ft without opportunity attacks (1/round).
- **Legendary**: Read Battlefield (1, Perception check), Tail (1, tail attack), Thunder Rush (2, move up to 30 ft and make one Claw attack).
- **Battle intelligence**: rapid positional pressure, breaks static defenses, changes pace; can elect investigation/dialogue over force.

### PROPOSED spell catalogue
| Magic ability | MP | Range / duration | Mechanics / limits |
|---|---:|---|---|
| Arc Lightning | 22 | 120 ft, instantaneous | +16 spell attack, **5d10 lightning** to one target, no automatic chaining. |
| Thunderclap Burst | 30 | 20-ft radius within 90 ft, instant | DC 24 CON, **6d8 thunder** half on save; failed save also pushed 10 ft to safe unoccupied space. |
| Stormwake Mantle | 38 | Self, 3 rounds, concentration | +2 AC and 10 lightning damage to first creature each round that hits him from within 10 ft; no stacking AC bonuses. |
| Gale Breaker | 32 | 90 ft, instantaneous | DC 24 STR; failure target pushed up to 30 ft along clear line, success no effect; no forced movement through walls. |
| Lightning Lattice | 44 | 60-ft line within 120 ft, up to 3 rounds, concentration | Area becomes dangerous ground; first time a creature enters on a turn DC 24 DEX or **4d8 lightning**, success half; damage at most once per creature per turn. |
| Thunderstep Surge | 28 | Self, bonus action, instantaneous | Fly/move 50 ft along valid unobstructed path without opportunity attacks; **not teleportation**. |
| Storm Archivist's Sight | 22 | Touch, up to 10 min, concentration | Examines visible scorch, wind and lightning traces to infer event direction; no omniscient replay or authenticated personal identity. |
| Resonant Breaker | 46 | 90 ft, instantaneous | +16 spell attack against one object or ward, **7d8 thunder**; affects barriers according to their real HP/resistance, cannot auto-dispel wards. |
| Thunder Ward | 26 | 60 ft, reaction | Reduce lightning or thunder damage to one ally by **4d10+10** (min 0), or reduce bludgeoning damage by **2d10** instead; one reaction. |
| Eye of the Storm | 62 | 30-ft radius centered within 120 ft, up to 3 rounds, concentration | Heavy wind imposes disadvantage on ranged **nonmagical** attacks passing through; flying creatures beginning turn inside DC 24 STR or move only half flight speed that turn. No total flight prohibition. |

**Magic proficiency** +16; listed DC 24 unless breath DC 25. Tharosyn is fastest, emphasizes momentum and area control but has no free infinite storms.

## Comparison / balance rationale

| Proposed feature | Vaeltharion | Aurelith | Tharosyn |
|---|---:|---:|---:|
| HP | 620 | 550 | 590 |
| AC | 25 | 24 | 24 |
| MP (finite) | 480 | 560 | 500 |
| Fly ft | 90 | 90 | 100 |
| Highest save DC (breath) | 25 | 24 | 25 |
| Main breath damage | 16d8 | 14d8 | 16d8 |
| Legendary resistances/day | 3 | 3 | 3 |
| Legendary points/round | 3 | 3 | 3 |
| Distinct spell choices | 10 | 10 | 10 |
| Primary combat identity | Defensive powerhouse / control | Strategist / wards / restoration | Mobility / disruptive storms |

- Proposed relative strengths are **situational**, not a ranking; the friendly exhibition finish is respected historically, not enforced by stat bias.
- These are boss-tier ancient dragons, not fair solo Level 5 opponents. HP and damage are intentionally far above Theron's 100 HP; use staged partial-power exercises with clear limits, never covertly pit him against full power.
- Magic uses an Action; therefore a dragon cannot simultaneously use Breath, Multiattack and Action spell on one turn. Legendary attacks occur between turns only and use points. MP pools cannot replenish silently midfight.
- Proposed rest resets listed per-day abilities and MP after the specified actual 8-hour conditions only; no free staff, Theron, wagon or sanctuary recharge.
- The full catalogue is the **known-to-GM drafted encounter repertoire**, not necessarily every spell the dragon has ever learned. Unknown advanced magical disciplines remain UNKNOWN; do not invent a new power in the middle of a fight to force an outcome.
- Possible environmental lair advantages (Hollow Veil, Silverwake, Stormvault) are **not specified or enabled**. Add only after separate grounds, budget and risk rulings; seven Vaeltharion anchors do not become additional combat charges.
- **Non-combat competencies (proposed skill uses):** Vaeltharion sanctuary stewardship and protection; Aurelith historical scholarship and discernment; Tharosyn archive investigation and storm reading. Skills are check modifiers, not automatic success.
- **Weaknesses** remain individual and UNVERIFIED; don't assume elemental opposites confer double damage.

## Encounter ledger format (required for adoption)

Date/time, arena or territory; actual participants and consent; full or restricted-power setting; starting HP/MP/charges for each; Theron's full equipped loadout/DEF and separately approved AC resolution; initiative and rolls; round; action/reaction/legendary expenditures; MP and breath recharge die; attack/damage/save/mitigation; movement, conditions, concentration saves; collateral, healing, consent withdrawal; injuries, end condition; observed information available to Raze; payments, earned progress and next checkpoint.

## Adoption gates / pending explicit approval

1. Player approves revised stats, magic catalogue and rules **as prospective rules**.
2. Player and GM settle Theron's DEF-versus-AC d20 resolution **without retroactively nerfing existing 46/49/51 DEF**.
3. Define controlled spar's finite power fraction, allowable injuries and stop conditions with participants before dice.
4. Keep historic dragon powers, histories, original sword origins, essence transfer and Dragon Slayer unlock unknown unless witnessed or authenticated.
