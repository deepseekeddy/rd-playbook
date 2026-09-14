# 项目智能体规则

- 所有需求相关分支、PR、TSD 和发布记录必须包含 `REQ-ID`。
- 开始开发前确认 PRD 与 TSD 状态为 Approved，并记录所用版本。
- 只修改当前任务范围内的文件；发现范围外问题时先报告，不顺手重构。
- 禁止读取或输出真实密钥、生产用户数据和未脱敏日志。
- 禁止由智能体执行生产部署、生产数据修改或最终 PR 合并。
- 修改业务逻辑必须补充对应测试；如未运行测试，明确说明原因。
- 数据库变更必须兼容旧版本，并提供迁移、验证和回滚方案。
- PR 描述必须包含变更摘要、需求链接、测试证据、风险和回滚方式。

## 项目命令占位

- 格式检查：`<replace-with-format-command>`
- 静态检查：`<replace-with-lint-command>`
- 单元测试：`<replace-with-unit-test-command>`
- 集成测试：`<replace-with-integration-test-command>`
