# coding: utf-8
from xml.etree.ElementTree import *

tree = parse("sample2.xml") # 返値はElementTree型
elem = tree.getroot() # ルート要素を取得(Element型)

print elem.tag
# 条件にマッチする要素をリストで返す
for e in elem.findall(".//content"):
    print e.tag
    
# findtextを分けて書くと以下の通り
#print elem.find(".//name").text

for f in elem.findall(".//content"):
    print f.text

#node = elements[0]   
#xmlnode.attrib["type"]
