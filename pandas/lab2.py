import pandas as pd
titanic = pd.read_csv("titanic.csv")
print(titanic)

print(titanic.head(8))
print(titanic.tail(8))
print((titanic.dtypes))
#print(titanic.to_excel("titanic.csv", sheet_name="passengers", index=False))
#print(titanic = pd.read_excel("titanic.csv", sheet_name="passengers"))
print(titanic.info())
