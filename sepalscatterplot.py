#The following plots the sepal length versus sepal width in the three seperate species
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

#from this plot we can see that the setosa species generally has the largest sepal width but sepal length is not the largest
#with the versicolor and virginica there is a greater crossover with the sepal width/length sizes
#so unlike the petal information this table would probably not be overly 
#helpful in the differentation between the versicolor and virginica species
#although it would likely help to identify between the setosa and the other two
#this may aid in identification along with other information