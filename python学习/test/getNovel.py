#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
import requests
import os, sys,time,random
# from chardet import detect

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
		"Content-Type": "text/html; charset=gbk",
		"Cache-Control": "no-cache",
		"Connection": "keep-alive",
		"Cookie": "bcolor=; font=; size=; fontcolor=; width=; Hm_lvt_e2dd101e353595a4015e04ed5efb8326=1667984890,1668045151,1668132655,1668396388; Hm_lpvt_e2dd101e353595a4015e04ed5efb8326=1668413412",
		"Host": "www.lvsewx.com",
		"Pragma": "no-cache",
		"Referer": "https://www.lvsewx.com/ebook/36780.html"
		# sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
		# sec-ch-ua-mobile: ?0
		# sec-ch-ua-platform: "macOS"
		# Sec-Fetch-Dest: document
		# Sec-Fetch-Mode: navigate
		# Sec-Fetch-Site: same-origin
		# Sec-Fetch-User: ?1
		# Upgrade-Insecure-Requests: 1
	}
	resp=requests.get(url, headers=headers)
	resp.encoding='gbk'
	bs=BeautifulSoup(resp.text, 'lxml')
	return bs

# ????????????
def getBookName(bs):
	return bs.select('div.info>h2')[0].string

# ????????????
def parseChapter(bs):
	chapters=bs.select('div.listmain>dl>dd>a')
	return chapters[9:]

# ????????????
def parseArticle(bs):
	chapter=bs.select('div.content>h1')
	title=chapter[0].string.split('???')[0] #???????????????
	title='???'+title.split(' ')[0]+'??? '+title.split(' ')[-1]# ????????? ????????????????????????
	article=bs.select('div#content')
	articleStr=""
	for item in article[0].children:
		if item is not None and item.name != 'br' and item.name != 'script' and item.name != 'div':	#??????br
			articleStr+='\n'+item
	# print(articleStr)
	return title+'\n\n'+articleStr

# ????????????
def writeToFile(name,str):
	with open(sys.path[0]+'/'+name+'.txt', 'a', encoding='utf-8') as f:
		f.writelines(str)
		f.write('\n\n\n\n')

def run():
	# ????????????'
	mainUrl='https://www.lvsewx.com'
	bookUrl='/ebook/36780.html'
	beginId=3392

	mainBs=send_request(mainUrl+bookUrl)
	chapters=parseChapter(mainBs)
	bookName=getBookName(mainBs)
	print('??????'+str(beginId)+'??????????????????'+bookName+'???')
	for chapter in chapters[beginId:]:
		href=mainUrl+chapter['href']
		article=parseArticle(send_request(href))
		writeToFile(bookName,article)
		current=chapters.index(chapter)
		total=len(chapters)
		progress=float((current-beginId)/(total-beginId))
		sys.stdout.write('????????????%d??????%.2f%%' % (current,progress*100) + '\r')
		sys.stdout.flush()
		time.sleep(random.randint(0,10))
	print('????????????')



if __name__=='__main__':
	run()




