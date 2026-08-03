# Evaluation-Driven Agent Learning Workflow

## Problem

把快速变化的 AI 仓库与本地工程经验转成可复用能力，同时避免把 Star、README、自述 Benchmark、完整 Trace 或单次成功误当成真实提升。

## Required context

- 固定任务 basis、范围、Ground Truth、失败条件与裁决规则；
- 候选 Runtime 的固定提交与具体来源 locator；
- Baseline 与 Treatment 的唯一变量；
- 运行输入、输出、工具事件、错误、成本和时间记录；
- 独立的功能回归与安全检查。

## Steps

1. 冻结问题和评分口径 — Check: 隐去方法名称后，另一位 reviewer 仍能按相同规则评分。
2. 选择覆盖任务所需工具、状态、HITL 与持久化能力的最小 Runtime — Check: 每项依赖都有需求映射。
3. 用同一 run identity 保存来源、输入、输出、Trace 与失败 — Check: 可重放，或明确不可重复边界。
4. 对照 Ground Truth 评分 task completion、tool correctness、FP、FN 和 actionability — Check: `unknown` 阻止增益声明。
5. 分开执行功能回归与风险适配的 red-team — Check: 两类结果不互相替代。
6. 只在至少两个异构案例出现重复增益且无不可接受回归后，生成 Skill 候选 — Check: trigger、inputs、workflow、constraints、outputs、tests 和 rollback 均已稳定。

## Boundaries

- 仓库 README 只能提供 `source_supported` 证据，不等于本机或项目运行验证。
- Star 只用于发现候选，不能决定技术选型。
- Trace 用于诊断，不直接证明结果正确。
- 单案例只支持案例级结论，不支持强制 Skill 规则。

## Anti-patterns

- **Popularity as proof**：高 Star 直接当采用理由；改为固定提交、任务匹配、边界和实验四重门禁。
- **Trace equals truth**：Trace 完整就宣称正确；改为独立 Ground Truth 与数据集评分。
- **Single-case Skill promotion**：一次成功就修改 Skill；改为至少两个异构案例的重复增益。

## Source trace

- `openai/openai-agents-python@000a96b` — `README.md / Core concepts`
- `langchain-ai/langgraph@b2926a0` — `README.md / Why use LangGraph?`
- `confident-ai/deepeval@0d100e3` — `README.md / Agentic metrics`
- `langfuse/langfuse@314804b` — `README.md / Observability, Evaluations, Datasets, Prompt Management`
- `promptfoo/promptfoo@82ca3c2` — `README.md / CI/CD integration and red teaming`

以上来源均固定到 2026-07-31 核验的提交；当前结论是来源支持的 Level 3 Framework，不是独立验证过的 Skill。
