import req, sys, re

class Article():
    def __init__(self, url, bookname):
        self.url=url
        self.bookname=bookname
        self.chaptername=''
        self.article=''
        self.get_article()

    def get_article(self):
        article_bs=req.send_request(self.url)
        self.parse_article(article_bs)

    def parse_article(self, bs):
        try:
            t=bs.select('#txt')[0].contents
            str=''
            for i in t:
                if i.name!='a':
                    if i.name=='br':
                        str+='\n'
                    else:
                        str+=i.string
        except:
            print('解析出错') 
    
        self.chaptername=bs.select('#chapter-title h1')[0].string
        try:
            if '第' in self.chaptername and '章' in self.chaptername:
                pass
            else:
                names=self.chaptername.split(' ')
                print(names)
                self.chaptername='第'+names[0]+'章 '+names[1]
        except:
            print(self.chaptername)
        self.article=str
        
    
if __name__=='__main__':
    article=Article('https://www.qu-la.com/booktxt/99789798116/413043721116.html')
    print(article.chaptername)
    print(article.article)
