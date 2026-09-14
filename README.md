# rd-playbook

面向 10 人软件研发团队的 TRAE 全流程协作与企业 Skill 库。

当前版本已经覆盖：需求接入、PRD、Figma 交付、TSD、任务拆分、开发评审、测试验收、发布、上线观测，以及跨系统的人员责任、状态、门禁和通知机制。

## 从这里开始

1. 阅读 [研发全流程设计](研发全流程设计.md)，理解各系统的职责边界。
2. 按 [第一阶段配置清单](starter/04-第一阶段配置清单.md) 建立一个真实需求的最小闭环。
3. 填写 [团队与责任台账](starter/01-团队与责任台账.csv)。
4. 在修改或发布 Skill 前运行：

   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/package_skills.py
   ```

   企业控制台上传使用 `dist/<skill-name>.zip`；根目录中的 `skills.zip` 是完整源码归档，不作为单个 Skill 上传包。

## 目录

```text
├── 研发全流程设计.md                  全局流程、角色和状态机
├── TRAE协作机制操作手册.md            日常协作方式
├── 团队调度与变更自动化设计.md        人员、通知、审核与客户变更
├── 企业Skill库发布清单.md             发布波次和治理规则
├── skills/                            11 个企业 Skill
├── starter/                           飞书、GitHub、团队试跑启动包
├── examples/                          AGENTS.md、PR 模板示例
├── scripts/                           校验与打包工具
├── dist/                              按 Skill 打包的上传 zip
└── .github/                           Issue/PR 模板、CI 校验
```

## 当前落地原则

- TRAE 是团队每天工作的 AI 执行入口。
- 飞书保存业务需求、决策、人员和通知主记录。
- Figma 保存视觉与交互事实。
- GitHub 保存研发任务、代码、评审和 CI 证据。
- AI 可以生成草稿、检查证据和执行获准操作，但不能代替真人审批、业务验收或生产 Go/No-Go。
