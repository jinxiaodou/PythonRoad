from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode
import os, sys,time,random, re

USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
 	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
]


# ????????????
def send_request(url):
	headers={
		"User-Agent": random.choice(USER_AGENTS),
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"Referer":"https://www.lvsewx.com/"
	}
	resp=requests.get(url, headers=headers)
	bs=BeautifulSoup(resp.text, 'lxml')
	return bs

def choose_novel(bs):
	list=bs.select('#search-main ul li')
	if len(list)==0:
		print('??????????????????')
		sys.exit()
	del list[0]
	print('?????????'+str(len(list))+'??????????????????')
	count=0
	for novel in list:
		bookname=novel.select('.s2 a')[0].string
		author=novel.select('.s4')[0].string
		print(str(count)+' ???'+bookname+'??? ?????????'+author)
		count+=1
	print('???????????????')
	novel=list[0].select('.s2 a')
	print('???????????????:???'+novel[0].string+'???, ????????????')
	href=novel[0]['href']
	return href
	
def check_host(host):
	# ????????????????????????????????????
	if 'www.qu-la.com'==host:
		return True
	print('???????????????????????????:'+host)
	sys.exit()
	return False

def parse_article(bs):
	list=bs.select('.book-chapter-list ul:nth-of-type(2) li')
	print(list)

def get_host(url):
	searchObj=re.search(r'(.*)//([^/]+)/(.*)',url)
	if searchObj and searchObj.group(2):
		return searchObj.group(2)
	else:
		print ("??????????????????URL!!")
		return None
	
def search(keyword):
	print('??????????????????:'+keyword)
	data=urlencode({'q': keyword}, encoding='gbk')
	search_url='https://so.biqusoso.com/s.php?ie=gbk&siteid=lvsewx.com&s=2758772450457967865&'+data
	bs=send_request(search_url)
	novel_href=choose_novel(bs)
	check_host(get_host(novel_href))
	article_bs=send_request(novel_href)
	parse_article(article_bs)

if __name__=='__main__':
	keyword='????????????'
	search(keyword)












