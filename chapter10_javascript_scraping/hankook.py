from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
from urllib.parse import quote

driver = webdriver.PhantomJS()
base = "http://hankookilbo.com/fd.aspx?q={}"
keyword = "김정남"
query = base.format(quote(keyword))
driver.get(query)

time.sleep(3)

html = driver.page_source
bs_obj = bs(html, 'html.parser')

tags = bs_obj.find_all("a", {"class": "gs-title"})

print(tags)
