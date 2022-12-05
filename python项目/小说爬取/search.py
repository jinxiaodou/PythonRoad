import req, sys, re, chapter
from urllib.parse import urlencode

class NovelSearch():
	SEARCH_URL='https://so.biqusoso.com/s.php?ie=gbk&siteid=lvsewx.com&s=2758772450457967865&'

	def __init__(self, keyword):
		self.keyword=keyword
		self.novel_list=[]
		self.search()
	
	def get_novels(self, bs):
		list=bs.select('#search-main ul li')
		if len(list)==0:
			print('未查到该书籍')
			return []
		print('检索到'+str(len(list)-1)+'本书籍')
		count=0
		for novel in list:
			if count==0:
				count+=1
				continue
			line1=novel.select('.s1')[0].string
			bookname=novel.select('.s2 a')[0].string
			href=novel.select('.s2 a')[0]['href']
			author=novel.select('.s4')[0].string
			book={'num': line1, 'name': bookname, 'href': href, 'author': author}
			self.novel_list.append(book)
		
	def check_host(self, host):
		# 检测网站是否是已破解网站
		if 'www.qu-la.com'!=host:
			print('该网站暂未录入规则:'+host)
			return False
		return True

	def get_host(self, url):
		searchObj=re.search(r'(.*)//([^/]+)/(.*)',url)
		if searchObj and searchObj.group(2):
			return searchObj.group(2)
		else:
			print ("请输入完整的URL!!")
			return None
		
	def choose_novel(self, num):
		novel_href=self.novel_list[num]['href']
		if self.check_host(self.get_host(novel_href)):
			chapterObj=chapter.Chapter(novel_href)
			return chapterObj
		else:
			print('未能获取到书籍')
			return None
		
	def search(self):
		print('开始查询书籍:'+self.keyword)
		data=urlencode({'q': self.keyword}, encoding='gbk')
		search_url=NovelSearch.SEARCH_URL+data
		bs=req.send_request(search_url)
		self.get_novels(bs)
		

if __name__=='__main__':
	s=NovelSearch('三寸人间')
	print(s.novel_list)
	s.choose_novel(0)