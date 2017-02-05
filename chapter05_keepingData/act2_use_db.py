from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='dnwls895', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")

def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute(
        "SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId))
    )
    if cur.rowcount == 0:
        cur.execute(
            "INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId))
        )
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            # 새 페이지를 만났으니 추가하고 링크를 검색합니다.
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel + 1)
        else:
            print("Skipping: "+str(link.attrs['href'])+" found on "+pageUrl)
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dnwls895', db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute("USE scraping")
#
# random.seed(datetime.datetime.now())
#
# def store(title, content):
#     cur.execute(
#         "INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",(title, content)
#     )
#     cur.connection.commit()
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     title = bsObj.find("h1").find("span").get_text()
#     content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
#     store(title, content)
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# try:
#     while len(links) > 0:
#         newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#         print(newArticle)
#         links = getLinks(newArticle)
# finally:
#     cur.close()
#     conn.close()


# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dnwls895',db='mysql')
# cur = conn.cursor()
# cur.execute("USE scraping")
# cur.execute("SELECT * FROM pages WHERE id=1")
# print(cur.fetchone())
# cur.close()
# conn.close()

