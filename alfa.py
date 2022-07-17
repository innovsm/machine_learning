# all the functions in this module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import talib as tb  
import yfinance as yf

# -----------------------  all functions ------------------------------------
def stock_check(company_name):    # daily 

    data_raw = yf.download(tickers=company_name,period = "400d" , interval = "1d")
    '''
    moving_average_20 = tb.EMA(data_raw["Close"],20)
    moving_average_50 = tb.EMA(data_raw["Close"],50)
    
    ma_50 = moving_average_50.dropna()
    ma_20 = moving_average_20.dropna()
    '''
    macd,macdsignal,macdhist = tb.MACD(data_raw["Close"].dropna())
    print(macd)
    



    df = pd.DataFrame({"macd": macd.dropna(), "macdsignal":macdsignal.dropna()})
    df["boolean"] = df["macd"]>df["macdsignal"]
    data_1 = list(df["macd"].tail(10))
    data_2 = list(df["macdsignal"].tail(10))
    data_3 = list(df["boolean"].tail(10))
    data = list(zip(data_1,data_2,data_3))
    #print(data)

   # moving_average = ma_check(ma_20,ma_50)   #moving average check


    # checking the stock
    x = data_3
    #print(data_3)
    if((x[9]> x[8])):
        
        print("possible uptrend")
        #enter_data(company_name)
        

        
    elif(x[9]<x[8]):
        print("possible downtrend")
    
    elif(x[9] == x[8]):

        data_1 = x[7]
        data_2 = x[8]
        data_3 = x[9]
        series_1 = pd.Series([data_1, data_2,data_3])  #main_series
        # sampler series
        series_2 = pd.Series([True, False, False]) #downtrend
        Series_3 = pd.Series([False,False, False]) #strong_downtrend
        series_4 = pd.Series([False,True, True])  #uptrend
        series_5 = pd.Series([True,True, True]) #strong_uptrend
        if((pd.Series(series_1 == series_4).all() == True) or (pd.Series(series_1 == series_5).all() == True)):
            if((pd.Series(series_1 == series_4).all() == True) ):
                print("Uptrend")
               # enter_data(company_name)
        else:

            print("downtrend")


#_----------------------- function 2 ----------------------------------



# main checker function for macd overlap for uptrend
# later adx\dms function will be added

def stock_check_weekly(dataset):    # weekly

    
    '''
    moving_average_20 = tb.EMA(data_raw["Close"],20)
    moving_average_50 = tb.EMA(data_raw["Close"],50)
    
    ma_50 = moving_average_50.dropna()
    ma_20 = moving_average_20.dropna()
    '''
    macd,macdsignal,macdhist = tb.MACD(dataset["Close"].dropna())
    print(macd)
    



    df = pd.DataFrame({"macd": macd.dropna(), "macdsignal":macdsignal.dropna()})
    df["boolean"] = df["macd"]>df["macdsignal"]
    data_1 = list(df["macd"].tail(10))
    data_2 = list(df["macdsignal"].tail(10))
    data_3 = list(df["boolean"].tail(10))
    data = list(zip(data_1,data_2,data_3))
    #print(data)

   # moving_average = ma_check(ma_20,ma_50)   #moving average check


    # checking the stock
    x = data_3
    #print(data_3)
    if((x[9]> x[8])):
        
        print("possible uptrend")
       # enter_data(company_name)
        

        
    elif(x[9]<x[8]):
        print("possible downtrend")
    
    elif(x[9] == x[8]):

        data_1 = x[7]
        data_2 = x[8]
        data_3 = x[9]
        series_1 = pd.Series([data_1, data_2,data_3])  #main_series
        # sampler series
        series_2 = pd.Series([True, False, False]) #downtrend
        Series_3 = pd.Series([False,False, False]) #strong_downtrend
        series_4 = pd.Series([False,True, True])  #uptrend
        series_5 = pd.Series([True,True, True]) #strong_uptrend
        if((pd.Series(series_1 == series_4).all() == True) or (pd.Series(series_1 == series_5).all() == True)):
            if((pd.Series(series_1 == series_4).all() == True) ):
                print("Uptrend")
               # enter(company_name)
        else:

            print("downtrend")

#-------------------------------------------------------

    

    

    

