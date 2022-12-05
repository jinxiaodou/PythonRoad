#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup

html='''
<html>
	<head>
		<title>标题</title>
	</head>
	<body>
		<h1 class="class_f bg" style="float: left">起点中文网</h1>
		<h2> <!--注释的内容--> 标题2</h2>
		<div class="books" id="book1">书名一</div>
		<div class="books book2" id="book2">书名二 <span>作者2</span></div>
		<div class="books bg">
			书名三
			<span id="auth">作者</span>
		</div>
	</body>
</html>
'''
# bs=BeautifulSoup(html, 'html.parse')
bs=BeautifulSoup(html, 'lxml')
print(bs.title)
print(bs.h1.attrs)
print(bs.h1.get('class'))
print(bs.h1['class'])
print(bs.h1.text)
print('---',bs.h2.text)
print('=============================')

print(bs.find('div',class_='books'), type(bs.find('div',class_='books'))) #获取满足条件的首个内容
print(bs.find_all('div',class_='books')) #获取满足条件的所有内容
for item in bs.find_all('div',class_='books'):
	print(item, type(item))
print('============================')

print(bs.select('#book1'))
print(bs.select('.book2'))
print(bs.select('div.bg>span'))


