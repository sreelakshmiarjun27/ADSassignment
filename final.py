# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 00:22:39 2023

@author: sreelakshmi
"""
import pandas as pd
import matplotlib.pyplot as plt


def population():
    """
    This function plots the total population for age 15-64 of different countries in the year 2016
    """
    data = pd.read_csv("population bar graph.csv")
    #to select specific row or column from dataset
    X = list(data.iloc[:, 0])
    #to select specific row or column from dataset
    Y = list(data.iloc[:, 1])
    plt.figure()
    #plot bar graph
    plt.bar(X, Y, color='r')
    #to Rotate the data on x-axis by 90
    plt.xticks(rotation=90)
    #Add title
    plt.title("Population 2016")
    #Add label for horizontal axis
    plt.xlabel("Countries")
    #Add label for vertical axis
    plt.ylabel("Total Population")
    #to save figure
    plt.savefig("population.png")
    #show the plot
    plt.show()
    return


def education():
    """
    This function plots the male and female employment in the world for different years
    """
    plt.figure()
    edu1 = pd.read_csv('line graph.csv')
    #to select specific row or column from dataset
    X = list(edu1.iloc[:, 0])
    Y = list(edu1.iloc[:, 1])
    plt.plot(X, Y, color='blue', label="Primary completion rate, female")
    edu2 = pd.read_csv("line2.csv")
    #to select specific row or column from dataset
    X = list(edu2.iloc[:, 0])
    Y = list(edu2.iloc[:, 1])
    #plot line graph
    plt.plot(X, Y, color='green', label="Primary completion rate, male")
    #Add legend
    plt.legend()
    #Add title
    plt.title("Education male and female")
    #Add label for Horizontal axis
    plt.xlabel("Year")
    #Add label for Vertical axis
    plt.ylabel("Education")
    #to save figure
    plt.savefig("education.png")
    #Show the plot
    plt.show()
    return


def unemployment():
    """
    This function analyse the median, maximum, minimum umemployment of Afghanistan for different years
    """
    data1 = pd.read_csv("box.csv")
    plt.figure()
    #to get box plot
    plt.boxplot(data1['Unemployment'], labels=['Afghanistan'])
    #Add title
    plt.title("Unemployment")
    #to save figure
    plt.savefig("unemployment.png")
    #Show the plot
    plt.show()
    return


#calling function to visualise line plot
population()

#calling function to visualise bar plot
education()

#calling function to visualise box plot
unemployment()
