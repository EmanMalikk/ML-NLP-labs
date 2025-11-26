import pandas as pd
titanic = pd.read_csv("titanic.csv")

print(titanic.head())

ages = titanic["Age"]

print(ages.head())
type=type(titanic["Age"])
print(type)
 

type2 =titanic["Age"].shape
print(type2)

age_sex = titanic[["Age", "Sex"]]

print(age_sex.head())

#print(type(titanic[["Age", "Sex"]]))
print(titanic[["Age", "Sex"]].shape)

above_35 = titanic[titanic["Age"] > 35]

you=above_35.head()

print(you)

me=titanic["Age"] > 35
print(me)

print(above_35.shape)

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

print(class_23.head())

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]

print(class_23.head())

age_no_na = titanic[titanic["Age"].notna()]

print(age_no_na.head())

print(age_no_na.shape)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

print(adult_names.head())

print(titanic.iloc[9:25, 2:5])

titanic.iloc[0:3, 3] = "anonymous"

print(titanic.head())



