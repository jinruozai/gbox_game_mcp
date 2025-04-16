# GBox MCP Server

GBox MCP Server 是一个基于 FastMCP 协议的服务器实现，提供了与 GBox 游戏引擎的实时通信和控制能力。它能帮助 AI 理解和操作 GBox 脚本，实现游戏运行时的智能控制和资源管理。同时通过与 ComfyUI 的集成，支持基于文本描述生成游戏素材和图像资源。

## Gbox游戏引擎介绍

Gbox是一个跨平台的轻量级游戏引擎,提供2D/3D图形渲染、粒子特效系统、动画系统、UI界面开发、音频处理、资源管理和脚本编程，让开发者能快速创建高质量游戏和交互应用

## 文档链接

- [Gbox API 文档](gbox/doc/gbox_api.md)
- [Gbox 语法文档](gbox/doc/gbox_syntax.md)
- [Gbox 语法示例](gbox/doc/gbox_example.gb)

## 功能特点

- 基于 FastMCP 协议实现
- 帮助AI理解Gbox脚本编程，并提供对Gbox游戏运行时的控制
- 与ComfyUI集成，支持直接在Gbox应用中生成和处理图像

## 系统要求

- Python 3.6+
- FastMCP
- ComfyUI (用于图像生成功能)

## 安装

1. 克隆仓库：

2. 安装依赖：
```bash
pip install -r requirements.txt
```

### MCP 配置方法

在您的 MCP 客户端配置中添加以下配置：

{
    "gbox": {
        "command": "python",
        "args": [
            "/path/to/gbox_mcp/gbox_mcp_server.py",
            "--gbox_ip", "gbox runtime address (ip:port), e.g. 127.0.0.1:30080",
            "--comfyui_ip", "http://127.0.0.1:8188"
        ]
    }
}

配置说明：
- `command`: 使用 python 执行服务器脚本
- `args`: 服务器脚本路径和参数
  - 第一个参数为服务器脚本的完整路径
  - `--gbox_ip`: 设置服务器监听的 GBox 地址（可选）
  - `--comfyui_ip`: ComfyUI服务器地址（可选），用于图像生成和处理功能

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。 