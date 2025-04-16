#  GBox API 文档
##  class
类是 Gbox 中的基本构建块，用于创建具有属性和方法的对象模板。类定义了对象的结构和行为，支持继承机制以实现代码复用。通过类，你可以封装数据和功能，从而创建可以服用的对象
  -  [GObj](#GObj)  -  基础类
  -  [GObjSandBox](#GObjSandBox)  -  基础沙盒对象类，提供沙盒环境的创建、表达式编译和参数获取功能
  -  [GObjVDisk](#GObjVDisk)  -  虚拟磁盘文件系统类，用于管理和访问虚拟文件空间
  -  [GObjZipFile](#GObjZipFile)  -  ZIP压缩文件处理类，提供ZIP文件的创建、读取和提取功能
  -  [GObjLZ4File](#GObjLZ4File)  -  LZ4高性能压缩文件处理类，用于打包和压缩多个文件
  -  [GSocket](#GSocket)  -  网络通信Socket类，管理TCP/IP连接和数据传输
  -  [GSocketC](#GSocketC)  -  客户端套接字类，用于建立与服务器的TCP连接和通信
  -  [GSocketS](#GSocketS)  -  套接字服务器窗口类，用于管理套接字服务器连接和事件处理，支持多客户端连接和数据传输
  -  [GSocketSBase](#GSocketSBase)  -  Socket服务器基类，负责监听和管理客户端连接
  -  [GVNetObj](#GVNetObj)  -  虚拟网络对象类，用于管理多客户端连接和通信
  -  [GSocketUdp](#GSocketUdp)  -  UDP套接字类，用于实现UDP通信和命令传输
  -  [GNetFileObj](#GNetFileObj)  -  网络文件对象类，提供文件传输与下载功能
  -  [GMIDFileObj](#GMIDFileObj)  -  中间存储键值对的文件对象类，用于在文件中持久化存储变量数据
  -  [GObjShow](#GObjShow)  -  2D显示对象基类，用于在2D场景中显示和管理可视对象
  -  [GObj2DWnd](#GObj2DWnd)  -  2D窗口对象类，提供操作系统窗口的创建和管理功能，支持窗口显示、交互和渲染等操作
  -  [GBoxShowApp](#GBoxShowApp)  -  应用程序显示框架类，用于管理应用窗口、输入事件和资源沙盒
  -  [GSandApp2DWnd](#GSandApp2DWnd)  -  2D沙盒应用窗口类，用于作为沙盒环境的显示根节点并处理窗口相关事件
  -  [GObj2DSandBox](#GObj2DSandBox)  -  2D沙盒环境类，用于创建和管理2D场景中的脚本执行环境，提供资源控制、对象创建和触控管理功能
  -  [GResManager](#GResManager)  -  这个类实现了资源管理器，负责资源的加载、缓存和管理，支持本地与网络资源，并维护资源引用关系与状态
  -  [GObjText](#GObjText)  -  2D文本对象类，提供文本渲染和属性控制功能，支持字体设置、对齐方式、颜色控制和下划线等文本显示效果
  -  [GObjShape](#GObjShape)  -  常用的2D形状
  -  [GObjView](#GObjView)  -  2D视图对象类，提供可滚动和缩放的视图功能，支持地图和视图坐标系转换、视图变换通知、滚动条显示和弹性拖拽等功能
  -  [GObjEdit](#GObjEdit)  -  编辑框对象类，继承自GObjShow，用于处理单行文本的编辑、显示和交互功能
  -  [GObjDoc](#GObjDoc)  -  文档对象类，用于处理文档的显示、编辑、样式和布局等功能
  -  [GObjAni](#GObjAni)  -  2D动画对象类，提供帧动画的加载、播放和控制功能，支持多种动画类型、缩放、旋转和轨迹显示，用于创建和管理交互式动画效果
  -  [GObjUndo](#GObjUndo)  -  撤销和重做操作管理类，用于记录和执行对象状态的撤销和重做功能
  -  [GObjTxt](#GObjTxt)  -  多行文本输出控件，支持日志记录、错误输出和调试信息显示，具有自动滚动、图标与颜色设置等功能
  -  [GObjSyntaxEdit](#GObjSyntaxEdit)  -  代码编辑文本框，提供语法高亮、代码折叠、智能缩进与自动补全，支持多种编程语言和自定义配色
  -  [GObjSheet](#GObjSheet)  -  表格控件类，提供灵活的行列数据管理和显示，支持单元格编辑、样式设置和多种类型数据展示
  -  [GObjSheetItem](#GObjSheetItem)  -  表格单元格类，实现表格中单个数据项的显示与交互，支持多种数据类型和显示样式
  -  [GObjLook](#GObjLook)  -  观察框对象类，提供对其他显示对象的观察和代理显示功能，支持坐标变换、触摸事件转发和独立显示标志设置
  -  [GObjSndStream](#GObjSndStream)  -  音频流处理类，提供音频录制和播放功能，支持网络音频数据传输
  -  [GWaveFFTShow](#GWaveFFTShow)  -  这个类实现了音频FFT频谱显示控件，用于对音频数据进行傅里叶变换分析并以可视化方式呈现频谱，支持实时波形分析和频带显示
  -  [GObjSndView](#GObjSndView)  -  这个类实现了音频可视化视图控件，用于显示和播放音频波形，支持音频文件加载、波形渲染、音量控制和选区播放
  -  [GObjCamera](#GObjCamera)  -  3D相机类，用于控制3D场景的视角和渲染
  -  [GObj3DShow](#GObj3DShow)  -  3D对象显示基类，提供3D显示、世界坐标变换和渲染管理功能
  -  [GObj3DWorld](#GObj3DWorld)  -  3D世界对象，管理场景中的3D对象、碰撞检测和光照效果
  -  [GObj3DLight](#GObj3DLight)  -  3D光照对象，用于管理场景中的光源效果
  -  [GObj3DSkyBox](#GObj3DSkyBox)  -  天空盒对象，用于渲染3D场景的背景天空
  -  [GObj3DShadowSSM](#GObj3DShadowSSM)  -  阴影贴图渲染类，使用分割空间映射(SSM)技术实现3D场景动态阴影效果
  -  [GObj3DWater](#GObj3DWater)  -  3D水体对象，用于渲染水面效果及其反射、折射
  -  [GObj3DGuid](#GObj3DGuid)  -  3D网格导航类，用于创建和管理3D场景中的网格导航系统
  -  [GObj3DCamera](#GObj3DCamera)  -  3D相机视锥体类，用于可视化和控制3D相机视锥体
  -  [GObj3DBlkMaker](#GObj3DBlkMaker)  -  3D区块生成器对象，用于创建和显示网格区块
  -  [GObj3DAni](#GObj3DAni)  -  3D动画对象，用于管理和播放3D模型动画
  -  [GObj3DCharacter](#GObj3DCharacter)  -  3D角色对象，提供角色动作控制、路径行走和跳跃功能
  -  [GObj3DAniMove](#GObj3DAniMove)  -  3D动画移动对象，提供角色移动、路径跟随和碰撞检测功能
  -  [GObj3DHit](#GObj3DHit)  -  3D碰撞检测类，用于管理3D场景中的对象碰撞检测和事件触发
  -  [GObj3DShape](#GObj3DShape)  -  3D基础形状对象类，用于在3D场景中创建和显示基本几何体
  -  [GObj3DLine](#GObj3DLine)  -  3D线条绘制类，用于在3D场景中创建和显示线条、坐标轴和文本标注
  -  [GObjMeshLod](#GObjMeshLod)  -  3D网格LOD优化类，用于自动简化网格模型并支持不同细节层次的显示
  -  [GMcWorldObj](#GMcWorldObj)  -  MC世界对象，管理体素世界的创建、加载和编辑
  -  [GObj3DPixelMc](#GObj3DPixelMc)  -  3D像素MC对象，用于渲染和管理体素世界的显示
  -  [GMcTreeMaker](#GMcTreeMaker)  -  MC树结构生成器，用于创建和管理体素树结构
  -  [GSandAppWnd](#GSandAppWnd)  -  沙盒应用窗口类，用于创建和管理沙盒环境中的应用窗口
  -  [GObj3DSandBox](#GObj3DSandBox)  -  3D沙盒环境类，用于创建和管理3D场景中的脚本执行环境
  -  [GObj3DDepMap](#GObj3DDepMap)  -  深度图渲染类，用于生成和管理3D场景深度图以实现遮挡剔除
  -  [GObj3DParticle](#GObj3DParticle)  -  3D粒子系统类，用于创建和管理3D场景中的粒子特效
  -  [GWebFile](#GWebFile)  -  HTTP文件下载类，提供多线程分块下载、断点续传和进度通知功能
  -  [GSandBoxWinApp](#GSandBoxWinApp)  -  
  -  [GWebLink](#GWebLink)  -  网络链接类，提供HTTP/HTTPS网页访问、数据传输和请求功能
##  eve
标准库,脚本可以直接调用库里的函数,无需写作用域.主要提供系统控制、任务管理和高级数学计算功能
  -  [:task](#:task)  -  任务控制接口类，提供脚本任务调度和管理功能
  -  [:math](#:math)  -  数学函数库类，提供各种随机数生成和3D数学计算功能
##  fixcall
标准库,脚本可以直接调用库里的函数,无需写作用域.主要提供基础数学运算、颜色处理和基础数据处理等功能
  -  [:fixcal](#:fixcal)  -  基础数学计算和格式化函数库，提供数值运算、颜色处理和字符串格式化功能
##  namespace
命名空间,脚本可以通过 命名空间::函数名 的格式来调用库中的函数
  -  [file](#file)  -  文件系统接口类，提供文件操作的核心功能
  -  [sys](#sys)  -  系统接口类，提供系统级操作、公共数据存储和设备信息访问功能
  -  [csvr](#csvr)  -  网络客户端服务器通信任务类，提供RPC功能和分布式通信
  -  [netapi](#netapi)  -  网络API接口类，提供服务器查找和远程函数调用功能
  -  [syshelp](#syshelp)  -  系统帮助类，提供类信息查询、脚本反射和配置管理功能
  -  [font](#font)  -  字体任务作用域，提供字体管理功能，包括清除所有字体缓存、注册FreeType字体和图像字体
  -  [showcmd](#showcmd)  -  显示命令处理类，用于创建和管理渲染指令
  -  [touch](#touch)  -  触摸事件管理任务类，处理触摸和鼠标事件
  -  [keyboard](#keyboard)  -  键盘事件管理任务类，处理键盘输入和焦点控制
  -  [res](#res)  -  资源作用域类，提供沙盒环境中的资源管理功能，支持资源ID获取、创建、数据读取和文件访问等操作
  -  [ease](#ease)  -  这个类实现了缓动动画效果控制，用于创建和管理对象属性的平滑过渡动画，支持多种缓动模式
  -  [showpath](#showpath)  -  显示路径处理类，用于生成和转换UI元素显示路径的坐标系统
  -  [snd](#snd)  -  音频任务作用域，提供沙盒环境中音频播放和控制的接口，支持音频资源播放、停止等操作
  -  [web](#web)  -  
  -  [locapi](#locapi)  -  本地API接口类，提供服务注册、查询和消息发送功能
##  ptrex
ptrex 是特殊的对象引用类型，用于安全地引用和操作游戏中的复杂对象（如模型、材质、粒子系统等）。它提供了引用计数机制和类型安全检查，确保对象正确管理。通过 ptrex，脚本可以创建、操作和共享游戏引擎中的核心对象
  -  [csvr::addr](#csvr::addr)  -  网络地址对象类，用于建立和管理远程服务器连接
  -  [rsa::publickey](#rsa::publickey)  -  这个类实现了RSA公钥解密功能，负责使用公钥解密由对应私钥加密的数据，支持标准RSA非对称加密
  -  [rsa::privateKey](#rsa::privateKey)  -  这个类实现了RSA私钥加密功能，负责生成密钥对并使用私钥加密数据，支持1024位RSA加密标准
  -  [file::ptr](#file::ptr)  -  文件指针操作类，提供底层文件读写功能
  -  [strtree](#strtree)  -  字符串树结构类，提供层次化的数据存储和访问功能
  -  [con2d::std](#con2d::std)  -  标准二维布局控制器类，用于管理对象的位置和大小
  -  [con2d:base](#con2d:base)  -  界面布局容器基类，负责管理UI组件的位置和边框布局
  -  [con2d::tab](#con2d::tab)  -  表格式二维布局控制器类，用于管理按列排列的对象布局
  -  [ani2d](#ani2d)  -  2D动画资源指针类，用于管理和操作2D动画资源
  -  [resdatptr](#resdatptr)  -  
  -  [img](#img)  -  图像资源类，用于管理和操作图像数据
  -  [sndbuf](#sndbuf)  -  音频缓冲区类，负责加载、保存和播放音频资源，提供音频数据的基本操作和播放控制功能
  -  [font::text](#font::text)  -  文本渲染类，用于管理字体、文本内容和绘制属性
  -  [draw::cmdsz](#draw::cmdsz)  -  绘图命令集合类，用于管理和执行渲染命令
  -  [material](#material)  -  材质管理类，用于定义和处理3D模型的PBR材质属性和贴图
  -  [ani3d](#ani3d)  -  3D动画资源指针类，用于管理和操作3D模型、动画、材质和节点数据
  -  [particle](#particle)  -  粒子定义类，用于管理粒子系统的整体配置和组成
  -  [atom::Atom](#atom::Atom)  -  粒子,基本粒子
  -  [.atombase](#.atombase)  -  粒子原子基类，粒子系统的基本构建单元
  -  [atom::Emitter](#atom::Emitter)  -  点发生器
  -  [.atomctrl](#.atomctrl)  -  粒子控制基类，用于控制粒子的运动、生成和特性
  -  [atom::ELine](#atom::ELine)  -  线形发生器
  -  [atom::ECircle](#atom::ECircle)  -  圆形发生器
  -  [atom::EBox](#atom::EBox)  -  盒形发生器
  -  [atom::ESphere](#atom::ESphere)  -  球形发生器
  -  [atom::Fire](#atom::Fire)  -  目标飞行,粒子控制器
  -  [atom::Roto](#atom::Roto)  -  旋转,粒子控制器
  -  [atom::Jet](#atom::Jet)  -  加速,粒子控制器
  -  [atom::Gravity](#atom::Gravity)  -  重力,粒子控制器
  -  [atom::Vortex](#atom::Vortex)  -  漩涡
  -  [atom::GWell](#atom::GWell)  -  引力点
  -  [atom::Snd](#atom::Snd)  -  声音,控制器
  -  [atom::Track](#atom::Track)  -  追踪
  -  [atom::ActRibbon](#atom::ActRibbon)  -  动作条带,基本粒子
  -  [atom::Ribbon](#atom::Ribbon)  -  粒子条带,基本粒子
  -  [atom::R_BindObj](#atom::R_BindObj)  -  条带控制器
  -  [atom::R_Twist](#atom::R_Twist)  -  条带缠绕控制器
  -  [atom::Snow](#atom::Snow)  -  粒子雪花系统类，用于创建和管理雪花粒子特效
##  varkind
varkind 定义了 Gbox 脚本中的变量类型系统。Gbox 支持多种变量类型，包括基本类型（int,float,bool,string）和复杂类型（var、obj、ptrex）。变量类型系统确保脚本中的数据操作安全有效，并提供了类型转换和检查功能
  -  [all kind](#all kind)  -  
  -  [string](#string)  -  字符串变量类，提供字符串操作和转换功能
  -  [var](#var)  -  集合变量类，提供命名值管理和JSON序列化功能
  -  [vec2](#vec2)  -  二维向量变量类，提供二维坐标和向量操作
  -  [vec3](#vec3)  -  三维向量变量类，提供三维坐标和向量操作
  -  [vec4](#vec4)  -  四维向量变量类，提供四元数旋转和矩形操作功能
  -  [ptr64](#ptr64)  -  64位指针变量类，用于远程对象和系统对象的引用管理
  -  [script](#script)  -  用于封装、编译和执行脚本代码的变量类型，提供表达式解析和动态执行功能
  -  [bin](#bin)  -  二进制数据变量类，用于存储和操作二进制数据
  -  [ptrex](#ptrex)  -  扩展指针变量类，提供对对象指针的引用计数和类型检查功能
  -  [mat3](#mat3)  -  矩阵3变量类，提供3x3矩阵运算和矩阵变换功能
  -  [mat4](#mat4)  -  4x4矩阵变量类，提供矩阵变换和3D空间操作功能

<!-- 目录结束了 -->
----
### GObj
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)
**描述**:基础类
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `obj GetWndObj()`  |  获取对象所在的窗口对象  |
|  `var IsClassCanNotes()`  |  检查类是否可以添加注释  |
|  `var GetClassNotes(strid secid=0)`  |  获取类的注释信息，参数：secid-注释段落ID  |
|  `void SetClassNotes(strid secid,var agv)`  |  设置类的注释信息，参数：secid-注释段落ID，agv-注释内容  |
|  `var GetClassNotesEx(strid secid=0)`  |  获取类的扩展注释信息，参数：secid-注释段落ID  |
|  `string GetClassName()`  |  获取类名  |
|  `int GetClassNameID()const`  |  获取类名对应的ID  |
|  `bool IsBaseClass(strid baseid,int bincludescript=0)`  |  检查是否继承自指定的基类，参数：baseid-基类ID，bincludescript-是否包含脚本类  |
|  `int GetTraceIconNo()`  |  获取用于调试显示的图标编号  |
|  `void DelThis()`  |  删除自己()  |
|  `bool SafeDelObj(obj p)`  |  安全删除指定对象，返回是否成功删除，参数：p-目标对象  |
|  `bool UseStyle(var styledef)`  |  使用指定样式定义，参数：styledef-样式定义  |
|  `bool IsStyle(strid styleid)`  |  检查是否使用了指定样式，参数：styleid-样式ID  |
|  `bool RunScriptFile(string pfilename)`  |  运行脚本文件，参数：pfilename-脚本文件名  |
|  `bool IsCanCreateClass(strid classid)`  |  检查是否可以创建指定类，参数：classid-类ID  |
|  `obj NewObj(var classdef,obj ppFather)`  |  创建新对象，参数：classdef-类定义，ppFather-父对象  |
|  `int IsHaveSubObj()const`  |  是否具有子对象  |
|  `int GetSubObjNum()const`  |  取子对象数目  |
|  `int GetAllSubObjNum()const`  |  取所有子对象总数  |
|  `void DeleteAllSub()`  |  删除所有子对象  |
|  `bool SetObjFather(obj p)`  |  设置对象的父对象，参数：p-新的父对象，返回是否成功  |
|  `bool IsSubObj(obj p)`  |  检查指定对象是否为当前对象的子对象，参数：p-要检查的对象  |
|  `void BringToTop()`  |  移动对象次序到顶  |
|  `void BringToBottom()`  |  移动对象次序到低  |
|  `int EventToAllSub(var pevename,var pcallagv=NULL,int btree=0)`  |  向所有子对象发送事件调用，参数：pevename-事件名，pcallagv-调用参数，btree-是否递归子树  |
|  `int GetAllSubObj(var& pret,int maxsublevel=0)`  |  获取所有子对象列表，参数：pret-返回结果，maxsublevel-最大子层级  |
|  `int GetAllSubObjEx(var& pret,var funname,var paramname,int maxsublevel=0)`  |  根据条件获取子对象列表，参数：pret-返回结果，funname-条件函数，paramname-参数名，maxsublevel-最大子层级  |
|  `var GetAllSubSz(var condition=NULL)`  |  获取所有子对象的数组，参数：condition-筛选条件  |
|  `bool NotiParamChged(strid nameid,var pval)`  |  通知参数变更，参数：nameid-参数名ID，pval-新值  |
|  `int IsParam(strid nameid,int paramkind=3)`  |  检查参数是否存在，参数：nameid-参数名ID，paramkind-参数类型(3表示所有类型)  |
|  `bool GetParam(strid nameid,var& val)`  |  获取参数值，参数：nameid-参数名ID，val-用于存储结果  |
|  `bool SetParam(strid nameid,var val,int bnoti=1)`  |  设置参数值，参数：nameid-参数名ID，val-新值，bnoti-是否发送通知  |
|  `bool FindFatherParam(strid paramid,var& val)`  |  查找父对象参数，参数：paramid-参数ID，val-用于存储结果  |
|  `bool AddParamNoti(strid paramid,obj pobj,strid funid,int bnotiimm=1)`  |  添加参数变更通知，参数：paramid-参数ID，pobj-接收通知的对象，funid-回调函数ID，bnotiimm-是否立即通知  |
|  `bool DelParamNoti(strid paramid,obj pobj,strid funid)`  |  删除参数变更通知，参数：paramid-参数ID，pobj-接收通知的对象，funid-回调函数ID  |
|  `int IsFunction(strid funid,int funkind=3)`  |  检查函数是否存在，参数：funid-函数ID，funkind-函数类型(3表示所有类型)  |
|  `bool CallByName(strid funid,var& pcallagv=NULL)`  |  通过名称调用函数，参数：funid-函数ID，pcallagv-调用参数  |
|  `bool CallByNameWithRet(strid funid,var& pcallagv)`  |  通过名称调用函数并获取返回值，参数：funid-函数ID，pcallagv-调用参数和返回值  |
|  `bool CallBack(var fun,var pagv=NULL,int bAsyncRun=0)`  |  回调函数，参数：fun-函数，pagv-调用参数，bAsyncRun-是否异步执行  |
|  `bool SetTimer(float delaysec,strid evenameid,var pagv=NULL,int times=0)`  |  设置定时器，参数：delaysec-延迟秒数，evenameid-事件名ID，pagv-事件参数，times-重复次数(0为无限)  |
|  `void KillTimer(strid evenameid=0)`  |  删除定时器，参数：evenameid-事件名ID(0表示删除所有)  |
|  `bool IsTimer(strid evenameid)`  |  检查定时器是否存在，参数：evenameid-事件名ID  |
|  `bool AddNoti(strid eveid,obj pobj,strid callfunid)`  |  添加事件通知，参数：eveid-事件ID，pobj-接收通知的对象，callfunid-回调函数ID  |
|  `bool DelNoti(strid eveid,obj pobj,strid callfunid=0)`  |  删除事件通知，参数：eveid-事件ID，pobj-接收通知的对象，callfunid-回调函数ID  |
|  `bool IsNoti(strid eveid)const`  |  检查事件通知是否存在，参数：eveid-事件ID  |
|  `int Emit(strid eveid,var pcallagv=NULL)`  |  触发事件，参数：eveid-事件ID，pcallagv-事件参数  |
|  `int AsyncEmit(strid eveid)`  |  异步触发事件，参数：eveid-事件ID  |
|  `int GetEmitObjSz(var paramnamesz,var& pret)`  |  获取可触发事件的对象列表，参数：paramnamesz-参数名数组，pret-返回结果  |
|  `int  EmitPackAll()`  |  清除所有无效监听  |
|  `bool IsCondition(var conditionsz)`  |  检查条件是否满足，参数：conditionsz-条件数组  |
|  `void SetUserAgv(strid secid,strid keyid,var val)`  |  设置用户自定义参数，参数：secid-段落ID，keyid-键ID，val-值  |
|  `GVar GetUserAgv(strid secid,strid keyid,var pdef=NULL)`  |  获取用户自定义参数，参数：secid-段落ID，keyid-键ID，pdef-默认值  |
|  `bool IsUserAgv(strid secid,strid keyid)`  |  检查用户自定义参数是否存在，参数：secid-段落ID，keyid-键ID  |
|  `bool DelUserAgv(strid secid,strid keyid)`  |  删除用户自定义参数，参数：secid-段落ID，keyid-键ID  |
|  `bool CallUserAgv(strid secid,strid keyid,var pagv=NULL,int bAsyncRun=0)`  |  调用用户自定义参数函数，参数：secid-段落ID，keyid-键ID，pagv-调用参数，bAsyncRun-是否异步执行  |
|  `bool SetTraceObj(obj p)`  |  设置跟踪对象，参数：p-跟踪对象  |
----
### GObjSandBox
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjSandBox](#GObjSandBox)
**描述**:基础沙盒对象类，提供沙盒环境的创建、表达式编译和参数获取功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void CreateSandBox()`  |  创建沙盒环境  |
|  `void Close()`  |  关闭并清理沙盒环境  |
|  `bool CompileExp(string pext)`  |  编译表达式，参数：pext-表达式文本，返回：编译是否成功  |
----
### GObjVDisk
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjVDisk](#GObjVDisk)
**描述**:虚拟磁盘文件系统类，用于管理和访问虚拟文件空间
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool OpenVDisk(string pfilename,string mappath,int breadonly=0,int badd=1)`  |  打开虚拟磁盘文件，参数：pfilename-文件名，mappath-映射路径，breadonly-是否只读，badd-是否追加  |
|  `void Close()`  |  关闭虚拟磁盘  |
|  `var ListDirEx(string listpath,int binfo=0)`  |  列出指定目录下的所有文件，参数：listpath-目录路径，binfo-是否包含详细信息  |
|  `bool PreWritePath(string path)`  |  预创建文件路径，参数：path-文件路径  |
|  `bool RemoveDir(string path)`  |  删除指定目录，参数：path-目录路径  |
|  `bool IfHaveFile(string fname, int date=0, int len=0)`  |  检查文件是否存在，参数：fname-文件名，date-日期(0忽略)，len-长度(0忽略)  |
|  `var GetFile(string fname)`  |  获取文件信息，参数：fname-文件名，返回：文件大小和日期  |
|  `bool LoadFileBin(var& pretbin,string pfilename)`  |  加载二进制文件内容，参数：pretbin-存储数据的变量，pfilename-文件名  |
|  `bool SaveFileBin(var& pwbin,string pfilename,int filetime=0)`  |  保存二进制数据到文件，参数：pwbin-数据变量，pfilename-文件名，filetime-文件时间  |
|  `bool SetFileTime(string pfilename,int filetime)`  |  设置文件时间，参数：pfilename-文件名，filetime-文件时间  |
|  `bool DeleteFile(string pfilename)`  |  删除文件，参数：pfilename-文件名  |
|  `bool LoadFileBinRange(var& pretbin,string pfilename,var startpos,int len)`  |  从指定位置加载二进制文件内容，参数：pretbin-存储数据的变量，pfilename-文件名，startpos-起始位置，len-长度  |
|  `bool SaveFileBinRange(var& pwbin,string pfilename,var startpos)`  |  从指定位置写入二进制数据，参数：pwbin-数据变量，pfilename-文件名，startpos-起始位置  |
----
### GObjZipFile
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjZipFile](#GObjZipFile)
**描述**:ZIP压缩文件处理类，提供ZIP文件的创建、读取和提取功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void BeginZip()`  |  开始创建ZIP文件  |
|  `bool AddFile(string filename,string destname=NULL)`  |  添加文件到ZIP，参数：filename-源文件路径，destname-目标路径(为空则使用源文件名)  |
|  `bool EndZip(string pfilename,string pass=NULL)`  |  完成ZIP文件创建，参数：pfilename-ZIP文件路径，pass-密码(可选)  |
|  `int OpenZip(string pfilename,string pass=NULL)`  |  打开ZIP文件，参数：pfilename-ZIP文件路径，pass-密码(可选)，返回：文件数量  |
|  `var GetZipInfo(int pos)`  |  获取ZIP文件信息，参数：pos-文件索引，返回：文件信息(名称、大小、时间等)  |
|  `void Close()`  |  关闭ZIP文件  |
|  `var GetFileBin(string pfilename)`  |  获取ZIP中的文件内容，参数：pfilename-文件名，返回：文件二进制数据  |
----
### GObjLZ4File
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjLZ4File](#GObjLZ4File)
**描述**:LZ4高性能压缩文件处理类，用于打包和压缩多个文件
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vExtInfo  |  var  |  扩展信息数据  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Begin()`  |  开始创建LZ4压缩文件  |
|  `bool AddFile(string filename,string destname)`  |  添加文件到压缩包，参数：filename-源文件路径，destname-目标路径  |
|  `bool AddBin(var bin,string destname,int date=0)`  |  添加二进制数据到压缩包，参数：bin-二进制数据，destname-目标路径，date-文件日期  |
|  `bool AddText(var strv,string destname,int utf8=1,int date=0)`  |  添加文本到压缩包，参数：strv-文本内容，destname-目标路径，utf8-是否使用UTF8编码，date-文件日期  |
|  `bool End(string pfilename)`  |  完成压缩文件创建，参数：pfilename-输出文件路径  |
----
### GSocket
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GSocket](#GSocket)
**描述**:网络通信Socket类，管理TCP/IP连接和数据传输
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nStrCode  |  int  |  字符串编码模式;0-unicode默认,1-UTF8,2-GBK  |
|  m_nStrBinLen  |  int  |  字符串编码模式二进制命令长度  |
|  m_nPing  |  int  |  当前网络延迟值(毫秒)  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool SendLine(string pMsg)`  |  发送文本行，根据当前编码模式自动转换  |
|  `bool SendBinDirect(var& binv)`  |  发送二进制数据，直接传输不做格式转换  |
|  `void EnableMon(int bmon=1)`  |  启用或禁用网络监控，参数：bmon-是否启用(1启用，0禁用)  |
|  `int GetAddress()`  |  获取连接的整数形式IP地址  |
|  `string GetAddressString()`  |  获取连接的字符串形式IP地址  |
|  `void SetOnDataMode(int mode)`  |  设置数据处理模式，参数：mode-处理模式(SOCKET_STR/SOCKET_BIN等)  |
|  `int GetOnDataMode()`  |  获取当前数据处理模式  |
|  `bool GetStrBinInfo(int &getsize,int &total)`  |  获取字符串编码模式下的数据长度信息，参数：getsize-已获取大小，total-总大小  |
|  `bool GetReadCache(var& getbin,int getlen=0,int bdel=0)`  |  获取读取缓存数据，参数：getbin-存储缓存数据的变量，getlen-获取长度(0全部)，bdel-是否删除  |
|  `bool IsConnected()`  |  检查连接是否已建立  |
|  `void Close()`  |  关闭并释放socket连接  |
----
### GSocketC
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GSocket](#GSocket)/[GSocketC](#GSocketC)
**描述**:客户端套接字类，用于建立与服务器的TCP连接和通信
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sServName  |  string  |  获取服务器名称  |
|  m_nPort  |  int  |  获取服务器端口  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Connect(string pservername, int iport,string perrconnecteve=NULL,var& perragv=NULL)`  |  连接到指定服务器，参数：pservername-服务器名称，iport-端口号，perrconnecteve-连接错误事件名，perragv-错误事件参数  |
|  `void OnConnectOutTime()`  |  连接超时处理  |
|  `void CloseSocket()`  |  关闭套接字连接  |
|  `void Relink()`  |  重新建立连接  |
|  `void TestBreak()`  |  测试连接中断  |
|  `void SetMaxReadTime(int t)`  |  设置最大读取时间，参数：t-最大时间值  |
----
### GSocketS
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GSocketSBase](#GSocketSBase)/[GSocketS](#GSocketS)
**描述**:套接字服务器窗口类，用于管理套接字服务器连接和事件处理，支持多客户端连接和数据传输
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool StartServer(int port,int bautoscanport=1,string pBindAddStr=NULL,int bReuseaddr=0)`  |  启动服务器，参数：port-监听端口，bautoscanport-是否自动扫描可用端口，pBindAddStr-绑定地址，bReuseaddr-是否地址重用，返回：是否成功  |
|  `bool IsStart()`  |  检查服务器是否已启动，返回：服务器状态  |
|  `void SetLimit(int max)`  |  设置最大连接数限制，参数：max-最大连接数  |
|  `int GetBindAddress()`  |  获取绑定地址，返回：绑定的IP地址整数形式  |
|  `int GetSocketNum()`  |  获取当前连接数，返回：当前连接的客户端数量  |
----
### GSocketSBase
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GSocketSBase](#GSocketSBase)
**描述**:Socket服务器基类，负责监听和管理客户端连接
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetRecClass(obj p,string pclassname=NULL)`  |  设置联入的GSocket父对象和派生类名  |
|  `int GetPort()`  |  返回端口号  |
|  `var GetAllRec()`  |  获取所有已连接的客户端  |
|  `void SetAutoPingDelay(int delay)`  |  设置自动ping延迟时间  |
----
### GVNetObj
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GVNetObj](#GVNetObj)
**描述**:虚拟网络对象类，用于管理多客户端连接和通信
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void AddLink(int64 mac,var paddr,var agv)`  |  添加网络链接，参数：mac-设备标识，paddr-地址对象，agv-附加参数  |
|  `void OnVAddressBreak(int errkind,var agv)`  |  处理地址中断事件，参数：errkind-错误类型，agv-附加参数  |
|  `void ToC(strid fun,var pagv=NULL)`  |  向所有客户端发送调用，参数：fun-函数ID，pagv-参数  |
----
### GSocketUdp
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GSocketUdp](#GSocketUdp)
**描述**:UDP套接字类，用于实现UDP通信和命令传输
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nPort  |  int  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int GetIpAddress(string paddress)`  |  获取IP地址，参数：paddress-地址字符串，返回：IP地址整数形式  |
|  `bool BindPort(int port=0,int scanenum=5,string pbindip=NULL)`  |  绑定端口，参数：port-起始端口号，scanenum-扫描端口数量，pbindip-绑定IP地址，返回：是否成功  |
|  `bool SendTo(int ip,int port,int cmdid,var pagv=NULL)`  |  发送UDP数据，参数：ip-目标IP地址，port-目标端口，cmdid-命令ID，pagv-参数，返回：是否成功  |
----
### GNetFileObj
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GNetFileObj](#GNetFileObj)
**描述**:网络文件对象类，提供文件传输与下载功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sUrlName  |  string  |  获取URL名称  |
|  m_sLocName  |  string  |  获取本地文件名  |
|  m_vDownInfo  |  var  |  获取下载信息  |
|  m_vPostDest  |  var  |  获取目标地址  |
|  m_vUserAgv  |  var  |  用户自定义参数  |
|  m_FileSize  |  int64  |  获取文件大小(字节)  |
|  m_FileDate  |  int  |  获取文件日期(时间戳)  |
|  m_TransLen  |  int64  |  获取已传输数据长度(字节)  |
|  m_fTransSpeed  |  float  |  获取传输速度(KB/秒)  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int64 GetFileSize()`  |  获取文件大小，返回：文件大小（字节数）  |
|  `int GetFileTime()`  |  获取文件时间戳，返回：文件时间（秒）  |
|  `bool SetFileTime(int time)`  |  设置文件时间戳，参数：time-时间戳（秒），返回：操作是否成功  |
|  `float GetTransSpeed()`  |  获取传输速度，返回：当前传输速度（字节/秒）  |
|  `void SetNoti(obj ptr,strid okfun,strid errfun,strid perfun=0)`  |  设置通知回调，参数：ptr-通知对象，okfun-成功回调函数ID，errfun-错误回调函数ID，perfun-进度回调函数ID  |
|  `bool StartDown(var postdest,string purl,string plocname,var fsize,int fdate)`  |  开始下载文件，参数：postdest-目标地址，purl-URL，plocname-本地文件名，fsize-文件大小，fdate-文件日期，返回：操作是否成功  |
|  `bool PerFileSvr(string pname,string plocname,int isupmode=0)`  |  配置文件服务器，参数：pname-服务器名称，plocname-本地文件名，isupmode-是否为上传模式，返回：操作是否成功  |
|  `var GetDownInfo()`  |  获取下载信息，返回：下载信息数组  |
|  `bool GetDown(var psvrlink,strid svrfunid,string purl,string plocname)`  |  获取下载文件，参数：psvrlink-服务器链接，svrfunid-服务器函数ID，purl-URL，plocname-本地文件名，返回：操作是否成功  |
|  `bool OnFileInfo(var info)`  |  处理文件信息回调，参数：info-文件信息，返回：处理是否成功  |
----
### GMIDFileObj
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GMIDFileObj](#GMIDFileObj)
**描述**:中间存储键值对的文件对象类，用于在文件中持久化存储变量数据
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Open(string pcachefilename,int breadnoly=0)`  |  打开或创建数据文件，参数：文件名路径，是否只读模式  |
|  `bool IsOpen()`  |  检查文件是否已成功打开  |
|  `bool Clean()`  |  清空并重新创建数据文件  |
|  `void Close()`  |  关闭数据文件  |
|  `bool WriteVar(var keyv,var v,int ziplevel=4)`  |  写入变量数据，参数：keyv-键值，v-要写入的变量，ziplevel-压缩级别(默认4)，返回：是否成功  |
|  `bool ReadVar(var keyv,var& v)`  |  读取变量数据，参数：keyv-键值，v-读取的变量，返回：是否成功  |
|  `bool DelVar(var keyv)`  |  删除变量，参数：keyv-要删除的键值，返回：是否成功  |
|  `bool IsHaveKey(var keyv)`  |  检查键值是否存在，参数：keyv-键值，返回：是否存在  |
|  `var ListKey(var key0,int k1=-1,int k2=-1)`  |  列出符合条件的所有键值，参数：key0-主键，k1-子键1(默认-1表示全部)，k2-子键2(默认-1表示全部)，返回：键值列表  |
|  `var ReadAllAsVar(var key0,int k1=-1,int k2=-1)`  |  读取所有符合条件的变量，参数：key0-主键，k1-子键1(默认-1表示全部)，k2-子键2(默认-1表示全部)，返回：变量集合  |
|  `int GetKeyNum()`  |  获取键值总数，返回：当前文件中存储的键值数量  |
|  `int64 GetNewKey0()`  |  生成新的唯一主键，返回：新的主键值  |
|  `int DelKey(var key0,int k1=-1,int k2=-1)`  |  删除符合条件的键值，参数：key0-主键，k1-子键1(默认-1表示全部)，k2-子键2(默认-1表示全部)，返回：删除的键值数量  |
|  `int GetFileLen()`  |  获取文件大小，返回：文件长度（字节）  |
|  `int GetUserFlag(int no)`  |  获取用户标志，参数：no-标志索引，返回：标志值  |
|  `void SetUserFlag(int no,int flag)`  |  设置用户标志，参数：no-标志索引，flag-标志值  |
----
### GObjShow
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)
**描述**:2D显示对象基类，用于在2D场景中显示和管理可视对象
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLayer  |  int  |  显示层号  |
|  m_fX  |  float  |  X坐标  |
|  m_fY  |  float  |  Y坐标  |
|  m_fZ  |  float  |  Z坐标(层级)  |
|  m_nPageFlag  |  int  |  页面标志  |
|  m_nCanTouch  |  int  |  touch查找标志  |
|  m_nTouchHook  |  int  |    |
|  m_nShow  |  int  |  是否可见  |
|  m_nShowMode  |  int  |  显示模式  |
|  m_fW  |  float  |  取对象宽  |
|  m_fH  |  float  |  取对象高  |
|  m_nClip  |  int  |  视区剪裁是否启用  |
|  m_nDisSubTouch  |  int  |  是否禁止子对象Touch  |
|  m_nDisable  |  int  |  是否禁止Touch  |
|  m_nEnable  |  int  |  是否启用Touch&key  |
|  m_nAlphaInherit  |  int  |  是否继承alpha透明度  |
|  m_nAbsMat  |  int  |  是否绝对矩阵变换  |
|  m_fAlpha  |  float  |  对象透明度值  |
|  pidshow  |  obj  |  显示父对象  |
|  m_pShowWnd  |  obj  |  所属窗口对象  |
|  m_vPos2  |  vec2  |  对象2D坐标(x,y)  |
|  m_vPos  |  vec3  |  对象3D坐标(x,y,z)  |
|  m_vRect  |  vec4  |  对象矩形区域(left,top,right,bottom)  |
|  m_vRectPos  |  vec4  |  对象在世界坐标中的矩形区域  |
|  m_vRectCenter  |  vec2  |  对象矩形中心点  |
|  m_vPosCenter  |  vec2  |  对象在世界坐标中的中心点  |
|  m_vRightBottom  |  vec2  |  对象右下角点  |
|  m_fPosLeft  |  float  |  对象左边界的世界坐标  |
|  m_fPosRight  |  float  |  对象右边界的世界坐标  |
|  m_fPosTop  |  float  |  对象上边界的世界坐标  |
|  m_fPosBottom  |  float  |  对象下边界的世界坐标  |
|  m_vSize  |  vec2  |  对象大小(width,height)  |
|  m_vColor  |  vec4  |  颜色vec4(r,g,b,a)  |
|  m_nColor  |  color  |  颜色ARGB值  |
|  m_nSelBoxColor  |  color  |  设置选择框颜色  |
|  m_pCon  |  ptrex  |  布局容器对象  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void DeleteAllShowSub(int bonlyshow=0,int bonlythisobj=1)`  |  删除所有显示子对象，参数：bonlyshow-是否只删除显示对象，bonlythisobj-是否只删除本对象的子对象  |
|  `var GetAllShowSubObj(int bonlyshow=0,int bonlythisobj=1)`  |  获取所有显示子对象，参数：bonlyshow-是否只获取显示对象，bonlythisobj-是否只获取本对象的子对象，返回：子对象数组  |
|  `vec2 PlaceShowSubObj(float startx,float starty,float dx,float dy,var ex=NULL)`  |  排列显示子对象，参数：startx-起始X坐标，starty-起始Y坐标，dx-X方向间距，dy-Y方向间距，ex-扩展参数，返回：排列后的结束坐标  |
|  `obj GetShowSub(int no)`  |  获取指定索引的显示子对象，参数：no-子对象索引，返回：子对象  |
|  `obj GetShowHead()`  |  获取第一个子对象，返回：第一个子对象  |
|  `obj GetShowTail()`  |  获取最后一个子对象，返回：最后一个子对象  |
|  `obj GetShowNext()`  |  获取下一个同级对象，返回：下一个同级对象  |
|  `obj GetShowBefore()`  |  获取上一个同级对象，返回：上一个同级对象  |
|  `void SetPos(float x,float y,float z=0)`  |  设置对象位置，参数：x-X坐标，y-Y坐标，z-Z坐标  |
|  `void OffSetPos(float dx,float dy,float dz=0)`  |  移动对象位置，参数：dx-X方向偏移，dy-Y方向偏移，dz-Z方向偏移  |
|  `void SetLayer(int layer)`  |  设置显示层号，参数：layer-层号  |
|  `void BringZPos(int mode)`  |  将对象置于前或后，参数：mode-模式(0:置于最前，1:置于最后)  |
|  `void MoveZPosTo(obj p,int after=1)`  |  将对象移动到指定对象的前或后，参数：p-目标对象，after-是否置于其后(1:后，0:前)  |
|  `void SetRect(float left,float top,float right,float bottom)`  |  设置对象矩形区域，参数：left-左边界，top-上边界，right-右边界，bottom-下边界  |
|  `var GetRect()`  |  获取对象矩形区域，返回：矩形区域(vec4格式)  |
|  `void SetPosR(float x,float y,float r)`  |  设置对象位置和半径，参数：x-中心X坐标，y-中心Y坐标，r-半径  |
|  `void SetSize(float w,float h)`  |  设置对象尺寸，参数：w-宽度，h-高度  |
|  `void GetSize(float &w,float &h)`  |  获取对象尺寸，参数：w-返回宽度，h-返回高度  |
|  `float GetWidth()`  |  获取对象宽度，返回：宽度  |
|  `float GetHeight()`  |  获取对象高度，返回：高度  |
|  `void SetPosSize(float x,float y,float w,float h)`  |  设置对象位置和尺寸，参数：x-X坐标，y-Y坐标，w-宽度，h-高度  |
|  `void SetShowMode(int showmode=0)`  |  设置显示模式，参数：showmode-显示模式  |
|  `void SetShow(int bshow=1)`  |  设置是否显示，参数：bshow-是否显示(1:显示，0:隐藏)  |
|  `void AddSizeNoti(obj p,strid sizefunid=0,int bcallimm=0)`  |  添加尺寸改变通知，参数：p-通知对象，sizefunid-回调函数ID，bcallimm-是否立即调用  |
|  `void DelSizeNoti(obj p,strid sizefunid=0)`  |  删除尺寸改变通知，参数：p-通知对象，sizefunid-回调函数ID  |
|  `void NotiOnSizeChged()`  |  触发尺寸改变通知  |
|  `bool IsPointIn(vec3 locpt)`  |  判断点是否在对象内，参数：locpt-本地坐标点，返回：是否在对象内  |
|  `bool SetPageFlag(int iflag,int bset=1)`  |  设置页面标志，参数：iflag-标志位，bset-是否设置(1:设置，0:清除)，返回：是否成功  |
|  `bool GetPageFlag(int iflag)`  |  获取页面标志，参数：iflag-标志位，返回：是否设置  |
|  `void SetDebug(int flag,int bset=1)`  |  设置调试标志，参数：flag-标志位，bset-是否设置(1:设置，0:清除)  |
|  `bool IsDebug(int flag)const`  |  获取调试标志，参数：flag-标志位，返回：是否设置  |
|  `void SetClip(int bclip)`  |  设置是否裁剪，参数：bclip-是否裁剪(1:裁剪，0:不裁剪)  |
|  `void SetOutClip(int bclip)`  |  设置是否外部裁剪，参数：bclip-是否外部裁剪(1:外部裁剪，0:不外部裁剪)  |
|  `void SetLastShow(int blast=1)`  |  设置是否最后显示，参数：blast-是否最后显示(1:最后显示，0:正常显示)  |
|  `bool IsScrWnd()`  |    |
|  `vec3 GetScr2Loc(vec2 pt)`  |  转换对象屏幕坐标到内部坐标  |
|  `vec2 GetLoc2Scr(vec3 pt)`  |  转换对象内部坐标到屏幕坐标  |
|  `vec3 ScrPathIn(vec2 pt,var showpath)`  |    |
|  `void GetPtOut(vec3& pt)`  |    |
|  `void GetPtIn(vec3& pt)`  |    |
|  `bool IsScrPtIn(vec2 scrpt)`  |    |
|  `void Center()`  |    |
|  `void SetCanTouch(int touchmode)`  |    |
|  `void AddCanTouch(int touchmode)`  |    |
|  `void SetTouchHook(strid hid)`  |    |
|  `void SetDisSubTouch(int bdisable)`  |  设置是否禁止子对象Touch，参数：bdisable-是否禁止(1禁止，0不禁止)，返回：无  |
|  `void Enable(int bable=1)`  |  设置对象是否启用，参数：bable-是否启用(1启用，0禁用)，返回：无  |
|  `void SetAlpha(float alpha)`  |  设置显示透明度，参数：alpha-透明度值(0.0-1.0)，返回：无  |
|  `bool TransPosTo(obj ptr,vec3& pt)`  |  转换坐标到目标对象，参数：ptr-目标对象，pt-坐标点，返回：转换是否成功  |
|  `bool MoveFatherTo(obj ptr,int transpos=1)`  |  移动对象到新的父对象下，参数：ptr-新父对象，transpos-是否转换位置(1转换，0不转换)，返回：是否成功  |
|  `bool SetShowFather(obj ptr,int transpos=0)`  |  设置显示父对象，参数：ptr-新父对象，transpos-是否转换位置(1转换，0不转换)，返回：是否成功  |
|  `void SetColor(color c,int a=0)`  |  设置颜色，参数：c-颜色值，a-透明度(可选)，返回：无  |
|  `void SetSelBoxColor(color c)`  |  设置选择框颜色，参数：c-颜色值，返回：无  |
|  `var GetPointObjSz(vec3 pt,int findmode,var agvex)`  |  根据点获取对象列表，参数：pt-点坐标，findmode-查找模式，agvex-扩展参数，返回：对象列表  |
|  `var GetRectObjSz(vec4 rect,int crossmode,int findmode,var agvex)`  |  根据矩形获取对象列表，参数：rect-矩形区域，crossmode-交叉模式，findmode-查找模式，agvex-扩展参数，返回：对象列表  |
|  `bool SetPerShowFun(strid funnameid)`  |  设置显示回调函数，参数：funnameid-函数名ID，返回：是否成功  |
|  `bool SetConClass(strid conclass=1)`  |  设置布局容器类，参数：conclass-容器类ID，返回：是否成功  |
|  `bool RefConClass(obj pshow)`  |  引用其他对象的布局容器，参数：pshow-引用对象，返回：是否成功  |
|  `void ConPlace(int bimm=0)`  |  执行布局，参数：bimm-是否立即执行，返回：无  |
----
### GObj2DWnd
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj2DWnd](#GObj2DWnd)
**描述**:2D窗口对象类，提供操作系统窗口的创建和管理功能，支持窗口显示、交互和渲染等操作
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vOutRect  |  vec4  |  窗口外部区域矩形  |
|  m_nTopMost  |  int  |  设置窗口是否置顶，参数：b-是否置顶(1置顶，0不置顶)，返回：是否设置成功  |
|  m_fAniSpeed  |  float  |  设置动画播放速度  |
|  m_vShapeEx  |  var  |  扩展形状属性  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool CreateOsWnd(int style=0)`  |  创建操作系统窗口，参数：style-窗口风格，返回：成功返回true，失败返回false  |
|  `bool SetOsWinStyle(int style)`  |  设置窗口显示风格，参数：style-窗口风格，返回：成功返回true，失败返回false  |
|  `void Set2DRender(int b2d=1)`  |  设置2D渲染模式，参数：b2d-是否启用2D渲染(1启用，0禁用)，返回：无  |
|  `void OnWndClose()`  |  窗口关闭时触发，返回：无  |
|  `void SetText(string pstr)`  |  设置窗口标题，参数：pstr-标题文字，返回：无  |
|  `string GetText()`  |  窗口标题，返回：标题文字  |
|  `bool SetWinIcon(string piconfilename)`  |  设置窗口图标，参数：piconfilename-图标文件名，返回：成功返回true，失败返回false  |
|  `void CloseWnd()`  |  关闭窗口，返回：无  |
|  `void DragAcceptFiles(int bacc=1)`  |  设置是否接受外部文件拖放，参数：bacc-是否接受(1接受，0不接受)，返回：无  |
|  `void FlashWindow(int bInvert=1)`  |  设置窗口闪烁，参数：bInvert-是否闪烁(1闪烁，0不闪烁)，返回：无  |
|  `void SetTopMost(int btop)`  |  设置窗口置顶，参数：btop-是否置顶(1置顶，0不置顶)，返回：无  |
|  `bool IsActive()`  |  判断窗口是否处于活动状态，返回：true表示活动，false表示非活动  |
|  `void SetAutoAct(int act)`  |  设置窗口自动激活，参数：act-是否自动激活(1自动激活，0不自动激活)，返回：无  |
|  `bool IsScrWnd()`  |  判断是否为屏幕窗口，返回：true表示是屏幕窗口，false表示非屏幕窗口  |
|  `void Enable(int bable=1)`  |  设置窗口启用状态，参数：bable-是否启用(1启用，0禁用)，返回：无  |
|  `int IsEnable()`  |  窗口启用状态，返回：1表示启用，0表示禁用  |
|  `int SetWndShow(int mode)`  |  设置窗口显示模式，参数：mode-显示模式，返回：当前显示模式  |
|  `void OnDropFiles(vec2 pt,var filenamesz)`  |  处理文件拖放事件，参数：pt-拖放位置坐标，filenamesz-文件名列表，返回：无  |
|  `var FindScrPtWnd(vec2 pt)`  |  根据屏幕坐标查找窗口，参数：pt-屏幕坐标，返回：窗口对象  |
----
### GBoxShowApp
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj2DWnd](#GObj2DWnd)/[GBoxShowApp](#GBoxShowApp)
**描述**:应用程序显示框架类，用于管理应用窗口、输入事件和资源沙盒
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fIMEPopH  |  float  |  输入法键盘弹出高度  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void CloseApp()`  |  关闭应用程序，返回：无  |
|  `var FindScrPtWnd(vec2 pt)`  |  根据屏幕坐标查找窗口，参数：pt-屏幕坐标，返回：窗口对象  |
|  `void SetIMEPopH(float h)`  |  设置输入法键盘弹出高度，参数：h-高度，返回：无  |
----
### GSandApp2DWnd
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj2DWnd](#GObj2DWnd)/[GSandApp2DWnd](#GSandApp2DWnd)
**描述**:2D沙盒应用窗口类，用于作为沙盒环境的显示根节点并处理窗口相关事件
----
### GObj2DSandBox
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj2DSandBox](#GObj2DSandBox)
**描述**:2D沙盒环境类，用于创建和管理2D场景中的脚本执行环境，提供资源控制、对象创建和触控管理功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pSandApp  |  obj  |  获取沙盒应用对象指针  |
|  m_nLaunchAppliction  |  int  |  启动外部应用程序的权限控制参数  |
|  m_nShellOpenDoc  |  int  |  Shell打开文档的权限控制参数  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `obj GetShowRoot()`  |  获取显示根对象，返回：显示根对象指针  |
|  `obj GetResCtrl()`  |  获取资源控制器对象，返回：资源控制器对象指针  |
|  `bool Reset()`  |  重置沙盒环境，返回：是否成功  |
|  `bool DefMacro(string pkey,var val)`  |  定义宏，参数：pkey-宏名称，val-宏值，返回：是否成功  |
|  `bool LoadScript(string pstartname)`  |  加载脚本文件，参数：pstartname-启动脚本文件名，返回：是否成功  |
|  `bool Start()`  |  启动沙盒环境，返回：是否成功  |
|  `bool GetScriptClassInfo(var& ret,var pobj)`  |  获取脚本类信息，参数：ret-返回的类信息，pobj-对象，返回：是否成功  |
|  `bool IsIncludeFile(int fid)`  |  检查文件是否已包含，参数：fid-文件ID，返回：是否已包含  |
|  `var GetIncludeFiles()`  |  获取所有包含的文件列表，返回：文件列表  |
|  `var GetRootClassPtr()`  |  获取根类指针，返回：根类指针  |
|  `var SeekFileClassFun(int fid,int line,int col)`  |  查找指定位置的类函数，参数：fid-文件ID，line-行号，col-列号，返回：查找结果  |
|  `obj NewSandBoxObj(strid classnameid,obj ppFather)`  |  创建沙盒对象，参数：classnameid-类名ID，ppFather-父对象，返回：创建的对象指针  |
|  `obj CreateSandAppObj(int b3d=0)`  |  创建沙盒应用对象，参数：b3d-是否为3D应用，返回：创建的应用对象指针  |
----
### GResManager
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GResManager](#GResManager)
**描述**:这个类实现了资源管理器，负责资源的加载、缓存和管理，支持本地与网络资源，并维护资源引用关系与状态
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sFilePath  |  string  |  资源文件路径  |
|  m_pStatusNoti  |  obj  |  状态通知对象  |
|  m_vDatInfo  |  var  |  资源管理器数据信息  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void RegResCtrl()`  |  注册资源控制器  |
|  `int LoadRes(string path,string resfilename)`  |  加载资源文件，指定路径和文件名  |
|  `void SetSvrLink(var psvrlink)`  |  设置服务器链接，关联资源服务器  |
|  `void SaveData()`  |  保存资源数据到文件，在系统退出时自动调用  |
|  `bool SetResData(var resdat)`  |    |
|  `bool IsRes(var resdat)`  |  检查是否为有效资源数据  |
|  `var GetResData(var resname)`  |  根据资源名称获取资源数据  |
|  `int GetResFileName(var resname,string &locname,var& linksz)`  |  获取资源文件名，返回本地文件路径和链接信息  |
|  `int PerRes(var resname,var& dat)`  |  处理资源，加载或更新资源数据  |
----
### GObjText
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjShape](#GObjShape)/[GObjText](#GObjText)
**描述**:2D文本对象类，提供文本渲染和属性控制功能，支持字体设置、对齐方式、颜色控制和下划线等文本显示效果
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vOutRect  |  vec4  |  获取文本外边距矩形，返回：边距向量(左,上,右,下)  |
|  m_sText  |  string  |  获取文本内容，返回：文本字符串  |
|  m_vTextColor  |  vec4  |  获取文本颜色，返回：颜色向量(r,g,b,a)  |
|  m_nTextColor  |  color  |  获取文本颜色，返回：ARGB颜色值  |
|  m_vColorEx  |  vec4  |  获取扩展颜色，返回：颜色向量(r,g,b,a)  |
|  m_nColorEx  |  color  |  获取扩展颜色，返回：ARGB颜色值  |
|  m_nFixRect  |  int  |  获取矩形固定模式，返回：固定模式值  |
|  m_sFontName  |  string  |  获取字体名称，返回：字体名称字符串  |
|  m_nFontW  |  int  |  获取字体宽度，返回：字体宽度值  |
|  m_nFontEx  |  int  |  获取字体扩展模式，返回：扩展模式值  |
|  m_nItalic  |  int  |  获取字体是否斜体，返回：0-正常，1-斜体  |
|  m_nWeight  |  int  |  获取字体粗细，返回：字体粗细值  |
|  m_nAlign  |  int  |  获取对齐方式，返回：对齐方式值(h*10+v)  |
|  m_nHAlign  |  int  |  获取水平对齐方式，返回：0-左，1-中，2-右  |
|  m_nVAlign  |  int  |  获取垂直对齐方式，返回：0-上，1-中，2-下  |
|  m_nUndLine  |  int  |  获取下划线设置，返回：0-不显示，1-显示  |
|  m_fAutoFixHeightMax  |  float  |  获取自动高度调整的最大高度，返回：最大高度值  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetText(string ptext)`  |  设置文本内容，参数：ptext-文本字符串  |
|  `string GetText()`  |  获取文本内容，返回：文本字符串  |
|  `void SetColorEx(color c,int a=0)`  |  设置扩展颜色，参数：c-ARGB颜色值，a-透明度(可选)  |
|  `void SetTextColor(color c,int a=0)`  |  设置文本颜色，参数：c-ARGB颜色值，a-透明度(可选)  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名称，w-字体宽度，h-字体高度，weight-字体粗细，bItalic-是否斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-字体宽度，h-字体高度  |
|  `void SetFixRect(int b)`  |  设置矩形固定模式，参数：b-固定模式(0-不固定，1-固定宽度自动高度，2-固定宽高)  |
|  `void SetAlign(int h=0,int v=0)`  |  设置文本对齐方式，参数：h-水平对齐(0-左，1-中，2-右)，v-垂直对齐(0-上，1-中，2-下)  |
|  `void SetUndLine(int bundline=1)`  |  设置下划线，参数：bundline-是否显示下划线(0-不显示，1-显示)  |
|  `void SetDef(float x,float y,string ptext,color color=0,int fontsize=0)`  |  快速设置文本对象属性，参数：x-x坐标，y-y坐标，ptext-文本内容，color-文本颜色，fontsize-字体大小  |
|  `void SetAutoFixHeightMax(float h)`  |  设置自动高度调整的最大高度，参数：h-最大高度值  |
----
### GObjShape
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjShape](#GObjShape)
**描述**:常用的2D形状
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vLineColor  |  vec4  |  形状线条颜色的vec4表示  |
|  m_nLineColor  |  color  |  形状线条颜色的ARGB值  |
|  m_fR  |  float  |  绑定圆角半径属性  |
|  m_fFade  |  float  |  绑定边缘过渡属性  |
|  m_nFrame  |  int  |  当前图像帧序号  |
|  m_vShapeEx  |  var  |  绑定形状扩展属性  |
|  m_fScale  |  float  |  形状的缩放比例  |
|  m_fDegree  |  float  |  形状的旋转角度（度数表示）  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetShape(color fillc,color linec=0,float r=0,float fade=0)`  |  设置形状的填充颜色、线条颜色、圆角半径和过渡效果，参数：fillc-填充颜色，linec-线条颜色，r-圆角半径，fade-边缘过渡  |
|  `void SetImg(var nameorid,int frameno=-1)`  |  设置形状显示的图像，参数：nameorid-图像名称或ID，frameno-帧序号，返回：无  |
|  `var GetImgPtr()`  |  当前使用的图像对象，返回：图像的GVar引用  |
|  `void SetShapeExImg(var nameorid,int repeat=1)`  |  设置形状的扩展图像，参数：nameorid-图像名称或ID，repeat-重复次数，返回：无  |
|  `void SetLineColor(color c,int a=0)`  |  设置线条颜色，参数：c-颜色值，a-透明度（可选），返回：无  |
|  `void SetScale(float f)`  |  设置形状的缩放比例，参数：f-缩放系数，返回：无  |
|  `void SetDegree(float deg)`  |  设置形状的旋转角度，参数：deg-角度（度数），返回：无  |
----
### GObjView
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)
**描述**:2D视图对象类，提供可滚动和缩放的视图功能，支持地图和视图坐标系转换、视图变换通知、滚动条显示和弹性拖拽等功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLineColor  |  color  |  线条颜色ARGB值  |
|  m_fR  |  float  |  圆角半径  |
|  m_fFade  |  float  |  边缘渐变  |
|  m_vShapeEx  |  var  |  扩展形状属性  |
|  m_nElasticDrag  |  int  |  弹性拖拽设置  |
|  m_vViewOrg  |  vec2  |  视图原点坐标  |
|  m_fViewX  |  float  |  视图X坐标  |
|  m_fViewY  |  float  |  视图Y坐标  |
|  m_fViewW  |  float  |  视图宽度  |
|  m_fViewH  |  float  |  视图高度  |
|  m_vMapSize  |  vec2  |  地图大小  |
|  m_nScrollW  |  int  |  显示垂直滚动条宽度  |
|  m_nScrollH  |  int  |  显示水平滚动条高度  |
|  m_vScrollColor  |  vec4  |  滚动条颜色  |
|  m_nScrollColor  |  color  |  滚动条颜色ARGB值  |
|  m_ScrollBkColor  |  vec4  |  滚动条背景颜色  |
|  m_nScrollBkColor  |  color  |  滚动条背景颜色ARGB值  |
|  m_fDegree  |  float  |  视图旋转角度(度)  |
|  m_fScale  |  float  |  视图缩放比例  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void AddViewNoti(obj p,strid funid,int bcallimm=1)`  |  添加视图变化通知，参数：p-接收通知的对象，funid-回调函数ID，bcallimm-是否立即回调(1立即，0不立即)，返回：无  |
|  `void DelViewNoti(obj p,strid funid=0)`  |  删除视图变化通知，参数：p-接收通知的对象，funid-回调函数ID(0表示删除所有)，返回：无  |
|  `void SetShape(color fillc,color linec=0,float r=0,float fade=0)`  |  设置视图形状，参数：fillc-填充颜色，linec-线条颜色，r-圆角半径，fade-边缘渐变，返回：无  |
|  `void SetMapSize(float w,float h)`  |  设置地图大小，参数：w-宽度，h-高度，返回：无  |
|  `void SetViewPos(float x,float y,float movesec=0)`  |  设置视图位置，参数：x-X坐标，y-Y坐标，movesec-移动动画时间(秒)，返回：无  |
|  `void OffSetViewPos(float x,float y,float movesec=0)`  |  偏移视图位置，参数：x-X偏移量，y-Y偏移量，movesec-移动动画时间(秒)，返回：无  |
|  `void SetViewPer(float perx,float pery,float movesec=0)`  |  按百分比设置视图位置，参数：perx-X百分比(0-1)，pery-Y百分比(0-1)，movesec-移动动画时间(秒)，返回：无  |
|  `void MakeRectVisable(vec4 v4,float movesec=0)`  |  使矩形区域可见，参数：v4-矩形区域(x,y,width,height)，movesec-移动动画时间(秒)，返回：无  |
|  `void StopViewMove()`  |  停止视图移动动画，返回：无  |
|  `void SetViewMove(vec2 speed)`  |  设置视图移动速度，参数：speed-速度向量，返回：无  |
----
### GObjEdit
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjEdit](#GObjEdit)
**描述**:编辑框对象类，继承自GObjShow，用于处理单行文本的编辑、显示和交互功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sText  |  string  |  编辑框文本内容  |
|  m_vTextColor  |  vec4  |  文本颜色(vec4格式)  |
|  m_nTextColor  |  color  |  文本颜色(ARGB格式)  |
|  m_vFillColor  |  vec4  |  填充颜色  |
|  m_vLineColor  |  vec4  |  边框颜色  |
|  m_nLineColor  |  color  |  边框颜色  |
|  m_nActBkColor  |  color  |  激活状态背景色  |
|  m_nActTextColor  |  color  |  激活状态文本颜色  |
|  m_nActLineColor  |  color  |  激活状态边框颜色  |
|  m_fR  |  float  |  圆角半径  |
|  m_vSelBkColor  |  vec4  |  选中区域背景色  |
|  m_nSelBkColor  |  color  |  选中区域背景色  |
|  m_vSelTextColor  |  vec4  |  选中区域文本颜色  |
|  m_nSelTextColor  |  color  |  选中区域文本颜色  |
|  m_vCurColor  |  vec4  |  光标颜色  |
|  m_nCurColor  |  color  |  光标颜色  |
|  m_sFontName  |  string  |  字体名称  |
|  m_nFontW  |  int  |  字体宽度  |
|  m_nFontEx  |  int  |  字体扩展模式  |
|  m_nItalic  |  int  |  是否斜体  |
|  m_nWeight  |  int  |  字体粗细  |
|  m_nSelStart  |  int  |  选中文本的起始位置  |
|  m_nSelEnd  |  int  |  选中文本的结束位置  |
|  m_nCurX  |  int  |  当前光标的X坐标位置  |
|  m_nActive  |  int  |  编辑框是否处于激活状态  |
|  m_nPass  |  int  |  是否为密码输入模式  |
|  m_fTextViewX  |  float  |    |
|  m_fMarginLeft  |  float  |    |
|  m_fMarginRight  |  float  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetText(string ptext)`  |  设置编辑框文本内容，参数：ptext-文本内容  |
|  `string GetText()const`  |  获取编辑框文本内容，返回：文本内容  |
|  `void SetFillColor(color c,int a=0)`  |  设置填充颜色，参数：c-颜色值，a-透明度  |
|  `void SetLineColor(color c,int a=0)`  |  设置边框颜色，参数：c-颜色值，a-透明度  |
|  `void SetShape(color fillc,color linec=0,float r=0)`  |  设置形状样式，参数：fillc-填充颜色，linec-边框颜色，r-圆角半径  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名，w-宽度，h-高度，weight-字重，bItalic-是否斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-宽度，h-高度  |
|  `void SetDef(float x,float y,string ptext,color color=0)`  |  设置默认属性，参数：x-横坐标，y-纵坐标，ptext-文本内容，color-文本颜色  |
|  `int GetCharIndex(float locx)`  |  获取指定位置的字符索引，参数：locx-横坐标，返回：字符索引  |
|  `float GetCharPos(int i)`  |  获取指定索引的字符位置，参数：i-字符索引，返回：字符位置  |
|  `int GetLength()`  |  获取文本长度，返回：文本长度  |
|  `int GetSelNum()`  |  获取选中文本长度，返回：选中文本长度  |
|  `string GetMidStr(int start,int end)`  |  获取指定范围的文本，参数：start-起始位置，end-结束位置，返回：文本内容  |
|  `void Insert(int i,string ptext)`  |  在指定位置插入文本，参数：i-插入位置，ptext-要插入的文本  |
|  `bool Delete(int i,int num=1)`  |  删除指定位置的文本，参数：i-起始位置，num-删除数量，返回：是否删除成功  |
----
### GObjDoc
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)/[GObjDoc](#GObjDoc)
**描述**:文档对象类，用于处理文档的显示、编辑、样式和布局等功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sText  |  string  |  文档文本内容  |
|  m_nTextColor  |  color  |  文档默认文本颜色  |
|  m_nColorEx  |  color  |  文档扩展文本颜色  |
|  m_nCursorColor  |  color  |  光标颜色  |
|  m_nSelBkColor  |  color  |  选中区域背景色  |
|  m_nSelTextColor  |  color  |  选中区域文本颜色  |
|  m_nHiCurBkColor  |  color  |  高亮光标背景色  |
|  m_vOutRect  |  vec4  |  文档输出矩形区域  |
|  m_nCurX  |  int  |  当前光标列位置  |
|  m_nCurY  |  int  |  当前光标行位置  |
|  m_nSelMode  |  int  |  选择模式  |
|  m_nSelX0  |  int  |  选择起始列位置  |
|  m_nSelX1  |  int  |  选择结束列位置  |
|  m_nSelY0  |  int  |  选择起始行位置  |
|  m_nSelY1  |  int  |  选择结束行位置  |
|  m_nMinW  |  int  |  最小宽度限制  |
|  m_nMaxW  |  int  |  最大宽度限制  |
|  m_nMinH  |  int  |  最小高度限制  |
|  m_nMaxH  |  int  |  最大高度限制  |
|  m_nLineNum  |  int  |  文档总行数  |
|  m_nFontStyleNum  |  int  |  字体样式数量  |
|  m_nStyleNum  |  int  |  形状样式数量  |
|  m_nClassNum  |  int  |  类样式数量  |
|  m_nTabNum  |  int  |  标签样式数量  |
|  m_nActive  |  int  |  文档激活状态  |
|  m_bAutoFit  |  int  |  是否自动适应大小  |
|  m_bAutoWarp  |  int  |  是否自动换行  |
|  m_vImgMap  |  var  |  图片映射表  |
|  m_vStyleMap  |  var  |  样式映射表  |
|  m_CursorRc  |  vec4  |  光标矩形区域  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetText(string ptext)`  |  设置文档文本内容，参数：ptext-文本内容  |
|  `string GetText(int mode=0)`  |  获取文档文本内容，参数：mode-获取模式，返回：文本内容  |
|  `bool Load(string pfilename)`  |  从文件加载文档内容，参数：pfilename-文件名，返回：是否加载成功  |
|  `bool Save(string pfilename,int mode=0)`  |  保存文档内容到文件，参数：pfilename-文件名，mode-保存模式，返回：是否保存成功  |
|  `bool AddText(string pstr,int selmode=0)`  |  添加文本到文档末尾，参数：pstr-要添加的文本，selmode-选择模式，返回：是否添加成功  |
|  `bool InsertText(int colx,int coly,string pstr,int selmode=0)`  |  在指定位置插入文本，参数：colx-列位置，coly-行位置，pstr-要插入的文本，selmode-选择模式，返回：是否插入成功  |
|  `void SetTextColor(color c)`  |  设置文档默认文本颜色，参数：c-颜色值  |
|  `void SetColorEx(color c)`  |  设置文档扩展文本颜色，参数：c-颜色值  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置文档字体，参数：pfontname-字体名，w-宽度，h-高度，weight-字重，bItalic-是否斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置文档字体大小，参数：w-宽度，h-高度  |
|  `void SetLineDh(int h)`  |  设置行间距，参数：h-行间距值  |
|  `void SetLineStart(int x)`  |  设置行起始位置，参数：x-起始位置值  |
|  `void SetCurChgEmit(strid eveid)`  |  设置当前变更事件ID，参数：eveid-事件ID  |
|  `void NeedReCal(int mode=1)`  |  标记需要重新计算文档，参数：mode-计算模式  |
|  `int GetPtLine(int x,int y,int &colx)`  |  获取指定坐标位置的行号和列位置，参数：x-横坐标，y-纵坐标，colx-列位置，返回：行号  |
|  `bool GetPtStyle(var& ret,float ptx,float pty,int mode=0)`  |  获取指定坐标位置的样式，参数：ret-返回样式，ptx-横坐标，pty-纵坐标，mode-模式，返回：是否成功  |
|  `void SetCurPtPos(int x,int y,int selmode=0)`  |  设置当前光标位置，参数：x-列位置，y-行位置，selmode-选择模式  |
|  `void SetCurPos(int x,int y,int selmode=0)`  |  设置当前光标位置，参数：x-列位置，y-行位置，selmode-选择模式  |
|  `void MoveCurPos(int dcolx,int dcoly,int selmode=0)`  |  移动当前光标位置，参数：dcolx-列偏移量，dcoly-行偏移量，selmode-选择模式  |
|  `void SetSelect(int selmode,int x0,int y0,int x1,int y1)`  |  设置选择区域，参数：selmode-选择模式，x0-起始列，y0-起始行，x1-结束列，y1-结束行  |
|  `bool SelectTextAtLine(int colx,int coly,int num)`  |  在指定行选择文本，参数：colx-列位置，coly-行位置，num-选择数量，返回：是否选择成功  |
|  `string GetSubText(int mode,int x0,int y0,int x1,int y1)`  |  获取指定区域的文本内容，参数：mode-获取模式，x0-起始列，y0-起始行，x1-结束列，y1-结束行，返回：文本内容  |
|  `var FindStr(int colx,int coly,string pstr,int flag=0,int strmode=1)`  |  查找指定文本，参数：colx-起始列，coly-起始行，pstr-查找文本，flag-标志，strmode-字符串模式，返回：查找结果  |
|  `int FindWithFinder(int colx,int coly,var finderv,int &rx0,int &rx1)`  |  使用查找器查找文本，参数：colx-起始列，coly-起始行，finderv-查找器，rx0-起始列，rx1-结束列，返回：查找结果  |
|  `void NoSelect()`  |  清除选择区域  |
|  `void SetSizeLimit(int minw,int maxw,int minh,int maxh)`  |  设置文档大小限制，参数：minw-最小宽度，maxw-最大宽度，minh-最小高度，maxh-最大高度  |
|  `void SetAutoFitSize(int bfit)`  |  设置自动适应大小，参数：bfit-是否自动适应  |
|  `void SetAutoWarp(int warp)`  |  设置自动换行，参数：warp-是否自动换行  |
|  `bool DeleteText(int x0,int y0,int x1,int y1,int selmode=0)`  |  删除指定区域的文本，参数：x0-起始列，y0-起始行，x1-结束列，y1-结束行，selmode-选择模式，返回：是否删除成功  |
|  `bool DelSelect()`  |  删除选择区域的文本，返回：是否删除成功  |
|  `bool SetSelectFontStyle(string pstyle)`  |  设置选择区域的字体样式，参数：pstyle-样式字符串，返回：是否设置成功  |
|  `string GetSelectText(int mode=0)`  |  获取选择区域的文本内容，参数：mode-获取模式，返回：文本内容  |
|  `bool SetLineAlign(int coly,int h,int v)`  |  设置行的对齐方式，参数：coly-行位置，h-水平对齐，v-垂直对齐，返回：是否设置成功  |
|  `void SetImgMap(strid nameid,var imgsrc)`  |  设置图片映射，参数：nameid-名称ID，imgsrc-图片源  |
|  `void SetStyleMap(string pname,string pcmdstr)`  |  设置样式映射，参数：pname-样式名，pcmdstr-命令字符串  |
----
### GObjAni
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjAni](#GObjAni)
**描述**:2D动画对象类，提供帧动画的加载、播放和控制功能，支持多种动画类型、缩放、旋转和轨迹显示，用于创建和管理交互式动画效果
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vLineColor  |  vec4  |  线颜色  |
|  m_nShowLineTrack  |  int  |  是否显示轨迹线  |
|  m_nLineColor  |  color  |  线颜色ARGB值  |
|  m_fFrame  |  float  |  当前动画帧  |
|  m_fScale  |  float  |  整体缩放比例  |
|  m_fDegree  |  float  |  整体旋转角度(度)  |
|  m_pAni  |  ptrex  |  动画对象指针  |
|  m_fAniSpeed  |  float  |  动画播放速度  |
|  m_fAniStartSec  |  float  |  动画起始时间(秒)  |
|  m_nPlayStatus  |  int  |  当前播放状态  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetNoti(int bnoti)`  |  设置通知标志，参数：bnoti-是否启用通知  |
|  `void SetImgSz(var var)`  |  设置图像集合，参数：var-图像数据  |
|  `void SetFrame(float t)`  |  设置动画帧，参数：t-帧时间  |
|  `void SetScale(float f)`  |  设置缩放比例，参数：f-缩放系数  |
|  `void SetDegree(float deg)`  |  设置旋转角度，参数：deg-旋转角度(度)  |
|  `void CreateAni()`  |  创建动画对象  |
|  `bool LoadAni(var name)`  |  加载动画，参数：name-动画名称，返回：是否加载成功  |
|  `bool SetAniKind(strid kindname)`  |  设置动画类型，参数：kindname-类型名称ID，返回：是否设置成功  |
|  `var GetAniKindSz()`  |  获取动画类型列表，返回：类型数组  |
|  `float GetAniLength(strid kindname=0)`  |  获取动画长度，参数：kindname-类型名称ID（默认当前类型），返回：动画长度(秒)  |
|  `void SetPlayStatus(int mode=1)`  |  设置播放状态，参数：mode-播放模式(1:播放，0:停止)  |
|  `void PlayAni(strid kind=0,float start=0,float speed=1)`  |  播放动画，参数：kind-动画类型ID，start-起始时间(秒)，speed-播放速度  |
----
### GObjUndo
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjUndo](#GObjUndo)
**描述**:撤销和重做操作管理类，用于记录和执行对象状态的撤销和重做功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_UndoNum  |  int  |  当前撤销操作数量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Destroy()`  |  销毁所有撤销和重做数据，返回：无  |
|  `int PerUndoOp(obj plink,strid nameid,strid undofunid)`  |  准备一个撤销操作，参数：plink-关联对象，nameid-操作名称ID，undofunid-撤销函数ID，返回：操作版本号  |
|  `bool AddUndo(int opver,strid opkind,var opkey,var opdat)`  |  添加撤销数据，参数：opver-操作版本号，opkind-操作类型，opkey-操作键，opdat-操作数据，返回：成功返回true，失败返回false  |
|  `bool EndUndoOp(int opver)`  |  结束撤销操作，参数：opver-操作版本号，返回：成功返回true，失败返回false  |
|  `bool TryUndo()`  |  尝试执行撤销操作，返回：成功返回true，失败返回false  |
----
### GObjTxt
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)/[GObjTxt](#GObjTxt)
**描述**:多行文本输出控件，支持日志记录、错误输出和调试信息显示，具有自动滚动、图标与颜色设置等功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nCurLineNo  |  int  |  当前行号  |
|  m_nAutoButtomView  |  int  |  自动滚动到底部视图  |
|  m_nMaxLine  |  int  |  最大显示行数  |
|  m_nBottomSpaceLine  |  int  |  底部额外空行数  |
|  m_nColorEx  |  color  |  扩展颜色  |
|  m_nFillColor  |  color  |  填充颜色  |
|  m_nHiBkColor  |  color  |  高亮背景颜色  |
|  m_vHiBkColor  |  vec4  |  高亮背景颜色矢量值  |
|  m_nHiTextColor  |  color  |  高亮文本颜色  |
|  m_vHiTextColor  |  vec4  |  高亮文本颜色矢量值  |
|  m_nIconBd  |  int  |  图标边框大小  |
|  m_nIconBk  |  color  |  图标背景颜色  |
|  m_nLineNum  |  int  |  获取总行数  |
|  m_nLineHeight  |  int  |  获取行高  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void ClearAll()`  |  清空所有文本内容  |
|  `void RegAsTrOut(int bdef=1)`  |  注册为调试输出对象，参数：bdef-是否默认输出对象  |
|  `void AddMsg(string pline)`  |  添加一条消息，参数：pline-消息内容  |
|  `void AddErr(string pline)`  |  添加一条错误消息，参数：pline-错误消息内容  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名，w-宽度，h-高度，weight-粗细，bItalic-斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-宽度，h-高度  |
|  `bool Load(string pfilename)`  |  加载文件内容，参数：pfilename-文件名，返回：是否加载成功  |
|  `bool Save(string pfilename,int mode=0)`  |  保存文件内容，参数：pfilename-文件名，mode-保存模式，返回：是否保存成功  |
|  `int AddLine(string pline,int color=0,int icon=0,var pMsg=NULL)`  |  添加一行文本，参数：pline-文本内容，color-颜色，icon-图标，pMsg-附加信息，返回：添加的行号  |
|  `bool DelLine(int lineno,int num=1)`  |  删除指定行，参数：lineno-起始行号，num-删除行数，返回：是否删除成功  |
|  `bool InsertLine(int lineno,string pline,int color=0)`  |  插入一行，参数：lineno-行号，pline-文本内容，color-颜色，返回：是否插入成功  |
|  `string GetLine(int lineno)`  |  获取指定行的文本内容，参数：lineno-行号，返回：行文本  |
|  `bool SetLine(int lineno,string pstr)`  |  设置指定行的文本内容，参数：lineno-行号，pstr-文本内容，返回：是否设置成功  |
|  `var GetLineMsg(int lineno)`  |  获取行附加信息，参数：lineno-行号，返回：附加信息  |
|  `bool SetLineMsg(int lineno,var v)`  |  设置行附加信息，参数：lineno-行号，v-附加信息，返回：是否设置成功  |
|  `int GetLineIcon(int lineno)`  |  获取行图标，参数：lineno-行号，返回：图标值  |
|  `bool SetLineIcon(int lineno,int icon)`  |  设置行图标，参数：lineno-行号，icon-图标值，返回：是否设置成功  |
|  `int GetLineColor(int lineno)`  |  获取行颜色，参数：lineno-行号，返回：颜色值  |
|  `bool SetLineColor(int lineno,color color)`  |  设置行颜色，参数：lineno-行号，color-颜色值，返回：是否设置成功  |
|  `bool GetPtLineNo(vec3 pt,int& lineno)`  |  从坐标获取行号，参数：pt-坐标点，lineno-接收行号的变量，返回：是否获取成功  |
|  `vec2 GetLinePt(int lineno)`  |  获取行坐标，参数：lineno-行号，返回：坐标点  |
|  `int MakeLineVisable(int lineno)`  |  使行可见，参数：lineno-行号，返回：是否成功  |
|  `void SetIcon(var nameorid,int w,int h)`  |  设置图标，参数：nameorid-图标名称或ID，w-宽度，h-高度  |
----
### GObjSyntaxEdit
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)/[GObjSyntaxEdit](#GObjSyntaxEdit)
**描述**:代码编辑文本框，提供语法高亮、代码折叠、智能缩进与自动补全，支持多种编程语言和自定义配色
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nCurLineNo  |  int  |  当前行号  |
|  m_nCurCol  |  int  |  当前列字符位置  |
|  m_nCursorX  |  int  |  光标X坐标  |
|  m_nCursorY  |  int  |  光标Y坐标  |
|  m_nLeftMargin  |  int  |  左边距像素值  |
|  m_nReadOnly  |  int  |  只读模式状态  |
|  m_nBkColor  |  int  |  背景颜色  |
|  m_nCursorColor  |  int  |  光标颜色  |
|  m_nLeftMarginColor  |  int  |  左边距颜色  |
|  m_nLineNumColor  |  int  |  行号颜色  |
|  m_CurLineBkColor  |  int  |  设置当前行背景颜色，参数：c-颜色值，返回：是否设置成功  |
|  m_SelectBkColor  |  int  |  设置选择区背景颜色，参数：c-颜色值，返回：是否设置成功  |
|  m_nIsModi  |  int  |  文档是否已修改  |
|  m_nLineNum  |  int  |  文档总行数  |
|  m_sTextCodeMode  |  string  |  文本编码模式  |
|  m_nHiWordColor  |  int  |    |
|  m_nHiShowKind  |  int  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void MakeCaretVisable(int outsize=0)`  |  使光标可见，确保当前光标位置在视图中可见，参数：外部边距大小  |
|  `void OnLBDown(int x, int y,int flag)`  |  处理鼠标左键按下事件，参数：x,y-坐标，flag-按键标志  |
|  `void OnLBUp(int x, int y,int flag)`  |  处理鼠标左键抬起事件，参数：x,y-坐标，flag-按键标志  |
|  `void OnLBDClick(int x,int y,int flag)`  |  处理鼠标左键双击事件，参数：x,y-坐标，flag-按键标志  |
|  `void OnMouseMove(int x,int y,int flag)`  |  处理鼠标移动事件，参数：x,y-坐标，flag-按键标志  |
|  `void OnKeyDown(int key,int keydata)`  |  处理键盘按键事件，参数：key-键值，keydata-按键标志  |
|  `void OnKeyChar(string pstr,int bmark)`  |  处理键盘字符输入事件，参数：pstr-字符，bmark-标记  |
|  `vec2 GetLineCharPos(int line,int index)`  |  获取行字符位置，参数：line-行号，index-字符索引，返回：位置坐标  |
|  `int GetLineHeight()`  |  获取行高，返回：行高像素值  |
|  `int GetCharIndexOfTxt(int line,int col)`  |  获取文本中字符的索引，参数：line-行号，col-列位置，返回：字符索引  |
|  `void MoveCursor(int dx,int dy)`  |  移动光标，参数：dx-水平移动距离，dy-垂直移动距离  |
|  `bool SelectText(int x1,int y1,int x2,int y2)`  |  选择文本，参数：x1,y1-起始位置，x2,y2-结束位置，返回：是否选择成功  |
|  `string GetSelectText()`  |  获取选中的文本，返回：选中的文本内容  |
|  `string GetWord(int line,int col)`  |  获取单词，参数：line-行号，col-列位置，返回：单词内容  |
|  `var GetWordDef(int line,int col)`  |  获取单词定义，参数：line-行号，col-列位置，返回：单词定义信息  |
|  `bool DeleteSelect()`  |  删除选中的文本，返回：是否删除成功  |
|  `void SelectAll()`  |  全选文本  |
|  `int GetSelectColStart()`  |  获取选择区域的起始列位置  |
|  `int GetSelectColEnd()`  |  获取选择区域的结束列位置  |
|  `int GetSelectLineNum()`  |  获取选择的行数，返回：选中的行数  |
|  `bool CopySelectToClipBoard()`  |  复制选中文本到剪贴板，返回：是否复制成功  |
|  `void InsertText(string ptext,int bsel=0)`  |  插入文本，参数：ptext-文本内容，bsel-是否选中  |
|  `bool GoToLine(int lineno,int x=-1)`  |  跳转到指定行，参数：lineno-行号，x-列位置，返回：是否跳转成功  |
|  `int GetLineIcon(int lineno)`  |  获取行图标，参数：lineno-行号，返回：图标值  |
|  `bool SetLineIcon(int lineno,int icon)`  |  设置行图标，参数：lineno-行号，icon-图标值，返回：是否设置成功  |
|  `bool TagLineIcon(int lineno,int iconmask)`  |  标记行图标，参数：lineno-行号，iconmask-图标掩码，返回：是否标记成功  |
|  `int GetLineHide(int lineno)`  |  获取行隐藏状态，参数：lineno-行号，返回：隐藏状态  |
|  `int GetLineExpStatus(int lineno)`  |  获取行展开状态，参数：lineno-行号，返回：展开状态  |
|  `int GetLineWidth(int lineno)`  |  获取行宽度，参数：lineno-行号，返回：行宽度  |
|  `bool TagLineHide(vec3 pt,int mode=0)`  |  在指定位置标记行隐藏状态，参数：pt-位置坐标，mode-模式，返回：是否标记成功  |
|  `bool HideAllLine(int level)`  |  根据级别隐藏所有行，参数：level-级别，返回：是否隐藏成功  |
|  `var GetLineIconMaskSz(int iconmask)`  |  获取带有特定图标掩码的行索引，参数：iconmask-图标掩码，返回：行索引数组  |
|  `string GetFileName()`  |  获取文件名，返回：文件名  |
|  `bool Load(string pfilename)`  |  加载文件，参数：pfilename-文件名，返回：是否加载成功  |
|  `void LoadEx(string ptrinfo)`  |  从信息字符串加载，参数：ptrinfo-信息字符串  |
|  `bool Save(string pfilename=NULL)`  |  保存文件，参数：pfilename-文件名，返回：是否保存成功  |
|  `void Active()`  |  激活编辑器  |
|  `void OnKeyFocus(int act)`  |  处理键盘焦点事件，参数：act-是否激活  |
|  `void SetText(string pstr)`  |  设置文本内容，参数：pstr-文本内容  |
|  `bool GetText(string &str)`  |  获取文本内容，参数：str-接收文本的变量，返回：是否获取成功  |
|  `void LoadSyntax(string pstxname)`  |  加载语法定义文件，参数：pstxname-语法文件名  |
|  `void SetTextColor(color c,string pstxname=NULL)`  |  设置文本颜色，参数：c-颜色值，pstxname-语法名称  |
|  `int GetTextColor(string pstxname=NULL)`  |  获取文本颜色，参数：pstxname-语法名称，返回：颜色值  |
|  `var GetColorTab()`  |  获取颜色表，返回：颜色表数据  |
|  `void SetColorTab(var v)`  |  设置颜色表，参数：v-颜色表数据  |
|  `string GetLine(int i)`  |  获取指定行的文本内容，参数：i-行号，返回：行文本  |
|  `bool SetLine(int i,string pstr)`  |  设置指定行的文本内容，参数：i-行号，pstr-文本内容，返回：是否设置成功  |
|  `bool SetLineBkColor(int i,int color)`  |  设置行背景颜色，参数：i-行号，color-颜色值，返回：是否设置成功  |
|  `bool SetLineTips(int i,string pstr)`  |  设置行提示信息，参数：i-行号，pstr-提示文本，返回：是否设置成功  |
|  `bool AddLine(string pstr)`  |  添加新行，参数：pstr-行文本，返回：是否添加成功  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名，w-宽度，h-高度，weight-粗细，bItalic-斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-宽度，h-高度  |
|  `bool GetPtLineNo(vec3 pt,int& lineno)`  |  从坐标点获取行号，参数：pt-坐标点，lineno-接收行号的变量，返回：是否获取成功  |
|  `bool GetPtLineNoCol(vec3 pt,int& lineno,int &col)`  |  从坐标点获取行列号，参数：pt-坐标点，lineno-接收行号的变量，col-接收列号的变量，返回：是否获取成功  |
|  `vec2 GetLinePt(int lineno,int col=0)`  |  获取行坐标点，参数：lineno-行号，col-列号，返回：坐标点  |
|  `int MakeLineVisable(int lineno,int col=0)`  |  使行可见，参数：lineno-行号，col-列号，返回：是否成功  |
|  `void SetCurChgEmit(strid id)`  |  设置光标变化事件，参数：id-事件ID  |
|  `bool GetLineWordSz(int lineno,int col,var& wordsz,int &colno)`  |  获取行单词列表，参数：lineno-行号，col-列号，wordsz-单词列表，colno-列号，返回：是否获取成功  |
|  `void SetCurPos(int x,int y)`  |  设置光标位置，参数：x-横坐标，y-纵坐标  |
|  `void SetCurSelect(int bclear=1)`  |  设置光标选择状态，参数：bclear-是否清除选择  |
|  `bool IfCurInSelect(int blinecheck=1)`  |  检查光标是否在选择区内，参数：blinecheck-是否检查行，返回：是否在选择区内  |
|  `bool MoveSelectToCur(int bcopy=0)`  |  将选择区移动到光标位置，参数：bcopy-是否复制，返回：是否移动成功  |
|  `void SetHiWord(string s,int kind=0)`  |    |
|  `void SetAutoFitSize(int bfit)`  |    |
----
### GObjSheet
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)/[GObjSheet](#GObjSheet)
**描述**:表格控件类，提供灵活的行列数据管理和显示，支持单元格编辑、样式设置和多种类型数据展示
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nColNum  |  int  |  列数  |
|  m_nLineNum  |  int  |  行数  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool SetItemStyle(var stylename)`  |  设置表格项目样式，参数：stylename-样式名称，返回：是否设置成功  |
|  `void ResetSheet()`  |  重置表格  |
|  `void CreateSheet(int w,int h=0,int defw=0,int deflineh=0)`  |  创建表格，参数：w-列数，h-行数，defw-默认列宽，deflineh-默认行高  |
|  `void SetDefLineH(int deflineh)`  |  设置默认行高，参数：deflineh-默认行高  |
|  `void ReCalAllPos()`  |  重新计算所有位置  |
|  `bool SetColAlign(int col,int a)`  |  设置列对齐方式，参数：col-列索引，a-对齐方式，返回：是否设置成功  |
|  `int GetColNo(int xpos)`  |  获取坐标对应的列索引，参数：xpos-X坐标，返回：列索引  |
|  `int GetLineNo(int ypos)`  |  获取坐标对应的行索引，参数：ypos-Y坐标，返回：行索引  |
|  `int GetPtColKind(vec2 pt,int &x,int &y,int kind=0)`  |  获取坐标对应的单元格位置和类型，参数：pt-坐标，x,y-返回的列行索引，kind-查找类型，返回：单元格类型  |
|  `string GetColVarName(int x,int y)`  |  获取单元格变量名，参数：x-列索引，y-行索引，返回：变量名  |
|  `bool GetVarNameCol(string pname,int &x,int &y)`  |  获取变量名对应的单元格位置，参数：pname-变量名，x,y-返回的列行索引，返回：是否找到  |
|  `bool SetItem(int x,int y,var data)`  |  设置单元格数据，参数：x-列索引，y-行索引，data-数据，返回：是否设置成功  |
|  `bool GetItem(int x,int y,var& data)`  |  获取单元格数据，参数：x-列索引，y-行索引，data-返回的数据，返回：是否获取成功  |
|  `obj GetItemObj(int x,int y,int bcreate=0)`  |  获取单元格对象，参数：x-列索引，y-行索引，bcreate-是否创建，返回：单元格对象  |
|  `var GetItemObjSz(int x1,int y1,int x2,int y2,int bcreate=0)`  |  获取区域单元格对象集合，参数：x1,y1-起始位置，x2,y2-结束位置，bcreate-是否创建，返回：对象数组  |
|  `var GetItemVarNameLink(strid varid)`  |  获取变量名关联的单元格集合，参数：varid-变量名ID，返回：关联单元格数组  |
|  `var GetColCreateData(int x)`  |  获取列创建数据，参数：x-列索引，返回：创建数据  |
|  `bool SetColCreateData(int x,var agv)`  |  设置列创建数据，参数：x-列索引，agv-创建数据，返回：是否设置成功  |
|  `int GetColXpos(int col)`  |  获取列X坐标，参数：col-列索引，返回：X坐标  |
|  `int GetColWidth(int col)`  |  获取列宽度，参数：col-列索引，返回：列宽度  |
|  `var GetColDef(int x,int nameid=0,var pdef=NULL)`  |  获取列定义，参数：x-列索引，nameid-属性名ID，pdef-默认值，返回：列定义  |
|  `bool SetColDef(int col,strid nameid,var val)`  |  设置列定义，参数：col-列索引，nameid-属性名ID，val-属性值，返回：是否设置成功  |
|  `bool SetColWidth(int x,int w)`  |  设置列宽度，参数：x-列索引，w-宽度，返回：是否设置成功  |
|  `void InsertCol(int col,var pcolcreatedat=NULL)`  |  插入列，参数：col-插入位置，pcolcreatedat-列创建数据  |
|  `bool DelCol(int col)`  |  删除列，参数：col-列索引，返回：是否删除成功  |
|  `int GetLineHeight(int y)`  |  获取行高度，参数：y-行索引，返回：行高度  |
|  `bool SetLineHeight(int y,int h)`  |  设置行高度，参数：y-行索引，h-高度，返回：是否设置成功  |
|  `bool GetItemRect(int x,int y,vec4& rect)`  |  获取单元格矩形区域，参数：x-列索引，y-行索引，rect-返回的矩形区域，返回：是否获取成功  |
|  `bool GetLineCreateData(int y,var& ret)`  |  获取行创建数据，参数：y-行索引，ret-返回的创建数据，返回：是否获取成功  |
|  `bool SetLineCreateData(int y,var agv)`  |  设置行创建数据，参数：y-行索引，agv-创建数据，返回：是否设置成功  |
|  `bool GetLineData(int y,var& dat,var& editret)`  |  获取行数据，参数：y-行索引，dat-返回的数据，editret-编辑结果，返回：是否获取成功  |
|  `bool SetLineData(int y,var dat,var editret)`  |  设置行数据，参数：y-行索引，dat-数据，editret-编辑结果，返回：是否设置成功  |
|  `bool InsertLine(int y,int addnum=1)`  |  插入行，参数：y-插入位置，addnum-添加数量，返回：是否插入成功  |
|  `bool DelLine(int y,int count=1)`  |  删除行，参数：y-行索引，count-删除数量，返回：是否删除成功  |
|  `bool SetSheetColor(int index,color c)`  |  设置表格颜色，参数：index-颜色索引，c-颜色值，返回：是否设置成功  |
|  `int GetSheetColor(int index)`  |  获取表格颜色，参数：index-颜色索引，返回：颜色值  |
----
### GObjSheetItem
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjSheetItem](#GObjSheetItem)
**描述**:表格单元格类，实现表格中单个数据项的显示与交互，支持多种数据类型和显示样式
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vShapeEx  |  var  |  形状扩展属性  |
|  m_nX  |  int  |  列索引  |
|  m_nY  |  int  |  行索引  |
|  m_nAlgin  |  int  |  对齐方式  |
|  m_vData  |  var  |  数据值  |
|  m_vEditData  |  var  |  编辑数据  |
|  m_sText  |  string  |  文本内容  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetData(var data)`  |  设置数据，参数：data-数据值  |
|  `void GetData(var& data)`  |  获取数据，参数：data-返回的数据值  |
|  `void SetDataEdit(var data,var editdata)`  |  设置数据和编辑数据，参数：data-数据值，editdata-编辑数据  |
|  `void DestroyData(int onlyedit=0)`  |  销毁数据，参数：onlyedit-是否只销毁编辑数据(0:全部，1:只编辑数据)  |
|  `bool GetCreateData(var& v,int onlyedit=0)`  |  获取创建数据，参数：v-返回的创建数据，onlyedit-是否只获取编辑数据，返回：是否获取成功  |
|  `bool SetCreateData(var v,int onlyedit=0)`  |  设置创建数据，参数：v-创建数据，onlyedit-是否只设置编辑数据，返回：是否设置成功  |
|  `void SetItemColor(int index,color c)`  |  设置项目颜色，参数：index-颜色索引，c-颜色值  |
|  `int GetItemColor(int index)`  |  获取项目颜色，参数：index-颜色索引，返回：颜色值  |
|  `void SetItemAlgin(int mode)`  |  设置项目对齐方式，参数：mode-对齐模式  |
|  `void SetText(string ptext)`  |  设置文本内容，参数：ptext-文本字符串  |
|  `void OnTouch(var& dn)`  |    |
|  `var GetColDef(strid nameid,var pdef=NULL)`  |  获取列定义，参数：nameid-属性名ID，pdef-默认值，返回：列定义  |
----
### GObjLook
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjShape](#GObjShape)/[GObjLook](#GObjLook)
**描述**:观察框对象类，提供对其他显示对象的观察和代理显示功能，支持坐标变换、触摸事件转发和独立显示标志设置
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pLook  |  obj  |  观察对象指针  |
|  m_nLookFlag  |  int  |  观察标志位  |
|  m_vLookOff  |  vec3  |  观察对象偏移量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool SetLook(obj pobj)`  |  设置观察对象，参数：pobj-对象指针，返回：是否设置成功  |
|  `void SetLookFlag(int flag,int bset=1)`  |  设置观察标志，参数：flag-标志位，bset-是否设置(1:设置，0:清除)  |
|  `bool IsLookFlag(int flag)const`  |  检查观察标志，参数：flag-标志位，返回：标志是否有效  |
|  `void SetDirectFlag(strid dshowflag)`  |  设置直接显示标志，参数：dshowflag-显示标志ID  |
----
### GObjSndStream
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjSndStream](#GObjSndStream)
**描述**:音频流处理类，提供音频录制和播放功能，支持网络音频数据传输
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nFrameSize  |  int  |  音频帧大小，单位为字节  |
|  m_nSamplesPerSec  |  int  |  音频采样率，单位为Hz  |
|  m_nBytePerSample  |  int  |  每个采样的字节数，用于确定音频精度  |
|  m_nClns  |  int  |  音频通道数，1为单声道，2为立体声  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool OpenOutStream()`  |  打开音频输出流，初始化音频播放设备，返回：是否成功创建  |
|  `bool CloseOutStream()`  |  关闭音频输出流，释放音频播放设备资源  |
|  `void OutData(var bindata)`  |  输出音频数据，将二进制音频数据发送到输出设备  |
|  `bool OpenRecStream(int recmode=0)`  |  打开音频录制流，初始化麦克风设备，recmode指定录制模式  |
|  `bool CloseRecStream()`  |  关闭音频录制流，停止麦克风录制并释放资源  |
|  `bool SetUdpSender(obj pudp,int ip,int port)`  |  设置UDP发送器，用于将音频数据通过网络发送  |
----
### GWaveFFTShow
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GWaveFFTShow](#GWaveFFTShow)
**描述**:这个类实现了音频FFT频谱显示控件，用于对音频数据进行傅里叶变换分析并以可视化方式呈现频谱，支持实时波形分析和频带显示
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Init(int SampleSize=512,int bound=48)`  |  初始化FFT显示，设置采样大小和频带数量  |
|  `void OnWavData(var bindata)`  |  处理波形数据，进行FFT分析和显示  |
----
### GObjSndView
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjView](#GObjView)/[GObjSndView](#GObjSndView)
**描述**:这个类实现了音频可视化视图控件，用于显示和播放音频波形，支持音频文件加载、波形渲染、音量控制和选区播放
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nShowSampleScale  |  int  |  获取采样显示比例，控制波形水平压缩程度  |
|  m_nSndLenMs  |  int  |  获取音频总时长，单位为毫秒  |
|  m_fVScale  |  float  |  获取波形垂直缩放比例，控制波形显示高度  |
|  m_sInfo  |  string  |  获取音频信息字符串，包含采样率、位深度等信息  |
|  m_fVal  |  float  |  获取音量值，范围0-100  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool LoadFile(string pname)`  |  加载音频文件，从指定路径读取音频数据  |
|  `void SelectInViewPos(int sx,int endx)`  |  在视图中选择音频片段，传入起始和结束位置  |
|  `void PlaySnd()`  |  播放整个音频文件  |
|  `void PlaySel()`  |  播放已选择的音频片段  |
|  `void AutoScale()`  |  自动调整波形显示比例，根据音频数据自适应缩放  |
|  `bool CreateData(int hz=8000,int bitpersmaple=2,int chls=1)`  |  创建音频数据，指定采样率、位深度和通道数  |
|  `void AddData(var bindata)`  |  添加音频数据，将二进制数据追加到当前音频buffer  |
|  `void SetVal(float n)`  |  设置音量值，控制音频播放音量  |
|  `bool SaveFile(string pname,int mode=0)`  |  保存音频文件，将当前音频数据保存到指定路径，mode指定格式  |
----
### GObjCamera
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObjCamera](#GObjCamera)
**描述**:3D相机类，用于控制3D场景的视角和渲染
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLookMode  |  int  |  相机观察模式：0-观察点模式，1-视点模式，-1-自由模式  |
|  m_nClearBk  |  int  |  是否清除背景  |
|  m_p3DTouchRoot  |  obj  |  3D触摸根节点  |
|  m_pLookAtObj  |  obj  |  观察目标对象  |
|  m_pShadowObj  |  obj  |  阴影对象  |
|  m_pDepObj  |  obj  |  深度对象  |
|  m_nLineColor  |  color  |  线条颜色  |
|  m_vEyePt  |  vec3  |  相机位置  |
|  m_vLookPt  |  vec3  |  观察点位置  |
|  m_fFov  |  float  |  视场角  |
|  m_fZn  |  float  |  近裁剪面距离  |
|  m_fZf  |  float  |  远裁剪面距离  |
|  m_fLookDis  |  float  |  观察距离  |
|  m_fRotoZ  |  float  |  绕Z轴旋转角度  |
|  m_fRotoY  |  float  |  绕Y轴旋转角度  |
|  m_fRoll  |  float  |  绕X轴旋转角度  |
|  m_vOffset  |  vec3  |  相机偏移量  |
|  m_vUpVec  |  vec3  |  上向量  |
|  m_vLookDir  |  vec3  |  观察方向  |
|  m_vLowVec  |  vec3  |  右向量  |
|  m_vCamera  |  var  |  相机参数  |
|  m_pWorld  |  obj  |  世界对象  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetRangeZ(float znear,float zfar)`  |  设置相机近远裁剪面，参数：znear-近裁剪面距离，zfar-远裁剪面距离  |
|  `void SetLookAt(vec3 pt)`  |  设置观察点，参数：pt-观察点坐标  |
|  `bool SetLookAtObj(obj p)`  |  设置观察目标对象，参数：p-目标对象，返回：是否设置成功  |
|  `bool SetWorld(obj pwd)`  |  设置世界对象，参数：pwd-世界对象，返回：是否设置成功  |
|  `bool GetPickLine(float x,float y,vec3& org,vec3& end)`  |  获取拾取射线，参数：x-屏幕X坐标，y-屏幕Y坐标，org-射线起点，end-射线终点，返回：是否成功  |
|  `bool GetPickDir(float x,float y,vec3& org,vec3& dir)`  |  获取拾取方向，参数：x-屏幕X坐标，y-屏幕Y坐标，org-射线起点，dir-射线方向，返回：是否成功  |
|  `bool GetPickPtOnPlane(float x,float y,vec3& pt,vec3 planepos,vec3 plandir)`  |  获取平面上的拾取点，参数：x-屏幕X坐标，y-屏幕Y坐标，pt-拾取点，planepos-平面位置，plandir-平面法向，返回：是否成功  |
|  `void UpdateFrustum()`  |  更新视锥体  |
|  `void OnTouch(var& dn)`  |  处理触摸事件，参数：dn-触摸数据  |
|  `void OnTouchWheel(float dz,vec3 pt,int ctrlkey,var extvar)`  |  处理鼠标滚轮事件，参数：dz-滚轮增量，pt-屏幕坐标，ctrlkey-控制键状态，extvar-扩展数据  |
|  `bool GetImg(var& imgdata,int w,int h,int scale=1,int bdcolor=0,int bdsize=0)`  |  获取相机截图，参数：imgdata-图像数据，w-宽度，h-高度，scale-缩放比例，bdcolor-边框颜色，bdsize-边框大小，返回：是否成功  |
|  `vec3 GetScreenPos(vec3 ptwd)`  |  获取世界坐标对应的屏幕坐标，参数：ptwd-世界坐标，返回：屏幕坐标  |
----
### GObj3DShow
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)
**描述**:3D对象显示基类，提供3D显示、世界坐标变换和渲染管理功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nZTest  |  int  |  Z测试状态，1表示启用，0表示禁用  |
|  m_nZWrite  |  int  |  Z写入状态，1表示启用，0表示禁用  |
|  m_nColorWrite  |  int  |  颜色写入状态，1表示启用，0表示禁用  |
|  m_nWireframe  |  int  |  线框模式状态，1表示启用，0表示禁用  |
|  m_nShowNormalLine  |  int  |  法线显示状态，1表示显示，0表示隐藏  |
|  m_nShowCullBox  |  int  |  裁剪盒显示状态，1表示显示，0表示隐藏  |
|  m_nShowCullBall  |  int  |  裁剪球显示状态，1表示显示，0表示隐藏  |
|  m_nDoubleface  |  int  |  双面渲染状态，1表示启用，0表示禁用  |
|  m_nNoLight  |  int  |  无光照状态，1表示无光照，0表示有光照  |
|  m_pWorld  |  obj  |  当前对象所属的3D世界指针  |
|  m_fScale  |  float  |  对象的统一缩放比例  |
|  m_vScale  |  vec3  |  对象的非统一缩放向量(x,y,z)  |
|  m_vRoto  |  vec4  |  对象的旋转四元数  |
|  m_vWorldMatrix  |  mat4  |  对象的世界变换矩阵  |
|  m_fForward  |  float  |  设置对象的前进方向，参数：f-Z轴旋转角度(度)，返回：成功为true  |
|  m_nHitFlag  |  int  |  碰撞检测标志  |
|  m_nCollisionID  |  int  |  地形碰撞ID  |
|  m_vMatToWorld  |  var  |  对象的世界变换矩阵  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetWireframe(int b)`  |  设置线框模式，参数：b-1启用/0禁用  |
|  `void CanShadow(int bcan)`  |  设置对象是否能投射阴影，参数：bcan-1能投射/0不能投射  |
|  `void OnShadow(int bon)`  |  设置对象是否接收阴影，参数：bon-1接收/0不接收  |
|  `void OnSnow(int bcan)`  |  设置对象是否接收雪，参数：bcan-1接收/0不接收  |
|  `bool GetCullBoxMinMax(vec3& min, vec3& max)`  |  获取裁剪盒的最小和最大边界，参数：min-最小边界，max-最大边界，返回：成功为true  |
|  `vec3 PtWorld2Loc(vec3 point)`  |  将世界坐标点转换为局部坐标，参数：point-世界坐标点，返回：局部坐标点  |
|  `vec3 PtLoc2World(vec3 point)`  |  将局部坐标点转换为世界坐标，参数：point-局部坐标点，返回：世界坐标点  |
|  `vec3 DirWorld2Loc(vec3 dir)`  |  将世界方向向量转换为局部方向，参数：dir-世界方向向量，返回：局部方向向量  |
|  `vec3 DirLoc2World(vec3 dir)`  |  将局部方向向量转换为世界方向，参数：dir-局部方向向量，返回：世界方向向量  |
|  `void Roto(vec4 q)`  |  对对象应用额外旋转，参数：q-旋转四元数  |
|  `void RotoX(float degree)`  |  绕X轴旋转对象，参数：degree-旋转角度(度)  |
|  `void RotoY(float degree)`  |  绕Y轴旋转对象，参数：degree-旋转角度(度)  |
|  `void RotoZ(float degree)`  |  绕Z轴旋转对象，参数：degree-旋转角度(度)  |
|  `void SetForward(float degree)`  |  设置对象的前进方向，参数：degree-Z轴旋转角度(度)  |
|  `void SetCollisionID(int id)`  |  设置地形碰撞ID，参数：id-碰撞ID  |
|  `int GetWorldStandPos(vec3& v,float upmax=1)`  |  获取对象下方的地形位置，参数：v-返回位置，upmax-最大向上检测距离，返回：状态码  |
|  `var GetMatToWorld()`  |  获取对象的世界变换矩阵，返回：矩阵变量  |
----
### GObj3DWorld
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DWorld](#GObj3DWorld)
**描述**:3D世界对象，管理场景中的3D对象、碰撞检测和光照效果
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLightWorld  |  int  |  光照世界标志  |
|  m_fAniSpeed  |  float  |  动画播放速度  |
|  m_fSnowLevel  |  float  |  雪地覆盖等级  |
|  m_nShowCollision  |  int  |  获取碰撞显示模式  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetSnowTexeure(var nameorid)`  |  设置雪地纹理，参数：nameorid-纹理名或ID  |
|  `void SetSelTexeure(var nameorid)`  |  设置选择区域纹理，参数：nameorid-纹理名或ID  |
|  `void SetCollisionTexeure(var nameorid)`  |  设置碰撞纹理，参数：nameorid-纹理名或ID  |
|  `var GetShpereHit(vec3 pos,float r,int hitmask,int crossmode=0)`  |  获取球体碰撞检测结果，参数：pos-球心位置，r-球半径，hitmask-碰撞掩码，crossmode-碰撞模式，返回：碰撞的对象  |
|  `void SetShowCollision(int mode)`  |  设置碰撞显示模式，参数：mode-显示模式(0-3)  |
|  `void RefCollision(float x0,float y0,float x1,float y1)`  |  刷新指定区域的碰撞信息，参数：x0,y0,x1,y1-区域的边界坐标  |
|  `int GetCollisionStandPos(vec3& v,float upmax)`  |  获取碰撞后的站立位置，参数：v-位置向量(引用)，upmax-向上最大距离，返回：是否有碰撞(整数)  |
|  `var GetCollisionLineCross(vec3 org,vec3 end,int mode=0)`  |  获取线段碰撞检测结果，参数：org-起点，end-终点，mode-碰撞模式，返回：碰撞信息  |
|  `var GetCollisionInfo(vec3 p0,vec3 p1,var pmat4=NULL,int mode=0)`  |  获取碰撞详细信息，参数：p0-起点，p1-终点，pmat4-变换矩阵(可选)，mode-碰撞模式，返回：碰撞信息  |
----
### GObj3DLight
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DLight](#GObj3DLight)
**描述**:3D光照对象，用于管理场景中的光源效果
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fLight  |  float  |  光源强度  |
|  m_fAmbient  |  float  |  环境光强度  |
|  m_fPointLen  |  float  |  点光源半径  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetDirectional(float f)`  |  设置为平行光，参数：f-光照强度  |
|  `void SetLocPointLight(float r)`  |  设置为点光源，参数：r-光照半径  |
----
### GObj3DSkyBox
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DSkyBox](#GObj3DSkyBox)
**描述**:天空盒对象，用于渲染3D场景的背景天空
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nHalfText  |  int  |  半球模式标志  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetTexture(var texname,int bhalf=1)`  |  设置天空纹理，参数：texname-纹理名称或资源，bhalf-半球模式标志  |
----
### GObj3DShadowSSM
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DShadowSSM](#GObj3DShadowSSM)
**描述**:阴影贴图渲染类，使用分割空间映射(SSM)技术实现3D场景动态阴影效果
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fFov  |  float  |  阴影光源视场角  |
|  m_fMaxDis  |  float  |  阴影最大渲染距离  |
|  m_fDepthBias  |  float  |  深度偏移值，用于避免阴影痤疮  |
|  m_fLightDis  |  float  |  光源距离  |
|  m_fT0  |  float  |  分割空间映射参数T0  |
|  m_fT1  |  float  |  分割空间映射参数T1  |
|  m_fT2  |  float  |  分割空间映射参数T2  |
|  m_fT3  |  float  |  分割空间映射参数T3  |
|  m_nTextLevel  |  int  |  阴影贴图纹理级别  |
|  m_nUseColorMap  |  int  |  是否使用颜色图  |
|  m_nEnable  |  int  |  是否启用阴影效果  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetTextLevel(int level)`  |  设置阴影贴图纹理级别，参数：level-级别(0=256,1=512,2=1024,3=2048等)  |
----
### GObj3DWater
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DWater](#GObj3DWater)
**描述**:3D水体对象，用于渲染水面效果及其反射、折射
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLinkLookAt  |  int  |  视点关联  |
|  m_nReflectMap  |  int  |  是否反射  |
|  m_fRefractBias  |  float  |  反射比例  |
|  m_fRefractPower  |  float  |  高光指数  |
|  m_fLookDepth  |  float  |  透视距离  |
|  m_fZscale  |  float  |  起伏比例  |
|  m_fTextrueScaleX  |  float  |  纹理X轴缩放系数  |
|  m_fTextrueScaleY  |  float  |  纹理Y轴缩放系数  |
|  m_fWaveSpeed  |  float  |  波浪移动速度  |
|  m_fWaveSpeedZ  |  float  |  波浪高度变化速度  |
|  m_fLightChgSpeed  |  float  |  光照变化速度  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void InitWater(var waterbump1name,var waterbump2name)`  |  初始化水体，参数：waterbump1name-第一张水波纹理，waterbump2name-第二张水波纹理  |
|  `bool SetTexture(int no,var imgname)`  |  设置水面纹理，参数：no-纹理索引，imgname-纹理名称，返回：是否设置成功  |
|  `void SetRefract(float refractBias,float refractPower)`  |  设置折射参数，参数：refractBias-折射比例，refractPower-高光指数  |
|  `void SetSize(float w,float h)`  |  设置水面大小，参数：w-宽度，h-高度  |
|  `float GetWidth()`  |  获取水面宽度，返回：宽度值  |
|  `float GetHeight()`  |  获取水面高度，返回：高度值  |
|  `void LoadLightImg(int no,var filename)`  |  加载光照贴图，参数：no-贴图索引，filename-贴图文件名  |
----
### GObj3DGuid
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DGuid](#GObj3DGuid)
**描述**:3D网格导航类，用于创建和管理3D场景中的网格导航系统
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nLineColor  |  color  |    |
|  m_nSubW  |  int  |  网格单元宽度  |
|  m_nSubH  |  int  |  网格单元高度  |
|  m_bTitle45  |  int  |  网格是否使用45度倾斜显示  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetImgSz(var var)`  |  设置网格使用的图像资源，参数：var-图像资源变量  |
|  `void Create(int xnum,int ynum,int subw=32,int subh=32)`  |  创建网格导航系统，参数：xnum-横向网格数，ynum-纵向网格数，subw-网格单元宽度，subh-网格单元高度  |
|  `bool SetGuidImg(int x,int y,int imgno,int f)`  |  设置网格单元图像，参数：x-横向位置，y-纵向位置，imgno-图像编号，f-帧号，返回：是否设置成功  |
|  `var GetGuidImg(int x,int y)`  |  获取网格单元图像信息，参数：x-横向位置，y-纵向位置，返回：包含图像编号和帧号的变量  |
|  `vec3 GetGuidPos(int x,int y,int btrans=1)`  |  获取网格单元位置，参数：x-横向位置，y-纵向位置，btrans-是否进行坐标转换，返回：网格单元中心点坐标  |
|  `void Clean()`  |  清除所有网格数据  |
|  `bool TestLineCallBack(vec3 start,vec3 end,float linew)`  |  测试线段与网格的碰撞，参数：start-线段起点，end-线段终点，linew-线段宽度，返回：是否发生碰撞  |
----
### GObj3DCamera
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DCamera](#GObj3DCamera)
**描述**:3D相机视锥体类，用于可视化和控制3D相机视锥体
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vCamera  |  var  |  相机参数，包含视锥体信息、视点、视向和上向量  |
----
### GObj3DBlkMaker
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DBlkMaker](#GObj3DBlkMaker)
**描述**:3D区块生成器对象，用于创建和显示网格区块
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nShowTrMode  |  int  |  显示模式，控制区块的三角形显示方式  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void CreateBuf(int w,int h,int subnum=2)`  |  创建缓冲区，参数：w-宽度，h-高度，subnum-子区块数量  |
----
### GObj3DAni
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DAni](#GObj3DAni)
**描述**:3D动画对象，用于管理和播放3D模型动画
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_p3DAni  |  ptrex  |  获取动画对象指针  |
|  m_fAniTime  |  float  |  获取当前动画时间  |
|  m_fAniSpeed  |  float  |  获取动画播放速度  |
|  m_nAniID  |  int  |  获取当前动画ID  |
|  m_bPlay  |  int  |  获取动画播放状态  |
|  m_vCullSphere  |  vec4  |  获取包围球  |
|  m_nBaseCircleColor  |  color  |  选择圆颜色  |
|  m_fBaseCircleR  |  float  |  底部圆半径  |
|  m_vOutlineColor  |  vec4  |  轮廓线颜色vec4  |
|  m_nOutlineColor  |  color  |  轮廓线颜色  |
|  m_fOutLineWidth  |  float  |  轮廓线大小  |
|  m_nOutlineAlways  |  int  |  是否outline穿透  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(var name)`  |  加载动画模型，参数：name-模型资源名称，返回：是否加载成功  |
|  `void OnAniReady()`  |  动画准备就绪回调函数  |
|  `void AddReadNoti(obj pobj,strid callfunid)`  |  添加动画加载就绪通知，参数：pobj-通知对象，callfunid-回调函数ID  |
|  `void AddAniNoti(obj pobj,strid callfunid)`  |  添加动画变化通知，参数：pobj-通知对象，callfunid-回调函数ID  |
|  `var CreateAni()`  |  创建动画对象，返回：包含动画对象指针的变量  |
|  `bool IsAniReady()`  |  检查动画是否就绪，返回：动画是否准备好  |
|  `void SetAniKind(strid aniid)`  |  设置动画类型，参数：aniid-动画ID  |
|  `void PlayAni(strid aniid,float st=0)`  |  播放动画，参数：aniid-动画ID，st-开始时间  |
|  `void PlayAniRet(strid aniid,float speed=0,strid endfunid=0)`  |  播放动画并设置结束回调，参数：aniid-动画ID，speed-播放速度，endfunid-结束回调函数ID  |
|  `void SetPlay(int bplay=1)`  |  设置动画播放状态，参数：bplay-是否播放(1播放，0暂停)  |
|  `void LinkTag(strid tagnameid)`  |  连接到标签，参数：tagnameid-标签名ID  |
|  `bool GetTagMat4(strid tagnameid,var& mat4)`  |  获取标签矩阵，参数：tagnameid-标签名ID，mat4-矩阵变量(引用)，返回：是否获取成功  |
|  `int ResetPart()`  |  重置所有部件，返回：操作结果代码  |
|  `int SetPart(strid partname,var loadid,strid tagnameid=0,int badd=0)`  |  设置部件，参数：partname-部件名，loadid-加载资源ID，tagnameid-标签名ID，badd-是否添加，返回：操作结果代码  |
|  `int DelPart(strid partname)`  |  删除部件，参数：partname-部件名，返回：操作结果代码  |
|  `bool SetPartMaterial(strid partname,strid paramid,var val)`  |  设置部件材质，参数：partname-部件名，paramid-参数ID，val-参数值，返回：是否设置成功  |
----
### GObj3DCharacter
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DAni](#GObj3DAni)/[GObj3DCharacter](#GObj3DCharacter)
**描述**:3D角色对象，提供角色动作控制、路径行走和跳跃功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fObjRotoZ  |  float  |  对象Z轴旋转角度  |
|  m_fManHeight  |  float  |  角色高度  |
|  m_fUpH  |  float  |  角色上半身高度  |
|  m_fManR  |  float  |  角色半径  |
|  m_vActMap  |  var  |  动作映射表  |
|  m_nShowPathColor  |  color  |  路径显示颜色  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool WalkTo(vec3 topos,float speed,float nearr=0)`  |  行走到指定位置，参数：topos-目标位置，speed-行走速度，nearr-到达距离，返回：是否成功  |
|  `bool WalkAngle(float angle,float speed)`  |  按角度行走，参数：angle-行走角度，speed-行走速度，返回：是否成功  |
|  `bool ToIdel()`  |  切换到空闲状态，返回：是否成功  |
|  `bool IsMove()`  |  是否正在移动，返回：移动状态  |
|  `bool Jump(float speed,float g=-9.8f)`  |  跳跃，参数：speed-跳跃速度，g-重力加速度，返回：跳跃是否成功  |
----
### GObj3DAniMove
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DAni](#GObj3DAni)/[GObj3DAniMove](#GObj3DAniMove)
**描述**:3D动画移动对象，提供角色移动、路径跟随和碰撞检测功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vActMap  |  var  |  动作映射表  |
|  m_bFlying  |  int  |  飞行状态  |
|  m_bOnGround  |  int  |  地面状态  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void InitBlock(float r,float h,float mt=1.0f)`  |  初始化碰撞块，参数：r-半径，h-高度，mt-重量  |
|  `void WalkAngle(float f,float wspeed,float ry=0.0f)`  |  按角度行走，参数：f-行走角度，wspeed-行走速度，ry-Y轴旋转角度  |
|  `bool ToIdel()`  |  切换到空闲状态，返回：成功为true  |
|  `void StopWalk()`  |  停止行走  |
|  `void LockStatus(int block=1)`  |  锁定状态，参数：block-锁定标志  |
|  `bool Jump(float speed,int bforce=0)`  |  跳跃，参数：speed-跳跃速度，bforce-强制跳跃标志，返回：跳跃是否成功  |
|  `void GetMoveAgv(var& agv)`  |  获取移动参数，参数：agv-返回的参数变量  |
|  `bool SetMoveAgv(var agv)`  |  设置移动参数，参数：agv-参数变量，返回：设置是否成功  |
|  `int GetStatus()`  |  获取当前状态ID，返回：状态ID  |
|  `string GetStatusName()`  |  获取当前状态名称，返回：状态名称字符串  |
|  `bool WalkTo(vec3 to,float speed,float fnear=1.0f,int testmax=6500)`  |  行走到指定位置，参数：to-目标位置，speed-行走速度，fnear-到达距离，testmax-测试最大步数，返回：成功为true  |
|  `bool RandGo(vec3 to,float speed)`  |  随机行走，参数：to-目标区域，speed-行走速度，返回：成功为true  |
|  `bool GetMovePath(var& ret)`  |  获取移动路径，参数：ret-返回的路径变量，返回：成功为true  |
|  `bool SetMovePath(var path,float speed)`  |  设置移动路径，参数：path-路径变量，speed-移动速度，返回：成功为true  |
----
### GObj3DHit
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DHit](#GObj3DHit)
**描述**:3D碰撞检测类，用于管理3D场景中的对象碰撞检测和事件触发
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Reset()`  |  重置所有碰撞检测数据  |
|  `void AddLink(obj pobj,float r,int flag=0,int mask=0,strid callback=0)`  |  添加碰撞检测对象，参数：pobj-目标对象，r-碰撞半径，flag-碰撞标志，mask-碰撞掩码，callback-回调函数ID  |
|  `void ClearLink(obj pobj)`  |  清除指定对象的碰撞检测，参数：pobj-要清除的目标对象  |
----
### GObj3DShape
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DShape](#GObj3DShape)
**描述**:3D基础形状对象类，用于在3D场景中创建和显示基本几何体
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetRenderLayer(int l)`  |  设置形状的渲染层级，参数：l-层级编号  |
|  `void Destroy()`  |  销毁当前形状对象  |
|  `void SetSphere(float r=1.0f,int level=0)`  |  设置为球体形状，参数：r-球体半径，level-细分级别  |
|  `void SetBox(float w=1.0f)`  |  设置为立方体形状，参数：w-边长大小  |
|  `void SetBoxEx(vec3 p1,vec3 p2)`  |  设置为自定义包围盒形状，参数：p1-最小点坐标，p2-最大点坐标  |
|  `void SetFace(float w=1.0f)`  |  设置为平面形状，参数：w-边长大小  |
|  `void SetTexture(var nameorid)`  |  设置形状的纹理，参数：nameorid-纹理名称或纹理ID  |
----
### GObj3DLine
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DLine](#GObj3DLine)
**描述**:3D线条绘制类，用于在3D场景中创建和显示线条、坐标轴和文本标注
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Reset()`  |  清空所有线条和文本数据  |
|  `void SetCullBox(vec3 pos1,vec3 pos2)`  |  设置裁剪包围盒，参数：pos1-最小点坐标，pos2-最大点坐标  |
|  `void AddLine(vec3 pos1,int color1,vec3 pos2,int color2)`  |  添加一条直线，参数：pos1-起点坐标，color1-起点颜色，pos2-终点坐标，color2-终点颜色  |
|  `void AddLineSz(vec3 pos1,int color1,vec3 pos2,int color2,int num,vec3 off)`  |  添加多条平行线段，参数：pos1-起点坐标，color1-起点颜色，pos2-终点坐标，color2-终点颜色，num-线条数量，off-偏移量  |
|  `void AddTr(vec3 p1,vec3 p2,vec3 p3,int c)`  |  添加一个三角形轮廓，参数：p1-点1坐标，p2-点2坐标，p3-点3坐标，c-颜色  |
|  `void AddDefCoordinate(float s=11,float dt=1,float sd=0.2f)`  |  添加标准3D坐标系，参数：s-坐标轴长度，dt-刻度间距，sd-刻度线长度  |
|  `void AddCoordinate(float s=10,float orgw=0.5)`  |  添加2D坐标系，参数：s-坐标轴长度，orgw-原点标记大小  |
|  `void AddBox(vec3 p1,vec3 p2,int color=0)`  |  添加线框盒子，参数：p1-最小点坐标，p2-最大点坐标，color-颜色  |
|  `void AddRect(float w,float h,int color=0)`  |  添加矩形轮廓，参数：w-宽度，h-高度，color-颜色  |
|  `var AddText(string ptext,vec3 p,color textc=0)`  |  添加3D文本标注，参数：ptext-文本内容，p-位置坐标，textc-文本颜色，返回：文本对象指针  |
|  `void DeleteText(int no=-1)`  |  删除文本标注，参数：no-文本序号，-1表示删除所有文本  |
----
### GObjMeshLod
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObjMeshLod](#GObjMeshLod)
**描述**:3D网格LOD优化类，用于自动简化网格模型并支持不同细节层次的显示
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nShowCost  |  int  |  是否显示边缘代价信息  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetTexture(var nameorid)`  |  设置网格纹理，参数：nameorid-纹理名称或ID  |
|  `bool ImportStl(string pname,float scale=1.0)`  |  从STL文件导入网格数据，参数：pname-文件名，scale-缩放比例，返回：成功返回true，失败返回false  |
|  `bool ImportRes(string pname,float scale=1.0)`  |  从资源文件导入网格数据，参数：pname-资源名，scale-缩放比例，返回：成功返回true，失败返回false  |
|  `void CleanData()`  |  清空所有网格数据  |
|  `void SetAddMat(int mat0,int mat1,int mat2)`  |  设置三角面的材质索引，参数：mat0-顶点0材质，mat1-顶点1材质，mat2-顶点2材质  |
|  `bool AddFace(vec3 p1,vec3 p2,vec3 p3)`  |  添加一个三角面，参数：p1-顶点1坐标，p2-顶点2坐标，p3-顶点3坐标，返回：成功返回true，失败返回false  |
|  `void EndAdd()`  |  结束添加，计算所有边缘折叠代价  |
|  `bool FindMinCost(float minlevel=0.5)`  |  查找具有最小代价的边，参数：minlevel-最小代价阈值，返回：找到返回true，否则返回false  |
|  `bool RemoveFindEdge()`  |  移除已找到的最小代价边，返回：成功返回true，失败返回false  |
|  `string GetInfo()`  |  获取当前网格信息，返回：包含面数、顶点数和已删除数量的字符串  |
----
### GMcWorldObj
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GMcWorldObj](#GMcWorldObj)
**描述**:MC世界对象，管理体素世界的创建、加载和编辑
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nAutoSaveDelay  |  int  |    |
|  m_vExtVid64  |  var  |  扩展视频数据  |
|  m_pTreeRoot  |  obj  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool CreateWorld(int dep,float subscale=1.0f)`  |  创建世界，参数：dep-深度，subscale-子区块缩放，返回：成功返回true  |
|  `bool SaveWorld()`  |  保存世界数据，返回：成功返回true  |
|  `string GetInfo()`  |  获取世界信息，返回：包含世界状态的字符串  |
|  `void LinkSvr(var svrpath,var indexbin)`  |  连接到服务器，参数：svrpath-服务器路径，indexbin-索引数据  |
|  `bool SaveLinkBack()`  |  保存链接数据，返回：成功返回true  |
|  `var GetPosBoxIndex(vec3 pos,float len)`  |  获取指定位置的盒子索引，参数：pos-位置，len-盒子长度，返回：索引数据  |
|  `bool SetData(var data)`  |  设置世界数据，参数：data-数据，返回：成功返回true  |
|  `bool GetData(var& data)`  |  获取世界数据，参数：data-数据引用，返回：成功返回true  |
|  `void DestroyWorld()`  |  销毁世界，释放所有资源  |
|  `bool LoadFile(string pfilename)`  |  从文件加载世界，参数：pfilename-文件名，返回：成功返回true  |
|  `bool SaveFile(string pfilename,int mode=0)`  |  保存世界到文件，参数：pfilename-文件名，mode-保存模式，返回：成功返回true  |
|  `bool LinkMID(string pmidfilename)`  |  链接MID文件，参数：pmidfilename-MID文件名，返回：成功返回true  |
|  `int BarPixel(int x1,int y1,int z1,int x2,int y2,int z2,var smatid)`  |  在两点间绘制方块，参数：x1,y1,z1-起点坐标，x2,y2,z2-终点坐标，smatid-材质ID，返回：创建的方块数量  |
|  `int FillSphere(vec3 pos,float r,var smatid,int mode=0,int shapemode=0)`  |  填充球体，参数：pos-球心，r-半径，smatid-材质ID，mode-填充模式，shapemode-形状模式，返回：修改的方块数量  |
|  `var GetPixel(int x,int y,int z,int mode=0)`  |  获取指定位置的像素数据，参数：x,y,z-坐标，mode-获取模式，返回：像素数据  |
|  `bool SetPixel(int x,int y,int z,int matid,int val)`  |  设置指定位置的像素数据，参数：x,y,z-坐标，matid-材质ID，val-值，返回：成功返回true  |
|  `bool CreateMatImg(int w,int h)`  |  创建材质图像，参数：w-宽度，h-高度，返回：成功返回true  |
|  `int SetMat(int matid,string pname,int defcolor=0xFFCCCCCC,string pimg=NULL,int anispeed=0,var puserv=NULL,int bkind=0)`  |  设置材质，参数：matid-材质ID，pname-名称，defcolor-默认颜色，pimg-图像路径，anispeed-动画速度，puserv-用户数据，bkind-类型，返回：成功返回1  |
|  `bool SetMatNormal(int matid,string pimg)`  |  设置材质法线贴图，参数：matid-材质ID，pimg-法线贴图路径，返回：成功返回true  |
|  `bool SetMatVid(var matst)`  |  设置材质视频，参数：matst-材质状态，返回：成功返回true  |
|  `void SetWidgetVid(var widget)`  |  设置部件视频，参数：widget-部件数据  |
|  `void SetMatReady()`  |  完成材质设置，应用所有材质配置  |
|  `int IsMatReady()`  |  检查材质是否就绪，返回：就绪返回1，否则返回0  |
|  `int GetMatNum()`  |  获取材质数量，返回：材质总数  |
|  `var GetMatSz()`  |  获取所有材质数据，返回：材质数组  |
|  `var GetMat(int matid)`  |  获取指定材质数据，参数：matid-材质ID，返回：材质数据  |
|  `var GetMatImg(int matid)`  |  获取指定材质的图像，参数：matid-材质ID，返回：图像数据  |
|  `void InitLibTex(int w=4096,int h=512)`  |  初始化纹理库，参数：w-宽度，h-高度  |
|  `var TestAllocTex(int w,int h)`  |  测试分配纹理，参数：w-宽度，h-高度，返回：分配结果坐标  |
|  `void GetAllIndex(var agv)`  |  获取所有索引，参数：agv-请求数据  |
|  `var GetMcIndexPt(int i)`  |  获取MC索引点，参数：i-索引，返回：索引点数据  |
|  `var GetMcPtBlock(vec3 pos)`  |  获取指定位置的MC方块，参数：pos-位置，返回：方块数据  |
----
### GObj3DPixelMc
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DPixelMc](#GObj3DPixelMc)
**描述**:3D像素MC对象，用于渲染和管理体素世界的显示
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pData  |  obj  |  获取数据对象指针  |
|  m_nMaxShowGuid  |  int  |  最大显示的GUID数量  |
|  m_fTestCrossMaxLen  |  float  |  射线检测的最大长度  |
|  m_fCrossDisAdd  |  float  |  射线相交的距离增量  |
|  m_nCacheDataUseSec  |  int  |  缓存数据使用时间(秒)  |
|  m_nMatTextureNo  |  int  |  材质纹理编号  |
|  m_fEmptySelectZ  |  float  |    |
|  m_nColorOnly  |  int  |    |
|  m_nShowWidget  |  int  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool LinkDatObj(obj pdat)`  |  链接到数据对象，参数：pdat-MC世界对象，返回：成功返回true  |
|  `void OnCtrlLBDown(int x,int y)`  |  处理左键按下事件，参数：x,y-鼠标坐标  |
|  `void RegCollision(int breg=1)`  |  注册碰撞检测，参数：breg-是否注册  |
|  `int SetPixel(int x,int y,int z,int smatid,int val=255)`  |  设置像素，参数：x,y,z-坐标，smatid-材质ID，val-值，返回：成功返回1  |
|  `int BarPixel(int x1,int y1,int z1,int x2,int y2,int z2,int smatid)`  |  绘制线条方块，参数：x1,y1,z1-起点坐标，x2,y2,z2-终点坐标，smatid-材质ID，返回：成功返回修改的方块数量  |
|  `int FillSphere(vec3 pos,float r,int id,int mode=0,int shapemode=0)`  |  填充球体，参数：pos-球心，r-半径，id-材质ID，mode-填充模式，shapemode-形状模式，返回：修改的方块数量  |
|  `bool FindRayCrossPt(vec3& iv,vec3& idit,float d=0)`  |  查找射线与物体的交点，参数：iv-交点，idit-交点法线，d-距离偏移，返回：成功返回true  |
|  `void OnDatModi()`  |  数据修改通知  |
|  `void OnMcLibReady()`  |  材质库就绪通知  |
----
### GMcTreeMaker
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GMcTreeMaker](#GMcTreeMaker)
**描述**:MC树结构生成器，用于创建和管理体素树结构
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool LinkDatObj(obj pdat)`  |  连接数据对象，参数：pdat-数据对象指针，返回：连接是否成功  |
|  `bool SaveAutoMakeDat(string pfilename)`  |  保存自动生成的数据，参数：pfilename-文件名，返回：保存是否成功  |
|  `bool LoadAutoMakeDat(string pfilename,string pimgpath)`  |  加载自动生成的数据，参数：pfilename-文件名，pimgpath-图像路径，返回：加载是否成功  |
|  `bool PerAutoMakeWd(obj pcon,var kindefv,string pimgpath)`  |  预处理自动生成世界，参数：pcon-容器对象，kindefv-类型定义，pimgpath-图像路径，返回：处理是否成功  |
|  `bool AddAutoMakeImg(string pimgname,int kindno,var agv)`  |  添加自动生成图像，参数：pimgname-图像名称，kindno-类型编号，agv-扩展参数，返回：添加是否成功  |
|  `bool SetAutoMakeKindImg(var agv)`  |  设置自动生成的类型图像，参数：agv-扩展参数，返回：设置是否成功  |
|  `void ReMakeAllGuid()`  |  重新生成所有引导  |
|  `void AutoMakeByCon(int ix,int iy)`  |  根据坐标自动生成，参数：ix-X坐标，iy-Y坐标  |
----
### GSandAppWnd
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GSandAppWnd](#GSandAppWnd)
**描述**:沙盒应用窗口类，用于创建和管理沙盒环境中的应用窗口
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetText(string pstr)`  |  设置窗口标题，参数：pstr-标题文本  |
|  `string GetText()`  |  获取窗口标题，返回：标题文本  |
|  `bool SetWinIcon(string piconfilename)`  |  设置窗口图标，参数：piconfilename-图标文件名，返回：是否设置成功  |
----
### GObj3DSandBox
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DSandBox](#GObj3DSandBox)
**描述**:3D沙盒环境类，用于创建和管理3D场景中的脚本执行环境
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pSandApp  |  obj  |  沙盒应用对象  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `obj GetShowRoot()`  |  获取显示根节点，返回：根节点对象  |
|  `obj GetResCtrl()`  |  获取资源控制器，返回：资源控制器对象  |
|  `bool Reset()`  |  重置沙盒环境，返回：是否重置成功  |
|  `bool LoadScript(string pstartname0,string pstartname1=NULL,string pstartname2=NULL)`  |  加载脚本，参数：pstartname0-主脚本文件名，pstartname1-辅助脚本文件名1，pstartname2-辅助脚本文件名2，返回：是否加载成功  |
|  `bool Start(int b3d=0)`  |  启动沙盒环境，参数：b3d-是否为3D环境，返回：是否启动成功  |
|  `bool GetScriptClassInfo(var& ret,var pobj)`  |  获取脚本类信息，参数：ret-返回的类信息，pobj-对象变量，返回：是否获取成功  |
|  `bool IsIncludeFile(int fid)`  |  检查文件是否被包含，参数：fid-文件ID，返回：是否被包含  |
|  `var GetIncludeFiles()`  |  获取所有包含的文件，返回：文件列表  |
|  `var GetRootClassPtr()`  |  获取根类指针，返回：根类指针  |
|  `var GetScriptRes()`  |  获取脚本资源，返回：资源变量  |
|  `var GetSystemVID()`  |  获取系统VID，返回：系统VID变量  |
|  `var SeekFileClassFun(int fid,int line,int col)`  |  查找文件中的类和函数，参数：fid-文件ID，line-行号，col-列号，返回：查找结果  |
|  `obj NewSandBoxObj(strid classnameid,obj ppFather)`  |  创建沙盒对象，参数：classnameid-类名ID，ppFather-父对象，返回：创建的对象  |
|  `obj CreateSandAppObj(int b3d=0)`  |  创建沙盒应用对象，参数：b3d-是否为3D环境，返回：创建的应用对象  |
----
### GObj3DDepMap
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DDepMap](#GObj3DDepMap)
**描述**:深度图渲染类，用于生成和管理3D场景深度图以实现遮挡剔除
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nTextLevel  |  int  |  深度图纹理级别(0=256,1=512,2=1024,3=2048等)  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetTextLevel(int level)`  |  设置深度图纹理级别，参数：level-级别(0=256,1=512,2=1024,3=2048等)  |
----
### GObj3DParticle
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj3DShow](#GObj3DShow)/[GObj3DParticle](#GObj3DParticle)
**描述**:3D粒子系统类，用于创建和管理3D场景中的粒子特效
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pAtom  |  ptrex  |  当前粒子系统的定义对象  |
|  m_fPlaySpeed  |  float  |  粒子系统的播放速度倍率  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(var name)`  |  加载粒子特效资源，参数：name-资源名称，返回：是否加载成功  |
|  `void Reset()`  |  重置粒子系统到初始状态  |
----
### GWebFile
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GWebFile](#GWebFile)
**描述**:HTTP文件下载类，提供多线程分块下载、断点续传和进度通知功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pNoti  |  obj  |  通知对象指针，用于接收下载进度和完成事件  |
|  m_sHeadEx  |  string  |  HTTP请求头信息，用于设置自定义的HTTP头字段  |
|  m_sUrl  |  string  |  当前下载URL地址  |
|  m_sLoc  |  string  |  本地文件保存路径  |
|  m_sTempFile  |  string  |  临时文件保存路径，用于下载过程中的数据缓存  |
|  m_nStatus  |  int  |  下载状态码，0-未开始，1-下载中，-1-下载出错  |
|  m_nDownNum  |  int  |  当前下载任务数量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetMaxDown(int n=8,int subsizekb=512)`  |  设置最大并发下载数和单个块大小，参数：n-最大并发数，subsizekb-单个块大小(KB)  |
|  `bool DownFile(string purl,string ploc,string ptmpfile=NULL,int suboutsec=3)`  |  下载文件并保存到本地，参数：purl-URL地址，ploc-本地保存路径，ptmpfile-临时文件路径，suboutsec-超时秒数，返回：是否成功启动下载  |
|  `void OnData(int l,int total,int uflag)`  |  处理下载进度数据，参数：l-当前已下载大小，total-总大小，uflag-用户标识  |
|  `void OnDownNetErr(int flag,string pmsg,int uflag)`  |  处理下载错误信息，参数：flag-错误标志，pmsg-错误信息，uflag-用户标识  |
|  `void OnDataReady(var retv)`  |  处理下载数据就绪事件，参数：retv-返回的数据变量  |
|  `void CheckDown()`  |  检查下载状态并处理下载分块  |
|  `void DownFileErr(string pmsg)`  |  处理下载错误，参数：pmsg-错误信息  |
|  `void OnFileReady()`  |  文件下载完成后的处理函数  |
----
### GSandBoxWinApp
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GObjShow](#GObjShow)/[GObj2DWnd](#GObj2DWnd)/[GBoxShowApp](#GBoxShowApp)/[GSandBoxWinApp](#GSandBoxWinApp)
**描述**:
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int UpdateGBoxExe(string pexename)`  |    |
----
### GWebLink
**类型**：[class](#class)　　　　**继承** ：[GObj](#GObj)/[GWebLink](#GWebLink)
**描述**:网络链接类，提供HTTP/HTTPS网页访问、数据传输和请求功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sUrl  |  string  |  URL地址  |
|  m_sHttpHead  |  string  |  HTTP请求头部  |
|  m_nPort  |  int  |  端口号码  |
|  m_bTrace  |  int  |  是否输出跟踪信息  |
|  m_vRetHead  |  var  |  返回的请求头中文件  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool SetUrl(string purl)`  |  设置URL地址，参数：purl-URL地址，返回：成功返回true，失败返回false  |
|  `bool Close()`  |  关闭网络连接，返回：成功返回true，失败返回false  |
|  `bool Post(string postdata)`  |  发送POST请求，参数：postdata-POST数据内容，返回：成功返回true，失败返回false  |
|  `bool SetNoti(string pfun)`  |  设置通知回调函数，参数：pfun-回调函数名，返回：成功返回true，失败返回false  |
|  `void SetCtrlFun(string pfunname)`  |  设置控制函数，参数：pfunname-函数名，返回：无  |
----
### :task
**类型**：[eve](#eve)　　　　**路径** ：[:task](#:task)
**描述**:任务控制接口类，提供脚本任务调度和管理功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var WaitMs(int ms,strid waitnameid=0)`  |  等待指定毫秒数，参数：ms-等待毫秒数，waitnameid-等待标识符，返回：函数执行状态  |
|  `var Wait(float sec,strid waitnameid=0)`  |  等待指定秒数，参数：sec-等待秒数，waitnameid-等待标识符，返回：函数执行状态  |
|  `var Abort(int my,var perragv=NULL)`  |  中止当前任务，参数：my-错误码，perragv-错误参数，返回：函数执行状态  |
|  `bool EndWait(strid waitnameid,var agv)`  |  结束指定等待任务，参数：waitnameid-等待标识符，agv-传递给等待任务的参数，返回：是否成功  |
|  `var BusyWait()`  |  执行忙等待，允许其他任务在当前任务暂停期间执行，返回：函数执行状态  |
|  `var StartTask(strid funid,var pstartagv=NULL,strid endfunid=0)`  |  启动新任务，参数：funid-函数标识符，pstartagv-启动参数，endfunid-结束回调函数，返回：函数执行状态  |
|  `void RegInterface(obj p,strid pname)`  |  注册接口对象，参数：p-对象指针，pname-接口名称  |
|  `obj FindInterface(strid facenameid,int bautofindfather=1)`  |  查找接口对象，参数：facenameid-接口名称，bautofindfather-是否自动查找父对象，返回：接口对象指针  |
|  `bool DelInterface(obj p,strid pname)`  |  删除接口对象，参数：p-对象指针，pname-接口名称，返回：是否成功  |
|  `string GetFunErrStr(int err)`  |  获取函数错误码对应的错误信息，参数：err-错误码，返回：错误信息字符串  |
|  `void Err(var v)`  |  输出错误信息，参数：v-错误信息  |
|  `obj GetCurTaskPtr()`  |  获取当前任务指针，返回：任务对象指针  |
|  `bool IsTaskPtr(obj p)`  |  检查指针是否为任务对象，参数：p-对象指针，返回：是否为任务对象  |
|  `var HoldTask()`  |  挂起当前任务，返回：函数执行状态  |
|  `bool ResumeTask(var ptask,var agv)`  |  恢复指定任务，参数：ptask-任务对象，agv-传递给任务的参数，返回：是否成功  |
|  `bool RemoveHoldTask(var ptask)`  |  移除挂起的任务，参数：ptask-任务对象，返回：是否成功  |
|  `var CallFunEx(var fun,var pagv)`  |  调用指定函数，参数：fun-函数标识符，pagv-函数参数，返回：函数执行状态  |
----
### :math
**类型**：[eve](#eve)　　　　**路径** ：[:math](#:math)
**描述**:数学函数库类，提供各种随机数生成和3D数学计算功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int rand(int maxv)`  |  取0-maxv之间的随机整数，参数：maxv-最大值，返回：随机整数  |
|  `float randf(float range=1.0f)`  |  取0.0f-range之间的随机浮点数，参数：range-范围值，返回：随机浮点数  |
|  `vec4 MakePlane(vec3 planepos,vec3 planedir)`  |  创建平面向量表示，参数：planepos-平面上的点，planedir-平面法向量，返回：平面方程向量(ax+by+cz+d=0)  |
|  `bool GetPtOnPlane(vec4 planev4,vec3 p1,vec3 p2,vec3& cross)`  |  计算线段与平面的交点，参数：planev4-平面向量，p1-线段起点，p2-线段终点，cross-输出交点，返回：是否有交点  |
|  `vec3 SeekPtOnPlane(vec3 planepos,vec3 planedir,vec3 lorig,vec3 ldir)`  |  计算射线与平面的交点，参数：planepos-平面上的点，planedir-平面法向量，lorig-射线起点，ldir-射线方向，返回：交点坐标  |
----
### :fixcal
**类型**：[fixcall](#fixcall)　　　　**路径** ：[:fixcal](#:fixcal)
**描述**:基础数学计算和格式化函数库，提供数值运算、颜色处理和字符串格式化功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var abs(var v)`  |  计算绝对值，参数：v-输入值，返回：绝对值  |
|  `float sqrt(float q)`  |  计算平方根，参数：q-输入值，返回：平方根值  |
|  `float sin(float rad)`  |  计算正弦值，参数：rad-弧度值，返回：正弦值  |
|  `float cos(float rad)`  |  计算余弦值，参数：rad-弧度值，返回：余弦值  |
|  `float tan(float rad)`  |  计算正切值，参数：rad-弧度值，返回：正切值  |
|  `float acos(float rad)`  |  计算反余弦值，参数：rad-输入值，返回：弧度值  |
|  `float asin(float rad)`  |  计算反正弦值，参数：rad-输入值，返回：弧度值  |
|  `float atan2(float dy,float dx)`  |  计算二参数反正切值，参数：dy-Y差值，dx-X差值，返回：弧度值  |
|  `float atan2ang(float dy,float dx)`  |  计算二参数反正切值并转换为角度，参数：dy-Y差值，dx-X差值，返回：角度值  |
|  `float ang2rad(float angle)`  |  角度转弧度，参数：angle-角度值，返回：弧度值  |
|  `float rad2ang(float rad)`  |  弧度转角度，参数：rad-弧度值，返回：角度值  |
|  `float fmod(float x,float y)`  |  计算浮点数取模，参数：x-被除数，y-除数，返回：余数  |
|  `float dot(var v1,var v2)`  |  计算向量点积，参数：v1-向量1，v2-向量2，返回：点积结果  |
|  `var clamp(var InValue,var InMin,var InMax)`  |  限制值在指定范围内，参数：InValue-输入值，InMin-最小值，InMax-最大值，返回：限制后的值  |
|  `var min(var pinAgv)`  |  取最小值，参数：pinAgv-参数数组，返回：最小值  |
|  `var max(var pinAgv)`  |  取最大值，参数：pinAgv-参数数组，返回：最大值  |
|  `var mix(var v0,var v1,float step)`  |  混合两个值，参数：v0-起始值，v1-结束值，step-混合比例，返回：混合结果  |
|  `var sz(var v)`  |  创建单元素数组，参数：v-数组元素，返回：包含该元素的数组  |
|  `string gmtsec_str(int gmt,int bcovloc=1)`  |  将GMT时间戳转换为字符串，参数：gmt-时间戳，bcovloc-是否转换为本地时间，返回：时间字符串  |
|  `string getsizestr(var v)`  |  将字节大小转换为可读字符串(B/KB/MB)，参数：v-字节数，返回：格式化的大小字符串  |
|  `var makevid(var v)`  |  创建NameID映射表，参数：v-键值对数组(key1,value1,key2,value2...)，返回：ID索引的变量  |
|  `var makenamedsz(var v)`  |  创建命名数组，参数：v-键值对数组(key1,value1,key2,value2...)，返回：命名索引的数组  |
|  `string FormatInt16Fix(int d,int fixw=0)`  |  格式化16进制整数，参数：d-整数值，fixw-固定宽度(补零)，返回：格式化后的字符串  |
|  `string Fomatint64X(var v)`  |  将64位整数转换为16进制字符串，参数：v-64位整数，返回：16进制字符串  |
|  `var RGBA(int r,int g,int b,int alpha=255)`  |  创建RGBA颜色值，参数：r-红色分量(0-255)，g-绿色分量(0-255)，b-蓝色分量(0-255)，alpha-透明度(0-255)，返回：颜色变量  |
|  `var MixColor(var c1,var c2,float mix)`  |  混合两个颜色，参数：c1-颜色1，c2-颜色2，mix-混合比例(0-1)，返回：混合后的颜色  |
|  `var FormatColor(var inval,int bvec4=0)`  |  格式化颜色值，参数：inval-输入颜色值，bvec4-是否返回vec4格式，返回：格式化后的颜色  |
|  `vec4 Color2Hsi(var c)`  |  将RGB颜色转换为HSI颜色空间，参数：c-RGB颜色，返回：HSI颜色(x=色调,y=饱和度,z=亮度,w=透明度)  |
|  `vec4 Hsi2Color(vec4 vhsi)`  |  将HSI颜色空间转换为RGB颜色，参数：vhsi-HSI颜色(x=色调,y=饱和度,z=亮度,w=透明度)，返回：RGB颜色  |
|  `string GetHSMStr(int d)`  |  将秒数转换为时:分:秒格式字符串，参数：d-秒数，返回：格式化的时间字符串(HH:MM:SS)  |
|  `string GetMsStr(var v)`  |  将毫秒数转换为时:分:秒.毫秒格式字符串，参数：v-毫秒数，返回：格式化的时间字符串(HH:MM:SS.mmm)  |
|  `var GetVarInfo(var v)`  |  获取变量的详细信息，参数：v-变量，返回：包含类型名、字符串表示和附加信息的数组  |
----
### file
**类型**：[namespace](#namespace)　　　　**路径** ：[file](#file)
**描述**:文件系统接口类，提供文件操作的核心功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `string GetSysFilePath()`  |  系统文件路径，返回：系统文件目录的完整路径  |
|  `string GetPublicPath()`  |  Gbox共享数据存储路径，返回：共享数据目录的完整路径  |
|  `string GetStartFileName()`  |  启动文件名，返回：应用程序启动文件的完整路径  |
|  `string GetTempPath()`  |  临时文件存储路径，返回：临时文件目录的完整路径  |
|  `string GetRelativePathName(string path,string pathname,int bpathonly=1)`  |  文件名的相对位置，参数：path-基准路径，pathname-目标路径，bpathonly-是否只返回路径，返回：相对路径字符串  |
|  `var ListDir(string listpath,int bhavesub=0,string pextstr=NULL,int maxnum=4096,int retmode=0)`  |  列出目录下的文件，参数：listpath-目录路径，bhavesub-是否包含子目录，pextstr-文件扩展名过滤，maxnum-最大文件数，retmode-返回模式，返回：文件列表  |
|  `var ListDirEx(string listpath,int info=1)`  |  列出目录详细信息，参数：listpath-目录路径，info-信息详细程度，返回：目录内容信息  |
|  `string MakeSysFileName(string pfilename)`  |  生成系统文件名，参数：pfilename-基础文件名，返回：完整系统文件路径  |
|  `bool IsAbsFileName(string path)`  |  判断是否为绝对文件路径，参数：path-文件路径，返回：true表示是绝对路径，false表示是相对路径  |
|  `string FixPath(string path)`  |  合并文件名中的..转义，参数：path-原始路径，返回：处理后的标准化路径  |
|  `int GetFileNameID(string fname)`  |  获取文件名ID(不区分大小写)，参数：fname-文件名，返回：文件名的唯一ID值  |
|  `string GetIDFileName(strid id)`  |  通过ID获取文件名，参数：id-文件ID，返回：对应的文件名  |
|  `bool IfHaveFile(string fname, int date=0, int len=0)`  |  检查文件是否存在，参数：fname-文件名，date-时间检查，len-长度检查，返回：true表示文件存在，false表示不存在  |
|  `bool SetFileTime(string lpszFileName, int time)`  |  设置文件时间，参数：lpszFileName-文件名，time-时间值，返回：操作是否成功  |
|  `int64 GetFileLen(string fname)`  |  获取文件字节长度，参数：fname-文件名，返回：文件长度，不存在返回0  |
|  `int GetFileTime(string fname)`  |  获取文件时间，参数：fname-文件名，返回：文件修改时间  |
|  `var GetFileLenTime(string fname)`  |  获取文件长度和时间，参数：fname-文件名，返回：包含文件长度[0]和时间[1]的数组  |
|  `string GetFileTimeGMT(int datetime)`  |  将时间转换为GMT格式字符串，参数：datetime-时间值，返回：GMT格式时间字符串(20xx-xx-11 8:00:00)  |
|  `bool PreWritePath(string lpszFileName)`  |  准备写文件的目录，参数：lpszFileName-文件路径，返回：目录准备是否成功  |
|  `void SlipFileName(string &Path,string &name,string pfullfilename)`  |  分割文件路径和文件名，参数：Path-输出路径，name-输出文件名，pfullfilename-完整文件路径  |
|  `string GetFileExtName(string pfullfilename)`  |  获取文件扩展名，参数：pfullfilename-完整文件路径，返回：文件扩展名  |
|  `string GetFileNameNoExt(string pfullfilename)`  |  获取不含扩展名的文件名，参数：pfullfilename-完整文件路径，返回：不含扩展名的文件名  |
|  `bool DeleteFile(string fname)`  |  删除文件，参数：fname-文件名，返回：操作是否成功，支持文件在各种pak包或IO中  |
|  `bool RemoveDir(string path)`  |  删除目录，参数：path-目录路径，返回：操作是否成功  |
|  `bool MoveFile(string pexist,string pnew)`  |  移动文件，参数：pexist-源文件路径，pnew-目标文件路径，返回：操作是否成功  |
|  `bool RenameFile(string pexist,string pnewname)`  |  文件重命名，参数：pexist-原文件路径，pnewname-新文件名，返回：操作是否成功  |
|  `bool UpdateFile(string fname)`  |  更新文件时间到当前，参数：fname-文件名，返回：操作是否成功，支持文件在各种pak包或IO中  |
|  `bool CopyFile(string lpExistingFileName,string lpNewFileName,int bFailIfExists=0)`  |  复制文件，参数：lpExistingFileName-源文件，lpNewFileName-目标文件，bFailIfExists-目标存在时是否失败，返回：操作是否成功  |
|  `bool LoadFileBin(var& pretbin,string pfilename)`  |  读取二进制文件内容，参数：pretbin-输出二进制数据，pfilename-文件名，返回：操作是否成功  |
|  `bool SaveFileBin(var& pwbin,string pfilename,int filetime=0)`  |  保存二进制数据到文件，参数：pwbin-二进制数据，pfilename-文件名，filetime-文件时间，返回：操作是否成功  |
|  `bool LoadFileBinRange(var& pretbin,string pfilename,var startpos,int len)`  |  读取二进制文件部分内容，参数：pretbin-输出数据，pfilename-文件名，startpos-起始位置，len-读取长度，返回：操作是否成功  |
|  `bool SaveFileBinRange(var& pwbin,string pfilename,var startpos)`  |  写入二进制数据到文件指定位置，参数：pwbin-数据，pfilename-文件名，startpos-起始位置，返回：操作是否成功  |
|  `bool LoadText(var& pstring,string pfilename)`  |  读取文本文件内容，参数：pstring-输出字符串，pfilename-文件名，返回：操作是否成功  |
|  `bool LoadTextSz(var& psz,string pfilename)`  |  读取文本文件按行分割，参数：psz-输出行数组，pfilename-文件名，返回：操作是否成功  |
|  `bool SaveText(var string,string pfilename,int utf8=1)`  |  保存文本内容到文件，参数：string-文本内容，pfilename-文件名，utf8-是否使用UTF8编码，返回：操作是否成功  |
|  `bool SaveVarAsFile(var& pwritev,string pfilename,int key=0,int filetime=0)`  |  保存变量到文件，参数：pwritev-变量数据，pfilename-文件名，key-加密密钥，filetime-文件时间，返回：操作是否成功  |
|  `bool LoadVarAsFile(var& pret,string pfilename,int key=0)`  |  从文件加载变量，参数：pret-输出变量，pfilename-文件名，key-解密密钥，返回：操作是否成功  |
|  `var GetAccessPathSz()`  |  获取所有可访问目录属性，返回：目录属性数组  |
|  `bool RegFileTransApi(obj psvr,string papiname,string pfunname)`  |  注册文件访问API，参数：psvr-服务对象，papiname-API名称，pfunname-函数名，返回：注册是否成功  |
|  `bool IsFileTrans(string papiname)`  |  检查文件访问API是否已注册，参数：papiname-API名称，返回：是否已注册  |
|  `var GetFileInfo(string pfilename)`  |  获取文件详细信息，参数：pfilename-文件名，返回：包含长度、时间、存储位置和只读状态的数组  |
|  `bool RegFileNoti(string pfilename,obj pcall,var fun)`  |  注册文件状态变化回调，参数：pfilename-文件名，pcall-回调对象，fun-回调函数，返回：注册是否成功  |
|  `bool DelFileNoti(string pfilename,obj pcall,var pfun=NULL)`  |  删除文件状态回调，参数：pfilename-文件名，pcall-回调对象，pfun-回调函数(NULL表示删除所有)，返回：操作是否成功  |
|  `void CheckNotiRegFile()`  |  检查所有注册文件的状态，触发必要的回调  |
|  `void NotiFileStatus(string plocname,int st)`  |  主动通知文件状态变化，参数：plocname-文件名，st-状态码  |
----
### sys
**类型**：[namespace](#namespace)　　　　**路径** ：[sys:task](#sys:task)
**描述**:系统接口类，提供系统级操作、公共数据存储和设备信息访问功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int LaunchAppliction(string pfilename,string pagv)`  |  启动外部应用程序，参数：pfilename-程序路径，pagv-命令行参数，返回：启动结果码  |
|  `bool ShellOpenDoc(string pfilename)`  |  使用系统默认程序打开文档，参数：pfilename-文件路径，返回：操作是否成功  |
|  `string GetAppBundleID()`  |  获取应用程序包ID，返回：应用包ID字符串  |
|  `string GetAppPathName()`  |  获取应用程序路径，返回：应用程序完整路径  |
|  `string ReadPublicString(string strSection,string keyname,string defaultstr=NULL)`  |  读取公共字符串配置，参数：strSection-配置区段，keyname-键名，defaultstr-默认值，返回：配置字符串  |
|  `bool WritePublicString(string strSection,string keyname,string string)`  |  写入公共字符串配置，参数：strSection-配置区段，keyname-键名，string-字符串值，返回：操作是否成功  |
|  `var ReadPublicVar(string strSection,string keyname,var pdefault=NULL)`  |  读取公共变量配置，参数：strSection-配置区段，keyname-键名，pdefault-默认值，返回：配置变量  |
|  `bool WritePublicVar(string strSection,string keyname,var wv)`  |  写入公共变量配置，参数：strSection-配置区段，keyname-键名，wv-变量值，返回：操作是否成功  |
|  `string GetSelfIPAddress()`  |  获取本机IP地址，返回：IP地址字符串  |
|  `var GetSystemVID()`  |  获取系统变量字典，返回：系统变量VID表  |
|  `bool IsSystem(strid nameid)`  |  检查系统变量是否存在，参数：nameid-变量ID，返回：变量是否存在  |
|  `var GetSystem(strid nameid,var pdef=NULL)`  |  获取系统变量值，参数：nameid-变量ID，pdef-默认值，返回：变量值  |
|  `void SetSystem(strid nameid,var v)`  |  设置系统变量值，参数：nameid-变量ID，v-变量值  |
|  `string GetIDString(int id)`  |  获取ID对应的字符串，参数：id-整数ID，返回：字符串  |
|  `var GetStringID(string str)`  |  获取字符串对应的ID，参数：str-字符串，返回：整数ID  |
|  `bool CopyToClipboard(string cpystring)`  |  写剪裁板文本，参数：cpystring-要复制的文本，返回：操作是否成功  |
|  `bool GetClipText(string& clpstr)`  |  获取剪贴板文本，参数：clpstr-输出文本，返回：操作是否成功  |
|  `bool IsClipText()`  |  检查剪贴板是否有文本，返回：true表示有文本，false表示无文本  |
|  `string GetMac(string pgamename,int needaddins=0)`  |  获取设备MAC地址，参数：pgamename-应用标识，needaddins-是否添加额外信息，返回：MAC地址字符串  |
|  `int64 GetMacID(string pgamename,int needaddins=0)`  |  获取设备MAC地址的整数表示，参数：pgamename-应用标识，needaddins-是否添加额外信息，返回：MAC地址的整数表示  |
|  `int64 GetOnlyInt64(int hbyte=0)`  |  获取唯一的64位整数ID，参数：hbyte-高字节标识，返回：64位整数  |
|  `int GetTickCount()`  |  获取系统启动后的毫秒数，返回：毫秒计数  |
|  `int GetSecCount()`  |  获取系统启动后的秒数，返回：秒计数  |
|  `int64 GetMsCount()`  |  获取系统启动后的毫秒数(64位)，返回：64位毫秒计数  |
|  `var GetDeviceMetrics()`  |  获取设备度量信息，返回：设备信息数组  |
|  `vec2 GetDeviceSize()`  |  获取设备屏幕尺寸，返回：屏幕尺寸向量(宽,高)  |
|  `bool OpenURL(string purl)`  |  打开网页，参数：purl-URL地址，返回：操作是否成功  |
|  `bool ShellBrowse(string path)`  |  打开系统浏览器浏览文件或目录，参数：path-路径，返回：操作是否成功  |
|  `int GetMacNum()`  |  获取MAC地址计数，返回：MAC地址计数值  |
----
### csvr
**类型**：[namespace](#namespace)　　　　**路径** ：[csvr:task](#csvr:task)
**描述**:网络客户端服务器通信任务类，提供RPC功能和分布式通信
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Start(int port=0,string pbindip=NULL)`  |  启动服务器，参数：port-监听端口(0为自动)，pbindip-绑定的IP地址  |
|  `int AutoStart(int port=1000,int scanenum=100,string pbindip=NULL)`  |  自动寻找可用端口启动服务器，参数：port-起始端口，scanenum-扫描端口数量，pbindip-绑定IP  |
|  `bool IsStart()`  |  检查服务器是否已启动  |
|  `bool RegSvr(obj pobj,string pname)`  |  注册服务对象，参数：pobj-服务对象，pname-服务名称  |
|  `bool BindSvrAddress(string path,string ipadd)`  |  绑定服务地址，参数：path-服务路径，ipadd-IP地址  |
|  `int GetLinkStatus(strid aid,int bautolink=1)`  |  获取链接状态，参数：aid-地址ID，bautolink-是否自动连接  |
|  `bool send(strid aid,strid svrid,strid fid,var pagv=NULL)`  |  发送消息，参数：aid-地址ID，svrid-服务ID，fid-函数ID，pagv-参数  |
|  `var call(strid aid,strid svrid,strid fid,var pagv=NULL,int outsec=10)`  |  调用远程函数并等待结果，参数：aid-地址ID，svrid-服务ID，fid-函数ID，pagv-参数，outsec-超时秒数  |
|  `var callptr(var psvr,strid fid,var pagv=NULL,int outsec=10)`  |  通过指针调用远程函数，参数：psvr-服务指针，fid-函数ID，pagv-参数，outsec-超时秒数  |
|  `bool post(var netaddress,strid fid,var pagv)`  |  直接向网络地址发送消息，参数：netaddress-网络地址，fid-函数ID，pagv-参数  |
|  `var MakePtr(var pobj,var address)`  |  创建网络对象指针，参数：pobj-对象，address-网络地址  |
|  `var GetInfo(strid kind,var pagv=NULL)`  |  获取系统信息，参数：kind-信息类型，pagv-附加参数  |
|  `bool OpenHole(string pipport)`  |  打开网络穿透通道，参数：pipport-IP和端口  |
|  `string GetSelfIp()`  |  获取本机IP地址  |
|  `var GetSelfIpSz()`  |  获取本机所有IP地址列表  |
|  `void AddSelfIpSz(string ipport)`  |  添加本机IP地址，参数：ipport-IP和端口  |
|  `var SelectIpSz(var ipsz)`  |  选择使用的IP地址，参数：ipsz-IP地址列表  |
----
### netapi
**类型**：[namespace](#namespace)　　　　**路径** ：[netapi:task](#netapi:task)
**描述**:网络API接口类，提供服务器查找和远程函数调用功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var FindSvr(string psvrname)`  |  查找服务器，参数：psvrname-服务器名称，返回：查找结果状态码  |
|  `var call(string svrname,strid funid,var pagv=NULL,int outsec=2)`  |  远程函数同步调用，参数：svrname-服务器名称，funid-函数ID，pagv-参数，outsec-超时秒数，返回：调用结果状态码  |
|  `void send(string svrname,strid funid,var pagv=NULL)`  |  远程函数异步发送，参数：svrname-服务器名称，funid-函数ID，pagv-参数  |
|  `void post(string svrname,strid funid,var pagv=NULL)`  |  远程事件发布，参数：svrname-服务器名称，funid-函数ID，pagv-参数  |
----
### syshelp
**类型**：[namespace](#namespace)　　　　**路径** ：[syshelp:task](#syshelp:task)
**描述**:系统帮助类，提供类信息查询、脚本反射和配置管理功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void GetSysIDName(var& all)`  |  获取所有系统ID名称映射，参数：all-输出名称映射表  |
|  `void GetSysAllClassDef(var& all)`  |  获取所有类定义信息，参数：all-输出类定义信息表  |
|  `void GetSysAllClassPathDef(var& all)`  |  获取所有类路径定义信息，参数：all-输出类路径信息表  |
|  `bool GetScriptClassInfo(var& ret,var pobjv)`  |  获取脚本类信息，参数：ret-输出信息数组，pobjv-目标对象，返回：操作是否成功  |
|  `var FindClassCfgVal(var path,var def)`  |  查找类配置值，参数：path-配置路径，def-默认值，返回：配置值  |
|  `var GetCfg(string path,var def)`  |  获取配置值，参数：path-配置路径，def-默认值，返回：配置值  |
|  `bool SetCfg(string path,var v,int bnoti=1)`  |  设置配置值，参数：path-配置路径，v-配置值，bnoti-是否通知变化，返回：操作是否成功  |
|  `var GetCfgSz(string path,strid musthaveid=0,int getlvl=-1)`  |  获取配置项数组，参数：path-配置路径，musthaveid-必须包含的ID，getlvl-获取层级，返回：配置项数组  |
|  `var GetFunInfo(var pfun,strid keyid=0,var cmpval=NULL)`  |  获取函数信息，参数：pfun-函数对象，keyid-键ID，cmpval-比较值，返回：函数信息数组  |
|  `var GetMarcoDef(int mode=0,var pagv=NULL)`  |  获取宏定义信息，参数：mode-获取模式，pagv-参数，返回：宏定义信息数组  |
|  `var FindClassPtr(var classname,var pfindclass=NULL)`  |  查找类指针，包括脚本和C++，参数：classname-类名，pfindclass-查找类，返回：类指针  |
|  `int GetClassInfo(var& ret,var pclass,string pfinddef)`  |  获取类信息，参数：ret-输出信息数组，pclass-类指针，pfinddef-查找定义，返回：信息数量  |
|  `var GetScriptIDStr(strid kindname)`  |  获取脚本ID字符串，参数：kindname-类型名，返回：ID字符串数组  |
|  `var DefStruct(string structname,var colsz,int isclass=1)`  |  定义结构，参数：structname-结构名，colsz-列定义，isclass-是否作为类，返回：定义结果  |
----
### font
**类型**：[namespace](#namespace)　　　　**路径** ：[font:task](#font:task)
**描述**:字体任务作用域，提供字体管理功能，包括清除所有字体缓存、注册FreeType字体和图像字体
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void ClearAllCache()`  |  清除所有字体缓存，释放内存并重置字体系统状态  |
|  `bool RegFreeTypeFont(string pfontname,string pfilename,string poutmaplib=NULL)`  |  注册FreeType字体，加载字体文件并使其在沙盒环境中可用，参数：pfontname-字体名称，pfilename-字体文件名，poutmaplib-输出映射库名  |
|  `bool RegFixImgFont(string pfontname,string pimgname,int w,int h,string pimgnamehi,string poutmaplib=NULL)`  |  注册图像字体，基于图像创建字体并在沙盒环境中注册，参数：pfontname-字体名称，pimgname-图像名称，w/h-宽高，pimgnamehi-高分辨率图像，poutmaplib-输出映射库  |
----
### showcmd
**类型**：[namespace](#namespace)　　　　**路径** ：[showcmd:task](#showcmd:task)
**描述**:显示命令处理类，用于创建和管理渲染指令
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var Make(var cmd)`  |  创建显示命令对象，参数：cmd-命令数据，返回：生成的显示命令  |
----
### touch
**类型**：[namespace](#namespace)　　　　**路径** ：[touch:task](#touch:task)
**描述**:触摸事件管理任务类，处理触摸和鼠标事件
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void ClearAll()`  |  清除所有触摸状态  |
|  `int GetLinkObjNum(int id)`  |  获取指定触摸ID关联的对象数量  |
|  `void CancelOther(int id,obj pthis)`  |  取消指定触摸ID下除了指定对象外的所有其他对象  |
|  `void Cancel(int id,obj pdel)`  |  取消指定触摸ID下的指定对象  |
|  `void ChgObj(int id,obj pthis,obj pto)`  |  更改触摸事件目标对象，参数：触摸ID，原对象，新对象  |
|  `bool SetUserAgv(int id,var v)`  |  设置触摸用户数据，参数：触摸ID，数据  |
|  `void SetTouchHookObj(obj pobj)`  |  设置触摸钩子对象，用于拦截处理触摸事件  |
|  `bool RegHookKind(strid hookid,var objorclass,strid hookfunid=0)`  |  注册触摸钩子类型，参数：钩子ID，对象或类ID，钩子函数ID  |
|  `bool RegHook(obj pobj,int breg=1)`  |  注册或取消触摸钩子对象，参数：钩子对象，是否注册  |
|  `vec2 GetLastPos()`  |  获取当前光标位置  |
----
### keyboard
**类型**：[namespace](#namespace)　　　　**路径** ：[keyboard:task](#keyboard:task)
**描述**:键盘事件管理任务类，处理键盘输入和焦点控制
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Reg(obj p,int keymode=0)`  |  注册键盘焦点对象，参数：焦点对象，键盘模式  |
|  `void UnReg(obj p)`  |  取消键盘焦点对象  |
|  `bool IsReg()`  |  检查是否已注册键盘焦点  |
|  `bool IsPress(int key)`  |  检查指定键是否被按下，参数：键码  |
|  `void RegHook(obj pobj,int breg=1)`  |  注册或取消键盘钩子对象，参数：钩子对象，是否注册  |
|  `void AddKeyChar(string pstr,int bmark=0)`  |  添加字符输入，参数：字符串，标记  |
|  `void SetKeyDown(int key)`  |  模拟按键按下，参数：键码  |
|  `void SetKeyUp(int key)`  |  模拟按键释放，参数：键码  |
----
### res
**类型**：[namespace](#namespace)　　　　**路径** ：[res](#res)
**描述**:资源作用域类，提供沙盒环境中的资源管理功能，支持资源ID获取、创建、数据读取和文件访问等操作
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Start(string pdbname)`  |  资源管理器启动服务，初始化资源数据库  |
|  `string GetName(var i64,int mode=0)`  |  获取资源名称，根据ID获取资源的字符串名称，mode决定返回格式  |
|  `int64 NewID(int type=0)`  |  创建新的资源ID，可指定资源类型  |
|  `int64 GetID(var resname)`  |  根据资源名称获取资源ID  |
|  `var GetImgInfo(var img)`  |  获取图像信息，返回图像的宽高和类型  |
|  `int AddResSz(var& sz,var resname)`  |  添加资源到资源数组中，返回资源在数组中的索引  |
|  `var GetResData(var resid)`  |  获取资源数据，根据资源ID获取资源内容  |
|  `obj GetCtrl()`  |  获取资源控制器对象指针  |
|  `int GetResFile(var resname,string &locname,strid fid=0)`  |  获取资源文件，将资源文件路径保存到locname，返回文件状态  |
|  `var GetScriptRes()`  |  获取脚本资源ID  |
----
### ease
**类型**：[namespace](#namespace)　　　　**路径** ：[ease](#ease)
**描述**:这个类实现了缓动动画效果控制，用于创建和管理对象属性的平滑过渡动画，支持多种缓动模式
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Begin(strid nameid,float waitsec=0)`  |  开始创建一个动画序列，参数：名称ID，等待时间  |
|  `bool AddWait(float sec,var pvend=NULL)`  |  添加等待状态，参数：等待秒数，结束回调  |
|  `bool Ani(strid paramname,int mode,var destv,float sec,var pstart=NULL,var pvend=NULL)`  |  创建动画，参数：参数名称，模式，目标值，时间，起始值，结束回调  |
|  `void End(int looptime=0)`  |  结束动画序列，参数：循环次数  |
|  `bool Remove(strid nameid)`  |  移除指定名称的动画，参数：动画名称ID  |
|  `bool IsHave(strid nameid)`  |  检查指定动画是否存在，参数：动画名称ID  |
|  `float Cal(int mode,float t,float b , float c, float d)`  |  计算缓动值，参数：模式，当前时间，起始值，变化量，总时间  |
|  `int GetModeNum()`  |  获取缓动模式数量  |
|  `string GetModeName(int mode)`  |  获取指定缓动模式的名称，参数：模式索引  |
----
### showpath
**类型**：[namespace](#namespace)　　　　**路径** ：[showpath:showhelp](#showpath:showhelp)
**描述**:显示路径处理类，用于生成和转换UI元素显示路径的坐标系统
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var Make(obj pobj,var pidsz,obj pend)`  |  创建显示路径，参数：pobj-起始对象，pidsz-路径ID数组，pend-终止对象，返回：显示路径变量  |
|  `bool PtIn(var showpath,vec3& pt)`  |  将世界坐标转换为局部坐标，参数：showpath-显示路径，pt-坐标点(输入输出)，返回：转换是否成功  |
|  `bool PtOut(var showpath,vec3& pt)`  |  将局部坐标转换为世界坐标，参数：showpath-显示路径，pt-坐标点(输入输出)，返回：转换是否成功  |
----
### snd
**类型**：[namespace](#namespace)　　　　**路径** ：[snd:task](#snd:task)
**描述**:音频任务作用域，提供沙盒环境中音频播放和控制的接口，支持音频资源播放、停止等操作
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Play(var sndid,int val=100,int pan=0,int bglfocus=0,int loop=0)`  |  播放音频，参数：sndid-音频资源ID，val-音量(0-100)，pan-声道平衡值，bglfocus-是否后台播放，loop-是否循环播放，返回：是否成功播放  |
|  `bool Stop(var sndid)`  |  停止播放指定音频，参数：sndid-要停止的音频资源ID，返回：是否成功停止  |
----
### web
**类型**：[namespace](#namespace)　　　　**路径** ：[web:task](#web:task)
**描述**:
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetHttpHead(string pheadex)`  |  设置HTTP请求头信息，参数：pheadex-HTTP头信息字符串  |
|  `void SetMaxIdel(int maxidel=8)`  |  设置最大空闲时间，参数：maxidel-最大空闲秒数  |
|  `var Get(string purl)`  |  发送HTTP GET请求获取数据，参数：purl-URL地址，返回：函数执行结果枚举值  |
|  `var Post(string purl,string postdata)`  |  发送HTTP POST请求提交数据，参数：purl-URL地址，postdata-要提交的数据，返回：函数执行结果枚举值  |
|  `var GetRange(string purl,int st,int end)`  |  获取指定范围的HTTP数据，参数：purl-URL地址，st-起始位置，end-结束位置，返回：函数执行结果枚举值  |
|  `var GetFile(string purl,string ploc,obj pnoti)`  |  下载文件并保存到本地，参数：purl-URL地址，ploc-本地保存路径，pnoti-通知对象，返回：函数执行结果枚举值  |
----
### locapi
**类型**：[namespace](#namespace)　　　　**路径** ：[locapi:task](#locapi:task)
**描述**:本地API接口类，提供服务注册、查询和消息发送功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int IsSvr(strid nameid)`  |  检查指定名称的服务是否存在，参数：nameid-服务名称ID，返回：存在返回1，不存在返回0  |
|  `int RegSvr(strid nameid,obj pobj)`  |  注册本地服务，参数：nameid-服务名称ID，pobj-服务对象，返回：注册结果状态码  |
|  `int Post(strid nameid,strid funid,var pagv=NULL)`  |  向指定服务发送消息，参数：nameid-服务名称ID，funid-函数ID，pagv-参数，返回：发送结果状态码  |
----
### csvr::addr
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[csvr::addr](#csvr::addr)
**描述**:网络地址对象类，用于建立和管理远程服务器连接
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool LinkSvr(var pobj,var ip)`  |  链接到服务器，参数：pobj-对象引用，ip-服务器IP地址，返回：链接是否成功  |
|  `bool InitBySvrIP(string pinfo)`  |  通过服务器IP初始化连接，参数：pinfo-服务器信息字符串(svrname::ip[:port])，返回：初始化是否成功  |
|  `int IsLink()`  |  检查是否已链接，返回：链接状态码  |
|  `int IsReady()`  |  检查连接是否就绪，返回：就绪状态码  |
|  `void SetIdelMax(int maxsec)`  |  设置最大空闲时间，参数：maxsec-最大空闲秒数  |
|  `int GetIdelMax()`  |  获取最大空闲时间，返回：最大空闲秒数  |
|  `string GetIp()`  |  获取IP地址，返回：IP地址字符串  |
|  `string GetIpPort()`  |  获取IP地址和端口，返回：IP:端口格式的字符串  |
|  `int GetRBufSize()`  |  获取读缓冲区大小，返回：缓冲区大小  |
|  `int GetWBufSize()`  |  获取写缓冲区大小，返回：缓冲区大小  |
|  `var Clone(var netobj64,int newvlink=0)`  |  克隆网络对象，参数：netobj64-网络对象ID，newvlink-是否创建新的虚拟链接，返回：克隆的对象  |
|  `var GetNetObj()`  |  获取网络对象，返回：网络对象引用  |
|  `var GetAddress(var pnetobj64=NULL)`  |  获取地址信息，参数：pnetobj64-网络对象ID(可选)，返回：地址信息  |
|  `void SetNotiObj(obj pobj,int mask=1)`  |  设置通知对象，参数：pobj-接收通知的对象指针，mask-通知掩码  |
|  `bool SendCall(strid funid,var pagv=NULL,var pnetobj64=NULL)`  |  发送远程调用，参数：funid-函数ID，pagv-参数列表，pnetobj64-网络对象ID(可选)，返回：调用是否成功  |
----
### rsa::publickey
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[rsa::publickey](#rsa::publickey)
**描述**:这个类实现了RSA公钥解密功能，负责使用公钥解密由对应私钥加密的数据，支持标准RSA非对称加密
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool DecryptVar(var sv,var& dv)`  |  使用公钥解密数据，参数：sv-加密数据，dv-解密结果，返回：解密是否成功  |
|  `var GetPublicKey()`  |  获取RSA公钥，返回：公钥数据  |
|  `bool SetPublicKey(var keyv)`  |  设置RSA公钥，参数：keyv-公钥数据，返回：设置是否成功  |
----
### rsa::privateKey
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[rsa::publickey](#rsa::publickey)/[rsa::privateKey](#rsa::privateKey)
**描述**:这个类实现了RSA私钥加密功能，负责生成密钥对并使用私钥加密数据，支持1024位RSA加密标准
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void CreateKey()`  |  生成m, e, p, q; 安全级别是1024位  |
|  `var GetPrivateKey()`  |  获取RSA私钥，返回：私钥数据  |
|  `bool SetPrivateKey(var keyv)`  |  设置RSA私钥，参数：keyv-私钥数据，返回：设置是否成功  |
|  `bool EncryptVar(var sv,var& dv)`  |  使用私钥加密数据，参数：sv-原始数据，dv-加密结果，返回：加密是否成功  |
----
### file::ptr
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[file::ptr](#file::ptr)
**描述**:文件指针操作类，提供底层文件读写功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Open(string pname,int mode=0)`  |  打开文件，参数：pname-文件名，mode-打开模式(0:只读,1:写,2:读写)，返回：操作是否成功  |
|  `void Close()`  |  关闭文件，释放资源  |
|  `bool IsOk()`  |  检查文件是否成功打开，返回：文件是否可用  |
|  `int64 GetFileSize()`  |  获取文件大小，返回：文件字节数  |
|  `bool SetFileSize(var len)`  |  设置文件大小，参数：len-新的文件大小，返回：操作是否成功  |
|  `bool SetFileTime(int time)`  |  设置文件时间，参数：time-时间值，返回：操作是否成功  |
|  `int GetFileTime()`  |  获取文件时间，返回：文件的修改时间  |
|  `bool SeekWrite(var pos,var bin)`  |  在指定位置写入数据，参数：pos-写入位置，bin-二进制数据，返回：操作是否成功  |
|  `bool SeekRead(var pos,var& bin,int maxlen=0)`  |  从指定位置读取数据，参数：pos-读取位置，bin-输出数据，maxlen-最大读取长度，返回：操作是否成功  |
----
### strtree
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[strtree](#strtree)
**描述**:字符串树结构类，提供层次化的数据存储和访问功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  level  |  int  |  节点层级  |
|  subnum  |  int  |  子节点数量  |
|  ref  |  int  |  引用计数  |
|  path  |  string  |  节点完整路径  |
|  name  |  string  |  节点名称(不含路径分隔符)  |
|  isval  |  int  |  节点是否有值  |
|  pidnode  |  var  |  父节点指针  |
|  val  |  var  |  节点值  |
|  pobj  |  obj  |  关联对象指针  |
|  flag  |  int  |  节点标志  |
|  mask  |  int  |  节点掩码  |
|  datkind  |  int  |  数据类型  |
|  sortkey  |  string  |  排序键  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var Set(string path,var v,int datkind=0)`  |  设置路径对应的值，参数：path-路径，v-值，datkind-数据类型，返回：节点指针  |
|  `var Get(string path,var defv)`  |  获取路径对应的值，参数：path-路径，defv-默认值，返回：路径值  |
|  `int GetDatKind(string path,int datkind=0)`  |  获取路径对应的数据类型，参数：path-路径，datkind-默认类型，返回：数据类型  |
|  `bool Del(string path)`  |  删除路径，参数：path-路径，返回：是否成功  |
|  `var GetNode(string path)`  |  获取路径对应的节点，参数：path-路径，返回：节点指针  |
|  `void Trace()`  |  输出树结构信息到调试窗口  |
|  `void GetSubNodeSz(var& ret,int lvl=0,int datmask=0,int submask=0,int sortkind=-1)`  |  获取子节点数组，参数：ret-返回数组，lvl-层级限制，datmask-数据掩码，submask-子节点掩码，sortkind-排序方式  |
|  `void GetSubObjSz(var& ret,int lvl=0,int datmask=0,int submask=0,int sortkind=-1)`  |  获取子对象数组，参数：ret-返回数组，lvl-层级限制，datmask-数据掩码，submask-子节点掩码，sortkind-排序方式  |
|  `void DeleteSub(int lvl=0,int datmask=0,int submask=0)`  |  删除子节点，参数：lvl-层级限制，datmask-数据掩码，submask-子节点掩码  |
|  `bool SetMask(int inmask,int bset=1)`  |  设置节点掩码，参数：inmask-掩码值，bset-设置方式(1设置/0清除/-1切换)，返回：是否改变  |
|  `void SetSplit(string pcharsz)`  |  设置路径分隔符，参数：pcharsz-分隔符字符串  |
|  `void SetCallBack(obj pc,strid crfunid,strid delfunid=0,strid chgfunid=0)`  |  设置节点回调函数，参数：pc-回调对象，crfunid-创建回调ID，delfunid-删除回调ID，chgfunid-修改回调ID  |
----
### con2d::std
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[con2d:base](#con2d:base)/[con2d::std](#con2d::std)
**描述**:标准二维布局控制器类，用于管理对象的位置和大小
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sModeName  |  string  |  获取模式名称  |
|  m_nDx  |  int  |  X方向位置偏移  |
|  m_nDy  |  int  |  Y方向位置偏移  |
|  m_nMinW  |  int  |  最小宽度  |
|  m_nMinH  |  int  |  最小高度  |
|  m_nMaxW  |  int  |  最大宽度  |
|  m_nMaxH  |  int  |  最大高度  |
|  m_nAlignH  |  int  |  获取水平对齐方式  |
|  m_nAlignV  |  int  |  获取垂直对齐方式  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetMode(strid modesid,int dx=0,int dy=0)`  |  设置布局模式，参数：模式ID，X偏移，Y偏移  |
|  `void SetAlign(int h=0,int v=0)`  |  设置对齐方式，参数：水平对齐，垂直对齐  |
|  `void SetLimit(int minw,int minh,int maxw,int maxh)`  |  设置尺寸限制，参数：最小宽度，最小高度，最大宽度，最大高度  |
----
### con2d:base
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[con2d:base](#con2d:base)
**描述**:界面布局容器基类，负责管理UI组件的位置和边框布局
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vBorder  |  vec4  |  边框矩形  |
|  m_fBorderLeft  |  float  |    |
|  m_fBorderTop  |  float  |    |
|  m_fBorderRight  |  float  |    |
|  m_fBorderBottom  |  float  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void LinkNeedPlace()`  |  通知链接对象需要重新布局，返回：无  |
|  `void SetBorder(float left,float top,float right,float bottom)`  |  设置边框大小，参数：left-左边距，top-上边距，right-右边距，bottom-下边距，返回：无  |
|  `void SetMoveFun(var v)`  |  设置移动函数，参数：v-移动函数变量，返回：无  |
----
### con2d::tab
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[con2d:base](#con2d:base)/[con2d::tab](#con2d::tab)
**描述**:表格式二维布局控制器类，用于管理按列排列的对象布局
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fDx  |  float  |  X方向浮点偏移量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void AddCol(float w,var def)`  |  添加列，参数：宽度，默认值  |
|  `bool SetColW(int no,float w)`  |  设置列宽度，参数：列号，宽度  |
|  `bool SetColDef(int no,var def)`  |  设置列定义，参数：列号，定义  |
|  `bool GetColDef(int no,var& ret)`  |  获取列定义，参数：列号，返回值  |
|  `void CreateCol(int num,float defw=50)`  |  创建指定数量的列，参数：列数，默认宽度  |
----
### ani2d
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)/[ani2d](#ani2d)
**描述**:2D动画资源指针类，用于管理和操作2D动画资源
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  获取动画名称  |
|  m_vImgSz  |  var  |  设置动画图像集，参数：v-图像集  |
|  m_nTrackNum  |  int  |  获取当前轨道数量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(string fname)`  |  加载动画数据，参数：fname-文件名  |
|  `bool Save(string fname)`  |  保存动画数据到文件，参数：fname-文件名  |
|  `void Destroy()`  |  销毁动画数据  |
|  `bool AddKind(string pname)`  |  添加动画类型，参数：pname-类型名称  |
|  `int AddTrack(string pname,int w,int h,int imgno)`  |  添加动画轨道，参数：pname-轨道名称，w-宽度，h-高度，imgno-图像编号  |
|  `bool DelTrack(int tno)`  |  删除动画轨道，参数：tno-轨道编号  |
|  `var GetKindSz()`  |  获取动画类型数组  |
|  `void SetImgSz(var imgsz)`  |  设置动画图像集，参数：imgsz-图像集  |
|  `bool SetCurKind(strid kid)`  |  设置当前动画类型，参数：kid-类型ID  |
|  `var GetCurTrack(int trno,int mode=0)`  |  获取当前轨道数据，参数：trno-轨道编号，mode-获取模式  |
|  `bool SetCurTrack(int trno,var dat)`  |  设置当前轨道数据，参数：trno-轨道编号，dat-轨道数据  |
|  `bool ChgCurTrack(int f,int to)`  |  调整当前轨道顺序，参数：f-起始位置，to-目标位置  |
|  `int AddFrameKey(int trno,float t,var pdef=NULL)`  |  添加帧关键点，参数：trno-轨道编号，t-时间位置，pdef-关键点定义  |
|  `bool DelFrameKey(int trno,int no)`  |  删除帧关键点，参数：trno-轨道编号，no-帧编号  |
|  `var GetFrameKey(int trno,int keyno,strid mode)`  |  获取帧关键点数据，参数：trno-轨道编号，keyno-关键点编号，mode-获取模式  |
|  `bool SetFrameKey(int trno,int keyno,var v)`  |  设置帧关键点数据，参数：trno-轨道编号，keyno-关键点编号，v-关键点数据  |
|  `bool SetFrameKeyPt(int trno,int keyno,int ptnum,strid mode,var v)`  |  设置帧关键点的具体属性，参数：trno-轨道编号，keyno-关键点编号，ptnum-点编号，mode-属性模式，v-属性值  |
----
### resdatptr
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)
**描述**:
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var GetName()`  |    |
----
### img
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)/[img](#img)
**描述**:图像资源类，用于管理和操作图像数据
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  width  |  int  |  图像宽度(像素)  |
|  height  |  int  |  图像高度(像素)  |
|  imgkind  |  int  |  图像格式类型  |
|  imgbyteper  |  int  |  图像每像素字节数  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(string fname)`  |  加载图像文件，参数：fname-文件名  |
|  `bool GetImgData(var& pret,strid format,int q=90)`  |  获取图像二进制数据，参数：pret-返回数据，format-格式(jpg/png)，q-压缩质量  |
|  `bool SetImgData(var data)`  |  从二进制数据设置图像，参数：data-图像数据  |
|  `bool Create(int w,int h)`  |  创建指定大小的空白图像，参数：w-宽度，h-高度  |
|  `void Clear(color color=0)`  |  清除图像内容，参数：color-背景色  |
|  `void Bar(int x1,int y1,int w,int h,color color)`  |  绘制矩形，参数：x1-左上角x，y1-左上角y，w-宽度，h-高度，color-颜色  |
|  `void PutPixel(int x,int y,color color,int alpha=255)`  |  设置像素点，参数：x-横坐标，y-纵坐标，color-颜色，alpha-透明度  |
|  `int GetPixel(int x,int y)`  |  获取像素点颜色，参数：x-横坐标，y-纵坐标，返回：颜色值  |
|  `void FillCircle(int x1,int y1,int x2,int y2,color color)`  |  绘制实心圆，参数：x1,y1-左上角，x2,y2-右下角，color-颜色  |
|  `void Blur(int x1, int y1, int x2, int y2,int radius=2)`  |  对指定区域进行模糊处理，参数：x1,y1-左上角，x2,y2-右下角，radius-模糊半径  |
|  `void Line(int x1,int y1,int x2,int y2,color color,int steps=1)`  |  绘制直线，参数：x1,y1-起点，x2,y2-终点，color-颜色，steps-线宽  |
|  `void Bit(var pimg,int x,int y)`  |  将另一张图像拷贝到当前图像，参数：pimg-源图像，x,y-目标位置  |
|  `bool SetAlphaImg(var imgres)`  |  设置透明通道图像，参数：imgres-透明度图像  |
|  `bool SavePng(string pname)`  |  保存为PNG格式图像，参数：pname-文件名  |
----
### sndbuf
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)/[sndbuf](#sndbuf)
**描述**:音频缓冲区类，负责加载、保存和播放音频资源，提供音频数据的基本操作和播放控制功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(string fname)`  |  加载声音文件，参数：fname-文件名，返回：成功返回true，失败返回false  |
|  `bool Save(string fname,int mode=0)`  |  保存声音文件，参数：fname-文件名，mode-保存模式，返回：成功返回true，失败返回false  |
|  `bool Play(int val,int pan,int bloop=0)`  |  播放声音，参数：val-音量(0-100)，pan-声道平衡(-100左声道,0居中,100右声道)，bloop-是否循环播放，返回：成功返回true，失败返回false  |
|  `bool IfPlaying()`  |  检查声音是否正在播放，返回：true表示正在播放，false表示未播放  |
|  `bool Stop()`  |  停止播放声音，返回：成功返回true，失败返回false  |
|  `bool SetValume(float val)`  |  设置音量，参数：val-音量值(0.0-1.0)，返回：成功返回true，失败返回false  |
----
### font::text
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[font::text](#font::text)
**描述**:文本渲染类，用于管理字体、文本内容和绘制属性
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sText  |  string  |  获取文本内容  |
|  m_nFontW  |  int  |  获取字体宽度  |
|  m_nFontEx  |  int  |  获取字体扩展模式  |
|  m_nItalic  |  int  |  获取字体斜体设置  |
|  m_nWeight  |  int  |  获取字体粗细  |
|  m_nTextColor  |  color  |  获取文本颜色  |
|  m_nColorEx  |  color  |  获取扩展颜色  |
|  m_nAlign  |  int  |  获取文本对齐方式  |
|  m_nFixRect  |  int  |  获取固定矩形模式  |
|  m_fX  |  float  |  X坐标  |
|  m_fY  |  float  |  Y坐标  |
|  m_fZ  |  float  |  Z坐标  |
|  m_vPos2  |  vec2  |  2D位置向量  |
|  m_vPos  |  vec3  |  3D位置向量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void SetText(string ptext)`  |  设置文本内容，参数：ptext-文本字符串  |
|  `string GetText()`  |  获取当前文本内容  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名称，w-宽度，h-高度，weight-粗细，bItalic-斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-宽度，h-高度  |
|  `void SetTextColor(color c)`  |  设置文本颜色，参数：c-颜色值  |
|  `void SetFixRect(int b)`  |  设置固定矩形模式，参数：b-模式(1为行高固定，2为矩形固定)  |
|  `void SetAlign(int h=0,int v=0)`  |  设置对齐方式，参数：h-水平对齐(0左对齐，1居中，2右对齐)，v-垂直对齐(0上对齐，1居中，2下对齐)  |
|  `void SetPos(float x,float y,float z=0)`  |  设置文本位置，参数：x,y,z-坐标位置  |
|  `void DrawTo(var pimg)`  |  绘制文本到图像，参数：pimg-目标图像  |
----
### draw::cmdsz
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[draw::cmdsz](#draw::cmdsz)
**描述**:绘图命令集合类，用于管理和执行渲染命令
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Destroy()`  |  清空所有绘图命令  |
|  `void BeginDraw(int reset=1)`  |  开始绘图，参数：reset-是否重置状态(1重置)  |
|  `void SetLineMode(float linew,int linemode=0,float anispeed=0)`  |  设置线条模式，参数：linew-线宽，linemode-线型，anispeed-动画速度  |
|  `void SetColor(color c1,color c2,color c3=0,color c4=0)`  |  设置颜色，参数：c1-颜色1，c2-颜色2，c3-颜色3，c4-颜色4  |
|  `void SetFont(string pfontname,int w,int h=0,int weight=0,int bItalic=0,int modeex=0)`  |  设置字体，参数：pfontname-字体名称，w-宽度，h-高度，weight-粗细，bItalic-斜体，modeex-扩展模式  |
|  `void SetFontSize(int w,int h=0)`  |  设置字体大小，参数：w-宽度，h-高度  |
|  `void SetFontWeight(int w)`  |  设置字体粗细，参数：w-粗细值  |
|  `void SetAlign(int hv)`  |  设置对齐方式，参数：hv-水平垂直对齐值  |
|  `void Line(float x1,float y1,float x2,float y2,color color=0)`  |  绘制线段，参数：x1,y1-起始点坐标，x2,y2-结束点坐标，color-线条颜色  |
|  `void Bar(float x,float y,float w,float h,color color=0)`  |  绘制矩形，参数：x,y-左上角坐标，w,h-宽高，color-填充颜色  |
|  `void SetClip(float left,float top,float right,float bottom,int binout=0)`  |  设置裁剪区域，参数：left,top,right,bottom-矩形边界，binout-是否外部裁剪  |
|  `void OffSetRect(float left,float top,float right,float bottom,int bin=0)`  |  偏移矩形区域，参数：left,top,right,bottom-偏移量，bin-是否启用  |
|  `void SetRect(float left,float top,float right,float bottom)`  |  设置矩形区域，参数：left,top,right,bottom-矩形边界  |
|  `void SetPosR(float x,float y,float r)`  |  设置中心点和半径，参数：x,y-中心点坐标，r-半径  |
|  `void Shape(color fillc,color linec=0,float r=0,float fade=0)`  |  设置形状样式，参数：fillc-填充颜色，linec-线条颜色，r-圆角半径，fade-渐变效果  |
|  `void Text(float x,float y,string ptext,color color=0)`  |  绘制文本，参数：x,y-文本位置，ptext-文本内容，color-文本颜色  |
|  `void EndDraw()`  |  结束绘图  |
----
### material
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[material](#material)
**描述**:材质管理类，用于定义和处理3D模型的PBR材质属性和贴图
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  name  |  string  |  名称  |
|  OpacityMode  |  int  |  透明模式;enum=(0,'不透明',1,'硬边',2,'Alpha')  |
|  bdouble  |  bool  |  强制双面  |
|  color  |  color  |  基本颜色  |
|  colorimg  |  GL_ImgPtr  |  颜色图  |
|  bwrap  |  bool  |  颜色图/环绕  |
|  lodoffset  |  float  |  颜色图/LOD偏移;range=(-2,2)  |
|  aniUV  |  vec2  |  颜色图/UV动画  |
|  normalimg  |  GL_ImgPtr  |  法线图  |
|  normalinvx  |  bool  |  法线图/red(x)反转  |
|  normalinvy  |  bool  |  法线图/green(y)反转  |
|  normalmix  |  float  |  法线图/系数;range=(0,1)  |
|  metallic  |  float  |  金属度;range=(0,1)  |
|  roughness  |  float  |  粗糙度;range=(0,1)  |
|  f0  |  float  |  镜面反射;range=(0,1)  |
|  parallaximg  |  GL_ImgPtr  |  高度图?视差偏移  |
|  parallax  |  float  |  高度图/偏移系数;range=(0,15)  |
|  bpshadow  |  bool  |  高度图/自阴影  |
|  parallaxhigh  |  bool  |  高度图/浮雕映射?高精度  |
|  metallicimg  |  GL_ImgPtr  |  混合贴图?r=金属度,\n可选[g=光滑度,b=F0]  |
|  wireline  |  color  |  线框颜色  |
|  emissive  |  color  |  自发光  |
|  matuseragv  |  var  |  自定义  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void GetLinkRes(var& ressz)`  |  获取所有链接资源列表，参数：ressz-存储资源列表的变量  |
----
### ani3d
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)/[ani3d](#ani3d)
**描述**:3D动画资源指针类，用于管理和操作3D模型、动画、材质和节点数据
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pLinkAni  |  ptrex  |  获取链接动画对象  |
|  m_sName  |  string  |  获取3D模型名称  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(string fname)`  |  加载3D动画数据，参数：fname-文件名  |
|  `bool Append(string fname)`  |  追加加载3D动画数据，参数：fname-文件名  |
|  `bool Save(string fname)`  |  保存3D动画数据，参数：fname-文件名  |
|  `bool ImportAni(string fname)`  |  导入动画数据，参数：fname-文件名  |
|  `bool LinkAni(var actname)`  |  链接动画，参数：actname-动画名称  |
|  `void GetLinkRes(var& ressz)`  |  获取链接资源列表  |
|  `int GetAniNum()`  |  获取动画数量  |
|  `var GetAni(int no=-1)`  |  获取动画信息，参数：no-动画编号(-1表示所有)  |
|  `var GetAniDat(int no)`  |  获取动画数据，参数：no-动画编号  |
|  `bool SetAniDat(var val)`  |  设置动画数据，参数：val-动画数据  |
|  `int FindAniNo(strid aninameid)`  |  查找动画编号，参数：aninameid-动画名称ID  |
|  `var GetAniTrack(int anino)`  |  获取动画轨道数据，参数：anino-动画编号  |
|  `int GetMaterialNum()`  |  获取材质数量  |
|  `var GetMaterial(int no=-1)`  |  获取材质信息，参数：no-材质编号(-1表示所有)  |
|  `int FindMaterial(string pname)`  |  查找材质编号，参数：pname-材质名称  |
|  `bool SetMaterial(int no,strid paramid,var val)`  |  设置材质参数，参数：no-材质编号，paramid-参数ID，val-参数值  |
|  `int GetModelNum()`  |  获取模型数量  |
|  `var GetModel(int no=-1)`  |  获取模型信息，参数：no-模型编号(-1表示所有)  |
|  `int GetNodeNum()`  |  获取节点数量  |
|  `var GetNode(int no=-1)`  |  获取节点信息，参数：no-节点编号(-1表示所有)  |
|  `var GetTag(int no=-1)`  |  获取标签信息，参数：no-标签编号(-1表示所有)  |
|  `void SetTagSz(var tagsz)`  |  设置标签数组，参数：tagsz-标签数组  |
|  `var GetCullSphere(int no=-1)`  |  获取碰撞球信息，参数：no-碰撞球编号(-1表示所有)  |
|  `void SetUserAgv(string pname,var dat)`  |  设置用户自定义数据，参数：pname-名称，dat-数据  |
|  `var GetUserAgv(string pname)`  |  获取用户自定义数据，参数：pname-名称  |
|  `void CreateSphere(float r,int level=0,float u=1,float v=1)`  |  创建球体模型，参数：r-半径，level-细分级别，u-U贴图坐标，v-V贴图坐标  |
|  `void CreateFace(float w,float h,float u=1,float v=1)`  |  创建平面模型，参数：w-宽度，h-高度，u-U贴图坐标，v-V贴图坐标  |
|  `bool SetPerviewData(var picdata)`  |  设置预览数据，参数：picdata-图片数据  |
|  `var GetPerviewData()`  |  获取预览数据  |
|  `var GetPerviewImg()`  |  获取预览图像  |
|  `var GetSkBoneCode()`  |  获取骨骼编码  |
----
### particle
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[resdatptr](#resdatptr)/[particle](#particle)
**描述**:粒子定义类，用于管理粒子系统的整体配置和组成
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  粒子系统名称  |
|  m_nTotalTime  |  int  |  总时长,豪秒,def=-1  |
|  m_vSndName  |  var  |  音效资源,类型:res(snd),def=nil  |
|  m_nSndVal  |  int  |  音量,def=100  |
|  m_nPlaySpeed  |  int  |  播放速度,def=1000  |
|  m_fWdLightR  |  float  |  全局灯光半径,def=0  |
|  m_vWdLightColor  |  vec3  |  全局灯光颜色,def=v3(0,0,0)  |
|  m_vWdLightPos  |  vec3  |  全局灯光位置,def=v3(0,0,0)  |
|  m_fScale  |  float  |  缩放比例,def=1  |
|  m_fSelecR  |  float  |  选择球半径,def=1  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool Load(string fname)`  |  加载粒子定义，参数：fname-文件名，返回：是否加载成功  |
|  `bool SetAsText(string pstr)`  |  从文本设置粒子定义，参数：pstr-文本内容，返回：是否设置成功  |
|  `var GetAtomSz()`  |  获取原子列表  |
|  `var AddAtom(string pclassname)`  |  添加原子，参数：pclassname-原子类名，返回：添加的原子  |
|  `bool DelAtom(int no)`  |  删除原子，参数：no-原子索引，返回：是否删除成功  |
----
### atom::Atom
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atombase](#.atombase)/[atom::Atom](#atom::Atom)
**描述**:粒子,基本粒子
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  名字,def=""  |
|  m_nVisualQuota  |  int  |  最大粒子数,def=999  |
|  m_Texture  |  GL_ImgPtr  |  贴图  |
|  m_nShowMode  |  int  |  显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=0  |
|  m_nWorldSpace  |  int  |  是否世界坐标,类型:枚举(0=否,1=是 绑定对象失效),def=0,  |
|  m_nBindToPos  |  int  |    |
|  m_nBindObjNo  |  int  |  坐标系绑定对象,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=0,  |
|  m_sBTagName  |  string  |  坐标系Tag名,设置序号:tagname,def=""  |
|  m_fMass  |  float  |  粒子质量,def=1  |
|  m_nBillboardKind  |  int  |  公告板模式,类型:枚举(0=无,1=照相机,2=保持方向),def=1  |
|  m_nAlginOrg  |  int  |  对齐方式,类型:枚举(0=lefttop,1=centertop,2=righttop,3=leftcenter,4=centercenter,5=rightcenter,6=leftbottom,7=centerbottom,8=rightbottom,9=镜像中心),def=4  |
|  m_fSpeedStretch  |  float  |  速度拉伸,def=0  |
|  m_fBiasSlope  |  float  |  显示Z偏移,def=0  |
|  m_vAtomScale  |  var  |  粒子大小,类型:GFloatTimerSz,def=1  |
|  m_vAtomRed  |  var  |  粒子Red,类型:GFloatTimerSz,def=1  |
|  m_vAtomGreen  |  var  |  粒子Green,类型:GFloatTimerSz,def=1  |
|  m_vAtomBlue  |  var  |  粒子Blue,类型:GFloatTimerSz,def=1  |
|  m_vAtomAlpha  |  var  |  粒子Alpha,类型:GFloatTimerSz,def=1  |
|  m_vBindModel  |  var  |  模型名,类型:res(3dani),def=nil  |
|  m_fFrameBegin  |  float  |  模型起始帧,def=0  |
|  m_fFrameEnd  |  float  |  模型结束帧,def=1000  |
|  m_fAniU  |  float  |  贴图动画U,def=0,UV动画速度 u分量  |
|  m_fAniV  |  float  |  贴图动画V,def=0,UV动画速度 v分量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Enable(int bable)`  |  设置粒子系统的启用状态，参数：bable-是否启用(0=禁用,1=启用)  |
|  `void MakeAtom(int life,vec3 pos,vec3 speeddir,float sizew=1.0f,float angle=0,float sizeh=0.0f)`  |  创建一个新粒子，参数：life-生命周期(毫秒)，pos-生成位置，speeddir-速度方向，sizew-宽度，angle-旋转角度，sizeh-高度  |
|  `void PlayAt(vec3 pos,float angle=0)`  |  在指定位置播放粒子效果，参数：pos-播放位置，angle-旋转角度(度)  |
----
### .atombase
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atombase](#.atombase)
**描述**:粒子原子基类，粒子系统的基本构建单元
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pDef  |  ptrex  |  获取粒子定义  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `var GetCtrlSz()`  |  获取控制器列表  |
|  `var AddCtrl(string pclassname)`  |  添加控制器，参数：pclassname-控制器类名，返回：添加的控制器  |
|  `bool DelCtrl(int no)`  |  删除控制器，参数：no-控制器索引，返回：是否删除成功  |
----
### atom::Emitter
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Emitter](#atom::Emitter)
**描述**:点发生器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nEmitRate  |  int  |  发生数量,发生间隔内发生粒子数量，单位为个,def=5  |
|  m_nChanceToEmit  |  int  |  发生几率,单位为百分比,def=100  |
|  m_nEmitDuration  |  int  |  持续时间,发生粒子的持续时间,def=1000  |
|  m_nDelay  |  int  |  发生间隔,发生粒子持续时间结束后距离下一次发生粒子之间的时间,def=0  |
|  m_nDelayFirst  |  int  |  首次延迟,第一次发生粒子之前延迟,def=0  |
|  m_nNumLoops  |  int  |  循环次数,-1为无限循环0为只发生一次不循环,def=-1  |
|  m_vPosition  |  vec3  |  发生坐标,设置粒子发生器的坐标,def=v3(0,0,0)  |
|  m_nBindObjNo  |  int  |  起点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0  |
|  m_sBTagName  |  string  |  起点对象Tag名,设置序号:tagname,def=""  |
|  m_vDirection  |  vec3  |  粒子方向,设置发生粒子的方向,def=v3(0,0,1)  |
|  m_nDirKind  |  int  |  方向类型,类型:枚举(0=无,1=人物方向,2=人物目标,10=发生绑定),def=0  |
|  m_fVelocity  |  var  |  初速率,类型:GFloatTimerSz  |
|  m_fAngle  |  var  |  粒子偏转,类型:GFloatTimerSz设置发生粒子在方向上的偏转角度,def=40  |
|  m_nRotoKind  |  int  |  偏转类型,类型:枚举(0=无,1=人物方向,2=人物目标),def=0  |
|  m_fRoll  |  var  |  粒子自旋,类型:GFloatTimerSz设置发生粒子的自旋  |
|  m_fParticleLife  |  var  |  生命周期,类型:GFloatTimerSz  |
|  m_fStartSize  |  float  |  粒子宽度,发生粒子的初始宽度,def=1  |
|  m_fStartHeight  |  float  |  粒子高度,发生粒子的初始高度,def=0  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void MakeAt(vec3 pos,float fw)`  |  在指定位置生成粒子，参数：pos-位置，fw-宽度因子  |
----
### .atomctrl
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)
**描述**:粒子控制基类，用于控制粒子的运动、生成和特性
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_pAtom  |  ptrex  |  获取关联的粒子原子  |
----
### atom::ELine
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Emitter](#atom::Emitter)/[atom::ELine](#atom::ELine)
**描述**:线形发生器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vEndPosition  |  vec3  |  终点坐标  |
|  m_nEndBindObjNo  |  int  |  终点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0  |
|  m_sEndTag  |  string  |  终点对象Tag名,设置序号:tagname,def=""  |
|  m_fMaxDeviation  |  float  |  坐标误差,def=0.05  |
----
### atom::ECircle
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Emitter](#atom::Emitter)/[atom::ECircle](#atom::ECircle)
**描述**:圆形发生器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fMinRadius  |  float  |  最小半径,def=1  |
|  m_fMaxRadius  |  float  |  最大半径,def=1  |
|  m_fStartStep  |  float  |  起始角度,def=0  |
|  m_fStep  |  float  |  步进角度,def=10  |
----
### atom::EBox
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Emitter](#atom::Emitter)/[atom::EBox](#atom::EBox)
**描述**:盒形发生器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fWidth  |  float  |  Box宽X,def=1  |
|  m_fHeight  |  float  |  Box高Y,def=1  |
|  m_fDepht  |  float  |  Box深Z,def=1  |
----
### atom::ESphere
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Emitter](#atom::Emitter)/[atom::ESphere](#atom::ESphere)
**描述**:球形发生器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fMinRadius  |  float  |  球半径,def=3  |
|  m_nIsHalf  |  int  |  是否半球,类型:枚举(0=否,1=是),def=1  |
----
### atom::Fire
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Fire](#atom::Fire)
**描述**:目标飞行,粒子控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nBindObjNo  |  int  |  起点对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0  |
|  m_sBindTagName  |  string  |  起点对象Tag名,设置序号:tagname  |
|  m_nDelayFirst  |  int  |  首次延迟,第一次发生粒子之前延迟,def=1  |
|  m_fFlySpeed  |  float  |  飞行速度,飞行速度,def=1  |
|  m_fSinT  |  float  |  发射角度,发射角度,def=30  |
|  m_sEnterAct  |  string  |  爆炸粒子  |
|  m_sDMake  |  string  |  尾烟粒子  |
|  m_fParticleLife  |  float  |  尾烟生命  |
|  m_fMakeLen  |  float  |  尾烟间隔,尾烟间隔,def=0.2  |
|  m_sDMake2  |  string  |  尾烟粒子2  |
|  m_fParticleLife2  |  float  |  尾烟生命2  |
|  m_fMakeLen2  |  float  |  尾烟2间隔,尾烟2间隔,def=0.2  |
|  m_vStartOff  |  vec3  |  起点偏移,粒子发生偏移坐标,def=v3(0,0,1)  |
|  m_vEndOff  |  vec3  |  终点偏移,粒子发生偏移坐标,def=v3(0,0,1)  |
----
### atom::Roto
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Roto](#atom::Roto)
**描述**:旋转,粒子控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fRotationSpeed  |  var  |  旋转速率,类型:GFloatTimerSz  |
----
### atom::Jet
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Jet](#atom::Jet)
**描述**:加速,粒子控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_fAcceleration  |  var  |  加速度,类型:GFloatTimerSz  |
----
### atom::Gravity
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Gravity](#atom::Gravity)
**描述**:重力,粒子控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vGravity  |  vec3  |  重力方向,控制粒子加速方向  |
----
### atom::Vortex
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Vortex](#atom::Vortex)
**描述**:漩涡
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vPosition  |  vec3  |  中心坐标  |
|  m_vDirection  |  vec3  |  旋转轴方向  |
|  m_fRate  |  float  |  旋转离心力  |
|  m_fAngle  |  float  |  方向偏角  |
----
### atom::GWell
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::GWell](#atom::GWell)
**描述**:引力点
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vPosition  |  vec3  |  中心坐标,def=v3(0,0,0)  |
|  m_fRate  |  var  |  引力加速,类型:GFloatTimerSz  |
|  m_fGg  |  float  |  加速比率  |
|  m_fRad  |  float  |  核心半径  |
|  m_nBindObjNo  |  int  |  绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0  |
|  m_sBindTagName  |  string  |  绑定对象Tag名,设置序号:tagname  |
|  m_sEnterAct  |  string  |  点进入启动粒子  |
----
### atom::Snd
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Snd](#atom::Snd)
**描述**:声音,控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vSndName  |  var  |  音效资源,类型:res(snd),def=nil  |
|  m_nSndVal  |  int  |  音量,def=100  |
|  m_nDelay  |  int  |  发生间隔,发生粒子持续时间结束后距离下一次发生粒子之间的时间,def=0  |
|  m_nDelayFirst  |  int  |  首次延迟,第一次发生粒子之前延迟,def=0  |
|  m_nNumLoops  |  int  |  循环次数,-1为无限循环0为只发生一次不循环def=1  |
----
### atom::Track
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::Track](#atom::Track)
**描述**:追踪
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_vPosition  |  vec3  |  中心坐标  |
|  m_nBindObjNo  |  int  |  绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它,5=坐标1,6=坐标2),def=0  |
|  m_sBindTagName  |  string  |  绑定对象Tag名,设置序号:tagname  |
|  m_fMaxSpeed  |  float  |  最大速度  |
|  m_fG  |  float  |  加速度  |
|  m_fRt  |  float  |  转角速度,0-1 速度大转方向快  |
|  m_sEnterAct  |  string  |  点进入启动粒子  |
----
### atom::ActRibbon
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atombase](#.atombase)/[atom::ActRibbon](#atom::ActRibbon)
**描述**:动作条带,基本粒子
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  粒子条带的名称  |
|  m_Texture  |  GL_ImgPtr  |  粒子条带的贴图纹理  |
|  m_fUScale  |  float  |  贴图U比例,def=1  |
|  m_nRed  |  int  |  条带颜色的红色分量(0-255),def=255  |
|  m_nGreen  |  int  |  条带颜色的绿色分量(0-255),def=255  |
|  m_nBlue  |  int  |  条带颜色的蓝色分量(0-255),def=255  |
|  m_nShowMode  |  int  |  显示方式,类型:枚举(0=正常,1=2X,2=亮度叠加,3=亮度相减,4=取最大值),def=2  |
|  m_nBindObjNo  |  int  |  绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=1  |
|  m_sBTag  |  string  |  条带起点绑定的目标标签名称  |
|  m_sAniName  |  string  |  条带使用的动画名称  |
|  m_fStartSteps  |  float  |  开始帧数,从指定帧开始生成  |
|  m_fEndSteps  |  float  |  条带生成的结束帧数  |
|  m_fTick  |  float  |  条带生成的帧间隔(0.01-0.9，越小生成越密集)  |
|  m_vMakeP1  |  vec3  |  条带生成的起点坐标  |
|  m_vMakeP2  |  vec3  |  条带生成的终点坐标  |
|  m_fOutSpeed  |  float  |  条带的离心扩散速度  |
|  m_fShowTick  |  float  |  条带的拖尾持续时间  |
|  m_fAlpha  |  float  |  透明比例,def=1  |
|  m_nLoop  |  int  |  循环,类型:枚举(0=单次,1=循环),def=0  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Start()`  |  重置并开始生成新的条带  |
|  `void Enable(int bable)`  |  设置条带效果的启用状态，参数：bable-是否启用(0=禁用,1=启用)  |
----
### atom::Ribbon
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atombase](#.atombase)/[atom::Ribbon](#atom::Ribbon)
**描述**:粒子条带,基本粒子
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  粒子条带的名称  |
|  m_Texture  |  GL_ImgPtr  |  粒子条带的贴图纹理  |
|  m_nShowMode  |  int  |  显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=2  |
|  m_nBindObjNo  |  int  |  绑定对象序号,类型:枚举(0=无,1=人物,2=目标,3=武器,4=其它),def=0  |
|  m_sBTag  |  string  |  条带起点绑定的目标标签名称  |
|  m_nOutTimer  |  int  |  条带的拖尾持续时间(毫秒)  |
|  m_fSpeedScale  |  float  |  条带的速度对透明度的影响系数  |
|  m_fAlpha  |  float  |  条带的基础透明度(0-1),def=1.0  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Start()`  |  重置并开始生成新的条带  |
----
### atom::R_BindObj
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::R_BindObj](#atom::R_BindObj)
**描述**:条带控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nBindObjNo  |  int  |  绑定对象的类型编号，0=无,1=人物,2=目标,3=武器,4=其它  |
|  m_sBTag  |  string  |  粒子发射起点的标签名称  |
|  m_vSOff  |  vec3  |  粒子发射起点的位置偏移量  |
|  m_sETag  |  string  |  粒子发射终点的标签名称  |
|  m_vEOff  |  vec3  |  粒子发射终点的位置偏移量  |
|  m_nDelayFirst  |  int  |  粒子系统首次发射前的延迟时间(毫秒)  |
|  m_nDuration  |  int  |  粒子系统持续发射的时间(毫秒)  |
----
### atom::R_Twist
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atomctrl](#.atomctrl)/[atom::R_Twist](#atom::R_Twist)
**描述**:条带缠绕控制器
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_nBindObjNo  |  int  |  绑定对象的类型编号，0=无,1=人物,2=目标,3=武器,4=其它  |
|  m_sBTag  |  string  |  粒子发射起点的标签名称  |
|  m_vSOff  |  vec3  |  粒子发射起点的位置偏移量  |
|  m_nDelayFirst  |  int  |  粒子系统首次发射前的延迟时间(毫秒)  |
|  m_nDuration  |  int  |  粒子系统持续发射的时间(毫秒)  |
|  m_nRotoMode  |  int  |  缠绕轴向，0=绕X轴,1=绕Y轴,2=绕Z轴  |
|  m_fRWidth  |  float  |  粒子条带的宽度(米)  |
|  m_fRotoTime  |  float  |  完成一次完整旋转所需的时间(秒)  |
|  m_vRad  |  var  |  粒子条带的旋转半径，类型:GFloatTimerSz  |
|  m_vOff  |  var  |  粒子条带在旋转轴向上的位置偏移，类型:GFloatTimerSz  |
----
### atom::Snow
**类型**：[ptrex](#ptrex)　　　　**路径** ：[ptrex](#ptrex)/[.atombase](#.atombase)/[atom::Snow](#atom::Snow)
**描述**:粒子雪花系统类，用于创建和管理雪花粒子特效
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  m_sName  |  string  |  名字  |
|  m_nMaxSnow  |  int  |  最大粒子数  |
|  m_nTestCross  |  int  |  碰撞方式,类型:枚举(0=无,1=世界碰撞)  |
|  m_Texture  |  GL_ImgPtr  |  贴图  |
|  m_nShowMode  |  int  |  显示方式,类型:枚举(0=正常,1=世界光照,2=亮度叠加,3=颜色叠加,4=2X),def=0  |
|  m_fScale  |  float  |  粒子大小  |
|  m_vDirection  |  vec3  |  运动方向,设置粒子运动的基本方向  |
|  m_fAngle  |  float  |  偏转扰动,方向上的偏转角度  |
|  m_fSpeedOut  |  float  |  扰动系数,数字越大越明显  |
|  m_nSnowW  |  int  |  半长宽,米  |
|  m_nTop  |  int  |  顶高,米  |
|  m_nBottom  |  int  |  底,米  |
|  m_nRed  |  int  |  粒子红色,0-255  |
|  m_nGreen  |  int  |  粒子绿色,0-255  |
|  m_nBlue  |  int  |  粒子蓝色,0-255  |
|  m_nAlpha  |  int  |  粒子Alpha,0-255  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Start()`  |    |
|  `void Stop()`  |    |
----
### all kind
**类型**：[varkind](#varkind)　　　　**路径** ：[var:void](#var:void)
**描述**:
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  size  |  int  |  变量大小  |
|  isnil  |  int  |  是否为空值  |
|  isobj  |  int  |  是否为对象  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int GetType()`  |  获取变量类型ID  |
|  `string GetTypeName()`  |  获取变量类型名称  |
|  `string GetTrace(GBR_Task *pTask,int mode=0)`  |  取调试信息  |
|  `void Trace(GBR_Task *pTask,color c=0)`  |  输出调试信息  |
|  `bool IsEmpty()`  |  检查变量是否为空  |
|  `bool IsInt()`  |  是否为整数  |
|  `bool IsInt64()`  |  是否为int64  |
|  `bool IsFloat()`  |  是否为浮点数  |
|  `bool IsNum()`  |  是否为数字  |
|  `bool IsPtr()`  |  是否为ptr  |
|  `bool IsSz()`  |  是否为数组  |
|  `bool IsString()`  |  是否为字符串  |
|  `bool IsVec2()`  |  是否为2D向量  |
|  `bool IsVec3()`  |  是否为3D向量  |
|  `bool IsVec4()`  |  是否为4D向量  |
|  `bool IsVec()`  |  是否为向量类型(2D/3D/4D)  |
|  `bool IsScript()`  |  是否为脚本对象  |
|  `bool IsPtrEx(strid classid=0)`  |  是否为扩展指针类型，参数：classid-类ID过滤(可选)，返回：是否匹配  |
|  `bool IsPtr64(strid kindid=0)`  |  是否为64位指针类型，参数：kindid-类型ID过滤(可选)，返回：是否匹配  |
|  `bool IsBin()`  |  是否为二进制数据  |
|  `bool isobj()`  |  是否为对象(兼容接口)  |
|  `bool Destroy()`  |  销毁变量，清空内容  |
|  `bool CreateSpaceStr(string pstr,string psplitstr,string pletchar,var pdef=NULL,int forcestrkind=0)`  |  从分隔字符串创建结构，参数：pstr-源字符串，psplitstr-分隔符，pletchar-左右括号，pdef-默认值，forcestrkind-强制类型  |
|  `string FormatInt16(int fixspace=0)`  |  格式化整数为16进制字符串，参数：fixspace-固定空格数，返回：格式化后的字符串  |
|  `string FormatFloat(int shows=3,int fixspace=0)`  |  格式化浮点数为字符串，参数：shows-小数位数，fixspace-固定空格数，返回：格式化后的字符串  |
|  `string FormatInt(int fixspace=0,int add0=0)`  |  格式化整数为字符串，参数：fixspace-固定空格数，add0-添加前导零，返回：格式化后的字符串  |
|  `bool vis(strid nameid)`  |  是否有vid id值  |
|  `var vid(strid nameid,var pdef=NULL)`  |  获取vid条目的指针，参数：nameid-ID名称，pdef-默认值，返回：vid指针  |
|  `var vget(strid nameid,var pdef=NULL)`  |  获取vid条目的值，参数：nameid-ID名称，pdef-默认值，返回：vid值  |
|  `bool vset(strid nameid,var v)`  |  设置vid条目的值，参数：nameid-ID名称，v-要设置的值，返回：是否成功  |
|  `bool vsetsz(var v)`  |  将数组设置为vid格式，参数：v-数组值，返回：是否成功  |
|  `bool vdel(strid nameid)`  |  删除vid条目，参数：nameid-ID名称，返回：是否成功  |
|  `bool vidAddSpaceStr(string pstr,string psplitstr,string pletchar,var pdef=NULL,int forcestrkind=0)`  |  为vid添加分隔字符串，参数：pstr-源字符串，psplitstr-分隔符，pletchar-左右括号，pdef-默认值，forcestrkind-强制类型  |
|  `var col(strid nameid,var pdef=NULL)`  |  获取结构列值，参数：nameid-列名，pdef-默认值，返回：列值  |
|  `bool ifcols(string pcolnamedefs)`  |  检查列条件是否满足，参数：pcolnamedefs-条件字符串(如"colname1>0;colname2;colname3!=nil")，返回：是否满足  |
|  `bool SzMake(int bszcacel=1)`  |  确保变量为数组类型，参数：bszcacel-是否取消数组转换，返回：是否成功  |
|  `bool SzInit(int size,var pinit=NULL)`  |  初始化数组，参数：size-数组大小，pinit-初始值，返回：是否成功  |
|  `bool SzAdd(var v)`  |  向数组添加元素，参数：v-要添加的值，返回：是否成功  |
|  `bool SzInsert(int insertpos,var v)`  |  在数组指定位置插入元素，参数：insertpos-插入位置，v-要插入的值，返回：是否成功  |
|  `bool SzDel(int delpos,int len=1)`  |  删除数组元素，参数：delpos-删除位置，len-删除长度，返回：是否成功  |
|  `bool SzGet(var& getv,var pos)`  |  获取数组元素，参数：getv-返回值，pos-位置/索引，返回：是否成功  |
|  `int SzFind(var psz,int startpos=0,int step=1)`  |  在数组中查找元素，参数：psz-查找值，startpos-起始位置，step-步长，返回：找到的位置，-1表示未找到  |
|  `int SzAddNoSame(var psz)`  |  向数组添加不重复元素，参数：psz-要添加的值，返回：元素在数组中的位置  |
|  `bool SzSort(int order=0,int subszstart=-1)`  |  对数组排序，参数：order-排序方式(0升序/非0降序)，subszstart-子数组起始位置，返回：是否成功  |
|  `int SzSearch(var psz,int startpos=0,int step=1,int subszno=0)`  |  在已排序数组中搜索，参数：psz-搜索值，startpos-起始位置，step-步长，subszno-子数组号，返回：位置，-1表示未找到  |
|  `int SzHalfSearch(var psz,int breverse=0)`  |  在已排序数组中使用二分查找，参数：psz-搜索值，breverse-是否逆序，返回：位置，-1表示未找到  |
|  `bool IsStruct(GBR_Task *pTask,var structnameid)`  |  检查变量是否为指定结构类型，参数：pTask-任务上下文，structnameid-结构名ID，返回：是否匹配  |
|  `bool CovStruct(GBR_Task *pTask,var structnameid)`  |  将变量转换为指定结构类型，参数：pTask-任务上下文，structnameid-结构名ID，返回：是否成功  |
|  `var GetStructDef()`  |  获取结构定义，返回：结构定义变量  |
|  `var GetStructPtr()`  |  获取结构指针，返回：结构指针变量  |
|  `string GetStructName()`  |  获取结构名称，返回：结构名称字符串  |
|  `int CopyStruct(var pfv)`  |  复制结构数据，参数：pfv-源结构，返回：复制的字段数  |
|  `int GetStructCol(strid colname)`  |  获取结构字段列索引，参数：colname-列名ID，返回：列索引，-1表示未找到  |
|  `int SzIsStruct(GBR_Task *pTask,var structnameid,int startpos=0,int step=1)`  |  检查数组中的元素是否为指定结构，参数：pTask-任务上下文，structnameid-结构名，startpos-起始位置，step-步长，返回：匹配元素数量  |
|  `int SzCovStruct(GBR_Task *pTask,var structnameid,int startpos=0,int step=1)`  |  将数组中元素转换为指定结构，参数：pTask-任务上下文，structnameid-结构名，startpos-起始位置，step-步长，返回：转换成功元素数量  |
|  `void SzLink(var linksz)`  |  连接两个数组，参数：linksz-要连接的数组  |
|  `int SzPtrPack(int subsize=1,int ptrpos=0)`  |  移除数组中的无效指针元素，参数：subsize-子数组大小，ptrpos-指针位置，返回：剩余有效元素数量  |
|  `int SzPtrFind(obj fptr,int subsize=1,int ptrpos=0)`  |  在指针数组中查找对象，参数：fptr-查找的对象指针，subsize-子数组大小，ptrpos-指针位置，返回：位置，-1表示未找到  |
|  `int SzPtrCallBack(var vfun,var pagv=NULL,int subsize=1,int ptrpos=0)`  |  对指针数组中的所有对象调用函数，参数：vfun-回调函数，pagv-参数，subsize-子数组大小，ptrpos-指针位置，返回：处理的元素数量  |
|  `int GetVecSize()`  |  获取向量维度，返回：维度(2/3/4)  |
|  `float GetVec(int no)`  |  获取向量分量值，参数：no-分量索引，返回：分量值  |
|  `bool SetVec(int no,float f)`  |  设置向量分量值，参数：no-分量索引，f-分量值，返回：是否成功  |
|  `string GetSafeStr()`  |  获取安全字符串表示，返回：转义后的安全字符串  |
|  `bool vis64(var id64)`  |  检查是否有64位ID值，参数：id64-64位ID，返回：是否存在  |
|  `var vget64(var id64,var pdef=NULL)`  |  获取64位ID对应的值，参数：id64-64位ID，pdef-默认值，返回：ID值  |
|  `bool vset64(var id64,var v)`  |  设置64位ID对应的值，参数：id64-64位ID，v-要设置的值，返回：是否成功  |
|  `bool vdel64(var id64)`  |  删除64位ID，参数：id64-64位ID，返回：是否成功  |
|  `var vid64(var id64,var pdef=NULL)`  |  获取64位ID的指针，参数：id64-64位ID，pdef-默认值，返回：ID指针  |
----
### string
**类型**：[varkind](#varkind)　　　　**路径** ：[var:string](#var:string)
**描述**:字符串变量类，提供字符串操作和转换功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  size  |  int  |  字符串长度  |
|  length  |  int  |  字符串长度  |
|  strid  |  int  |  字符串的整数标识  |
|  strid64  |  int64  |  字符串的64位整数标识  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `int GetLength()`  |  返回字符串长度  |
|  `int Find(string sfind,int fromindex=0)`  |  查找子字符串，参数：sfind-要查找的字符串，fromindex-起始位置，返回：找到的位置，-1表示未找到  |
|  `int FindEx(string sfind,int flag,int fromindex=0)`  |  扩展查找功能，参数：sfind-查找内容，flag-查找标志(1=区分大小写,2=单词匹配)，fromindex-起始位置，返回：位置  |
|  `int FindInverse(string sfind,int fromindex=0)`  |  反向查找字符串，参数：sfind-查找内容，fromindex-起始位置，返回：位置  |
|  `string Mid(int first, int count)`  |  截取子字符串，参数：first-起始位置，count-长度，返回：截取的字符串  |
|  `string Left(int num)`  |  截取左侧字符串，参数：num-长度，返回：截取的字符串  |
|  `string Right(int num)`  |  截取右侧字符串，参数：num-长度，返回：截取的字符串  |
|  `bool GetWord(string& retstr,string psplitchar,int bmusthavech=0,int bmoveempty=1)`  |  获取字符串中的单词，参数：retstr-返回的单词，psplitchar-分隔符，bmusthavech-必须包含分隔符，bmoveempty-是否移除空值，返回：是否成功  |
|  `bool GetLastWord(string& retstr,string psplitchar,int bmusthavech=0)`  |  获取字符串最后一个单词，参数：retstr-返回的单词，psplitchar-分隔符，bmusthavech-必须包含分隔符，返回：是否成功  |
|  `bool GetKeyWord(string& retstr)`  |  获取字符串中的关键字，参数：retstr-返回的关键字，返回：是否成功  |
|  `void Delete(int pos,int delnum=1)`  |  删除指定位置的字符，参数：pos-位置，delnum-删除数量  |
|  `void MakeLower()`  |  转换为小写  |
|  `void MakeUpperCase()`  |  转换为大写  |
|  `bool Compare(string pstr)`  |  比较字符串，参数：pstr-比较的字符串，返回：是否相等  |
|  `bool CompareMax(string pstr)`  |    |
|  `bool CompareNoCase(string pstr)`  |  比较字符串(忽略大小写)，参数：pstr-比较的字符串，返回：是否相等  |
|  `bool CompareNoCaseMax(string pstr)`  |    |
|  `void Insert(int insertpos,string pstr)`  |  插入字符串，参数：insertpos-插入位置，pstr-插入的字符串  |
|  `int Replace(string pstr,string tostr,int start=0,int maxreplace=0)`  |  替换字符串，参数：pstr-查找串，tostr-替换串，start-起始位置，maxreplace-最大替换次数，返回：替换次数  |
|  `int GetInt(int def,string psplitchar)`  |  从字符串中提取整数，参数：def-默认值，psplitchar-分隔符，返回：提取的整数  |
|  `var GetColor(int def,string psplitchar)`  |  从字符串中提取颜色值，参数：def-默认值，psplitchar-分隔符，返回：颜色变量  |
|  `int64 GetInt64(int def,string psplitchar)`  |  从字符串中提取64位整数，参数：def-默认值，psplitchar-分隔符，返回：64位整数值  |
|  `float GetFloat(float def,string psplitchar)`  |  从字符串中提取浮点数，参数：def-默认值，psplitchar-分隔符，返回：浮点数值  |
|  `int FindEnd(string pfind,int formindex=0)`  |  查找字符串结束位置，参数：pfind-要查找的字符串，formindex-起始位置，返回：结束位置  |
|  `int GetMidStr(string &retstr,string pfind,string pend,int formindex=0,int bhaveflag=0)`  |  提取字符串中指定字符串之间的内容，参数：retstr-返回结果，pfind-起始字符串，pend-结束字符串，formindex-起始位置，bhaveflag-是否包含边界，返回：结束位置  |
|  `int GetAscll(int num)`  |  获取指定位置字符的ASCII码，参数：num-字符位置，返回：ASCII码值  |
|  `void MakeWord()`  |  字符串去不可见字符  |
|  `var Split(string psplitstr,int bskipformat=0)`  |  按分隔符拆分字符串，参数：psplitstr-分隔字符串，bskipformat-是否跳过格式化，返回：拆分后的字符串数组  |
|  `bool CreateWithSafeStr(var& agv)`  |  创建安全字符串，参数：agv-目标变量，返回：是否成功  |
|  `bool GetTextSkipStr(string &sret,string psplitchar)`  |  跳过特定字符获取文本，参数：sret-返回文本，psplitchar-跳过的字符，返回：是否成功  |
|  `bool RemoveLastChar(string psplitchar)`  |  移除最后一个指定字符，参数：psplitchar-要移除的字符，返回：是否成功  |
|  `void SetLastChar(string psplitchar)`  |  设置最后一个字符，参数：psplitchar-要设置的字符  |
|  `int Str2UINT()`  |  字符串转换为无符号整数，返回：转换后的整数值  |
|  `string UrlDecode()`  |  URL解码  |
|  `string UrlEncode()`  |  URL编码  |
|  `string EncodeBase64()`  |  Base64编码  |
|  `string DecodeBase64()`  |  Base64解码  |
|  `string CovToNormalStr(int btry=0)`  |  转换为普通字符串，参数：btry-是否尝试转换特殊字符  |
|  `string CovToTextedStr(int bdq=1)`  |  转换为带引号的字符串，参数：bdq-是否使用双引号  |
|  `var JsonToStrVal()`  |  将字符串解析为JSON对象，返回：解析后的变量对象  |
|  `var GetFinder(int flag=0)`  |  创建字符串查找器，参数：flag-查找选项，返回：查找器对象  |
|  `int OnFind(var finder,int fromindex=0)`  |  执行字符串查找，参数：finder-查找器，fromindex-起始位置，返回：找到的位置  |
|  `var PerReplaceSz(var repstrsz)`  |    |
|  `int ReplaceSz(var repstrbin,int start=0)`  |    |
----
### var
**类型**：[varkind](#varkind)　　　　**路径** ：[var:var](#var:var)
**描述**:集合变量类，提供命名值管理和JSON序列化功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  size  |  int  |  集合中元素的数量  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `bool svAdd(string name,var pinit=NULL)`  |  添加命名变量到集合，不覆盖已有值，参数：name-变量名，pinit-初始值  |
|  `bool svSet(string name,var pinit=NULL)`  |  设置命名变量，覆盖已有值，参数：name-变量名，pinit-设置的值  |
|  `int svPos(string name)`  |  查找命名值的位置索引，参数：name-名称，返回：位置索引，不存在返回-1  |
|  `bool svGet(string pname,var& pret)`  |  获取命名变量值，支持多级路径，参数：pname-变量路径，pret-返回值  |
|  `var svVal(string name,var pdef=NULL)`  |  获取命名值，参数：name-名称，pdef-默认值，返回：命名值或默认值  |
|  `bool svDel(string name)`  |  删除命名值，参数：name-名称，返回：是否删除成功  |
|  `bool svGetJsonText(string &txt,int bcr=0)`  |  获取JSON文本格式，参数：txt-输出文本，bcr-是否格式化，返回：是否获取成功  |
----
### vec2
**类型**：[varkind](#varkind)　　　　**路径** ：[var:vec2](#var:vec2)
**描述**:二维向量变量类，提供二维坐标和向量操作
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  x  |  float  |  向量X坐标分量  |
|  y  |  float  |  向量Y坐标分量  |
|  xy  |  vec2  |  完整二维向量  |
|  yx  |  vec2  |  向量YX平面坐标，X和Y坐标交换  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Set(float x,float y)`  |  设置向量值，参数：x-X坐标，y-Y坐标  |
|  `void Normalize()`  |  将向量归一化为单位向量  |
|  `float Length()`  |  计算向量长度，返回：向量的模长  |
|  `vec3 GetVec3(float z=0)`  |  转换为三维向量，参数：z-Z坐标值(默认为0)，返回：三维向量  |
|  `vec2 Roto(float degree)`  |  旋转向量，参数：degree-旋转角度(度)，返回：旋转后的向量  |
|  `bool IsZero()`  |  检查向量是否为零向量，返回：true表示是零向量，false表示非零向量  |
----
### vec3
**类型**：[varkind](#varkind)　　　　**路径** ：[var:vec3](#var:vec3)
**描述**:三维向量变量类，提供三维坐标和向量操作
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  x  |  float  |  向量X坐标分量  |
|  y  |  float  |  向量Y坐标分量  |
|  z  |  float  |  向量Z坐标分量  |
|  xy  |  vec2  |  向量XY平面坐标  |
|  xyz  |  vec3  |  完整三维向量  |
|  yx  |  vec2  |  向量YX平面坐标  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Set(float x,float y,float z)`  |  设置向量值，参数：x-X坐标，y-Y坐标，z-Z坐标  |
|  `void Normalize()`  |  将向量归一化为单位向量  |
|  `float Length()`  |  计算向量长度，返回：向量的模长  |
|  `vec2 GetVec2()`  |  转换为二维向量，返回：舍弃Z坐标后的二维向量  |
|  `vec3 RotoX(float degree)`  |  绕X轴旋转向量，参数：degree-旋转角度(度)，返回：旋转后的向量  |
|  `vec3 RotoY(float degree)`  |  绕Y轴旋转向量，参数：degree-旋转角度(度)，返回：旋转后的向量  |
|  `vec3 RotoZ(float degree)`  |  绕Z轴旋转向量，参数：degree-旋转角度(度)，返回：旋转后的向量  |
|  `bool IsZero()`  |  检查向量是否为零向量，返回：true表示是零向量，false表示非零向量  |
|  `void GetAsEulerMatrix3(var& vmat3)`  |  将向量作为欧拉角转换为3x3矩阵，参数：vmat3-输出矩阵  |
|  `void GetAsEulerMatrix4(var& vmat4)`  |  将向量作为欧拉角转换为4x4矩阵，参数：vmat4-输出矩阵  |
----
### vec4
**类型**：[varkind](#varkind)　　　　**路径** ：[var:vec4](#var:vec4)
**描述**:四维向量变量类，提供四元数旋转和矩形操作功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  x  |  float  |  向量X坐标分量  |
|  y  |  float  |  向量Y坐标分量  |
|  z  |  float  |  向量Z坐标分量  |
|  w  |  float  |  向量W坐标分量，用于齐次坐标系  |
|  xy  |  vec2  |  向量XY平面坐标  |
|  xyz  |  vec3  |  向量XYZ空间坐标  |
|  left  |  float  |  矩形左边界坐标  |
|  top  |  float  |  矩形上边界坐标  |
|  right  |  float  |  矩形右边界坐标  |
|  bottom  |  float  |  矩形下边界坐标  |
|  lefttop  |  vec2  |  矩形左上角坐标  |
|  rightbottom  |  vec2  |  矩形右下角坐标  |
|  rectw  |  float  |  矩形宽度  |
|  recth  |  float  |  矩形高度  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Normalize()`  |  将向量归一化为单位向量  |
|  `void Set(float x,float y,float z,float w)`  |  设置向量值，参数：x-X坐标，y-Y坐标，z-Z坐标，w-W坐标  |
|  `vec4 InitRotationX(float degree)`  |  初始化为绕X轴旋转的四元数，参数：degree-旋转角度(度)，返回：初始化后的四元数  |
|  `vec4 InitRotationY(float degree)`  |  初始化为绕Y轴旋转的四元数，参数：degree-旋转角度(度)，返回：初始化后的四元数  |
|  `vec4 InitRotationZ(float degree)`  |  初始化为绕Z轴旋转的四元数，参数：degree-旋转角度(度)，返回：初始化后的四元数  |
|  `vec4 InitRotationZXY(float degz,float degx,float degy)`  |  初始化为按Z-X-Y顺序旋转的四元数，参数：degz-Z轴角度，degx-X轴角度，degy-Y轴角度，返回：初始化后的四元数  |
|  `void InitShortestArc(vec3 from, vec3 to)`  |  计算两向量间最短旋转弧的四元数，参数：from-起始向量，to-目标向量  |
|  `void Roto(vec4 r)`  |  四元数旋转，参数：r-旋转量  |
|  `void GetMatrix4(var& pmat)`  |  获取四元数对应的4x4变换矩阵，参数：pmat-输出矩阵  |
|  `void Blend(float d,vec4 q)`  |  四元数插值混合，参数：d-混合比例，q-目标四元数  |
|  `void InitRotoZTo(vec3 dir,float roll)`  |  初始化为使Z轴对准指定方向的四元数，参数：dir-目标方向，roll-滚转角度  |
|  `int GetColorARGB()`  |  获取颜色值的ARGB格式，返回：ARGB格式的整数颜色值  |
|  `void SetColorARGB(int c)`  |  设置颜色值的ARGB格式，参数：c-ARGB格式的整数颜色值  |
|  `bool IsZero()`  |  检查向量是否为零向量，返回：true表示是零向量，false表示非零向量  |
|  `void RectOffset(vec2 off)`  |  偏移矩形位置，参数：off-偏移向量  |
|  `bool RectIsEmpty()`  |  检查矩形是否为空，返回：true表示矩形为空，false表示矩形有效  |
|  `void RectUnion(vec4 s)`  |  合并另一个矩形，参数：s-要合并的矩形  |
|  `void RectUnionPt(vec2 s)`  |  合并一个点到矩形，参数：s-要包含的点  |
|  `bool IsPtInRect(vec2 pt)`  |  检查点是否在矩形内，参数：pt-要检查的点，返回：true表示点在矩形内，false表示点在矩形外  |
|  `vec2 RectSize()`  |  获取矩形大小，返回：包含宽度和高度的二维向量  |
----
### ptr64
**类型**：[varkind](#varkind)　　　　**路径** ：[var:ptr64](#var:ptr64)
**描述**:64位指针变量类，用于远程对象和系统对象的引用管理
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Trace()`  |  输出指针信息到调试跟踪窗口  |
|  `bool SetObj(obj p)`  |  设置对象指针，参数：p-对象指针，返回：是否设置成功  |
|  `bool isobj()`  |  检查是否为有效对象指针，返回：是否为有效对象  |
|  `bool IsSysObj()`  |  检查是否为系统对象，返回：是否为系统对象  |
|  `obj GetObj()`  |  获取对象指针，返回：对象指针结构  |
----
### script
**类型**：[varkind](#varkind)　　　　**路径** ：[var:script](#var:script)
**描述**:用于封装、编译和执行脚本代码的变量类型，提供表达式解析和动态执行功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Trace(GBR_Task *ptask)`  |  输出脚本信息到调试跟踪窗口，参数：ptask-当前任务对象  |
|  `var SetRuner(obj p)`  |  设置脚本运行器对象，参数：p-运行器对象，返回：设置后的脚本变量  |
|  `var CompileExp(GBR_Task *ptask,string pext,var& pvarnamevid)`  |  编译表达式为脚本，参数：ptask-当前任务，pext-表达式文本，pvarnamevid-变量名ID，返回：编译结果  |
|  `var runExp(GBR_Task *ptask,var& pvarnamevid)`  |  执行脚本，参数：ptask-当前任务，pvarnamevid-变量名ID，返回：执行结果  |
----
### bin
**类型**：[varkind](#varkind)　　　　**路径** ：[var:bin](#var:bin)
**描述**:二进制数据变量类，用于存储和操作二进制数据
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  binsize  |  int  |  获取二进制数据的大小，返回：数据大小（字节数）  |
|  datname  |  int  |    |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Empty()`  |  清空二进制数据，将数据大小设为0  |
|  `int Length()`  |  获取二进制数据的长度，返回：数据长度（字节数）  |
|  `bool Compress_LZ4(var& pret,int flag,int ziplevel=6)`  |  使用LZ4算法压缩二进制数据，参数：pret-压缩结果，flag-标志，ziplevel-压缩级别，返回：是否成功  |
|  `bool UnCompress_LZ4(var& pret,int flag)`  |  解压LZ4压缩的二进制数据，参数：pret-解压结果，flag-标志，返回：是否成功  |
|  `int GetBinSize()`  |  获取二进制数据的大小，返回：数据大小（字节数）  |
|  `void SetBinSize(int size,int addbuf=16)`  |  设置二进制数据的大小，参数：size-数据大小，addbuf-额外缓冲区大小  |
|  `bool SetByte(int pos,int byte)`  |  设置指定位置的字节值，参数：pos-位置，byte-字节值，返回：是否成功  |
|  `int GetByte(int pos)`  |  获取指定位置的字节值，参数：pos-位置，返回：字节值，失败返回-1  |
|  `bool FillByte(int pos,int set,int size)`  |  填充字节值，参数：pos-起始位置，set-填充值，size-填充长度，返回：是否成功  |
|  `bool DelByte(int pos,int delnum)`  |  删除字节，参数：pos-起始位置，delnum-删除数量，返回：是否成功  |
|  `bool SetInt(int pos,int d)`  |  设置指定位置的整数值，参数：pos-位置，d-整数值，返回：是否成功  |
|  `void AddInt(int d)`  |  添加整数到二进制数据末尾，参数：d-整数值  |
|  `int FindInt(int d,int st=0,int emsize=4)`  |  查找整数值，参数：d-要查找的整数值，st-起始位置，emsize-元素大小，返回：找到的位置，失败返回-1  |
|  `int GetInt(int pos)`  |  获取指定位置的整数值，参数：pos-位置，返回：整数值，失败返回-1  |
|  `bool SetFloat(int pos,float d)`  |  设置指定位置的浮点数值，参数：pos-位置，d-浮点数值，返回：是否成功  |
|  `void AddFloat(float f)`  |  添加浮点数到二进制数据末尾，参数：f-浮点数值  |
|  `float GetFloat(int pos)`  |  获取指定位置的浮点数，参数：pos-位置，返回：浮点数值，失败返回0  |
|  `bool SetInt64(int pos,var i64)`  |  设置指定位置的64位整数，参数：pos-位置，i64-64位整数值，返回：是否成功  |
|  `void AddInt64(var i64)`  |  添加64位整数到二进制数据末尾，参数：i64-64位整数值  |
|  `int64 GetInt64(int pos)`  |  获取指定位置的64位整数，参数：pos-位置，返回：64位整数值，失败返回0  |
|  `bool GetAsStr(var& retstr)`  |  将二进制数据转换为16进制字符串，参数：retstr-返回的字符串，返回：是否成功  |
|  `bool SetAsStr(var str)`  |  将16进制字符串转换为二进制数据，参数：str-源字符串，返回：是否成功  |
|  `string GetBase64()`  |  将二进制数据转换为Base64编码字符串，返回：Base64编码字符串  |
|  `bool SetBase64(var str)`  |  将Base64编码字符串转换为二进制数据，参数：str-Base64编码字符串，返回：是否成功  |
----
### ptrex
**类型**：[varkind](#varkind)　　　　**路径** ：[var:ptrex](#var:ptrex)
**描述**:扩展指针变量类，提供对对象指针的引用计数和类型检查功能
#### 变量
|  变量名  |  数据类型  |  描述  |
|-------|--------|------|
|  classid  |  int  |  指针对象的类ID  |
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `string GetClassName()`  |  获取指针对象的类名，返回：类名字符串  |
|  `bool New(GBR_Task *ptask)`  |  创建新的指针对象实例，参数：ptask-任务上下文，返回：是否成功  |
|  `bool IsEmpty()`  |  检查指针是否为空，返回：是否为空  |
|  `bool Delete(GBR_Task *ptask)`  |  删除指针对象，参数：ptask-任务上下文，返回：是否成功  |
|  `bool GetParam(strid nameid,var& val)`  |  获取指针对象的参数，参数：nameid-参数名ID，val-返回值，返回：是否成功  |
|  `bool SetParam(GBR_Task *ptask,strid nameid,var val)`  |  设置指针对象的参数，参数：ptask-任务上下文，nameid-参数名ID，val-设置值，返回：是否成功  |
----
### mat3
**类型**：[varkind](#varkind)　　　　**路径** ：[var:mat3](#var:mat3)
**描述**:矩阵3变量类，提供3x3矩阵运算和矩阵变换功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Init()`  |  清空矩阵，将所有元素初始化为0  |
|  `void Init2DMatrix(float scale,float rad,float offx,float offy)`  |  初始化2D矩阵，参数：scale-缩放比例，rad-旋转角度，offx-X轴偏移，offy-Y轴偏移  |
|  `var Inverse()`  |  求矩阵的逆矩阵，返回：逆矩阵  |
|  `var Transpose()`  |  转置矩阵，返回：转置后的矩阵  |
|  `bool SetSub(int pos,float v)`  |  设置矩阵指定位置的值，参数：pos-位置索引(0-8)，v-设置的值，返回：是否设置成功  |
|  `float GetSub(int pos)`  |  获取矩阵指定位置的值，参数：pos-位置索引(0-8)，返回：指定位置的值  |
----
### mat4
**类型**：[varkind](#varkind)　　　　**路径** ：[var:mat4](#var:mat4)
**描述**:4x4矩阵变量类，提供矩阵变换和3D空间操作功能
#### 函数
|  函数原型  |  描述  |
|-------|------|
|  `void Init()`  |  初始化矩阵为单位矩阵  |
|  `void Init2DMatrix(float scale,float rad,float offx,float offy)`  |  初始化为2D变换矩阵，参数：scale-缩放比例，rad-旋转角度，offx-X偏移，offy-Y偏移  |
|  `void InitRotationX(float rad)`  |  初始化为绕X轴旋转矩阵，参数：rad-旋转角度(度)  |
|  `void InitRotationY(float rad)`  |  初始化为绕Y轴旋转矩阵，参数：rad-旋转角度(度)  |
|  `void InitRotationZ(float rad)`  |  初始化为绕Z轴旋转矩阵，参数：rad-旋转角度(度)  |
|  `void InitRotationZX(float radz,float radx)`  |  初始化为先绕Z轴后绕X轴的组合旋转矩阵，参数：radz-Z轴旋转角度(度)，radx-X轴旋转角度(度)  |
|  `void InitVectorRotation(float x, float y, float z, float a)`  |  初始化为绕任意向量旋转的矩阵，参数：x,y,z-旋转轴向量，a-旋转角度  |
|  `var Inverse()`  |  计算矩阵的逆矩阵，返回：逆矩阵  |
|  `var Transpose()`  |  计算矩阵的转置矩阵，返回：转置矩阵  |
|  `vec3 GetOffSet()`  |  获取矩阵的位移分量，返回：位移向量(x,y,z)  |
|  `void OffSet(float x,float y,float z)`  |  设置矩阵的位移分量，参数：x,y,z-位移向量  |
|  `void Scale(float s)`  |  对矩阵应用均匀缩放，参数：s-缩放比例  |
|  `bool SetSub(int pos,float v)`  |  设置矩阵的指定元素值，参数：pos-元素索引(0-15)，v-元素值，返回：操作是否成功  |
|  `float GetSub(int pos)`  |  获取矩阵的指定元素值，参数：pos-元素索引(0-15)，返回：元素值  |
|  `void GetTransRotScale(vec3& trans,vec4& rot,vec3& scale)`  |  分解矩阵为位移、旋转和缩放分量，参数：trans-输出位移向量，rot-输出旋转四元数，scale-输出缩放向量  |
|  `void SetTransRotScale(vec3 trans,vec4 rot,vec3 scale)`  |  从位移、旋转和缩放分量合成矩阵，参数：trans-位移向量，rot-旋转四元数，scale-缩放向量  |
----
