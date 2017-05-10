# -*- coding: utf-8 -*-
"""

Created on Wed May 10 11:46:19 2016

@author: gnaveen
Simple Linear Regression using sklearn

"""

import pandas as pd
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    
    #Reading the data set
    collection = pd.read_csv("linear_data.csv")
    data = collection.loc[:,['x','y']]
    x_values = data['x']
    y_values = data['y']
    
    #Linear Regression usin sklearn
    clf  = LinearRegression()
    array_x = np.array(x_values)
    array_y = np.array(y_values)
    x_reshaped = array_x.reshape(-1,1)
    y_reshaped = array_y.reshape(-1,1)
    linear  = clf.fit(x_reshaped, y_reshaped)
    
    #print coefficient and intercept
    print ("coefficient:",linear.coef_)
    print ("intercept:",linear.intercept_)
    #print ("prediction=", clf.predict(3))
    
    #print score
    print("score:",linear.score(x_reshaped, y_reshaped))
    
    #@print (clf.score(X_test,Y_test))
    #scr = clf.score(array_x, array_y)
    #print("scr=", scr)'''
    
    #sample prediction for input 4.5
    print("samp_pred:", linear.predict(4.5))
    
    #ploting predictions and y_values
    predictions = []
    for x in x_values:
        predictions.append((linear.predict(x)).item())
        #print((linear.predict(x)).item())
    
    print("predictions=", predictions)
        
    pyplot.plot(y_values, predictions)
    pyplot.show()

main()