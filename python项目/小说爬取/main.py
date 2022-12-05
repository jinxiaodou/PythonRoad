import search, writeFile
import sys, time, random

'''
使用biqusoso网站搜索小说

'''
def run():
    keyword=input('请输入书名:\n')
    result=search.NovelSearch(keyword)

    print('序号\t作品名称\t作者')
    for book in result.novel_list:
        print(book['num']+'\t'+book['name']+'\t'+book['author'])
    try:
        num=int(input('查到以上作品, 请输入序号:\n'))
    except:
        print('请输入数字编号')
    chapterObj=result.choose_novel(num-1)
    print('章节列表如下：')
    count=1
    length=len(chapterObj.chapter_list)
    for chapterm in chapterObj.chapter_list:
        print(str(count)+'\t'+chapterm['name'])
        count+=1
        if count >=20:
            print('...')
            print(str(length)+'\t'+chapterObj.chapter_list[length-1]['name'])
            break
    try:
        chapterId=int(input('请输入查看的章节编号,下载请按0:\n'))
    except:
        print('请输入数字编号')
    if chapterId==0:
        fromId=int(input('请输入下载起始章节,从头开始按0:\n'))
        for i in range(fromId,length):
            art=chapterObj.choose_chapter(i)
            writeFile.writeToFile(art.bookname,  art.chaptername+'\n\n\n'+art.article)
            progress=float((i+1-fromId)/(length-fromId))
            sys.stdout.write('已下载第%d章：%.2f%%' % (i+1,progress*100) + '\r')
            sys.stdout.flush()
            time.sleep(random.randint(0,100)/100.0)
        print('下载完成！')
    else:
        try:
            art=chapterObj.choose_chapter(chapterId-1)
            print(art.chaptername)
            print('')
            print('')
            print('')
            print(art.article)
        except:
            print('文章读取失败')

if __name__=='__main__':
    run()