# coding: utf-8
from xml.etree import ElementTree

XMLFILE = "store_review.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()
print root.tag  # feedと出力

#print root.attrib  # {'attrB': 'value B', 'attrA': 'value A'}

# 子タグの一括出力
"""
for e in root:
    print e.tag
"""

e = root.find('{http://www.w3.org/2005/Atom}id')
print e.text  # 内容を出力

e = root.find('{http://www.w3.org/2005/Atom}title')
print e.text  # title Cと出力

#updateタグの一括取得
es = root.findall('.//{http://www.w3.org/2005/Atom}updated')
for e in es:
    print e.tag, e.text

"""
es = root.findall('{http://www.w3.org/2005/Atom}entry')
for e in es:
    print e.tag
    f = root.find('./{http://www.w3.org/2005/Atom}entry/{http://www.w3.org/2005/Atom}updated')
    print f.tag, f.text
"""

es = root.findall(".//{http://www.w3.org/2005/Atom}content[@type='text']")
for e in es:
    print e.tag, e.text
    
#es = root.findall(".//category[@term='Asia']")
#for e in es:
#    print e.tag, e.attrib, e.text

#print "アサート"
    
#es = root.findall(".//feed/categories/category[1]")
#for e in es:
#    print e.tag, e.attrib, e.text

#/feed/entry[2]/title