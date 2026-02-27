"""
小爱 AI - 魔搭社区 MCP 客户端
支持调用魔搭社区的 MCP 服务
"""

import json
import urllib.request
import urllib.parse
from typing import Dict, List, Any, Optional


class ModelScopeMCP:
    """
    魔搭社区 MCP 客户端
    
    功能：
    - 搜索 MCP 服务
    - 调用 MCP 工具
    - 管理 MCP 服务
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or ""
        self.base_url = "https://api.modelscope.cn/v1"
        self.mcp_registry = self._load_mcp_registry()
    
    def _load_mcp_registry(self) -> Dict[str, Dict]:
        """
        加载内置 MCP 服务注册表
        """
        return {
            "modelscope_search": {
                "name": "模型搜索",
                "description": "搜索魔搭社区的 AI 模型",
                "endpoint": "https://api.modelscope.cn/v1/models",
                "category": "search"
            },
            "modelscope_inference": {
                "name": "模型推理",
                "description": "调用魔搭社区的模型进行推理",
                "endpoint": "https://api.modelscope.cn/v1/inference",
                "category": "ai"
            },
            "alipay": {
                "name": "支付宝支付",
                "description": "支付宝交易创建、查询、退款",
                "endpoint": "https://mcp.alipay.com/api",
                "category": "payment",
                "require_auth": True
            },
            "minimax_tts": {
                "name": "MiniMax 语音合成",
                "description": "语音生成、语音克隆",
                "endpoint": "https://api.minimax.chat/v1/t2a",
                "category": "audio"
            },
            "minimax_image": {
                "name": "MiniMax 图像生成",
                "description": "图片生成",
                "endpoint": "https://api.minimax.chat/v1/image_generation",
                "category": "image"
            },
            "minimax_video": {
                "name": "MiniMax 视频生成",
                "description": "视频生成",
                "endpoint": "https://api.minimax.chat/v1/video_generation",
                "category": "video"
            },
            "amap_map": {
                "name": "高德地图",
                "description": "地图服务、路线规划、地理编码",
                "endpoint": "https://restapi.amap.com/v3",
                "category": "map"
            },
            "web_search": {
                "name": "网页搜索",
                "description": "互联网搜索",
                "endpoint": "https://api.duckduckgo.com",
                "category": "search"
            }
        }
    
    def list_services(self, category: str = None) -> List[Dict]:
        """
        列出可用的 MCP 服务
        
        Args:
            category: 可选，按分类筛选
            
        Returns:
            MCP 服务列表
        """
        services = []
        for mcp_id, mcp_info in self.mcp_registry.items():
            if category is None or mcp_info.get("category") == category:
                services.append({
                    "id": mcp_id,
                    "name": mcp_info["name"],
                    "description": mcp_info["description"],
                    "category": mcp_info.get("category", "other")
                })
        return services
    
    def search_models(self, query: str, page: int = 1, page_size: int = 10) -> Dict:
        """
        搜索魔搭模型
        
        Args:
            query: 搜索关键词
            page: 页码
            page_size: 每页数量
            
        Returns:
            模型列表
        """
        url = f"{self.base_url}/models?query={urllib.parse.quote(query)}&page={page}&page_size={page_size}"
        
        try:
            req = urllib.request.Request(url)
            if self.api_key:
                req.add_header("Authorization", f"Bearer {self.api_key}")
            
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"error": str(e), "data": []}
    
    def call_mcp(self, mcp_id: str, params: Dict) -> Dict:
        """
        调用 MCP 服务
        
        Args:
            mcp_id: MCP 服务 ID
            params: 调用参数
            
        Returns:
            调用结果
        """
        if mcp_id not in self.mcp_registry:
            return {"error": f"未知的 MCP 服务: {mcp_id}"}
        
        mcp_info = self.mcp_registry[mcp_id]
        
        # 根据不同 MCP 服务调用
        if mcp_id == "modelscope_search":
            return self._call_search(params)
        elif mcp_id == "modelscope_inference":
            return self._call_inference(params)
        elif mcp_id.startswith("minimax"):
            return self._call_minimax(mcp_id, params)
        elif mcp_id == "amap_map":
            return self._call_amap(params)
        elif mcp_id == "web_search":
            return self._call_web_search(params)
        else:
            return {"error": f"暂不支持调用: {mcp_id}"}
    
    def _call_search(self, params: Dict) -> Dict:
        """调用模型搜索"""
        query = params.get("query", "")
        return self.search_models(query)
    
    def _call_inference(self, params: Dict) -> Dict:
        """调用模型推理"""
        model = params.get("model", "qwen/Qwen-7B-Chat")
        prompt = params.get("prompt", "")
        
        url = f"{self.base_url}/inference"
        data = {
            "model": model,
            "input": {"prompt": prompt}
        }
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode('utf-8'),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}" if self.api_key else ""
                }
            )
            
            with urllib.request.urlopen(req, timeout=60) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"error": str(e)}
    
    def _call_minimax(self, mcp_id: str, params: Dict) -> Dict:
        """调用 MiniMax MCP"""
        api_keys = params.get("api_key", self.api_key)
        if not api_keys:
            return {"error": "需要 MiniMax API Key"}
        
        endpoints = {
            "minimax_tts": "/v1/t2a",
            "minimax_image": "/v1/image_generation",
            "minimax_video": "/v1/video_generation"
        }
        
        endpoint = endpoints.get(mcp_id)
        if not endpoint:
            return {"error": f"未知的 MiniMax 服务: {mcp_id}"}
        
        url = f"https://api.minimax.chat{endpoint}"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_keys}"
        }
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(params.get("payload", {})).encode('utf-8'),
                headers=headers
            )
            
            with urllib.request.urlopen(req, timeout=120) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"error": str(e)}
    
    def _call_amap(self, params: Dict) -> Dict:
        """调用高德地图"""
        action = params.get("action", "geocode/geo")
        key = params.get("key", "")  # 需要高德 API Key
        
        url = f"https://restapi.amap.com/v3/{action}?key={key}"
        
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"error": str(e)}
    
    def _call_web_search(self, params: Dict) -> Dict:
        """调用网页搜索"""
        query = params.get("query", "")
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json"
        
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"error": str(e)}
    
    def get_categories(self) -> List[str]:
        """获取所有分类"""
        categories = set()
        for mcp_info in self.mcp_registry.values():
            categories.add(mcp_info.get("category", "other"))
        return sorted(list(categories))


def demo():
    """演示"""
    mcp = ModelScopeMCP()
    
    print("=" * 50)
    print("魔搭社区 MCP 服务演示")
    print("=" * 50)
    
    # 列出所有服务
    print("\n📦 可用的 MCP 服务:")
    services = mcp.list_services()
    for s in services:
        print(f"  - {s['name']}: {s['description']}")
    
    # 列出分类
    print("\n📂 服务分类:")
    categories = mcp.get_categories()
    print(f"  {', '.join(categories)}")
    
    # 搜索模型示例
    print("\n🔍 搜索模型示例:")
    result = mcp.search_models("llama")
    if "data" in result:
        print(f"  找到 {len(result['data'])} 个模型")
    else:
        print(f"  需要 API Key 才能搜索")


if __name__ == "__main__":
    demo()
