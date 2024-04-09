# 7.1input()函数的工作原理

# 7.1.1编写清晰的提示
message = input("请输入您的信息：")
print(message, type(message))

# 7.1.2使用int()来获取数值输入

# input()函数默认输入为字符串，通过int()来转换成整数
number_d = int(input("请输入数字: "))
print(number_d)

# input()函数默认输入为字符串，通过float()来转换成浮点数
number_f = float(input("请输入数字: "))
print(number_f)

# 7.1.3 求模运算符
# 求模运算符（%）将两数相除并返回余数。

a = 148
b = 72
c = a % b
print(f"两数的相除后的余数为：{c}")

number_n = int(input("请输入整数，判断奇偶数："))
if number_n % 2 == 0:
    print(f"{number_n}为偶数")
else:
    print(f"{number_n}为奇数")
