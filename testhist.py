import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

irisdata = pd.read_csv("iris.csv")
#Histogram to show the distribution of the data from the iris.csv dataset
fig, axes = plt.subplots(2, 2, figsize=(16,9))
axes[0,0].set_title("Distribution of Sepal Width")
axes[0,0].hist(irisdata['sepalwidthcm'], bins=5);
axes[0,1].set_title("Distribution of Sepal Length")
axes[0,1].hist(irisdata['sepallengthcm'], bins=7);
axes[1,0].set_title("Distribution of Petal Width")
axes[1,0].hist(irisdata['petalwidthcm'], bins=5);
axes[1,1].set_title("Distribution of Petal length")
axes[1,1].hist(irisdata['petallengthcm'], bins=6);

#plt.show()

#The following adds univariate analysis to the columns
sns.FacetGrid(irisdata,hue="species",height=5).map(sns.displot, "petalwidthcm").add_legend();
plt.show()
#again as we have seen in the scatterplots the setosa species stands out on its own measurement wise with no real crossover with the other two
#as we have seen previously there is a significant crossover between the versicolor and virginica

#sns.FacetGrid(irisdata,hue="species",height=5).map(sns.displot,"petallengthcm").add_legend();
#plt.show()
