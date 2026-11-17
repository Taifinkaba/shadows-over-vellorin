---
id: magic-and-combat-integration
type: mechanics
status: canon
visibility: gm-reference
source_refs:
- changes/chronicles/phase2-08-magic-combat-approval.md
- entities/mechanics/theron-spells.md
- entities/mechanics/theron-abilities.md
- entities/mechanics/theron-skills.md
- archive/legacy-modules/world/02-2-rules-of-the-world.md
---

# Magic, combat and Phase 2 integration

Approved public classification/procedure only. Spell, item, creature, progression and current resource owners remain authoritative. No new spell, usable opponent, secret outcome or gameplay action is created.

```json
{
  "schema_version": 1,
  "classification": "APPROVED INTEGRATION DESIGN",
  "approval_source_ref": "changes/chronicles/phase2-08-magic-combat-approval.md",
  "authority_refs": {
    "spells": "theron-spells",
    "abilities": "theron-abilities",
    "skills": "theron-skills",
    "story_mode": "story-mode",
    "travel": "travel-procedure",
    "settlements": "settlement-services",
    "communications": "settlement-communications",
    "law": "justice-and-jurisdiction",
    "guilds": "guild-membership-and-contracts",
    "dungeons": "dungeon-design-proposals",
    "monsters": "dungeon-ecology-and-hazards",
    "exploration": "dungeon-exploration",
    "economy": "economy-accounting",
    "property": "property-financial-references",
    "autonomy": "npc-autonomy-and-time",
    "events": "world-event-references",
    "quests": "quest-continuation-and-completion",
    "ledger": "state/finance-ledger.json",
    "checkpoint": "state/checkpoint.json"
  },
  "schools": [
    {
      "id": "school:elemental",
      "name": "Elemental Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Frost Lance",
        "Frost Veil",
        "Glacial Step",
        "Rime Snare"
      ],
      "principles": "Bounded manipulation of established elemental effects; the current catalog specifically supports cryomancy. Fire, water, wind and earth are classification families, not newly learned spells.",
      "applications": "Use only sourced ice attack, brief concealment, foothold or restraint scopes. Existing effects do not create unlimited matter, breathable air or permanent terrain.",
      "resource_requirements": "Finite verified caster/pool, stated cost and any existing materials/environmental requirements; no energy extraction loop.",
      "training": "Prerequisites, supervised safe practice and actual trial evidence; cryomancy specialization is distinct from mastered core skills.",
      "casting_constraints": "Verify range, line of sight, duration, target, footing and concentration where required; undocumented elemental modes remain unavailable.",
      "failure_conditions": "Interruption, resistance, unsuitable footing, intervening cover or insufficient resources can prevent intended results; no automatic weakness multiplier.",
      "defensive_interactions": "Existing barriers, cover and environmental constraints apply; no universal fire/ice cancellation or immunity is granted.",
      "ethical_legal_limits": "Protect bystanders, buildings, lawful resource rights and consent; actual jurisdiction and collateral consequences require review.",
      "unresolved": "Exact non-ice spell repertoire, many effect/damage values and elemental interaction formulas remain UNKNOWN."
    },
    {
      "id": "school:restoration",
      "name": "Restoration Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Minor Restoration",
        "Deep Restoration",
        "Regenerative Weave",
        "Master Restoration Weave"
      ],
      "principles": "Sourced finite healing operates within living physiology, established spell scope and actual treatment conditions.",
      "applications": "Distinguish stabilization, physical healing and condition treatment; none is resurrection or automatic restoration of mana.",
      "resource_requirements": "Use established listed costs and full-cost exceptions; no unlimited HP, universal cure or free item/ally refill.",
      "training": "Sacred Healing Theory and Maternal Healing Mastery retain their original tracks and actual training evidence.",
      "casting_constraints": "Check living target, injury/condition, willingness, access, casting requirements and specific treatment limits before application.",
      "failure_conditions": "Unsupported condition, interruption, lack of access, resistance or insufficient resources can limit treatment; outcome is not guaranteed.",
      "defensive_interactions": "Protection or resistance must come from established target/spell rules, never assumed immunity or automatic ward penetration.",
      "ethical_legal_limits": "Respect consent, competent practice, patient autonomy and applicable law; incapacitation does not transfer ownership or legal rights.",
      "unresolved": "Exact HP restored, treatment of unspecified injuries and two supplied but unlocated spell references remain unresolved; no resurrection is introduced."
    },
    {
      "id": "school:runecraft",
      "name": "Runecraft",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Rune Barrier",
        "Greater Rune Barrier",
        "Runic Edge",
        "Ward Sense"
      ],
      "principles": "Prepared inscriptions and established rune/ward effects depend on knowledge, materials, construction, activation and finite power.",
      "applications": "Reference classification of existing rune/ward names only; no expanded detection, damage or protection scope follows from a school label.",
      "resource_requirements": "Identify material provenance, item owner, verified activation cost/source and remaining charge; independent reservoirs are not pooled.",
      "training": "Advanced Runecrafting mastery does not complete separate engineering/wearable specializations or unfinished systems.",
      "casting_constraints": "Follow the particular preparation, placement, contact, trigger and concentration requirements actually supported by the owner.",
      "failure_conditions": "Damaged construction, missing material/knowledge, exhausted charge or unverified trigger may prevent operation.",
      "defensive_interactions": "Wards interact only within established tested scope; no permanent unlimited barrier, universal dispel or arbitrary anti-magic field.",
      "ethical_legal_limits": "Owner consent, lawful installation, safe materials and construction/payment evidence remain necessary.",
      "unresolved": "Unspecified construction stages, trigger details, recharge rates, staff subsystems and numerical ward interactions remain UNKNOWN."
    },
    {
      "id": "school:mental",
      "name": "Mental Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Mental Probe",
        "Dreamfall Mastered",
        "Mirror Mind",
        "Mental Link"
      ],
      "principles": "Mental effects are bounded interactions with actual targets, memory, attention and supported channels, not omniscience.",
      "applications": "Use existing probe, sleep/dream and mental-reference scopes; a name such as Mirror Mind grants no undocumented protection rule.",
      "resource_requirements": "Pay the verified cost once from an authorized finite pool; mastery supplies no free interrogation or remote information.",
      "training": "Mental Magic mastery and dual-mind/dual-casting tracks remain independent of new spells, immunity or unrestricted simultaneous concentration.",
      "casting_constraints": "Preserve Dreamfall range/area/selectable duration, concentration and waking rules; verify consent, resistance and target limits for other effects.",
      "failure_conditions": "Resistance, incomplete/false memory, target unavailability, interruption or waking can end or limit an effect; do not fabricate hidden knowledge.",
      "defensive_interactions": "Existing mind protection and saves apply only where sourced; no blanket immunity, irresistible probe or automatic truth detection.",
      "ethical_legal_limits": "Consent, privacy, lawful investigative authority, due process and independent agency remain material constraints.",
      "unresolved": "Unspecified protective formulas, memory completeness, other ranges/durations and outcomes remain UNKNOWN."
    },
    {
      "id": "school:spatial",
      "name": "Spatial Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Spatial Step",
        "Extended Spatial Transfer"
      ],
      "principles": "Sourced relocation is a particular constrained spell, not general permission to ignore geography or containment.",
      "applications": "Use only existing movement modes and verified destinations; no new teleport anchor or destination is created.",
      "resource_requirements": "Verify cost, caster/item pool, preparation and target/load restrictions; travel consumes actual resources and time where required.",
      "training": "Existing learned spells do not establish new range, mass capacity, mass transport or portal engineering.",
      "casting_constraints": "Honor prepared-anchor requirements wherever the original mode requires them; verify which mode, destination, lawful access, physical conditions and wards apply.",
      "failure_conditions": "Unprepared/unknown destination, spatial ward, unsafe receiving conditions, insufficient resources or interruption may block use.",
      "defensive_interactions": "Established spatial barriers/containment require their actual supported resolution; no universal bypass or invented opposed-roll formula.",
      "ethical_legal_limits": "Property access, custody, passenger consent and applicable jurisdiction still apply; magic is no search warrant.",
      "unresolved": "Full original anchor specifications, ranges, carried mass, ward interactions and unverified destinations remain unresolved."
    },
    {
      "id": "school:temporal",
      "name": "Temporal Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [],
      "principles": "Temporal classification distinguishes observed phenomena and independent beings from accessible player abilities.",
      "applications": "Chronos Eye remains locked; Shattered Meridian anomalies are proposed environmental designs, not time travel or player powers.",
      "resource_requirements": "No temporal energy supply, rewind budget, automatic foresight or free repeat attempt is established.",
      "training": "Chronal Theory and approximately19% Chronos Eye development do not unlock the ability; Dragon Slayer remains separately locked.",
      "casting_constraints": "Use only explicitly established voluntary finite interactions; no temporal casting procedure or future sight is added.",
      "failure_conditions": "Lack of an established ability is a hard limitation, not a roll for a new power; anomaly outcomes remain unknown.",
      "defensive_interactions": "No immunity, time stop, universal temporal defense or reversal of damage/death is granted.",
      "ethical_legal_limits": "Preserve autonomy, chronology, permanent-death rules and original protective covenants; no coercion of an independent being.",
      "unresolved": "No active temporal spell catalog or usable Shattered Meridian numerical anomaly package is established."
    },
    {
      "id": "school:spirit",
      "name": "Spirit Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [],
      "principles": "Spirit-related classification preserves independent consenting entities and the established personal mana assimilation process.",
      "applications": "Spirit Mana Assimilation II has its sourced personal recovery behavior; Caelrix remains voluntarily bonded and independent.",
      "resource_requirements": "24 personal MP per complete uninterrupted10minutes with usable ambient source and concentration, capped at current personal maximum; no actual recovery occurs here.",
      "training": "Existing mastery and observed trials remain unchanged; no new bonds, activation, essence acceptance or progression follows.",
      "casting_constraints": "Check uninterrupted conditions and the actual source; Raze analysis, Aegis defense, staff, wagon and allies create no free personal mana.",
      "failure_conditions": "Interrupted concentration, unusable ambient source or lack of willingness/support prevents an unsupported recovery or interaction.",
      "defensive_interactions": "Established protective functions remain limited; no automatic spirit control, possession defense, resurrection or unlimited shielding.",
      "ethical_legal_limits": "Independent spirit consent and established covenant restrictions remain binding; a bond is not ownership.",
      "unresolved": "Unspecified energy sources, recharge intervals and unfinished equipment functions remain UNKNOWN."
    },
    {
      "id": "school:shadow",
      "name": "Shadow Magic",
      "classification": "REFERENCE CLASSIFICATION",
      "spell_owner_ref": "theron-spells",
      "ability_owner_ref": "theron-abilities",
      "existing_spell_names": [
        "Umbral Bolt",
        "Umbral Murmur",
        "Shadow Mantle",
        "Phantom Procession"
      ],
      "principles": "Existing shadow effects shape supported concealment, sound or appearance within their recorded limits.",
      "applications": "Use sourced bolt, displaced whisper, dim-light mantle and non-damaging duplicates; intimidation is an attempt, not mind control.",
      "resource_requirements": "Use the existing costs without another discount; rehearsed combinations are not free spells or new mana pools.",
      "training": "Shadowcraft/Stealth and Dread Arts specializations retain actual progress; no automatic fear or concealment mastery is granted.",
      "casting_constraints": "Follow each existing light, range, duration, number and concentration limit; dual-casting mastery alone permits no new stacking.",
      "failure_conditions": "Visibility, observation, disbelief where supported, resistance, interruption or finite resources can frustrate the intended outcome.",
      "defensive_interactions": "Existing senses, light, cover and wards require actual resolution; no automatic invisibility, silence, fear or immunity.",
      "ethical_legal_limits": "Stealth and intimidation remain subject to consent where relevant, proportionate conduct, property law and due process.",
      "unresolved": "Undocumented damage, detection/save formulas and interactions stay unresolved; no new terror power is introduced."
    }
  ],
  "combat_procedures": [
    {
      "id": "combat:initiative-action-order",
      "procedure": "Use an established scene-specific order and declare it before resolution. A universal initiative roll, action economy and tie-breaker are not established by the retrieved owners; do not invent one."
    },
    {
      "id": "combat:movement",
      "procedure": "Track actual distance, terrain, mode, access and line of sight. No universal feet-per-round, flight, underwater mobility or teleport destination is added."
    },
    {
      "id": "combat:attacks",
      "procedure": "Declare objective, eligible target, range/sight, supported modifier/DC or other established resolution, costs and plausible consequences before a dangerous roll. The sourced d20+relevant modifier versus declared DC is not a new universal attack-vs-DEF formula."
    },
    {
      "id": "combat:defense",
      "procedure": "Use original defense/equipment owners and condition/activation evidence: normal equipped49, conditional51 only if Night Sovereign is worn. Current wearing remains UNKNOWN; DEF is not silently reinterpreted as armor class or damage reduction."
    },
    {
      "id": "combat:damage",
      "procedure": "Use only a documented weapon/spell/hazard damage rule. No universal damage, critical-hit, resistance, rank-scaling or HP-at-zero formula fills missing mechanics."
    },
    {
      "id": "combat:healing",
      "procedure": "Respect living target, exact sourced cost, condition/scope, consent and limitations. Stabilization, condition care and HP healing are separate; no automatic resurrection, full heal or mana restoration."
    },
    {
      "id": "combat:spellcasting",
      "procedure": "Identify known spell, governing revision, verified cost, eligible finite pool, target, range/duration and any material/preparation. Preserve listed costs while repricing is unresolved; no automatic school-based grant."
    },
    {
      "id": "combat:concentration",
      "procedure": "Track the specific effect and its interruption/end conditions. Preserve Dreamfall and other sourced constraints; dual-mind/dual-casting mastery alone adds no universal concentration slot, saving throw or new stack."
    },
    {
      "id": "combat:status-effects",
      "procedure": "Use sourced onset, duration, resistance and removal requirements; record actual effects. No universal poison, sleep, unconsciousness or condition cure is inferred."
    },
    {
      "id": "combat:environmental-hazards",
      "procedure": "Require actual exposure/trigger, warnings, conditions, available mitigation and sourced effects. The twelve PR5 hazard designs create no automatic damage or current placement."
    },
    {
      "id": "combat:retreat",
      "procedure": "Allow attempts to disengage, withdraw, negotiate or seek assistance using actual routes, time, mobility and opposition. No guaranteed escape, safe corridor or free recall."
    },
    {
      "id": "combat:nonlethal",
      "procedure": "Preserve Theron’s preference for restraint, disarmament, intimidation, negotiation, incapacitation and capture; declare intent and use supported means. Independent opponents may resist, surrender, flee or negotiate. No automatic nonlethal conversion."
    },
    {
      "id": "combat:defeat-permanent-death",
      "procedure": "Resolve actual injury/defeat/capture/death under established rules, fair warning and player agency. Death is permanent absent an already established successful exception; none is introduced here."
    },
    {
      "id": "combat:rest-recovery",
      "procedure": "Record real duration, safety and resources; no automatic rest reset, current healing or reservoir recharge. Assimilation II is personal-only24/10min with source/concentration and cap; no unsupported HP/rest rates."
    },
    {
      "id": "combat:resource-expenditure",
      "procedure": "Declare and record actual costs before/when resolution requires, including failure costs where established. Reference the original pool/inventory/ledger once by event ID; do not charge twice or assume failure refunds."
    },
    {
      "id": "combat:encounter-consequences",
      "procedure": "Record only played outcomes in original affected owners, dated chronicle/checkpoint and proper resource authorities; preserve history, knowledge, legal/custody/property and NPC independence. No encounter is resolved here."
    }
  ],
  "environment_interactions": [
    {
      "id": "environment:fire-combustibles",
      "procedure": "Only an established effect and actual combustible exposure can cause ignition/spread; fuel, ventilation, bystanders and containment matter. No new fire spell, damage or permanent transmutation."
    },
    {
      "id": "environment:ice-water",
      "procedure": "Sourced cryomancy respects actual water, surface, load, duration and temperature conditions; ice is no guaranteed bridge or unlimited fresh water."
    },
    {
      "id": "environment:electricity",
      "procedure": "No electrical spell or attack is verified in the current catalog. Discuss interaction only if a separately established effect/source supports it; no lightning power or damage modifier."
    },
    {
      "id": "environment:darkness-visibility",
      "procedure": "Record actual lighting, sight lines and established senses. Dim-light concealment is not guaranteed invisibility or new darkvision."
    },
    {
      "id": "environment:sound-stealth",
      "procedure": "Actual sound, listeners, cover and supported range matter; a displaced whisper supplies no universal silence, perfect disguise or automatic intimidation."
    },
    {
      "id": "environment:water-breathing",
      "procedure": "Flooding, current, air and physical capacity require evidence. Water association grants no breathing, immunity, safe air pocket or automatic rescue."
    },
    {
      "id": "environment:heat-endurance",
      "procedure": "Exposure, ventilation, rest, condition and protection constrain action. No new heat immunity, endurance formula or hazard damage."
    },
    {
      "id": "environment:poison-biology",
      "procedure": "Identify actual substance/exposure, species/condition and supported response. No generic venom ability, poison immunity or universal restoration cure."
    },
    {
      "id": "environment:spatial-barriers",
      "procedure": "Use specific sourced anchors, geometry, containment and ward interactions; no automatic bypass or new destination."
    },
    {
      "id": "environment:mental-defenses",
      "procedure": "Actual target, established resistance/consent/protection and memory limitations apply. A probe is no guarantee of truth, complete memory or private knowledge."
    },
    {
      "id": "environment:magical-wards",
      "procedure": "Require verified ward purpose, condition, trigger, finite power and tested scope; no unlimited ward, universal counterspell or automatic safe disarm."
    },
    {
      "id": "environment:structural-damage",
      "procedure": "Actual material, supports, load, access and collateral/legal risks constrain effects. No universal collapse calculation or automatically opened passage."
    }
  ],
  "cost_policy": {
    "owner_ref": "theron-spells",
    "current_ordinary_discount_percent": 40,
    "automatic_repricing": false,
    "new_rounding_formula": null,
    "additional_discount_application": false,
    "unverified_player_references": [
      {
        "name": "Deep Mend",
        "supplied_mp": 17,
        "verified_owner_cost": null,
        "granted": false
      },
      {
        "name": "Greater Healing",
        "supplied_mp": 21,
        "verified_owner_cost": null,
        "granted": false
      }
    ]
  },
  "recovery_policy": {
    "owner_ref": "theron-abilities",
    "personal_only": true,
    "automatic_recovery": false
  },
  "equipment_owner_refs": [
    "sovereign-nexus",
    "sovereign-expedition-wagon",
    "dawnbreakers-promise",
    "night-sovereign",
    "guardian-links"
  ],
  "phase2_links": [
    {
      "phase": 1,
      "owner_ids": [
        "world-geography",
        "travel-routes",
        "travel-procedure"
      ]
    },
    {
      "phase": 2,
      "owner_ids": [
        "settlement-services",
        "settlement-trade",
        "settlement-communications"
      ]
    },
    {
      "phase": 3,
      "owner_ids": [
        "justice-authorities",
        "justice-and-jurisdiction"
      ]
    },
    {
      "phase": 4,
      "owner_ids": [
        "guild-network",
        "guild-membership-and-contracts",
        "illicit-commerce-design"
      ]
    },
    {
      "phase": 5,
      "owner_ids": [
        "dungeon-design-proposals",
        "dungeon-ecology-and-hazards",
        "dungeon-exploration"
      ]
    },
    {
      "phase": 6,
      "owner_ids": [
        "economy-accounting",
        "property-financial-references",
        "payroll-construction-and-trade"
      ]
    },
    {
      "phase": 7,
      "owner_ids": [
        "npc-autonomy-and-time",
        "independent-assignments",
        "world-event-references"
      ]
    }
  ],
  "rank_policy": {
    "adventurer_scale_owner_ref": "guild-network",
    "dungeon_rating_domain": "dungeon-threat",
    "shattered_meridian_raw_label": "SS",
    "compatible_adventurer_rank": null,
    "status": "UNRESOLVED LEGACY SS",
    "changes_theron_rank": false
  },
  "actual_casts": [],
  "actual_combat_events": [],
  "actual_recovery_events": [],
  "actual_monster_instances": [],
  "actual_loot_events": [],
  "new_spells": [],
  "new_equipment": [],
  "new_progression": [],
  "automatic_resolution": false
}
```

