# UI系统库 (ui_sys) API文档

UI系统库是一个用于创建用户界面的综合工具包，提供了丰富的UI组件、样式和工具函数。

## 目录结构

- **base**: 基础UI组件
- **adv**: 高级UI组件
- **style**: UI样式系统
- **mod**: 功能模块
- **res**: 资源文件

## 基础组件 (base)

### SysBtn

按钮组件，继承自SysText和SysBtnStyle。

**配置属性**:
- `shapecolor`: 按钮形状颜色 (默认: rgb#ff383b42)
- `roundcorner`: 圆角半径 (默认: 5)
- `outrect`: 外部矩形偏移 (默认: vec4(3,3,-3,-3))
- `alignh`: 水平对齐方式 (默认: 1)
- `alignv`: 垂直对齐方式 (默认: 1)
- `sound_click`: 点击音效资源 (默认: res#0433B6CA_00DA0105)

**成员变量**:
- `m_vRect`: 按钮区域 (默认: vec4(0,0,100,24))

**方法**:
- `void SetDef(string name, var fun=nil, obj p=NULL, float w=100, float h=24)`: 设置按钮默认属性
- `void SetImgBtn(var res, var fun, obj p=NULL, int c=0, float w=32, float h=32)`: 设置图片按钮
- `void SetMainColor(int c)`: 设置按钮主色调
- `void OnTouchSound(var &dn)`: 按钮触摸音效处理

### SysDragOutBtn

可拖拽按钮，继承自SysBtn。

**方法**:
- `int IsCanDragOut()`: 判断是否可拖出 (默认返回1)
- `void OnTouch(var &dn)`: 处理触摸事件
- `void BeginSysDrag(obj pshow, var &dat)`: 开始拖拽
- `void EndSysDrag(obj to, var dat)`: 结束拖拽

### SysEdit

编辑框组件，继承自GObjEdit、SysLinkChgStyle、SysAlign和SysAutoTabStyle。

**配置属性**:
- `actshapecolor`: 活动状态背景色 (默认: rgb#ff555555)
- `cursorcolor`: 光标颜色 (默认: rgb#ffeeeeee)
- `selbkcolor`: 选中背景色 (默认: rgb#FF6087EA)
- `shapecolor`: 形状颜色 (默认: rgb#FF33353A)
- `textcolor`: 文本颜色 (默认: rgb#fff2f2f2)
- `roundcorner`: 圆角半径 (默认: 3)

**成员变量**:
- `m_nFormat`: 格式类型
- `m_nEnterClear`: 回车后是否清空
- `m_nIsEdtingCall`: 输入过程中是否call
- `m_nEnterKeepActive`: 回车后是否保持激活
- `m_nUnactiveNotCall`: 失去焦点时是否不调用
- `m_szMinMax`: 最小最大值范围

**方法**:
- `void SetDef(string name, var linkcall="", obj linkobj=NULL)`: 设置编辑框默认属性
- `void SetFormat(int kind)`: 设置格式类型
- `void SetEditingCall(int b)`: 设置是否在编辑过程中调用回调
- `void SetEnterClear(int b)`: 设置回车后是否清空
- `void SetEnterKeepActive(int b)`: 设置回车后是否保持活跃状态
- `int _SetValue(var value)`: 设置值
- `var GetValue()`: 获取值
- `void SetMinMax(float fmin, float fmax)`: 设置最小最大值
- `int Active()`: 激活编辑框
- `void UnActive()`: 取消激活
- `void SelectAll()`: 选择所有文本
- `void SelectText(int start=0, int end=0)`: 选择指定范围文本
- `void OnKeyFocus(int bact)`: 处理键盘焦点
- `bool IsValidChar(string &str)`: 判断字符是否有效
- `int DelSel()`: 删除选中内容
- `void FormatText()`: 格式化文本

### SysTree

树形控件，继承自SysShape和SysLinkChgStyle。

**配置属性**:
- `itemclass`: 树节点类名 (默认: "SysTreeItem")
- `shapecolor`: 形状颜色 (默认: rgb#ff222222)
- `indent`: 缩进值 (默认: 8)
- `expandlv`: 默认展开层级 (默认: 2)

**成员变量**:
- `string m_sItemClass`: 子节点类名
- `float m_fIndent`: 缩进值
- `int m_nDefExpandLv`: 默认展开层级
- `int m_nSelectMode`: 选择模式 (0x1:是否可以选中; 0x2:是否可多选; 0x4:是否只能选择叶节点)
- `int m_nShowRoot`: 是否显示根节点
- `int m_nDBClickExpand`: 双击是否展开节点
- `int m_nKeepOrder`: 是否保持添加顺序
- `int m_nShowMode`: 显示模式 (0x3:父节点叶节点都显示; 1:显示父节点; 2:显示子节点)
- `float m_fAniTime`: 动画时间
- `float m_fItemSize`: 项目尺寸
- `int m_nFlat`: 是否扁平化显示
- `int m_nEnableDrag`: 项目是否可拖拽
- `string m_sFilterStr`: 搜索过滤字符串

**方法**:
- `vec2 GetMapSize()`: 获取映射尺寸
- `void SetClassKind(int datkind, string classname)`: 设置类型对应的类名
- `void SetShowRoot(int b)`: 设置是否显示根节点
- `void SetKeepOrder(int b)`: 设置是否保持添加顺序
- `void SetDefExpandLv(int lv)`: 设置默认展开层级
- `void EnableDrag(int b)`: 启用或禁用拖拽
- `void SetFilterStr(string s)`: 设置过滤字符串
- `obj SetString(string path, var dat=nil, int datkind=0, string sortkey="")`: 设置项目
- `obj SetString_File(string filepath, string path="")`: 设置文件项目
- `obj SetString_Obj(obj p, string path="", int showasleaf=1)`: 设置对象项目
- `obj SetString_Input(string path, var value, var vformat=nil, var linkchg=nil, obj linkobj=NULL, var vfunex=nil, int linkmode=0, string sortkey="", int hidename=0)`: 设置输入项目

### SysTreeItem

树形控件节点，继承自SysText和SysStateBtnStyle。

**配置属性**:
- `shapecolor`: 未激活形状颜色 (默认: rgb#00383b42)
- `textcolor`: 未激活文本颜色 (默认: rgb#ffe8ebef)
- `accentcolor`: 激活形状颜色 (默认: rgb#ff618beb)
- `accenttextcolor`: 激活文本颜色 (默认: rgb#ffe8ebef)
- `cornerround`: 圆角半径 (默认: 5)
- `outrect`: 外部矩形偏移 (默认: vec4(3,3,-3,-3))
- `alignh`: 水平对齐方式 (默认: 1)
- `alignv`: 垂直对齐方式 (默认: 1)

**成员变量**:
- `obj m_pIcon`: 图标对象
- `float m_fLastItemSize`: 上次项目尺寸
- `ptrex:strtree m_pNode`: 节点指针
- `obj m_pExpand`: 展开按钮
- `int m_nbInit`: 是否已初始化
- `color m_nAccentColor`: 激活颜色
- `color m_nAccentTextColor`: 激活文本颜色
- `color m_nUnAccentColor`: 未激活颜色
- `color m_nUnAccentTextColor`: 未激活文本颜色

**方法**:
- `string GetName()`: 获取名称
- `var GetIcon()`: 获取图标
- `void CheckUnSelectItem(obj ptag)`: 检查未选中项
- `int CheckShow()`: 检查是否显示
- `obj MakeExpand()`: 创建展开按钮
- `void UpdateVal()`: 更新值
- `void UpdateState()`: 更新状态
- `void UpdateSub()`: 更新子节点
- `void UpdateItem(int flag=0, int no=-1)`: 更新项目
- `void UpdateSize()`: 更新尺寸
- `int Expand(int b=-1)`: 展开或折叠
- `void MakeVisable()`: 使节点可见
- `void OnValueChg()`: 处理值变化
- `void DelItem()`: 删除项目
- `void OnClick(var dn=nil)`: 处理点击
- `void OnDBClick(var dn=nil)`: 处理双击
- `void OnTouchPop(vec3 pt)`: 处理弹出触摸

### SysCombo

下拉框组件，继承自SysBtn和SysLinkIntStyle。

**成员变量**:
- `float m_fPopMaxHeight`: 弹出最大高度 (默认: 240)
- `int m_nValue`: 当前选中索引

**方法**:
- `void SetDef(var v, int index=0, var linkcall=nil, var linkobj=NULL)`: 设置默认属性
- `int GetIndex()`: 获取当前索引
- `int SetIndex(int index)`: 设置索引
- `void SetFormat(var data)`: 设置格式
- `var GetSelectData(var def=nil)`: 获取选中数据
- `var GetDataByIndex(int index, var def=nil)`: 根据索引获取数据
- `void OnValueChg()`: 处理值变化

### SysComboEx

扩展下拉框，继承自SysCombo，返回内容而非索引。

**方法**:
- `void SetDef(var v, var sel=0, var linkcall=nil, var linkobj=NULL)`: 设置默认属性
- `var GetValue()`: 获取值
- `int _SetValue(var value)`: 设置值

### SysComboStrID

字符串ID下拉框，继承自SysComboEx。

**方法**:
- `void SetFormat(var data)`: 设置格式
- `int _SetValue(var value)`: 设置值
- `var GetDataByIndex(int index, var def=nil)`: 根据索引获取数据

### SysProgress

进度条组件，继承自SysText和SysLinkChgStyle。

**配置属性**:
- `bkcolor`: 背景颜色 (默认: rgb#ff383b42)
- `textcolor`: 文本颜色 (默认: rgb#fff1f1f1)
- `accentcolor`: 重点颜色 (默认: rgb#ff618beb)
- `roundcorner`: 圆角半径 (默认: 5)
- `outrect`: 外部矩形偏移 (默认: vec4(3,3,-3,-3))
- `alignh`: 水平对齐方式 (默认: 1)
- `alignv`: 垂直对齐方式 (默认: 1)

**成员变量**:
- `float m_fValue`: 当前值
- `float m_fMin`: 最小值 (默认: 0)
- `float m_fMax`: 最大值 (默认: 1.0)
- `float m_nIsInt`: 是否为整数 (默认: -1)
- `int m_nCanOverMax`: 是否可超过最大值
- `color m_nAccentColor`: 重点颜色
- `color m_nBkColor`: 背景颜色
- `string m_sDefText`: 默认文本

**方法**:
- `void SetDef(var value, var linkcall=nil, obj linkobj=NULL, var vfunex=nil)`: 设置默认属性
- `void SetText(string s)`: 设置文本
- `void SetBkColor(int c)`: 设置背景颜色
- `void SetAccentColor(int c)`: 设置重点颜色
- `void SetMainColor(int bkcolor, int accentcolor)`: 设置主颜色
- `void SetMinMax(float fmin, float fmax)`: 设置最小最大值
- `void SetCanOverMax(int b)`: 设置是否可超过最大值
- `void SetValueAndMax(var value, float fmax)`: 设置值和最大值
- `void SetValueToMax()`: 设置值为最大值
- `float GetPercent()`: 获取百分比
- `var GetValue()`: 获取值
- `int _SetValue(var value)`: 设置值
- `void UpdateText()`: 更新文本
- `void OnValueChg()`: 处理值变化
- `void OnSizeChged()`: 处理尺寸变化

### SysSlider

滑块组件，继承自SysProgress。

**配置属性**:
- `textcolor`: 文本颜色 (默认: rgb#ff1e1e1e)
- `outrect`: 外部矩形偏移 (默认: vec4(0,24,0,0))

**方法**:
- `void OnTouch(var &dn)`: 处理触摸事件
- `void OnValueChg()`: 处理值变化

## 样式系统 (style)

### SysBtnStyle

按钮样式，继承自SysLinkVarStyle。

**成员变量**:
- `m_nCanTouch`: 可触摸标志 (默认: TOUCHFLAG_NORMAL|TOUCHFLAG_KEYFOCUS)

**静态方法**:
- `static void BaseTouchEffect(var &dn, obj plink, int cdown=0, int cin=0, int useragvid=id#touchagv_btn)`: 基础触摸效果

**方法**:
- `void OnTouchSound(var &dn)`: 触摸音效
- `void OnTouchEffect(var &dn)`: 触摸效果
- `void OnTouch(var &dn)`: 处理触摸事件
- `void OnTouchMove(var &dn)`: 处理移动事件
- `virtual int GetClickMode()`: 获取点击模式
- `virtual void OnDBClick(var dn=nil)`: 双击处理
- `virtual void OnClick(var dn=nil)`: 点击处理

### SysAlign

UI自动对齐样式。

**成员变量**:
- `id#anchor/id#mask`: 对齐掩码 (每位依次对应是否响应 x,y,w,h)
- `id#anchor/id#percent`: 对齐百分比
- `id#anchor/id#margin`: 对齐边距
- `id#anchor/id#ignorepivot`: 是否忽略自身轴心点

**方法**:
- `vec4 GetAnchorRect()`: 获取锚点矩形
- `int IsAnchor()`: 判断是否有锚点
- `void ClearAnchor()`: 清除锚点
- `void SetAnchor_IgnoreSelfRect(int b)`: 设置是否忽略自身矩形
- `void SetAnchor_Copy(obj p)`: 复制锚点
- `void SetAnchor(vec4 v, var margin=nil, int mask=0x1F, int update=1)`: 设置锚点
- `void UpdateAnchorMargin()`: 更新锚点边距

**快捷接口**:
- `void SetAnchor_Align(int ha=0, int va=0, var offset=nil, int usecursize=0, int mask=0x13, int update=1)`: 设置对齐锚点
- `void SetAnchor_Fill(var margin=nil, int dir=-1, var offset=nil, int usecursize=0, int mask=0x1F, int update=1)`: 设置填充锚点
- `void SetAnchor_CalFit()`: 计算适合的锚点
- `void SetAnchor_FitRect(int clearmargin=1)`: 适应矩形
- `void SetAnchor_Center(var offset=nil, int usecursize=0)`: 设置居中锚点
- `void SetAnchor_Left(var offset=nil, int usecursize=0)`: 设置左对齐锚点
- `void SetAnchor_Top(var offset=nil, int usecursize=0)`: 设置顶部对齐锚点
- `void SetAnchor_Right(var offset=nil, int usecursize=0)`: 设置右对齐锚点
- `void SetAnchor_Bottom(var offset=nil, int usecursize=0)`: 设置底部对齐锚点
- `void SetAnchor_LeftTop(var offset=nil, int usecursize=0)`: 设置左上对齐锚点
- `void SetAnchor_RightTop(var offset=nil, int usecursize=0)`: 设置右上对齐锚点
- `void SetAnchor_LeftBottom(var offset=nil, int usecursize=0)`: 设置左下对齐锚点
- `void SetAnchor_RightBottom(var offset=nil, int usecursize=0)`: 设置右下对齐锚点
- `void SetAnchor_FillLeft(var margin=nil, var offset=nil, int usecursize=0)`: 设置左填充锚点
- `void SetAnchor_FillTop(var margin=nil, var offset=nil, int usecursize=0)`: 设置顶部填充锚点
- `void SetAnchor_FillRight(var margin=nil, var offset=nil, int usecursize=0)`: 设置右填充锚点
- `void SetAnchor_FillBottom(var margin=nil, var offset=nil, int usecursize=0)`: 设置底部填充锚点
- `void SetAnchor_FillCenterW(var margin=nil, var offset=nil, int usecursize=0)`: 设置居中并横向充满锚点
- `void SetAnchor_FillCenterH(var margin=nil, var offset=nil, int usecursize=0)`: 设置居中并竖向充满锚点
- `void SetAnchor_FillW(float perw=1.0, float offsetw=0)`: 设置填充宽度
- `void SetAnchor_FillH(float perw=1.0, float offsetw=0)`: 设置填充高度

### SysCon

容器样式。

**静态方法**:
- `static void NoPlace()`: 设置无位置标志
- `static void CR()`: 设置换行标志
- `static obj Line(float h=2, int c=0, float w=0)`: 创建线条
- `static obj LineCR(float h=2, int c=0, float w=0)`: 创建带换行的线条
- `static obj Placeholder(float w=0, float h=0, int cr=0)`: 创建占位符
- `static obj Class(string classname)`: 创建指定类名的对象
- `static obj Obj(obj p)`: 添加对象到容器
- `static obj Int(int value, var linkcall=nil, obj linkobj=NULL)`: 创建整数输入框
- `static obj Float(float value, var linkcall=nil, obj linkobj=NULL, var minmax=nil)`: 创建浮点数输入框
- `static obj String(string value, var linkcall=nil, obj linkobj=NULL)`: 创建字符串输入框
- `static obj Vec(var value, var linkcall=nil, obj linkobj=NULL)`: 创建向量输入框
- `static obj Var(var value, var linkcall=nil, obj linkobj=NULL)`: 创建变量输入框
- `static obj Text(string s, int c=0)`: 创建文本
- `static obj LineText(string s, int c=0)`: 创建行文本
- `static obj Edit(string s, var linkcall=nil, obj linkobj=NULL)`: 创建编辑框
- `static obj LineEdit(string s, var linkcall=nil, obj linkobj=NULL)`: 创建行编辑框
- `static obj EditPass(string s="", var linkcall=nil, obj linkobj=NULL)`: 创建密码编辑框
- `static obj LineEditPass(string s="", var linkcall=nil, obj linkobj=NULL)`: 创建行密码编辑框
- `static obj SearchEdit(string s="", var linkcall=nil, obj linkobj=NULL)`: 创建搜索编辑框
- `static obj Progress(var value, float fmin=0, float fmax=1.0)`: 创建进度条
- `static obj Slider(var value, float fmin=0, float fmax=1.0, var linkcall=nil, obj linkobj=NULL)`: 创建滑块
- `static obj Btn(string s, var fun=nil, obj linkobj=NULL, var c=nil, float w=100, float h=24)`: 创建按钮
- `static obj LineBtn(string s, var fun=nil, obj linkobj=NULL, var c=nil)`: 创建行按钮
- `static obj TextBtn(string s, var fun=nil, obj linkobj=NULL, int c=0x00111111)`: 创建文本按钮
- `static obj LineTextBtn(string s, var fun=nil, obj linkobj=NULL, int c=0x00111111)`: 创建行文本按钮
- `static obj ImgBtn(var res, var fun=nil, obj linkobj=NULL, int c=0, float w=32, float h=32)`: 创建图片按钮
- `static obj State(string s, int b=0, var linkcall=nil, obj linkobj=NULL)`: 创建状态按钮
- `static obj ImgState(string s, int b=0, var linkcall=nil, obj linkobj=NULL)`: 创建图片状态按钮
- `static obj Radio(string s, int b=0, var linkcall=nil, obj linkobj=NULL)`: 创建单选按钮
- `static obj Check(string s, int b=0, var linkcall=nil, obj linkobj=NULL)`: 创建复选按钮
- `static obj Toggle(string s, int b=0, var linkcall=nil, obj linkobj=NULL)`: 创建开关按钮
- `static obj Color(var c, var linkcall=nil, obj linkobj=NULL)`: 创建颜色选择器
- `static obj Combo(var data, int index=0, var linkcall=nil, obj linkobj=NULL)`: 创建下拉框
- `static obj Tab(var sztab, int index=0, var linkcall=nil, obj linkobj=NULL)`: 创建标签页
- `static obj Shape(float w=64, float h=64, float c=0xffffffff, float cl=0, float r=0)`: 创建形状
- `static obj Img(var vres, float w=64, float h=64, float c=0xffffffff)`: 创建图片
- `static obj Copy(obj p)`: 创建对象拷贝

### SysConKey

用于管理具有键名的容器对象的样式。

**静态方法**:
- `static obj Get(int namekey)`: 通过键获取对象
- `static void Del(int namekey)`: 删除键对应的对象
- `static obj Class(int namekey, string classname)`: 获取或创建指定类名的对象
- `static obj Int(int namekey, int value, var linkcall=nil, obj linkobj=NULL)`: 获取或创建整数输入框
- `static obj Float(int namekey, float value, var linkcall=nil, obj linkobj=NULL, var minmax=nil)`: 获取或创建浮点数输入框
- `static obj String(int namekey, string value, var linkcall=nil, obj linkobj=NULL)`: 获取或创建字符串输入框

## 高级组件 (adv)

### SysDocker

停靠容器，用于创建可停靠的面板。

**方法**:
- `void SetDef()`: 设置默认属性
- `void OnDockMove(var &dn)`: 处理停靠移动
- `void OnDockResize(var &dn)`: 处理停靠调整大小

### SysTreeDocker

树形停靠容器，继承自SysDocker。

**方法**:
- `void SetDef()`: 设置默认属性
- `void AddTreeItem(obj item)`: 添加树节点
- `void RemoveTreeItem(obj item)`: 移除树节点

### SysLoading

加载进度显示组件。

**成员变量**:
- `m_nProgress`: 进度值 (0-100)
- `m_sText`: 显示文本

**方法**:
- `void SetProgress(int value)`: 设置进度值
- `void SetText(string text)`: 设置显示文本

## 数据结构

### SysParamNotesSt

参数注释结构体。

**成员**:
- `string name`: 名称
- `var value`: 值
- `var format`: 格式
- `string showname`: 显示名称
- `string mem`: 备注

## 常用路径

- `PATH_SYS_RES`: 系统资源路径，默认为 "res/" 