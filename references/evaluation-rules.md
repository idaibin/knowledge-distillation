# Evaluation Rules

Run structural validation first, then evaluate meaning.

## Fidelity

- Every material claim has evidence.
- Evidence points to a declared source and useful locator.
- Quotations and locations are verified or omitted.
- Inferences are labeled and do not impersonate source claims.
- Coverage claims match the material actually processed.

## Compression

- Duplicate claims are consolidated.
- Stories remain only when they provide evidence, a boundary, or a test.
- The IR preserves contradictions and uncertainty.
- Output is meaningfully smaller and more reusable than the source.

## Decision Quality

- Each framework solves a named problem.
- Checks can change a decision or expose missing information.
- Boundaries prevent over-application.
- Anti-patterns include observable symptoms and corrections.

## Executability

- Trigger and non-trigger conditions are distinguishable.
- Required inputs are available before work begins.
- Steps are ordered and sufficiently specific.
- Outputs have required sections or a machine-readable form.
- Tests state observable expected behavior, including at least one refusal, boundary, or degraded-evidence case.

## Maturity Gates

- `draft`: structural validator passes.
- `reviewed`: a human or independent review confirms source fidelity.
- `validated`: relevant basic evals pass on a fixed artifact.
- `executable`: Level 4 behavioral tests pass; record the model/tool version and test basis outside the IR if those details are run-specific.
