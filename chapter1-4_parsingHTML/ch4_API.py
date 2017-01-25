# Use APIs,

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # 개정 내역 페이지 URL은 다음과 같은 형식입니다.
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl += pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # 사용자명 대신 IP 주소가 담긴, 클래스가 mw-anonuserlink인 링크만 찾습니다.
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")


links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("--------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)



# import json
#
# jsonString = """{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],
#                 "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}"""
# jsonObj = json.loads(jsonString)
#
# print(jsonObj.get("arrayOfNums"))
# print(jsonObj.get("arrayOfNums")[1])
# print(jsonObj.get("arrayOfNums")[1].get("number")+jsonObj.get("arrayOfNums")[2].get("number"))
# print(jsonObj.get("arrayOfFruits")[2].get("fruit"))

# import json
# from urllib.request import urlopen
#
# def getCountry(ipAddress):
#     response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
#     responseJson = json.loads(response)
#     return responseJson.get("country_code")
#
# print(getCountry("50.78.253.58"))


# from urllib.request import urlopen
#
# url = "https://maps.googleapis.com/maps/api/geocode/json?address=1+Science+Park+Boston+MA+-2114&key=AIzaSyAK-Xisps1kzYxtjfoJIC0QCS1wvm21gR8"
# response = urlopen(url).read()
# print(response)
# https://maps.googleapis.com/maps/api/timezone/json?location=42.3677994,-71.0708078xtamp=1412649030&key=AIzaSyAK-Xisps1kzYxtjfoJIC0QCS1wvm21gR8
# https://maps.googleapis.com/maps/api/timezone/json?location=42.3677994,-71.0708078&timestamp=1412649030&key=AIzaSyAK-Xisps1kzYxtjfoJIC0QCS1wvm21gR8
# https://maps.googleapis.com/maps/api/eleation/json?locations=42.3677994,-71.0708078&key=AIzaSyAK-Xisps1kzYxtjfoJIC0QCS1wvm21gR8


# from twitter import *
#
# t = Twitter(auth=OAuth("547837599-DFpwWHyBddbNGi3TTYWSkWqXWWuTeAVxKjMEcElf",
#                        "Ft1Lfx1aA5QaBF9GaTxN5wTMeQSpNEHJXAAzWHQc3vvQG",
#                        "H8maKmrih4DV0nKQmr2gKk1WT",
#                        "y53frztKrXL815WgG0gKWT27OgZLB3KFrEsTWgij9VntH0Upna"))
# pythonTweets = t.search.tweets(q = "#python")
# print(pythonTweets)

# statusUpdate = t.statuses.update(status='Hello, world!')
# print(statusUpdate)

# pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
# print(pythonStatuses)
