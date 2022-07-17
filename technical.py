import matplotlib.pyplot as plt
import numpy as np
import talib as tb 
import yfinance as yf
import datetime


#--------------------functions----------------------------------------------------------------

# moving avergae

def company_data(company_name):
    data  = yf.Ticker(company_name)
    date_now = datetime.date.today()
    data_raw = data.history(end= date_now,start= (date_now - datetime.timedelta(100)))
    moving_average = tb.SMA(data_raw["Close"],20)
    ma = moving_average.dropna()
    fig,axes = plt.subplots(1,1)
    axes.plot(ma)



    
    




# data = company_data("RELIANCE.NS")
# print(tb.SMA(data['Close'],5))  # set moving-average timeframe here 
# please enter minimum of the timeframe limit or the system will return Nan

