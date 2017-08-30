import requests
from bs4 import BeautifulSoup
res=requests.get('http://www.neihan8.com/article/')
res.encoding='utf-8'
#print (res.text)
soup=BeautifulSoup(res.text,'html.parser')

for new in soup.select('.text-column-item'):
    h1 = new.select('.title')[0].text
    a = new.select('.desc')[0].text

    print(h1)

    print(a)
