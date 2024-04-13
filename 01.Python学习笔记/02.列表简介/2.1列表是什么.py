# 2.1列表是什么

# 列表 list 由一系列按特定顺序排列的元素组成；用方括号（[]）表示列表，列表元素之间用逗号分隔。

# 列表是Python中使用最频繁的数据类型。

# 定义一个空列表name_list
name_list = []
# 定义一个列表name_list_1，其中包含三个元素'a', 'b', 'c'
name_list_1 = ['a', 'b', 'c']

# 显式指定类型方式定义一个列表name_list_2，其中包含三个元素'a', 'b', 'c'和一个整数1, 2, 3
name_list_2: list = ['a', 'b', 'c', 1, 2, 3]
# 显式指定类型方式定义一个空列表name_list_3
name_list_3: list = []

print(name_list, name_list_1, name_list_2, name_list_3)

# 访问列表的元素
# 访问列表name_list_1的第一个元素
print(name_list_1[0])  # 输出：a
print(f"将{name_list_1[0]}字母转换成大写输出：{name_list_1[0].title()}")  # 小写转换大写输出：A

# Python中，第一个列表元素的索引为0、而不是1， -1表示最后一个元素


