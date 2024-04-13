# 5.2遍历字典
"""
 即可遍历字典的所有键值对，也可只遍历键或值。
 使用for循环遍历字典的键值对
 使用for循环遍历字典的时，声明两个变量，分别用于存储键和值，然后按顺序遍历它们。

"""

dict_name_3 = {  # 创建一个包含多个键值对的字典,
    "name": "地球",
    "age": 10000,
    "planet": "地球",
    "moons": 1,
    "rings": False,
}
# 5.2.1 遍历所有的键值对
for key, value in dict_name_3.items():  # items()方法可以返回一个键值对列表
    print(key, value)

# 5.2.2 遍历所有的键
for key in dict_name_3.keys():  # keys()方法可以返回一个键列表
    print(key.title())

# 5.2.3 遍历所有的值
for value in dict_name_3.values():  # values()方法可以返回一个值列表
    print(value)

# 5.2.4 按特点的顺序遍历字典中的所有键值
for key in sorted(dict_name_3.keys()):  # sorted()方法可以返回一个已排序的键列表
    print(key.title(), dict_name_3[key])
