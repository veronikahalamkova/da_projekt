# %%

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import time
import datetime

# %%

### choosing the index for data smoothing

index_choice = 'dow'

# %%

### loading the time series dataframe

file_path = os.path.join("temp",f"{index_choice}",f"{index_choice}_final.csv")
final_df = pd.read_csv(file_path)
final_df["datetime"] = final_df["date"].apply(lambda s: datetime.datetime.strptime(s, "%Y-%m-%d"))


# %%

### % change in open stock price & moving average

final_df["change_open"]= (final_df.groupby("ticker")["open_x"].apply(pd.Series.pct_change))

window_size= 7
final_df["weekly_rolling_avg_open"]= final_df.groupby("ticker").rolling(window=window_size, min_periods= 1)['change_open'].mean().reset_index(drop=True)

window_size= 30
final_df["monthly_rolling_avg_open"]= final_df.groupby("ticker").rolling(window=window_size, min_periods= 1)['change_open'].mean().reset_index(drop=True)

# %%

window_size= 7
final_df["weekly_rolling_avg_open"]= final_df.groupby("ticker").rolling(window=window_size, min_periods= 1)['change_open'].mean().reset_index(drop=True)


# %%

### saving stock price data after smoothing

final_df.to_csv(f'temp\{index_choice}\{index_choice}_final_smoothed.csv', mode='w', header=True, index = False)


# %%
final_df.tail(10)
# %%
