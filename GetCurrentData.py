import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
yf.pdr_override()
files = []

today = str(dt.date.today())
before = str(dt.date.today() - pd.offsets.DateOffset(months=9)).split(" ")[0]
#print(today)
#print(before)

ticker_list = ['AAPL','GOOGL','FB','AMZN','MSFT','SSNLF','INTC','WMT']
#Apple, Google, Facebook, Amazon, Microsoft, Samsung, Intel, Wallmart

def getData(ticker):
	print(ticker)
	data = pdr.get_data_yahoo(ticker,start=before,end=today)	
	files.append(ticker)
	saveData(data, ticker)

def saveData(df, filename):
	df.to_csv('data/' + filename + '.csv')

for tik in ticker_list:
	getData(tik)