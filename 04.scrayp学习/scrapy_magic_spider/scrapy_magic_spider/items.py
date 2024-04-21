# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义爬虫的数据结构类型
class ScrapyMagicSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()  # 书名
    book_author = scrapy.Field()  # 作者
    book_score = scrapy.Field()  # 评分
    book_appraise = scrapy.Field()  # 评价人数
