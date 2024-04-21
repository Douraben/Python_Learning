# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class ScrapyMagicSpiderPipeline:

    def __init__(self):
        # 创建一个新的Excel文件
        self.file_xlsx = openpyxl.Workbook()
        # 获取当前活动的工作表
        self.sheet = self.file_xlsx.active
        # 在工作表中添加表头
        self.sheet.append(['书名', '作者', '评分', '评价人数'])

    def process_item(self, item, spider):
        # 将获取到的数据添加到line列表中
        line = [item["book_name"],
                item["book_author"],
                item["book_score"],
                item["book_appraise"]]

        # 将line列表添加到sheet工作表中
        self.sheet.append(line)
        # 返回item
        return item

    def close_spider(self, spider):
        # 保存Excel文件
        self.file_xlsx.save('G:/book_file.xlsx')
        # 关闭Excel文件
        self.file_xlsx.close()
