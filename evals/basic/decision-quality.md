# Decision Quality Eval

## Purpose

Distinguish an actionable framework from a topical outline.

## Input

Use source material describing a recurring operational problem, several diagnostic checks, and at least one situation where the method should stop.

## Pass Criteria

- `framework.problem` names one concrete decision or diagnosis.
- Steps are ordered and use contiguous integer IDs.
- Each step contains an action and a check that can change the next decision.
- At least one boundary prevents over-application.
- Anti-patterns include a symptom and correction.
- Level 3 is selected unless all Level 4 fields and behavioral tests are supported.

## Failure Signals

- Steps repeat chapter headings.
- Checks merely restate actions.
- Framework applies to every problem in the domain.
- Uncertainty is removed to make the artifact look complete.
