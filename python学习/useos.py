import os

os.system('notepad.exe') # 打开记事本
os.system('calc.exe')   # 打开计算器
# os.startfile('C:\\Program Files\\Tencent\\QQ\\bin\\qq.exe') #\转义，运行可执行文件 该方法仅支持windows

print(os.getcwd())  # 获取当前的工作目录
lst=os.listdir('test')  # 返回指定路径下的文件和目录信息
print(lst)
path='newdir'
# os.mkdir(path)      # 创建目录
# paths='test1/test2'
# os.makedirs(paths)   # 创建多级目录
# os.rmdir(path)      # 删除目录
# os.removedirs(paths) # 删除多级目录
# os.chdir(path)      # 将path设置为当前工作目录
# print(os.getcwd())

from os import path as ospath

current_path=os.getcwd()
ospath.abspath(current_path)                            # 获取文件或目录的绝对路径
isExist=ospath.exists(current_path)                     # 判断文件或目录是否存在，返回Bool值
print(isExist)
name='中庸之道.txt'
newpath=ospath.join(current_path,name)                  # 将目录与目录或者文件名拼接起来
names=ospath.splitext(name)                             # 分离文件名和扩展名
print(names)
basename=ospath.basename(newpath)                       # 从路径中提取文件名
print(basename)
somepath=ospath.dirname(newpath)                        # 从路径中提取文件路径，不包括文件名
isdir=ospath.isdir(somepath)                            # 是否为路径
print(somepath+' 是路径吗：'+str(isdir))
isdir1=ospath.isdir(newpath)                            # 是否为路径
print(newpath+' 是路径吗：'+str(isdir1))
