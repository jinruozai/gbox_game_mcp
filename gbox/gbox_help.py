class GboxHelp:
    def __init__(self):
        """初始化 GboxHelp 类，读取必要的文档文件"""
        import os
        # 使用绝对路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.api_doc_path = os.path.join(base_dir, "gbox", "doc", "gbox_api.md")
        self.example_doc_path = os.path.join(base_dir, "gbox", "doc", "gbox_example.gb")
        
        # 初始化变量
        self._api_content = ""
        self._example_content = ""
        self._api_sections = {}
        self._api_toc = ""  # 添加这个初始化
        
        # 初始化时加载文档
        self._load_api_doc()
        self._load_example_doc()
        
    def _load_api_doc(self):
        """加载 API 文档并解析成不同部分"""
        try:
            with open(self.api_doc_path, 'r', encoding='utf-8') as f:
                self._api_content = f.read()
                
            # 用 ---- 分割文档
            sections = self._api_content.split('\n----\n')
            
            # 第一部分是目录
            self._api_toc = sections[0].strip() if sections else ""
            
            # 解析其他部分为具体内容
            for section in sections[1:]:
                if not section.strip():
                    continue
                    
                # 分离标题和内容
                lines = section.strip().split('\n')
                if lines:
                    # 提取标题（去掉可能的 ### 前缀）
                    title = lines[0].lstrip('#').strip()
                    content = '\n'.join(lines)
                    self._api_sections[title] = content
                    
        except Exception as e:
            print(f"Error loading API doc: {e}")
            self._api_content = ""
            self._api_toc = ""  # 确保在出错时也有值
            
    def _load_example_doc(self):
        """加载语法说明文档"""
        try:
            with open(self.example_doc_path, 'r', encoding='utf-8') as f:
                self._example_content = f.read()
        except Exception as e:
            print(f"Error loading example doc: {e}")
            self._example_content = ""
            
    def get_api_toc(self):
        """获取 GBox API 文档目录
        
        Returns:
            str: API 文档目录内容
        """
        return self._api_toc if self._api_toc else "API 目录加载失败"
        
    def get_api_section(self, section_name):
        """获取指定类或命名空间的具体内容
        
        Args:
            section_name (str): 要查询的类或命名空间名称
            
        Returns:
            str: 对应的文档内容，如果未找到则返回 None
        """
        return self._api_sections.get(section_name)
        
    def get_syntax_guide(self):
        """获取完整的语法说明文档
        
        Returns:
            str: 语法说明文档内容
        """
        return self._example_content if self._example_content else "语法说明文档加载失败"

# 使用示例
if __name__ == "__main__":
    help = GboxHelp()
    
    # 获取目录
    print("=== API 目录 ===")
    print(help.get_api_toc())
    print("\n")
    
    # 获取特定类的文档
    print("=== GObj 类文档 ===")
    print(help.get_api_section("GObjShape"))
    print("\n")
    
    # 获取语法说明
    print("=== 语法说明 ===")
    print(help.get_syntax_guide())
