#This program will be used to analyse the
#Iris Dataset
#Author: Carolyn Moorhouse

import pandas as pd
data = pd.read_csv("iris.csv")

numericaldata = data[["sepallengthcm", "sepalwidthcm", "petallengthcm", "petalwidthcm"]]
#print(numericaldata)
data.iloc[5]

data.loc[data["species"] == "Iris-setosa"]
print(data.loc)
