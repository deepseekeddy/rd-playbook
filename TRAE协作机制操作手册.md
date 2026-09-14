# TRAE 协作机制操作手册

本文把“单一事实源与版本”落到 TraeWork、TraeCode、飞书、Figma、GitHub 和 CI/CD 的具体动作。示例需求统一使用：

> `REQ-2026-042`：运营人员批量导出订单；DRI 为产品经理王敏；目标版本 `v2.8.0`。

涉及团队任务分配、状态审核、知识同步和客户变更广播的自动化细节，见 [团队调度与变更自动化设计](团队调度与变更自动化设计.md)。

## 1. 先明确：TRAE 中什么可以共享

TRAE 的对话和任务适合个人执行与推理，不应成为团队正式记录。团队共享靠外部事实源：

| 信息 | 唯一事实源 | TRAE 的作用 |
|---|---|---|
| 需求状态与关联关系 | 飞书多维表格 | 查记录、补字段、更新状态 |
| PRD/TSD/决策 | 飞书云文档 | 读取、生成草稿、评审、授权后回写 |
| 交互与视觉 | Figma | 读取设计节点、检查交付、辅助生成代码 |
| 代码与评审 | Git/GitHub | 修改代码、生成 PR、检查 diff |
| 构建/测试/发布 | CI/CD | 触发、读取状态、汇总证据 |

因此，同一需求可以有多个 TRAE 任务，但只能有一个 `REQ-ID`，所有正式结论必须回到事实源。

## 2. 管理员一次性配置

### 2.1 将飞书接入 TraeWork

成员在 TraeWork 中操作：

1. 左侧进入 **插件市场**。
2. 点击右上角 **管理 → 应用授权**。
3. 找到飞书，点击 **连接**。
4. 在飞书授权页选择需要的权限，再确认账号和授权范围。

最小建议权限：读取/编辑指定云文档、读取/更新指定多维表格；只有需要由 TRAE 建日程或通知时才开放日历、消息权限。不要全员默认开放整个飞书空间。

连接后，TraeWork 可以在授权范围内搜索、读取、创建和更新云文档及多维表格。第一次让 AI 写入正式文档前，先用测试空间验证字段和权限。

### 2.2 建立 TRAE 企业文档集

管理员在 TRAE 企业版控制台操作：

1. 飞书开放平台创建企业自建应用。
2. 至少开放 `docs:document.content:read` 和 `drive:drive.metadata:readonly`。
3. 发布应用，取得 App ID/App Secret。
4. 在目标飞书文档的分享设置中给该应用访问权限。
5. 进入 **企业配置 → 企业文档集 → 管理飞书应用**，接入应用。
6. 点击 **新增文档集 → 飞书文档**，粘贴文档链接并设置可见范围。

建议建立 `RD-Policy`、`Product-Knowledge`、`Architecture`、`Quality`、`Operations` 五个文档集。在 TraeCode 中，成员可从 **设置 → 索引与文档 → 内置文档集** 查看，并在对话框用 `#Doc` 引用。

注意：企业文档集只索引纯文本。Figma 画面、飞书图片、附件和只画图不写说明的架构图，AI 无法仅靠文档集可靠理解；必须配文字规格。

### 2.3 发布企业 Skill

管理员进入 **企业配置 → 企业技能 → 添加技能**，上传本项目各 Skill 的 `SKILL.md`；包含模板的 Skill 应把整个目录压缩为 zip 上传。

成员添加方式：

- TraeCode：**设置 → 技能与命令 → 技能 → 添加 → 从企业添加**。
- TraeWork：左侧 **技能 → 企业技能**，添加所需 Skill。
- 项目级技能：复制到仓库 `.trae/skills/<skill-name>/`，随代码评审和版本管理。

首批只给试点成员开放 `requirement-intake`、`prd-authoring`、`tsd-authoring`、`code-review`、`release-readiness`。

### 2.4 配置项目规则

在代码仓库根目录放置 `AGENTS.md`，TraeCode 中进入 **设置 → 规则**，打开“将 AGENTS.md 包含在上下文中”。示例见 [AGENTS.example.md](examples/AGENTS.example.md)。

