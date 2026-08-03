# MCP Tool Authorization Boundaries

## Problem

决定一次已发现的 MCP 或 Composio 工具调用是否可以执行，并证明其目标后置条件已达成、临时权限已撤销。

## Required context

- operation、side-effect class、principal、session、account/organization、target、data scope、arguments、duration；
- 需要的 MCP server/tool 或 Composio toolkit、版本、transport、sandbox/proxy 与网络边界；
- 可接受的本地/外部风险、精确审批人和拒绝条件。

## Steps

1. 冻结 operation、主体、会话、账号、目标、参数、期限和副作用分类。缺任何字段即停止。
2. 只发现所需 MCP server/tool 或 Composio toolkit，记录 commit、版本、transport 和 session。发现结果必须与请求一一对应。
3. 校验 principal→session→account→target 绑定。`default`、过期、跨组织或未授权目标都拒绝；相邻目标探针必须保持拒绝。
4. 设置最小 allowlist：tool/toolkit、目录或仓库、域名、凭证、sandbox/proxy 和参数 schema；把“配置存在”与“服务端已执行”分开记账。
5. 对外部写入、特权、破坏性或不可逆动作，在逐次调用前展示精确目标、参数、后果和过期时间，取得当前审批。
6. 以 run/idempotency 标识执行一次，保存参数、结果、错误和外部 receipt。没有 receipt 或 receipt 仅来自工具自述时标为 `unknown`。
7. 独立读取目标状态并与预期 postcondition 比对。冲突、部分成功、无法回读或只能依赖成功文案时不关闭任务。
8. 撤销临时 session、连接、token、mount、proxy 或浏览器权限，记录残留副作用和过期；撤销能力未验证则停止发布。

## Branches and outputs

- **Deny**：身份、目标、scope、参数或审批缺失/越界；输出拒绝原因与未执行证明。
- **Execute-but-unknown**：调用完成但 receipt、readback 或 revoke 不可得；输出原始结果、缺口和隔离动作，不宣称完成。
- **Verified completion**：审批、结果、独立 readback 和 revoke 均有可追溯记录；输出 `authorization_record`、`execution_record`、`postcondition_record`、`revocation_record`。

## Stop conditions

- 只能用 connected/login/endpoint/sandbox 证明权限；
- principal/session/account/target 任一绑定不一致；
- 工具结果与独立目标状态冲突，或副作用可能部分发生；
- 发现的配置或 README 被当作运行时授权、租户隔离、receipt、readback 或 revoke 证据。

## Boundaries

MCP servers 固定提交的 README 明确其为教育性 reference implementations；Composio 配置类型和安全文档是来源支持的描述，不是本环境的服务端执行证明。receipt、readback、revocation 是本地控制假设，当前来源不足时保持 `unverified`。

## Anti-patterns

- **Discovered means allowed**：发现即执行；补齐 principal/session/account/target 和逐次审批。
- **Default identity in multi-user execution**：复用 `default` userId；改用稳定生产标识并验证组织范围。
- **Success response closes the task**：只看成功文案；要求独立 readback、receipt 和 revoke，否则输出 `unknown`。

## Source trace

- `modelcontextprotocol/servers@76d64c8` — `README.md` blob `fe5351a…`; `src/fetch/tests/test_server.py` blob `96c1cb3…`; `src/fetch/src/mcp_server_fetch/server.py` blob `b42c7b1…`。
- `ComposioHQ/composio@f1c1aa5` — `README.md` blob `951b2ea…`; `ts/docs/core-concepts.md` blob `35ae0a0…`; `docs/content/docs/security/overview.mdx` blob `13a2a857a5812911509ea12ba150bfb638012343`; `python/composio/core/models/tool_router.py` blob `2994995…`。

## Fixed experiment trace

- [ai-handbook MCP experiment](https://github.com/idaibin/ai-handbook/blob/main/experiments/ai-capability-clusters/mcp-tools/README.md) — recorded local fake-server/fixture observation: `python3 run_experiment.py`; `runs/baseline.json` SHA-256 `1fc1868772343d2e27788e7cf611fa17dd0a13cf9364c5e61cf70741a33ec52f`; `runs/treatment.json` SHA-256 `38874556525b09a4faf68e2d441c4c8e3cb62b4385890ec684efaf384a57b3df`. It independently verifies only the fake-server/fixture receipt, readback, and revoke contract, not real MCP, identity, network, or production behavior.

以上 source trace 仅支持发现、身份、账号范围、隔离与策略分支。当前为 Level 3 draft，绝非 Level 4 或 Skill；真实 receipt/readback/revoke 仍待运行时验证。
