---
name: fixed-basis-repo-review
description: Review a repository, commit, branch, or fixed diff for actionable defects with explicit evidence and verification limits. Use for review-only requests with an identifiable code basis.
---

# Fixed-Basis Repository Review

1. Record the repository root, branch, fixed commit or diff range, and requested scope. Stop or mark the review provisional if the basis is moving.
2. Read effective repository instructions and inspect the affected contracts, implementation, and tests.
3. Reproduce suspected defects on the fixed basis. Distinguish verified facts, evidence-backed inference, and unverified risks.
4. Report actionable findings first with impact and precise location. Then report verification coverage and residual risks.

Do not edit files or mutate Git during a review-only request. Do not present static checks as runtime or production proof.
