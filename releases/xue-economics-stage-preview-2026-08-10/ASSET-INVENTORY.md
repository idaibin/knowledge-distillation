# 资产盘点

## 口径

源资产口径为仓库内 `.codex/artifacts/` 的 regular files（不含目录项；无 symlink）。字节数使用文件 `stat` 的逻辑长度，MiB 使用 `bytes / 1024^2`；`du` 是文件系统分配的磁盘占用，二者不等价。源盘点因此为 **790 files / 494,670,096 B / 471.754166 MiB**。

| 来源分组 | 文件数 | stat bytes | MiB |
| --- | ---: | ---: | ---: |
| `dedao-xue-economics-001-005/` | 124 | 254,786,123 | 242.982982 |
| `dedao-xue-economics-course-system/` | 666 | 239,883,973 | 228.771184 |
| **合计** | **790** | **494,670,096** | **471.754166** |

## 文件类型

| 类型 | 文件数 | stat bytes | MiB |
| --- | ---: | ---: | ---: |
| `.png` | 227 | 363,317,141 | 346.486226 |
| `.zip` | 5 | 126,747,626 | 120.875956 |
| `.yaml` | 451 | 3,332,546 | 3.178164 |
| `.md` | 86 | 807,885 | 0.770459 |
| `.pyc` | 6 | 262,844 | 0.250668 |
| `.py` | 6 | 164,624 | 0.156998 |
| `.html` | 3 | 25,819 | 0.024623 |
| `.json` | 5 | 7,552 | 0.007202 |
| `.sh` | 1 | 4,059 | 0.003871 |
| **合计** | **790** | **494,670,096** | **471.754166** |

## course-system 分组

| 子组 | 文件数 | stat bytes | MiB |
| --- | ---: | ---: | ---: |
| `card-production/` | 311 | 236,173,924 | 225.233006 |
| `lessons/` | 208 | 1,871,538 | 1.784054 |
| `supplementary/` | 125 | 647,167 | 0.616996 |
| `reviews/` | 15 | 453,694 | 0.432594 |
| 顶层 7 份规划/索引 Markdown/YAML | 7 | 737,650 | 0.703478 |
| **合计** | **666** | **239,883,973** | **228.771184** |

> 顶层 7 份文件为 `card-plan.md`、`concept-taxonomy.md`、`course-map.md`、`lesson-manifest.yaml`、`review-learning-loop.md`、`season-outline.md`、`story-bible.md`；其 bytes 合计为 `73,699+189,508+76,262+164,656+96,954+57,447+79,124=737,650`。

## 每个 card-production 故事目录

`final/` 是目录内的精选最终快照；`non-final` 是候选、历史 review、操作记录和其它非 final 文件。这里的 `non-final` 只用于源盘点，不表示它们被复制进本 release。

| 故事目录 | 全部文件 | 全部 stat bytes | final 文件 / bytes | non-final 文件 / bytes |
| --- | ---: | ---: | ---: | ---: |
| `broken-window-unseen-cost` | 104 | 66,613,282 | 9 / 16,346,843 | 95 / 50,266,439 |
| `cooperation-with-rules` | 9 | 5,526,339 | 0 / 0 | 9 / 5,526,339 |
| `cooperation-with-rules-v2` | 70 | 49,725,959 | 9 / 16,867,489 | 61 / 32,858,470 |
| `durable-apple-service-validation` | 5 | 11,863,941 | 0 / 0 | 5 / 11,863,941 |
| `exchange-without-more` | 35 | 48,485,931 | 7 / 21,317,150 | 28 / 27,168,781 |
| `riverbend-farm-rule-adaptation` | 87 | 53,950,979 | 10 / 20,364,275 | 77 / 33,586,704 |

## 本 release 三套包的 final / non-final 对照

| 包 | final 快照 | non-final 源历史 | 选入 release（文件 / stat bytes） |
| --- | ---: | ---: | ---: |
| `broken-window-unseen-cost` | 9 / 16,346,843 B | 95 / 50,266,439 B | 24 / 16,524,519 B |
| `cooperation-with-rules-v2` | 9 / 16,867,489 B | 61 / 32,858,470 B | 30 / 16,955,499 B |
| `riverbend-farm-rule-adaptation` | 10 / 20,364,275 B | 77 / 33,586,704 B | 32 / 20,579,838 B |
| **三包** | **28 / 53,578,607 B** | **233 / 116,711,613 B** | **86 / 54,059,856 B（文档与 SHA 文件加入前）** |

