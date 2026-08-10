# 课程卡生产流水线规范

本文件是课程卡（course-card）生产的 canonical 流程。它约束从知识证据到可审查阶段交付的顺序、门禁、哈希绑定和资产分层；它不授权抓取付费正文、发布内容、上传外部服务或把本地通过误报为正式发布。

## 适用范围与状态词

- **课程单元**：一个 lesson、chapter 或 transcript segment。先用 batch manifest 固定范围、来源定位、覆盖率和使用边界；覆盖不完整时不得称为“课程总结”。
- **Knowledge IR**：唯一的知识事实来源。故事、卡片、图片和 HTML 都是 IR 的下游派生物。
- **阶段包（stage package）**：可追踪但未必可发布的本地交付物；它可以包含 `formal: false` 的完整 HTML。
- **正式映射（formal mapping）**：只有所有正式门禁通过后，才允许写入正式计数或目录映射。`locally_reviewed`、`externally_reviewed`、`stage release` 都不等于正式映射。
- **Not verified**：证据尚未取得或当前范围没有覆盖。它不是 pass，也不是 fail；必须保留在 checkpoint、review record 和交付报告中。

“通过”只表示当前固定 basis 上的门禁通过。任何上游文字、IR、图片、HTML 或审查输入改变，均使受影响的下游审查和 checkpoint 失效。

## Canonical 顺序

每个课程卡包按以下顺序执行到外部审查；随后分为正式映射与阶段发布两条分支。不得跳过各分支自身门禁或把后置证据倒写到前置状态。

| 阶段 | 必需输入 | 完成条件与证据 | 失败处理 |
| --- | --- | --- | --- |
| 1. IR | batch manifest、来源 locator、使用/版权边界 | `knowledge.yaml` 结构有效；每条 material claim 有 evidence、locator 和边界；推断单独标注；覆盖率与实际读取范围一致 | 保持 `draft`，补证据或缩小主张；不得渲染为正式卡片 |
| 2. `validated` gate | IR、schema、来源与证据检查 | `validate_ir.py` 及相关语义检查通过；IR maturity 设为 `validated`；未核验事实仍为 `Not verified` | 回到 IR；不得生成故事或图片 |
| 3. Story/card basis | validated IR、允许使用的 concept IDs、系列学习记录 | 冻结 `story.yaml`、`text-layer.yaml`、`storyboard.yaml`、`card-plan.yaml`、`visual-plan.yaml`、`continuity-ledger.yaml`；明确每卡 function、因果链、候选/基线、角色与数量；完成内容复审并生成 `content-checkpoint.yaml` | 标记 revision；保留原 basis；不得沿用失效 checkpoint 生成图片 |
| 4. 生图 | 冻结的 card plan、visual plan、单卡 prompt、生成操作 provenance | 每卡只允许一个选定 final；记录 prompt/operation/output SHA、尺寸和来源；候选与失败图保留为历史，不进入 final | 标记 `historical`/`failed`/`revise`；禁止重发、覆盖或作为下一卡 baseline，除非新一轮 basis 明确授权 |
| 5. Native + 320 review | 选定 native 图、320px 缩略图、card basis | 每卡 native 与 320px 主读检查均通过；检查文字、构图、角色/物件数量、连续性、视觉功能、版权与移动可读性；记录 review 文件及 hash | 回到单卡生图或 card basis；旧候选保持不可变历史 |
| 6. HTML | final 图片、冻结 text-layer/narration、story manifest | 本地 HTML 静态检查通过：卡片数、图片数、narration 数一致；所有图片为包内引用；远程资源为 0；响应式断点和移动字号已检查；生成 `final/story-manifest.yaml` | 回到 HTML 组装；HTML 改动会使 final checkpoint 与整包复审失效 |
| 7. Full-package review | final HTML、manifest、所有 final 图片、content checkpoint | 至少两份独立整包复审绑定当前 basis；复核知识保真、叙事连贯、视觉/角色一致性、native/320 结果、移动排版、累计替代风险和学习记录；生成 `final-checkpoint.yaml` | 进入 revision；历史复审保留并标为 `historical_pre_html_fix` 或相应状态，不计入当前通过数 |
| 8. External review | 去版权化的 IR 摘要、story/text/manifest、必要图像和固定 basis | 按 `ZCode → 本地执行/协调 → Sol 独立复审` 处理；若有修订，再按 `ZCode follow-up → 本地执行/协调 → Sol final review` 收口。只发送 transformed artifacts，不发送付费正文、账户数据、浏览器状态或凭据 | 外部会话/视觉证据缺失时保持 `Not verified`；不得把 text-only 或本地像素审查写成 live visual pass |
| 9A. Formal mapping | validated IR、内容/最终 checkpoint、逐卡与整包复审、外部证据、版权结论、学习记录 | 所有必需门禁均为 pass；review record 的 `gate.result=pass`；才可更新 `formally_mapped` 或正式计数 | 维持 `formal=false`、`formally_mapped=0`；记录具体 blocker |
| 9B. Stage release | 已锁定 final 的完整包、审查证据、清单、状态报告 | 选择规则通过；release 仅收录最小可追踪集合；生成 SHA256 清单和 release README；记录 base/head commit、tree、文件数、总字节数和未验证项。9A 未通过时允许生成明确标为 `formal: false` 的阶段预览，但不得正式发布或计数 | 不发布该阶段版本；在本地/Drive 历史区保留候选，修复后从新 basis 重新开始 |

