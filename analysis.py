#This program will be used to analyse the
#Iris Dataset
#Author: Carolyn Moorhouse

import pandas as pd
data = pd.read_csv("iris.csv")

#the function head() will display the top rows of the dataset "iris.csv"
#the default value of this function is 5
#so it will show the top 5 rows when no argument is given

data.head()
print(data.head())

data.sample(10)

data.columns
print(data.columns)

data.shape
print(data.shape)

print(data)