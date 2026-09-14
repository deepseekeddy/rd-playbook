---
name: release-readiness
description: 在上线前核对代码、测试、制品、迁移、配置、权限、监控、沟通和回滚是否就绪。当用户要求发布检查、Go/No-Go、变更单、发布说明、灰度或回滚计划时使用。
---

# 发布就绪检查

使用 [assets/release-template.md](assets/release-template.md) 生成发布单。

核对：批准的版本与范围；不可变制品；CI 状态；测试/UAT；漏洞与许可证；配置/密钥；数据库迁移；容量；监控/告警；灰度；回滚；值守与通知。

输出发布单：`REQ-ID`、版本/制品摘要、变更、影响、窗口、步骤、验证、阈值、回滚、Owner、审批、沟通、证据链接。

结论只能是 `GO`、`CONDITIONAL GO`、`NO-GO`。Blocker 未关闭、回滚不可行、无监控或无授权审批时必须 NO-GO。

生产操作必须在动作发生时由授权人员确认；不得把草稿或 AI 建议当成审批。
