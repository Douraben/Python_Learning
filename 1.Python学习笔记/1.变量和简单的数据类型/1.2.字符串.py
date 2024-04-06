# 2.字符串
message = " hello eric,would you like to learn python with me? "  # 定义名为message的字符串变量

print(message.title())  # 每个单词首字母大写

print(message.upper())  # 全部大写

print(message.lower())  # 全部小写

print(message.capitalize())  # 一行首字母大写

print(message.count("o"))  # 统计字符串中某个字符出现的次数

print(message.find("would"))  # 返回字符串中子字符串的第一个字符的索引值

print(message.replace("eric", "tom"))  # 替换字符串中的字符

print(message.split())  # 字符串分割
print(message.split(" "))  # 字符串分割

print(len(message))  # 字符串长度

print(message[1])  # 获取字符串中索引为1的字符

print(message.strip())  # 去除字符串两端的空格

print(message.lstrip())  # 去除字符串左端的空格

print(message.rstrip())  # 去除字符串右端的空格

# 单引号和双引号的嵌套使用方法
message_1 = "法律法规是指‘国家、政府、司法机关、行政机关、社会团体、企业等制定并发布的，具有强制性、约束力、规范性、指导性、法律效力，对公民、法人、社会团体、企业’等具有法律约束力的规范性文件。"
message_2 = '法律法规是指"国家、政府、司法机关、行政机关、社会团体、企业等制定并发布的，具有强制性、约束力、规范性、指导性、法律效力，对公民、法人、社会团体、企业"等具有法律约束力的规范性文件。'

print(f"字符串中使用变量的方法:\n\t{message_1}\n\t{message_2}")  # 格式化字符串，字符串中使用变量的方法

print(message_1.removeprefix("法律法规"))   # 去除字符串前后缀
