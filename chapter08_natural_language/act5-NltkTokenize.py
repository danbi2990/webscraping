from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print(text)

# from nltk.book import text1
# len(text6)/len(words)
