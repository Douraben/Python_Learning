import requests
import sqlite3
from bs4 import BeautifulSoup


class Magic_spider:
    """
    MagicSpider类用于爬取指定网站的数据。
    """

    def __init__(self):
        """
        初始化MagicSpider类。
        """
        self.url = "https://bj.fang.lianjia.com/loupan/pg{0}/"
        # self.keyword = keyword
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}
        # self.data_list = []

    def get_data_html(self, url):
        """
        获取HTML页面

        :return:
        """
        data_html = requests.get(url, headers=self.headers)
        print(url)
        if data_html.status_code == 200:
            return data_html.text.encode('utf-8')

    def parse_html_data(self, html_page):

        data_list = []
        # 使用BeautifulSoup解析html_page，解析器为html.parser
        parse_data = BeautifulSoup(html_page, "html.parser")
        # 查找ul标签，class为resblock-list-wrapper
        html_ul = parse_data.find("ul", class_="resblock-list-wrapper")
        # 查找所有li标签
        html_li_list = html_ul.find_all("li")
        for itme in html_li_list:
            house_name = itme.find("a", class_="name").text.strip()
            house_type = itme.find("span", class_="resblock-type").text.strip()
            house_status = itme.find("span", class_="sale-status").text.strip()
            house_address = itme.find("div", class_="resblock-location")
            house_add = house_address.find("a").text.strip()
            house_price = itme.find("div", class_="main-price").text.strip().replace("\n\xa0", "")
            # house_guwen = itme.find("span", class_="ke-agent-sj-name").text.strip()

            # 提取数据
            data_list.append((house_name, house_type, house_status, house_add, house_price))

        return data_list

        # 解析HTML页面，提取所需数据

    def save_data_sqlite(self, data_save):

        #  保存数据到SQLite数据库
        # 连接到SQLite数据库
        conn = sqlite3.connect("DataBase\magic_spider_v2.db")
        # 创建一个游标对象
        cursor = conn.cursor()
        # 创建一个表
        cursor.execute('''CREATE TABLE IF NOT EXISTS house_data
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         house_name TEXT,
                         house_type TEXT,
                         house_status TEXT,
                         house_add TEXT,
                         house_price TEXT)''')
        # 插入数据
        for data in data_save:
            cursor.execute('''INSERT INTO house_data
                            (house_name, house_type, house_status, house_add, house_price)
                            VALUES (?,?,?,?,?)''', data)
        # 提交事务
        conn.commit()
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return "数据保存成功"

    def magic_spider_start(self):
        for i in range(1, 28):
            html_url = self.url.format(i)
            data_html = self.get_data_html(html_url)
            data_list = self.parse_html_data(data_html)
            save_type = self.save_data_sqlite(data_list)
            print(save_type)


if __name__ == '__main__':
    magic_spider = Magic_spider()
    magic_spider.magic_spider_start()
