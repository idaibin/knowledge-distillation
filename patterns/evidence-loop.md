# Evidence Loop

## Problem

An AI reviewer can turn a plausible hypothesis into a confident finding before the relevant code path, impact, or reproduction method has been checked. This increases false positives and makes later comparison impossible.

## Principle

Every material finding follows one traceable chain:

```text
observation -> evidence -> reasoning -> impact -> verification -> adjudication
```

If the chain cannot be completed, retain the item as an explicit hypothesis or drop it. Do not silently promote it to a finding.

## Finding Gate

A reportable finding must provide:

1. a precise location or other reproducible evidence;
2. reasoning that connects the evidence to the claimed defect;
3. a concrete engineering or user impact;
4. a verification method or already observed result;
5. confidence and human adjudication as separate fields.

Use these adjudication states:

- `confirmed`: a reviewer accepted the finding;
- `rejected`: a reviewer disproved or declined it;
- `unknown`: evidence remains insufficient;
- `fixed`: the accepted defect was remediated and the relevant path was rerun.

## Evidence Score

Score one point for each present and usable component: location, reasoning, impact, and verification. The score measures evidence completeness, not truth. A four-point false positive remains false and must be recorded as `rejected`.

## Boundaries

- Static inspection does not prove runtime behavior.
- A build or test proves only the path it exercised.
- Confidence is not evidence.
- Matching an expected answer is not enough when the location or causal chain is wrong.

## Validation

On a fixed case set, compare prompt-only and pattern-assisted runs using precision, recall, evidence score, severity alignment, actionability, and false-positive count. Reject any apparent improvement achieved only by emitting more findings.
