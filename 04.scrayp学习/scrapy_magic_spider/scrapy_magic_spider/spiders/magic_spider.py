import scrapy
from bs4 import BeautifulSoup
from ..items import ScrapyMagicSpiderItem


class MagicSpiderSpider(scrapy.Spider):
    """
    爬取豆瓣图书top250
    """
    name = 'magic_spider'
    allowed_domains = ['book.douban.com/top250']
    start_urls = ['https://book.douban.com/top250?start=0',
                  'https://book.douban.com/top250?start=25',
                  'https://book.douban.com/top250?start=50',
                  'https://book.douban.com/top250?start=75',
                  'https://book.douban.com/top250?start=100',
                  'https://book.douban.com/top250?start=125',
                  'https://book.douban.com/top250?start=150',
                  'https://book.douban.com/top250?start=175',
                  'https://book.douban.com/top250?start=200',
                  'https://book.douban.com/top250?start=225',
                  ]

    def parse(self, response):
        # 解析页面
        soup = BeautifulSoup(response.text, 'lxml')

        # 获取所有的tr标签
        itme_list = soup.find_all('tr', class_="item")

        for itme_data in itme_list:
            book_name = itme_data.find_all("a")[1]["title"]  # 获取书名
            book_author = itme_data.find("p", class_="pl").text  # 获取作者
            book_score = itme_data.find_all("span", class_="rating_nums")[0].text  # 获取评分
            # 获取评价人数
            book_appraise = itme_data.find("span", class_="pl").text.replace("(", "").replace(")", "").strip()

            # 创建ScrapyMagicSpiderItem的类对象
            item = ScrapyMagicSpiderItem()
            item["book_name"] = book_name
            # 将book_name添加到item_data字典中，键为book_name
            item["book_author"] = book_author
            # 将book_author添加到item_data字典中，键为book_author
            item["book_score"] = book_score
            # 将book_score添加到item_data字典中，键为book_score
            item["book_appraise"] = book_appraise
            # 将book_appraise添加到item_data字典中，键为book_appraise

            # 数据分装完毕之后提交引擎
            yield item
