# AI knowledge engineering v1.0 Skill gate assessment — 2026-08-03

## Decision and basis

**Decision: no-promotion.** 本轮三项 application 的 paired rule experiment 均记录了 treatment 的正向 lift，但证据仍不足以把规则实验提升为生产 Skill。

主证据是 [ai-handbook experiments](https://github.com/idaibin/ai-handbook/tree/main/experiments/ai-capability-clusters/applications) 下三个 case 的 README、冻结 basis、baseline/treatment runs、预注册 oracle、adjudication 与 summary。三案本次均重跑两次。每案只说明其固定输入和本地独立检查实际覆盖的范围；不据此宣称真实 provider、浏览器或生产运行时效果。

Promotion gate 采用以下必要条件：至少两个任务形态异构的正向 paired lift、一个独立的负边界 case、precision 不下降且无新增 false positive。任何一项缺失，规则继续保留在实验与 framework 范围。

## Paired evidence

| Case | Task shape and treatment | Baseline TP/FP/FN; P/R/F1 | Treatment TP/FP/FN; P/R/F1 | Oracle pass and independent checks | Gate observations |
|---|---|---|---|---|---|
| [01: RustZen navigation audit](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/README.md) | 固定 Git object 的路由—owner/capability 闭环；treatment 从 routes 与 capability-map 通用枚举固定 target-scope candidates，不读取 oracle/expected answers。 | 0/0/3; 0.0/0.0/0.0 | 3/0/0; 1.0/1.0/1.0 | `true`; frozen commit 与全部目标路径已读；`missing_mapping_decoy=/system/status` 在 routes 中但无 exact capability row，`scope_external=/manage/task` 在 routes/map 中却不进 target findings；二者无 FP。注入 decoy mapping 或移除 external mapping 的 synthetic parser 负测均失败；oracle `4522c7...01685` 未变。browser/visual 为 `Not verified`。见 [adjudication](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/adjudication.json) 与 [oracle](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/oracle.json)。 | F1 +1.0；precision 未降；无新增 FP。 |
| [02: source coverage audit](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/README.md) | 固定 coverage manifest/batches 的 source-role 覆盖；treatment 为 validator + normalized records。 | 0/12/60; 0.0/0.0/0.0 | 60/0/0; 1.0/1.0/1.0 | `true`; validator exit 0、errors=0、counts match。remote path/blob/locator 为 `Not verified`。见 [adjudication](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/adjudication.json) 与 [oracle](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/oracle.json)。 | F1 +1.0；precision 未降；FP 从 12 降至 0，无新增 FP。 |
| [03: isolated knowledge patch](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/README.md) | 隔离 IR 副本的精确 mutation、diff、validator 与 receipt；treatment 为 fail-closed 最小 workspace/target containment 规则。 | 0/0/5; 0.0/0.0/0.0 | 5/0/0; 1.0/1.0/1.0 | `true`; source/forbidden paths unchanged、scoped diff、validator exit 0、target/workspace match、无 residual permissions。sibling、absolute、`..` 与 symlink target 均在 write/delete 前 nonzero；oracle `887799...26634` 未变。见 [adjudication](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/adjudication.json) 与 [oracle](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/oracle.json)。 | F1 +1.0；precision 未降；无新增 FP。 |

三项准确数值来自各案 runs 与 adjudication：Case 01 的 [baseline](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/runs/baseline.json) / [treatment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/runs/treatment.json)，Case 02 的 [baseline](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/runs/baseline.json) / [treatment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/runs/treatment.json)，以及 Case 03 的 [baseline](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/runs/baseline.json) / [treatment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/runs/treatment.json)。各案 summary 分别见 [01](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit/summary.md)、[02](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit/summary.md)、[03](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch/summary.md)。

## Gate assessment

| Required condition | Status | Evidence-bounded conclusion |
|---|---|---|
| At least two heterogeneous positive lifts | Pass, within task shape | 三案分别是导航审计、source coverage 审计、隔离知识补丁；均为 F1 0.0→1.0。 |
| Precision non-decrease | Pass, within the recorded metrics | 每案由 0.0 到 1.0。 |
| No new false positives | Pass, within the recorded metrics | Case 01/03 的 FP 保持 0；Case 02 从 12 降至 0。 |
| Independent negative boundary case | **Not satisfied** | 当前没有一项单独冻结的 treatment 负边界，去证明规则在不应触发时 fail closed、且经独立 oracle/adjudication 评分。Case 03 的 baseline 越界/无证据完成是正向 treatment 的反例，不是 treatment 的负边界。 |

因此，三个正向 paired results 不能单独通过 production-Skill gate：缺少负边界即为 `no-promotion`。下次重审前，必须为同一候选规则加入一个预注册、冻结的负案例，并保留 baseline/treatment、oracle 与 adjudication，证明 treatment 不会在合理的非目标输入上制造 finding、越权 mutation 或无证据完成。

三案任务形态彼此异构，但仍是同一 workspace 中的规则实验；它们不构成跨应用或跨仓库泛化样本。跨应用/仓库泛化、真实 agent/provider 行为、浏览器行为与生产运行时均为 `Not verified`。Case 01 只验证固定 Git-object 的 source path；Case 02 的本地 coverage 已通过 60/60，但当前 `--verify-remote` 因无法连接 `api.github.com` 为 `Not verified`；Case 03 没有打开外部 credential、browser profile、MCP session 或生产副作用。

## Interpretation boundary

这些是以预注册 oracle、固定输入和脚本化 baseline/treatment 得到的 paired evidence。它们证明本地规则在给定 basis 与固定 mock/脚本条件下满足本案 oracle，不证明真实模型会遵守规则、不同 provider 会取得相同结果，或生产任务的 precision/recall 会保持不变。生产 Skill 至少还需要：

1. 上述独立负边界 case；
2. 跨应用或跨仓库的冻结任务复现；
3. 对真实 agent/provider、浏览器或运行时结论所需的独立 run/replay 证据；
4. 没有将实验固定 oracle、mock 策略或 case-specific path 直接固化为默认生产指令的审查记录。

旧 repo-review benchmark summary 仅作历史对照：它使用不同案例与 treatment，不参与本轮任何 TP/FP/FN 或 gate 数值；该历史资料未纳入本次公开仓库范围。

## Recheck commands

```sh
# Set these to clones in any filesystem location; no sibling-directory layout is required.
export AI_HANDBOOK_ROOT="${AI_HANDBOOK_ROOT:?Set AI_HANDBOOK_ROOT to a clone of idaibin/ai-handbook}"
export RUSTZEN_ADMIN_REPO="${RUSTZEN_ADMIN_REPO:?Set RUSTZEN_ADMIN_REPO to the RustZen Admin repository}"
export KNOWLEDGE_DISTILLATION_ROOT="${KNOWLEDGE_DISTILLATION_ROOT:-$(git rev-parse --show-toplevel)}"

(cd "$AI_HANDBOOK_ROOT/experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit" && python3 run_experiment.py)
(cd "$AI_HANDBOOK_ROOT/experiments/ai-capability-clusters/applications/case-02-source-coverage-audit" && python3 run_experiment.py)
(cd "$AI_HANDBOOK_ROOT/experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch" && python3 run_experiment.py)
git diff --check --no-index /dev/null skill-feedback/2026-08-03-ai-knowledge-engineering-v1-skill-gate-assessment.md
```
