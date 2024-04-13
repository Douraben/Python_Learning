# -*- coding: utf-8 -*-
# 10.3 异常 (exception)

# 异常是使用tpy-except代码块处理的

# 10.3.1 处理ZeroDivisionError异常---------------------------------------
# print(5/0)
# Traceback (most recent call last):
#   File "G:\Python\Python_Learning\01.Python学习笔记\10.文件和异常处理\10.3异常.py", line 8, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero

# 10.3.2 使用tpy-except代码块---------------------------------------------
# try-except 代码块是 Python 中的一个错误处理机制，用于捕获和处理代码块中可能发生的异常。
# 当程序运行时，如果发生异常，程序会跳转到 except 代码块，执行其中的代码。
# 使用异常避免崩溃
# try 代码块中放置可能引发异常的代码，except 代码块中放置处理异常的代码

a = 5
b = 0
try:
    c = a / b
    print(c)
except ZeroDivisionError:  # 捕获所有错误
    print("除法无法执行")

# 10.3.4 else 代码块-----------------------------------------------------
# 只有可能引发异常的代码才需要放在try语句中
a = 5
b = 0
try:  # 尝试执行以下代码
    c = a / b  # 计算a除以b的结果
except ZeroDivisionError:  # 如果发生ZeroDivisionError错误
    print("除法无法执行")  # 输出提示信息
else:  # 如果代码没有发生错误执行
    print(c)  # 输出计算结果

# 10.3.5 异常FileNotFoundError异常---------------------------------------

from pathlib import Path

file = ""
try:
    open_file = Path("file/file.txt")
    file = open_file.read_text(encoding="utf-8")
except FileNotFoundError as e:
    print(f"文件异常,原因{e}")
else:
    print(file)
# ---------------------------------------------------------------------
file1 = ""
try:
    with open("file/file_w.txt", "r", ) as file_name:
        file1 = file_name.read()
except FileNotFoundError as e:
    print(f"文件异常，原因:{e}")
else:
    print(file1)


# 10.3.6 静默失败--------------------------------------------------------
# python中有个pass语句，可在代码块中使用它来什么都不做，充当了占位符
def name_mian():
    pass


if True:
    pass

for i in range(10):
    pass

# 10.3.9 决定报告哪些错误--------------------------------------------------
