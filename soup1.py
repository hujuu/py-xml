from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null, break,あるいはプランBを実行
else:
    pass
    
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
print(bsObj.html.h1)
print(bsObj.body.h1)