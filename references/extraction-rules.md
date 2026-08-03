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

Treat `evidence.type` as claim origin and `evidence.verification_status` as verification state. A course locator can make a claim `source_supported`; it does not make the claim `independently_verified`. Use `unverified` when the source-to-claim mapping itself has not been checked.

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

## Licensed and Private Sources

For paid courses, internal SOPs, private notes, and authenticated pages:

- set the source access accurately;
- keep raw text outside public repositories;
- retain locators and transformed notes instead of full transcripts whenever possible;
- mark public-content publication review as required unless reuse rights are confirmed;
- send external reviewers only transformed claims, boundaries, and card drafts—not the raw licensed source;
- preserve a coverage manifest so a five-item batch is not mistaken for a complete course.
- require publication constraints that prohibit source text and source-substitute positioning, and review cumulative coverage across batches before public release;
- transform source-specific lesson titles and ordering when public packaging would otherwise reconstruct the paid course.
