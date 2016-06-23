# _*_ coding:UTF-8 _*_
import xml.dom.minidom

def walk(node):
    n = node.firstChild
    while n:
        if n.nodeType == xml.dom.Node.ELEMENT_NODE:
            print n.nodeName
            walk(n)
        elif n.nodeType == xml.dom.Node.TEXT_NODE and len(n.nodeValue.strip()) != 0:
            print n.nodeValue
        n = n.nextSibling
    
#doc = xml.dom.minidom.parse('sample.xml')
doc = xml.dom.minidom.parse('store_review.xml')
root = doc.documentElement
walk(root)