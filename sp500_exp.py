# %%
import pandas as pd
import traceback
import numpy as np
import os
import glob

df = pd.read_csv('output\sp500_allstock.csv')


# %%
df.info()