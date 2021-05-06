#The following plots the petal width versus sepal width in the three seperate species
#Out of curiousity plotted the widths of the petals vs width of the sepals
#Author: Carolyn Moorhouse

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

xpoint = iris["petalwidthcm"]
ypoint = iris["sepalwidthcm"]

for name, group in iris.groupby("species"):
    plt.scatter(xpoint[group.index], ypoint[group.index], label=name)

plt.title("Petal Width vs Sepal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Sepal Width (cm)")

plt.legend()
plt.show()
