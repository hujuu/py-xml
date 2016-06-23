# coding: utf-8
# タグの中身のテキストにアクセス
 
from xml.dom import minidom
 
# sample.xmlファイルを読み込む
xdoc = minidom.parse("sample.xml")
 
# recipe タグの0番目の要素を取得
recipe_element = xdoc.getElementsByTagName("site")[0]
 
# データを表示
print(recipe_element.childNodes[0].data)
 
# データを変更
recipe_element.childNodes[0].data = "基本的ではないパン"
 
# データを再表示
print(recipe_element.childNodes[0].data)