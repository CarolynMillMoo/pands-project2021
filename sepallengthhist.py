#a program which plots a histogram of the salaries from topic 08 question1
#Author: Carolyn Moorhouse

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

sepallength = iris["sepallengthcm"]

for name, group in iris.groupby("species"):
    plt.hist(sepallength[group.index], group.index, label=name)

plt.title("Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.legend()
plt.show()
