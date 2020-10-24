# %%

###importing stuff

import pandas as pd
import os

# %%

### defining stock index

index_choice = 'nasdaq'

# %%

# merging timeseries and industry data into final df

stock_file = os.path.join(f"output\{index_choice}\data_series", f"{index_choice}_allstock.csv")
df_stock = pd.read_csv(stock_file)

stock_industries_file = os.path.join(f"output\{index_choice}\industries", f"{index_choice}_industries.csv")
df_industries = pd.read_csv(stock_industries_file)

df_stock_final = df_stock.merge(df_industries, how = "left", left_on= "ticker", right_on="ticker")

# %%

#print(df_sp500_final)
df_stock_final.tail()

# %%

# saving the extended dataframe to csv

df_stock_final.to_csv(f'temp\{index_choice}\{index_choice}_final.csv', mode='w', header=True, index = False)

