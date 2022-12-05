#!/usr/bin/python
# coding=utf-8

import requests

# 不带参数的get请求
urlbaidu = 'https://www.baidu.com'
resp = requests.get(urlbaidu)
resp.encoding = 'utf-8'
cookies = resp.cookies
headers = resp.headers
# print('响应返回值：' + resp.text)
print('请求的网址：' + resp.url)
print('响应状态码：' + str(resp.status_code))
# print('响应cookies：' + resp.cookies)	# cookie是对象，无法直接打印
# print('响应头：' + resp.headers)			# headers是对象，无法直接打印

# 带参数的get请求
# urlso = 'https://www.so.com/s'
# params = {'q': 'python'}
# respso = requests.get(urlso, params)
# respso.encoding = 'utf-8'
# print(respso.text)		# 打印数据太多

# 请求json
urljson = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9373300356864509384&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%8D%A1%E9%80%9A&queryWord=%E5%8D%A1%E9%80%9A&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e0000000000001e&1665976876423='
# params1 = {'tn': 'resultjson_com', 'word': '卡通'}
respJson = requests.get(urljson)
respJson.encoding = 'utf-8'
jsonData = respJson.json()
print(jsonData)


