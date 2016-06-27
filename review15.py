# coding: utf-8

import feedparser

url = "http://okuzawats.com/feed"

response = feedparser.parse(url)

print response.feed.title
print response.feed.link

for entry in response.entries:
    title = entry.title
    link  = entry.link
    updated = entry.updated
    print title,link,updated