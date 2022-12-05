import req, re
import article

class Chapter():
    def __init__(self, url):
        self.bookname=''
        self.author=''
        self.chapter_list=[]
        self.url=url
        self.get_novel()

    def get_novel(self):
        article_bs=req.send_request(self.url)
        self.get_bookname(article_bs)
        self.parse_chapter(article_bs)
        return self.chapter_list

    def parse_chapter(self, bs):
        list=bs.select('.book-chapter-list ul:nth-of-type(2) li')
        for item in list:
            name=item.select('a')[0].string
            href=item.select('a')[0]['href']
            try:
                if '第' in name and '章' in name:
                    pass
                else:
                    names=name.split(' ')
                    name='第'+names[0]+'章 '+names[1]
            except:
                print(name)
            chapter={'name': name, 'url': href}
            self.chapter_list.append(chapter)
    
    def get_httphost(self):
        searchObj=re.search(r'(.*)//([^/]+)/(.*)',self.url)
        if searchObj and searchObj.group(2):
            return searchObj.group(1)+'//'+searchObj.group(2)
        else:
            print ("请输入完整的URL!!")
            return None
	
    def get_bookname(self, bs):
        self.bookname=bs.select('.book-text>h1')[0].string
        author=bs.select('.book-text>span')[0].string
        self.author=re.split(' ', author)
    
    def choose_chapter(self, num):
        # try:
        obj=self.chapter_list[num]
        url=self.get_httphost()+obj['url']
        art=article.Article(url, self.bookname)
        return art
        # except:
        #     print('获取章节内容失败')
        #     return None

if __name__=='__main__':
    chapter=Chapter('https://www.qu-la.com/booktxt/99789798116/')
    print(chapter.bookname, chapter.author)
    # print(chapter.chapter_list)
    chapter.choose_chapter(2)
