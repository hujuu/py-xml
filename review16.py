# coding: utf-8

import feedparser

url = "https://itunes.apple.com/jp/rss/customerreviews/page=1/id=878506376/sortBy=mostRecent/xml"

response = feedparser.parse(url)
print response.namespaces

for entry in response.entries:
    title = entry.title
    updated = entry.updated
    content = entry.content[0].value

    print updated, title, content
