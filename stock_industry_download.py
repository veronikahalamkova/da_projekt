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
pd.set_option('display.max_rows', 10000)

# %%
# defining stock index and importing stocks

index_choice = 'nasdaq'
stock_list = si.tickers_nasdaq()
#print (stock_list)

# %%

### importing industry info about each stock

industry_all = {}
for stock in stock_list:
    try:
        Firma = yf.Ticker(stock)
        industry_all[stock]=Firma.info
    except Exception as e:
        print (repr(e))
    else: 
        print(Firma.info)


# %%

### converting dictionary into dataframe

df_industry = pd.DataFrame.from_dict(industry_all)
df_industry = df_industry.transpose()
df_industry.index.name = "ticker"
#print(df_industry)

# %%

### saving industry info into a seperate file

df_industry.to_csv(f'output\{index_choice}\industries\{index_choice}_industries.csv', index = True)


# %%
