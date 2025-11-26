#method 1
import string
file = open()
originalText = file.read()
print = originalText
puncRemoved = originalText.translator(str.maketrans('','',string.punctuation))
print(puncRemoved)