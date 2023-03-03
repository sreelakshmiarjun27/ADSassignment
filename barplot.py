# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt


def population():
       data = pd.read_csv("population bar graph.csv")
       print(data)
       X = list(data.iloc[:, 0])
       Y = list(data.iloc[:, 1])
       plt.bar(X,Y,color ='r')
       plt.xticks(rotation=90)
       plt.title("Population 2016")
       plt.xlabel("Countries")
       plt.ylabel("Total Population")
       plt.savefig("population.png")
       plt.show()
       return        

population()        
        
        
  

    


