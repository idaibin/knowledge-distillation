# Course and Long-Form Batches

Use this flow for a bounded set of lessons, chapters, episodes, or transcript segments.

## Manifest First

Create one batch manifest from `assets/templates/batch-manifest.yaml` containing:

- source identity and access level;
- exact included item IDs, titles, locators, and URLs when available;
- requested range and known exclusions;
- extraction status, IR path, selected level, and render targets per item;
- explicit coverage statement such as `5 of 408 numbered lessons`.
- cumulative public coverage and publication status across all earlier batches from the same source.

## Per-Item Processing

1. Read only the requested item.
2. Exclude comments, recommendations, and unrelated page chrome unless the user requests them.
3. Store transformed claims and source locators; do not retain full licensed transcripts by default.
4. Create one IR per item so evidence and revision state remain independently auditable.
5. Validate every IR before rendering.
6. Render requested cards or models from the validated IR.

## Cross-Item Consolidation

After all items pass individually:

- identify repeated principles without deleting item-level provenance;
- record contradictions and progression across lessons;
- keep the batch index separate from per-item IR;
- never call the batch a course summary when coverage is partial.
- do not add dependency DAGs, automatic copyright scores, or cross-item merge engines unless a real workflow requires them.

## Review Payload

For external review, send the batch manifest, transformed lesson summaries, IR decisions, and rendered drafts. Do not send full licensed source text, account data, or browser state.

Before public release, review the accumulated series rather than only the current batch. Do not preserve enough original ordering, titles, or distinctive narrative detail to position the output as a substitute for the paid source.
