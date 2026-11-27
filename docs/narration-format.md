# Permanent campaign narration format

Player-approved in [Day472 handoff](../archive/session-handoffs/year847-day472-user-handoff.txt). These rules govern future campaign responses; entity files remain ordinary Markdown.


These rules are approved by the player and apply to future campaign responses.

### Dialogue formatting

Every spoken line must identify its speaker:

**Theron:** "Before we do anything, I want answers."

**Lyanna:** "And nobody uses my memories without permission."

**Caelrix:** "That's a remarkably sensible plan."

Do not use unattributed quotations when the line is spoken by a character.

Use the same format for Raze, Aegis, Guardians, dragons, prisoners and NPCs.

Keep speaker names consistent. Narrative descriptions should remain ordinary prose.

### Collapsible bookkeeping

The main reading experience must prioritize immersive storytelling.

Keep the following detailed information inside **clickable, collapsible dropdown boxes**, closed by default:

- Independent party assignments.
- Loot and recovered inventory.
- Shady Salvage locations and status.
- Launder inventory and processing results.
- Quest requirements and technical conditions.
- Guardian-chain status.
- Guild statistics and detailed skill records.
- Mana expenditure tables.
- Treasury ledgers and account balances.
- Long prisoner or settlement registers.
- Large progress and task-tracking tables.

Show concise summaries outside the dropdowns only when needed.

**IMPORTANT:** The user approved actual expand/collapse controls, NOT popovers, tooltips, or merely italicized headings.

In a DIL-compatible ChatGPT response, use state and `pressable` with conditional content, or an equivalent functioning collapsible component available in the current renderer.

Conceptual DIL example:

```jsx
{@body const [lootOpen,setLootOpen]=DIL.useState(false)}

<box border radius="lg" gap={0}>
  <pressable padding={3} onClick={()=>setLootOpen(!lootOpen)}>
    <row align="center" justify="between">
      **Recovered Items & Launder**
      <icon name={lootOpen?"chevron-up":"chevron-down"}/>
    </row>
  </pressable>
  {#if lootOpen}
    <box padding={3}>
      | Item | Quantity |
      |---|---:|
      | Old coinage | 6 gp 8 sp |
      | Rune-setting tools | 2 |
    </box>
  {/if}
</box>
```

This is a rendering example, not a request to force DIL source into Markdown campaign entity files. Store these rules in the repository's appropriate narration/style configuration or guidance document. If there is no suitable existing file, create a dedicated narration-format document and reference it from `AGENTS.md`.

Each dropdown must:
- Be closed initially.
- Open when clicked.
- Close when clicked again.
- Have its own state.
- Retain readable table formatting.
- Avoid disrupting the chapter's narration.

### Storytelling style

- Keep a few substantial atmospheric scenes.
- Clearly identify locations and in-world times.
- Use concise, natural conversations.
- Preserve distinct personalities and independent NPC decisions.
- Avoid repeated disclaimers, duplicated summaries and lengthy mechanical interruptions.
- Preserve medieval high fantasy: swords, sorcery, dragons, ancient runes, mystical wards, and no modern or science-fiction technology.
- Preserve nonlethal, eerie Blackscale tactics where appropriate.
- Maintain player choice and meaningful consequences.
- Show suitable fantasy scene illustrations when available and requested by campaign convention.
- Finish active scenes with relevant selectable choices.
- Never award abilities or stats merely because the narration sounds impressive.
- Never silently resolve an ongoing quest offscreen.
- For END SESSION, produce a checkpoint and Codex/next-chat handoff instead of continuing the story.


## Renderer fallback

Use functioning stateful DIL controls when supported. In a Markdown renderer supporting native HTML disclosure, `<details><summary>Title</summary>…</details>` without `open` is an equivalent independent, initially closed toggle; keep blank lines around tables. Never substitute popovers, tooltips or static headings for collapsible controls. If a renderer cannot provide functioning controls, state that limitation briefly and provide concise summaries; do not claim a static label is interactive. No raw DIL source in entity records.

## Year 853 Day 52 standing additions

Update `docs/narration-format.md` and other existing guidance files where appropriate.

These corrections are player-approved standing requirements.

### Exact timestamps

Every narrative section and subsection must show:

**Year · Annual Day · Exact Time | Location**

Example:

#### 1. The Ashvale Investigation

Year 853 · Day 53 · 8:00 AM | Westbridge

#### 1.1. Examining the original AV-07 register

Year 853 · Day 53 · 8:30 AM | Westbridge Records Office

Independent events must use the same timeline.

Do not advance the clock twice for parallel events.

### Dialogue

Every spoken line identifies its speaker.

Preserve established voices, personalities and relationships.

Avoid generic repetitive dialogue.

### Interactive bookkeeping

Use functioning, independently collapsible sections that are closed by default.

Apply them to:

- Assignment trackers.
- Character statistics.
- Guild contract registers.
- Financial ledgers.
- Loot and salvage.
- Inventory.
- Quest requirements.
- Research progress.
- Mana expenditure.
- Independent organizations.
- Student records.

Assignment trackers should allow selection by person or team and display assignment and status.

Do not substitute static headings, tooltips or popovers for functioning expand/collapse controls.

When the renderer cannot support interactive controls, state the limitation and use concise tables.

Repository entity files remain ordinary Markdown or structured data.

Do not insert raw ChatGPT-specific interface markup into canonical entity files.

### Artwork

Use existing approved repository character artwork whenever available.

Consult:

- `artwork/character-references/README.md`
- `artwork/character-references/manifest.json`
- `artwork/player-cards/README.md`
- Existing dragon artwork and reference records.

Do not replace approved portraits with arbitrary internet images.

New conceptual illustrations are not automatic character appearance canon.

### Story progression

- Follow the established Story Mode / Favored Protagonist rules.
- Preserve Theron's established strength.
- Avoid unnecessary grind.
- Avoid repetitive document-to-document investigations that never conclude.
- Existing unresolved antagonists take priority over unnecessary new masterminds.
- Provide meaningful discoveries and conclusions.
- Maintain credible consequences and player agency.
- Preserve autonomous NPC decisions.
- Maintain medieval high fantasy.
- Do not award skills or powers simply because narration sounds impressive.
- Respect previously authorized combined objectives.
- Do not repeatedly stop to request permission for routine actions already authorized.

### Knowledge separation

GM knowledge is not automatically Theron's knowledge.

Independent developments require actual reporting, communication or discovery.

Do not reveal protected NPC locations, unrevealed identities, hidden abilities or GM-only conclusions without proper discovery.

### Session commands

START SESSION:

- Read the current checkpoint.
- Read the next-chat handoff.
- Retrieve relevant owner records.
- Continue from the exact established scene.
- Do not repeat completed introductory events.

PAUSE:

- Stop gameplay and campaign time.
- Permit canon audits and maintenance.

END SESSION:

- Stop gameplay.
- Produce the Codex implementation handoff.
- Produce the next-chat GPT handoff.
- Include relevant transactions, changes, quest status, character progression and unresolved items.
- Do not narrate additional actions after the endpoint.
