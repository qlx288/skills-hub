# API 参考

## Agent 类

### AgentConfig

智能体配置类。

```python
@dataclass
class AgentConfig:
    name: str           # 智能体名称
    model: str         # 模型标识 (claude-sonnet-4-20250514, gpt-4o, etc.)
    role: str          # 角色描述
    tools: List[str]   # 可用工具列表
    system_prompt: str # 系统提示词
    temperature: float # 温度参数 (0-2)
    max_tokens: int    # 最大 token 数
```

### Agent

智能体实例。

```python
agent = Agent(config)
```

#### 方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| `chat(message, context)` | message: str, context: dict | str | 发送消息并获取回复 |
| `tool_call(tool_name, **kwargs)` | tool_name: str | Any | 调用工具 |

## AgentManager 类

智能体管理器。

```python
manager = AgentManager()
```

#### 方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| `create_agent(name, model, role, **kwargs)` | 名称、模型、角色 | Agent | 创建智能体 |
| `get_agent(name)` | name: str | Agent | 获取智能体 |
| `list_agents()` | - | List[Agent] | 列出所有智能体 |
| `remove_agent(name)` | name: str | None | 移除智能体 |

## Memory 类

记忆数据类。

```python
@dataclass
class Memory:
    key: str                          # 记忆键
    value: str                        # 记忆值
    memory_type: MemoryType           # 记忆类型
    importance: float                # 重要性 (0-1)
    timestamp: float                  # 时间戳
    metadata: Dict                    # 元数据
    embeddings: Optional[List[float]] # 向量嵌入
```

## HybridMemoryStore 类

混合记忆存储。

```python
store = HybridMemoryStore()
```

#### 方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| `remember(key, value, importance, metadata)` | 记忆内容 | Memory | 存储记忆 |
| `recall(query, top_k)` | 查询内容 | List[Memory] | 检索记忆 |
| `recall_by_key(key)` | 记忆键 | Optional[Memory] | 按键检索 |
| `forget(key)` | 记忆键 | None | 删除记忆 |
| `get_context_for_agent(agent_name, max_tokens)` | 智能体名称 | str | 获取上下文 |

## Group 类

协作群组。

```python
group = Group(name="项目组", members=["Alice", "Bob"])
```

#### 方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| `add_agent(agent)` | Agent | None | 添加智能体 |
| `remove_agent(name)` | 名称 | None | 移除智能体 |
| `on(event, handler)` | 事件名、回调 | None | 注册事件 |
| `add_message(author, content, metadata)` | 作者、内容 | Message | 添加消息 |
| `discuss(topic, context)` | 主题、上下文 | DiscussionResult | 发起讨论 |
| `discuss_until_consensus(topic, max_rounds)` | 主题、轮数 | str | 讨论直到共识 |
| `assign_task(goal, agents, strategy)` | 目标、智能体、策略 | TaskResult | 分配任务 |
| `get_context(for_agent)` | 智能体名称 | str | 获取上下文 |

#### 事件

| 事件名 | 参数 | 说明 |
|--------|------|------|
| `message` | Message | 新消息 |
| `task_complete` | Task | 任务完成 |
| `task_failed` | Task | 任务失败 |

## RAGEngine 类

RAG 知识检索引擎。

```python
rag = RAGEngine(embedding_model="text-embedding-3-small", chunk_size=500)
```

#### 方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| `add_document(content, metadata)` | 内容、元数据 | str | 添加文档 |
| `add_documents(documents)` | 文档列表 | List[str] | 批量添加 |
| `search(query, top_k)` | 查询、返回数 | List[Dict] | 语义检索 |
| `get_context(query, max_tokens)` | 查询、最大token | str | 获取上下文 |
| `answer(query, llm_func)` | 查询、LLM函数 | str | RAG问答 |
| `delete_document(doc_id)` | 文档ID | None | 删除文档 |

## CollaborationStrategy 枚举

协作策略。

```python
CollaborationStrategy.SEQUENTIAL   # 顺序执行
CollaborationStrategy.PARALLEL     # 并行执行  
CollaborationStrategy.DISCUSSION   # 讨论模式
```

## MemoryType 枚举

记忆类型。

```python
MemoryType.WORKING     # 短期记忆
MemoryType.LONG_TERM   # 长期记忆
MemoryType.VECTOR      # 向量记忆
```
