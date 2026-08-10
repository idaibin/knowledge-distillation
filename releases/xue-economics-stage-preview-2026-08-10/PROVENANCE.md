# Provenance、边界与校验

## 来源边界

- 源仓库：`/Users/daibin/Codex/repos/knowledge-distillation`，当前快照源目录：`.codex/artifacts/dedao-xue-economics-course-system/card-production/<story>/`。
- 本 release 只从三个故事目录复制：`broken-window-unseen-cost`、`cooperation-with-rules-v2`、`riverbend-farm-rule-adaptation`。
- 每包复制 `final/` 完整目录、根级 `final-checkpoint.yaml`、存在的 `content-checkpoint.yaml` / `production-package.yaml`、story/text/storyboard/card-plan/visual-plan/continuity-ledger/browser-operation 等 basis，以及 `review-control/` 下支持当前状态的 `.md` / `.yaml`。候选图、缩略图、contact sheet、prompt 和其它历史大图不在 release。
- `broken-window-unseen-cost/browser-operation.source.txt` 保留源 `.codex/.../browser-operation.yaml` 的原始字节，不改内容、不改 SHA。该上游账本在同一 mapping 内重复出现同值 `status` 键，strict unique-key YAML loader 会拒绝；因此 release 以 `.source.txt` 标记为原样 provenance，而不是创建 wrapper 或声称其可解析。复制的 `final-checkpoint.yaml` / manifest 保留上游原路径和原字节；release 不宣称可直接重跑原 hash chain，原始账本实际文件名以 `.source.txt` 为准。
- `.gitattributes` 仅声明 `packages/** whitespace=-blank-at-eof`。七个源快照文件仍逐字保留 EOF 空行；该属性让 Git 的 staged whitespace 检查跳过这一既有字节特征，属于 byte-faithful snapshot 例外，不改变任何快照或源资产。
- 当前 snapshot 没有复制 `.codex` 之外的课程正文，也没有把付费页面或 provider prompt 当作正文来源；生成图是原创情景化产物，IR 仅保留去版权化的机制、定位和边界。

## 源快照锚点 SHA-256

以下 SHA 是复制前源文件的 SHA；release 内所有实际文件（包括这些锚点文件的副本）以 [SHA256SUMS](SHA256SUMS) 为准。路径均相对于 `.codex/artifacts/dedao-xue-economics-course-system/card-production/`。

### broken-window-unseen-cost

| 源相对路径 | SHA-256 |
| --- | --- |
| `broken-window-unseen-cost/final/story.html` | `e354c46236a28fbcdffd91eba7a552cf4130a0a4f4a2882fc17ec89ae6a65a2f` |
| `broken-window-unseen-cost/final/story-manifest.yaml` | `92b9c80d4afd904689793454e2957f50b2519d9797eeddae513c1760340618e6` |
| `broken-window-unseen-cost/final-checkpoint.yaml` | `08a202ae2277a1ad45f45e19b8a92f3ad5678972c1b421d9d5a84bb1b6f82b3d` |
| `broken-window-unseen-cost/content-checkpoint.yaml` | `6f56e8b8ea2bafe5e59c57904cf6a877a1070f4aabd75845838779dd417dd90` |
| `broken-window-unseen-cost/production-package.yaml` | `73f1504f4fdd98bba2a749f9635b4e7d8ea8a6fdc12c91704143ecc425d73940` |
| `broken-window-unseen-cost/browser-operation.yaml`（release: `browser-operation.source.txt`） | `1b9da1197aaf61da57f0181be290633e4826d3c0e30ba05694d7b995ac80bd47` |

### cooperation-with-rules-v2

