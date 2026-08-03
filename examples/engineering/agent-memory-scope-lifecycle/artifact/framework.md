# Scoped Memory Lifecycle Gate

## Problem

Decide what an agent may persist, which scope owns it, how it is updated and forgotten, and how reads prevent cross-scope or sensitive-data leakage.

## Required context

- Datum purpose, retention, deletion owner, and sensitivity classification;
- Workflow/thread/session/user/agent/graph identity model;
- Transcript, state, memory, vector, graph, backup, and index stores;
- Update, expiry, deletion, provenance, and post-forgetting readback mechanisms.

## Steps

1. Classify datum as workflow state, transcript/raw content, or durable memory — Check: missing purpose, retention, or deletion owner keeps it ephemeral.
2. Choose the narrowest scope and require its identity in storage and query — Check: missing `user_id`, `agent_id`, `run_id`, or equivalent filter is rejected.
3. Extract/deduplicate only durable facts and attach provenance/expiry — Check: secrets, credentials, tokens, or unredacted sensitive fields are removed or the write is refused.
4. Read with scope filters before ranking — Check: cross-scope fixtures return no records and invalid/empty query parameters are rejected.
5. Apply update and forgetting events — Check: scoped post-forgetting read plus index/backup audit finds no record, or erasure remains `not_verified`.
6. Evaluate accuracy, token cost, latency, leakage, sensitive-data rejection, and deletion separately — Check: unrun backend/provider paths remain `not_verified`.

## Boundaries

- Inference-enabled Mem0 stores extracted memories, not a verbatim transcript; raw-content mode is explicit.
- Mem0 scope filters do not prove tenant isolation or external-store security.
- LangGraph persistence/memory capability does not define application retention or deletion semantics.
- Managed benchmark scores are not proof of OSS reproduction.

## Anti-patterns

- Transcript as memory: copy every message into long-term recall; classify roles and retain raw content only by policy.
- Scope-free recall: widen a search when no result is found; require identity filters and reject missing scope.
- Deletion claim without readback: trust a delete response; read back and audit all stores, otherwise keep erasure unverified.

## Source trace

- `mem0ai/mem0@760dca6` — `README.md` (scopes/basic flow), `docs/core-concepts/how-it-works.mdx` (messages vs memories, extraction/retrieval, filters), `docs/core-concepts/memory-evaluation.mdx` (accuracy/cost/latency), `mem0/memory/main.py` (`_SENSITIVE_FIELDS_EXACT`, `_IDENTITY_KEYS`, `_validate_search_params`).
- `langchain-ai/langgraph@b2926a0` — `README.md` (`## Why use LangGraph?`, durable execution and memory capability descriptions).

## Fixed experiment trace

- [ai-handbook memory experiment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/memory/README.md) — recorded local mock/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `5e95e63482a181efe20009cc0d5f6bf9dff35137c0fb8b62c897c4d42f63f13f`; `runs/treatment.json` SHA-256 `274041d7d308c82f9d5c32551a2e632f8894625bc69f25d78dac4bbfed0f778f`. This independently verifies only the fixed mock/fixture lifecycle contract, not a Mem0/LangGraph runtime or production isolation.

This is a Level 3 draft. Fixed-commit source claims do not verify a selected backend's extraction quality, isolation, or deletion behavior; it is not Level 4 or a Skill.
