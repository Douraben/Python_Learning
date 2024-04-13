# 3.5元组tuple
# 元组是指由用圆括号，逗号分隔的值组成的序列，它与列表类似，但元组一旦创建就不能修改。

# 3.5.1元组定义
# 定义一个元组tuple_name，包含元素12和字符串"name"
tuple_name = (12, "name")
# 显式指定类型方式定义一个元组tuple_name_0，包含元素"value1"和"value2"
tuple_name_0: tuple = ("value1", "value2")
# 显式指定类型方式定义一个元组tuple_name_1，包含元素1,2,3,4,5
tuple_name_1: tuple = (1, 2, 3, 4, 5)
# 定义一个空元组tuple_name_2
tuple_name_2 = ()

# 3.5.2遍历元组中所有的值
for value in tuple_name:
    print(value)
