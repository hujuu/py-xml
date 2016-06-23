# coding: utf-8
# タグの属性にアクセス
 
from xml.dom import minidom
 
# sample.xmlファイルを読み込む
xdoc = minidom.parse("sample.xml")
 
# recipe タグの0番目の要素を取得
recipe_element = xdoc.getElementsByTagName("site")[0]
 
# name 属性を取得して表示
print(recipe_element)