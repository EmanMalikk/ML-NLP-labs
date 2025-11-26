#language detection method 1
from googletrans import Translator
translate = Translator()
L = translate.detect ("she is a girl")
print(L)