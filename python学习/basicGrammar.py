#!/usr/bin/python
# coding=utf-8

print('hello world')

"""
Python 保留字符
"""
import keyword
print(keyword.kwlist)

"""
行和缩进
"""
if True:
	print("True")
else:
	print("False")

"""
多行语句
Python语句中一般以新行作为语句的结束符。
但是我们可以使用斜杠（ \）将一行的语句分为多行显示
语句中包含 [], {} 或 () 括号就不需要使用多行连接符
"""
total = "今天" + \
		"天气" + \
		"很好！"
print(total)

"""
Python 引号
Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 \"\"\" ) 来表示字符串，引号的开始与结束必须是相同类型的。
其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
"""
word = 'word'
juzi = "这是一个句子"
duohang = """这是一个多行
语句
呢！"""
print(duohang)

"""
Python注释
python中单行注释采用 # 开头。
"""
'''
这是多行注释
'''
"""
这也是多行注释
"""
a = 100 #这是一个注释

"""
Python空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""

"""
等待用户输入
下面的程序执行后就会等待用户输入，按回车键后就会退出
"""
name = input("请输入姓名，按enter后退出...\n")
print("名字叫" + name)

"""
同一行显示多条语句
"""
import sys; x = 'runoob'; sys.stdout.write(x + "\n")

"""
python转义
	\n: 换行
	\t: 制表符
	\r: 覆盖
	\b: 删除
	\\: 两个反斜线代表一个\
"""
print("换行\n")
print("制表\t符")
print("这是\r覆盖模式")
print("这是\b删除")
print(r"大小写r使转义字符\n失效")

"""
python的空值 -- None 什么都没有
内置函数的返回值
"""

"""
字符串string
"""
#切片 [开始:结尾:步长] 取左不取右
name1 = "二营长你的意大利炮呢"
print(name1[0:3])
print(name1[-1])
print(name1[-3:-1])
print("步长：" + name1[0:6:2])

"""
字符串格式化 {} .format()
"""
s2 = "大家好，我叫{}，今年{}岁，性别{}".format("王劲松", "50", "男")
print(s2)
s3 = "大家好，我叫{1}，今年{0}岁，性别{2}".format("王劲松", "50", "男")
print(s3)

















