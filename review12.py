import xml.etree.ElementTree as etree    
tree = etree.parse('feed.xml')  
root = tree.getroot()                    
print root
print root.tag

len(root)

for child in root:
    print(child)
    
print root.attrib

print root[4]

print root[4].attrib

tree.findall('{http://www.w3.org/2005/Atom}entry')
entries = tree.findall('{http://www.w3.org/2005/Atom}entry')

print len(entries)

title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')

print title_element.text