#The following plots the petal length versus petal width in the three seperate species
#Author: Carolyn Moorhouse

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

xpoint = iris["petallengthcm"]
ypoint = iris["petalwidthcm"]

for name, group in iris.groupby("species"):
    plt.scatter(xpoint[group.index], ypoint[group.index], label=name)

plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

plt.legend()
plt.show()