规则用于长期、无条件的项目约束，例如分支命名、测试命令、禁止访问目录；Skill 用于某类任务的工作流。不要把完整 PRD 或 TSD 塞进规则。

### 2.5 连接 Figma

在 TraeCode 中：

1. 进入 **设置 → MCP**。
2. 点击 **添加 → 从市场添加**。
3. 添加 `Figma AI Bridge`，配置具有目标文件访问权的 Figma Token。
4. 只为设计/前端相关智能体开放该 MCP。

使用时在 Figma 选中目标 Frame，右键 **Copy/Paste as → Copy link to selection**，把选中节点链接交给 TRAE。不要只给整个文件首页链接，否则上下文过大且容易读错版本。

### 2.6 连接 GitHub

TraeWork 切到 **Code 模式**，进入 **头像 → 设置 → 外部应用授权 → GitHub → 连接**。只授权需要的组织和仓库。

若不是 GitHub，在 TraeCode/CLI 中继续用现有 Git 命令和企业批准的 MCP；PR 合并仍由 Git 平台保护规则控制。

## 3. 每个需求在 TRAE 中如何组织

不要用一个无限增长的聊天承载整个项目。推荐每阶段一个任务：

```text
REQ-2026-042-01-intake
REQ-2026-042-02-prd
REQ-2026-042-03-design-review
REQ-2026-042-04-tsd
REQ-2026-042-05-implementation
REQ-2026-042-06-test
REQ-2026-042-07-release
REQ-2026-042-08-observe
```

新任务的第一条指令固定声明：`REQ-ID`、当前阶段、事实源链接、目标、允许写入的系统、禁止动作。任务结束时把摘要和证据写回飞书主记录，而不是要求下一个任务依赖聊天记忆。

## 4. PRD：从需求表到批准版本

### 4.1 PM 创建 PRD 草稿

PM 在 TraeWork **Work 模式**新建任务 `REQ-2026-042-02-prd`，选择飞书插件和 `prd-authoring` Skill，输入：

```text
使用 prd-authoring 处理 REQ-2026-042。

事实源：
1. 飞书需求表：[需求记录链接]
2. 产品术语文档：[文档链接]
3. PRD 模板：[模板链接]

请先读取需求记录，只在信息足够时起草 PRD；未知内容标记“待确认”，不要自行编造业务口径。
输出前先给我：已知事实、假设、待确认问题。
确认后创建飞书 PRD，标题为“[REQ-2026-042] 批量导出订单 PRD”。
正文首部必须写：Status=Draft、Owner=王敏、Reviewers、Version=v0.1、Last Updated、REQ-ID。
最后将 PRD 链接写回需求表的“PRD”字段，将状态更新为“PRD Draft”。
```

执行分两段：第一段只读并生成澄清清单；PM 回答后，第二段才授权创建文档和更新多维表格。这样可避免 AI 用错误假设污染正式文档。

### 4.2 异步评审 PRD

设计、TL、QA 分别开独立任务，避免被 PM 原对话中的推理锚定。示例：

```text
使用 prd-review 评审 [PRD 飞书链接]，关联 REQ-2026-042。
同时读取 #Doc Product-Knowledge 和 #Doc RD-Policy。

请从设计、研发、测试三个视角检查：
- 用户流程、状态和异常是否完整；
- 数据量、权限、隐私、导出格式和失败重试是否明确；
- 每个 FR-ID 是否有可测试验收标准。

只输出 Blocker/Major/Minor、建议 Owner 和 Approved/Approved with actions/Rejected。
不要修改正式 PRD。
```

评审意见先写入飞书评论。PM 修改 PRD 后把版本升为 `v0.2`，逐条回复处理结果。所有 Blocker 关闭、产品/设计/TL/QA 真人确认后，PM 才将正文状态更新为 `Approved`，需求表状态改为 `PRD Approved`。

AI 可以汇总批准证据，但不得替人批准。

### 4.3 PRD 版本规则

