import scrapy


class BiqugespiderSpider(scrapy.Spider):
    name = "biqugespider"
    allowed_domains = ["www.biqg.cc"]
    start_urls = ["https://www.biqg.cc/book/3817/2.html"]

    def parse(self, response):
        # 提取标题
        title = response.xpath('//h1[@class="wap_none"]/text()').extract()
        # 提取内容
        content = response.xpath('string(//div[@id="chaptercontent"])').extract_first().strip().replace("　　",
                                                                                                        "\n").replace(
            "请收藏本站：https://www.biqg.cc。笔趣阁手机版：https://m.biqg.cc", "").replace("『点此报错』『加入书签』", "\n")
        next_url = "https://www.biqg.cc" + response.xpath(
            '//div[@class ="Readpage pagedown"]/a[3]/@href').extract_first()

        yield {
            "title": title,
            "content": content
        }

        # 请求下一页
        yield scrapy.Request(next_url, callback=self.parse)

