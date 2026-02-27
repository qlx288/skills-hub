# 协作模式示例

## 1. 顺序协作 (Sequential)

适用于需要上一步输出作为下一步输入的任务。

```python
from teamily import Group, Agent, CollaborationStrategy

# 创建智能体
researcher = manager.create_agent("Researcher", "claude-sonnet-4-20250514", 
                                    "负责市场调研")
writer = manager.create_agent("Writer", "gpt-4o", 
                               "负责撰写报告")
designer = manager.create_agent("Designer", "gpt-4o-mini",
                                 "负责制作图表")

# 创建群组
group = Group(name="产品团队", members=["张三", "李四"])
group.add_agent(researcher)
group.add_agent(writer)
group.add_agent(designer)

# 顺序执行任务
result = group.assign_task(
    goal="完成新能源汽车市场分析报告",
    agents=[researcher, writer, designer],
    strategy=CollaborationStrategy.SEQUENTIAL
)
```

### 流程

```
Researcher → 调研分析 → Writer → 撰写报告 → Designer → 制作图表
```

## 2. 并行协作 (Parallel)

适用于可以独立同时执行的任务。

```python
# 并行执行多个独立任务
result = group.assign_task(
    goal="收集以下信息：市场数据、竞品分析、用户反馈",
    agents=[agent_a, agent_b, agent_c],
    strategy=CollaborationStrategy.PARALLEL
)
```

### 流程

```
    ┌─→ Agent A: 市场数据
    │
Agent ─→ Agent B: 竞品分析  →  汇总结果
    │
    └─→ Agent C: 用户反馈
```

## 3. 讨论模式 (Discussion)

适用于需要多方观点和头脑风暴的场景。

```python
# 发起讨论
result = group.discuss(
    topic="选择哪个技术方案？A: 微服务 B: 单体",
    context={"项目规模": "中大型", "时间限制": "3个月"}
)

# 讨论直到共识
conclusion = group.discuss_until_consensus(
    topic="确定产品定位",
    max_rounds=5
)
```

### 流程

```
Round 1: Agent A 发表观点 → Agent B 发表观点 → Agent C 发表观点
Round 2: 基于上轮观点继续讨论
...
Round N: 达成共识或超时
```

## 4. 混合模式

复杂任务可以组合多种模式。

```python
# 阶段1: 并行调研
research_results = group.assign_task(
    goal="调研：技术趋势、用户需求、竞品动态",
    agents=[agent_tech, agent_user, agent_comp],
    strategy=CollaborationStrategy.PARALLEL
)

# 阶段2: 讨论分析
analysis = group.discuss(
    topic=f"基于调研结果分析机会点",
    context={"调研结果": research_results}
)

# 阶段3: 顺序执行
final_output = group.assign_task(
    goal="产出：分析报告 + 建议方案",
    agents=[writer, reviewer],
    strategy=CollaborationStrategy.SEQUENTIAL
)
```

## 5. 人机协作

人类参与的多智能体协作。

```python
# 人类用户参与讨论
group.add_message("张三", "我们需要讨论一下下周的工作安排")

# AI 智能体响应
response = group.discuss(topic="工作安排讨论")

# 人类可以随时插入
group.add_message("李四", "我同意 Agent A 的建议")

# 任务分配时也可以包含人类
result = group.assign_task(
    goal="完成代码审查",
    agents=[reviewer_agent],  # 人类可以后续参与
    strategy=CollaborationStrategy.SEQUENTIAL
)
```

## 6. 记忆驱动的协作

利用长期记忆保持上下文。

```python
# 第一次协作
group.assign_task(goal="讨论项目目标")
group.memory.remember(
    key="project_goals", 
    value="打造最好的AI协作平台",
    importance=0.9
)

# 后续协作 - 自动带上下文
group.assign_task(goal="制定里程碑")  # 自动包含项目目标记忆
```

## 7. 事件驱动的协作

基于事件触发后续动作。

```python
# 任务完成时自动触发下一步
@group.on("task_complete")
def on_task_complete(task):
    if task.assignee.config.name == "Researcher":
        # 触发 Writer 开始工作
        writer.chat(f"调研已完成: {task.result[:500]}")
```