- 小修正文但不改变行为：`v0.1 → v0.2`。
- 批准后发生影响验收的变更：`v1.0 → v1.1`，并创建变更记录。
- 范围或目标发生重大变化：`v1.x → v2.0`，重新走 PRD 评审。
- 不复制“最终版、最终版2”；用状态和版本号表达。

## 5. TSD：从 PRD、设计和代码生成技术方案

TL 在 TraeCode 打开目标仓库，等待 `#Workspace` 索引完成，新建任务 `REQ-2026-042-04-tsd`。

```text
使用 tsd-authoring 为 REQ-2026-042 编写 TSD 草稿。

上下文：
- #Doc [已批准 PRD]
- #Doc Architecture
- Figma 交付链接：[冻结的 selection/version 链接]
- #Workspace
- 重点读取 #Folder services/order-export 和 #Folder apps/admin

先验证 PRD 状态必须为 Approved，并总结当前实现。
方案必须覆盖：异步导出任务、权限校验、对象存储下载、10 万行容量、幂等、失败重试、审计日志、监控、灰度、数据兼容和回滚。
输出到 docs/tsd/REQ-2026-042-order-export.md，仅生成草稿，不改业务代码。
列出 FR-ID 到组件、接口和测试层级的映射。
```

建议先在仓库生成 Markdown 草稿，以便与代码一起验证。TL 完成技术评审后，由有飞书编辑权限的成员在 TraeWork 执行：

```text
读取本地 TSD 文件和飞书 TSD 正式文档。
仅将已批准的 v1.0 内容同步到飞书；保留正文头部的 Owner、Reviewers、REQ-ID、版本和变更记录。
同步后返回文档链接和修改摘要，不更新其他文档。
```

飞书 TSD 是正式签字版本；仓库中的 Markdown 可以作为与代码同步的技术副本，但必须在页首写明正式文档链接和对应版本，避免双主。

## 6. Figma：冻结设计并交付给开发

### 6.1 Figma 文件结构

```text
00-Cover
  REQ-2026-042 / Status=Ready for Dev / Version=1.0 / Owner=李婷
10-Flow
20-Screens
30-Components
40-Prototype
90-Archive
```

`00-Cover` 中同时放 PRD 链接、交付日期、断点范围和变更摘要。`20-Screens` 的 Frame 命名包含页面和状态，例如：

```text
OrderList/Desktop/Default
OrderExport/Desktop/Config
OrderExport/Desktop/Exporting
OrderExport/Desktop/Success
OrderExport/Desktop/Error
OrderExport/Desktop/NoPermission
```

### 6.2 在 TRAE 中做交付检查

设计师冻结 Figma version，并复制关键 Flow/Frame 的 selection 链接。前端或设计师在 TraeCode 调用 `figma-handoff`：

```text
使用 figma-handoff 检查 REQ-2026-042 的设计交付。
PRD：#Doc [PRD v1.0]
Figma：
- 主流程 selection：[链接]
- 导出配置 Frame：[链接]
- 状态页 Frame：[链接]

通过 Figma MCP 读取选中节点，生成：
1. FR-ID 到 Frame 的映射；
2. Loading/Empty/Error/Success/Disabled/NoPermission 状态矩阵；
3. 组件和变量复用清单；
4. 响应式、键盘焦点和可访问性缺口；
5. 可以进入开发/需要修改的结论。
不要修改 Figma 文件。
```

设计师修复缺口后，在 Figma 创建 `Design v1.0` 版本，把 version/selection 链接写入 PRD 首部和需求表的 Figma 字段。之后开发只引用冻结链接，不引用“当前文件状态”。

### 6.3 设计修改示例

开发中若仅调整按钮间距，设计师更新 `v1.0.1`，记录非行为变更，不重走 PRD/TSD。若新增导出筛选字段，则进入需求变更流程，不能直接在 Figma 改完通知开发。

## 7. 代码：每项变更通过 PR，聊天结论回写决策日志

### 7.1 创建隔离开发任务

在 TraeWork **Code 模式**选择仓库和基线分支，为需求创建分支：

```text
feat/REQ-2026-042-order-export
```

