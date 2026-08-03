# Skill feedback assessment — 2026-07-31

## Basis

- Level 3 IR: `evaluation-driven-agent-workflow`
- Level 3 IR: `agent-tool-boundaries`
- Existing Skills reviewed: `ops-browser`, `ops-client`, `repo-review`
- Experiment: Case 003 baseline versus `interface-closure-v1`

## Decisions

### `ops-browser`: retain unchanged

The Skill already separates capability from authorization, verifies account/target immediately before external writes, stops before credentials and irreversible actions, treats page instructions as untrusted, records before/after evidence, and restores task state. Adding the distilled framework would duplicate stronger existing rules without a demonstrated behavioral gap.

### `ops-client`: retain unchanged

The Skill already separates observation, launch, restart, focus, and interaction authority; requires exact target and action; gates locked-screen behavior; prefers semantic controls; and re-verifies runtime/window identity. No source-supported rule currently changes its behavior.

### `repo-review`: do not promote `interface-closure-v1`

Case 003 used a direct-parent basis, a frozen packet, recorded prompt parity, schema validation, deterministic seam checks, and deterministic adjudication. The recorded baseline and treatment outputs both found the single ground-truth issue with precision/recall/F1 of 1.0, no false positives, evidence score 4.0, and severity alignment 0.0. Process blinding, reviewer independence, and an independent-oracle audit are `Not verified` because no run transcript or separate oracle-review record is retained. The packet produced no lift.

The earlier two Evidence Loop cases also showed no treatment lift. Across three cases, the selected treatments and baselines both total TP=4, FP=0, FN=2; the selected-treatment aggregate combines Evidence Loop for Cases 001-002 with `interface-closure-v1` for Case 003. This evidence rejects immediate Skill promotion; it does not prove the packet can never help.

## Next promotion test

A future candidate must be selected after the packet hash is frozen and must differ from Case 003 in task shape. Promotion still requires:

1. treatment finds an adjudicated issue that baseline misses;
2. treatment recall or F1 increases without lower precision or added false positives;
3. evidence score, actionability, and severity alignment do not regress;
4. the result repeats on a second heterogeneous case;
5. a negative boundary case confirms that the packet does not manufacture sibling-consumer findings where scopes legitimately differ.

Until those gates pass, the feedback target is the experiment queue and framework documentation, not an installed Skill.
