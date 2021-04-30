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

#the following calculates the mean of the sepal width, sepal length, petal width and petal length
#specific to each species. This mean info helps us to see the differences in mean length and widths and thus makes
#it easier to perhaps roughly identify the species.
#and also appends this information to the iris txt file
data = pd.read_csv("iris.csv")
df = data.groupby("species")

mean_sepalwidthspecies = df["sepalwidthcm"].mean()
mean_sepallengthspecies = df["sepallengthcm"].mean()
mean_petalwidthspecies = df["petalwidthcm"].mean()
mean_petallengthspecies = df["petallengthcm"].mean()


print("\n\nMean Sepal Width(cm) by species:", mean_sepalwidthspecies, "\n\nMean Sepal Length(cm) by species: ", mean_sepallengthspecies, "\n\nMean Petal Width (cm) by species: ", mean_petalwidthspecies, "\n\nMean Petal Length (cm) by species: ", mean_petallengthspecies)

with open("iris.txt", "a") as f:
   data = f.write('\n\nMean Sepal width by species (cm):'+str(mean_sepalwidthspecies))
   data = f.write('\n\nMean Sepal length by species (cm):'+str(mean_sepallengthspecies))
   data = f.write('\n\nMean Petal width by species (cm): '+str(mean_petalwidthspecies))
   data = f.write('\n\nMean Petal length by species (cm):'+str(mean_petallengthspecies))

#the following calculates the median of the sepal width, sepal length, petal width and petal length
#specific to each species. This median info helps us to see the differences in median length and widths and thus makes
#it easier to perhaps roughly identify the species.
#and also appends this information to the iris txt file
data = pd.read_csv("iris.csv")
df = data.groupby("species")

median_sepalwidthspecies = df["sepalwidthcm"].median()
median_sepallengthspecies = df["sepallengthcm"].median()
median_petalwidthspecies = df["petalwidthcm"].median()
median_petallengthspecies = df["petallengthcm"].median()


print("\n\nMedian Sepal Width(cm) by species:", median_sepalwidthspecies, "\n\nMedian Sepal Length(cm) by species: ", median_sepallengthspecies, "\n\nMedian Petal Width (cm) by species: ", median_petalwidthspecies, "\n\nMedian Petal Length (cm) by species: ", median_petallengthspecies)

with open("iris.txt", "a") as f:
   data = f.write('\n\nMedian Sepal width by species (cm):'+str(median_sepalwidthspecies))
   data = f.write('\n\nMedian Sepal length by species (cm):'+str(median_sepallengthspecies))
   data = f.write('\n\nMedian Petal width by species (cm): '+str(median_petalwidthspecies))
   data = f.write('\n\nMedian Petal length by species (cm):'+str(median_petallengthspecies))

#the following calculates the sum of the total sepal width, sepal length, petal width and petal length
#specific to each species. The sums of these measurements may show if there are significant differences in lengths and widths 
#Not to be used as a tool to identify between species just for our own information,
#and also appends this information to the iris txt file
data = pd.read_csv("iris.csv")
df = data.groupby("species")

sum_sepalwidthspecies = df["sepalwidthcm"].sum()
sum_sepallengthspecies = df["sepallengthcm"].sum()
sum_petalwidthspecies = df["petalwidthcm"].sum()
sum_petallengthspecies = df["petallengthcm"].sum()


print("\n\nSum Sepal Width(cm) by species:", sum_sepalwidthspecies, "\n\nSum Sepal Length(cm) by species: ", sum_sepallengthspecies, "\n\nSum Petal Width (cm) by species: ", sum_petalwidthspecies, "\n\nSum Petal Length (cm) by species: ", sum_petallengthspecies)

with open("iris.txt", "a") as f:
   data = f.write('\n\nSum Sepal width by species (cm):'+str(sum_sepalwidthspecies))
   data = f.write('\n\nSum Sepal length by species (cm):'+str(sum_sepallengthspecies))
   data = f.write('\n\nSum Petal width by species (cm): '+str(sum_petalwidthspecies))
   data = f.write('\n\nSum Petal length by species (cm):'+str(sum_petallengthspecies))

#Results: There are some differences between the sums of these measurements in the species, interesting to note.mean_petallengthspecies









