import pandas as pd
titanic = pd.read_csv("titanic.csv")

print(titanic.head())
print(titanic["Name"].str.lower())
print(titanic["Name"].str.split(","))
us=titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)

titanic["Surname"]
print(us)

print(titanic["Name"].str.contains("Countess"))
print(titanic[titanic["Name"].str.contains("Countess")])
print(titanic["Name"].str.len())
print(titanic["Name"].str.len().idxmax())
print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})

print(titanic["Sex_short"])

we=titanic["Sex_short"] = titanic["Sex"].str.replace("female", "F")
print(we)
wee=titanic["Sex_short"] = titanic["Sex_short"].str.replace("male", "M")
print(wee)