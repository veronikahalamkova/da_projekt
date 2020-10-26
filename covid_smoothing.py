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

### loading the covid dataframe

covid_df = pd.read_csv("world_covid_data.csv",encoding="UTF8")
covid_df.head()

covid_df["datetime"] = covid_df["date"].apply(lambda s: datetime.datetime.strptime(s, "%d/%m/%Y"))

covid_usa = covid_df.loc[covid_df["iso_code"] == "USA"]
covid_usa.info()


# %%

### % change in covid new cases & moving average

covid_usa["change_new_cases"]= covid_usa["new_cases"].pct_change()

window_size= 7
covid_usa["rolling_avg_new_cases"]= covid_usa.rolling(window=window_size, min_periods= 1)["change_new_cases"].mean()

# %%


### saving stock price data after smoothing

covid_usa.to_csv('covid_usa_smoothed.csv', mode='w', header=True, index = False)


# %%
