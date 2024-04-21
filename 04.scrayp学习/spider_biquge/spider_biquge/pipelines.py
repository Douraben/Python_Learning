# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderBiqugePipeline:
    # 打开爬虫时执行，初始化文件
    def open_spider(self, spider):
        self.file_txt = open("G:/file_biquge.txt", "w", encoding="utf-8")

    # 处理爬取到的数据存储
    def process_item(self, item, spider):
        info = ''.join(item["title"]) + "\n\t\t" + item["content"]
        self.file_txt.write(info)
        return item

    # 关闭爬虫时执行，关闭文件
    def close_spider(self, spider):
        self.file_txt.close()
