# Knowledge Distillation

> Build reusable AI knowledge assets from human expertise.

`knowledge-distillation` is a schema-driven Agent Skill for turning books, courses, SOPs, research, transcripts, and lived experience into traceable structured knowledge. It produces the lowest sufficient artifact: a card, a knowledge model, a decision framework, or—only when the source supports it—an executable Agent Skill.

It is not a generic summarizer. A summary compresses prose for reading; this project extracts claims, evidence, decision logic, boundaries, anti-patterns, and validation cases for reuse.

## Architecture

```text
source material
      │
      ▼
Knowledge IR instance (knowledge.yaml)
      │ validated by schemas/knowledge.schema.yaml
      ▼
┌──────────┬───────────────┬────────────────────┬──────────────────┐
│ Level 1  │ Level 2       │ Level 3            │ Level 4          │
│ Card     │ Knowledge     │ Decision           │ Executable       │
│          │ Model         │ Framework          │ Agent Skill      │
└──────────┴───────────────┴────────────────────┴──────────────────┘
```

`auto` selects the highest level supported by the evidence. Output rendering is independent: a Level 2 model can still render as a card. Level 4 is never the default.

## What It Does

- Defines what should and should not be distilled.
- Records claims with `citation`, `experience`, `observation`, or `inference` evidence.
- Separates principles, decision frameworks, anti-patterns, boundaries, and unresolved questions.
- Validates structural and semantic requirements before rendering.
- Keeps knowledge transformation separate from scraping, visual design, publishing, and growth operations.
- Keeps paid or private raw sources out of public repositories and external review payloads.
- Reviews cumulative coverage and source-substitution risk before publishing a series derived from licensed or private material.

## Quick Start

Install the repository as an Agent Skill, then invoke it with a source:

```text
Use $knowledge-distillation to turn these course notes into a traceable
Knowledge IR and select the highest fully supported knowledge level.
```

Validate an IR instance locally:

```bash
python3 scripts/validate_ir.py schemas/knowledge.example.yaml
```

Optionally run the standards-based JSON Schema validator installed with Homebrew:

```bash
brew install check-jsonschema
check-jsonschema --schemafile schemas/knowledge.schema.yaml schemas/knowledge.example.yaml
```

Run deterministic positive and negative contract cases:

```bash
python3 scripts/run_basic_evals.py
```

The repository validator uses Python 3 and PyYAML for semantic guards. `check-jsonschema` independently verifies the JSON Schema 2020-12 contract expressed as YAML.

## Repository Layout

```text
SKILL.md                    Agent orchestration entry point
agents/openai.yaml          Codex UI metadata
schemas/                    Knowledge IR contract and canonical example
references/                 Extraction, leveling, and evaluation rules
assets/templates/           Render templates copied into task outputs
scripts/validate_ir.py      Deterministic IR checks
examples/                   Multi-domain proofs of concept
evals/basic/                Reusable behavioral evaluation cases
```

Canonical course-card pipeline: [references/course-card-pipeline.md](references/course-card-pipeline.md).

## Maturity Model

- `draft`: extracted but not independently checked.
- `reviewed`: source trace and interpretation reviewed.
- `validated`: artifact-level evaluations passed.
- `executable`: Level 4 only; behavioral tests passed on a fixed test set.

Maturity describes evidence, not confidence or writing quality.

## Non-Goals

- Bulk copying or republishing copyrighted sources
- Browser acquisition or paywall circumvention
- Image or video generation
- Social publishing or account automation
- SEO, growth, or monetization workflows

## Status

v0.1 focuses on the Knowledge IR contract, deterministic validation, representative examples, and basic behavioral evals.

Current engineering example: [Image-First UI Delivery With Implementation Closure](examples/engineering/image-first-ui-delivery/artifact/framework.md). It keeps generated visual direction, provider originals, local UI specifications, implementation, and browser evidence as separate artifacts.

## License

MIT. See [LICENSE](LICENSE).
