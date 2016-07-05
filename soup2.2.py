from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

#表題行を含む全ての行を印刷
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

#表題行（一列目）を除いた全ての製品行を印刷する
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

