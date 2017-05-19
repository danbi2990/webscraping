from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string


def cleanInput(inputs):
    inputs = re.sub('\n+', " ", inputs)
    inputs = re.sub('\[[0-9]*\]', "", inputs)
    inputs = re.sub(' +', " ", inputs)
    inputs = bytes(inputs, "UTF-8")
    inputs = inputs.decode("ascii", "ignore")
    cleanInput = []
    inputs = inputs.split(' ')
    for item in inputs:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(inputs, n):
    inputs = cleanInput(inputs)
    output = {}
    for i in range(len(inputs)-n+1):
        tu = tuple(inputs[i:i+n])
        if output.get(tu) is None:
            output[tu] = 1
        else:
            output[tu] += 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
# ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
ngrams = sorted(ngrams.items(), key=lambda t: t[1], reverse=True)

print(ngrams)
print("2-grams count is: "+str(len(ngrams)))
