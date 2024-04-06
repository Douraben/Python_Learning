# 5.3嵌套


# 5.3.1字典列表----字典嵌套列表--------------------------------------------

# 假设我们想创建一个字典列表，其中每个字典都包含学生姓名和年龄、成绩。
student_0 = {"name": "周日", "age": "12", "score": 90}  # 定义一个字典
student_1 = {"name": "周一", "age": "13", "score": 80}
student_2 = {"name": "周二", "age": "14", "score": 70}
student_3 = {"name": "周三", "age": "15", "score": 60}
student_4 = {"name": "周四", "age": "16", "score": 50}

student_list = [student_0, student_1, student_2, student_3, student_4]  # 创建一个字典列表

print(student_list)

for student in student_list:  # 遍历字典列表
    print(student)

for n in range(len(student_list)):  # 遍历字典列表
    print(student_list[n])

student_name = []  # 创建一个空列表,添加一部字典到列表
for n in range(10):
    student_name.append(student_0)  # 添加一部字典到列表

for n in range(len(student_name)):
    student_name[n]["name"] = str(n)  # 修改字典中的值
    print(student_name[n])

for name in student_name:  # 遍历字典列表
    name["name"] = "三好学生"  # 修改字典中的值
    print(name)

# 5.3.2在字典中存储列表---列表嵌套字典----------------------------

dict_name = {
    # 键是"name"，值是"label"
    "name": "label",
    # 键是"info"，值是一个列表，包含两个字符串，一个是"36岁"，另一个是"china"
    "info": ["36岁", "china"]
}

print(dict_name["name"])
for info in dict_name["info"]:  # 遍历字典中列表
    print(info)

# 定义一个字典，包含name、age、add、score四个键，对应的值为列表
dict_name_0 = {
    "name": ["label", "label1", "label2"],
    "age": [12, 13, 14],
    "add": ["china", "china", "china"],
    "score": [90]
}
# 遍历字典中的所有键值对
for key, value in dict_name_0.items():
    # 打印键
    print(key)
    # 如果值的长度大于1
    if len(value) > 1:
        # 遍历值中的所有元素
        for info in value:
            # 打印元素
            print(info)
    else:
        # 打印第一个元素
        print(value[0])

# 5.3.3在字典中存储字典----字典嵌套字典----------------------------------------

dict_name_1 = {  # 定义字典嵌套字典
    "name_0": {
        "name": "卡卡",
        "xb": "男",
        "age": 12,
        "add": "china"
    },

    "name_1": {
        "name": "娜娜",
        "xb": "女",
        "age": 13,
        "add": "china"
    }
}
# 遍历字典dict_name_1
for key, value in dict_name_1.items():
    # 打印键key
    print(key)
    # 遍历字典value的键值对
    for ke, va in value.items():
        # 打印键ke和值va
        print(ke, va)