| 源相对路径 | SHA-256 |
| --- | --- |
| `cooperation-with-rules-v2/final/story.html` | `8ba44a30956f95c4e719e85f0e96ee37d13f621637e6976a2a855494b3321e6b` |
| `cooperation-with-rules-v2/final/story-manifest.yaml` | `32ef9f842f3a402d6baae9b73690624c260ca7145efbf6b8ab43e4f410d87e83` |
| `cooperation-with-rules-v2/final-checkpoint.yaml` | `c17b8b2fcc3c19319986b9877fd273af8c4e238652c61c9d2f55d736e2eda82a` |
| `cooperation-with-rules-v2/content-checkpoint.yaml` | `75a3d1fde0d15f4652cde7259808df2bc0f5c29204482ff4103408f382a5f539` |
| `cooperation-with-rules-v2/review-control/browser-operation.yaml` | `2045ca83f66ab9138fea018a4576af679c5ac264d2f1a7bc91ac233798511650` |

### riverbend-farm-rule-adaptation

| 源相对路径 | SHA-256 |
| --- | --- |
| `riverbend-farm-rule-adaptation/final/story.html` | `ba544454ca1a11ed2be76a876ed2a39c96ad1285b50b6a8681fa2f00e105444a` |
| `riverbend-farm-rule-adaptation/final/story-manifest.yaml` | `ce962c83b4d2bf70e78c68074f5397a6b436e752e663e844fd46fcf2802d5b96` |
| `riverbend-farm-rule-adaptation/final-checkpoint.yaml` | `f7f5cae7956338640645076b34d05984597483afc29493cf9443f3ddf6281c4e` |
| `riverbend-farm-rule-adaptation/content-checkpoint.yaml` | `3081c04851b993ac5c9d5ce81b79e946a884f599d08412f8471c4a979b4f603c` |
| `riverbend-farm-rule-adaptation/production-package.yaml` | `88bce97d811958be46f067e6e5126523d2fb3a8020ee702f2994252e60657918` |
| `riverbend-farm-rule-adaptation/browser-operation.yaml` | `18b79bf555de8a2d3478dabbd4cb2e6d8b2c6cb481237eba03a261a89c2f9a60` |

## 生成图与审查边界

- 每包 `final/cards/001.png`–`007.png` 是当前选定的七张生成图；没有把 provider 候选、r1/r2/r3 缩略图或 contact sheet 混入精选快照。
- `broken-window-unseen-cost`：本地七卡、HTML、尺寸和 independent full-package r2 记录通过；ChatGPT Review Control 仍 pending，ZCode 仅 text-only，视觉 `Not verified`，`formal=false`。
- `cooperation-with-rules-v2`：本地七卡/HTML/尺寸通过；Review Control 在 locked Mac file chooser 阶段阻塞，ZCode 视觉 `Not verified`，`formal=false`。
- `riverbend-farm-rule-adaptation`：ZCode text/HTML reconciliation 与生命周期闭环可追踪，Sol 当前独立整包记录 `2/2 pass`；live mobile、Review Control/browser runtime 外部视觉仍 `Not verified`，`formal=false`。
- Riverbend 的交接顺序应理解为 `ZCode 持久会话 → 本地执行/协调修订（执行代理模型身份 Not verified） → Sol 复审 → 再修订 → 第二次 Sol 复审`；没有可核验的独立 Luna/model metadata，本快照不将其推断为已完成审查。正式证据以 `review-control/text-html-reconciliation-2026-08-10.yaml`、`zcode-lifecycle-round2-reconciliation-2026-08-10.yaml`、`independent-final-review-sol.yaml` 和 `independent-final-review-sol-b.yaml` 及 SHA 为准。

## Not verified 与隐私扫描解释

`Not verified` 是有意保留的证据状态，不等同于通过或失败：包括 live browser/runtime、live mobile render、未接收像素的 ZCode 视觉轴，以及尚未提交的 Review Control。`browser-operation.yaml` / `browser-operation.source.txt` 中的 `authorization`、`authenticated_session`、project/conversation/file ID 是操作 provenance 的普通字段，不是凭据；release 不包含 token、password、cookie、Bearer/API secret 或可复用授权材料。最终 `rg` 扫描结果与排除说明由交付验证记录回传。
