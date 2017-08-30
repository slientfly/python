# -*- coding:utf-8 -*-
import urllib2
def load_page(url):
	user_agent="Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0;"
	headers={"User-Agent":user_agent}
	req=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(req)
	html=response.read()
	return html
	
def write_to_file(new_file,txt):
	print "正在存储文件"+new_file
	f=open(new_file,'w')
	f.write(txt)
	f.close()

def neihan_spider(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		x=i
		my_url=url+str(x)+".html"
		html=load_page(my_url)
		new_file=str(x)+".html"
		write_to_file(new_file,html)
		

if __name__=="__main__":
	url=raw_input("请输入url")
	begin_page=int(raw_input("请输入起始页码"))
	end_page=int(raw_input("请输入终止页码"))
	neihan_spider(url,begin_page,end_page)
