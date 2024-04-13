# 2.3列表管理
list_name: list = ["b", "a", "d", "c"]      # 显式指定类型，列表元素为字符串

# 2.3.1使用sort()方法对列表进行永久排序
list_name.sort()  # 默认情况下，sort()方法按升序排序列表元素
print(list_name)

# 也可以按与字母顺序相反的顺序排序列表元素
list_name.sort(reverse=True)  # reverse参数为True时，表示逆序
print(list_name)

# 数字列表的排序
list_number: list = [3, 1, 4, 5, 9, 2, 6, 5]
list_number.sort()  # 默认情况下，sort()方法按升序排序列表元素
print(list_number)
list_number.sort(reverse=True)  # 逆序排序,需要遇到reverse=True
print(list_number)

# 2.3.2使用sorted()函数对列表进行临时排序
# 注意：sorted()函数返回的是一个新的列表，而不会修改原列表
print(sorted(list_name))  # 默认情况下，sorted()函数按升序排序列表元素
print(sorted(list_name, reverse=True))  # 逆序排序,需要遇到reverse=True
print(sorted(list_number))
print(sorted(list_number, reverse=True))

# 2.3.3使用reverse()方法对列表进行永久反转
# 注意：reverse()方法永久会修改原列表元素排序，可以随时回复到原排序，再次使用reveres()方法
print(list_name)
list_name.reverse()  # 列表元素反转
print(list_name)

# 2.3.4使用len()函数获取列表长度
print(len(list_name))  # 列表长度
