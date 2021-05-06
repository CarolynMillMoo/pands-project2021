#The following plots the petal length versus sepal length in the three seperate species
#Out of curiousity plotted the lengths of the petals vs length of the sepals
#Author: Carolyn Moorhouse

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

xpoint = iris["petallengthcm"]
ypoint = iris["sepallengthcm"]

for name, group in iris.groupby("species"):
    plt.scatter(xpoint[group.index], ypoint[group.index], label=name)

plt.title("Petal Length vs Sepal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Length (cm)")

plt.legend()
plt.show()
