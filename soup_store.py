from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen("https://itunes.apple.com/jp/rss/customerreviews/page=1/id=878506376/sortBy=mostRecent/xml")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("content", {"type":"text"})
for name in nameList:
    print(name.get_text())
    
nameList = bsObj.findAll("im:rating")
for name in nameList:
    print(name.get_text())
    
#nameList = bsObj.findAll(text = "the prince")
#print(len(nameList))