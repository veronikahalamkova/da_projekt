# %%
import pandas as pd

#%%
# read in covid dataset without header
covid_data = pd.read_csv('world_covid_data.csv', skiprows = 1, header = None)  

# %%
covid_data

# %%
type(covid_data)

# %%
covid_data.head()

# %%
# remove dates after 30/09/2020
covid_data_edit = covid_data[covid_data[3] != '01/10/2020']

covid_data_edit = covid_data_edit[covid_data_edit[3] != '02/10/2020']

covid_data_edit = covid_data_edit[covid_data_edit[3] != '03/10/2020']

covid_data_edit = covid_data_edit[covid_data_edit[3] != '04/10/2020']

# %%
covid_data_edit

# %%
