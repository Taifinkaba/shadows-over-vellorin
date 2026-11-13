# Day472 END SESSION canon and narration update

- Archived the exact supplied Day472 checkpoint and preserved Day153 snapshot and structured values.
- Advanced only records to Year847 Day472 16:10, Hollow of the First Hour, ENDED; restored First Hour outcome, voluntary release, custody and ongoing Guardian/Crown work.
- Updated existing party, creatures, mechanics, quest and estate entities; indexed new Guardian, witnesses/prisoners, Accord, staff/bracers, registries and project/handoff references.
- Preserved mastered skills, spell costs, prior sessions, locked abilities, finite mana, NPC independence and historical unresolved quests.
- Added permanent attributed dialogue/collapsible bookkeeping narration rules linked from AGENTS and README.
- Schema3 supports verified partial account allocation and unknown individual mana expenditures; keeps schema2 historical validation. Cash673gp9sp reconciles final scene only; intermediate accounts remain unverified. No invented income, rewards, prisoner transfer or play.

# Change log
- **Initial modular import:** Split three source documents into targeted modules, preserved originals, extracted paused checkpoint and verification queue. No in-world changes.
- **v2 entity pass:** Curated 56 small entity records; moved 41 former modules to `archive/legacy-modules/` with index, preserved originals. No gameplay changes.

- **Canon validation maintenance:** Parse safe YAML frontmatter; require and type-check metadata; reject duplicate keys, IDs and paths; verify entity/archive coverage and source files; compare structured entity facts with the checkpoint; sum currency in integer copper. Add regression tests and pinned PyYAML dependency to CI.
- **Retrieval and provenance maintenance:** Index verified Theron abilities, skills and spells plus party financial boundaries; cite A-07's 17-day evidence; add unresolved custody-fund disposition to the verification queue; document archive source resolution. Historical evidence and checkpoint bytes are unchanged; no time, HP, MP, money, quest, mystery, knowledge or relationship change.

- **Character card artwork:** Add labeled PNG cards and a gallery for Theron Ashvale (with Shade), Garrick Vale, Nyx Thorne (with Ember), and Lyra Moonvale. Unspecified appearances are artistic interpretations. No gameplay or canon changes.

- **Expanded artwork:** Add 15 labeled illustrations for the Ashvale family, Tomas and two hounds, six animal companions, Vaeltharion, the hidden woodland lodge, Ashvale Estate, and Wayfarers’ Guild. Add categorized galleries with source links and interpretation notes. No canon or checkpoint changes.

- **Year847 Day153 22:05 cumulative canon sync:** Preserve exact user handoff and Day46 checkpoint. Reconcile reported freedom/consent covenant, academy and lodge development, treasury consolidation, creature links/bonds, learned spells and specialized research, Caelan’s limited rehabilitation, and freight evidence chain. Add confidence-labeled chronicles and explicit unresolved timeline/accounting questions. Current HP100/100 MP337/400 DEF26 S+ Level5; party/lodge cash555gp; academy separate. Update checkpoint schema and regression checks without rewriting legacy archives or merging the PR.
