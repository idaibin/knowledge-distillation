# 薛兆丰经济学故事卡：阶段预览快照

日期：2026-08-10

这是一个可追踪的阶段交付目录，不是正式发布包，也不是课程正文镜像。它只收录三套当前 HTML 预览和支持当前状态的最小文字、YAML、审查与生成 provenance；历史候选图、缩略图、contact sheet、prompt 和付费正文均不复制。

`broken-window-unseen-cost/browser-operation.source.txt` 是上游 `browser-operation.yaml` 的历史账本原样字节快照（SHA-256 不变：`1b9da119…ac80bd47`）。源账本在同一 mapping 内重复出现同值 `status` 键，严格 unique-key YAML 解析会拒绝它；因此 release 不把它伪装成可解析 YAML，也不创建 wrapper。复制的 `final-checkpoint.yaml` / manifest 保留上游原路径和原字节；release 明确不宣称可直接重跑原 hash chain，原始账本实际文件名以 `.source.txt` 为准。

release 根的 `.gitattributes` 是 byte-faithful snapshot 例外：仅对 `packages/**` 设置 `whitespace=-blank-at-eof`，使 Git 暂存检查忽略源快照原有的 EOF 空行，不改七个文件的字节内容。该例外只服务于 `git diff --cached --check` 的诊断，不是内容清洗或格式化。

## 当前课程与正式边界

- 目录统计：主干 `213/213`，内容型扩展 `125/206`，全目录 `indexed=338/419`，`remaining=81`。
- 已过 `validated` Gate 的课程：`001, 002, 003, 004, 005, 006, 007, 009`。这只表示对应 IR/source gate 通过，不代表整季课程或故事卡正式发布。
- 现有文档中的 `formal=1` 必须按其真实字段解释：它来自 `catalog_basis.coverage.card_review.locally_reviewed=1`（唯一贡献为 `exchange-without-more` v0.4），不是“正式发布 1 套”。当前 `story_mapping.formally_mapped=0`，因此正式映射仍为 0。
- 当前 manifest card-review counters 为 `drafted=1`、`locally_reviewed=1`、`externally_reviewed=1`、`learning_records=1`、`learning_applied=0`。本目录中的三套包均明确 `formal=false` / `formal_package_counted=false`。

## 从 IR 到 formal 的完整路径

1. **目录与来源边界**：固定课程目录、来源定位、读取状态和版权边界；付费来源只保留 locator 与经转换的概念/机制，不复制原文。
2. **Knowledge IR**：先形成 `draft` / `source_extracted_draft`，记录输入、机制、反事实、限制、测试和待核验项。
3. **IR Gate**：通过 schema、来源路径与 SHA、locator/evidence 和边界检查后才可标为 `validated`；未验证事实、法律、实证和政策外推继续保持 `Not verified`。
4. **故事生产准备**：将 validated IR 映射为原创 story、text-layer、storyboard、card-plan、visual-plan 与 continuity ledger，冻结角色、数量、持有者、转移状态和时间线。
5. **本地包检查**：生成七张卡，锁定 final 选择并绑定 SHA；执行逐卡 review、数量/同类物排除、320px 主读、1086×1448 尺寸、HTML 静态结构、本地图片引用和旁白一致性检查。
6. **Checkpoint**：`content-checkpoint.yaml` 只允许内容与 IR 进入下一步；`final-checkpoint.yaml` 绑定当前 final manifest、HTML、审查记录和下一步阻塞，不能把本地通过自动升级为 formal。
7. **独立审查与复盘**：按当前 Review Control 合同提交可复现的固定 basis，并用持久 ZCode 会话、独立整包复核（本轮 Riverbend 记录了 Sol 2/2）和必要的文本/HTML reconciliation 处理离散问题；图像未到达审查模型的轴必须保持 `Not verified`。
8. **formal Gate**：只有 validated IR、content/final checkpoints、全部本地与逐帧审查、必需外部审查、版权结论和学习记录都通过，并由 `validate_reviews.py` 形成 `gate.result=pass` 的 review record，才可派生正式计数和 `formally_mapped`。本快照没有新增该计数。

## 三套 HTML 状态

