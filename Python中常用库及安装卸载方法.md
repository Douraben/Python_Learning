Python�г��ÿ⼰��װж�ط���

==================================================================
һ��PYthon�ⰲװ������

pip install -i  requests

�廪��ѧ�ľ���Դ��ַ���ذ�װ(�ٶȿ죩��
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

==================================================================
����Python��ж�ط�����

  	pip uninstall requests

==================================================================
����Python�г��ÿ⣺

��һ����sqlite3 �� Python ��һ�����ÿ⣬������ SQLite ���ݿ���н�����SQLite ��һ�������������ݿ⣬�����������ݿ�洢��һ�������ļ��С�

import sqlite3 
conn = sqlite3.connect('example.db')

-------------------------------------------------------------------
��������re �� Python ��һ�����ÿ⣬���ڴ���������ʽ��������ʽ��һ������ƥ��ʹ����ַ�����ǿ�󷽷���

import re

-------------------------------------------------------------------
��������requests ��һ�� Python HTTP �⣬������������ HTTP ��������һ���ǳ����еĵ������⣬��������ץȡ��ҳ����ȡ���ݵȡ�

import  requests
response = requests.get('https://www.example.com')
content = response.content
print(content)

-------------------------------------------------------------------
���ģ���xlwt?��һ�� Python �⣬���ڴ�����д�� Excel �ļ��������Դ���һ���µ� Excel �ļ�����ӹ�����д�����ݵȡ�

import xlwt
workbook = xlwt.Workbook() # ѡ��������
worksheet = workbook.add_sheet('Sheet1') # д������ 		worksheet.write(0, 0, 'Hello')
worksheet.write(0, 1, 'World') # ���� Excel �ļ� 	workbook.save('example.xls')

-------------------------------------------------------------------
���壩��bs4?�� Python ��һ���������⣬ȫ���� BeautifulSoup�����ڽ��� HTML �� XML �ĵ��������԰����������ɵش���ҳ����ȡ��������ݡ�

from bs4 import BeautifulSoup
html = '<html><head><title>Example Page</title></head><body><p>This 
is an example page.</p></body></html>' 
soup = BeautifulSoup(html, 'html.parser')
title = soup.title
print(title)

��������sys

���ߣ���time

���ˣ���Kivy��װ
��򵥵ķ����ǰ�װ kivy-team �ṩ�� PyPi ���ӵĵ�ǰ�ȶ��汾

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple "kivy[base]" kivy_examples

Ҫ���ⰲװ֧����Ƶ/��Ƶ�� Kivy���밲װKivy �������kivy[base,media]kivy[full]
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple "kivy[media]"
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple " kivy[full]"








