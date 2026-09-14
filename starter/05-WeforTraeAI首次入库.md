# WeforTraeAI 首次入库与试跑

## 当前状态

- GitHub 仓库：`https://github.com/deepseekeddy/WeforTraeAI.git`
- 默认分支：建议使用 `main`
- 远端当前为空；本地资料位于 `trae-rd-system/`
- 本阶段目标是建立可评审的代码库，不直接开启无人值守写入、自动审批或生产发布。

## 第一次提交前

在仓库根目录执行：

```bash
python3 trae-rd-system/scripts/validate_skills.py
python3 trae-rd-system/scripts/package_skills.py
git status --short
```

确认校验通过，并人工检查提交中不包含账号、Token、客户数据和本机临时文件。

企业控制台导入 Skill 时，逐个上传 `trae-rd-system/dist/<skill-name>.zip`。`trae-rd-system/skills.zip` 是完整源码归档，包含多个 Skill，不作为单个企业 Skill 上传。

## 建议的首个 Pull Request

标题：

```text
[BOOTSTRAP] 建立 TRAE 研发协作与 Skill 库基线
```

内容至少说明：

- 11 个 Skill 的范围和 P0/P1/P2 波次；
- 飞书、Figma、GitHub、CI/CD 与 TRAE 的事实源边界；
- AI 不代替真人审批和生产发布确认；
- 第一阶段只选择一个 5–10 个工作日可完成的真实需求；
- P0 Skill 在正式发布前每个至少通过 2 个真实样例。

## 首周只做一个闭环

1. 填写 10 人责任台账，确认每人的 GitHub 用户名、飞书账号、角色、负责目录和备份人。
2. 在飞书建立一条父需求并生成 `REQ-ID`。
3. 用 `requirement-intake` 和 `prd-authoring` 形成 PRD 草稿。
4. 在 GitHub 创建父 Issue 与 5–8 个可验收子任务。
5. 用 `tsd-authoring`、`code-review` 和 `test-acceptance` 完成一次真实交付。
6. 用 `release-readiness` 输出发布检查；最终 Go/No-Go 由授权人员决定。
7. 记录触发错误、字段遗漏、人工编辑量、返工和等待时间，作为 Skill 迭代输入。

## 首周成功标准

- 每条需求和开发任务都有唯一 ID 与单一 Owner。
- 所有状态推进都有真实链接或检查结果作为证据。
- 需求变更能定位受影响人，而不是默认通知全员。
- P0 Skill 的失败样例和人工修改被记录，可进入下一轮修订。
