import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


iris = pd.read_csv("iris.csv")

iris_setosa=iris.loc[iris["species"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["species"]=="Iris-virginica"]
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")

iris_setosa=iris.loc[iris["species"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["species"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["species"]=="Iris-versicolor"]

sns.FacetGrid(iris,hue="species",size=3).map(sns.distplot,"petallengthcm").add_legend()
sns.FacetGrid(iris,hue="species",size=3).map(sns.distplot,"petalwidthcm").add_legend()
sns.FacetGrid(iris,hue="species",size=3).map(sns.distplot,"sepallengthcm").add_legend()
sns.FacetGrid(iris,hue="species",size=3).map(sns.distplot,"sepalwidthcm").add_legend()
plt.show()

#Petal Length:for the petal length histogram the iris-setosa is the only species clearly seperate
#the iris versicolor and virginica have a good bit of overlap
#Sepal length/width: Too much overlap between the values of the species for these values
#Petal Width: distribution isnt good.