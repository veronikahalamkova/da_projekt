# %%
import pandas as pd
#%%
covid_data = pd.read_csv('world_covid_data.csv', skiprows = 1, header = None)  
# %%
covid_data

# %%
type(covid_data)
# %%
