---
name: delivery-orchestrator
description: 贯通需求、PRD、设计、TSD、开发、测试、发布和运营，维护阶段状态、门禁、Owner 与证据链。当用户要求规划、推进、检查或汇报一个跨阶段研发交付时使用。
---

# 研发交付编排

1. 获取 `REQ-ID`、目标、DRI、当前阶段、目标版本和风险等级。缺失时先建立需求主记录草稿。
2. 判定下一阶段及其入口条件；只调用完成该阶段所需的专业 Skill。
3. 维护状态：`Idea → Triaged → PRD Draft → PRD Approved → Design Ready → TSD Approved → Ready for Dev → In Dev → In Test → Ready for Release → Released → Observing → Closed`。
4. 每次推进前验证上游链接、批准人、版本和未决项。没有证据时不得声称完成。
5. 输出一页状态摘要：当前结论、已完成证据、风险/阻塞、下一动作、Owner、截止时间。

对范围、架构、安全或发布有实质影响的变更，回退到相应门禁重新评审。生产写操作、最终业务验收和 Go/No-Go 必须由授权人员确认。

完成定义：状态与证据一致，下一步唯一明确，所有阻塞都有 Owner 和处理时限。
