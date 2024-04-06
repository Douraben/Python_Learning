# 3.1遍历整个列表（for循环）

list_name = ["apple", "banana", "cherry"]
for name in list_name:  # 通过for循环遍历列表中的每个元素
    print(name)
    print(name.title() + " \n")  # for循环中执行更多的操作

print("for循环后面，没有缩进给的代码都会执行一次，不会重复执行")
# 注意：for循环后面，没有缩进给的代码都会执行一次，不会重复执行


for i in range(len(list_name)):     # 通过for循环遍历列表中的每个元素,根据列表元素长度来循环次数
    print(list_name[i].upper())     # for循环中执行更多的操作
