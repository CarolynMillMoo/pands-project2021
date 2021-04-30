#This program will be used to analyse the
#Iris Dataset
#Author: Carolyn Moorhouse

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("iris.csv")

#Species count: counting the instance of each species
#in the iris.txt file
data["species"].value_counts()
print(data["species"].value_counts())

sum_sepallength = data["sepallengthcm"].sum()
mean_sepallength = data["sepallengthcm"].mean()
median_sepallength = data["sepallengthcm"].median()

with open("iris.txt", "w") as f:
    data = f.write('Sepal Length Sum(cm):'+str(sum_sepallength))
    print(data)

print("Sepal Length Sum(cm):",sum_sepallength, "\nMean Sepal Length(cm):", mean_sepallength, "\nMedian Sepal Length(cm):", median_sepallength)





