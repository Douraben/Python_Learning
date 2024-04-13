"""
13.1.1 什么是正则表达式？
正则表达式是一种用于匹配和处理字符串的强大工具，它可以让你轻松地处理字符串中的特定部分，而不需要手动编写复杂的字符串处理代码。在Python中，re模块提供了正则表达式的支持。

实现原理：正则表达式是一种基于文本匹配的搜索方法，它使用特定的字符和符号来描述要匹配的文本模式。当你使用正则表达式时，它会根据你提供的模式来查找和匹配字符串中的特定部分。

用途：正则表达式在许多场景下都有其独特的用途，例如：

数据解析：正则表达式可以用来从文本中提取和解析数据，例如从网页中提取链接、图片等。

文本处理：正则表达式可以用来替换、删除或修改文本中的特定部分，例如将文本中的所有空格替换为下划线。

验证：正则表达式可以用来验证用户输入的数据是否符合预期的格式，例如验证电子邮件地址、密码等。

注意事项：在使用正则表达式时，需要注意以下几点：

特殊字符：正则表达式中的特殊字符需要使用反斜杠（\）进行转义，例如，要匹配点（.），需要使用正则表达式中的点（.）。

量词：正则表达式中的量词用于指定匹配字符或字符串的次数，例如，* 表示匹配零个或多个字符，+ 表示匹配一个或多个字符。

组：正则表达式中的组用于将匹配的文本分组，以便在匹配成功后对其进行操作。例如，使用（）将匹配的文本分组，然后使用\1、\2等引用组中的内容。

模式：正则表达式中的模式用于指定匹配的起始位置和结束位置，例如，^ 表示匹配字符串的开头，$ 表示匹配字符串的结尾。



13.1.2 常用的函数和方法：
re.compile(pattern): 将正则表达式的字符串形式编译成一个Pattern对象。这个对象可以用于匹配和搜索字符串。

re.search(pattern, string): 在字符串中搜索正则表达式pattern匹配的子串。如果匹配成功，返回一个Match对象；否则返回None。

re.match(pattern, string): 从字符串的开头开始匹配正则表达式pattern。如果匹配成功，返回一个Match对象；否则返回None。

re.findall(pattern, string): 查找字符串中所有匹配正则表达式pattern的子串，并将其以列表的形式返回。

re.finditer(pattern, string): 查找字符串中所有匹配正则表达式pattern的子串，并将其以迭代器的形式返回。

re.sub(pattern, repl, string): 将字符串中所有匹配正则表达式pattern的子串替换为repl。

re.split(pattern, string): 根据正则表达式pattern拆分字符串，并将其以列表的形式返回。

"""

import re

name = "asdfgasdfg"
# 使用re.match()函数匹配"as"在name中的位置，从头开始匹配，头部未能匹配的不再执行匹配
r_match= re.match("as", name)
# 打印匹配结果
print(r_match)
# 打印匹配位置
print(r_match.span())
# 打印匹配到的字符
print(r_match.group())

# 使用re模块的search函数，在name字符串中查找"ga",全局匹配，只会找出第一个值返回，之后的不在匹配
r_search=re.search("ga",name)
# 打印r_search
print(r_search)
# 打印r_search的span()，即匹配到的字符串在name中的位置
print(r_search.span())
# 打印r_search的group()，即匹配到的字符串
print(r_search.group())


# 使用re模块的findall函数查找字符串name中所有匹配的子串"a",全局匹配，找出所有值返回列表值，
r_findall=re.findall("a",name)
# 打印查找结果
print(r_findall)
# 遍历查找结果
for r_name in r_findall:
    # 打印每一个匹配的子串
    print(r_name)