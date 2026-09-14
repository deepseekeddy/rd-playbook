# TRAE 十人团队协作启动包

这个目录用于把研发协作方案真正落地。先用一个真实需求试跑，不在第一天配置所有自动化。

## 今天的完成标准

1. 填完 `01-团队与责任台账.csv`。
2. 在飞书创建“研发交付主表”，按 `02-飞书需求主表字段.md` 建字段。
3. 选一个中等规模真实需求，生成 `REQ-YYYY-NNN`。
4. 在真实 GitHub 仓库中创建组织级 Project。
5. 把 `github-template/.github` 中的模板经替换占位符后复制到真实仓库。
6. 十名成员在 Trae 中运行一次 `03-Trae每日工作入口.md` 中的指令。

## 系统边界

- Trae：每个人的工作入口、上下文读取、AI 执行和摘要。
- 飞书：客户需求、PRD/TSD、业务状态、决策、通知。
- Figma：设计源文件和冻结版本。
- GitHub：开发任务、代码、PR、CI、技术审核和发布证据。
- 进度管理工作台：从飞书和 GitHub 聚合生成驾驶舱，不独立人工维护状态。

## 实施顺序

`Team roster → 飞书需求主表 → REQ-ID → GitHub Project → Issue/Sub-issue → PR/Review → QA/Release → 通知 → Trae 驾驶舱`

## 启用前必须替换

- `YOUR_ORG`：GitHub Organization 名称。
- `YOUR_REPO`：仓库名称。
- `@your-org/...`：真实 GitHub Team。
- 示例成员和日期。
- 仓库真实存在的 CI 检查名称。
