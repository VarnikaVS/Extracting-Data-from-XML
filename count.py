import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_193786.xml"
print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counting =  tree.findall('.//count')
print("Count: " + str(len(counting)))

accumulator = 0

for count in counting:
    accumulator += int(count.text)

print("Sum:" + str(accumulator))
