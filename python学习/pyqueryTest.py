#!usr/bin/python
#coding=utf-8

from pyquery import PyQuery as pq
html='''
<html>
<head>
</head>
	<title>pyquery测试</title>
<body>
	<h1>PYQuery</h1>
	<div id="main">
		主要内容
	</div>
</body>
</html>
'''

# 引入方式一 字符串方式
doc=pq(html)
print(doc)
print(type(doc))
print(type(html))
print(doc('title'))
print(doc('#main'))


# 引入方式二 url方式
# pq(url='https://www.baidu.com',encoding='utf-8')

# 引入方式三 文件方式
# pq(filename='demo.html')
