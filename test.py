import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("iris.csv")

sum_sepallength = data["sepallengthcm"].sum()
mean_sepallength = data["sepallengthcm"].mean()
median_sepallength = data["sepallengthcm"].median()

print("Sepal Length Sum(cm):",sum_sepallength, "\nMean Sepal Length(cm):", mean_sepallength, "\nMedian Sepal Length(cm):", median_sepallength)

