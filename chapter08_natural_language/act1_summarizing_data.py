from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


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
        ngramTemp = " ".join(inputs[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)
