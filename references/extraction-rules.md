# Extraction Rules

## Establish the Boundary

Before extracting, record:

- the supplied source set and access level;
- the user's intended reuse;
- the target audience and decision context;
- topics explicitly included and excluded;
- copyright, privacy, or confidentiality constraints.

Do not acquire sources outside the user's authorization. Do not bypass authentication, paywalls, or access controls.

## Preserve Source Identity

Assign every source a stable `sources[].id`. Point evidence to that ID and a useful locator such as a section, page, timestamp, repository path, dated observation, or named workflow stage.

Use excerpts only when necessary and keep them short. If an exact quotation was not verified, omit `excerpt` and paraphrase in the claim.

## Filter Noise

Usually exclude:

- repeated anecdotes that add no new rule;
- promotional material;
- rhetorical transitions;
- examples that cannot be generalized safely;
- unsupported claims that cannot be marked as inference;
- platform-specific packaging unrelated to the underlying knowledge.

Keep a story when it supplies evidence, a boundary case, or a concrete test.

## Chunk Long Sources

For long material:

1. Build a source manifest.
2. Extract candidate claims per chunk with locators.
3. Merge duplicates without losing evidence.
4. Resolve contradictions or add them to `open_questions`.
5. Build frameworks only after cross-chunk consolidation.

Never claim full-source coverage when only excerpts or selected chapters were processed.

