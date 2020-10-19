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
for akcie in stock_list:
    try:
        Firma = yf.Ticker(akcie)
        industry_all [akcie] = Firma.info
    except Exception as e:
        industry= "N/A"

# print(industry_all)

#%%

print(industry_all)

# %%

# converting dictionary into dataframe

df_industry = pd.DataFrame.from_dict(industry_all)
df_industry = df_industry.transpose()
df_industry.index.name = "ticker"
#print(df_industry)

# %%

# merging industry data with the all_stock_dataframe

dow_file = os.path.join("output\dow", "dow_allstock.csv")
df_dow = pd.read_csv(dow_file)
df_dow=df_dow.merge(df_industry, left_on= "ticker", right_on="ticker")
print(df_dow)

# %%

# saving the extended dataframe (overwriting the original one)

df_dow.to_csv('output\dow\dow_allstock.csv', mode='w', header=True)

# %%
