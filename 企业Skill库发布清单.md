# 企业 Skill 库发布清单

## 首批发布优先级

| 波次 | Skill | Owner 建议 | 发布条件 |
|---|---|---|---|
| P0 | requirement-intake、prd-authoring、tsd-authoring、code-review、release-readiness | PM/TL/SRE | 各通过 2 个真实样例 |
| P1 | prd-review、figma-handoff、implementation-planning、test-acceptance | PM/设计/TL/QA | 与现有模板完成字段映射 |
| P2 | delivery-orchestrator、operate-observe | TL/SRE | MCP/Hook 与追踪链路稳定 |

## 发布步骤

1. 由 Owner 将 Skill 替换为企业术语、工具名、模板字段和门禁阈值。
2. 在项目仓库中评审 `SKILL.md` 与 assets；至少一名业务评审人和一名技术评审人批准。
3. 使用真实任务验证触发、缺失输入处理、输出结构和禁止行为。
4. 在 TRAE 企业控制台进入 `企业配置 → 企业技能 → 添加技能`，上传单个 `SKILL.md` 或包含资源的 zip。
5. 首先仅对试点成员启用；记录错误触发、字段遗漏、人工修改和返工。
6. 两周后正式发布并标记版本；修改后重复验证。CLI 项目级 Skill 可放入 `.traecli/skills/<skill-name>/` 并随仓库版本管理。

## 每个 Skill 上线前检查

- `name` 与目录名一致，仅含小写字母、数字、连字符。
- `description` 同时写清“做什么”和“何时触发”，与相邻 Skill 不重叠。
- 明确输入、缺失信息、输出格式、完成定义、禁止行为和人工审批点。
- 模板和参考资料无重复、无敏感数据、无过期链接。
- 不声称未执行的测试、不伪造审批或外部系统状态。
- 设置 Owner、Maintainer、版本、适用团队、灰度范围和回滚方式。
