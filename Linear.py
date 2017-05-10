# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 17:18:32 2016

@author: gnaveen
Simple Linear Regression Without Using sklearn
"""
import math
import csv
import pandas as pd
from matplotlib import pyplot

def mean(values):
    return sum(values)/len(values)
    
def variance(values):
    sum = 0;
    for i in values:
        #print(i)
        #print (mean(values))
        #print (pow((i - mean(values)),2))
        sum = sum + (pow((i - mean(values)),2))
        #print(sum)
    #print (sum)
    return sum
    
    
def convariance(xvalues,yvalues):
    sum = 0;
    for i in range(len(xvalues)):
        #print(i)
        #print (mean(xvalues))
        #print ((xvalues[i] - mean(xvalues))*
        #       (yvalues[i] - mean(yvalues)))
        sum = sum + ((xvalues[i] - mean(xvalues))*
               (yvalues[i] - mean(yvalues)))
        #print(sum)
    #print (sum)
    return sum
    
   
def main():   
    #Reading the data set
    collection = pd.read_csv("linear_data.csv")
    print ("collection=", collection)
    data = collection.loc[:,['x','y']]
    print("data=", data)
    x_values = data['x']
    #with index
    print("x_values", x_values)
    #without index
    print (x_values.to_string(index=False))
    #mean of x
    print("mean=" , mean(x_values))
    #variance of x
    print ("var=", variance(x_values))
    #y values
    y_values = data['y']
    print ("y_values", y_values)
    print ("mean=", mean(y_values))
    print ("var=", variance(y_values))
    print ("covariance", convariance(x_values,y_values))
    m = convariance(x_values,y_values)/variance(x_values)
    c = mean(x_values ) - m * mean(y_values)
    #slope value
    print("m=", m)
    #intercept
    print("c=", c)
    out = []
    for i in x_values:
        out.append (m*i + c) 
        print(m*i + c)  
    print("predictions=", out)
    #ploting predictions
    pyplot.plot(y_values, out)
    pyplot.show()
    
main()