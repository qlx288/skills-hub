# 🤝 贡献指南 / Contributing Guide

感谢你对 Skill Hub 的兴趣！以下是贡献的几种方式。

## 提交新 Skill

### Skill 质量标准

一个好的 Skill 应该具备：

1. **明确的角色定义** — 开头说清楚"你是谁"
2. **结构化的工作流程** — 分步骤执行，而不是一段笼统的描述
3. **具体的搜索/操作策略** — 给出实际的命令和模板，不要模糊指令
4. **质量红线** — 定义什么是不可接受的输出
5. **输出格式** — 明确报告/结果的格式要求
6. **错误处理** — 遇到失败（如 403/404）怎么办

### 文件结构

```
skills/你的skill名/
├── skill-name.md        # 入口文件（轻量，负责触发）
├── SKILL.md             # 主文件（完整工作流程）
└── skills/              # 子 skill（可选，复杂 skill 才需要）
    ├── sub-skill-1/
    │   └── SKILL.md
    └── sub-skill-2/
        └── SKILL.md
```

**如果你的 Skill 不复杂**，一个单文件就够了，不需要子 skill 架构。

### Frontmatter 格式

```yaml
---
name: your-skill-name
description: "一句话描述这个 skill 做什么"
temperature: 0.3  # 0 = 精确任务, 0.3 = 一般, 0.7 = 创意任务
tools:
  read: true
  write: true
  websearch: true
  fetch: true
  # 只声明你实际需要的工具
---
```

### 提交流程

1. Fork 本仓库
2. 创建分支：`git checkout -b skill/your-skill-name`
3. 在 `skills/` 下创建你的 Skill 目录
4. 写好 Skill 文件
5. 在 PR 描述中附上：
   - Skill 简介
   - 至少一个使用示例（截图或文字）
   - 测试过的模型和平台

## 改进现有 Skill

- 搜索策略不够好？补充更多渠道
- 输出格式不理想？优化报告模板
- 发现 bug？提 Issue 或直接 PR

## Skill 开发技巧

### 通用原则

- **先搜后抓**：WebFetch 的 URL 必须来自 WebSearch 结果，不要猜 URL
- **宁精勿滥**：5 条高质量输出 > 50 条未验证的结果
- **分步骤执行**：把复杂任务拆成明确的步骤，每步有清晰的输入输出
- **考虑失败情况**：网页打不开、信息查不到都是正常情况，要有兜底方案

### 适配不同模型

如果你的 Skill 比较复杂，考虑提供多个版本：

| 版本 | 体量建议 | 适合 |
|------|---------|------|
| 完整版 | 不限 | 大模型 API (Opus/Sonnet/GPT-4) |
| 精简版 | <15K chars | 中等模型 |
| 单文件版 | <5K chars | 本地小模型 (30B以下) |

精简技巧：
- 去掉示例 JSON 输出格式（模型能自己推断）
- 合并重复的规则描述
- 用列表代替长段落
- 去掉子 skill 架构，合并到单文件

## 行为准则

- 尊重每个贡献者
- 建设性的反馈
- 不提交恶意或有害的 Skill
