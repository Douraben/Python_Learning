# -*- coding: utf-8 -*-
import requests
import sqlite3
from bs4 import BeautifulSoup
import threading
import time

# 创建一个类来封装爬虫功能
class Magic_spider(threading.Thread):
    """
    MagicSpider类用于爬取指定网站的数据。
    """
    def __init__(self):
        """
        初始化MagicSpider类。
        """
        super().__init__()  # 先调用父类的__init__方法，然后将当前类的实例作为参数传递。

        self.url = f"https://bj.fang.lianjia.com/loupan/pg{0}/"  # 设置url
        # 设置请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}
        self.data_html = ""
        self.data_list = []

    def get_html_data(self, url):
        """
        获取HTML页面
        :return:
        """
        data_html = requests.get(url, headers=self.headers)
        # print(self.url)
        if data_html.status_code == 200:
            return data_html.text.encode('utf-8')

    def parse_html_data(self):
        """
        解析HTML页面，提取所需数据
        :return:
        """
        # 解析HTML页面，提取所需数据
        data_list = []
        # 使用BeautifulSoup解析html_page，解析器为html.parser
        parse_data = BeautifulSoup(self.data_html, "html.parser")
        # 查找ul标签，class为resblock-list-wrapper
        html_ul = parse_data.find("ul", class_="resblock-list-wrapper")
        # 查找所有li标签
        html_li_list = html_ul.find_all("li", class_="resblock-list post_ulog_exposure_scroll has-results")
        for itme in html_li_list:
            house_name = itme.find("a", class_="name").text.strip()
            house_type = itme.find("span", class_="resblock-type").text.strip()
            house_status = itme.find("span", class_="sale-status").text.strip()
            house_address = itme.find("div", class_="resblock-location")
            house_add = house_address.find("a").text.strip()
            house_price = itme.find("div", class_="main-price").text.strip().replace("\n\xa0", "")

            # 提取数据
            data_list.append((house_name, house_type, house_status, house_add, house_price))
        return data_list

    def save_data_sqlite(self):
        const = 0

        # 保存数据到SQLite数据库
        # 连接到SQLite数据库
        conn = sqlite3.connect("DataBase/magic_spider_v2.db")
        # 创建一个游标对象
        cursor = conn.cursor()
        # 创建一个表
        sql_create = '''CREATE TABLE IF NOT EXISTS house_data
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         house_name TEXT,
                         house_type TEXT,
                         house_status TEXT,
                         house_add TEXT,
                         house_price TEXT)'''

        cursor.execute(sql_create)
        # 插入数据
        sql_insert = '''INSERT INTO house_data
                            (house_name, house_type, house_status, house_add, house_price)
                            VALUES (?,?,?,?,?)'''
        for data in self.data_list:
            cursor.execute(sql_insert, data)

        # 提交事务
        conn.commit()
        # 关闭游标和连接
        cursor.close()
        conn.close()
        const += 1
        print(f"第{const}条数据写入数据库成功！")

    def magic_spider_start(self, i):
        """
        启动爬虫
        :return:
        """
        self.data_html = self.get_html_data(self.url.format(i))  # 调用获取HTML页面get_data_html（）方法
        self.data_list = self.parse_html_data()  # 调用解析HTML页面parse_html_data（）方法
        self.save_data_sqlite()  # 调用保存数据到SQLite数据库save_data_sqlite（）方法

    def run(self):  # 启动线程-----------------------------------------------------
        """
        启动线程
        :return:
        """
        i = 0
        while i < 26:  # 循环26次
            i += 1
            stat_1 = threading.Thread(target=self.magic_spider_start, kwargs={"i": i})  # 创建线程---1
            stat_1.start()  # 启动线程1

            i += 1
            stat_2 = threading.Thread(target=self.magic_spider_start, kwargs={"i": i})  # 创建线程---2
            stat_2.start()  # 启动线程2

            i += 1
            stat_3 = threading.Thread(target=self.magic_spider_start, kwargs={"i": i})  # 创建线程----3
            stat_3.start()  # 启动线程3

            # 等待所有线程完成


if __name__ == '__main__':
    magic_spider = Magic_spider()  # 创建MagicSpider对象
    magic_spider.run()  # 调用线程
