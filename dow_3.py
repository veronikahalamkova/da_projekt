# %%

#importing stuff
import yahoo_fin
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import pandas
import yfinance as yf
import traceback
import numpy as np
pandas.set_option('display.max_rows', 10000)
dow_list = si.tickers_dow()

# %%

#getting data from Yahoo Finance
all_stock = []
for akcie in dow_list:
    akcie_daily = get_data(akcie, start_date="01/01/2019", end_date="10/01/2020", index_as_date = True, interval="1d")
    all_stock.append(akcie_daily)
    print (all_stock)

# %%

#Converting data into dictionary format
all_stock_dict=[]
for i in range (len(dow_list)):
    all_stock_dict.append(all_stock[i].to_dict())
    i +=1
#print (all_stock_dict)
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