并发任务使用 TraeWork Worktree，避免不同 AI 任务修改同一工作目录。开发提示词：

```text
实现 REQ-2026-042 的 TASK-03：创建异步导出任务 API。

上下文：
- #Doc [PRD v1.0]
- #Doc [TSD v1.0]
- #File AGENTS.md
- #Folder services/order-export

先给实施计划和待确认项；确认后再修改。
必须补充单元/集成测试、日志、指标和错误处理。
运行 AGENTS.md 指定的最小验证命令。
不要修改 TSD 未授权的模块，不执行生产部署。
最后输出改动、测试证据、风险和待办。
```

### 7.2 创建和检查 PR

AI 完成后，TraeWork 对话顶部会显示 PR 操作。点击 **AI 创建 PR**，先在 DiffView 检查变更，再选择创建 PR；最终仍在 GitHub 中由人确认和合并。

PR 描述使用 [pull_request_template.example.md](examples/pull_request_template.example.md)，至少包含：REQ-ID、PRD/TSD/Figma、范围、测试、迁移、监控、风险和回滚。

创建后点击 **AI 检查 PR**，或输入：

```text
使用 code-review 检查当前 PR。
以 REQ-2026-042 的 PRD v1.0、TSD v1.0 和 AGENTS.md 为准。
先检查需求覆盖和安全/数据风险，再检查代码质量。
问题必须给出文件、行、复现条件和影响；区分 P0-P3。
列出实际执行过的测试；未执行的明确写“未执行”。
```

### 7.3 聊天中的架构决定如何固化

假设开发和 TRAE 讨论后决定“导出文件 24 小时后自动删除”。不能只留在聊天中，应创建决策记录：

```text
请把刚才确认的“导出文件保留 24 小时”整理为决策草稿，包含：
背景、候选方案、最终选择、理由、隐私/成本影响、相关 FR-ID、批准人待填。
写入 docs/decisions/REQ-2026-042-export-retention.md。
不要把讨论中未确认的观点写成最终决定。
```

TL/PM 批准后，同步到飞书决策日志，并在 TSD 中引用该记录。聊天任务可以删除，决策仍可追踪。

## 8. PRD Approved 后的轻量变更控制

### 8.1 示例：新增“客户手机号”导出列

这是行为、权限和隐私变更，不能直接让开发多加一个字段。PM 在 TraeWork 新建 `REQ-2026-042-change-01`：

```text
为 REQ-2026-042 创建变更 CR-01。

原批准范围：订单号、金额、时间、状态。
拟新增：客户手机号。
原因：客服批量回访。

请读取 PRD v1.0、TSD v1.0、Figma v1.0 和需求主记录，输出：
1. 变化前后对比；
2. 用户价值与不做的影响；
3. 权限、隐私、审计、脱敏、数据接口、设计和测试影响；
4. 估算与排期影响；
5. 哪些门禁必须重开；
6. 建议批准人。
先生成草稿，不更新任何状态。
```

AI 应得到类似结论：

| 产物/门禁 | 是否重开 | 原因 |
|---|---|---|
| PRD | 是 | 导出字段与权限规则改变 |
| Figma | 视交互而定 | 若用户可选择字段，需要新增控件和状态 |
| TSD | 是 | 涉及 PII、脱敏、接口与审计 |
| 开发计划 | 是 | 后端、前端、安全与测试任务增加 |
| 测试 | 是 | 权限、脱敏、审计和回归范围变化 |
| 已合并代码 | 评估 | 不直接回滚，建立增量任务 |

### 8.2 变更单字段

在飞书需求表增加子表或关联记录：

```text
Change-ID: CR-01
REQ-ID: REQ-2026-042
Requested by: 客服负责人
Changed: 新增手机号导出列
Reason: 批量回访
Impact: PRD/TSD/Test/Security
Schedule delta: +2 人日
Decision: Pending / Approved / Rejected
Approvers: PM、TL、安全、QA
Approved at:
Affected versions:
```

审批完成后再让 TraeWork 更新：

