import os
import sys
import asyncio
import threading
import argparse
from mcp.server.fastmcp import FastMCP
from gboxtcp import GBoxTCP
import time
from typing import Dict, List, Union
from mcp.server.lowlevel.server import NotificationOptions
from gbox.gbox_help import GboxHelp
# 定义全局变量
# 全局配置
config = {
    'gbox_ip': '127.0.0.1:30080',  # GBox Runtime 默认地址
    'comfyui_ip': 'http://127.0.0.1:8188'  # ComfyUI 默认地址
}

_gbox_tcp = None
_gbox_help = GboxHelp()
# 初始化MCP
mcp = FastMCP("GBox")
# 启用工具变更通知
mcp._mcp_server.notification_options.tools_changed = True

def fetch_tools(tagmcp,funname,params=None)->bool:
    """初始化所有工具"""
    # 获取工具列表
    tools_info = _gbox_tcp.call(None, funname,params)  # obj 为 None，因为是全局函数
    
    # 检查tools_info是否为列表类型
    if not isinstance(tools_info, list):
        print(f"获取到的工具信息格式不正确: {tools_info}")
        return False
        
    # 遍历工具列表并添加到MCP
    try:
        for tool in tools_info:
            # 检查工具信息是否包含必要的字段
            if not isinstance(tool, dict) or 'name' not in tool or 'description' not in tool:
                print(f"工具信息格式不正确，跳过: {tool}")
                continue
                
            # 为每个工具创建一个lambda函数，捕获工具名称、对象引用和参数定义
            tool_func = lambda tool_name=tool['name'], tool_obj=tool['obj'], tool_params=tool.get('parameters'): \
                _gbox_tcp.call(tool_obj, tool_name, tool_params)
                
            # 添加工具到MCP
            tagmcp.add_tool(
                tool_func,
                name=tool['name'],
                description=tool['description']
            )
        print(f"成功初始化 {len(tools_info)} 个工具")
        
        # 尝试通知工具变更
        try:
            if hasattr(tagmcp._mcp_server, 'send_notification'):
                tagmcp._mcp_server.send_notification('$/tools/changed', None)
        except Exception as e:
            print(f"发送工具变更通知时出错: {str(e)}")
        
        return True
    except Exception as e:
        print(f"初始化工具时发生错误: {str(e)}")
    return False


def init_tools():
    fetch_tools(mcp,"get_tools")

@mcp.tool()
def get_gbox_api_toc() -> str:
    """获取 GBox API 文档目录。
    
    GBox 引擎在不断发展，预训练的知识可能已经过时，不能完全依赖。
    此工具用于获取最新的 GBox API 目录结构，帮助你了解所有可用的类和命名空间。
    无论你对 GBox 有多熟悉，在处理任何 GBox 相关的问题时，都应该先调用此工具了解最新的 API 结构。
    如果你的已有知识与文档内容有冲突，应该以文档为准。
    
    使用场景：
    - 当你需要快速浏览 GBox API 的整体结构
    - 想要了解有哪些可用的类和命名空间
    - 需要查找特定功能所在的类或命名空间时
    
    重要提示：
    在进行以下操作前，应当先通过此工具了解 GBox API 的整体结构：
    - 修改或创建 .gb 文件
    - 回答 GBox 相关的问题
    - 提供 GBox 相关的建议
    这样可以确保你对 GBox 的功能体系有全面的认识，避免给出不准确的信息。
    """
    return _gbox_help.get_api_toc()

@mcp.tool()
def get_gbox_api_section(section_name: str) -> str:
    """获取 GBox API 中指定类或命名空间的详细文档。
    
    GBox 引擎在不断发展，预训练的知识可能已经过时，不能完全依赖。
    此工具用于获取最新的 GBox API 详细文档，确保你使用的是最新的接口和正确的用法。
    无论你对某个 GBox 类或功能有多熟悉，在使用它们之前，都应该先调用此工具查看最新文档。
    如果你的已有知识与文档内容有冲突，应该以文档为准。
    
    使用场景：
    - 当你需要查看某个具体类或命名空间的详细说明
    - 需要了解特定类的方法和属性时
    - 想要深入学习某个功能模块的使用方法
    
    重要提示：
    在进行以下操作前，必须先通过此工具查阅相关类或命名空间的详细文档：
    - 使用或修改特定的 GBox 类
    - 回答关于特定 GBox 功能的问题
    - 编写涉及特定 GBox 类的代码
    这确保了你完全理解了相关功能的使用方法和限制，能够提供准确的建议和实现。
    
    Args:
        section_name: 要查询的类或命名空间名称
    """
    result = _gbox_help.get_api_section(section_name)
    if result is None:
        return f"Error: Section '{section_name}' not found in API documentation"
    return result

