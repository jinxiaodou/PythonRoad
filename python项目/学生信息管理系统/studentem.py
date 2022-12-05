import os

FILE_NAME='students.txt'
menumsg='''
====================学生信息管理系统====================
-----------------------功能菜单------------------------
    1.录入学生信息
    2.查找学生信息
    3.删除学生信息
    4.修改学生信息
    5.排序
    6.统计学生总人数
    7.显示所有学生信息
    0.退出系统
------------------------------------------------------
'''

def main():
    while True:
        try:
            menuId=int(menus())
        except:
            print('菜单选择错误')
            continue
        if menuId in [0,1,2,3,4,5,6,7]:
            if menuId==0:
                print('感谢您的使用，再见！')
                break
            elif menuId==1:
                insert()
            elif menuId==2:
                search()
            elif menuId==3:
                delete()
            elif menuId==4:
                modify()
            elif menuId==5:
                sort()
            elif menuId==6:
                total_count()
            elif menuId==7:
                show()
        else:
            print('菜单选择错误')
            continue

def menus():
    print(menumsg)
    menuId=input('请选择：')
    return menuId

def insert():
    student_list=[]
    while True:
        try:
            sid=int(input('请输入学生ID:'))
        except:
            print('学生ID必须为数字int')
            continue
        sname=input('请输入学生姓名:')
        if sname=='':
            print('未输入姓名')
            continue
        try:
            senglish_score=int(input('请输入学生英语成绩:'))
            schinese_score=int(input('请输入学生语文成绩:'))
            smath_score=int(input('请输入学生数学成绩:'))
        except:
            print('成绩必须为数字int')
            continue
        total_score=senglish_score+schinese_score+smath_score
        student={'id': sid, 'name': sname, 'english': senglish_score, 'chinese': schinese_score, 'math': smath_score, 'total': total_score}
        student_list.append(student)
        save(student_list)
        print('学生信息录入成功!')
        student_list=[]
        next=input('是否继续添加y/n：')
        if next!='y' and next!='Y':
            break

def save(list):
    try:
        file=open(FILE_NAME, 'a', encoding='utf-8')
    except:
        file=open(FILE_NAME, 'w', encoding='utf-8')
    for item in list:
        file.write(str(item)+'\n')
    file.close()

def search():
    while True:
        sortmethod=input('按ID查询请输入1，按姓名查询请输入2：')
        if sortmethod=='1':
            msg='请输入学生ID：'
        elif sortmethod=='2':
            msg='请输入学生姓名：'
        else:
            print('查询方式输入错误!')
            continue
        keyword=input(msg)
        checkFile()
        with open(FILE_NAME, 'r') as file:
            list=file.readlines()
            for student in list:
                s=dict(eval(student))
                if sortmethod=='1':
                    if str(s['id'])==keyword:
                        print('ID\t姓名\t英语\t语文\t数学\t总分')
                        print(show_student(student))
                        break
                else:
                    if s['name']==keyword:
                        print('ID\t姓名\t英语\t语文\t数学\t总分')
                        print(show_student(student))
                        break
            else:
                print('未找到该学生')
        next=input('是否继续查询？y/n：')
        if next!='y' and next!='Y':
            break

def delete():
    while True:
        try:
            deleteID=int(input('请输入被删除学生的ID：'))
        except:
            print('输入ID格式错误')
            continue
        if deleteID != '':
            checkFile()
            with open(FILE_NAME, 'r+', encoding='utf-8') as file:
                list=file.readlines()
                for student in list:
                    s=dict(eval(student))
                    if s['id']==deleteID:
                        print('ID为'+str(deleteID)+'的学生已删除！')
                        list.remove(student)
                        break
                else:
                    print('未找到ID为'+str(deleteID)+'学生！')
                file.seek(0)            # 将指针移到开头
                file.truncate()         # 从文章size处开始进行截断，无size表示从当前位置截断，截断后的内容将被删除
                file.writelines(list)
            show()
        else:
            print('删除ID输入为空')
        next=input('是否继续删除？y/n：')
        if next!='y' and next!='Y':
            break

