# coding: utf-8
from xml.dom import minidom

xdoc = minidom.parse("sample.xml")

#print xdoc.toxml()

elements = xdoc.getElementsByTagName("site")

node = elements[0]

childeNodes = node.childNodes

if node.nodeType in [node.TEXT_NODE, node.COMMENT_NODE]:
   print node.data


#print(elements)

#node = elements[0]

#

#attr = node.attributes["属性の名前"]

