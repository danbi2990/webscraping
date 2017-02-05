from nltk.book import text6
from nltk import FreqDist
fdist = FreqDist(text6)
fdist.most_common(10)
