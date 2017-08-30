# -*- coding:utf-8 -*-
import re
import urllib2

url='http://www.cabi.org/isc/search/?q=China&types=7&rows=10&sort=Relevance&facets=2&facet1f=Datasheet+Type&facet1v=Invasive+Species&facet2f=Geographical+Location&facet2v=China&page=10&s0=0&s1=40'
user_agent='Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0;'
headers={"User-Agent":user_agent}
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
html=response.read()
pattern=re.compile(r'<a href="/isc/datasheet/\d+" id="datasheet_\d+">.*?</a>')
new_html=pattern.findall(html)

def write(txt):
	f=open('frist.txt','a')
	f.write(txt)
	f.close
for x in new_html:
	new_pattern=re.compile(r'>.*?</a>')
	y=new_pattern.findall(str(x))
	w=y[0]
	r=w.replace('>',' ').replace('</a>',' ').replace('</a','')
	write(r)


