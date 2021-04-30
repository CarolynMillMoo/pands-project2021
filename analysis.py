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
with open("iris.txt", "w") as f:
    data = f.write("Instance of each species of iris: "+str(data["species"].value_counts()))

data = pd.read_csv("iris.csv")

sum_sepallength = data["sepallengthcm"].sum()
mean_sepallength = data["sepallengthcm"].mean()
median_sepallength = data["sepallengthcm"].median()

print("Sepal Length Sum(cm):",sum_sepallength, "\nMean Sepal Length(cm):", mean_sepallength, "\nMedian Sepal Length(cm):", median_sepallength)

with open("iris.txt", "a") as f:
    data = f.write('\nTotal Sepal Length all species Sum(cm):'+str(sum_sepallength))
    data = f.write('\nMean Sepal length all species (cm):'+str(mean_sepallength))
    data = f.write('\nMean Sepal length all species (cm): '+str(median_sepallength))







