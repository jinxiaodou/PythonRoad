#!usr/bin/python
#coding=utf-8

import csv

# 打开文件
with open('students.csv', 'a+') as file:
	# 创建writer对象
	writer=csv.writer(file)
	# 写入一行数据
	writer.writerow(['赵六','男',19])
	# 写入多行数据
	list=[
		['五六','女',22],
		['五七','男',23],
		['马走日','男',34]
	]
	writer.writerows(list)


# 读取文件
with open('students.csv', 'r') as file:
	reader=csv.reader(file)
	for row in reader:
		print(row)


import requests
import json

def parse_html():
	dic=json.load(open('jingdongComment.json',encoding='utf-8'))
	comments=dic['comments']
	list=[]
	for comment in comments:
		content=comment['content']
		createTime=comment['creationTime'].split(' ')[0]
		list.append([createTime, content])
	return list

def save_to_csv(data):
	with open('jingdongComment.csv','a+') as file:
		writer=csv.writer(file)
		writer.writerows(data)
	print('已保存到文件jingdongComment.csv')


def start():
	list=parse_html()
	save_to_csv(list)

start()