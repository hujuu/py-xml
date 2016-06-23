# coding: utf-8
from xml.etree import ElementTree

XMLFILE = "store_review1.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()
print root.tag  # feedと出力

#print root.attrib  # {'attrB': 'value B', 'attrA': 'value A'}

print 1

for e in root:
    print e.tag  # title, categoriesと出力
    
e = root.find('{http://www.w3.org/2005/Atom}id')
print e.tag  # titleと出力
print e.text  # title Cと出力

e = root.find('{http://www.w3.org/2005/Atom}title')
print e.tag  # titleと出力
print e.text  # title Cと出力

#es = root.findall('.//title')
#for e in es:
#    print e.tag, e.attrib  # 出力なし

#es = root.findall(".//category[@term='Asia']")
#for e in es:
#    print e.tag, e.attrib, e.text

#print "アサート"
    
#es = root.findall(".//feed/categories/category[1]")
#for e in es:
#    print e.tag, e.attrib, e.text

#/feed/entry[2]/title