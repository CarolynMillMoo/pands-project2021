import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("Iris.csv")
   
print (data.head(10))

iris = pd.read_csv("Iris.csv")
iris.groupby('species')
 
#plt.plot(iris.IDNumber, iris["sepallengthcm"], "r--")
#plt.show()

iris.plot(kind ="scatter",
          x ='sepallengthcm',
          y ='petallengthcm', color = "red")
plt.show()