from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
    
nameList = bsObj.findAll(text = "the prince")
print(len(nameList))


#allText = bsObj.findAll({"id":"title"},{"class":"text"})

#allText = bsObj.findAll(id="title", class="text")
#print(allText[0].get_text())