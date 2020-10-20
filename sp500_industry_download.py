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
stock_list = si.tickers_sp500()

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

sp500_file = os.path.join("output\sp500", "sp500_allstock.csv")
df_sp500 = pd.read_csv(sp500_file)
df_sp500=df_sp500.merge(df_industry, left_on= "ticker", right_on="ticker")
print(df_sp500)

# %%

# saving the extended dataframe (overwriting the original one)

df_sp500.to_csv('output\sp500\sp500_allstock.csv', mode='w', header=True)

# %%
df_sp500.info()