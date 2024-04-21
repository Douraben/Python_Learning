# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLieyunproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义item字段
    title = scrapy.Field()
    author_name = scrapy.Field()
    date_time = scrapy.Field()
    content = scrapy.Field()
    art_url = scrapy.Field()
