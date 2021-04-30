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

#The following calculates the sum, mean and median of the sepal length for all species
#and also appends this info to the iris txt file
data = pd.read_csv("iris.csv")

sum_sepallength = data["sepallengthcm"].sum()
mean_sepallength = data["sepallengthcm"].mean()
median_sepallength = data["sepallengthcm"].median()

print("Sepal Length Sum(cm):",sum_sepallength, "\nMean Sepal Length(cm):", mean_sepallength, "\nMedian Sepal Length(cm):", median_sepallength)

with open("iris.txt", "a") as f:
    data = f.write('\nTotal Sepal Length all species Sum(cm):'+str(sum_sepallength))
    data = f.write('\nMean Sepal length all species (cm):'+str(mean_sepallength))
    data = f.write('\nMean Sepal length all species (cm): '+str(median_sepallength))

#the following calculate the sum, mean and median of the sepal width for all species
#and also appends this to the iris txt file
data = pd.read_csv("iris.csv")

sum_sepalwidth = data["sepalwidthcm"].sum()
mean_sepalwidth = data["sepalwidthcm"].mean()
median_sepalwidth = data["sepalwidthcm"].median()

print("Sepal Width Sum(cm):",sum_sepalwidth, "\nMean Sepal Width(cm):", mean_sepalwidth, "\nMedian Sepal width(cm):", median_sepalwidth)

with open("iris.txt", "a") as f:
    data = f.write('\nTotal Sepal width all species Sum(cm):'+str(sum_sepalwidth))
    data = f.write('\nMean Sepal width all species (cm):'+str(mean_sepalwidth))
    data = f.write('\nMean Sepal width all species (cm): '+str(median_sepalwidth))

#the following calculate the sum, mean and median of the petal length for all species
#and also appends this to the iris txt file
data = pd.read_csv("iris.csv")

sum_petallength = data["petallengthcm"].sum()
mean_petallength = data["petallengthcm"].mean()
median_petallength = data["petallengthcm"].median()

print("Petal Length Sum(cm):",sum_petallength, "\nMean Petal Length(cm):", mean_petallength, "\nMedian Petal Length(cm):", median_petallength)

with open("iris.txt", "a") as f:
    data = f.write('\nTotal Petal Length all species Sum(cm):'+str(sum_petallength))
    data = f.write('\nMean Petal Length all species (cm):'+str(mean_petallength))
    data = f.write('\nMean Petal Length all species (cm): '+str(median_petallength))

#the following calculate the sum, mean and median of the petal width for all species
#and also appends this to the iris txt file
data = pd.read_csv("iris.csv")

sum_petalwidth = data["petalwidthcm"].sum()
mean_petalwidth = data["petalwidthcm"].mean()
median_petalwidth = data["petalwidthcm"].median()

print("Petal Width Sum(cm):",sum_petalwidth, "\nMean Petal Width(cm):", mean_petalwidth, "\nMedian Petal width(cm):", median_petalwidth)

with open("iris.txt", "a") as f:
    data = f.write('\nTotal Petal width all species Sum(cm):'+str(sum_petalwidth))
    data = f.write('\nMean Petal width all species (cm):'+str(mean_petalwidth))
    data = f.write('\nMean Petal width all species (cm): '+str(median_petalwidth))

#the following calculate the sum, mean and median of the sepal width for all species
#and also appends this to the iris txt file
data = pd.read_csv("iris.csv")
df = data.groupby("species")

mean_sepalwidthspecies = df["sepalwidthcm"].mean()


print("\nMean Sepal Width(cm) by species:", mean_sepalwidthspecies)

with open("iris.txt", "a") as f:
   data = f.write('\n\nMean Sepal width by species (cm):'+str(mean_sepalwidthspecies))
  






