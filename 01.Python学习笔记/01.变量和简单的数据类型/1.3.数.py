# 3.数 number

# 整数 integer
num_int = 12  # 默认是int类型
num_int_1: int = 14  # 显式指定类型#
nums = num_int + num_int_1
print(f"{num_int}+{num_int_1}={nums}")

# 浮点数 float
num_float = 2.5  # 默认是float类型
num_float_1: float = 3.3  # 显式指定类型
nums_1 = num_float * num_float_1
print(f"{num_float}*{num_float_1}={nums_1}")

# 数中的下划线
num_int_2 = 123_456_000  # 在书写很大的整数时，可以使用下划线来提高可读性，不会打印其中的下划线或不会影响运算
print(num_int_2)

# 同时多个变量赋值
a, b, c = 1, 2, 3       # 同时给三个变量赋值,只要变量数和变量值得个数相同，能准确地赋值
print(a, b, c)

# 常量 constant
# 常量是指在程序的整个生命周期内都保持不变的变量。
PI = 3.14   # 常量的变量名使用大写字母命名
print(PI)
