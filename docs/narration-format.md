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
