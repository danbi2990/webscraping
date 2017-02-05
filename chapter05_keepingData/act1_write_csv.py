
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# 비교 테이블은 현재 페이지의 첫 번째 테이블입니다.
table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("files/editors.csv",'wt',encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            print(cell.get_text())
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()



# import csv
#
# csvFile = open("files/test.csv", 'w+')
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10):
#         writer.writerow((i, i+2, i*2))
# finally:
#     csvFile.close()


# import os
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# downloadDirectory = "downloaded"
# baseUrl = "http://pythonscraping.com"
#
#
# def getAbsoluteURL(baseUrl, source):
#     if source.startswith("http://www."):
#         url = "http://" + source[11:]
#     elif source.startswith("http://"):
#         url = source
#     elif source.startswith("www."):
#         url = source[4:]
#         url = "http://" + source
#     else:
#         url = baseUrl + "/" + source
#     if baseUrl not in url:
#         return None
#     return url
#
#
# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
#     path = absoluteUrl.replace("www.", "")
#     path = path.replace(baseUrl, "")
#     path = downloadDirectory + path
#     directory = os.path.dirname(path)
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     return path
#
#
# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, "html.parser")
# downloadList = bsObj.findAll(src=True)
#
# for download in downloadList:
#     fileUrl = getAbsoluteURL(baseUrl, download["src"])
#     if fileUrl is not None:
#         print(fileUrl)
#
# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))


# imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
