# Historical evidence and path resolution

The three original documents and 41 split legacy modules are preserved historical evidence. Follow `governance/precedence.md`; older statements and instructions do not override later approved canon or the current checkpoint.

Path conventions:

- `index.json` paths, its `archive_index`, all entity `source_refs`, and `archive/legacy-index.json` module `path` values resolve from the repository root.
- Archive-index module `source` values are original-document **basenames relative to `archive/`**. For example, `Shadows_Over_Vellorin_World_Bible_v1.md` resolves to `archive/Shadows_Over_Vellorin_World_Bible_v1.md`.
- Bare original-document filenames inside historical text use that same `archive/` base, regardless of the historical module's own directory. They are provenance names, not root-level files.

The validator checks module paths and each original `source` using these conventions. This documentation adds explicit resolution without rewriting historical evidence. Secrets in historical material remain GM knowledge; fetching evidence does not reveal it to Theron.

## Cumulative session evidence

`session-handoffs/year847-day153-user-handoff.txt` preserves the user’s exact cumulative update through Year847 Day153 22:05. It reports played developments, testimony and unresolved questions; it is not a full transcript. Referenced entity records and confidence-labeled chronicles apply those distinctions. `checkpoints/year847-day046-0915.json` preserves the prior checkpoint byte for byte. Legacy originals/modules remain unchanged.
