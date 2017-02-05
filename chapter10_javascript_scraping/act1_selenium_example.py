from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)

print(driver.find_element_by_id("content").text)
print(driver.find_element_by_css_selector("#content").text)
print(driver.find_element_by_tag_name("div").text)
print(driver.find_elements_by_css_selector("#content"))
print(driver.find_elements_by_tag_name("div"))

pageSource = driver.page_source
bsObj = bs(pageSource, 'html.parser')
print(bsObj.find(id="content").get_text())

driver.close()
