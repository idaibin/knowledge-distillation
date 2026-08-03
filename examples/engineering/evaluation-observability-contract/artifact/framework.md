# Evaluation and Observability Contract

## Problem

判断一次 agent 改动是否改善固定任务，同时不把 Trace、单一 metric 或测试计划当成 correctness oracle。

## Required context

- 固定 task basis、输入、expected outcome、允许/禁止动作、裁决 rubric、baseline/treatment 唯一变量；
- run identity、输出、trace/observation、retrieval、tool calls、错误、成本、时间、provider 和 evaluator 版本；
- 三轴阈值：outcome（任务结果）、process（工具选择/参数/路径）、security（违规/越权/对抗成功）。

## Steps

1. 冻结 basis 与 ground truth；缺少独立裁决规则即停止。
2. 建立三个互不替代的 score record。任何轴的 `unknown` 都不能被 aggregate 掩盖。
3. 用同一 run identity 保存输入、输出、Trace、观察、工具事件、错误、时间与成本；Trace 缺口显式记为 unknown。
4. 按固定 schema 归一化 observations；配对的 tool name/arguments 必须可解析，malformed JSON 按声明的 fallback 保留原值。
5. 用独立 expected output/human adjudication 评 outcome；用 tool selection、argument/path 检查评 process；用独立 adversarial/policy cases 评 security。
6. 分别执行 regression 与 red-team；保留 pass/fail/unknown、配置/Provider 错误与 exit code。
7. 仅在三轴均有证据且无安全回归时比较 baseline/treatment；否则只报告 case-level 结果，不推广 Skill。

## Branches and outputs

- **Pass**：三轴都有独立证据且阈值满足，输出 `outcome_record`、`process_record`、`security_record`、`run_manifest`。
- **Fail**：任一轴违反 rubric 或 security policy，输出轴、证据、回归范围和停止理由。
- **Unknown**：ground truth、normalization、provider、evaluator 或 security evidence 缺失/冲突，输出缺口与待补实验；不得声称改善。

## Stop conditions

- Trace 完整但没有独立 expected outcome；
- 只跑了一个 metric 或只通过功能回归，未覆盖 process/security；
- Smoke-test 计划、CLI 注册或配置存在被误报为运行通过；
- evaluator/provider error、Malformed observation 或 security 证据缺失被默认为 pass。

## Boundaries

Langfuse 的 traces/observations、DeepEval 的 tool-use metric、Promptfoo 的 eval/red-team/CLI 仅提供来源支持的能力描述。没有本机运行、Provider 输出、校准研究或部署审计时，结果仍是 `source_supported` 或 `unknown`。

## Anti-patterns

- **Trace equals truth**：Trace 完整就判正确；改为独立 ground truth。
- **One score hides three axes**：把 outcome/process/security 平均成一个分数；改为三条记录并传播 unknown。
- **Planned test equals passing test**：计划或 CLI 注册当作绿灯；改为保存真实命令输出和 exit code。

## Source trace

- `langfuse/langfuse@314804b` — `README.md` blob `aa96cd8…`; `.agents/ARCHITECTURE_PRINCIPLES.md` blob `b4b5d32…`; `packages/shared/src/features/evals/observationForEval.test.ts` blob `9270a89…`。
- `confident-ai/deepeval@0d100e3` — `evaluation-test-cases.mdx` blob `798fa75…`; `deepeval/metrics/tool_use/tool_use.py` blob `6ccd80a…`。
- `promptfoo/promptfoo@82ca3c2` — `README.md` blob `9ffb6e9…`; `SECURITY.md` blob `59590f1…`; `docs/plans/smoke-tests.md` blob `362f021…`; `src/main.ts` blob `84a88f4…`。

## Fixed experiment trace

- [ai-handbook evaluation/observability experiment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/evaluation-observability/README.md) — recorded local mock/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `61f013c7589899cc22dcf2a4f2010c3161e3c79518ea31967222c4a9d60491aa`; `runs/treatment.json` SHA-256 `80b185220eb3bd57ed66db55fd4048c56b1db44eb1fdfcb79c648f5f48ffc2be`. It independently verifies only the JSON/fixture handling of three axes and `unknown`, not real telemetry, an evaluator, provider, or production security behavior.

以上 source trace 不替代运行时验证；当前仅可交付 Level 3 draft contract/framework，绝非 Level 4 或 Skill。
