# 5.1使用字典 (键值对）
"""
字典（dictionary）是一系列键值对，其中每个键都映射到一个值，
可以使用键来访问相应的值。
与键关联的值可以是数字、字符串、列表、字典等Python对象。
字典中储存多少和键值对都可以的
"""

# 字典的定义：放在方括号中，键值对用冒号分隔，多个键值对用逗号分隔
dict_name: dict = {}  # 显形定义方式创建一个空字典
dict_name_0 = {}  # 创建一个空字典
dict_name_1 = {'name': '地球', 'age': 10000}  # 创建一个包含两个键值对的字典
dict_name_2 = dict(key1='value1', key2='value2')  # 通过dict()函数转换成字典，并赋值dict_name_2

dict_name_3 = {  # 创建一个包含多个键值对的字典,
    "name": "地球",
    "age": 10000,
    "planet": "地球",
    "moons": 1,
    "rings": False,
}

# 5.1.1 访问字典中的值
print(dict_name_1['name'])
print(dict_name_1["age"])

# 5.1.2 字典中添加键值对
dict_name_1['y'] = 42.00
dict_name_1['x'] = 3.14
print(dict_name_1)

# 已创建的空字典中添加键值对
dict_name_0['name'] = '月亮'
dict_name_0['age'] = 1000000000000000000000000000000000000000000000000000000
print(dict_name_0)

# 5.1.4 修改字典中的值
if dict_name_1['name'] == '地球':
    dict_name_1['name'] = '太阳'  # 修改字典中的值
else:
    dict_name_1['age'] = 80000  # 修改字典中的值
print(dict_name_1)


# 5.1.5 删除字典中的键值对
# 使用del语句将相应的键值对彻底删除
del dict_name_1['y']
print(dict_name_1)

# 使用pop()方法将相应的键值对删除，并返回被删除的值
value = dict_name_1.pop('age')
print(value)
print(dict_name_1)

# 使用popitem()方法将最后一个键值对删除，并返回被删除的键值对
print(dict_name_3)
key, value = dict_name_3.popitem()
print(key, value)
print(dict_name_3)


# 5.1.6使用get()来访问字典中的值
# 访问字典中的值，如果键不存在，返回None，不会报错.
print(dict_name_1.get('name'))
print(dict_name_1.get('z'))     # 不存在的键值对，返回None


