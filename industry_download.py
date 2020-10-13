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
dow_list = si.tickers_dow()

# %%

### Getting data on stock industry
industry_all = {}
for akcie in dow_list:
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
df_industry.transpose()

# %%

# merging industry data with the all_stock_dataframe

sp_500_file = os.path.join("output", "dow_allstock.csv")
df = pd.read_csv(dow_file)
