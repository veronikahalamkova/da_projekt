# %%

#importing stuff
import yahoo_fin
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import pandas as pd
import yfinance as yf
import traceback
import numpy as np
import os

# %%
pandas.set_option('display.max_rows', 10000)
dow_list = si.tickers_dow()

# %%

#getting data from Yahoo Finance

all_stock_dict = {}
#all_stock_dict['dow']= 'hello world'
for akcie in dow_list:
    akcie_daily = get_data(akcie, start_date="01/01/2019", end_date="10/01/2020", index_as_date = True, interval="1d")
    all_stock_dict[akcie]=akcie_daily

print (all_stock_dict)

# %%
for nazev_akcie, hodnota_akcie in all_stock_dict.items():
  date_range = f"{str(hodnota_akcie.index[0])[:-9]}_{str(hodnota_akcie.index[-1])[:-9]}"
  filename = f"{nazev_akcie}_{date_range}.csv"
  full_filename = os.path.join ('output', filename)
  print(full_filename)
  hodnota_akcie.to_csv(full_filename, index=True)

# %%
pokus = pd.read_csv(r'C:\Users\veron\DA\da_projekt\output\AAPL_2019-01-02_2020-09-30.csv')
pokus.head()

# %%
all_stock_dict = {}
all_stock_dict['dow']= 'hello world'

# %%
print(dow_list)
# %%

#Converting data into dictionary format
all_stock_dict=[]
for i in range (len(dow_list)):
    all_stock_dict.append(all_stock[i].to_dict())
    i +=1
#print(all_stock_dict)
#print(all_stock_dict[1])
#print(all_stock_dict[1].values())
#print(all_stock_dict[1].keys())
#print(all_stock_dict[1].items())

# %%

# Getting data on stock industry
industry_all = []
i = 0
for akcie in dow_list:
    try:
        Firma = yf.Ticker(akcie)
        industry = Firma.info["sector"]
    except Exception as e:
        industry= "N/A"
    finally: 
        industry_all.append(industry)
        i +=1
print(industry_all)
print(len(industry_all))

# %%

# Appending industry to stock data
for i in range (len(dow_list)):
    all_stock_dict[i] ["Ind"] = industry_all[i]

#pandas.DataFrame.from_dict(all_stock_dict[1])

# %%

# Getting the dateframe of the stock dataset
dateframe_all= []
for i in range (len(dow_list)):
    dateframe= f"{str(all_stock[i].index[0])[:-9]}_{str(all_stock[i].index[-1])[:-9]}"
    dateframe_all.append(dateframe)
    i +=1
print (dateframe_all)

# %%

# Creating individual dictionary files for each stock 
for i in range (len(dow_list)):
    np.save (f"{dow_list[i]}_{dateframe_all[i]}.npy", all_stock_dict[i])

#read_dictionary = np.load ('AXP.npy',allow_pickle='TRUE').item()
#print (read_dictionary)

# %%