## Cost and resource interpretation

The later40% ordinary discount supersedes the older30% arrangement, but original base prices and many per-spell40% recalculations remain unverified. Existing listed costs are not discounted again. The prior30% rounded-up procedure is historical, not authority for a new40% rounding rule. Full-cost exceptions stay exempt. Day124 explicitly confirms Shadow Mantle16, Umbral Murmur9 and Mental Probe13; Day156 establishes the three maternal healing costs36/32/48. Exact governing sources remain in the original owners, not a competing tariff. Deep Mend17 and Greater Healing21 are supplied continuity references absent from the current spell owner; they are not granted or silently adopted.

Dreamfall Mastered remains21MP,60ft range,20ft radius, selectable1–30minutes, concentration and established waking on damage, shaking or ended concentration; its recorded mental save remains in the spell owner. These limits grant no permanent sleep or irresistible effect.

Normal equippedDEF49 and conditional51 require original equipment evidence. Day156 wearing observations do not certify current Day181 configuration. Staff156/180 and wagon60/60 remain separate; normal ambient recharge language specifies no new interval or unplayed gain. Item construction, voluntary spirit status and unfinished systems are unchanged. Lyanna retains her item ownership; source-restricted subsystem details are not expanded or republished by this public integration. No automatic long-range rescue is certified.
