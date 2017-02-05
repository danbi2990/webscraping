from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

def waitForLoad(driver):
    # elem = driver.find_element_by_tag_name("html")
    elem = driver.find_element_by_tag_name("div")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            print(elem == driver.find_element_by_tag_name("div"))
            # print(elem == driver.find_element_by_tag_name("body"))
            # print(driver.find_element_by_tag_name("div"))
        except NoSuchElementException:
            return

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
