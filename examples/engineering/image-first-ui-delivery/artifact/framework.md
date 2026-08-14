# Image-First UI Delivery With Implementation Closure

## Problem

生成图擅长快速确定构图、层级、配色和资产方向，但它不会自动提供真实组件、响应式行为、交互状态或运行证据。把图片直接当实现规范，会造成尺寸失真、组件伪造和“看起来完成”的假闭环。

## Required context

- 本地 UI 规范、真实业务内容和明确排除项；
- 目标组件库、既有 Token、交互与状态所有者；
- 固定视口和关键状态验收矩阵；
- 完整、版本化的生图提示词；
- 提供方会话、原图尺寸、哈希和完成证据；
- 目标项目的源码、构建、浏览器和运行时证据。

## Seven-step loop

1. **冻结本地规范**：明确页面任务、画布、组件约束、真实内容、状态和排除项。Check：规范能够拒绝“漂亮但虚构”的图片。
2. **生成完整提示词**：提示词只从本地规范派生，并在发送前版本化。Check：包含精确画布、构图、禁止项和单轮停止条件。
3. **单次提交并留证**：记录操作、会话、完成状态、提供方原图尺寸和哈希。Check：中断只回查原操作，不重复发送。
4. **审查候选图**：核对层级、密度、文字、组件真实性、产品事实、无障碍影响和原生尺寸。Check：放大图不能冒充原生目标画布。
5. **先改本地文件再迭代**：每轮调整先修改 UI 规范和完整提示词。Check：聊天历史不是唯一设计依据。
6. **按现有组件系统实现**：把视觉方向翻译成目标项目已有组件、Token、数据状态和响应式布局。Check：不把生成像素描成装饰性假控件。
7. **在运行页面验收**：按固定视口和关键状态验证，记录截图、功能检查、与候选图的差异和风险。Check：图片、源码、构建、浏览器和生产证据分开报告。

## What the Neo Mirai case contributes

Impeccable 的 [Neo Mirai 案例](https://impeccable.style/cases/neo-mirai/) 展示了“高保真方向图 → 品牌与资产拆解 → 语义化响应式实现 → 浏览器修正”的闭环。可迁移的是流程：图像作为 north star、图片资产与 HTML/CSS 分工、浏览器逐轮修正。不可直接迁移的是该活动营销站的日式复古视觉语言。

## Boundaries

- 生成图是视觉方向，不是产品或交互合同。
- 提供方原图与本地衍生图必须分开保存和命名。
- 营销页案例不能替代后台系统的密度、可读性和组件约束。
- 单个案例只支持 Level 3 Framework；在异构项目出现可重复增益前，不晋级为强制 Skill。

## Source trace

- `pbakaus/impeccable@d14711a` — README and Neo Mirai workflow.
- `impeccable.style/cases/neo-mirai/` — first-party case study, observed 2026-08-13.
- `ConardLi/garden-skills@aaf9a82` — `skills/web-design-engineer/SKILL.md`.

以上来源支持工作流结构，但没有独立证明其能提升任意目标项目。本条知识当前为 `draft`、Level 3 Framework。
