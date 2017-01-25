


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")

print(content)


# http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
# s = 'Flügel 字'
# print(s)
# print(b'prefix in Python 3.x')
# nonlat = '字'
# print(bytes(nonlat, 'utf-8'))
# print(nonlat)
# print(bytes(nonlat))    # error: string argument without an encoding
# print(b'\xff\xfeW['.decode('utf-8'))
# # error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
# print(b'\xff\xfeW['.decode('utf-16'))



# from urllib.request import urlopen
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textPage.read(), 'utf-8'))


# from urllib.request import urlopen
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textPage.read())
