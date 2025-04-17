import socket
import threading
import time
import json

class GBoxTCP:
    def __init__(self, gbox_ip='127.0.0.1:30080'):
        """初始化GBoxTCP实例
        
        Args:
            gbox (str): GBox Runtime 地址，格式为 ip:port，例如 127.0.0.1:30080
        """
        # 解析地址
        try:
            self.ip, port = gbox_ip.split(':')
            self.port = int(port)
        except ValueError:
            # 如果解析失败，使用默认值
            self.ip = '127.0.0.1'
            self.port = 30080
            
        self.sock = None
        self.connected = False
        self.receive_thread = None
        self.running = False
        self.response_event = threading.Event()
        self.last_response = None
        self.waiting_for_response = False
        print(f"初始化GBoxTCP实例: {self.ip}:{self.port}")
        # 初始化时直接连接
        self.connect()

    def connect(self):
        """建立TCP连接"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5)
            self.sock.connect((self.ip, self.port))
            self.connected = True
            
            # 启动接收线程
            self.running = True
            self.receive_thread = threading.Thread(target=self._receive_loop)
            self.receive_thread.daemon = True
            self.receive_thread.start()
            
            return True
        except Exception as e:
            self.connected = False
            return False

    def send(self, message: str):
        """发送原始字符串"""
        if not self.connected:
            if not self.connect():
                return False
                
        # 统一消息格式：移除所有可能的结尾符，然后添加一个标准的\r\n
        message = message.rstrip('\r\n') + '\r\n'
        
        try:
            # 发送数据
            # 转换为UTF-16LE (Unicode)格式
            data = message.encode('utf-16le')
            total_sent = 0
            while total_sent < len(data):
                sent = self.sock.send(data[total_sent:])
                if sent == 0:
                    raise RuntimeError("连接断开")
                total_sent += sent
            return True
        except Exception as e:
            self.connected = False
            return False

    def _receive_loop(self):
        """接收消息的循环"""
        buffer = bytearray()
        self.sock.settimeout(1)
        
        while self.running:
            try:
                data = self.sock.recv(1024)
                if not data:
                    self.connected = False
                    break
                
                # 添加到字节缓冲区
                buffer.extend(data)
                
                # 处理可能的多行数据
                while True:
                    # 查找\n的Unicode编码
                    try:
                        cr_index = buffer.index(b'\n\x00')
                        # 提取一行（不包含\n）
                        line = buffer[:cr_index].decode('utf-16le')
                        # 移除已处理的数据（包含\n）
                        buffer = buffer[cr_index + 2:]
                        # 去除可能的\r
                        line = line.rstrip('\r')
                        print(f"收到原始数据: {line}")
                        self._on_message_received(line)
                    except ValueError:
                        # 没有找到完整的行，但这是正常的
                        break
                    except UnicodeDecodeError as e:
                        # 清空有问题的数据
                        buffer = buffer[cr_index + 2:]
                        continue
                
            except socket.timeout:
                # 超时是正常的，继续等待
                continue
            except Exception as e:
                if self.running:
                    self.connected = False
                break

    def _on_message_received(self, message: str):
        """处理接收到的消息"""
        print(f"开始解析消息: {message}")
        if self.waiting_for_response:
            try:
                parsed_response = orjson.loads(message)
                print(f"解析后的数据: {parsed_response}")
                print(f"解析后itemid类型: {type(parsed_response.get('result', {}).get('itemid'))}")
                self.last_response = message
            except Exception as e:
                print(f"解析JSON时出错: {e}")
                self.last_response = message
            self.response_event.set()
            self.waiting_for_response = False

    def close(self):
        """关闭连接"""
        self.running = False
        
        if self.receive_thread:
            self.receive_thread.join(timeout=2)
        
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
        
        self.connected = False
        self.sock = None

    def __del__(self):
        """析构函数，确保资源被正确释放"""
        self.close()

    def call(self, obj, function_name, params=None):
        """调用GBox函数
        
        Args:
            obj (str): 对象地址，例如 "&03E3FC48:4E"
            function_name (str): 函数名
            params (dict, optional): 函数参数字典
            
        Returns:
            str: 函数返回值，如果调用失败返回None
        """
        if params is None:
            params = {}
            
        # 构造JSON消息
        message = {
            "obj": obj,
            "name": function_name,
            "arguments": params
        }
        
        # 重置响应事件和上次响应
        self.response_event.clear()
        self.last_response = None
        self.waiting_for_response = True
        
        # 发送JSON消息
        s=json.dumps(message)
        print(f"发送消息: {s}")
        if not self.send(s):
            self.waiting_for_response = False
            return None
            
        # 等待响应，最多等待5秒
        if not self.response_event.wait(5):
            self.waiting_for_response = False
            return None
            
        # 尝试解析响应为JSON
        try:
            response = json.loads(self.last_response)
            if isinstance(response, dict) and 'result' in response:
                return response['result']
            return response
        except json.JSONDecodeError:
            return {"raw_response": self.last_response}