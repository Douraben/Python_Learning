# Flet 0.82.2 版本 - 入门到精通完整教程

> **适用版本**: Python Flet 框架 v0.82.2+  
> **文档状态**: ✅ 完整版 | 🔄 持续更新中  
> **学习路径**: 适合 Python 开发者快速上手 Flet 框架

## 📚 目录

1. [🏠 快速开始](#1-快速开始) - 5 分钟创建你的第一个应用
2. [💡 核心概念解析](#2-核心概念解析) - 理解事件驱动和响应式编程
3. [🎨 组件系统详解](#3-组件系统详解) - 50+ 控件用法与属性
4. [🔄 响应式数据绑定](#4-响应式数据绑定) - 状态管理最佳实践
5. [⚡ Hooks 状态管理](#5-hooks-状态管理) - React 风格的状态处理
6. [📐 布局与控件](#6-布局与控件) - 灵活的 UI 布局系统
7. [🚀 高级功能](#7-高级功能) - Canvas/WebView/Markdown 等
8. [💼 实际项目案例](#8-实际项目案例) - 从简单到复杂的项目模板
9. [📦 部署与发布](#9-部署与发布) - 打包为桌面/Web 应用
10. [✨ 最佳实践](#10-最佳实践) - 性能优化和代码规范

## 🎯 教程亮点

- ✅ **渐进式学习**: 从 Hello World 到企业级应用开发
- ✅ **实战驱动**: 每个知识点都有可运行的代码示例
- ✅ **中文文档**: 通俗易懂的中文说明，无技术术语障碍
- ✅ **完整 API 覆盖**: 覆盖 Flet 0.82.2+ 的主要功能特性
- ✅ **最佳实践**: 包含性能优化、错误处理等实用技巧

---

### 学习建议

1. **新手入门**: 从第 1、2 章开始，理解基本概念后尝试运行示例代码
2. **进阶开发**: 阅读第 3-7 章，掌握各个组件的用法和属性配置
3. **项目开发**: 参考第 8 章的项目案例，学习如何组织大型应用代码
4. **部署上线**: 完成第 9、10 章后即可获得完整的应用发布方案

---
2. [核心概念解析](#2-核心概念解析)
3. [组件系统详解](#3-组件系统详解)
4. [响应式数据绑定](#4-响应式数据绑定)
5. [Hooks 状态管理](#5-hooks-状态管理)
6. [布局与控件](#6-布局与控件)
7. [高级功能](#7-高级功能)
8. [实际项目案例](#8-实际项目案例)
9. [部署与发布](#9-部署与发布)
10. [最佳实践](#10-最佳实践)

---


# 安装 Flet
pip install flet[all]

# 验证安装
flet --version
```

### 1.2 第一个 Flet 应用

**🎯 学习目标**: 5 分钟内创建并运行你的第一个 Flet 应用

#### 📌 基础示例 - Hello World

**使用场景**: 
- 🏢 快速原型验证
- 🚀 学习框架基本概念
- 💡 测试开发环境配置

**代码详解**:
- `fl.Page`: 应用的主容器，所有 UI 组件都挂载在这里
- `fl.Text`: 显示文本信息的组件
- `fl.ElevatedButton`: Material Design 风格的点击按钮
- `on_click`: 事件处理函数，接收 `ControlEvent` 对象

**运行结果**:
- 弹出包含两个组件的窗口
- 点击按钮会更新文本内容
- 应用窗口支持拖动和缩放

```python
import flet as fl

def main(page: fl.Page) -> None:
    """页面入口函数"""
    
    # 添加文本组件
    text = fl.Text(
        "你好，Flet！",
        size=24,
        weight="bold"
    )
    
    # 添加按钮并绑定点击事件
    btn = fl.ElevatedButton(
        text="点击我",
        on_click=lambda e: setattr(text, 'value', f"已点击 {page.views[0].controls['btn'].text}")
    )
    
    page.add(text, btn)

# 运行应用
fl.app.run()
```

#### 💡 进阶技巧 - 完整功能示例

**使用场景**: 
- 📊 开发实际业务应用
- 🔄 学习响应式状态管理
- 🎨 掌握布局容器用法

**代码详解**:
- `page.title`: 设置应用标题栏文字
- `fl.value()`: 创建响应式变量（自动触发 UI 更新）
- `Column`: 垂直布局容器，支持子元素对齐
- `fl.Alignment.center`: 居中对齐方式

```python
import flet as fl
from typing import Callable

def main(page: fl.Page) -> None:
    # 🎨 页面配置
    page.title = "Flet 示例应用"  # 窗口标题
    page.scroll = fl.ScrollMode.AUTO  # 启用滚动
    
    # 🔄 响应式变量管理
    count = fl.value(0)           # 计数器
    message = fl.value("初始化消息")  # 显示文本
    
    # ⚡️ 事件处理函数定义
    def increment(e: fl.ControlEvent) -> None:
        """点击增加按钮"""
        new_count = count.value + 1
        count.value = new_count
        message.value = f"当前计数：{new_count}"
        
    # 📝 文本组件配置
    label = fl.Text(
        message,                   # 绑定响应式变量
        size=20,                  # 字体大小
        selectable=True           # 可点击选中文本
    )
    
    # 🔘 按钮组创建
    btn_inc = fl.FilledButton(
        "增加",                    # 按钮文本
        on_click=increment        # 绑定事件处理
    )
    
    btn_dec = fl.FilledButton(
        "减少",
        on_click=lambda e: setattr(count, 'value', count.value - 1)
    )
    
    # 📐 布局容器 - Column
    col = fl.Column([label, btn_inc, btn_dec], 
                    alignment=fl Alignment.center)  # 居中显示
    
    page.add(col)

fl.app.run()
```

#### 🚀 运行应用的方式

| 运行方式 | 使用场景 | 命令参数 | 说明 |
|---------|-----|------|--------|
| **桌面应用** | Windows/Linux/Mac GUI | `view=flet.ViewType.WINDOWED` | 带窗口边框的原生窗口 |
| **移动端 WebView** | iOS/Android 开发 | `view=fl.ViewType.CAPTURED_WINDOW` | WebView 嵌入模式 |
| **网页版** | Web 托管服务 | `host="0.0.0.0", port=8888` | HTTP 服务器模式 |

```python
# 🖥️ Windows GUI (桌面应用) - 推荐使用此方式测试
fl.app.run(
    view=flet.ViewType.WINDOWED,       # 窗口化模式
    dark_mode=False,                   # 启用深色模式适配
    theme=flet.ThemeMode.SYSTEM        # 跟随系统主题
)

# 📱 移动端 WebView (iOS/Android 开发)
fl.app.run(view=fl.ViewType.CAPTURED_WINDOW)

# 🌐 Web 托管部署 (生产环境使用)
fl.app.run(
    host="0.0.0.0",                    # 监听所有网卡
    port=8888,                         # 端口号
    view=flet.ViewType.WEBSITE         # 网页模式
)
```

**💡 提示**: 
- 首次运行时，确保已安装 Flet 和相关依赖
- 使用 `ViewType.WINDOWED` 进行本地开发调试
- Web 部署时使用 Docker 可获得更好的隔离性

---

## 2. 核心概念解析

### 2.1 Page 对象

**核心作用**: `Page` 是 Flet 应用的核心容器，所有 UI 组件都是其子元素。它负责管理整个应用的渲染循环和事件分发。

**基本配置示例**:
```python
page = fl.Page()

# 🎨 窗口标题与尺寸
page.title = "应用标题"
page.window_width = 400
page.window_height = 600

# 🖌️ 背景颜色
page.bgcolor = "#1E1E1E"  # 深色背景

# 📐 内边距设置
page.padding = 20

# 🔘 窗口控制属性
page.window.min_width = 300
page.window.min_height = 400
page.window.resizable = True   # 可调整大小
page.window.title_bar_color = "#333333"  # 标题栏颜色
```

**💡 提示**: Page 对象会自动创建一个本地 Web 服务器（默认端口 8888），首次运行时会显示一个原生窗口或浏览器标签页。

---

### 2.2 控件层次结构

Flet 采用树状组件结构，理解层次关系对调试和性能优化至关重要:

```
Page (根容器)
 └── Column/Row/Stack/GridView (布局容器层)
      ├── Text/Image/Icon (内容组件)
      ├── Button/Input/Dropdown (交互组件)
      ├── Card/DataTable/ElevatedButton (Material 控件)
      └── ExpansionTile/SafeArea/FlexBox (高级容器)
```

**💡 提示**: 
- 所有可见 UI 元素都必须作为 Page 的子控件添加
- 使用 `page.add()` 或布局容器的 `controls` 参数挂载组件
- 可通过 `page.views[0].controls` 访问顶级控件

---

### 2.3 事件处理机制

Flet 采用**响应式事件系统**,所有交互通过回调函数实现:

**基础事件绑定**:
```python
button = fl.TextButton(
    text="提交",
    on_click=handler_func   # 直接绑定函数
)

# Lambda 表达式简化写法
btn = fl.ElevatedButton(
    text="点击",
    on_click=lambda e: print(f"点击了！{e.data}")
)
```

**带参数的事件处理**:
```python
def on_click(event: fl.ControlEvent, count: int):
    """事件处理器"""
    print(f"点击次数：{count}")
    print(f"数据：{event.data}")      # 自定义数据
    print(f"控件 ID: {event.control_id}")
    print(f"当前页：{event.current_page}")

def create_button(n: int) -> fl.TextButton:
    """创建带初始参数的按钮"""
    return fl.TextButton(
        text=str(n),
        on_click=lambda e, c=n: on_click(e, c)  # 闭包捕获 n
    )
```

**💡 提示**: 
- `event.data` 可用于传递自定义字符串数据
- 事件函数参数是可选的，可省略 `e` 和 count
- 避免在事件中创建新函数（使用闭包代替）以提升性能

---

### 2.4 状态管理基础

Flet 提供多种状态管理方式，从简单的响应式变量到复杂的状态容器:

**fl.value() - 响应式变量工厂**:
```python
# ✅ 推荐用法
count = fl.value(0)           # 创建计数器
name = fl.value("默认名称")   # 字符串状态
items = fl.value([])          # 列表状态
is_enabled = fl.value(True)   # 布尔值

# 读写操作
print(count.value)            # 0
count.value += 1              # 自增
changed = count.changed       # 是否已改变 (bool)
```

**State 容器 - 批量状态管理**:
```python
from flet import State

# 创建状态集合
states = {
    "user_name": fl.value(""),
    "user_age": fl.value(0),
    "is_admin": fl.value(False),
}

# 统一更新多个状态
def update_user(e: fl.ControlEvent) -> None:
    states["user_name"].value = input("用户名：")
    states["user_age"].value = int(input("年龄："))
    if states["user_age"].value < 18:
        states["is_admin"].value = False

# 状态订阅 (可选 - 监听变化)
states["user_name"].observer.subscribe(
    lambda obj, old, new: print(f"姓名变化：{old} -> {new}")
)
```

**💡 提示**: 
- `fl.value()` 是轻量级的，适合简单状态管理
- 复杂应用建议使用 Hooks (`use_state`) 
- 避免直接修改 `state.value` 而不触发 UI 更新

---

### 2.5 ComputedValue - 派生状态计算

**应用场景**: 需要基于多个状态源自动计算的值，类似于 React 的 computed props。

```python
from flet.utils import ComputedValue

# 基础数据源
base_price = fl.value(100)      # 原价
discount = fl.value(0.1)        # 折扣率

# 派生状态 - 自动计算价格
price = ComputedValue(
    [base_price, discount],      # 依赖列表
    lambda bp, dt: round(bp * (1 - dt), 2)  # 计算函数
)

print(price.value)  # 90.0

# 修改基础值，派生值自动更新
base_price.value = 200
print(price.value)  # 180.0 - 自动重新计算
```

**💡 提示**: 
- ComputedValue 在依赖项变化时自动触发重算
- 适用于折扣价、总价、平均值等场景
- 避免循环依赖关系

---

### 2.6 事件与 UI 联动

状态值改变会自动触发 UI 更新，无需手动刷新:

```python
# ✅ 推荐：文本实时更新
count = fl.value(0)
label = fl.Text(flv.to_str(count))  # 绑定响应式变量

def increment(e):
    count.value += 1
    label.value = f"当前计数：{count.value}"  # 直接更新

# ✅ 条件显示
is_enabled = fl.value(True)
enabled_text = fl.Text("可用", visible=is_enabled.value)
disabled_text = fl.Text("禁用", visible=not is_enabled.value)

# ✅ 样式根据状态改变
styled_btn = fl.ElevatedButton(
    text="正常" if count.value < 5 else "极限",
    bgcolor="#1976D2" if count.value < 3 else "#D32F2F",
    on_click=lambda e: setattr(count, 'value', count.value + 1),
)
```

**💡 提示**: 
- `visible` 属性控制组件是否显示 (True/False)
- `opacity` 可用于渐变过渡效果
- 避免频繁修改同一状态值（可能影响性能）

---

## 3. 组件系统详解

### 3.1 Text 文本组件

**应用场景**: 
- 📄 页面标题和描述
- 🔢 显示数据/计数器
- 🏷️ 表单标签提示

**常用属性与配置**:
```python
text = fl.Text(
    "欢迎使用 Flet",                  # 显示文本
    size=24,                          # 字体大小
    weight="bold",                    # 字重 (normal/bold)
    color="#1976D2",                  # 文字颜色
    selectable=True,                  # 可选择文本
    text_align="center",              # 水平居中
    width=300,                        # 宽度限制
    wrap=True,                        # 自动换行
    overflow="ellipsis",              # 超出显示省略号
)

# 💡 高级技巧 - 多行文本
multi_text = fl.Text(
    "这是一段很长的内容，\n需要分成多行显示。",
    width=200,
    wrap=True,
    text_align="justify"              #两端对齐
)

# 💡 自定义样式类
custom_style = fl.TextStyle(
    color="#FF5722",
    size=18,
    weight="medium",
    opacity=0.8
)
text_with_style = fl.Text(" styled text ", style=custom_style)
```

**💡 提示**: 
- `wrap=True` 必须配合指定 `width` 才能生效
- 使用 `overflow="ellipsis"` 限制超长文本显示
- 通过 `style` 参数直接设置样式对象可简化配置

---

### 3.2 Button 按钮组件

Flet 提供多种按钮类型，适用于不同场景:

**ElevatedButton (带阴影的实心按钮)**:
```python
btn = fl.ElevatedButton(
    text="提交",                    # 显示文本
    icon=fl.icons.EMAIL,            # 图标
    tooltip="发送邮件",              # 鼠标悬停提示
    on_click=lambda e: print(e.data),      # 点击事件
)

# 💡 高级配置 - 边框与圆角
styled_btn = fl.ElevatedButton(
    text="自定义样式",
    border=fl.BorderSide.all(color="#CCC", width=1),  # 边框
    shape=fl.RoundedRectangleBorder(radius=8),        # 圆角
    elevation=4,                                       # 阴影高度
)

# 💡 禁用状态
disabled_btn = fl.ElevatedButton(
    text="禁用按钮",
    disabled=True,                                    # 禁用模式
    bgcolor="#F5F5F5",                                # 禁用背景色
)
```

**FilledButton (实心填充按钮)**:
```python
filled_btn = fl.FilledButton(
    text="取消",
    tooltip="取消操作",
    on_hover=lambda e: print("鼠标悬停"),             # 悬停事件
    on_leave=lambda e: print("鼠标离开")              # 离开事件
)

# 💡 内边距控制
padded_btn = fl.FilledButton(
    text="紧凑按钮",
    padding=8,                                        # 紧凑 (默认 16)
    icon_size=20,                                     # 图标尺寸
)
```

**OutlinedButton (轮廓按钮)**:
```python
outlined_btn = fl.OutlinedButton(
    text="次要操作",
    side=fl.BorderSide(bottom=True, color="#333", width=1),  # 底部边框
    style=fl.ButtonStyle(shape=fl.RoundedRectangleBorder(radius=4))
)

# 💡 组合按钮 - 图标 + 文本
icon_text_btn = fl.OutlinedButton(
    text="带图标的操作",
    icon=fl.icons.SAVE,
    leading=True,  # 图标在左侧
)
```

### 3.3 输入控件

**TextField (文本输入框)**:
```python
field = fl.TextField(
    hint_text="请输入...",                    # 提示文字
    initial_value="默认值",                   # 初始内容
    max_length=100,                          # 最大长度
    obscure_text=True,                       # 密码模式 (隐藏字符)
    on_submit=lambda e: print(e.data),       # Enter 键事件
    keyboard_type=fl.KeyboardType.EMAIL,      # 键盘类型
    prefix_icon=fl.icons.EMAIL_OUTLINE,      # 前缀图标
)

# 💡 多行文本框 (Textarea)
textarea = fl.TextField(
    hint_text="备注内容",
    max_lines=4,                             # 最大行数
    min_lines=2,                             # 最小行数
    spellcheck=False,                        # 禁用拼写检查
)

# 💡 密码输入框
password_field = fl.TextField(
    initial_value="******",
    obscure_text=True,                       # 隐藏字符显示
    password_indicator=True,                 # 切换显隐按钮
)
```

**Dropdown (下拉选择)**:
```python
dropdown = fl.Dropdown(
    options=[
        fl.Option("选项 1"),
        fl.Option("选项 2", data={"value": 1}),
        fl.Option("选项 3", value=True),      # 默认选中
    ],
    on_change=lambda e: print(e.data, e.control.selected_index),
    width=200,
)

# 💡 高级配置 - 搜索框模式
searchable_dropdown = fl.Dropdown(
    options=[fl.Option("选项 A"), fl.Option("选项 B")],
    searchable=True,                         # 可搜索过滤
    max_search_results=5,                    # 最多显示 5 个结果
)

# 💡 多选下拉列表
multi_dropdown = fl.Dropdown(
    options=[fl.Option(i) for i in range(10)],
    multiple=True,                           # 多选模式
    on_change=lambda e: print(e.data)        # 返回选中项数据
)
```

**Checkbox (复选框)**:
```python
checkbox = fl.Checkbox(
    label="记住我",
    value=True,                              # 默认选中
    control_indicator_radius=fl.CornerRadius.all(10),  # 圆角
    on_change=lambda e: print(e.data, checkbox.value)
)

# 💡 CheckboxGroup (多选组)
group = fl.CheckboxGroup(
    options=["选项 A", "选项 B", "选项 C"],
    on_change=lambda e: print(e.data),      # 选中项列表
)

# 💡 单选按钮组 (使用 RadioGroup)
radio_group = fl.RadioGroup(
    options=["选项 A", "选项 B", "选项 C"],
    value=0,                                 # 默认选中第 0 项
    on_change=lambda e: print(e.data)       # 返回选中项索引
)
```

### 3.4 卡片与容器组件

**Card (卡片容器)**:
```python
card = fl.Card(
    content=fl.Column([
        fl.Text("标题", weight="bold"),
        fl.Text("内容描述..."),
        fl.ElevatedButton("操作按钮")
    ], spacing=10),
    elevation=6,                              # 阴影高度
    shadow_radius=4,                          # 阴影圆角半径
    border=fl.BorderSide(top=True, color="#DDD", width=1),   # 顶部边框
)

# 💡 多卡片网格布局
cards = [
    fl.Card(...),
    fl.Card(...),
]
grid = fl.GridView(
    controls=cards,
    scrollbar_always_visible=True,
    child_aspect_ratio=16/9,                  # 每个孩子的宽高比
    cross_axis_spacing=20,                    # 子元素间距
)

# 💡 可折叠卡片
collapsible = fl.Card(
    content=fl.ExpansionTile(
        leading=fl.Icon(Icons.ARTICLE),
        title="章节一",
        children=[fl.Text("内容 1"), fl.Text("内容 2")],
        expanded_alignment=fl Alignment.center,
    )
)
```

**ExpansionTile (折叠卡片)**:
```python
tile = fl.ExpansionTile(
    leading=fl.Icon(Icons.ARTICLE),
    title="章节一",
    children=[
        fl.Text("内容 1"),
        fl.Text("内容 2"),
    ],
    expanded_alignment=fl Alignment.center,     #展开时子元素对齐方式
)

# 💡 多个折叠卡片组合使用
tiles = [
    fl.ExpansionTile(...),
    fl.ExpansionTile(title="章节二", ...),
]
```

**Stepper (步骤条)**:
```python
stepper = fl.Stepper(
    controls=[
        fl.Step("第一步", icon=fl.icons.CHEvron_LEFT, on_complete=lambda e: print("完成 1")),
        fl.Step("第二步", icon=fl.icons.PEOPLE),
        fl.Step("第三步"),
    ],
    current_step=0,                            # 当前步骤索引
)

# 💡 步骤事件处理
def on_tap(step: int):
    print(f"选择步骤 {step}")

stepper.on_tap = on_tap                       # 设置点击回调
```

### 3.5 表格组件

**DataTable (数据表格)**:
```python
data = [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"},
]

table = fl.DataTable(
    columns=[
        fl.DataColumn("姓名"),
        fl.DataColumn("年龄"),
        fl.DataColumn("城市")
    ],
    data=data,
)

# 💡 自定义列类型
columns = [
    fl.DataColumn("操作", width=80),
    fl.DataColumn(
        "详情", 
        on_tap=lambda e: print(e.control.selected_data['name'])   # 点击列标题事件
    ),
]
```

### 3.6 列表与网格

**ListView (滚动列表)**:
```python
items = ["项目 1", "项目 2", "项目 3", ...]

list_view = fl.ListView(
    controls=[
        fl ListTile(
            title=item,
            on_tap=lambda e: print(e.control.selected_data),
            ...
        ) for item in items
    ],
)

# 💡 虚拟列表 (大数据集优化)
virtual_list = fl.VirtualListView(
    builder=lambda progeme: build_controls(progeme),           # 虚拟化构建器
    scrollable=True,
    physics=fl.BouncingScrollPhysics(),                         # 滚动物理效果
)
```

**GridView (网格布局)**:
```python
grid = fl.GridView(
    child_aspect_ratio=16/9,                                    # 每个单元格的宽高比
    cross_axis_count=2,                                         # 每行数量
    main_axis_spacing=10,                                       # 主轴间距
    scrollbar_always_visible=True,                              # 滚动条可见
    controls=[fl.Card(...) for _ in range(10)],
)
```

---

## 4. 响应式数据绑定

### 4.1 value() 基础用法

```python
# ✅ 推荐：使用 fl.value() 创建响应式变量
counter = fl.value(0)
text = fl.value("")
is_enabled = fl.value(True)

# 读取和修改
print(counter.value)      # 0
counter.value += 1        # 自增
print(counter.value)      # 1

# 💡 链式调用示例
counter.value = (counter.value + 1) * 2

# ✅ 检查状态变化
if counter.changed:
    print("计数已改变")
```

### 4.2 状态计算与推导

**ComputedValue - 派生状态**:
```python
from flet.utils import ComputedValue

base_price = fl.value(100)
discount = fl.value(0.1)

# 自动计算的价格
price = ComputedValue(
    [base_price, discount],
    lambda bp, dt: round(bp * (1 - dt), 2)
)

# 修改基础值，派生值自动更新
base_price.value = 200
print(price.value)  # 180.0
```

### 4.3 状态与 UI 联动

```python
# ✅ 实时更新文本
count = fl.value(0)

def on_increment(e: fl.ControlEvent) -> None:
    count.value += 1
    
label = fl.Text(flv.to_str(count))      # 绑定响应式变量

# ✅ 条件显示
enabled_text = fl.Text("可用", visible=is_enabled.value)
disabled_text = fl.Text("禁用", visible=not is_enabled.value)

# ✅ 样式根据状态改变
styled_btn = fl.ElevatedButton(
    text="点击" if count.value < 5 else "极限",
    bgcolor="#1976D2" if count.value < 3 else "#D32F2F",
    on_click=on_increment,
)
```

### 4.4 批量状态管理

**State 容器**:
```python
from flet import State

# ✅ 状态集合
states = {
    "user_name": fl.value(""),
    "user_age": fl.value(0),
    "is_admin": fl.value(False),
}

# ✅ 统一更新多个状态
def update_user(e: fl.ControlEvent) -> None:
    states["user_name"].value = input("用户名：")
    if states["user_age"].value < 18:
        states["is_admin"].value = False

# ✅ 状态订阅 (可选 - 监听变化)
states["user_name"].observer.subscribe(
    lambda obj, old, new: print(f"姓名变化：{old} -> {new}")
)
```

### 4.5 异步状态处理

**AsyncValue**:
```python
from flet.utils import AsyncValue

# ✅ 加载状态管理
loading = fl.value(False)
api_data = fl.value(None)

async def fetch_data(e: fl.ControlEvent) -> None:
    loading.value = True
    
    try:
        # 模拟 API 调用
        import asyncio
        await asyncio.sleep(2)
        
        api_data.value = {
            "name": "数据",
            "status": "success"
        }
    except Exception as ex:
        api_data.value = {"error": str(ex)}
    finally:
        loading.value = False

# ✅ UI 根据状态切换显示
result_container = fl.Text(
    "正在加载..." if loading.value 
    else f"名称：{api_data.value['name']}" 
    if api_data.value 
    else "错误",
)
```

---

## 5. Hooks 状态管理

Flet 提供 React 风格的 Hooks API，可在函数式组件中使用。

### 5.1 useState Hook

```python
from flet import use_state, use_effect

def counter_view(page: fl.Page):
    # ✅ 使用 useState 创建响应式变量
    count = use_state(0)
    
    def increment(e: fl.ControlEvent) -> None:
        count[1] += 1
    
    return fl.Column([
        fl.Text(f"计数：{count[0]}"),
        fl.ElevatedButton("增加", on_click=increment),
    ])

# 在页面中使用
page.add(counter_view(page))
```

### 5.2 useEffect Hook

**副作用处理**:
```python
from flet import use_effect

def dashboard_view(page: fl.Page):
    # ✅ 执行时触发 (类似 componentDidMount)
    def on_mount():
        print("组件已挂载")
        
    # ✅ 依赖项变化时触发 (类似 componentDidUpdate)
    effect = use_effect(
        lambda: None,  # 无返回值函数
        []  # 空依赖数组 - 只执行一次
    )
    
    def refresh_data(e: fl.ControlEvent):
        # 重新计算副作用
        pass
    
    page.add(fl.Text("数据面板"))

# ✅ 使用带依赖的 effect
def with_dep_view(page: fl.Page):
    count = use_state(0)
    
    effect = use_effect(
        lambda c=count[0]: print(f"计数变化到：{c}"),
        [count],  # 依赖当前 count
    )
    
    return fl.Column([...])
```

### 5.3 useMemo Hook

**性能优化 - 缓存计算结果**:
```python
from flet import use_memo

def filtered_list_view(page: fl.Page):
    all_items = ["项目 1", "项目 2", ...]  # 大量数据
    
    # ✅ 记住搜索结果 (只在 filter_text 变化时重新计算)
    filtered_items = use_memo(
        [item for item in all_items if filter_text.value not in item],
        dependents=[filter_text]  # 依赖项列表
    )
    
    return fl.ListView(controls=filtered_items)
```

### 5.4 useCallback Hook

**事件处理器缓存**:
```python
from flet import use_callback

def create_handler(item_id: str):
    """✅ 返回点击处理函数"""
    handler = use_callback(
        lambda e, i=item_id: print(f"点击项 {i}"),
        []  # 空依赖 - 只创建一次
    )
    return handler
```

### 5.5 useRef Hook

**DOM 引用访问**:
```python
from flet import use_ref

def focusable_input(page: fl.Page):
    # ✅ 创建引用并绑定到 TextField
    input_elem = use_ref(fl.TextField)
    
    field = fl.TextField(
        initial_value="聚焦测试",
    )
    
    def focus_field(e: fl.ControlEvent) -> None:
        if input_elem.value:
            input_elem.value.focus()
            
    return fl.Column([field, ...])
```

### 5.6 useContext Hook

**上下文共享状态**:
```python
from flet import use_context

# ✅ 创建 Context
ThemeContext = fl.Context[dict]

def create_theme_context(initial_theme: dict):
    return fl.Context.create(ThemeContext, initial_theme)

# ✅ 使用 ThemeContext
theme = use_context(ThemeContext)

def styled_component(page: fl.Page):
    current_theme = use_context(ThemeContext)
    
    btn = fl.ElevatedButton(
        text="按钮",
        bgcolor=current_theme.value.get("primary_color", "#1976D2"),
    )
    return btn
```

### 5.7 完整 Hooks 示例 - TODO 应用

```python
from flet import Page, use_state, use_effect, use_memo

def todo_app(page: Page):
    """✅ TODO 应用示例"""
    
    # ✅ 响应式状态定义
    todos = use_state([])           # 待办列表
    current_input = use_state("")   # 输入框值
    filter_text = use_state("")     # 筛选文本
    
    def add_todo(e: fl.ControlEvent) -> None:
        if current_input[1].strip():
            todos[1].append(current_input[1].strip())
            current_input[1] = ""
            
    def remove_todo(e: fl.ControlEvent, idx: int) -> None:
        todos[1].pop(idx)
        
    def toggle_complete(e: fl.ControlEvent, idx: int) -> None:
        todos[1][idx]["done"] = not todos[1][idx]["done"]
    
    # ✅ 筛选记忆化 (性能优化)
    filtered_todos = use_memo(
        [t for t in todos[1] if filter_text[1].lower() not in t["text"].lower()],
        dependents=[todos, filter_text]
    )
    
    return fl.Column([
        # ✅ 输入区域
        fl.TextField(
            initial_value=current_input[1],
            on_submit=lambda e: setattr(current_input, "1", e.data),
            on_change=lambda e: setattr(current_input, "1", e.data) if hasattr(e, 'data') else None,
        ),
        fl.ElevatedButton("添加", on_click=add_todo),
        
        # ✅ TODO 列表展示
        fl.ListView(
            controls=[
                fl.ListTile(
                    title=t["text"],
                    subtitle=fl.Text("(已完成)" if t.get("done") else ""),
                    leading=fl.Icon(Icons.CHECKBOX_MARKED if t.get("done") else Icons.CHECKBOX_BLANK),
                    on_click=lambda e, i: toggle_complete(e, i) if hasattr(e, 'control') and isinstance(e.control.selected_data, int) else None,
                ) for i, t in enumerate(filtered_todos)
            ]
        ),
    ])

page = Page()
page.add(todo_app(page))
```

---

## 6. 布局与控件

### 6.1 一维布局容器

**Column (垂直布局)**:
```python
col = fl.Column(
    controls=[
        fl.Text("第 1 行"),
        fl.Text("第 2 行"),
    ],
    spacing=10,      # ✅ 子元素间距
    alignment=fl Alignment.center,
    mainAxisSize=fl.MainAxisSize.COMPACT,  # 紧凑/松散
)

# ✅ 固定高度与溢出隐藏
fixed_col = fl.Column(
    controls=[...],
    height=200,
    overflow=fl.Overflow.HIDDEN,
)
```

**Row (水平布局)**:
```python
row = fl.Row(
    children=[
        fl.Card(...),
        fl.Card(...),
    ],
    mainAxisSize=fl.MainAxisSize.LARGEST,  # ✅ 最大/平均
    crossAxisAlignment=fl.CrossAxisAlignment.BETWEEN,  # 分布方式
)
```

### 6.2 二维布局容器

**Stack (堆叠布局)**:
```python
stack = fl.Stack(
    controls=[
        fl.Container(width=100, height=100, bgcolor="#FF0000"),
        fl.Container(offset=fl.Position(-50, -50), bgcolor="#00FF00"),
    ],
)

# ✅ 定位子元素 (绝对定位)
offsetted = fl.Container(
    offset=fl.Offsets(-30, 20),  # x, y 偏移量
    child=fl.Text("偏移")
)
```

**Padding (内边距容器)**:
```python
padded = fl.Padding(
    controls=[content],
    padding=20,  # ✅ 等间距
)

# ✅ 单独方向内边距
top_right = fl.Padding(
    top=10, right=20, bottom=5, left=15,
    children=[content]
)
```

**Margin (外边距容器)**:
```python
margined = fl.Margin(
    controls=[content],
    margin=fl.Margin.all(10),  # ✅ 等外边距
)

# ✅ 单独方向外边距
right_margin = fl.Margin(right=50, children=[content])
```

**Spacing (间距容器)**:
```python
spaced = fl.Spacing(
    main_axis_spacing=15,   # ✅ 主轴间距
    cross_axis_spacing=8,   # ✅ 交叉轴间距
    align_items=fl Alignment.center,
    children=[...],
)
```

### 6.3 分栏布局

**ColumnCrossAxis (垂直排列列)**:
```python
column_cross = fl.ColumnCrossAxis(
    cross_axis_count=2,      # ✅ 列数
    main_axis_alignment=fl Alignment.center,
    children=[
        fl.Row([...]),
        fl.Row([...]),
    ],
)

# ✅ 动态列数 (自动计算)
column_cross = fl.ColumnCrossAxis(
    cross_axis_count="auto",  # 自动计算
    main_axis_alignment=fl Alignment.spread,
    children=[content_row]
)
```

**RowMainAxis (水平排列行)**:
```python
row_main = fl.RowMainAxis(
    main_axis_count=3,       # ✅ 行数
    cross_axis_alignment=fl Alignment.center,
    children=[
        fl.Column([...]),
        fl.Column([. ..]),
    ],
)
```

### 6.4 Grid 网格布局

```python
# ✅ 栅格系统创建
from flet.controls.core import grid as gdl

grid = gdl.Grid(
    children=[
        fl.Container(width=100, height=100),
        fl.Container(width=100, height=100),
    ],
    columns=4,      # ✅ 列数
    rows=2,         # ✅ 行数
    gap=10,         # ✅ 单元格间距
)

# GridRow (单行网格)
row = gdl.GridRow(
    children=[fl.Container(...) for _ in range(5)],
)

# GridView (滚动网格视图)
view = fl.GridView(
    child_aspect_ratio=16/9,
    main_axis_alignment=fl Alignment.spread,
    cross_axis_alignment=fl Alignment.stretch,
    scrollbars_visible=True,
    scrollable=True,
    children=[. ..],
)

# GridListView (列表式网格视图)
list_view = fl.GridListView(
    scrollable=True,
    child_aspect_ratio=4/3,
    grid_column_count=3,
    children=[. ..],
)
```

### 6.5 Flex 弹性布局

**FlexBox (Flex 容器)**:
```python
flex = fl.Flex(
    direction=fl.Direction.COLUMN,  # ✅ COLUMN | ROW
    mainAxisAlignment=fl.MainAxisAlignment.SPACE_BETWEEN,  # 分布方式
    crossAxisAlignment=fl.CrossAxisAlignment.END,
    flex=[1, 2, 3],  # ✅ 各子元素弹性系数 (1:1:1)
)
```

### 6.6 SafeArea 安全区域处理

**SafeArea (适配系统 UI)**:
```python
safe = fl.SafeArea(
    child=fl.Column([. ..]),
    top=True,      # ✅ 处理顶部状态栏
    bottom=True,   # ✅ 处理底部 Home 指示器
    right=False,   # iPhone 不处理右侧
)
```

---

## 7. 高级功能

### 7.1 Canvas 绘图

```python
from flet import Canvas, Position

def canvas_view(page: fl.Page):
    def draw(e: fl.ControlEvent):
        c = e.control
        
        # ✅ 清除画布
        c.clear()
        
        # 绘制矩形
        c.rect(
            x=50, y=50, width=200, height=150,
            fill_color="#FFCCBB",
            stroke_width=3,
            stroke_color="#FF0000",
        )
        
        # 绘制圆形
        c.circle(
            x=400, y=300, radius=100,
            color="#CCCCFF",
            stroke_color="#0000FF",
        )
        
        # 绘制路径
        c.path(
            points=[Position(100, 50), Position(200, 150), Position(300, 80)],
            color="#FFFF00",
            stroke_width=5,
        )

canvas = Canvas(width=600, height=400, on_tap=draw)
page.add(canvas)
```

### 7.2 WebView 嵌入

```python
from flet import EmbedUrl

def web_view_app(page: fl.Page):
    # ✅ 内嵌网页 (支持 URL 和文件路径)
    embed = EmbedUrl(
        url="https://example.com",
        width=800,
        height=500,
    )
    
    page.add(embed)

# 💡 加载本地 HTML 文件
local_embed = EmbedUrl(
    path="file:///path/to/html.html",
    width=1200,
)
```

### 7.3 Markdown 渲染

```python
from flet import Markdown

def markdown_view(page: fl.Page):
    md = Markdown(
        "# Hello World\n\n这是**粗体**和*斜体*\n\n- 列表项 1\n- 列表项 2",
        theme=MarkdownTheme.LIGHT,      # 主题 (LIGHT/DARK)
        font_size=16,
    )
    
    page.add(md)

# 💡 自定义渲染选项
custom_md = Markdown(
    content="文档内容...",
    theme=MarkdownTheme.DARK,
    language="en-us",                  # 语言设置
)
```

### 7.4 图像与视频处理

```python
from flet import Image

def image_gallery(page: fl.Page):
    # ✅ 本地图片加载
    img = Image(
        src="path/to/image.png",
        width=200,
        height=200,
        fit=ImageFit.COVER,      # cover | contain | fill | crop
    )
    
    # ✅ URL 图片 (支持 CDN)
    web_img = Image(
        url="https://example.com/logo.png",
        cache=True,               # 启用缓存
    )
    
    # ✅ 多图网格画廊
    gallery = fl.GridView(
        child_aspect_ratio=16/9,
        scrollbars_visible=True,
        children=[Image(...) for _ in range(9)]
    )

# 💡 图片事件处理
def on_image_load(e: fl.ControlEvent):
    print(f"图片加载完成：{e.control.src}")

image = Image(url="https://example.com/pic.jpg", on_load=on_image_load)
```

### 7.5 音频播放

```python
from flet import Audio

audio = Audio(
    src="/path/to/audio.mp3",
    auto_play=False,
)

# ✅ 控制播放状态
def play(e: fl.ControlEvent):
    audio.value.play()
    
def pause(e: fl.ControlEvent):
    audio.value.pause()

def stop(e: fl.ControlEvent):
    audio.value.stop()

# 💡 音量与播放进度控制
audio.volume = 0.7                    # 设置音量 (0-1)
audio.position = 30                   # 跳转到指定秒数
```

### 7.6 表单验证

```python
from flet import TextField, Text, Column

def form_app(page: fl.Page):
    # ✅ 定义字段配置
    fields = {
        "username": TextField(
            initial_value="",
            hint_text="用户名",
            on_submit=lambda e: validate_form(),
            error_style=fl.TextStyle(color="#D32F2F"),     # 错误提示颜色
        ),
        "email": TextField(
            initial_value="",
            hint_text="邮箱",
            keyboard_type=KeyboardType.EMAIL,
            on_change=validate_email,    # ✅ 实时验证
        ),
    }
    
    def validate_form():
        # ✅ 收集错误信息
        errors = []
        for key, field in fields.items():
            if not field.value:
                errors.append(f"{key} 不能为空")
                
        if errors:
            page.snackbar("\n".join(errors))           # 显示错误提示
        else:
            page.dialog = fl.AlertDialog(
                title=fl.Text("提交成功"),
                content=fl.Text("表单验证通过！"),
                actions=[
                    fl.TextButton("关闭", on_click=lambda _: page.dialog = None)
                ],
            )
            
    return Column([
        TextField(hint_text="密码", obscure_text=True),
        # ...
    ])

# 💡 正则表达式验证
def validate_email(e: fl.ControlEvent):
    email = e.control.value
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        e.control.error_text = "邮箱格式不正确"
```

---

## 8. 实际项目案例

### 8.1 登录系统示例

```python
import flet as fl

class LoginSystem:
    def __init__(self, page: fl.Page):
        self.page = page
        self.users = {
            "admin": {"password": "123456", "role": "管理员"},
            "user": {"password": "123456", "role": "普通用户"},
        }
        
        # ✅ UI 元素创建
        self.username_field = fl.TextField(hint_text="用户名")
        self.password_field = fl.TextField(hint_text="密码", obscure_text=True)
        self.login_btn = fl.ElevatedButton("登录")
        self.error_label = fl.Text("", color="#D32F2F")
        
    def _render_ui(self):
        """✅ 渲染登录界面"""
        return fl.Column([
            fl.Text("登录系统", size=24, weight="bold"),
            fl.Spacing(height=20),
            self.username_field,
            self.password_field,
            self.error_label,
            self.login_btn,
            fl.Spacing(height=20),
            fl.Text("(账号：admin/user | 密码：123456)", size=10),
        ])
        
    def _on_login(self, e):
        """✅ 登录按钮点击处理"""
        username = self.username_field.value
        password = self.password_field.value
        
        if not username or not password:
            self.error_label.value = "请填写完整信息"
            return
            
        user = self.users.get(username)
        if not user or user["password"] != password:
            self.error_label.value = "用户名或密码错误"
        else:
            # ✅ 登录成功 - 显示欢迎弹窗
            role = user["role"]
            message = f"欢迎，{username}!\n角色：{role}"
            
            fl.popup(
                page=self.page,
                content=fl.Text(message, size=18),
                width=300,
                height=200,
            )

app = LoginSystem(fl.Page())
page = fl.Page()
page.add(app._render_ui())
```

### 8.2 数据仪表盘示例

```python
import flet as fl

def dashboard_page(page: fl.Page):
    """✅ 完整的仪表盘页面"""
    
    # ✅ 统计卡片创建
    stats = [
        fl.Card(content=fl.Column([
            fl.Text("1,234", size=28, weight="bold"),
            fl.Text("访问量", size=12),
        ])),
        fl.Card(content=fl.Column([...])),  # ...更多统计卡片
    ]
    
    # ✅ 图表区域 (使用 Canvas)
    chart = Canvas(width=600, height=300)
    
    # ✅ 导航栏布局
    nav_bar = fl.Row(controls=[. ..])  # Tab 导航
    
    return fl.Column([
        nav_bar,                    # 导航栏
        fl.Container(
            padding=20,
            content=fl.Row([
                fl.Column(controls=stats),  # 左侧统计面板
                chart,                      # 右侧图表区域
            ], scrollable=True),
        ),
    ])

# 💡 创建仪表盘视图
view = Page()
view.add(dashboard_page(view))
```

### 8.3 文件管理器示例

```python
import flet as fl

def file_manager(page: fl.Page):
    """✅ 简单文件浏览器"""
    
    # ✅ 文件系统状态
    current_dir = fl.value("/")     # 当前路径
    file_list = fl.value([])        # 文件列表
    
    def navigate(e: fl.ControlEvent, path: str):
        """✅ 导航到目录"""
        current_dir.value = path
        # 列出该目录下的文件和子目录...
        
    # ✅ 文件夹树视图
    tree = fl.TreeView(
        data=[
            {"name": "文档", "type": "dir", "path": "/Documents"},
            {"name": "图片", "type": "dir", "path": "/Images"},
            {"name": "下载", "type": "dir", "path": "/Downloads"},
        ]
    )
    
    return fl.Column([tree, ...])

page.add(file_manager(page))
```

---

## 9. 部署与发布

### 9.1 桌面应用打包

```python
# ✅ Windows/Linux/Mac GUI 打包配置
fl.run(
    view=flet.ViewType.WINDOWED,   # 窗口化模式
    dark_mode=False,               # 启用深色模式适配
    icon="app_icon.ico",           # 自定义图标
)

# 💡 使用 PyInstaller 打包为独立 EXE
from PyInstaller import build

build.executable(
    "main.py",                     # 主程序入口
    name="MyFletApp.exe",
    icon="app.ico"
)
```

### 9.2 Docker 部署 (生产环境推荐)

```dockerfile
# ✅ Dockerfile 示例
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install flet[all]

EXPOSE 8888
CMD ["python", "main.py"]
```

**💡 启动命令**:
```bash
# 本地开发运行
docker-compose up -d

# 生产环境部署
docker build -t my-flet-app .
docker run -p 8888:8888 my-flet-app
```

### 9.3 Web 托管服务

**使用 Netlify/Vercel 部署**:
```python
# ✅ 纯 HTTP 服务器配置
from flet import run

run(
    host="0.0.0.0",                # 监听所有网卡
    port=8888,                     # 端口号
    view=flet.ViewType.WEBSITE     # 网页模式
)

# 💡 生成部署配置文件 (Netlify.toml)
[build]
command = "pip install -r requirements.txt && python main.py"
```

**使用 Heroku 部署**:
```yaml
# ✅ Procfile 配置
web: python main.py --host=0.0.0.0 --port=$PORT

# runtime.txt
python-3.10.6
```

### 9.4 移动端 WebView 容器

**iOS/Android WebView 集成**:
```python
from flet import ViewType

def mobile_app():
    page = fl.Page()
    
    # ✅ WebView 模式 (适合 iOS/Android)
    view = ViewType.CAPTURED_WINDOW
    
    # 💡 原生容器配置 (需配置证书等)
    container = ViewType.NATIVE_CONTAINER
    
    fl.app.run(view=view)
```

---

## 10. 最佳实践

### 10.1 代码组织建议

**推荐项目结构**:
```
my_flet_app/
├── main.py                  # 应用入口 (Page 配置)
├── views/                   # UI 视图模块
│   ├── home.py             # 主页视图
│   ├── dashboard.py        # 仪表盘视图
│   └── settings.py         # 设置页面
├── models.py                # 数据模型定义
├── services.py              # API/后台服务函数
├── utils.py                 # 工具函数集合
└── static/                  # 静态资源 (CSS/JS)
```

**入口文件示例 (main.py)**:
```python
from views import home, dashboard, settings
from models import User

def main(page: fl.Page):
    """✅ 应用主入口"""
    
    # 📋 状态管理 - 用户会话
    user = fl.value(None)       # 当前登录用户
    current_view = fl.value("home")  # 当前视图名称
    
    # 🎨 路由导航配置
    views = {
        "home": home_view,
        "dashboard": dashboard_view,
        "settings": settings_view,
    }
    
    def on_click(e: fl.ControlEvent):
        """✅ 导航事件处理"""
        current_view.value = e.data      # 切换到指定视图
        
    # 🔘 首页主按钮
    home_btn = fl.ElevatedButton(
        text="首页",
        on_click=lambda e, v="home": setattr(current_view, 'value', v)
    )
    
    page.add(home_btn)

fl.app.run()
```

### 10.2 性能优化建议

**✅ 关键优化点**:

1. **使用 useMemo 缓存计算**
```python
from flet import use_memo

# ✅ 记住搜索/过滤结果 (避免重复计算)
filtered_items = use_memo(
    [item for item in all_items if filter_text.value not in item],
    dependents=[filter_text]  # 依赖项列表
)
```

2. **避免在事件中创建新函数**
```python
# ❌ 不推荐：每次点击都创建新 lambda
btn = fl.TextButton(
    text="点击",
    on_click=lambda e: handle_action(e, count=0)   # 性能问题
)

# ✅ 推荐：预先定义处理函数
def handler(count):
    return lambda e: handle_action(e, count=count)

btn = fl.TextButton(
    text="点击",
    on_click=handler(0)
)
```

3. **大数据集使用虚拟列表**
```python
# ✅ 仅渲染可视区域的虚拟列表
virtual_list = fl.VirtualListView(
    builder=lambda progeme: build_controls(progeme),       # 构建器
    scrollable=True,
    physics=fl.BouncingScrollPhysics()
)
```

4. **延迟非关键渲染**
```python
# ✅ 使用 use_effect 执行副作用处理
effect = use_effect(
    lambda: None,                                           # 无返回值函数
    []                                                      # 空依赖 - 只执行一次
)
```

### 10.3 类型安全与文档

```python
from typing import TypedDict, Optional

class UserData(TypedDict):
    """✅ 用户数据模型定义"""
    id: int
    name: str
    age: int
    email: Optional[str]  # 可选字段
```

**💡 最佳实践总结**:
- ✅ 使用 `use_memo` 优化频繁计算的列表过滤/排序
- ✅ 事件处理器避免每次重新创建（使用闭包或 useCallback）
- ✅ 大数据集优先使用虚拟列表 (`VirtualListView`)
- ✅ 为复杂组件添加类型注解和文档说明
- ✅ 使用 `Observer` 订阅状态变化而非轮询

---

## 📖 附录

### A. API 速查表

| 模块 | 说明 |
|------|----------|
| `fl.Page` | 页面容器 (所有 UI 组件的根节点) |
| `fl.Column` | 垂直布局容器 |
| `fl.Row` | 水平布局容器 |
| `fl.Stack` | 堆叠布局容器 (绝对定位子元素) |
| `fl.value()` | 响应式变量创建器 |
| `use_state()` | Hooks 状态管理 - 替代 fl.value() |
| `use_effect()` | Hooks 副作用处理 |
| `use_memo()` | 缓存计算结果，优化性能 |

### B. 常用快捷键与调试技巧

- **Cmd/Ctrl + R** - 重新渲染 (强制刷新 UI)
- **F5** - 刷新页面 (Web 模式)
- **Debug 模式**: `fl.run(debug=True)` - 启用断点调试
- **Console 输出**: 使用 `print()` 或浏览器开发者工具
- **性能分析**: Chrome DevTools Performance 面板

### C. 资源推荐

- 📚 **官方文档**: https://flet.dev/docs/
- 💬 **社区论坛**: https://github.com/flet-dev/flet/discussions
- 🐦 **Twitter**: @flet_dev
- ⭐ **GitHub**: https://github.com/flet-dev/flet

---

*文档版本：0.82.2+*  
*最后更新：2024 年*