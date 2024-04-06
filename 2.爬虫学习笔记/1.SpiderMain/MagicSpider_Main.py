# @Code name：Magic Spider(魔幻蜘蛛)V0.1
# @File: MagicSpider_Main.py
# @Purpose: Crawler learning
# @Author：la_ben
# @Time：2024.04.01
# @software：PyCharm

import sqlite3
import re
import requests
import xlwt
from bs4 import BeautifulSoup
import sys
import time

# 定义浏览器-请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36 Edg/123.0.0.0"
}

html_www = "https://www.meijui.net"


# 0.分析robots规则是否允许爬取
def rules_robots(url):
    """
    通过Robots规则分析是否允许爬取
    :return: 返回允许爬取的URL，允许返回True，不允许返回False
    """
    try:
        # 发送GET请求，获取robots.txt文件
        response = requests.get(url + "/robots.txt", headers=headers, timeout=5)
        # 使用正则表达式提取Allow和Disallow规则
        rules = re.findall(r'Allow:\s*(.*)|Disallow:\s*(.*)', response.text)
        print(rules)
        # 遍历规则，如果允许爬取，则返回True
        for Allow, Disallow in rules:
            if Allow:
                print(f"允许爬取{Allow}")
                return True
            else:
                print(f"不允许爬取{Disallow}")
                return False

    except requests.exceptions.RequestException as e:
        print(f"请求超时,原因：{e}")


# 1.获取数据
def get_web_data(url):
    """
    获取网页数据
    :param url: 网址
    :return: 返回网页数据
    """
    web_data = ""

    try:
        for url_number in range(1, 1246):  # 通过for循环网址页面添加到1246页
            url_info = url + str(url_number) + ".html"  # 已完成网址
            print(f"\t\t正在爬取第{url_number}页数据......{url_info}")
            # 发送get请求
            response = requests.get(url_info, headers=headers, timeout=5)
            # 返回请求结果
            web_data = web_data + response.text

        return web_data

    except requests.exceptions.RequestException as e:
        # 判断是否有状态码属性
        if hasattr(e, "code"):
            print(f"请求异常,状态码：{e.code}")

        # 判断是否有原因属性
        if hasattr(e, "reason"):
            print(f"请求异常,原因：{e.reason}")


# 2.数据解析--- find_all(),re.compile()
def parse_data(html):
    """
    解析网页数据
    :param html: 网页数据
    :return: 返回解析后的数据
    """
    try:
        data_list = []
        ps = BeautifulSoup(html, 'html.parser')  # 利用html解析器
        # 遍历所有符合条件的元素
        for itme in ps.find_all('article', class_="u-movie"):
            data_l = []
            # 影片名称
            find_name = re.compile(r'<a .*title="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
            # 影片地址
            find_link = re.compile(r'<a href="(.*?)".*>')
            # 影片图片
            find_mage = re.compile(r'<img .*data-original="(.*?)"', re.S)  # re,S 让换行符包含在字符中，忽视换行符
            # 影片评分
            find_score = re.compile(r'</a><div class="pingfen"><span>(.*?)分</span>')

            itme = str(itme)  # itme转换成字符串

            name = re.findall(find_name, itme)  # re库用来通过正则表达式查找指定的字符串
            data_l.append(name[0])  # 影片名称添加到data列表中

            link = re.findall(find_link, itme)
            data_l.append(html_www + link[0])  # 影片地址添加到data列表中

            mage = re.findall(find_mage, itme)
            data_l.append(html_www + mage[0])  # 影片图片添加到data列表中

            score = re.findall(find_score, itme)
            if score:  # 判断是否有评分，否侧结束本次循环，不在数据添加到data_list列表中
                data_l.append(score[0])  # 影片评分添加到data列表中
            else:
                continue

            data_list.append(data_l)
        return data_list

    except Exception as e:
        print(f"数据解析失败，原因：{e}")


# 数据保存到电子表格中
def xlsx_save_data(path, save_list):
    """
   数据保存到电子表格中
   :param path: 保存数据路径
   :param save_list: 要保存的数据列表
   :return: 返回数据保存情况
   """
    try:
        # 创建电子表格
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)
        sheet = book.add_sheet('Magic Spider(魔幻蜘蛛)V0.1')
        title = ("影片名称", "影片网址", "影片图片地址", "影片评分")
        # 写入数据
        for i in range(0, 4):
            sheet.write(0, i, title[i])
        for row in range(0, len(save_list)):
            # print(f"\t\t正在保存第{row}条数据......")
            for col in range(0, len(save_list[row])):
                sheet.write(row + 1, col, save_list[row][col])
            # 保存电子表格
        book.save(path)
        return "Xlsx数据保存成功！"

    except PermissionError as e:
        print(f"数据保存失败，原因：{e}")


def sqlite_save_data(save_data_list, path_db):
    """
    数据保存到数据库中
    :param save_data_list:
    :param path_db:
    :return:
    """
    sqlite_init(path_db)  # 调用初始化数据库函数
    sqlite_insert_data(save_data_list, path_db)  # 调用插入数据函数
    return "Sqlite数据库数据保存成功！"


def sqlite_init(path_db):
    """
    初始化数据库
    :param path_db:
    :return:
    """
    # 连接数据库
    conn = sqlite3.connect(path_db)
    # 获取游标
    cursor = conn.cursor()
    # 创建表格，如果不存在
    sql = """
    CREATE TABLE IF NOT EXISTS MagicSpider( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    link TEXT,
    mage TEXT,
    score INTEGER)
    """
    cursor.execute(sql)
    # 提交
    conn.commit()
    # 关闭
    conn.close()


def sqlite_insert_data(save_data_list, path_db):
    """
    插入数据到数据库
    :return:
    """
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    # 插入数据
    for data in save_data_list:
        # 插入数据
        sql = f"""
        INSERT INTO MagicSpider(name,link,mage,score)
        VALUES('{data[0]}','{html_www + data[1]}','{html_www + data[2]}','{data[3]}')
        """
        cursor.execute(sql)
        # 提交
        conn.commit()
        # 关闭
    conn.close()


def magic_spider_main():  # 定义主函数
    url_http = "https://www.meijui.net/list/1/page/"  # 美剧网网址
    save_path = "G:\pythonProject\PythonLearning\2.爬虫学习笔记\1.SpiderMain\DataBase/MagicSpider.xlsx"  # 保存路径
    save_path_db = "G:\pythonProject\PythonLearning\2.爬虫学习笔记\1.SpiderMain\DataBase/MagicSpider.db"

    print(f"Magic Spider(魔幻蜘蛛)V0.1\n\t\t开始对{url_http}网站进行爬取数据......\n")

    html = get_web_data(url_http)
    print(f"\t\t{url_http}获取网页数据成功")

    save_data_list = parse_data(html)
    print(f"\t\t{url_http}解析网页数据成功")

    xlsx_save = xlsx_save_data(save_path, save_data_list)
    print(f"\t\t{url_http}", xlsx_save)

    sqlite_save = sqlite_save_data(save_data_list, save_path_db)
    print(f"\t\t{url_http}", sqlite_save)

    print(
        f"Magic Spider(魔幻蜘蛛)V0.1爬取已完成！\n\t\t已获取数据以表格形式保存至：{save_path};"
        f"\n\t\t已获取数据以数据库形式保存至：{save_path_db}。\n")


if __name__ == "__main__":  # 开始执行

    magic_spider_main()  # 调用magic_spider_main()函数，开始执行程序#
