# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:08:42 2023

@author: sreelakshmi
"""
import matplotlib.pyplot as plt
import pandas as pd
plt.figure()
data = pd.read_csv('box.csv')
plt.boxplot(data['Unemployment'],labels =['Afghanistan'])
plt.show()