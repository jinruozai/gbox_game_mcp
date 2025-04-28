#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用WebSocket接口执行ComfyUI工作流并实时获取图像
基于官方websockets_api_example_ws_images.py示例修改
"""

import websocket  # 需要安装: pip install websocket-client
import uuid
import json
import urllib.request
import urllib.parse
import os
import argparse
import io
from PIL import Image
import time
import datetime

# ComfyUI服务器地址
server_address = "127.0.0.1:8188"
# 默认工作流文件名
DEFAULT_WORKFLOW = "flux_schnell_checkpoint.json"

class ComfyUI:
    def __init__(self, server_addr=None):
        self.server_address = server_addr or server_address
        self.client_id = str(uuid.uuid4())
    
    def queue_prompt(self, prompt):
        """将工作流发送到ComfyUI服务器并排队执行"""
        p = {"prompt": prompt, "client_id": self.client_id}
        data = json.dumps(p).encode('utf-8')
        req = urllib.request.Request(f"http://{self.server_address}/prompt", data=data)
        try:
            return json.loads(urllib.request.urlopen(req).read())
        except urllib.error.HTTPError as e:
            print(f"HTTP错误: {e.code} - {e.reason}")
            print("请求数据:", json.dumps(p, indent=2))
            raise

    def get_images(self, ws, prompt):
        """通过WebSocket连接获取图像"""
        print("正在提交工作流...")
        prompt_id = self.queue_prompt(prompt)['prompt_id']
        print(f"等待图像生成，任务ID: {prompt_id}")
        
        output_images = {}
        current_node = ""
        
        # 设置超时和监控机制
        img_received = False
        last_msg_time = time.time()
        no_msg_timeout = 15  # 15秒没有新消息则认为可能已完成
        
        while True:
            try:
                out = ws.recv()
                last_msg_time = time.time()
                
                if isinstance(out, str):
                    message = json.loads(out)
                    
                    if message['type'] == 'executing':
                        data = message['data']
                        
                        if data['prompt_id'] == prompt_id:
                            if data['node'] is None:
                                print("工作流执行完成!")
                                break  # 执行完成
                            else:
                                current_node = data['node']
                                print(f"正在执行节点: {current_node}")
                else:
                    # 这是图像数据
                    print(f"收到来自节点 '{current_node}' 的图像数据")
                    images_output = output_images.get(current_node, [])
                    images_output.append(out[8:])  # 去掉WebSocket图像前缀
                    output_images[current_node] = images_output
                    img_received = True
                    
                # 检查是否已收到图像且一段时间没有新消息，可能服务器未发送明确的完成消息
                current_time = time.time()
                if img_received and (current_time - last_msg_time) > no_msg_timeout:
                    print(f"已超过 {no_msg_timeout} 秒没有新消息，且已收到图像数据，认为工作流可能已完成")
                    break
                    
            except websocket.WebSocketTimeoutException as e:
                print(f"WebSocket超时: {e}")
                if img_received:
                    print("已接收图像数据，尽管超时，继续处理")
                    break
                else:
                    raise  # 如果还没有收到任何图像，则重新抛出异常
        
        if output_images:
            print(f"已收集图像数据，准备处理")
        return output_images

    def add_websocket_node(self, workflow_data):
        """添加SaveImageWebsocket节点到工作流"""
        # 检查工作流中是否已经有SaveImageWebsocket节点
        for node_id, node in workflow_data.items():
            if node.get("class_type") == "SaveImageWebsocket":
                print("工作流已包含SaveImageWebsocket节点")
                return workflow_data
        
        # 查找VAEDecode节点和SaveImage节点
        vae_node_id = None
        save_node_id = None
        save_node_input = None
        
        for node_id, node in workflow_data.items():
            if node.get("class_type") == "VAEDecode":
                vae_node_id = node_id
            elif node.get("class_type") == "SaveImage":
                save_node_id = node_id
                if "inputs" in node and "images" in node["inputs"]:
                    save_node_input = node["inputs"]["images"]
        
        # 如果找到SaveImage节点的输入，使用它
        if save_node_input:
            input_source = save_node_input
            print(f"使用SaveImage节点的输入源: {input_source}")
        # 否则尝试使用VAEDecode节点的输出
        elif vae_node_id:
            input_source = [vae_node_id, 0]
            print(f"使用VAEDecode节点输出作为输入源: {input_source}")
        else:
            print("警告: 无法找到合适的图像输入源，工作流可能无法正常工作")
            return workflow_data
        
        # 添加SaveImageWebsocket节点
        workflow_data["save_image_websocket_node"] = {
            "class_type": "SaveImageWebsocket",
            "inputs": {
                "images": input_source
            }
        }
        
        print("已添加SaveImageWebsocket节点到工作流")
        return workflow_data
    
    def generate_images(self, prompt_text=None, workflow_path=None, output_dir=None):
        """
        生成图像并返回保存的文件路径列表
        
        Args:
            prompt_text: 提示词文本
            workflow_path: 工作流文件名或路径
            output_dir: 输出目录
        
        Returns:
            保存的图像路径列表
        """
        # 设置输出目录
        if output_dir is None:
            import tempfile
            import os.path
            # 使用固定的临时目录
            temp_dir = os.path.join(tempfile.gettempdir(), "gbox_comfyui_images")
            os.makedirs(temp_dir, exist_ok=True)
            output_dir = temp_dir
            print(f"使用临时目录: {output_dir}")
        else:
            # 使用用户指定的目录
            os.makedirs(output_dir, exist_ok=True)
        
        # 加载工作流JSON文件
        if workflow_path:
            # 首先检查传入的是否为完整路径
            if os.path.exists(workflow_path):
                workflow_file = workflow_path
                print(f"使用指定的工作流文件: {workflow_file}")
            else:
                # 尝试作为文件名在workflow目录中查找
                workflow_dir = os.path.join(os.path.dirname(__file__), "workflow")
                potential_file = os.path.join(workflow_dir, workflow_path)
                
                if os.path.exists(potential_file):
                    workflow_file = potential_file
                    print(f"使用工作流文件: {workflow_file}")
                else:
                    # 尝试添加.json扩展名
                    if not workflow_path.endswith('.json'):
                        potential_file_with_ext = os.path.join(workflow_dir, f"{workflow_path}.json")
                        if os.path.exists(potential_file_with_ext):
                            workflow_file = potential_file_with_ext
                            print(f"使用工作流文件: {workflow_file}")
                        else:
                            # 如果都找不到，使用默认工作流
                            print(f"警告: 找不到工作流文件 '{workflow_path}'，使用默认工作流")
                            workflow_file = os.path.join(workflow_dir, DEFAULT_WORKFLOW)
                            if not os.path.exists(workflow_file):
                                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                                workflow_file = os.path.join(base_dir, "comfyui", "workflow", DEFAULT_WORKFLOW)
                    else:
                        # 如果找不到，使用默认工作流
                        print(f"警告: 找不到工作流文件 '{workflow_path}'，使用默认工作流")
                        workflow_file = os.path.join(workflow_dir, DEFAULT_WORKFLOW)
                        if not os.path.exists(workflow_file):
                            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                            workflow_file = os.path.join(base_dir, "comfyui", "workflow", DEFAULT_WORKFLOW)
        else:
            # 使用默认路径
            workflow_file = os.path.join(os.path.dirname(__file__), "workflow", DEFAULT_WORKFLOW)
            if not os.path.exists(workflow_file):
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                workflow_file = os.path.join(base_dir, "comfyui", "workflow", DEFAULT_WORKFLOW)
            print(f"使用默认工作流文件: {workflow_file}")
        
        try:
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
        except Exception as e:
            print(f"加载工作流文件失败: {e}")
            raise
        
        # 如果文件不是以提示词节点，尝试找到合适的提示词节点
        prompt_node = None
        if prompt_text:
            # 首先尝试找到可能的提示词节点
            for node_id, node in workflow_data.items():
                if node.get("class_type") == "CLIPTextEncode" and "inputs" in node and "text" in node["inputs"]:
                    if not prompt_node or node_id == "6":  # 优先使用id为6的节点，这是常见的正向提示词节点
                        prompt_node = node_id
            
            if prompt_node:
                old_prompt = workflow_data[prompt_node]["inputs"]["text"]
                workflow_data[prompt_node]["inputs"]["text"] = prompt_text
                print(f"提示词: {prompt_text}")
            else:
                print("警告: 未找到提示词节点，将使用原始提示词")
        else:
            print("未提供提示词，使用原始提示词")
        
        # 添加SaveImageWebsocket节点到工作流
        workflow_data = self.add_websocket_node(workflow_data)
        
        # 连接WebSocket
        print(f"连接WebSocket服务器: ws://{self.server_address}/ws?clientId={self.client_id}")
        ws = websocket.WebSocket()
        
        # 设置超时时间，避免永久等待
        ws.settimeout(60)  # 设置60秒超时
        
        saved_paths = []
        
        try:
            ws.connect(f"ws://{self.server_address}/ws?clientId={self.client_id}")
            
            # 获取图像
            try:
                images = self.get_images(ws, workflow_data)
            except websocket.WebSocketTimeoutException:
                print("警告: WebSocket接收消息超时，可能是服务器没有发送完成消息")
                print("尝试继续处理已收到的图像")
                images = {}  # 如果出现超时，使用空字典
            except Exception as e:
                print(f"获取图像时出错: {e}")
                raise
            
            # 保存图像
            image_count = 0
            
            # 生成唯一标识符
            # 使用时间戳和随机UUID组合生成唯一标识符
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_id = str(uuid.uuid4())[:8]  # 使用UUID的前8位
            
            for node_id, image_list in images.items():
                for i, image_data in enumerate(image_list):
                    try:
                        image = Image.open(io.BytesIO(image_data))
                        # 使用时间戳、唯一ID和计数器组合生成唯一文件名
                        output_name = f"comfyui_{timestamp}_{unique_id}_{image_count}.png"
                        output_path = os.path.join(output_dir, output_name)
                        image.save(output_path)
                        saved_paths.append(output_path)
                        # 获取并显示保存图片的完整绝对路径
                        full_output_path = os.path.abspath(output_path)
                        print(f"图像已保存: {full_output_path}")
                        image_count += 1
                    except Exception as e:
                        print(f"保存图像失败: {e}")
            
            print(f"\n成功生成并保存 {image_count} 张图像")
            
            # 尝试自动打开第一张图片
            if saved_paths:
                try:
                    first_image_path = saved_paths[0]
                    # 尝试使用系统默认方式打开图片
                    import subprocess
                    import platform
                    
                    system = platform.system()
                    try:
                        if system == 'Darwin':  # macOS
                            subprocess.run(['open', first_image_path], check=True)
                        elif system == 'Windows':
                            os.startfile(first_image_path)
                        elif system == 'Linux':
                            subprocess.run(['xdg-open', first_image_path], check=True)
                        # 获取并显示图片的完整绝对路径
                        full_image_path = os.path.abspath(first_image_path)
                        print(f"已尝试在系统默认应用中打开图片: {full_image_path}")
                    except Exception as e:
                        # 如果系统命令打开失败，不要报错，只打印信息
                        print(f"自动打开图片失败: {e}")
                except Exception as e:
                    # 如果任何部分失败，不影响主功能
                    print(f"尝试自动打开图片时出错: {e}")
            
        except Exception as e:
            print(f"执行工作流时出错: {e}")
            raise
        finally:
            try:
                ws.close()
            except:
                pass
        
        return saved_paths

def run_comfyui(prompt=None, output_dir=None, workflow_file=None, server_addr=None):
    """运行ComfyUI生成图像的便捷函数"""
    comfy = ComfyUI(server_addr)
    return comfy.generate_images(prompt, workflow_file, output_dir)

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='执行ComfyUI工作流并实时获取图像')
    parser.add_argument('prompt', nargs='?', help='可选的提示词，如不提供则使用原始提示词')
    parser.add_argument('--output', '-o', help='图像输出目录，如不提供则使用临时目录')
    parser.add_argument('--workflow', '-w', help='工作流JSON文件名或路径，如不提供则使用默认路径')
    parser.add_argument('--server', '-s', help='ComfyUI服务器地址')
    args = parser.parse_args()
    
    # 运行ComfyUI
    try:
        run_comfyui(
            prompt=args.prompt,
            output_dir=args.output,
            workflow_file=args.workflow,
            server_addr=args.server
        )
    except Exception as e:
        print(f"执行失败: {e}")
        import sys
        sys.exit(1) 