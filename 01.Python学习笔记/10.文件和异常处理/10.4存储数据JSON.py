# -*- coding: utf-8 -*-
# 10.4数据存储 json
# json模块是Python中用于处理JSON（JavaScript Object Notation）数据格式的一个库。
# 它提供了将Python对象转换为JSON格式以及将JSON数据转换为Python对象的功能。

"""
Python的json模块提供了以下常用方法：

json.dumps()：将Python对象转换为JSON格式的字符串。

json.loads()：将JSON格式的字符串转换为Python对象。

json.dump()：将Python对象转换为JSON格式的字符串，并将其写入文件。

json.load()：从文件中读取JSON格式的字符串，并将其转换为Python对象。

json.JSONDecodeError：当解析JSON数据时发生错误时抛出的异常。

json.JSONEncodeError：当将Python对象转换为JSON格式时发生错误时抛出的异常。
"""
import json  # 导入json模块

# 将Python对象转换为JSON格式的字符串
json_str = json.dumps([1, 2, 3])
print(json_str)  # 输出：[1, 2, 3]

# 将JSON格式的字符串转换为Python对象
python_obj = json.loads(json_str)
print(python_obj)  # 输出：[1, 2, 3]

# 将Python对象转换为JSON格式的字符串，并将其写入文件
with open('file/data.json', 'w') as f:
    json.dump([1, 2, 3], f)

# 从文件中读取JSON格式的字符串，并将其转换为Python对象
with open('file/data.json', 'r') as f:
    python_obj = json.load(f)
print(python_obj)  # 输出：[1, 2, 3]

# 10.4.1 使用json.dumps()和json.loads()
from pathlib import Path

name = ["北京市", "天津市", "河北省", "内蒙古自治区", "辽宁省", "吉林省", "黑龙江省", "上海市"]

try:
    # 定义一个Path对象，路径为json_file.json
    path_file = Path("file/json_file.json")
    # 将name转换为json格式
    json_file = json.dumps(name)
    # 将json格式的name写入json_file1.json文件
    path_file.write_text(json_file)
except FileNotFoundError as e:
    # 如果文件不存在，则抛出异常
    print(f"json文件异常，原因：{e}")
else:
    # 如果文件存在，则打印文件写入成功
    print("json文件写入成功！")
# ------------------------------------------------------------------------
try:
    # 以写入模式打开json文件，编码为utf-8
    with open("file/json_file.json", "w", encoding="utf-8") as f:
        # 将name转换为json格式
        jsonf_file = json.dumps(name)
        # 将json格式的name写入json文件
        f.write(jsonf_file)
except FileNotFoundError as e:
    # 抛出文件未找到异常
    print(f"json文件异常，原因：{e}")
else:
    # 文件写入成功
    print("json文件写入成功！")

# -----------------------------------------------------------------
with open("file/json_file.json", "r", encoding="utf-8") as f:
    open_file1 = json.loads(f.read())
    print(open_file1)

# 10.4.2 保存和读取用户生产的数据---------------------------------------
# exists()方法检查给定的文件路径是否存在，如存在返回True,否则False

path_file2 = Path("file/json_file22.json")
if path_file2.exists():      # exists()方法检查给定的文件路径是否存在，如存在返回True,否则False
    open_file2 = json.loads(path_file2.read_text(encoding="utf-8"))
    print(open_file2)
else:
    open_file2=json.dumps(name)
    path_file2.write_text(open_file2)
    print("数据不存在，已写入成功！")
