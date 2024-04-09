# 7.2 while循环简介
# for循环用于针对集合中的每一个元素执行一个代码块，while循环则不断地运行，直到指定条件不再满足为止
# 避免无限循环 即可按Ctrl+C键终止循环

# 7.2.1 使用while循环

# n = 0
# while n < 10:
#     n += 1
#     print(n)


# 7.2.2 让用户选择何时推出
# quit_e = ""
# while quit_e != "exit":
#     quit_e = input("请输入退出命令:")
#     if quit_e != "exit":
#         print(f"{quit_e},命令输入有误，系统无法退出!")
#     else:
#         print("即将退出系统！")


# 7.2.3使用标志
# ture_b = True
# while ture_b:
#     quit_t = input("请输入退出命令:")
#     if quit_t != "exit":
#         print(f"{quit_t},命令输入有误，系统无法退出!")
#     else:
#         ture_b = False
#         print("即将退出系统！")


# 7.2.4 使用break退出循环

# 使用break退出整个循环体，不在执行循环
# while True:
#     quit_d = input("请输入退出命令:")
#     if quit_d == "exit":
#         print("即将退出系统！")
#         break
#     else:
#         print(f"{quit_d},命令输入有误，系统无法退出!")

# 7.2.5 在循环中使用continue
# 使用continue退出本次循环，跳转执行下一次循环

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        print(i)
        continue




