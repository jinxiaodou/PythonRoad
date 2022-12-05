#!/usr/bin/python
# coding=utf-8

import urllib.parse
import urllib.request
import ssl

u = "http://www.baidu.com/s?ie=UTF-8&wd=%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A"
kw = {'wd': '新浪微博'}
#编码
res = urllib.parse.urlencode(kw)
print(res)

#解码
res1 = urllib.parse.unquote(res)

# ulopen(url,data=None,[timeout,]*,cafile=None, capath=None,cadefault=False,context=None)
# data 默认是None，None时为get请求，否则是post，
url = 'https://www.qidian.com/'
# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8') #decode将bytes类型转成str类型
# print(html)

# 以下地址已过期
# url1 = 'https://www.xslou.com/login.php'
# data = {'usernanem': '11', 'password': '', 'action': 'login'}
# response1 = urllib.request.urlopen(url1, data = bytes(urllib.parse.urlencode(data), encoding = 'utf-8'))
# html1 = response1.read().decode('gbk')
# print(html1)

# 创建请求对象

urlnew = 'https://www.121du.cc/13743/'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
req = urllib.request.Request(urlnew, headers = headers)
# response = urllib.request.urlopen(req)
# htmls = response.read().decode('utf-8')
# print(htmls)

# IP代理

# 免费代理:		https://www.xicidaili.com/nn/
# 大象代理 收费:	https://www.daxiangdaili.com/
# 快代理 收费:	https://www.kuaidaili.com/
# 可以建立自己的IP池 类似ProxyPool  https://github.com/jhao104/proxy_pool
# proxy = urllib.request.ProxyHandler({'https': '27.105.130.93:8080'})
# opener = urllib.request.build_opener(proxy)
# urlb = 'https://www.qidian.com/'
# resb = opener.open(urlb)
# htmlb = resb.read().decode('utf-8')
# print(htmlb)


# 使用cookie
# 案例，获取百度贴吧的cookie保存到本地

from http import cookiejar

filename = 'cookie.txt'

# 获取cookie
def get_cookies():
	# 实例化一个MozillaCookiejar 用于保存cookie
	cookie = cookiejar.MozillaCookieJar(filename)
	# 创建handler对象
	handler = urllib.request.HTTPCookieProcessor(cookie)
	# 创建opener对象
	opener = urllib.request.build_opener(handler)
	# 请求网址
	urlTieba = 'https://tieba.baidu.com'
	respTie = opener.open(urlTieba)
	# 保存cookie信息
	cookie.save()

# 读取cookie
def use_cookies():
	# 实例化一个MozillaCookiejar
	cookie = cookiejar.MozillaCookieJar()
	# 加载cookie文件
	cookie.load(filename)
	print(cookie)

if __name__ == '__main__':
	get_cookies()
	# use_cookies()

# 异常捕获
import urllib.error

# URLError 
urlerror = 'http://www.google.com'
try:
	resperror = urllib.request.urlopen(urlerror)
except urllib.error.URLError as e:
	print(e.reason)
else:
	pass
finally:
	pass

# HTTPError

# urlHError = 'https://movies.douban.com'
# try:
# 	respHE = urllib.request.urlopen(urlHError)
# except urllib.error.HTTPError as e:
# 	print('原因：' + e.reason)
# 	print('响应状态码：' + str(e.code))
# 	print('响应头数据：' + str(e.headers))
# else:
# 	pass
# finally:
# 	pass
