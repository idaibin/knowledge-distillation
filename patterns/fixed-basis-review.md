# Fixed-Basis Review

## Problem

Review results drift when the repository, branch tip, requested scope, or governing constraints change during analysis. Two runs may then appear inconsistent even though they examined different inputs.

## Principle

Freeze the review target before forming final findings:

```text
basis = repository + base commit + head commit + scope + constraints + exclusions
```

Record the basis in machine-readable metadata and derive the patch from the recorded commits. If the basis changes, invalidate the affected review and rerun it.

## Workflow

1. Resolve the real Git root and effective instructions.
2. Record base and head commit SHAs; use a patch hash when the case stores a patch.
3. State included paths, excluded paths, review question, and severity policy.
4. Inspect references outside the patch only when needed to trace an affected contract; record that expansion.
5. Bind human findings, agent output, and evaluation to the same case ID and basis.
6. Before comparison, verify that every artifact declares the same basis.

## Boundaries

- A branch name alone is not immutable.
- An uncommitted worktree is not a stable benchmark unless its patch is captured and hashed.
- Fixed basis controls inputs; it does not prove that the review is correct.
- Review authorization does not authorize edits, commits, pushes, or publication.

## Validation

A fixed-basis case is valid only when another reviewer can reconstruct the reviewed diff and confirm that the human and agent findings refer to it. A mismatched SHA, patch hash, scope, or schema version makes the comparison invalid rather than merely lower scoring.
