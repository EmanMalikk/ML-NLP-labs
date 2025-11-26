import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.head())

print(titanic["Age"].mean())
print(titanic[["Age", "Fare"]].median())
print(titanic[["Age", "Fare"]].describe())

me=titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
print(me)

you=titanic[["Sex", "Age"]].groupby("Sex").mean()
print(you)

print(titanic.groupby("Sex").mean(numeric_only=True))

print(titanic.groupby("Sex")["Age"].mean())

print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())
print(titanic["Pclass"].value_counts())

print(titanic.groupby("Pclass")["Pclass"].count())
