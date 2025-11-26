import nltk
file = open()
originalText = file.read()
print(originalText)

from nltk.corpus import stopwords
swords = stopwords.words("english")
print(swords)

words = [word for word in originalText.split() if word.lower() not in swords]
new_text = "".join (words)
print(new_text)