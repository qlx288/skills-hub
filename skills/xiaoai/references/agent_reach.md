# Agent Reach 集成

## 简介

[Agent-Reach](https://github.com/Panniantong/Agent-Reach) 让 AI 拥有读取互联网的能力：
- 🌐 任意网页
- 📺 YouTube/B站 字幕
- 🐦 Twitter/X
- 📕 小红书
- 📦 GitHub
- 🔍 全网搜索

## 安装

```bash
# 让 AI 自动安装
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

# 或者手动安装
pip install agent-reach
agent-reach install
agent-reach doctor
```

## 配置

### 基础功能（无需配置）
- 网页读取
- YouTube/B站 字幕
- GitHub

### 需要 Cookie（可选）
- Twitter/X：导出 Cookie 后配置
- 小红书：导出 Cookie 后配置

## 使用示例

```python
from scripts.web_agent import WebAgent

# 创建带网页能力的 AI
web_agent = WebAgent(agent, model="meta/llama-3.1-70b-instruct")

# 读取网页
result = web_agent.read_url("https://github.com/Panniantong/Agent-Reach")

# 搜索
result = web_agent.search("最新的 AI 新闻")

# 提取 YouTube 字幕
result = web_agent.get_youtube_transcript("https://youtube.com/watch?v=xxx")

# 读取小红书
result = web_agent.read_xiaohongshu("https://xiaohongshu.com/explore/xxx")
```

## 在项目团队中使用

```python
from examples.project_team import AIProjectTeam

team = AIProjectTeam("市场调研")

# AI 自动搜索网上信息
tasks = [
    {"task": "搜索竞品最新动态", "agent": "researcher"},
    {"task": "搜索用户评价", "agent": "competitor"},
]
```
