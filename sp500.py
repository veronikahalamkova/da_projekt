
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
sp500_list = si.tickers_sp500()
#print(sp500_list)
len(sp500_list)

# %%

### getting data from Yahoo Finance

all_stock_dict = {}
#all_stock_dict['sp500']= 'hello world'
for stock in sp500_list:
    try:
      stock_daily = get_data(stock, start_date="01/01/2019", end_date="10/01/2020", index_as_date = True, interval="1d")
      all_stock_dict[stock]=stock_daily
    except Exception as e:
        print (repr(e))
    else:
        print (stock_daily)


print (all_stock_dict)

# %%
### exporting to CSVs
for stock_key, stock_value in all_stock_dict.items():
  date_range = f"{str(stock_value.index[0])[:-9]}_{str(stock_value.index[-1])[:-9]}"
  filename = f"{stock_key}_{date_range}.csv"
  full_filename = os.path.join ('output\sp500', filename)
  print(full_filename)
  stock_value.to_csv(full_filename, index=True)

# %%

### reading one csv at a time

amzn = pd.read_csv(r'C:\Users\veron\DA\da_projekt\output\sp500\AMZN_2019-01-02_2020-09-30.csv')

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

path = r'C:\Users\veron\DA\da_projekt\output\sp500' 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

sp500_frame = pd.concat(li, axis=0, ignore_index=True)

#sp500_frame.head()
#len(sp500_frame)
# %%

# rename first column in df

def rename(col):
    if col.startswith("Unnamed: "):
        return "date"
    else:
        return col

sp500_frame.columns = [rename(col) for col in sp500_frame.columns]

sp500_frame.head()
#%%
sp500_frame.info()
# %%
