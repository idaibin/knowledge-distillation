# Control-and-Resume Runtime Gate

## Problem

Choose conversation ownership and establish guardrail, checkpoint, interrupt/resume, and idempotency controls before allowing a stateful agent run to perform consequential work.

## Required context

- Conversation owner and specialist boundaries;
- Tool and handoff inventory, guardrail timing, and maximum-turn policy;
- Checkpointer/durability option and interrupt approval state;
- External side effects, stable operation keys, and postcondition checks.

## Steps

1. Write the run contract and choose manager-as-tools or handoff — Check: a single owner or explicit transfer is named; otherwise stop.
2. Map input, output, and function-tool guardrails — Check: first-agent input, final-agent output, and every configured function tool are covered; uncovered hosted/handoff paths stop the run.
3. Select persistence and checkpointer — Check: the durability mode reaches the required resume point; otherwise disclose non-resumable behavior.
4. Put approval before the consequential operation — Check: resume validates the same target and arguments; stale or broadened approval is rejected.
5. Fence external effects — Check: duplicate resume with the same operation key cannot create a second effect, or the path stops before enabling resume.
6. Drill guardrail trip, max turns, timeout, checkpoint loss, interrupt, and retry — Check: each produces an observable stop/refusal/degraded result; untested paths stay `not_verified`.

## Boundaries

- FakeModel tests do not prove real-provider safety, latency, or sandbox containment.
- An interrupt re-executes its node and is not an exactly-once transaction boundary.
- CPU-bound or synchronous work can delay cooperative timeout cancellation.
- Persistence features do not define the application state schema or approval policy.

## Anti-patterns

- Guardrail illusion: treat first-agent input checks as coverage for every delegated tool; map and test each execution boundary.
- Checkpoint equals exactly once: allow a resumed external write without an idempotency fence; add a stable operation key and postcondition check.

## Source trace

- `openai/openai-agents-python@000a96b602889b00f7cfaa210c41e1a74be65272` — `docs/agents.md` (`## Multi-agent system design patterns`), `docs/guardrails.md` (`## Workflow boundaries`, `## Tool guardrails`), `src/agents/run.py` (`Runner.run`, `Runner.run_sync`, `AgentRunner.run_streamed`), `tests/test_guardrails.py` (`test_blocking_guardrail_prevents_agent_execution`).
- `langchain-ai/langgraph@b2926a0ff9589c28c7e01fe7cdbb337b86d5a4b4` — `libs/langgraph/langgraph/types.py` (`Durability`, `interrupt`, `TimeoutPolicy`), `libs/langgraph/langgraph/pregel/main.py` (`Pregel.ainvoke`).

## Fixed experiment trace

- `experiments/ai-capability-clusters/agent-runtime-orchestration/README.md` — recorded local mock/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `b222ad858f0d4f9521423475d270584ec41cb9090b921f31a709041819d1e0a9`; `runs/treatment.json` SHA-256 `e69292f90a5810b5a19e2f66edfa56e07900fd040558621a67b5c205e50ee94d`. This independently verifies only the fixed mock/fixture contract, not an upstream runtime or production behavior.

This is a Level 3 draft: source descriptions and the ordered local method are distinct. Idempotency fencing, real-provider behavior, and deployment security remain unverified; this is not Level 4 or a Skill.
