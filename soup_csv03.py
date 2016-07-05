# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://itunes.apple.com/jp/rss/customerreviews/page=1/id=878506376/sortBy=mostRecent/xml")
bsObj = BeautifulSoup(html, "html.parser")

#ページの読み込み確認
print("ページ読み込み完了")

#主たる比較表はページの最初の表
rows = bsObj.findAll("entry")
    
csvFile = open("reviews.csv", 'wt', newline='', encoding = 'utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        
        for cell in row.findAll(['updated','title','im:rating']):
            csvRow.append(cell.get_text())
        
        nameList = row.findAll("content", {"type":"text"})
        for name in nameList:
            #print(name.get_text())
            csvRow.insert(3, name.get_text())
        
        writer.writerow(csvRow)

finally:
    csvFile.close()
    
    
#ページの読み込み確認
print("1ページ目の読み込み完了")