## 两个 review checkpoint

必须有两个不同时间点的 checkpoint：

1. `content-checkpoint.yaml` 在 story/text basis 冻结后建立，绑定 IR SHA、story/text/plan/ledger 的 SHA 和内容复审结果。
2. `final-checkpoint.yaml` 在 final 图片、HTML 和 manifest 冻结后建立，绑定 final text、HTML、manifest、browser-operation、review package 及每一张 final frame 的 SHA。

审查记录可以引用 checkpoint；checkpoint 不反向引用或修改审查记录。任何修改都按新 basis 重跑受影响门禁，不能通过改状态字段“补齐”证据。

## 单向 hash/checkpoint 链

```text
source locator + source SHA
        ↓
validated IR SHA
        ↓
story/text/card/visual/continuity basis SHA
        ↓
content-checkpoint SHA
        ↓
prompt + generation provenance + native frame SHA
        ↓
320px derivative SHA + native/320 review SHA
        ↓
HTML + narration + final manifest SHA
        ↓
final-checkpoint SHA + full-package review SHA
        ↓
external review evidence SHA
        ↓
formal gate / stage release manifest / SHA256SUMS
```

规则：

- 每个下游节点只消费已冻结的上游 SHA，并将自己的输出 SHA 写入下一节点。
- 上游内容、图片、HTML、manifest 或审查 basis 变化时，后续节点全部标为 stale，重新生成；不得沿用旧 review。
- `SHA256SUMS` 覆盖 release 中除自身之外的文件；release README 记录清单摘要，不能替代逐文件校验。
- 原始文件无法严格解析（例如历史 YAML 重复键）时，保留原字节快照并改用 `.source.txt` 等明确名称；不得创建 wrapper 后声称可重跑原 hash chain。

## 审查顺序与证据边界

审查必须按固定 basis 运行，并记录 `repository + base/head commit + scope + exclusions`。推荐的课程卡顺序是：

1. ZCode：文本、HTML、生命周期与审查问题发现。
2. 本地执行/协调：只实施已确认的窄范围修订；执行代理具体模型/角色 metadata 不可见时写 `Not verified`。
3. Sol：独立整包复审，检查知识、叙事、视觉函数、native/320、移动排版和版权边界。
4. 如需修订，重复 ZCode follow-up → 本地执行/协调 → Sol final review；只有最终 basis 的记录计入当前通过数。

