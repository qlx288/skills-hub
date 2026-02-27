# 模型配置指南

## 支持的模型

### Anthropic 模型

| 模型ID | 说明 | 上下文 |
|--------|------|--------|
| claude-sonnet-4-20250514 | Sonnet 4.0 | 200K |
| claude-opus-4-20250514 | Opus 4.0 | 200K |
| claude-3-5-sonnet-20241022 | Sonnet 3.5 | 200K |
| claude-3-opus-20240229 | Opus 3.0 | 200K |

### OpenAI 模型

| 模型ID | 说明 | 上下文 |
|--------|------|--------|
| gpt-4o | GPT-4 Omni | 128K |
| gpt-4o-mini | GPT-4 Omni Mini | 128K |
| gpt-4-turbo | GPT-4 Turbo | 128K |
| gpt-4 | GPT-4 | 8K |

## 环境配置

### 获取 API Key

```bash
# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."

# OpenAI  
export OPENAI_API_KEY="sk-..."
```

### 代码中配置

```python
import os
os.environ["ANTHROPIC_API_KEY"] = "your-key"
os.environ["OPENAI_API_KEY"] = "your-key"
```

## 模型选择建议

### 任务类型推荐

| 任务 | 推荐模型 | 原因 |
|------|----------|------|
| 复杂推理 | claude-opus-4 | 最强推理能力 |
| 日常对话 | claude-sonnet-4 | 性价比高 |
| 快速响应 | gpt-4o-mini | 延迟低 |
| 代码生成 | gpt-4o | 代码能力强 |

### 多模型组合

```python
# 组合使用
config = {
    "primary": {
        "model": "claude-sonnet-4-20250514",
        "provider": "anthropic"
    },
    "fallback": {
        "model": "gpt-4o", 
        "provider": "openai"
    },
    "embedding": {
        "model": "text-embedding-3-small",
        "provider": "openai"
    }
}
```

## 成本优化

### Token 估算

- 1 token ≈ 0.75 个英文单词
- 1 token ≈ 1.5 个中文字符

### 成本对比

| 模型 | 输入 ($/1M) | 输出 ($/1M) |
|------|-------------|-------------|
| claude-sonnet-4 | $3.00 | $15.00 |
| gpt-4o | $2.50 | $10.00 |
| gpt-4o-mini | $0.15 | $0.60 |

### 优化建议

1. 使用 `max_tokens` 限制输出
2. 合理使用 `temperature` (非创意任务用 0.2-0.5)
3. 使用缓存减少重复调用
4. 嵌入模型用便宜的 text-embedding-3-small
