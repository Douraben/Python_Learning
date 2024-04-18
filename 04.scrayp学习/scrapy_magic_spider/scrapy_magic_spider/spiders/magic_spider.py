import scrapy


class Magic_spider(scrapy.Spider):
    """
    爬虫类
    """
    # 爬虫名称
    name = "magic_spider"

    # 爬虫允许的域名
    allowed_domains = ["example.com"]

    # 爬取的起始URL列表
    start_urls = ["http://example.com"]

    # 解析函数
    def parse(self, response):

        print(response.text)


