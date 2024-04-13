# 3.3创建数值列表

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3.3.1使用range()函数
"""
range()生成一个整数序列，从指定的第一个值开始数，并在到达指定的第二个值时停止，因此输出不包含第二个值本身，
range(start,stop,step)
start：第一个参数是开始值，stop：第二个参数是结束值，step：第三个参数是步长（没有步长时，默认为1）
"""


for number in range(10):  # 也不设置开始值，默认从0开始取值0-9赋值给number
    print(number)
print("\n")

for number in range(1, 10):  # 通过for循环range输出1-9赋值给number
    print(number)
print("\n")

for number in range(1, 10, 2):  # 通过for循环range输出1-9之间步长为2取值赋值给number（1，3，5，7，9）
    print(number)
print("\n")

for number in range(len(list_number)):
    print(list_number[number])

# 3.3.2使用range()函数创建数值列表

list_number_0 = list(range(10))  # 创建一个包含0-9的列表
print(list_number)

list_number_1 = list(range(1, 10))  # 创建一个包含1-9的列表
print(list_number_1)

list_number_2 = list(range(1, 10, 2))  # 创建一个包含1-9之间步长为2的列表
print(list_number_2)

list_number_3 = []  # 创建一个空列表
for number in range(1, 10):
    number = number ** 5
    list_number_3.append(number)  # 把每次循环的number添加到list_number_3列表中
print(list_number_3)

# 3.3.3对数值列表执行简单的统计计算
print(sum(list_number_3))  # 通过sum()函数求列表元素数值和
print(max(list_number_3))  # 通过max()函数求列表元素最大值
print(min(list_number_3))  # 通过min()函数求列表元素最小值

# 3.3.4列表推导式（list comprehension）
# 列表推导式提供了从序列创建列表的简单而高效的方法
# 列表推导式（list comprehension）将for循环和创建新元素的代码合并成一行，并自动附加新元素
list_number_4 = [number ** 2 for number in range(1, 10)]
print(list_number_4)
for number_0 in list_number_4:
    print(number_0)