```text
CR-01 已由 [真实姓名/链接] 批准。
请执行以下受限更新：
1. 需求表状态改为 Change Approved；
2. PRD 从 v1.0 升为 v1.1，在变更记录追加 CR-01；
3. TSD 状态改为 Needs Update；
4. 添加受影响任务清单。
不要修改 Figma、代码或发布状态。
完成后返回每个被修改对象的链接和字段差异。
```

真人必须先在飞书完成审批；提示词中的一句“已批准”不能代替证据。

### 8.3 什么变化需要重走哪些门禁

| 变化 | PRD | Figma | TSD | Test | Release |
|---|---:|---:|---:|---:|---:|
| 错别字、非行为文案 | 轻量记录 | 可能 | 否 | 冒烟 | 否 |
| UI 布局/交互变化 | 可能 | 是 | 影响前端架构时 | 是 | 已发布则是 |
| 验收行为或业务规则变化 | 是 | 可能 | 是 | 是 | 是 |
| API/数据模型/迁移变化 | 可能 | 否 | 是 | 是 | 是 |
| 权限、隐私、安全变化 | 是 | 可能 | 是+安全评审 | 是 | 是 |
| 目标、用户或范围重大变化 | 全量重开 | 是 | 是 | 是 | 是 |

## 9. 一个完整日常协作样例

| 时间 | 人 | TRAE 中的动作 | 写回事实源 |
|---|---|---|---|
| 周一 10:00 | PM | Work 模式读取需求表，调用 requirement-intake | 需求表 `Triaged` |
| 周一 15:00 | PM | 调用 prd-authoring 创建 PRD v0.1 | 飞书 PRD、状态 `PRD Draft` |
| 周二 | 设计/TL/QA | 各自调用 prd-review 异步评审 | 飞书评论与行动项 |
| 周三 | PM | 汇总修订，真人批准 | PRD v1.0、状态 `Approved` |
| 周三–四 | 设计 | Figma 设计；TRAE 做 handoff 检查 | Figma v1.0 冻结链接 |
| 周四 | TL | TraeCode 用 #Doc+#Workspace 生成 TSD | 飞书 TSD v1.0 |
| 周五 | 开发 | Code 模式/Worktree 实现、测试 | Git 分支和 Commit |
| 下周一 | 开发/Reviewer | AI 创建 PR、AI 检查 PR、人工评审 | GitHub PR/CI 证据 |
| 下周二 | QA | test-acceptance 生成并执行矩阵 | 测试报告、缺陷记录 |
| 下周三 | SRE/TL | release-readiness 检查，真人 Go/No-Go | 发布单、制品、部署记录 |
| 发布后 | PM/SRE | operate-observe 汇总指标 | 看板、复盘、改进项 |

## 10. 团队日常检查清单

每次在 TRAE 发起任务前检查：

- 是否写明 `REQ-ID`、阶段和目标？
- 是否引用了正确版本的 PRD/TSD/Figma，而非搜索到的旧文档？
- 是否说明哪些系统允许读取、哪些允许写入？
- 是否要求 AI 区分事实、假设和未执行项？
- 是否明确最终批准必须由真人完成？

每次任务结束检查：

- 正式产物是否写回唯一事实源？
- 需求表中的状态、版本和链接是否同步？
- 关键决定是否进入决策日志？
- 测试、批准和部署是否都有真实证据？
- 下一动作是否有 Owner 和截止时间？

## 11. TRAE 官方参考

- [TraeWork 飞书集成](https://docs.trae.cn/work_feishu-integration)
- [TRAE 企业文档集](https://docs.trae.cn/enterprise_enterprise-doc-set)
- [TraeCode Skill](https://docs.trae.cn/ide_skills)
- [TraeCode 上下文引用：#Doc/#Workspace/#File](https://docs.trae.cn/ide_number-sign)
- [TraeCode Rule 与 AGENTS.md](https://docs.trae.cn/ide_rules)
- [Figma AI Bridge 教程](https://docs.trae.cn/ide_tutorial-mcp-figma)
- [TraeWork GitHub 集成与 PR](https://docs.trae.cn/work_github-integration)
- [TraeWork Worktree](https://docs.trae.cn/work_worktree)
