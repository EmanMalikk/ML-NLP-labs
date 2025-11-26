import pandas as pd

import matplotlib.pyplot as plt

air_quality = pd.read_csv("air.csv", index_col=0, parse_dates=True)

print(air_quality.head())

print(air_quality.plot())
plt.show()

print(air_quality["station_paris"].plot())
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

plt.show()

us=[
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]

print(us)

print(air_quality.plot.box())


plt.show()

#print(axs = air_quality.csv.plot.area(figsize=(12, 4), subplots=True))

plt.show()
#print(axs=plt.subplots(figsize=(12, 4)))

#air_quality.plot.area(ax=axs)


#axs.set_ylabel("NO$_2$ concentration")


#fig.savefig("no2_concentrations.png")

plt.show()

fig, axs = plt.subplots(figsize=(12, 4))        # Create an empty Matplotlib Figure and Axes
air_quality.plot.area(ax=axs)                   # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")          # Do any Matplotlib customization you like
fig.savefig("no2_concentrations.png")           # Save the Figure/Axes using the existing Matplotlib method.
plt.show()

