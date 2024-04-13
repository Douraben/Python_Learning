# 2.2修改、添加、删除元素

# 2.2.1修改列表元素
name_list = ["kaka", "momo", "lili", "jjj", "kkk"]
print(name_list)
name_list[0] = "大千世界"  # 列表中的第一个元素值被修改为：大千世界
print(name_list)

# 2.2.2列表中添加元素
# 2.2.2.1修改列表元素_在列表末尾添加元素:追加append()
name_list.append("你好，世界！")  # 列表末尾添加元素
print(name_list)

# 2.2.2.2修改列表元素_在列表中插入元素：任意位置插入新元素insert()
name_list.insert(1, "浩瀚宇宙")  # 在列表第二个位置插入新元素
print(name_list)

# 2.2.3列表中删除元素
# 2.2.3.1使用del语句删除元素，可删除任意位置的元素，只需要知道其索引即可
del name_list[2]  # 删除列表中第二个元素
print(name_list)

# 2.2.3.2使用pop()方法删除元素，可删除任意位置的元素，只需要知道其索引即可,但会返回被删除的元素
name_list_1 = name_list.pop()  # 未添索引值时，默认删除列表中最后一个元素,并返回值
name_list_2 = name_list.pop(1)  # 根据索引删除列表中第二个元素，并返回值
print(name_list_1, name_list_2)
print(name_list)

# 2.2.3.3使用remove()方法删除元素，根据所知的元素值来删除相应指定的元素，且不返回被删除的元素
# remove()方法只会删除第一个匹配到的元素，若列表中有多个相同的元素，则需要循环删除
name_list.remove("kkk")  # 删除列表中值为kkk的元素
print(name_list)

# 2.2.3.4使用clear()方法清空列表
name_list.clear()  # 清空列表
print(name_list)
