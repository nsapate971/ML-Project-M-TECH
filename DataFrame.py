# dataframe
import numpy
import pandas
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

#Import the CSV data file
def Read_Bands():
    url = pd.read_csv("E:/mean_180319.csv")
    #Importing the Sensitive bands for analysis of crop health
    print ("Following values are the Wavelength values which represent sensitive bands for the observation and analysis of crops \n")
    print (url.loc [[490,630,750], : ])
def Plot_Bands():
    url = pd.read_csv("E:/mean_180319.csv")
    plt.plot(url.Wavelength, url.Reflectance)
    plt.show()