def modify():
    while True:
        show()
        modifyID=input('请输入需要修改学生的ID：')
        checkFile()
        with open(FILE_NAME, 'r+') as file:
            list=file.readlines()
            count=0
            for student in list:
                s=dict(eval(student))
                if str(s['id'])==modifyID:
                    print('找到ID为'+modifyID+'的学生，可以修改他的相关信息了！')
                    try:
                        sid=int(input('请输入学生ID:'))
                    except:
                        print('学生ID必须为数字int')
                        break
                    sname=input('请输入学生姓名:')
                    if sname=='':
                        print('未输入姓名')
                        break
                    try:
                        senglish_score=int(input('请输入学生英语成绩:'))
                        schinese_score=int(input('请输入学生语文成绩:'))
                        smath_score=int(input('请输入学生数学成绩:'))
                    except:
                        print('成绩必须为数字int')
                        break
                    
                    total_score=senglish_score+schinese_score+smath_score
                    student={'id': sid, 'name': sname, 'english': senglish_score, 'chinese': schinese_score, 'math': smath_score, 'total': total_score}
                    list[count]=str(student)
                    break
                count+=1
            else:
                print('未找到该学生！')
            file.seek(0)            # 将指针移到开头
            file.truncate()         # 从文章size处开始进行截断，无size表示从当前位置截断，截断后的内容将被删除
            file.writelines(list)
            file.flush()            # 立即将缓冲区内容写入文件
            show()
        next=input('是否继续修改？y/n：')
        if next!='y' and next!='Y':
            break

def sort():
    while True:
        sortby=input('学号排序请按1，英语排序请按2，语文排序请按3，数学排序请按4，总分排序请按5：')
        sort_key='id'
        if sortby=='1':
            sort_key='id'
        elif sortby=='2':
            sort_key='english'
        elif sortby=='3':
            sort_key='chinese'
        elif sortby=='4':
            sort_key='math'
        elif sortby=='5':
            sort_key='total'
        else:
            print('排序方式输入错误!')
            continue
        sorttype=input('升序请按1，降序请按2：')
        if sorttype not in ['1', '2']:
            print('升降序输入错误!')
            continue
        checkFile()
        with open(FILE_NAME, 'r') as file:
            list=file.readlines()
            i=0
            for item in list:
                student=dict(eval(item))
                minsortnum=int(student[sort_key])
                j=i+1
                for j in range(i+1,len(list)):
                    aitem=list[j]
                    astudent=dict(eval(aitem))
                    asortnum=int(astudent[sort_key])
                    if asortnum < minsortnum:
                        minsortnum=asortnum
                        tmp=list[i]
                        list[i]=aitem
                        list[j]=tmp
                    j+=1
                i+=1
            
            if sorttype=='2':
                list.reverse()
            print('ID\t姓名\t英语\t语文\t数学\t总分')
            for item in list:
                print(show_student(item))
        next=input('是否继续排序？y/n：')
        if next!='y' and next!='Y':
            break

def total_count():
    with open(FILE_NAME, 'r') as file:
        data=file.readlines()
        print('学生总人数为：'+str(len(data)))

def show():
    checkFile()
    with open(FILE_NAME, 'r') as file:
        data=file.readlines()
        if len(data)==0:
            print('暂无数据！')
            return
        print('ID\t姓名\t英语\t语文\t数学\t总分')
        for item in data:
            print(show_student(item))

def checkFile():
    if not os.path.exists(FILE_NAME) or not os.path.isfile(FILE_NAME):
        file=open(FILE_NAME, 'w', encoding='utf-8')

def show_student(s):
    stu=dict(eval(s))
    student_info=''
    key_list=list(stu.keys())
    count=0
    for keys in key_list:
        student_info+=str(stu[keys])
        count+=1
        if count!=len(key_list):
            student_info+='\t'
    return student_info

main()

# 打包使用PYInstaller 需要pip安装，使用命令PYInstaller -F xxx.py 记得注意PYInstaller大小写，否则会报错
# -F 打包单个文件，产生单个的可执行文件
# -D 打包多个文件，产生一个目录（包含多个文件）作为可执行程序
# -w 指定程序运行时不显示命令行窗口（仅对 Windows 有效）
