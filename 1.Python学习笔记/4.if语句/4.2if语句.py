# 4.2if语句
name = ["aaa", "", "ccc"]

for n in range(len(name)):
    if name[n]:
        print(f"name列表元素{n}不为空")
    else:
        print(f"name列表元素{n}为空")
"""
对于数值0、空值None、单引号字符串''、双引号字符串""、空列表[]、空元组()、
空字典{}，以及任何其他“空”值，if语句中的条件表达式将会计算为false
"""

name_office = ["aaa", "bbb", "ccc", "ddd", "eee"]
# 遍历name_office列表中的每一个元素
for name_o in name_office:
    # 如果name_o元素在name列表中
    if name_o in name:
        # 打印出name_office列表元素在name列表中的信息
        print(f"name_office列表元素{name_o}在name列表中")
    # 如果name_o元素不在name列表中
    else:
        # 打印出name_office列表元素不在name列表中的信息
        print(f"name_office列表元素{name_o}不在name列表中")
