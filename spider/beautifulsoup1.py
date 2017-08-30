import requests
import re
from bs4 import BeautifulSoup
res=requests.get('http://www.cabi.org/isc/search/?q=China&types=7&rows=10&sort=Relevance&facets=2&facet1f=Datasheet+Type&facet1v=Invasive+Species&facet2f=Geographical+Location&facet2v=China&page=1&s0=0&s1=0')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')


for page in soup.select('.Product_item'):
    h2=page.select('a')
    # print(h2)
    r=re.compile(r'<a href.*?</a>')
    s=r.findall(str(h2))
    n=re.compile(r'>.*?</a>')
    m=n.findall(str(s))
    z=m[0]
    w=z.replace('</a>','').replace('>','')
    print(w)

