# GBox Game MCP Server

GBox Game MCP Server 是一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的游戏运行时控制服务器，专门用于与正在运行的 GBox 游戏实例进行实时通信和控制。它能够动态发现和调用游戏中的工具和函数，实现对游戏状态的智能操作和管理。

## 关于 GBox 游戏引擎

GBox 是一个跨平台的轻量级游戏引擎，提供以下核心功能：

- **2D/3D 图形渲染** - 高性能的渲染管线
- **粒子特效系统** - 丰富的视觉效果
- **动画系统** - 帧动画和3D模型动画
- **UI 界面开发** - 完整的界面控件体系
- **音频处理** - 音频播放、录制和特效
- **资源管理** - 高效的资源加载和缓存
- **脚本编程** - 支持自定义的 .gb 脚本语言

## 主要功能

### 游戏运行时控制
- **TCP 连接通信** - 通过 TCP 协议与运行中的 GBox 游戏实例建立连接
- **动态工具发现** - 自动发现游戏中可用的工具和函数
- **实时函数调用** - 支持调用游戏中的任意函数，传递参数并获取返回值
- **状态监控** - 实时监控游戏状态变化
- **智能控制** - 通过 AI 助手实现对游戏的智能操作

### 核心特性
- **异步通信** - 基于多线程的异步消息处理
- **JSON 协议** - 使用 JSON 格式进行数据交换
- **UTF-16 编码** - 支持 Unicode 字符编码
- **自动重连** - 连接断开时自动尝试重新连接
- **错误处理** - 完善的错误处理和日志记录

## 工作原理

1. **连接建立**：服务器启动时自动连接到指定的 GBox 游戏实例
2. **工具发现**：通过调用 `get_tools` 函数动态获取游戏中可用的工具列表
3. **MCP 注册**：将发现的工具注册到 MCP 框架中
4. **实时调用**：AI 助手可以通过 MCP 调用这些工具，实现对游戏的控制

## 安装和使用

### 系统要求

- Python 3.8 或更高版本
- MCP 兼容的 AI 客户端（如 Claude Desktop、Cline 等）
- 运行中的 GBox 游戏实例（监听 TCP 端口）

### 安装步骤

1. 克隆或下载本项目：
```bash
git clone <repository-url>
cd gbox_game_mcp
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

### 配置 MCP 客户端

在您的 MCP 客户端配置文件中添加以下配置：

```json
{
  "mcpServers": {
    "gbox-game": {
      "command": "python",
      "args": [
        "/path/to/gbox_game_mcp/gbox_mcp_server.py",
        "--gbox_ip", "127.0.0.1:30080"
      ]
    }
  }
}
```

### 配置参数

- `--gbox_ip`: GBox 游戏实例的 TCP 地址，格式为 `ip:port`
  - 默认值：`127.0.0.1:30080`
  - 示例：`192.168.1.100:8080`

### 使用示例

配置完成后，AI 助手将能够：

1. **查看可用工具**：
   ```
   请列出当前游戏中可用的所有工具
   ```

2. **控制游戏对象**：
   ```
   请移动角色到坐标 (100, 200)
   ```

3. **查询游戏状态**：
   ```
   请获取当前关卡的所有敌人列表
   ```

4. **执行游戏操作**：
   ```
   请暂停游戏并保存当前进度
   ```

## 项目结构

```
gbox_game_mcp/
├── gbox_mcp_server.py          # MCP 服务器主程序
├── gbox/                       # 核心模块目录
│   ├── gbox_tcp.py            # TCP 通信核心类
│   ├── logger.py              # 日志记录模块
│   ├── gbox_mcp_client.gb     # GBox 客户端脚本
│   └── generate_gbox_api.gb   # API 生成脚本
├── requirements.txt           # Python 依赖
├── LICENSE                    # MIT 许可证
└── README.md                  # 项目说明
```

## 技术细节

### TCP 通信协议
- **编码格式**：UTF-16LE (Unicode)
- **消息格式**：JSON 字符串，以 `\r\n` 结尾
- **连接管理**：自动重连和心跳检测
- **异步处理**：基于线程的消息接收和处理

### 消息格式
发送到游戏的消息格式：
```json
{
  "obj": "对象地址（如 &03E3FC48:4E）",
  "name": "函数名",
  "arguments": {
    "参数名": "参数值"
  }
}
```

### 工具注册
- 动态发现游戏中的工具
- 自动注册到 MCP 框架
- 支持工具变更通知

## 开发和调试

### 启动服务器
```bash
python gbox_mcp_server.py --gbox_ip 127.0.0.1:30080
```

### 查看日志
服务器运行时会输出详细的调试信息，包括：
- TCP 连接状态
- 消息发送和接收
- 工具注册过程
- 错误和异常处理

### 常见问题

1. **连接失败**：检查 GBox 游戏是否正在运行并监听指定端口
2. **工具列表为空**：确认游戏中已实现 `get_tools` 函数
3. **调用超时**：检查网络连接和游戏响应速度

## 与其他项目的关系

- **gbox_engine_mcp**：提供 GBox 引擎的文档查询功能，与本项目互补
- **GBox 脚本**：支持通过 .gb 脚本扩展游戏功能
- **游戏资源管理**：可以集成第三方工具生成游戏素材

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 相关链接

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [FastMCP 文档](https://github.com/jlowin/fastmcp)
- [GBox 游戏引擎文档服务器](../gbox_engine_mcp/)

---

**注意**：本项目专注于游戏运行时控制，如需 GBox 引擎的文档查询功能，请参考 [gbox_engine_mcp](../gbox_engine_mcp/) 项目。 