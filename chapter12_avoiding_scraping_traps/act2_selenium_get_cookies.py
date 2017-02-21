from selenium import webdriver
from pprint import pprint

targetURL = "http://pythonscraping.com"

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
pprint(driver.get_cookies())

savedCookies = driver.get_cookies()
driver2 = webdriver.PhantomJS()
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
driver2.delete_all_cookies()

for cookie in savedCookies:
    # fix the 2nd problem
    for k in ('name', 'value', 'domain', 'path', 'expiry'):
        if k not in list(cookie.keys()):
            if k == 'expiry':
                cookie[k] = 1475825481
    # fix the 1st problem
    driver2.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})
print("----------------------------------------------------------")


driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
pprint(driver2.get_cookies())
