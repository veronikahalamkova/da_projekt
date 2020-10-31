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
pd.set_option('display.max_rows', 10000)
stock_list = si.tickers_dow()

# %%

### Getting data on stock industry
industry_all = {}
for stock in stock_list:
    try:
        company = yf.Ticker(stock)
        industry_all [stock] = company.info
    except Exception as e:
        industry= "N/A"

# print(industry_all)


# %%

for stock in industry_all:
    print(stock)
    print(len(industry_all[stock]))

# %%

# converting dictionary into dataframe

df_industry = pd.DataFrame.from_dict(industry_all)
df_industry = df_industry.transpose()
df_industry.index.name = "ticker"
#print(df_industry)
#df_industry.info()
#df_industry.head()

# %%
df_industry.to_csv('output\dow\industries\dow_industries.csv', index = True)

# %%
