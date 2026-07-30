# Executability Eval

## Purpose

Verify that a proposed Level 4 artifact changes Agent behavior in an observable, bounded way.

## Required Cases

1. Happy path with all required inputs.
2. Missing-input path that must stop or ask for the missing basis.
3. Non-trigger case that should not invoke the Skill.
4. Boundary case that must refuse, degrade, or report uncertainty.

## Pass Criteria

- Trigger and non-trigger cases are distinguishable.
- Workflow preserves the Knowledge IR's principles and boundaries.
- Output contains every required section.
- Expected behavior is observable; it does not say only "produce a good answer."
- The Skill does not claim tools, permissions, or validation it lacks.
- Repeated runs on the fixed cases preserve the same decisions even if wording varies.

Passing a structural validator is necessary but not sufficient for `status.maturity: executable`.
