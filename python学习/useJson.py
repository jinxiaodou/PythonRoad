#!usr/bin/python
#coding=utf-8

import json

# json.dumps() python类型转化为json字符串，返回string对象
# json.loads() 把json格式字符串转化成python对象
# json.dump() 将python内置类型序列化为json对象后写入文件
# json.load() 读取文件中json形式的字符串转化为python类型

# 字符串转对象
s='{"name": "张三"}'
obj=json.loads(s)
print(type(obj))
print(obj)

# 对象转字符串
ss=json.dumps(obj)
print(ss)

sss=json.dumps(obj, ensure_ascii=False)  # 可显示中文
print(sss)

# 对象保存在文件中
json.dump(obj, open('name.text','w',encoding='utf-8'), ensure_ascii=False)

names=json.load(open('name.text',encoding='utf-8'))
print(names)


import requests

def send_request(url):
	headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
	resp=requests.get(url,headers=headers)
	return resp.text

def parse_json(data):
	return data.replace('fetchJSON_comment98(','').replace(');','')

def type_change(data):
	return json.loads(data)

def save(data):
	json.dump(data,open('jingdongComment.json','w',encoding='utf-8'),ensure_ascii=False)
	print('已保存到文件jingdongComment.json')


def start():
	url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=43838886842&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
	data=send_request(url)
	s=parse_json(data)
	t=type_change(s)
	save(t)

start()