External review 的最小 payload 是 batch manifest、去版权化 lesson summary、IR decisions、story/text/manifest 和必要图片。不得发送原始付费课程文本、完整浏览器状态、cookie、token、password、Bearer/API secret 或可复用授权材料。

## 失败候选与历史资产

失败或被替换的候选必须原地保留、标明状态和原因，并与 final 分区：

- `historical_frozen`：曾审查通过但被后续 basis 替代；禁止重发、编辑、移动或作为新卡 baseline。
- `failed` / `revise`：审查发现问题；只能在新 basis 中重新生成，旧文件不可覆盖。
- `excluded_history`：保留用于 provenance，但不计入 final card count、HTML 或 formal mapping。

release 只选择当前 final manifest 明确引用且所有本地门禁通过的资产；历史候选可以进入本地/Drive archive，但不能混入 release 的 `final/`、正式计数或 HTML。

## Asset 分层：Git、工作树与 Google Drive

| 层 | 保存内容 | 是否进 Git | 规则 |
| --- | --- | --- | --- |
| 本地工作资产（通常 `.codex/artifacts`） | 原始读取 provenance、候选/失败图、prompt、浏览器操作记录、临时缩略图和授权边界 | 否，除非明确选入 release | 可复现生产和审查；不得把付费正文或凭据复制进仓库 |
| Git 追踪层 | 去版权化 IR 绑定、最终 story/text/plan、final 图片、HTML、manifest、checkpoint、review evidence、`PROVENANCE.md`、`ASSET-INVENTORY.md`、`SHA256SUMS` | 是 | 小而完整、可审查；每个 release 绑定 commit/tree；不把整个 `.codex` 强行加入 Git |
| Google Drive 规范目录 | 全量资产归档（final、历史候选、失败记录、contact sheet、必要 provenance）以及面向协作的预览 | 否（外部归档） | 按治理仓库的 storage policy 分层；Git 索引只记录逻辑路径、文件名、字节数、SHA 和同步状态，不记录真实 Drive ID/URL；真实 ID 仅保留在连接器或本地私有证据中；未实际验证前状态写 `Not verified` |

Git release 与 Drive archive 必须通过同一份 manifest 对齐；Drive 不是 Git 的替代品，Git 也不是全量二进制资产仓库。任何外部上传都必须在交付报告中单独报告“已上传/失败/Not verified”，不能由本地文件存在推断上传成功。

## Release 选择与工作树门禁

发布阶段包前必须记录：

- `git status --short --branch`、当前 branch、base/head commit 和 tree；
- release 路径、文件数、总字节数、`SHA256SUMS` 摘要；
- final card count、HTML 静态检查、远程资源数、review 计数、formal 状态和所有 `Not verified` 项；
- release 是否仅为本地提交、是否已推送、Drive 上传状态。

`knowledge-distillation` 的 release 工作树必须完全干净；其它仓库（如 `ai-handbook`）可以保留与本任务无关的既有修改，但只能提交明确同步的台账/索引文件。未授权时不执行 push、deploy、删除或覆盖外部资产。

## 最小交付清单

每个 stage release 至少包含：

```text
README.md
PROVENANCE.md
ASSET-INVENTORY.md
SHA256SUMS
packages/<story>/story.yaml
packages/<story>/text-layer.yaml
packages/<story>/storyboard.yaml
packages/<story>/card-plan.yaml
packages/<story>/visual-plan.yaml
packages/<story>/continuity-ledger.yaml
packages/<story>/content-checkpoint.yaml
packages/<story>/final-checkpoint.yaml
packages/<story>/final/story.html
packages/<story>/final/story-manifest.yaml
packages/<story>/final/cards/*.png
packages/<story>/review-control/*（仅必要的审查证据）
```

交付报告必须区分：已验证事实、推断、`Not verified`、阻塞责任人、剩余风险；不能用测试数量、会话数量或本地文件数量代替业务完成度。
