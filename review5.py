# coding: utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
root = tree.getroot()

#print root.find(".//name").text
#print root.findtext(".//name")#これでも上と全く同じ結果になる
#print root.find(".//name").text

print root.find("./site/name").text

print root.find(".//content").text