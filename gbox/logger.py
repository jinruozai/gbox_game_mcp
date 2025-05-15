import logging
import sys
import os

def setup_logger(name, level=logging.INFO, log_to_file=False, file_path=None):
    """
    设置并返回一个配置好的logger
    
    Args:
        name (str): 日志记录器名称
        level (int): 日志级别，默认为INFO
        log_to_file (bool): 是否将日志写入文件，默认为False
        file_path (str): 日志文件路径，如果未提供且log_to_file为True，则使用默认路径
        
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 防止重复添加处理器
    if logger.handlers:
        return logger
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # 创建标准错误流处理器
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)
    
    # 如果需要，创建文件处理器
    if log_to_file:
        if file_path is None:
            # 默认日志文件路径在项目根目录的logs文件夹下
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            logs_dir = os.path.join(base_dir, 'logs')
            os.makedirs(logs_dir, exist_ok=True)
            file_path = os.path.join(logs_dir, f'{name}.log')
        
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# 创建一个默认的根记录器
root_logger = setup_logger('gbox_mcp')

def get_logger(name=None):
    """
    获取一个已配置的日志记录器
    
    Args:
        name (str, optional): 记录器名称，如果不提供则使用根记录器
        
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    if name is None:
        return root_logger
    
    # 使用模块名组合记录器名称
    full_name = f'gbox_mcp.{name}'
    return setup_logger(full_name) 