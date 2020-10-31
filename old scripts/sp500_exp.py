# %%
import pandas as pd
import traceback
import numpy as np
import os
import glob


sp_500_file = os.path.join("output", "sp500_allstock.csv")
df = pd.read_csv(sp_500_file)


# %%
df.info()
# %%
