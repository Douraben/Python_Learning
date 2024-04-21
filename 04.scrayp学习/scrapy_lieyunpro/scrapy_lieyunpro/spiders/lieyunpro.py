import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyLieyunproItem


class LieyunproSpider(CrawlSpider):
    # 定义爬虫名称
    name = "lieyunpro"
    # 定义允许爬取的域名
    allowed_domains = ["lieyunpro.com"]
    # 定义起始URL
    start_urls = ["https://lieyunpro.com/archives"]

    rules = (
        # 匹配 /archives/p123.html 这样的链接，并继续跟踪这个链接
        Rule(LinkExtractor(allow=r"/archives/p\d+.html"), follow=True),
        # 匹配 /archives/2012 这样的链接，并调用 parse_item 函数处理这个链接
        Rule(LinkExtractor(allow=r"/archives/\d+"), callback="parse_item", follow=False)
    )

    # 定义解析新闻列表页的方法
    def parse_item(self, response):
        # 获取标题
        title = response.xpath('//h1[@class="lyw-article-title-inner"]/text()')[1].getall()
        title = ''.join(title).split()
        # 获取作者名字
        author_name = response.xpath('//div[@class="main-text"]/p/strong/text()').get()
        # 获取发布时间
        date_time = response.xpath('//h1[@class="lyw-article-title-inner"]/span/text()').get()
        # 获取正文内容
        content = response.xpath('//div[@class ="main-text"]//text()').getall()
        content = ''.join(content).split()
        # 获取文章链接
        art_url = response.url

        item = ScrapyLieyunproItem()
        item["title"] = title
        item["author_name"] = author_name
        item["date_time"] = date_time
        item["content"] = content
        item["art_url"] = art_url

        yield item


