# coding: utf-8
from xml.etree import ElementTree

XMLFILE = "sample3.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()
print root.tag  # feedと出力

print root.tag  # feed
print root.attrib  # {'attrB': 'value B', 'attrA': 'value A'}

for e in root:
    print e.tag  # title, categoriesと出力
    
e = root.find('title')
print e.tag  # titleと出力
print e.text  # title Cと出力

es = root.find('.//category')
print ">>テスト"
print es.tag  # titleと出力
print es.text  # title Cと出力

es = root.findall('.//category')
for e in es:
    print e.tag, e.attrib
    
es = root.findall(".//category[@term='Asia']")
for e in es:
    print e.tag, e.attrib, e.text

#print "アサート"
    
#es = root.findall(".//feed/categories/category[1]")
#for e in es:
#    print e.tag, e.attrib, e.text
