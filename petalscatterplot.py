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

#From this plot we can see that the Iris-setosa has much smaller petal length & width compared to the other 2 species
#there is some crossover with the sizes of the Versicolor & virginica but it
#can be seen that for the most part the Virginica species has the largest petal of the three.
#Thus this information would be very useful in the identification of the three species