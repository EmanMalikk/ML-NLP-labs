from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize

porter = PorterStemmer()
lancaster = LancasterStemmer()

print(porter.stem("cats"))
print(porter.stem("used"))
print(porter.stem("buying"))
print(porter.stem("cars"))

print(lancaster.stem("cats"))
print(lancaster.stem("used"))
print(lancaster.stem("buying"))
print(lancaster.stem("cars"))

sentence = "i am using Python for writing programs"
print(porter.stem(sentence))

print(lancaster.stem(sentence))

sentence=" i used  writing programs in c++ but now i love coding in python programming language"

token_words = word_tokenize(sentence)
print(token_words)

stem_words = []
for word in token_words:
    stem_words.append(porter.stem(word))
    stem_words.append("")

print("".join(stem_words))    


