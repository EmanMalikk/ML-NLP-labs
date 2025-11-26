#language detection method 2
from textblob import textblob
text = "she is a girl"
lang = textblob(text)
print(lang.detect_language())