# Evaluation Rules

Run structural validation first, then evaluate meaning.

## Fidelity

- Every material claim has evidence.
- Evidence points to a declared source and useful locator.
- Evidence distinguishes claim origin from verification: `source_supported` is not the same as `independently_verified`.
- For public sources, verify author, title, venue, year, and stable identifier against the source's official citation metadata. A publisher or hosting institution is not the author unless the source explicitly declares institutional authorship.
- Treat laws, regulatory thresholds, platform rules, prices, and other time-sensitive values as historical unless a current official source and effective date have been checked. Preserve the source-era rule separately from the current correction.
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
- When evaluating fees, taxes, subsidies, fines, or transfers, separate private burden, purchasing-power transfer, and real resource costs such as administration, evasion, distortion, delay, and enforcement before aggregating social cost.
- Before using a rate, score, premium, or model parameter, determine whether it is one component or the complete aggregate measure; do not promote a component into the total without the remaining terms and scope.

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

## Rights and Distribution

- Source access matches the actual page or material.
- Raw licensed/private text is not copied into public artifacts or unrelated external reviews.
- `usage.visibility` and `publication_review` match the intended downstream action.
- Public cards transform the source, add independent framing, and do not substitute for the original lesson.
- Missing `usage` denies public release; `publication_review: required` or `blocked` cannot be overridden by another usage field.
- For licensed/private series, review cumulative public coverage, retained ordering, source-specific titles, and substitute positioning—not only whether each card quotes source text.
- Treat transformation and substitution risk as human review checks, not self-certified boolean facts.

## Iterative Course-Card Learning

For a course-card series, evaluate the complete story package rather than isolated frames.

- Review knowledge fidelity, narrative causality, visual and character consistency, mobile typography, and cumulative source-substitution risk after every completed package.
- Require both checkpoints: content review immediately after story/text freeze, and final review after image/text-layout freeze.
- Bind the content checkpoint to its text-layer hash, then require that hash to equal the final text-layer hash when the package passes. Bind final review to the final IR and every frame hash. Any changed basis returns the package to revision.
- Record what the visual style should retain or change and why. Then record one actionable learning with a testable hypothesis, or a specific reason no new rule emerged after completing the full self-review. Avoid vague lessons such as “make it prettier” or “improve storytelling.”
- The immediately following package must cite the previous learning ID and either apply the rule or explain why it does not apply; later target packages can continue testing it but cannot replace the adjacent check.
- Promote a learning into a series rule only after it works across more than one topic and survives a cluster review.
- Use independent ChatGPT and Gemini review for a new series, material style change, high-risk claim, more than eight frames, more than three recorded core concepts, unresolved local choice, or scheduled cluster/batch review. Derive density triggers from the review basis instead of trusting hand-entered trigger codes. Redact licensed source text and reconcile both reviews locally before accepting them.
