from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 페이지에서 발견된 내부 링크를 모두 목록으로 만듭니다.
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # /로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    targetUrl = splitAddress(startingPage)[0]
    externalLinks = getExternalLinks(bsObj, targetUrl)
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, targetUrl)
        return externalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

# 사이트에서 찾은 외부 URL을 모두 리스트로 수집
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj,splitAddress(domain)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(domain)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link == "/":
            link = domain
        elif link[0:2] == "//":
            link = "http:" + link
        elif link[0:1] == "/":
            link = domain + link
        if link not in allIntLinks:
            print("About to get link: "+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

domain = "http://journalism.semyung.ac.kr/vishome"
getAllExternalLinks(domain)

# followExternalOnly("http://journalism.semyung.ac.kr/vishome/")
# html = urlopen("http://journalism.semyung.ac.kr/vishome/")
# bsObj = BeautifulSoup(html, "html.parser")
# targetUrl = splitAddress("http://journalism.semyung.ac.kr/vishome/")[0]
# print(targetUrl, getInternalLinks(bsObj, targetUrl))




# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print("This page is missing something! No worries though!")
#     for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 print("--------------\n"+newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks("")


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
# random.seed(datetime.datetime.now())
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)


# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")

# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
# # for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)[^:.]*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

