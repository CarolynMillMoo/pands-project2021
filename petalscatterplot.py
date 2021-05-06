#The following plots the sepal width versus sepal length in the three seperate species
#Author: Carolyn Moorhouse

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

ratio = iris["petallengthcm"]/iris["petalwidthcm"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()