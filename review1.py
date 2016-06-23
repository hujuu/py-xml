# coding: utf-8
# xmlファイルを読み込んで表示
 
from xml.dom import minidom
 
# sample.xmlファイルを読み込む
xdoc = minidom.parse("store_review.xml")
 
# 内容を文字列に変換して表示
print(xdoc.toxml())