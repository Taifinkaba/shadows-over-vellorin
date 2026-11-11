# Change log
- **Initial modular import:** Split three source documents into targeted modules, preserved originals, extracted paused checkpoint and verification queue. No in-world changes.
- **v2 entity pass:** Curated 56 small entity records; moved 41 former modules to `archive/legacy-modules/` with index, preserved originals. No gameplay changes.

- **Canon validation maintenance:** Parse safe YAML frontmatter; require and type-check metadata; reject duplicate keys, IDs and paths; verify entity/archive coverage and source files; compare structured entity facts with the checkpoint; sum currency in integer copper. Add regression tests and pinned PyYAML dependency to CI.
- **Retrieval and provenance maintenance:** Index verified Theron abilities, skills and spells plus party financial boundaries; cite A-07's 17-day evidence; add unresolved custody-fund disposition to the verification queue; document archive source resolution. Historical evidence and checkpoint bytes are unchanged; no time, HP, MP, money, quest, mystery, knowledge or relationship change.

- **Character card artwork:** Add labeled PNG cards and a gallery for Theron Ashvale (with Shade), Garrick Vale, Nyx Thorne (with Ember), and Lyra Moonvale. Unspecified appearances are artistic interpretations. No gameplay or canon changes.