## Top 20（源 `.codex/artifacts/`，按 stat bytes 降序）

| # | 文件 | bytes |
| ---: | --- | ---: |
| 1 | `dedao-xue-economics-001-005/economics-cards-001-005-v2.zip` | 54,820,165 |
| 2 | `dedao-xue-economics-001-005/economics-cards-001-005-v3-compact.zip` | 39,470,865 |
| 3 | `dedao-xue-economics-001-005/economics-cards-lesson-001-v5-full-image.zip` | 25,888,427 |
| 4 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/review-control/riverbend-contact-sheet.png` | 5,447,545 |
| 5 | `dedao-xue-economics-course-system/card-production/exchange-without-more/final/contact-sheet.png` | 5,419,551 |
| 6 | `dedao-xue-economics-001-005/exports/v5-full-image/001/001-03.png` | 3,485,292 |
| 7 | `dedao-xue-economics-001-005/exports/v5-full-image/001/001-04.png` | 3,460,416 |
| 8 | `dedao-xue-economics-course-system/card-production/durable-apple-service-validation/candidates/001-v1.png` | 3,341,031 |
| 9 | `dedao-xue-economics-001-005/exports/v5-full-image/001/001-02.png` | 3,325,814 |
| 10 | `dedao-xue-economics-001-005/economics-cards-001-005.zip` | 3,289,309 |
| 11 | `dedao-xue-economics-001-005/economics-cards-001-005-portable.zip` | 3,278,860 |
| 12 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/card-005.png` | 3,150,688 |
| 13 | `dedao-xue-economics-001-005/exports/v5-full-image/001/001-05.png` | 3,118,568 |
| 14 | `dedao-xue-economics-001-005/exports/v5-full-image/001/001-01.png` | 3,108,399 |
| 15 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/card-002.png` | 3,085,552 |
| 16 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/final/cards/002.png` | 3,085,552 |
| 17 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/card-004.png` | 3,069,222 |
| 18 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/final/cards/004.png` | 3,069,222 |
| 19 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/card-003.png` | 3,066,052 |
| 20 | `dedao-xue-economics-course-system/card-production/riverbend-farm-rule-adaptation/final/cards/003.png` | 3,066,052 |

## Release 实际占用（含文档与 SHA256SUMS）

阶段 release v03 归档固定绑定 commit `096c4cf32c2828557c3b556b4c5f877206ebd6ff`，内容基线为 **97 files / 54,241,825 B / 51.729035 MiB**；后续对索引文字或校验记录的修订不反向冒充该不可变归档基线。

当前 release 目录含新增元数据后为 **97 files / 54,242,186 B / 51.729380 MiB**（`SHA256SUMS` 自身 12,459 B；它不参与自身哈希）。文件系统分配占用为 **53,152 KiB**（`du -sk`，约 52M），与 stat 逻辑字节不同。三包目录仍为 86 files / 54,059,856 B；其余 11 个根级文件合计 182,330 B。

release 内可按 strict unique-key loader 解析的 YAML 为 **50 files**；上游重复键账本 `packages/broken-window-unseen-cost/browser-operation.source.txt` 保留原字节但不计入 YAML。

复算命令：

```sh
find releases/xue-economics-stage-preview-2026-08-10 -type f -print0 \
  | xargs -0 stat -f '%z' | awk '{n+=1; b+=$1} END {printf "%d files / %d B / %.6f MiB\n", n, b, b/1024/1024}'
du -sk releases/xue-economics-stage-preview-2026-08-10
```

## Drive 上传盘点

stage 文件已原位替换为绑定 commit `096c4cf32c2828557c3b556b4c5f877206ebd6ff` 的 v03；full-assets 保持通过 exact-set、byte-match 和 SHA-256 审计的 v02。未创建重复项，stage 目录保持 2 项、full-assets 目录保持 9 项，全部通过 metadata readback。逻辑路径以 [DRIVE-ASSET-INDEX.yaml](DRIVE-ASSET-INDEX.yaml) 为准：40-Exports 为 AI Engineering Lab/40-Exports/Review-Packages/xue-economics/2026-08-10-stage-preview，90-Archive 为 AI Engineering Lab/90-Archive/xue-economics/2026-08-10-full-assets。每个分卷低于连接器 100 MiB 限制；完整约 467 MiB tar.gz 仍保留本地，未作为单文件上传。
