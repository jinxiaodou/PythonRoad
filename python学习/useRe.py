#!usr/bin/python
#coding=utf-8

import re

str=input('请输入字符：')
reEmail=re.match('^([\w-])+@([\w-])+(\.[\w-]+)+$', str)
print('邮箱匹配结果：')
print(reEmail)
reMobile1=re.match('^[1][\d]{10}$', str) #简易手机号规则
print('简易手机号匹配结果：')
print(reMobile1)
reMobile2=re.match('^[1][3-9]\d{9}$', str)
print('手机号匹配结果：')
print(reMobile2)
reChinese=re.match('[\u4e00-\u9fa5]+', str)
print('中文匹配结果：')
print(reChinese)
