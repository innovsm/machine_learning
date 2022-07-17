import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast

################################
# this module will hold all the functions and classes related to plotting

#---------------- to get the data --------------------

def read_data(company_name):
    data_1 = open(company_name+".txt",'r')
    dict_1 = {}
    for data in data_1:
        dict_1 = ast.literal_eval(data)
    return dict_1


#------------ to compare different data-points between different companies

data_points = ['Total common shares outstanding', 'Float shares outstanding',
#--------------- [0 - 1] -------------
 'Number of employees', 'Number of shareholders', 
#---------------- [2,3] ---------------------
'Price to earnings ratio', 'Price to sales ratio', 
# ------------------ [4,5] -------------------------------
'Price to cash flow ratio', 'Price to book ratio', 'Enterprise value',
#------------------[6,7,8] -----------------------------------
 'Enterprise value to EBITDA ratio', 'Return on assets %', 'Return on equity %',
# -----------------------[9,10] --------------------------------
 'Return on invested capital %', 'Gross margin %', 
# -----------------------[11,12,13,14,15] -----------------------
'Operating margin %', 'EBITDA margin %', 'Net margin %', 'Quick ratio', 'Current ratio',
# -----------------------[16,17,18] ---------------------------
 'Inventory turnover', 'Asset turnover', 'Debt to assets ratio',
#------------------------ [19,20] --------------------------------
 'Debt to equity ratio', 'Long term debt to total assets ratio']

# ------------------- helper function---------------------
def helpme():
    counter = 0
    print("enter the following  command \n")
    for data in data_points:
    
        print("["+data+"]"+"----->> "+ str(counter)+"\n")
        counter += 1


# ------------------------ compare function -------------------

#simple plottng function 
def plot_data(point,company_data):

    fig =plt.figure()
    fig,axes = plt.subplots(1,1)
    axes.plot(company_data[data_points[point]])
    return axes


#------------live test data --------------------
