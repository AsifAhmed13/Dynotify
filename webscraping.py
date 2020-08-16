import requests
import re
from bs4 import BeautifulSoup
product = input()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
product_name=product.lower()
product_name=re.sub("\s", "+",product_name)
URL = "http://www.amazon.com/s?k="+product_name
print(URL)
r = requests.get(URL,headers=headers)
soup = BeautifulSoup(r.content,'html5lib')
alls = []
for d in soup.findAll('div',attrs={'class':'a-section a-spacing-medium'}):
    n = d.find('div',attrs={'class':'a-section aok-relative s-image-square-aspect'})
    if n is not None:
        img = n.find_all('img',attrs={'class':'s-image'})
    title = d.find('span',attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    rating = d.find('span',attrs={'class':'a-icon-alt'})
    price = d.find('span',attrs={'class':'a-offscreen'})
    all1  = {}
    if n is not None:
        all1['image'] = img[0]['src']
    else:
        all1['image'] = "unknown-product"
    if(title is not None):
        all1['title'] = title.text
    else:
        all1['title'] = '0'
    if(rating is not None):
        all1['rating'] = rating.text
    else:
        all1['rating'] = '-1'
    if price is not None:
        all1['price'] = price.text
    else:
        all1['price'] = '0'
    alls.append(all1)
print(alls)
    
    

