import pandas as pd

import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_long.csv")
#parse_dates=pd.read_json

air_quality = air_quality.rename(columns={"date.utc": "datetime"})

print(air_quality.head())

print(air_quality.city.unique())

air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

print(air_quality["datetime"])
#me=pd.read_csv("air_quality_long.csv", parse_dates=["datetime"])
#print(me)

print(air_quality["datetime"].min(), air_quality["datetime"].max())

print(air_quality["datetime"].max() - air_quality["datetime"].min())

air_quality["month"] = air_quality["datetime"].dt.month

print(air_quality.head())

us=air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"])["value"].mean()
print(us)

you=fig, axs = plt.subplots(figsize=(12, 4))

air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind='bar', rot=0, ax=axs
)
print(you)


plt.xlabel("Hour of the day");  # custom x label using Matplotlib

plt.ylabel("$NO_2 (µg/m^3)$")
plt.show()

no_2 = air_quality.pivot(index="datetime", columns="location", values="value")

#print(no_2.head())

#print(no_2.index.year, no_2.index.weekday)
#print(no_2["2019-05-20":"2019-05-21"].plot())

monthly_max = no_2.resample("M").max()

print(monthly_max)

print(monthly_max.index.freq)

print(no_2.resample("D").mean().plot(style="-o", figsize=(10, 5)))