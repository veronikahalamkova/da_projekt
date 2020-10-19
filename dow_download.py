# %%

###importing stuff
import yahoo_fin
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import pandas as pd
import yfinance as yf
import traceback
import numpy as np
import os
import glob

# %%
pd.set_option('display.max_rows', 10000)
stock_list = si.tickers_dow()
#print(stock_list)
len(stock_list)

# %%

### getting data from Yahoo Finance

all_stock_dict = {}
#all_stock_dict['sp500']= 'hello world'
for stock in stock_list:
    try:
      stock_daily = get_data(stock, start_date="01/01/2019", end_date="10/01/2020", index_as_date = True, interval="1d")
      all_stock_dict[stock]=stock_daily
    except Exception as e:
        print (repr(e))
    else:
        print (stock_daily)


print (all_stock_dict)

# %%

for stock in all_stock_dict:
    print(stock)
    print(len(all_stock_dict[stock]))


# %%

### exporting to CSVs

for stock_key, stock_value in all_stock_dict.items():
  date_range = f"{str(stock_value.index[0])[:-9]}_{str(stock_value.index[-1])[:-9]}"
  filename = f"{stock_key}_{date_range}.csv"
  full_filename = os.path.join ('output\dow', filename)
  print(full_filename)
  stock_value.to_csv(full_filename, index=True)

# %%

### reading one csv at a time

amzn = pd.read_csv(r'output\AMZN_2019-01-02_2020-09-30.csv')

def rename(col):
    if col.startswith("Unnamed: "):
        return "date"
    else:
        return col

amzn.columns = [rename(col) for col in amzn.columns]
#amzn.head()
#amzn.info()

# %%

### merging all stock CSVs into one dataframe

path = r'output\dow' 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

stock_frame = pd.concat(li, axis=0, ignore_index=True)


# %%

len(stock_frame)

# %%

len(stock_frame["ticker"].unique())

stock_frame.groupby(["ticker"]).size()

# %%

#stock_frame[stock_frame.ticker=="AAPL"].date

stock_daily = get_data("AAPL", start_date="01/01/2019", end_date="10/01/2020", index_as_date = False, interval="1d")
print (len(stock_daily))
stock_daily.date

# %%

# rename first column in df

def rename(col):
    if col.startswith("Unnamed: "):
        return "date"
    else:
        return col

stock_frame.columns = [rename(col) for col in stock_frame.columns]

stock_frame.head()

# %%
stock_frame.to_csv('output\dow\dow_allstock.csv', index = False)
#%%
stock_frame.info()
# %%

