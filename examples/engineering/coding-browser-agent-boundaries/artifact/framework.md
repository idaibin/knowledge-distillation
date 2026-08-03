# Coding and Browser Agent Boundaries

## Problem

判断 coding/browser agent 是否可以执行，以及是否以受控 workspace/profile/network/credential 和动作预算完成目标，而不是把 agent 成功文案当作证明。

## Required context

- 任务、批准的 repository/workspace、browser profile/context、network/domain、credential class；
- tools/skills、mutation class、命令/导航/提交动作预算、timeout/max_failures；
- 预期代码 diff 或 DOM postcondition、测试/断言、receipt 格式与撤销路径。

## Steps

1. 冻结 intent、workspace、profile、网络、凭证、工具、动作预算和预期 diff/DOM。缺一项停止。
2. 选最窄 runtime 和 isolation（Docker/project mount、浏览器会话、domain allowlist、secret broker、command/file adapter），列出可达文件、进程、浏览器态和网络。
3. 配置 task/model/tools/skills、timeout、max_failures 和预算；禁用无关能力，禁止跨任务复用 profile/credential。
4. 每次命令、写文件、表单提交、有副作用导航或凭证使用前，展示精确 target、参数、后果和剩余预算，取得不可转移的当前审批。
5. 在预算内执行并记录 run id、profile、URL/selector、命令、错误、凭证句柄（不含 secret）。漂移、超时、预算耗尽或日志缺失即停止/unknown。
6. Coding：检查 scoped diff 并跑目标测试；Browser：断言 DOM/state 并保存非敏感 receipt/screenshot reference。
7. 撤销临时 credential/session/mount/profile/network exception，记录残留副作用；无 revoke 或 postcondition 证据不得宣称完成。

## Branches and outputs

- **Deny**：边界或审批缺失/越界；输出 `denial_record` 与未执行证明。
- **Unknown**：执行过但 diff/test/DOM/receipt/revoke 缺失或冲突；输出事件、缺口和隔离动作。
- **Verified completion**：审批、scoped diff/DOM、目标测试/断言、receipt 和 revoke 均可追溯；输出 `run_manifest`、`mutation_record`、`postcondition_record`、`revocation_record`。

## Stop conditions

- dockerless host filesystem/network 或 mounted project scope 未被明确批准；
- browser profile、domain、credential、target 或动作预算漂移；
- 只保存 agent success、diff 或 form submission，没有独立 test/DOM/receipt；
- 将 hosted cloud 能力或构造器参数当成本地运行时隔离与安全证明。

## Boundaries

OpenHands 固定提交说明 dockerless Agent Server 可访问 host filesystem、执行 shell 并访问 network；project mount 仍授予 mount 范围。Browser-use 区分 OSS 与 hosted cloud，构造器参数不证明循环、工具执行或 browser watchdog 的安全性。当前未运行真实 workspace、browser、provider、DOM、receipt 或 revoke。

## Anti-patterns

- **Mount/profile means permission**：可达即获准；改为逐字段边界和逐次审批。
- **Constructor controls equal safety**：timeout/max_failures/tools 参数即安全；改为运行时拒绝和预算耗尽测试。
- **Diff/browser success equals completion**：成功文案即完成；要求独立 diff/test/DOM/receipt/revoke，否则 `unknown`。

## Source trace

- `OpenHands/OpenHands@2feab55` — `README.md` blob `973cbf1…`; `docs/architecture.md` blob `14bbf01…`; `docs/SELF_HOSTING.md` blob `7b8cc12…`; `src/api/runtime-service/agent-server-runtime-service.ts` blob `83d4584…`; mocked test blob `e37bdb3…`。
- `browser-use/browser-use@f0aa3a8` — `README.md` blob `4eec683…`; `browser_use/agent/service.py` blob `4bee7b6…`。

## Fixed experiment trace

- [ai-handbook coding/browser experiment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/coding-browser-agent/README.md) — recorded local mock/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `c1219ecbfb673bb5ea495b7f6d53bb44bdd703a07a7f5565fdaa51118bf23bdc`; `runs/treatment.json` SHA-256 `e0cccaf14627f6b9676ce6a73330d6f3fe10b5d1f5eaff5138fe70ee64eed2a9`. It independently verifies only the mock workspace/DOM fixture policy, approval, diff, DOM, and receipt contract, not a real browser, workspace, credential, sandbox, or production behavior.

以上 source trace 只支持边界和能力描述。当前为 Level 3 draft，绝非 Level 4 或 Skill；真实 diff/test/DOM/receipt/revoke 仍需运行时验证。
