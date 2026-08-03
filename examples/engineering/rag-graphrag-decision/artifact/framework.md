# Retrieval-to-GraphRAG Escalation Gate

## Problem

Decide whether a target corpus and query workload justify supplementing simple RAG with GraphRAG's graph extraction, community/report, and synthesis pipeline.

## Required context

- Frozen target corpus and representative query classes;
- Gold answers or reference evidence, provenance requirements, and risk level;
- Simple-RAG baseline traces (contexts, response, coverage/relevance, faithfulness, latency, cost);
- GraphRAG pilot budget and rollback path.

## Steps

1. Freeze corpus, queries, answer contract, and adjudicated test set — Check: missing representative questions or reference evidence stops the decision as `not_verified`.
2. Run simple RAG and score coverage/relevance separately from faithfulness — Check: unknown or incomparable evaluator fields block an upgrade claim.
3. Classify residual failures — Check: tune simple retrieval for local passage/chunking failures; continue only for recurring multi-hop, global-synthesis, or provenance gaps.
4. Pilot GraphRAG on the small target set — Check: extraction, embeddings, reports, and provenance are present; nonempty graph output is not treated as factual proof.
5. Compare on the same items — Check: select GraphRAG only when graph-shaped cases gain material coverage/faithfulness within accepted cost and latency, otherwise retain simple RAG.
6. Record decision and rollback — Check: absent reproducible metrics, human provenance review, or target-corpus traces, keep the result provisional.

## Boundaries

- GraphRAG is documented as a demonstration and indexing can be expensive; prompt tuning may be required.
- LlamaIndex evaluator examples use LLM judges and do not prove calibration for the target dataset.
- GraphRAG guidance retains trusted-user, domain-expert, and provenance-review assumptions.
- No fixed source here supplies a universal GraphRAG-win threshold.

## Anti-patterns

- Graph novelty as justification: add a graph without recurring graph-shaped baseline failures; require a fixed comparison.
- One evaluator number as truth: collapse coverage, faithfulness, relevance, cost, and provenance into one score; report them separately.
- Nonempty graph equals factual graph: treat extraction rows as verified facts; inspect provenance and adjudicate target examples.

## Source trace

- `run-llama/llama_index@c864fcf` — `docs/src/content/docs/framework/getting_started/concepts.mdx` (`## Agentic Applications`, `## Agents`, `## Retrieval Augmented Generation (RAG)`; local synthesis), `docs/src/content/docs/framework/module_guides/evaluating/usage_pattern.md` (faithfulness/relevancy/batch evaluation), `llama-index-core/llama_index/core/query_engine/retriever_query_engine.py` (`retrieve`, `synthesize`, `_query`).
- `microsoft/graphrag@14a00ad` — `README.md` (overview/cost), `docs/index/architecture.md` (knowledge model/workflows/cache), `RAI_TRANSPARENCY.md` (evaluation/limitations), `packages/graphrag/graphrag/index/workflows/extract_graph.py` (graph extraction).

## Fixed experiment trace

- [ai-handbook RAG/GraphRAG experiment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/rag-graphrag/README.md) — recorded local mock/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `47527ac8de3bbf9d93b99df590ed195ffdb8a218e960affb389896f2067f6888`; `runs/treatment.json` SHA-256 `8965588dee0335c28e39729969490199cd76f9b3af98ec2789f0124850f5d505`. This independently verifies only the fixed mock/fixture comparison, not an upstream retriever, model, target corpus, or production behavior.

This is a Level 3 draft: target-corpus quality, metrics, and cost remain unverified; it is not Level 4 or a Skill.
