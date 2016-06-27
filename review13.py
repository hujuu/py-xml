from lxml import etree
tree = etree.parse('feed.xml')
root = tree.getroot()
root.findall('{http://www.w3.org/2005/Atom}entry')


es = root.findall('{http://www.w3.org/2005/Atom}entry')
for e in es:
    print e
