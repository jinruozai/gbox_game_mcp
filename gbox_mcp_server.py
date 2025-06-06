import argparse
from mcp.server.fastmcp import FastMCP
from gbox.gbox_tcp import GBoxTCP
from gbox.logger import get_logger

# 获取logger
logger = get_logger('server')

# 定义全局变量
# 全局配置
config = {
    'gbox_ip': '127.0.0.1:30080'  # GBox Runtime 默认地址
}

_gbox_tcp = None
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
        logger.error(f"获取到的工具信息格式不正确: {tools_info}")
        return False
        
    # 遍历工具列表并添加到MCP
    try:
        for tool in tools_info:
            # 检查工具信息是否包含必要的字段
            if not isinstance(tool, dict) or 'name' not in tool or 'description' not in tool:
                logger.warning(f"工具信息格式不正确，跳过: {tool}")
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
        logger.info(f"成功初始化 {len(tools_info)} 个工具")
        
        # 尝试通知工具变更
        try:
            if hasattr(tagmcp._mcp_server, 'send_notification'):
                tagmcp._mcp_server.send_notification('$/tools/changed', None)
        except Exception as e:
            logger.error(f"发送工具变更通知时出错: {str(e)}")
        
        return True
    except Exception as e:
        logger.error(f"初始化工具时发生错误: {str(e)}")
    return False


def init_tools():
    fetch_tools(mcp,"get_tools")


def parse_args():
    """解析命令行参数并更新全局配置"""
    parser = argparse.ArgumentParser(description='GBox MCP服务器')
    parser.add_argument('--gbox_ip', type=str, help='GBox Runtime 地址，格式为 ip:port，例如 127.0.0.1:30080')
    
    # 解析参数，只更新config中已有的项
    args = parser.parse_args()
    for k, v in vars(args).items():
        if k in config and v is not None:
            config[k] = v
    
    logger.info(f"使用服务器配置: " + ", ".join(f"{k}={v}" for k, v in config.items()))
    return config

if __name__ == "__main__":
    # 解析命令行参数并更新配置
    params = parse_args()
    
    # 初始化GBoxTCP实例
    _gbox_tcp = GBoxTCP(params['gbox_ip'])

    # 初始化工具
    init_tools()
    
    # Attempt to notify about tool changes (from init_tools). 
    # Statically registered tools/resources are available immediately.
    try:
        if hasattr(mcp._mcp_server, 'send_notification'):
            mcp._mcp_server.send_notification('$/tools/changed', None)
            logger.info("发送了动态获取工具变更的通知")
    except Exception as e:
        logger.error(f"发送工具变更通知时出错: {str(e)}")

    mcp.run(transport='stdio')
    
    