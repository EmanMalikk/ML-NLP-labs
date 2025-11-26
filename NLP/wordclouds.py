import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df = pd.read_csv()

df.head()

df.category()

df.isna().sum()

text= "".join(cat.split()[1] for cat in df.category)

word_cloud = WordCloud(collocations =False,background_color = 'white').generate(text)
plt.imshow(word_cloud,interpolation='bilinear')
plt.axis("off")
plt.show()

