# Agent Tool Authorization and Execution Boundaries

## Problem

Agent 能调用工具，并不等于当前用户已经授权这次调用。需要把工具发现、身份、目标、参数、审批、沙箱和结果验证拆开处理。

## Required context

- 操作类型与真实副作用；
- 执行主体、目标、数据范围和凭证；
- 可接受的本地与外部风险；
- 可用的隔离、审批、回读与撤销机制。

## Steps

1. 分类真实副作用：只读、本地写入、外部写入、特权、破坏性或难恢复。
2. 明确主体、用户意图、目标、数据边界与所需凭证；缺失时停止。
3. 限制到最小工具集、账号、目录、域名和参数，并验证相邻目标被拒绝。
4. 选择能限制文件、进程、浏览器身份、网络和 Secret 的执行边界。
5. 对未被精确授权的重大操作，在执行前展示具体目标与后果并请求审批。
6. 【本地综合假设，待验证】单次执行，保存工具结果与外部 receipt（如有），再回读目标状态验证后置条件。
7. 【本地综合假设，待验证】撤销临时会话、挂载、凭证或浏览器访问，记录未闭合副作用。

## Boundaries

- 沙箱限制本地爆炸半径，但不授权消息、购买、发布、删除或生产变更。
- 类型校验只约束参数结构，不证明权限、事实或后置条件。
- 已连接、已登录或存在 MCP endpoint 都不是当前调用的授权证据。
- README 证据均为 `source_supported`，没有独立证明生产安全性。

## Anti-patterns

- **Connected means permitted**：把能调用误当成能执行；补齐主体、目标、参数和当前授权。
- **Sandbox as universal permission**：把隔离误当外部授权；分离 blast-radius 与 approval。
- **Success response as completion**：只看返回成功；【本地综合假设，待验证】增加 receipt 与目标状态回读。

## Source trace

- `modelcontextprotocol/servers@76d64c8` — README warning and reference-server scope
- `ComposioHQ/composio@f1c1aa5` — README lines 27–38, 55–57, 96–98
- `browser-use/browser-use@f0aa3a8` — README browser actions and authentication FAQ
- `OpenHands/OpenHands@2feab55` — README Quickstart sandbox warnings
- `pydantic/pydantic-ai@6e96a74` — README Human-in-the-Loop Tool Approval

步骤 6-7 与 receipt/readback/revocation 规则是待任务级验证的本地综合假设，不是这些 README 已直接支持的要求。当前最高等级为 Level 3 Framework；只有跨工具行为测试通过后，才能生成 Skill。
