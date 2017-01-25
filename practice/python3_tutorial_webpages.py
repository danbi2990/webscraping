from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.python-course.eu/python3_course.php")
bsObj = BeautifulSoup(html, "html.parser")
items = bsObj.findAll("a", {"href":re.compile("python3_")})

i = 0
for item in items:
    print(str(i) +" " + item.get_text())
    i += 1


