import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")

print(titanic.head())
air_quality = pd.read_csv(
    "air_quality_long.csv", index_col="date.utc", parse_dates=True
)


print(air_quality.head())

print(titanic.sort_values(by="Age").head())

print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())

no2 = air_quality[air_quality["parameter"] == "no2"]
print(no2)

# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

print(no2_subset)

print(no2_subset.pivot(columns="location", values="value"))
print(no2.head())

print(no2.pivot(columns="location", values="value").plot())
plt.show()

new=air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
print(new)

new1=air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)
print(new1)

#print(air_quality.groupby(["parameter", "location"]).mean())

no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

print(no2_pivoted.head())
no_2 = no2_pivoted.melt(id_vars="date.utc")

print(no_2.head())

no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)


print(no_2.head())