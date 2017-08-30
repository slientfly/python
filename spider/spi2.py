# -*- coding:utf-8 -*-
import urllib2
def load_page(url):
	#发送url请求，返回url请求的静态html页面
	user_agent="Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0;"
	headers={"User-Agent":user_agent}
	req=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(req)
	html=response.read()
	return html
def write_to_file(file_name,txt):
	print "正在存储文件"+file_name
	f=open(file_name, 'w')
	f.write(txt)
	f.close()


def tieba_spider(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
 		pn=50*(i-1)
		my_url=url+str(pn)
		#print my_url
		html=load_page(my_url)
		file_name=str(i)+".html"
		write_to_file(file_name,html)
		
if __name__=="__main__":
	url=raw_input("请输入贴吧的url地址")
	begin_page=int(raw_input("请输入起始页码"))
	end_page=int(raw_input("请输入终止页码"))
	#print begin_page
	#print end_page
	tieba_spider(url,begin_page,end_page) 
