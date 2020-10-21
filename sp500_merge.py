# %%

import pandas as pd
import os

# %%

# merging timeseries and industry data into final df

sp500_file = os.path.join("output\sp500\download", "sp500_allstock.csv")
df_sp500 = pd.read_csv(sp500_file)

sp500_industries_file = os.path.join("output\sp500\industries", "sp500_industries.csv")
df_industries = pd.read_csv(sp500_industries_file)

df_sp500_final = df_sp500.merge(df_industries, how = "left", left_on= "ticker", right_on="ticker")

# %%

#print(df_sp500_final)
df_sp500_final.tail()

# %%

# saving the extended dataframe to csv

df_sp500_final.to_csv('temp\sp500\sp500_final.csv', mode='w', header=True, index = False)

# %%