@mcp.tool()
def get_gbox_syntax_guide() -> str:
    """获取 GBox 语法说明文档。
    
    GBox 引擎在不断发展，预训练的知识可能已经过时，不能完全依赖。
    此工具用于获取最新的 GBox 语法规则说明，确保你使用的是正确的语法格式。
    无论你对 GBox 语法有多熟悉，在编写或修改代码之前，都应该先调用此工具查看最新的语法规则。
    如果你的已有知识与文档内容有冲突，应该以文档为准。
    
    使用场景：
    - 当你需要了解 GBox 的基本语法规则时
    - 在开始编写 GBox 代码之前，建议先阅读此文档
    - 当遇到语法相关的错误时，可以查阅此文档进行排查
    
    重要提示：
    在进行以下操作前，应当先通过此工具熟悉 GBox 的语法规则：
    - 编写或修改任何 .gb 文件
    - 回答有关 GBox 语法的问题
    - 调试 GBox 代码问题
    这确保了你能够按照正确的语法规范提供建议和实现，避免语法错误。
    """
    return _gbox_help.get_syntax_guide()

@mcp.tool()
def generate_ai_image(prompt: str, workflow_file: str = None) -> Dict[str, Union[List[str], List[str]]]:
    """使用 ComfyUI 根据文本提示生成 AI 图像。
    
    使用场景：
    - 当你需要根据文本描述生成图像时
    - 为项目创建视觉内容或概念图
    - 生成艺术作品或设计灵感
    - 根据用户输入的描述创建可视化内容
    
    Args:
        prompt: 描述想要生成的图像内容的文本提示词
        workflow_file: 可选，指定自定义的 ComfyUI 工作流文件路径
        
    Returns:
        包含生成图像信息的字典，包括：
        - file_paths: 保存的图像文件路径列表
    """
    from comfyui_workflow.comfyui import ComfyUI
    
    try:
        # 设置输出目录
        output_dir = os.path.join(os.path.dirname(__file__), "generated_images")
        os.makedirs(output_dir, exist_ok=True)
        
        # 创建ComfyUI实例，使用配置的地址
        comfy = ComfyUI(config['comfyui_ip'])
        file_paths = comfy.generate_images(
            prompt_text=prompt,
            workflow_path=workflow_file,
            output_dir=output_dir
        )
        
        # 返回结果
        return {
            "file_paths": file_paths
        }
    except Exception as e:
        print(f"生成图像时发生错误: {str(e)}")
        return {"error": str(e), "file_paths": []}

def parse_args():
    """解析命令行参数并更新全局配置"""
    parser = argparse.ArgumentParser(description='GBox MCP服务器')
    parser.add_argument('--gbox_ip', type=str, help='GBox Runtime 地址，格式为 ip:port，例如 127.0.0.1:30080')
    parser.add_argument('--comfyui_ip', type=str, help='ComfyUI 服务器地址')
    
    # 解析参数，只更新config中已有的项
    args = parser.parse_args()
    for k, v in vars(args).items():
        if k in config and v is not None:
            config[k] = v
    
    print(f"使用服务器配置:", ", ".join(f"{k}={v}" for k, v in config.items()))
    return config

if __name__ == "__main__":
    # 解析命令行参数并更新配置
    params = parse_args()
    
    # 初始化GBoxTCP实例
    _gbox_tcp = GBoxTCP(gbox=params['gbox_ip'])

    # 初始化工具
    init_tools()
    
    # Attempt to notify about tool changes (from init_tools). 
    # Statically registered tools/resources are available immediately.
    try:
        if hasattr(mcp._mcp_server, 'send_notification'):
            mcp._mcp_server.send_notification('$/tools/changed', None)
            print("Sent notification about dynamically fetched tool changes.")
    except Exception as e:
        print(f"发送工具变更通知时出错: {str(e)}")

    mcp.run(transport='stdio')
    
    