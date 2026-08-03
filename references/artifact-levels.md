# Artifact Levels

`selected_level` records the highest knowledge capability supported by the IR. `render_targets` records what the user wants produced from that IR. A Level 2 model may therefore render as both `model` and `card` without changing its evidence-backed level.

## Level 1: Card

Use for one bounded idea with a traceable definition, example, boundary, and takeaway. A card is for fast human comprehension, not an Agent trigger.

Minimum: one principle with evidence.

## Level 2: Knowledge Model

Use when several related principles, relationships, examples, and boundaries form a reusable domain model.

Minimum: multiple connected claims plus explicit boundaries or open questions.

## Level 3: Decision Framework

Use when the source supports an ordered method for diagnosing or deciding a named problem.

Minimum: one framework with actionable steps, checks, boundaries, and evidence.

## Level 4: Executable Agent Skill

Use only when all Level 3 requirements pass and the IR also contains complete trigger, inputs, workflow, outputs, constraints, and behavioral tests.

Level 4 is invalid when:

- steps are merely chapter headings;
- the trigger is broad or identity-based;
- required inputs are unknown;
- success cannot be observed;
- source boundaries are missing;
- the proposed Skill mostly imitates a living author's voice or republishes protected material.

## Auto Selection

Evaluate from Level 4 downward and select the highest fully supported level, but prefer the lower level whenever a required field is inferred, unstable, or untested. Record the rationale. Then select render targets independently from the requested deliverable.

Allowed render targets:

- `card`: concise human-facing learning or social draft;
- `model`: structured knowledge document;
- `framework`: decision or diagnostic workflow;
- `skill`: Agent Skill, allowed only when `selected_level: level_4`.

`model` shows variables, relationships, or mechanisms without requiring a fixed procedure. `framework` provides a repeatable analysis order or checklist. Arrows in rendered frameworks indicate analysis order, not inevitable causation.
