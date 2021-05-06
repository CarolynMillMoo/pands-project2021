#The following plots the sepal width versus sepal length in the three seperate species
#Author: Carolyn Moorhouse

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

xpoint = iris["sepallengthcm"]
ypoint = iris["sepalwidthcm"]

for name, group in iris.groupby("species"):
    plt.scatter(xpoint[group.index], ypoint[group.index], label=name)

plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.legend()
plt.show()