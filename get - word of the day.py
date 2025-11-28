"""
Gets the random word of the day and its definition from the Wordsmith RSS feed
"""
import re

import feedparser


def remove_img_tags(data):
    """
    Remove img tags from the data
    """
    pattern = re.compile(r'<img.*?/>')
    return pattern.sub('', data)


URL = "https://wordsmith.org/awad/rss1.xml"
entries = feedparser.parse(URL)["entries"][:1]
for entry in entries:
    title = remove_img_tags(entry['title'])
    output_desc = remove_img_tags(entry['description'])
    output = output_desc.replace("<p>", "").replace("</p>", "")
    print(f"{title}; {output}")
