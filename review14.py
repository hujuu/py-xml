import lxml.etree
tree = lxml.etree.parse('feed.xml')
NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}                    
entries = tree.xpath("//atom:category[@term='accessibility']/..",namespaces=NSMAP)
print entries                                                        
entry = entries[0]
entry.xpath('./atom:title/text()', namespaces=NSMAP)