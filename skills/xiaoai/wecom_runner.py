#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
企业微信 + Teamily AI 启动器

需要配置环境变量:
- WECOM_CORP_ID: 企业ID
- WECOM_SECRET: 应用Secret
- WECOM_AGENT_ID: 应用AgentID
- NVIDIA_API_KEY: NVIDIA API Key

运行方式:
1. 正式模式: python wecom_runner.py
2. 测试模式: python wecom_runner.py --test
"""
import os
import sys
import argparse

# 设置编码
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()


def test_mode():
    """测试模式 - 模拟企业微信消息"""
    print("="*60)
    print("企业微信 + Teamily AI 测试模式")
    print("="*60)
    
    from scripts.agent_manager import AgentManager
    from scripts.proactive_agent import ProactiveAgent, ActiveGroupChat, Message
    from scripts.wecom_integration import WeComMessageHandler
    
    # 1. 创建 AI 智能体
    nvidia_key = os.getenv("NVIDIA_API_KEY") or "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"
    os.environ["NVIDIA_API_KEY"] = nvidia_key
    
    # ======== 在这里填入你的企业微信配置 ========
    WECOM_CONFIG = {
        "corp_id": "your-corp-id-here",      # 企业ID
        "secret": "your-secret-here",         # 应用Secret
        "agent_id": "your-agent-id-here",    # AgentID
    }
    # ============================================
    
    manager = AgentManager()
    agent = manager.create_agent(
        "AI小助手",
        "meta/llama-3.1-70b-instruct",
        "企业微信群的活跃助手，擅长聊天和解答问题"
    )
    
    proactive = ProactiveAgent(agent, "AI小助手")
    proactive.config["cooldown"] = 1
    
    handler = WeComMessageHandler(
        corp_id=WECOM_CONFIG["corp_id"],
        secret=WECOM_CONFIG["secret"],
        agent_id=WECOM_CONFIG["agent_id"]
    )
    handler.set_agent(proactive)
    
    manager = AgentManager()
    agent = manager.create_agent(
        "AI小助手",
        "meta/llama-3.1-70b-instruct",
        "企业微信群的活跃助手，擅长聊天和解答问题"
    )
    
    # 2. 创建主动介入智能体
    proactive = ProactiveAgent(agent, "AI小助手")
    proactive.config["cooldown"] = 1
    
    # 3. 创建消息处理器
    handler = WeComMessageHandler(
        corp_id="test",
        secret="test",
        agent_id="test"
    )
    handler.set_agent(proactive)
    
    # 4. 模拟消息
    print("\n--- 模拟企业微信群聊 ---\n")
    
    test_messages = [
        {"from": "张三", "content": "大家早上好！"},
        {"from": "李四", "content": "早上好，今天有什么计划？"},
        {"from": "王五", "content": "@AI小助手 推荐一部电影吧"},
        {"from": "赵六", "content": "有什么好看的科幻片吗？"},
        {"from": "钱七", "content": "谁了解Python的异步编程？"},
    ]
    
    for msg in test_messages:
        print(f"\n【{msg['from']}】: {msg['content']}")
        
        # 处理消息
        msg_data = {
            "msgtype": "text",
            "from_user_name": msg["from"],
            "content": msg["content"]
        }
        
        response = handler.handle_message(msg_data)
        
        if response:
            print(f"\n【AI小助手】: {response[:200]}...")
        
        print("-"*40)
    
    print("\n测试完成!")


def run_mode():
    """正式运行模式 - 需要企业微信配置"""
    print("="*60)
    print("企业微信 + Teamily AI 正式模式")
    print("="*60)
    
    # 检查配置
    required = ["WECOM_CORP_ID", "WECOM_SECRET", "WECOM_AGENT_ID", "NVIDIA_API_KEY"]
    missing = [k for k in required if not os.getenv(k)]
    
    if missing:
        print(f"\n缺少配置: {', '.join(missing)}")
        print("\n请设置以下环境变量:")
        print("  WECOM_CORP_ID     - 企业ID")
        print("  WECOM_SECRET      - 应用Secret")
        print("  WECOM_AGENT_ID   - 应用AgentID")
        print("  NVIDIA_API_KEY   - NVIDIA API Key")
        return
    
    from scripts.agent_manager import AgentManager
    from scripts.proactive_agent import ProactiveAgent
    from scripts.wecom_integration import WeComMessageHandler
    import requests
    from flask import Flask, request, jsonify
    
    # 创建 AI 智能体
    os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")
    
    manager = AgentManager()
    agent = manager.create_agent(
        "AI小助手",
        "meta/llama-3.1-70b-instruct",
        "企业微信群的活跃助手"
    )
    
    proactive = ProactiveAgent(agent, "AI小助手")
    proactive.config["cooldown"] = 30
    
    # 创建消息处理器
    handler = WeComMessageHandler(
        corp_id=os.getenv("WECOM_CORP_ID"),
        secret=os.getenv("WECOM_SECRET"),
        agent_id=os.getenv("WECOM_AGENT_ID")
    )
    handler.set_agent(proactive)
    
    # 创建 Flask 服务器
    app = Flask(__name__)
    
    @app.route("/wechat", methods=["GET", "POST"])
    def wechat():
        """企业微信回调"""
        # 验证签名（生产环境需要）
        
        if request.method == "GET":
            # 验证 URL
            echostr = request.args.get("echostr")
            return echostr
        
        # 处理消息
        msg_data = request.get_json()
        response = handler.handle_message(msg_data)
        
        if response:
            # 这里需要根据消息来源回复
            pass
        
        return jsonify({"errcode": 0})
    
    print("\n服务已启动!")
    print("请在企业微信后台配置回调 URL:")
    print("  URL: https://你的域名/wechat")
    print("  Token: 可自定义")
    print("  EncodingAESKey: 可自定义")
    print("\n按 Ctrl+C 退出")
    
    # 启动服务（需要公网域名）
    # app.run(host="0.0.0.0", port=8000)


def main():
    parser = argparse.ArgumentParser(description="企业微信 + Teamily AI")
    parser.add_argument("--test", action="store_true", help="测试模式")
    args = parser.parse_args()
    
    if args.test:
        test_mode()
    else:
        # 检查是否有企业微信配置
        if os.getenv("WECOM_CORP_ID"):
            run_mode()
        else:
            print("未检测到企业微信配置，切换到测试模式")
            test_mode()


if __name__ == "__main__":
    main()
