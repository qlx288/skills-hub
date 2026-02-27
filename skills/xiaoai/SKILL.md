---
name: xiaoai
description: "小爱 AI - 多智能体协作核心能力包。支持创建人类与 AI 智能体共存的协作环境，包含：多智能体实时协作、跨群组持久记忆、任务分配与协作执行、RAG 知识检索、工作流自动化、技能市场(ClawHub+魔搭MCP)、主动介入群聊、自我学习能力、企业微信接入、网页采集、GUI 自动化。使用 NVIDIA Llama/Claude/OpenAI/魔搭模型。"
homepage: https://github.com/qlx288/skills-hub
metadata:
  clawdbot:
    emoji: "🤖"
    requires:
      env: ["NVIDIA_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "MODELSCOPE_API_KEY"]
    primaryEnv: "NVIDIA_API_KEY"
    files: ["scripts/*"]
temperature: 0.7
tools:
  skill: true
  read: true
  write: true
  edit: true
  bash: true
  fetch: true
  websearch: true
  codesearch: true
  grep: true
  glob: true
---

# Teamily AI Core

多智能体协作核心能力包，支持创建人类与 AI 智能体共存的协作环境。

## 核心功能

### 1. 多智能体群聊协作
多个 AI 智能体可以在同一个"群组"中实时协作，模拟真实团队讨论。

### 2. 跨群组持久记忆
AI 智能体的记忆可以在不同群组之间共享，形成持续学习的知识积累。

### 3. 任务分配与协作执行
自动分解复杂任务，分配给合适的智能体执行，支持顺序和并行两种模式。

### 4. RAG 知识检索
基于向量数据库的知识检索，让智能体能够从知识库中获取相关信息。

### 5. 工作流自动化
定义可复用的工作流程，自动执行多步骤任务。

### 6. 技能市场 (内置 + ClawHub)
- 内置 8+ 个常用技能（网页采集、数据分析、文档生成等）
- **ClawHub 集成**：接入 OpenClaw 官方技能市场 (3000+ 技能)
- 智能体可根据任务自动调用

### 7. 主动介入群聊
AI 可以像群成员一样主动参与讨论，不只是响应用户指令。

### 8. 自我学习能力
遇到未知问题时，自动搜索互联网寻找解决方案并学习。

### 9. 企业微信接入
集成企业微信机器人，支持消息收发和群管理。

### 10. GUI 自动化
通过鼠标和键盘控制自动化执行桌面操作。

## 快速开始

### 基本用法

```python
from scripts.agent_manager import AgentManager
from scripts.group_manager import GroupManager
from scripts.memory_store import MemoryStore

# 1. 初始化
manager = AgentManager()
memory = MemoryStore()
group = GroupManager()

# 2. 创建智能体
agent = manager.create_agent(
    name="Researcher",
    model="nvidia",  # nvidia/claude/openai
    role="负责调研和信息收集"
)

# 3. 创建群组并添加成员
group_id = group.create_group("项目组")
group.add_member(group_id, agent)
```

### 群体智能讨论

```python
from scripts.swarm_intelligence import SwarmIntelligence

swarm = SwarmIntelligence()

# 创建多个智能体进行协作思考
result = swarm.collaborate(
    topic="分析新能源汽车市场趋势",
    agents=[
        {"name": "分析师", "role": "市场数据分析"},
        {"name": "研究员", "role": "行业趋势研究"},
        {"name": "写手", "role": "报告撰写"}
    ]
)
```

### 使用技能市场

```python
from scripts.skill_market import SkillMarket

market = SkillMarket()

# 调用技能
result = market.execute_skill(
    skill_name="web_scraper",
    params={"url": "https://example.com"}
)
```

### 使用魔搭社区 MCP

```python
from scripts.skill_market import SkillMarket

market = SkillMarket()

# 列出所有 MCP 服务
services = market.search_modelscope()
for s in services:
    print(f"{s['name']}: {s['description']}")

# 搜索模型
models = market.search_modelscope("llama")
print(f"找到 {len(models)} 个模型")

# 调用 MCP 服务
result = market.call_modelscope_mcp(
    mcp_id="modelscope_search",
    params={"query": "Qwen"}
)

# 调用 MiniMax 语音合成
result = market.call_modelscope_mcp(
    mcp_id="minimax_tts",
    params={
        "api_key": "your_minimax_key",
        "payload": {
            "text": "你好，我是小爱",
            "voice_id": "Chinese_Male_Bada"
        }
    }
)
```

### 使用 ClawHub 技能市场

```python
from scripts.skill_market import SkillMarket

market = SkillMarket()

# 搜索 ClawHub 技能（如 email、github、slack 等）
skills = market.search_clawhub("email")
for s in skills:
    print(f"{s.name}: {s.description} (⭐ {s.stars})")

# 安装 ClawHub 技能
market.install_clawhub_skill("gmail")
market.install_clawhub_skill("github")

# 列出已安装的 ClawHub 技能
installed = market.list_clawhub_skills()
print(f"已安装: {installed}")
```

### 自我学习

```python
from scripts.self_learning import SelfLearning

learner = SelfLearning()

# 遇到问题时让 AI 自主学习解决方案
solution = learner.solve_unknown_problem(
    problem="如何抓取需要登录的网页？"
)
```

## 支持的模型

| 模型 | Provider | 说明 |
|------|----------|------|
| nvidia | NVIDIA API | 推荐使用 meta/llama-3.1-70b-instruct |
| claude | Anthropic | claude-sonnet-4-20250514 |
| gpt-4o | OpenAI | GPT-4O |

## 配置

```python
# 环境变量
NVIDIA_API_KEY=your_nvidia_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## 示例

```bash
# 群体智能测试
python examples/test_swarm.py

# 主动介入测试
python examples/test_proactive.py

# 项目团队演示
python examples/project_team.py

# 工作流+技能市场
python examples/test_workflow_skill.py

# 自我学习测试
python examples/test_self_learning.py
```

## 使用场景

- **团队协作**：创建 AI + 人类的混合团队
- **知识管理**：跨群组共享记忆和知识
- **自动化工作流**：定义和执行复杂业务流程
- **智能客服**：多智能体协作处理客户咨询
- **研究分析**：群体智能进行市场/技术调研
- **桌面自动化**：GUI 操作自动化

## 注意事项

1. 使用前需要配置相应的 API Key
2. NVIDIA 模型需要 NVIDIA API Key
3. 企业微信功能需要企业微信开发者权限
4. GUI 自动化需要在桌面环境运行
