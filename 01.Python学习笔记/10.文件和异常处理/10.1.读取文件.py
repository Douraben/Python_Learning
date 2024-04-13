# 10.1读取文件

# 10.1.1读取文件的全部内容
# 有两种方式可以读写文件操作：

# 10.1.1.1 利用pathlib模块中Path类读写文件操作-----------------------------------
from pathlib import Path

# 导入Path模块
from pathlib import Path

# 创建一个Path对象，指定文件名为file.txt
path_file = Path("file/file.txt")

# 使用read_text()方法读取文件内容，并打印文件内容
print(path_file.read_text(encoding="utf-8"))  # text()方法中可以设置编码为utf-8

# 10.1.1.2 利用open()函数读写文件操作--------------------------------------------

# open()第一种方法，读取完毕后关闭文件操作
# 打开一个文件，并将其命名为file.txt，以只读模式打开，编码为utf-8
open_file1 = open("file/file.txt", "r", encoding="utf-8")
# 使用read()方法取读 文件内容并打印
print(open_file1.read())
# 关闭文件
open_file1.close()

# open()第二种方法，使用with语句可以帮助你自动管理资源，确保资源在使用完毕后被正确关闭。
with open("file/file.txt", "r", encoding="utf-8") as open_file:
    print(open_file.read())

"""
open() 和 Path 是 Python 中处理文件和目录的两种不同方法。

open() 函数用于打开一个文件，并返回一个文件对象。文件对象可以用于读取、写入或追加文件内容。使用 open() 函数打开文件后，需要手动关闭文件，以确保资源被正确释放。

Path 是 Python 3.4 引入的一个新特性，它是一个路径对象，用于表示文件系统中的文件和目录。与 open() 函数相比，Path 对象提供了更高级的文件系统操作，如读取、写入、查找文件等。使用 Path 
对象可以避免手动关闭文件，因为当 Path 对象被销毁时，它会自动关闭文件。

Path 对象的主要优点如下：

更简洁的语法：使用 Path 对象可以简化文件和目录的表示，例如 Path('file.txt') 表示文件 file.txt。
更丰富的功能：Path 对象提供了许多有用的方法，如 read()、write()、glob() 等，可以方便地读取、写入、查找文件等。
自动关闭文件：当 Path 对象被销毁时，它会自动关闭文件，无需手动关闭。
Path 对象的主要缺点如下：

兼容性问题：Path 对象在 Python 2.7 和 Python 3.3 中不受支持，需要使用第三方库 pathlib 进行兼容。 性能问题：Path 对象在某些情况下可能比 open() 
函数更慢，因为它需要进行额外的文件系统操作。 总结：open() 函数和 Path 对象都是 Python 中处理文件和目录的常用方法，具体使用哪种方法取决于你的需求和场景。如果你需要更简洁的语法和更丰富的功能，可以使用 Path 
对象；如果你需要更高的性能和兼容性，可以使用 open() 函数。

"""

# 10.1.2相对文件路劲和绝对文件路径----------------------------------------------------------
# 相对文件路径：相对于当前运行程序的所在目录的指定位置查找，如：
# path_file = Path("file.txt")

# 绝对文件路径：在计算机中的准确位置查找，不用管当前运行程序的存储位置，如：
# path_file = Path("G:\Python\Python_Learning\01.Python学习笔记\10.文件和异常处理\file.txt")
# 使用绝对路径，可以读取系统中任何位置的文件
# 在显示文件路劲时，windows系统中使用反斜杠（\）,而不是反斜杠（/)


# 10.1.3 访问文件中的各行------------------------------------------------------------------
# Path中可以使用splitlines()方法将冗长的字符串转换为一系列行，在使用for循环以每次一行的方式

# 创建一个Path对象，指定文件名为file.txt
path_file1 = Path("file/file.txt")
# 使用read_text()方法读取文件path_file1的内容读
list_file = path_file1.read_text("utf-8")
# 将文件内容按行
list_f = list_file.splitlines()  # 字符串转分割换为列表
# 遍历每一行
print(list_f)
for f in list_f:
    # 打印每一行
    print(f)

# open(）中可以使用splitlines()方法将冗长的字符串转换为一系列行，在使用for循环以每次一行的方式
# 打开文件file.txt，以只读模式，编码utf-8
with open("file/file.txt", "r", encoding="utf-8") as open_file:
    # 读取文件内容
    open_f = open_file.read()
    # 将文件内容按行分割
    open_f_list = open_f.splitlines()
    # 打印分割后的文件内容
    print(open_f_list)
    # 遍历文件内容
    for f_list in open_f_list:
        # 打印每一行内容
        print(f_list)

# 10.1.4 使用文件内容-------------------------------------------------------------------
# 打开文件file.txt，以只读模式，编码utf-8
with open("file/file.txt", "r", encoding="utf-8") as open_file1:
    # 读取文件内容，并以换行符分割
    open_f1 = open_file1.read().splitlines()
    # 创建空字符串open_string
    open_string = ""
    # 遍历open_f1，将每一行拼接到open_string
    for f_list1 in open_f1:
        open_string += f_list1
        # 打印每一行
        print(f_list1)
    # 打印open_string
    print(open_string)
    print(open_string[0:12])  # [0:12]是指截取字符从0到11，不包含12表示。
