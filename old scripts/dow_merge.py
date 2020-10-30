# %%

import pandas as pd
import os

# %%

# merging timeseries and industry data into final df

dow_file = os.path.join("output\dow\download", "dow_allstock.csv")
df_dow = pd.read_csv(dow_file)

dow_industries_file = os.path.join("output\dow\industries", "dow_industries.csv")
df_industries = pd.read_csv(dow_industries_file)

df_dow_final = df_dow.merge(df_industries, how = "left", left_on= "ticker", right_on="ticker")

#print(df_dow_final)
#df_dow_final.head()

# %%

# saving the extended dataframe to csv

df_dow_final.to_csv('temp\dow\dow_final.csv', mode='w', header=True, index = False)

# %%