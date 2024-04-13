# 3.4使用列表的一部分
list_name = ["name", "age", "gender", "address", "phone"]

# 3.4.1 切片（slice）

print(list_name[1:3])  # 切片索引1到2元素，不包括索引3

print(list_name[3:])  # 切片索引3到最后

print(list_name[:3])  # 切片索引0到2元素，不包括索引3

print(list_name[-3:-1])  # 切片索引-3到-1元素，不包括索引-1

print(list_name[-1:])  # 切片索引-1到最后

print(list_name[::2])   # 切片步长为2，索引0到结束元素


# 3.4.2遍历切片
for item in list_name[0:5:2]:
    print(item.title())


# 3.4.3 复制列表
list_name_copy = list_name[:]   # 通过切片复制列表

list_name.append("email")

print(f"复制前的原列表list_name：\n{list_name}")
print(f"复制后的新列表list_name_copy：\n{list_name_copy}")

list_name_copy_1 = list_name  # 直接赋值指向关联，不是复制
print(f"指向关联后列表list_name_copy：\n{list_name_copy_1}")
