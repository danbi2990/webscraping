
# lambda, regex, parent, siblings, child, children, tag's attribute

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")


"""
items = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for item in items:
    print(item)

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
"""
