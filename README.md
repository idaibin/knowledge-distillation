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

`auto` selects the lowest level supported by the IR. Level 4 is never the default.

## What It Does

- Defines what should and should not be distilled.
- Records claims with `citation`, `experience`, `observation`, or `inference` evidence.
- Separates principles, decision frameworks, anti-patterns, boundaries, and unresolved questions.
- Validates structural and semantic requirements before rendering.
- Keeps knowledge transformation separate from scraping, visual design, publishing, and growth operations.

## Quick Start

Install the repository as an Agent Skill, then invoke it with a source:

```text
Use $knowledge-distillation to turn these course notes into a traceable
Knowledge IR and select the lowest sufficient artifact level.
```

Validate an IR instance locally:

```bash
python3 scripts/validate_ir.py schemas/knowledge.example.yaml
```

Run deterministic positive and negative contract cases:

```bash
python3 scripts/run_basic_evals.py
```

The validator uses Python 3 and PyYAML. The schema is JSON Schema 2020-12 expressed as YAML.

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

## License

MIT. See [LICENSE](LICENSE).
