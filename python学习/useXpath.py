#!/usr/bin/python
# coding=utf-8

import requests
from lxml import etree

# url='https://www.bqg99.com/book/1933/'
url='https://www.qidian.com/rank/yuepiao/'
headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# 发送请求
resp=requests.get(url, headers)
e=etree.HTML(resp.text) #str转换成class
# names=e.xpath('//div[@class="listmain"]/text()')
names=e.xpath('//div[@class="book-mid-info"]/h2/a/text()')
print(names)