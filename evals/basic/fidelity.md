# Fidelity Eval

## Purpose

Detect unsupported attribution, broken evidence trace, and overstated source coverage.

## Input

Use a source excerpt with:

- two explicit claims;
- one illustrative anecdote;
- one unresolved limitation;
- no executable workflow.

## Pass Criteria

- Every retained principle points to the supplied source and an accurate locator.
- Exact wording is quoted only when verified.
- The anecdote is removed or retained with a stated evidentiary purpose.
- The limitation appears in a boundary or open question.
- Output does not claim full-book or full-course coverage from the excerpt.
- Selected artifact is below Level 4.

## Automatic Guards

`scripts/validate_ir.py` must reject undeclared `source_ref` values, missing evidence locators, missing verification status, and licensed/private inputs without minimum publication constraints.
