# 10.2 写入文件
from pathlib import Path

# 只能将字符写入文件中，如要数值数据存储文件中，必须str()函数转换成字符串格式
# 使用write_text()方法时，务必谨慎，如指定已存在将会删除其内容


# 10.2.1 写入一行------------------------------------------------
file_path = Path("file/file_w.txt")

file_path.write_text("你好 世界 ，文件写入成功！")

# 10.2.2 写入多行------------------------------------------------

name = "山西省\n"
name += "内蒙古自治区\n"
name += "辽宁省\n"
name += "吉林省\n"
name += "黑龙江省\n"
name += "上海市\n"
name += "浙江省\n"

file_path.write_text(name)  # 调用write_text()方法写入文件
file_path = Path("file/file_w.txt")
print(file_path.read_text())
