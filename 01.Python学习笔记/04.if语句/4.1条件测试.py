# 4.1条件测试
# if语句 检查是否相等时区分大小写的，使用 == 和 !=

# 4.1.1 如何检查时是否相等时忽略大小写
# 不区分大小写的相等检查，将转换成全小写，再进行比较
name = "John"
if name.lower() == "john":  # 检查是否为全小写的 "john"
    print("Hello, John!")

# 4.1.2 如何检查多个条件
x = 10
y = 20
z = 0
name = ["aaa", "bbb", "ccc"]

# 4.1.2.1使用and 操作符，检查多个条件
# and 操作符，检查多个条件，只有所有条件都为真时，才会返回True，否则返回False
if x > 0 and y > 0:  # 通过and检查x和y是否都大于0
    print("均大于零")

# 4.1.2.2使用or 操作符，检查多个条件
if x >= 0 or z >= 0:  # 通过or检查x和y是否至少有一个大于0
    print("至少有一个大于零")

# 4.1.2.3使用in 操作符，检查特定的值是否在列表中
if "aaa" in name:  # 检查"aaa"是否在name列表中
    print("aaa在列表中")

# 4.1.2.3使用not 操作符，检查特定的值是否不在列表中
if "ddd" not in name:  # 检查"ddd"是否不在name列表中
    print("ddd不在列表中")

# 4.1.3 布尔表达式
if name:
    print("name列表不为空")