指标顺序为 `article / img / narration / remote resources / visible narrator label`；前三项是结构计数，最后一项是实际可见的 `<strong>旁白</strong>` 标签计数。

| 包 | HTML | 本地结构 | 可见旁白标签 | 当前审查边界 | formal |
| --- | --- | --- | ---: | --- | --- |
| `broken-window-unseen-cost` | [story.html](packages/broken-window-unseen-cost/final/story.html) | `7 / 7 / 7 / 0` | 7 | 本地 final/HTML 通过；ChatGPT Review Control 当前 pending，ZCode 为 text-only，视觉 `Not verified` | `false` |
| `cooperation-with-rules-v2` | [story.html](packages/cooperation-with-rules-v2/final/story.html) | `7 / 7 / 7 / 0` | 7 | 本地 final/HTML 通过；ChatGPT Review Control 被 locked Mac file chooser 阻塞，ZCode 视觉 `Not verified` | `false` |
| `riverbend-farm-rule-adaptation` | [story.html](packages/riverbend-farm-rule-adaptation/final/story.html) | `7 / 7 / 7 / 0` | 0 | ZCode 文本/HTML reconciliation 已完成，Sol 当前整包复核 `2/2 pass`；live mobile/browser external visual 仍 `Not verified` | `false` |

前两套保留源 HTML 的七个可见旁白标签，未在本轮改写；这是已知的历史预览缺口，不能声称已完成“可见旁白 0”优化。Riverbend 本轮已移除七个标签，但七段 narration 文本、图片字节和七卡结构保持不变。三套均无远程资源，浏览器打开 HTML 时使用包内 `final/cards/*.png`。

## Riverbend 本轮迭代

本轮按 `ZCode 持久会话 → 本地执行/协调修订（执行代理模型身份 Not verified） → Sol 复审 → 再修订 → 第二次 Sol 复审` 的交接顺序处理；不把任何未落盘的 Luna/model 身份写成已验证结论。交付证据以仓库内可复核文件为准：

- ZCode text/HTML review 先指出生命周期表达需要统一，并发现七个可见 `旁白` 前缀；后续 reconciliation 将 C1–C7（事故、两个候选、首日短期试行、数日后继续试行、比较、未试行基线、程序结语）写入六份 planning/text 文件，补齐 C3/C4/C6 可见过渡，并移除七个 HTML `旁白` 前缀。
- 中间本地执行/协调修订统一采用 ZCode reconciliation 文件中的窄范围变更：统一 C1–C7 生命周期、补齐 C3/C4/C6 可见过渡、移除旁白标签，并保留 immutable 历史记录；执行代理的具体模型身份 `Not verified`。
- Sol 对当前固定 basis 完成两份独立整包 PASS（本地像素范围），确认七卡、七段 narration、0 remote、生命周期与程序性结尾；live mobile/browser external visual 未验证，故仍 `formal=false`。证据路径为 `review-control/text-html-reconciliation-2026-08-10.yaml`、`zcode-lifecycle-round2-reconciliation-2026-08-10.yaml` 和 `independent-final-review-sol*.yaml`。

## 剩余阻塞与版权边界

- 三包都尚未满足可计入 formal 的全部外部/运行时门禁；formal mapping 仍为 0。
- `broken-window-unseen-cost`：当前 basis 的 ChatGPT Review Control 尚 pending，ZCode 视觉未验证。
- `cooperation-with-rules-v2`：ChatGPT Review Control 在提交前被 Mac locked file chooser 阻塞；ZCode 视觉未验证。
- `riverbend-farm-rule-adaptation`：Review Control/browser runtime 外部视觉仍未完成；Sol 的 2/2 是当前本地固定包复核，不替代 live mobile 或正式 external gate。
- 当前 release 不含付费课程正文、逐字稿或长引文；仅含 de-copyrighted IR 绑定、原创故事/卡片文字、生成图 final 快照和审查记录。来源、边界、Not verified 以及源文件 SHA 见 [PROVENANCE.md](PROVENANCE.md)，资产总盘点见 [ASSET-INVENTORY.md](ASSET-INVENTORY.md)，release 文件校验见 [SHA256SUMS](SHA256SUMS)。
